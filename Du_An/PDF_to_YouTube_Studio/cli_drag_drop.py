"""
Quick Drag-and-Drop CLI Tool for PDF to YouTube Video Conversion
Usage:
- Drag and drop any PDF file directly onto 'KE_THA_PDF_TAO_VIDEO.bat' on Desktop!
- Or run in terminal: python cli_drag_drop.py "path/to/book.pdf"
"""

import os
import sys
import subprocess

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

from core.video_composer import VideoComposer
from core.pdf_reader import PDFReader

def main():
    print("="*65)
    print("🎬 CÔNG CỤ TỰ ĐỘNG CHUYỂN ĐỔI SÁCH PDF THÀNH VIDEO YOUTUBE (CLI)")
    print("="*65)

    # 1. Resolve PDF Path
    if len(sys.argv) > 1 and sys.argv[1].strip():
        pdf_path = sys.argv[1].strip().strip('"').strip("'")
    else:
        print("\n💡 Mẹo: Bạn có thể KÉO VÀ THẢ trực tiếp file PDF vào cửa sổ này rồi nhấn Enter.")
        pdf_path = input("Nhập đường dẫn file PDF: ").strip().strip('"').strip("'")

    if not os.path.exists(pdf_path):
        print(f"\n❌ Lỗi: Không tìm thấy file tại đường dẫn: {pdf_path}")
        input("\nNhấn Enter để thoát...")
        sys.exit(1)

    # 2. Inspect PDF
    reader = PDFReader(pdf_path)
    total_pages = reader.total_pages
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    book_title = base_name.split("]")[-1].strip() if "]" in base_name else base_name

    print(f"\n📖 Tác phẩm phát hiện: {book_title}")
    print(f"📄 Tổng số trang PDF: {total_pages} trang")

    # 3. Choose page range
    print(f"\nThiết lập khoảng trang cần chuyển thể thành Video:")
    try:
        p_in = input(f"Nhập trang bắt đầu và kết thúc (mặc định 4-5) [Enter để chọn 4-5]: ").strip()
        if p_in and "-" in p_in:
            parts = p_in.split("-")
            start_p = int(parts[0].strip())
            end_p = int(parts[1].strip())
        else:
            start_p = min(4, total_pages)
            end_p = min(5, total_pages)
    except Exception:
        start_p = min(4, total_pages)
        end_p = min(5, total_pages)

    print(f"👉 Sẽ chuyển thể từ trang {start_p} đến trang {end_p}...")

    # 4. Choose Voice
    v_in = input("Chọn giọng đọc (1: Nam trầm ấm [Mặc định], 2: Nữ truyền cảm) [Enter=1]: ").strip()
    voice_gender = "female" if v_in == "2" else "male"

    # 5. Execute Processing
    composer = VideoComposer(workspace_dir=CURRENT_DIR)
    
    print("\n🚀 Bắt đầu quá trình render tự động...")
    try:
        result = composer.process_audiobook(
            pdf_path=pdf_path,
            book_title=book_title,
            chapter_title=f"Trích Đoạn Trang {start_p}-{end_p}",
            start_page=start_p,
            end_page=end_p,
            voice_gender=voice_gender,
            voice_speed="+0%",
            render_16_9=True,
            render_9_16=True
        )

        print("\n" + "="*65)
        print("🎉 XUẤT BẢN THÀNH CÔNG RỰC RỠ!")
        print("="*65)
        if result["video_16_9"]:
            print(f"📺 Video 16:9 Dài: {result['video_16_9']}")
        if result["video_9_16"]:
            print(f"📱 Video 9:16 Shorts: {result['video_9_16']}")
        print(f"📝 Gói SEO YouTube: {result['metadata_path']}")
        print("="*65)

        # Open Output folder in Windows File Explorer
        print("\n📂 Đang tự động mở thư mục chứa video...")
        subprocess.run(["explorer.exe", composer.output_dir])

    except Exception as e:
        print(f"\n❌ Đã xảy ra lỗi: {e}")

    input("\nNhấn Enter để đóng cửa sổ...")

if __name__ == "__main__":
    main()
