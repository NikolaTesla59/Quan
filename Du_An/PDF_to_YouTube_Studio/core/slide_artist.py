"""
Slide Artist: Typography & Storyboard Frame Generator
Renders 16:9 Full HD Landscape & 9:16 Vertical Shorts frames using Pillow and Windows TrueType Fonts.
"""

import os
from typing import Dict, Any, List
from PIL import Image, ImageDraw, ImageFont

class SlideArtist:
    def __init__(self):
        self.font_dir = r"C:\Windows\Fonts"
        self.font_title_path = self._pick_font(["timesbd.ttf", "segoeuib.ttf", "arialbd.ttf"])
        self.font_body_path = self._pick_font(["times.ttf", "segoeui.ttf", "arial.ttf"])
        self.font_sans_bold = self._pick_font(["segoeuib.ttf", "arialbd.ttf"])

    def _pick_font(self, candidates: List[str]) -> str:
        for name in candidates:
            p = os.path.join(self.font_dir, name)
            if os.path.exists(p):
                return p
        return "arial.ttf"

    def _wrap_text(self, text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> List[str]:
        words = text.split()
        lines = []
        cur_line = []
        for w in words:
            test = " ".join(cur_line + [w])
            bbox = draw.textbbox((0, 0), test, font=font)
            if (bbox[2] - bbox[0]) <= max_width:
                cur_line.append(w)
            else:
                if cur_line:
                    lines.append(" ".join(cur_line))
                    cur_line = [w]
                else:
                    lines.append(w)
                    cur_line = []
        if cur_line:
            lines.append(" ".join(cur_line))
        return lines

    def render_landscape(self, scene: Dict[str, Any], output_path: str, total_scenes: int = 1) -> str:
        """16:9 1920x1080 Full HD YouTube Video Slide."""
        W, H = 1920, 1080
        img = Image.new("RGB", (W, H), color=(10, 14, 23))
        draw = ImageDraw.Draw(img)

        # Ambient Glow
        for r in range(350, 0, -25):
            alpha = (14 + int((350 - r) * 0.05), 20 + int((350 - r) * 0.06), 36 + int((350 - r) * 0.09))
            draw.ellipse([W//2 - r*2, H//2 - r, W//2 + r*2, H//2 + r], fill=alpha)

        # Outer Royal Gold Border Frame
        m = 48
        draw.rectangle([(m, m), (W - m, H - m)], outline=(212, 175, 55), width=3)
        draw.rectangle([(m + 6, m + 6), (W - m - 6, H - m - 6)], outline=(55, 65, 81), width=1)

        # Header Info
        f_tag = ImageFont.truetype(self.font_sans_bold, 22)
        f_book = ImageFont.truetype(self.font_title_path, 36)
        f_chap = ImageFont.truetype(self.font_sans_bold, 25)

        draw.text((W // 2, 95), "AUDIOBOOK KINH ĐIỂN • NGUYÊN TÁC TRỌN VẸN", font=f_tag, fill=(212, 175, 55), anchor="mm")
        draw.text((W // 2, 145), scene.get("book_title", "TỦ SÁCH KINH ĐIỂN").upper(), font=f_book, fill=(255, 255, 255), anchor="mm")
        draw.text((W // 2, 195), f"— {scene.get('chapter_title', 'Trích Đoạn')} —", font=f_chap, fill=(156, 163, 175), anchor="mm")
        draw.line([(W//2 - 200, 225), (W//2 + 200, 225)], fill=(212, 175, 55), width=2)

        # Main Body Text
        f_body = ImageFont.truetype(self.font_body_path, 44)
        max_w = 1520
        lines = self._wrap_text(scene["text"], f_body, max_w, draw)
        line_h = 66
        total_h = len(lines) * line_h
        start_y = (H // 2) - (total_h // 2) + 35

        # Decorative Quotes
        f_q = ImageFont.truetype(self.font_title_path, 110)
        draw.text((150, start_y - 60), "“", font=f_q, fill=(212, 175, 55))

        for i, l in enumerate(lines):
            draw.text((W // 2, start_y + (i * line_h)), l, font=f_body, fill=(243, 244, 246), anchor="mm")

        # Footer Progress Bar & Metadata
        curr = scene.get("scene_index", 1)
        ratio = curr / max(1, total_scenes)
        bar_w = 640
        bx = (W - bar_w) // 2
        by = H - 105
        draw.rectangle([(bx, by), (bx + bar_w, by + 6)], fill=(55, 65, 81))
        draw.rectangle([(bx, by), (bx + int(bar_w * ratio), by + 6)], fill=(212, 175, 55))

        f_foot = ImageFont.truetype(self.font_sans_bold, 19)
        draw.text((W // 2, H - 70), f"PHẦN {curr:02d} / {total_scenes:02d}  •  TỰ ĐỘNG XUẤT BẢN BỞI YOUTUBE STUDIO AI", font=f_foot, fill=(107, 114, 128), anchor="mm")

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        img.save(output_path, quality=95)
        return output_path

    def render_portrait(self, scene: Dict[str, Any], output_path: str, total_scenes: int = 1) -> str:
        """9:16 1080x1920 YouTube Shorts / TikTok Frame."""
        W, H = 1080, 1920
        img = Image.new("RGB", (W, H), color=(10, 12, 20))
        draw = ImageDraw.Draw(img)

        # Neon Accent Frame
        m = 36
        draw.rectangle([(m, m), (W - m, H - m)], outline=(234, 179, 8), width=4)

        # Top Hook Header
        f_tag = ImageFont.truetype(self.font_sans_bold, 28)
        f_book = ImageFont.truetype(self.font_title_path, 42)
        f_chap = ImageFont.truetype(self.font_sans_bold, 30)

        draw.rectangle([(W//2 - 200, 130), (W//2 + 200, 185)], fill=(234, 179, 8))
        draw.text((W // 2, 157), "BÀI HỌC KINH ĐIỂN", font=f_tag, fill=(0, 0, 0), anchor="mm")

        draw.text((W // 2, 240), scene.get("book_title", "TINH HOA NHÂN LOẠI").upper(), font=f_book, fill=(255, 255, 255), anchor="mm")
        draw.text((W // 2, 295), scene.get("chapter_title", "Trích Đoạn"), font=f_chap, fill=(156, 163, 175), anchor="mm")

        # Center Body Text for Mobile
        f_body = ImageFont.truetype(self.font_title_path, 50)
        max_w = 880
        lines = self._wrap_text(scene["text"], f_body, max_w, draw)
        line_h = 78
        total_h = len(lines) * line_h
        start_y = (H // 2) - (total_h // 2)

        f_q = ImageFont.truetype(self.font_title_path, 130)
        draw.text((90, start_y - 90), "“", font=f_q, fill=(234, 179, 8))

        for i, l in enumerate(lines):
            y = start_y + (i * line_h)
            # Text shadow for mobile readability
            draw.text((W // 2 + 2, y + 2), l, font=f_body, fill=(0, 0, 0), anchor="mm")
            draw.text((W // 2, y), l, font=f_body, fill=(255, 255, 255), anchor="mm")

        # Bottom CTA
        curr = scene.get("scene_index", 1)
        f_cta = ImageFont.truetype(self.font_sans_bold, 30)
        f_sub = ImageFont.truetype(self.font_sans_bold, 22)

        draw.text((W // 2, H - 230), f"PHẦN {curr:02d} / {total_scenes:02d}", font=f_cta, fill=(234, 179, 8), anchor="mm")
        draw.text((W // 2, H - 180), "👉 BẤM ĐĂNG KÝ KÊNH ĐỂ XEM TIẾP", font=f_sub, fill=(209, 213, 219), anchor="mm")

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        img.save(output_path, quality=95)
        return output_path
