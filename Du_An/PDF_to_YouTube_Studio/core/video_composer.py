"""
Video Composer Engine powered by FFmpeg
Assembles visual slide frames + speech audio into 16:9 and 9:16 MP4 video files.
Generates YouTube SEO optimization packages.
"""

import os
import subprocess
import time
from typing import List, Dict, Any, Callable, Optional
import imageio_ffmpeg

from .pdf_reader import PDFReader
from .voice_engine import VoiceEngine
from .slide_artist import SlideArtist

class VideoComposer:
    def __init__(self, workspace_dir: str):
        self.workspace_dir = os.path.abspath(workspace_dir)
        self.temp_dir = os.path.join(self.workspace_dir, "temp")
        self.output_dir = os.path.join(self.workspace_dir, "output")
        os.makedirs(self.temp_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

        self.ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        self.slide_artist = SlideArtist()

    def render_clip(self, image_path: str, audio_path: str, output_clip_path: str) -> bool:
        """Renders a single scene clip by pairing the slide frame with the spoken audio."""
        os.makedirs(os.path.dirname(os.path.abspath(output_clip_path)), exist_ok=True)
        cmd = [
            self.ffmpeg_exe, "-y",
            "-loop", "1",
            "-i", image_path,
            "-i", audio_path,
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "aac",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            output_clip_path
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return res.returncode == 0 and os.path.exists(output_clip_path)

    def concatenate_clips(self, clip_paths: List[str], final_mp4_path: str) -> bool:
        """Merges all scene clips into a single master MP4 video using the concat demuxer."""
        if not clip_paths:
            return False
        os.makedirs(os.path.dirname(os.path.abspath(final_mp4_path)), exist_ok=True)
        concat_txt = os.path.join(self.temp_dir, f"concat_{int(time.time())}.txt")
        
        with open(concat_txt, "w", encoding="utf-8") as f:
            for cp in clip_paths:
                f.write(f"file '{os.path.abspath(cp).replace('\\', '/')}'\n")

        cmd = [
            self.ffmpeg_exe, "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", concat_txt,
            "-c", "copy",
            final_mp4_path
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if os.path.exists(concat_txt):
            try:
                os.remove(concat_txt)
            except OSError:
                pass
        return res.returncode == 0 and os.path.exists(final_mp4_path)

    def process_audiobook(
        self,
        pdf_path: str,
        book_title: str,
        chapter_title: str,
        start_page: int,
        end_page: int,
        voice_gender: str = "male",
        voice_speed: str = "+0%",
        render_16_9: bool = True,
        render_9_16: bool = True,
        progress_callback: Optional[Callable[[int, str], None]] = None
    ) -> Dict[str, Any]:
        """
        End-to-end Audiobook video generator.
        Processes verbatim text, generates speech, renders frames, and outputs MP4s.
        """
        def update_progress(pct: int, msg: str):
            if progress_callback:
                progress_callback(pct, msg)
            print(f"[{pct}%] {msg}")

        update_progress(5, f"Đang trích xuất nguyên tác từ trang {start_page} đến {end_page}...")
        reader = PDFReader(pdf_path)
        pages_data = reader.extract_text_range(start_page=start_page, end_page=end_page)
        scenes = reader.chunk_into_audiobook_scenes(
            pages_content=pages_data,
            book_title=book_title,
            chapter_title=chapter_title,
            words_per_scene=35
        )
        total_scenes = len(scenes)
        if total_scenes == 0:
            raise ValueError("Không tìm thấy nội dung văn bản nào trong khoảng trang đã chọn.")

        update_progress(15, f"Khởi tạo giọng đọc AI ({voice_gender})...")
        voice = VoiceEngine(voice_gender=voice_gender, speed_rate=voice_speed)

        # 1. Synthesize audio
        audio_files = []
        for i, s in enumerate(scenes):
            pct = 15 + int((i / total_scenes) * 35) # 15% -> 50%
            update_progress(pct, f"Đang lồng tiếng phân đoạn {s['scene_index']}/{total_scenes}...")
            a_path = os.path.join(self.temp_dir, f"audio_{s['scene_index']:03d}.mp3")
            ok = voice.synthesize(s["text"], a_path)
            if not ok:
                raise RuntimeError(f"Lỗi khi tạo âm thanh cho phân đoạn {s['scene_index']}")
            audio_files.append(a_path)
            time.sleep(0.15)

        # 2. Render visual frames & video clips
        clips_16_9 = []
        clips_9_16 = []

        for i, (s, a_path) in enumerate(zip(scenes, audio_files)):
            pct = 50 + int((i / total_scenes) * 40) # 50% -> 90%
            update_progress(pct, f"Đang render phân cảnh video {s['scene_index']}/{total_scenes}...")

            if render_16_9:
                img_16 = os.path.join(self.temp_dir, f"frame_16_9_{s['scene_index']:03d}.png")
                clip_16 = os.path.join(self.temp_dir, f"clip_16_9_{s['scene_index']:03d}.mp4")
                self.slide_artist.render_landscape(s, img_16, total_scenes=total_scenes)
                self.render_clip(img_16, a_path, clip_16)
                clips_16_9.append(clip_16)

            if render_9_16:
                img_9 = os.path.join(self.temp_dir, f"frame_9_16_{s['scene_index']:03d}.png")
                clip_9 = os.path.join(self.temp_dir, f"clip_9_16_{s['scene_index']:03d}.mp4")
                self.slide_artist.render_portrait(s, img_9, total_scenes=total_scenes)
                self.render_clip(img_9, a_path, clip_9)
                clips_9_16.append(clip_9)

        # 3. Concatenate into Final Masters
        update_progress(92, "Đang ghép nối các phân cảnh thành Master Video...")
        safe_title = "".join(c for c in book_title if c.isalnum() or c in (" ", "_", "-")).strip().replace(" ", "_")
        
        final_16_9 = None
        final_9_16 = None

        if render_16_9 and clips_16_9:
            out_16 = os.path.join(self.output_dir, f"{safe_title}_16x9_Landscape.mp4")
            if self.concatenate_clips(clips_16_9, out_16):
                final_16_9 = out_16

        if render_9_16 and clips_9_16:
            out_9 = os.path.join(self.output_dir, f"{safe_title}_9x16_Shorts.mp4")
            if self.concatenate_clips(clips_9_16, out_9):
                final_9_16 = out_9

        # 4. Generate SEO Metadata Package
        update_progress(98, "Đang tạo gói SEO YouTube Studio...")
        meta_path = os.path.join(self.output_dir, f"{safe_title}_SEO_Metadata.txt")
        meta_content = self._build_seo_package(book_title, chapter_title, scenes)
        with open(meta_path, "w", encoding="utf-8") as f:
            f.write(meta_content)

        update_progress(100, "Hoàn tất trọn vẹn quy trình xuất bản!")
        return {
            "book_title": book_title,
            "chapter_title": chapter_title,
            "total_scenes": total_scenes,
            "video_16_9": final_16_9,
            "video_9_16": final_9_16,
            "metadata_path": meta_path
        }

    def _build_seo_package(self, title: str, chapter: str, scenes: List[Dict[str, Any]]) -> str:
        pts = "\n".join([f"• Phân đoạn {s['scene_index']}: {s['text'][:65]}..." for s in scenes[:6]])
        return f"""=====================================================================
GÓI NỘI DUNG YOUTUBE SEO (COPY TRỰC TIẾP LÊN YOUTUBE STUDIO)
=====================================================================

[1. TIÊU ĐỀ VIDEO CHÍNH (16:9)]:
{title} — {chapter} | Sách Nói Nguyên Tác & Phân Tích Triết Học

[2. TIÊU ĐỀ YOUTUBE SHORTS (9:16)]:
Nguyên Tắc Bất Biến Từ {title}! #shorts #sachnoi #triethoc

[3. NỘI DUNG MÔ TẢ (DESCRIPTION)]:
Chào mừng quý thính giả đến với kênh Sách Nói Tinh Hoa & Tri Thức Bất Biến.
Lắng nghe trọn vẹn chương sách: "{chapter}" trích từ tác phẩm kinh điển "{title}".

Các luận điểm cốt lõi trong video:
{pts}

📌 Tác quyền nội dung: Tác phẩm kinh điển thuộc Phạm vi Công cộng (Public Domain). Được sản xuất và biên tập với visual typography và giọng đọc truyền cảm nhằm mục đích giáo dục, bảo tồn và lan tỏa tri thức nhân loại.

🔔 Nhấn ĐĂNG KÝ (Subscribe) và Bật Chuông thông báo để không bỏ lỡ các tác phẩm kinh điển tiếp theo!

[4. THẺ TỪ KHÓA (TAGS)]:
sách nói, {title}, {chapter}, triết học, tư tưởng lớn, bài học lãnh đạo, sách kinh điển, audiobook tiếng việt
"""
