# 🎬 YouTube Video Studio AI (Độc Lập)

Hệ thống độc lập tự động chuyển đổi sách PDF, tác phẩm văn học, kinh tế, triết học thành Video YouTube 16:9 Full HD và Video dọc 9:16 Shorts/TikTok kèm giọng đọc AI Studio tiếng Việt và gói SEO tối ưu.

---

## 🚀 Hai Cách Sử Dụng Độc Lập Nhanh Nhất

### 1. Dùng Giao Diện Web Studio Trực Quan
- **Nhấp đúp chuột vào file ngoài Desktop**: `YOUTUBE_VIDEO_STUDIO.bat`
- Giao diện Web (Streamlit) sẽ tự động mở trên trình duyệt tại `http://localhost:8502`.
- Tính năng:
  - Tự động quét và chọn nhanh các tác phẩm có sẵn trong thư viện `Desktop/Sách`.
  - Tùy chỉnh khoảng trang (ví dụ từ trang 4 đến 5).
  - Tùy chỉnh giọng đọc Nam (trầm ấm) hoặc Nữ (truyền cảm), tốc độ đọc.
  - Xem trước video 16:9 và Shorts 9:16 trực tiếp trên trình duyệt.
  - Sao chép gói SEO (Tiêu đề, mô tả, thẻ tags) với 1 click.
  - Nút mở nhanh thư mục chứa video trên máy tính.

### 2. Dùng Công Cụ Kéo-Thả Nhanh (Drag & Drop)
- **Kéo bất kỳ file PDF nào trên máy tính và thả trực tiếp vào icon**: `KEO_THA_PDF_TAO_VIDEO.bat` ngoài Desktop.
- Hệ thống sẽ tự động khởi động cửa sổ xử lý dòng lệnh, bóc tách trang và render video ngay lập tức.
- Khi hoàn thành, thư mục thành phẩm chứa file `.mp4` sẽ tự động mở lên!

---

## 📁 Cấu Trúc Thư Mục Độc Lập

```
C:\Users\Admin\.gemini\antigravity\scratch\pdf_to_youtube_studio\
├── app.py                      # Ứng dụng Web Studio độc lập (Streamlit)
├── cli_drag_drop.py            # Script xử lý kéo thả file PDF nhanh
├── core/
│   ├── pdf_reader.py           # Module trích xuất nguyên tác & chia phân cảnh
│   ├── voice_engine.py         # Module lồng tiếng AI đa tầng (Edge-TTS + Google TTS)
│   ├── slide_artist.py         # Module thiết kế visual frame (Pillow 16:9 & 9:16)
│   └── video_composer.py       # Module render video và concat FFmpeg
├── output/                     # Thư mục chứa video thành phẩm (.mp4) và SEO (.txt)
└── temp/                       # Thư mục tạm lưu frame và audio từng cảnh
```
