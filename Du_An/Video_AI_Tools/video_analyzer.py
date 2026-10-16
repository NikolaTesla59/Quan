import os
import sys
import time
import winreg
from google import genai
from google.genai import types

def get_gemini_api_key():
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as reg_key:
            val, _ = winreg.QueryValueEx(reg_key, "GEMINI_API_KEY")
            return val
    except Exception:
        return None

def analyze_video(video_path, custom_prompt=None):
    api_key = get_gemini_api_key()
    if not api_key:
        print("[LỖI] Không tìm thấy biến môi trường GEMINI_API_KEY. Vui lòng kiểm tra lại.")
        return

    client = genai.Client(api_key=api_key)
    
    print(f"[*] Đang tải video lên máy chủ Gemini File API: {video_path}...")
    video_file = client.files.upload(file=video_path)
    print(f"[*] Đã tải lên. File URI: {video_file.uri}")

    # Chờ video xử lý xong trên máy chủ Google
    while video_file.state.name == "PROCESSING":
        print("[*] Video đang được AI phân tích và lập chỉ mục từng khung hình (PROCESSING)...")
        time.sleep(5)
        video_file = client.files.get(name=video_file.name)

    if video_file.state.name == "FAILED":
        raise ValueError(f"[LỖI] Xử lý video thất bại: {video_file.error.message}")

    print("[*] Phân tích video hoàn tất! Đang trích xuất tri thức...")

    prompt = custom_prompt or (
        "Bạn là chuyên gia phân tích video hàng đầu. Hãy xem toàn bộ video này và bóc tách cấu trúc nội dung chi tiết:\n"
        "1. Tóm tắt nội dung cốt lõi và thông điệp chính của video trong 3-5 gạch đầu dòng.\n"
        "2. Bảng Timeline chi tiết theo mốc thời gian [Phút:Giây] - Từng phân cảnh, luận điểm và hành động quan trọng.\n"
        "3. Trích xuất các số liệu, công thức, slide hoặc đồ thị xuất hiện trong video (nếu có).\n"
        "4. Top 5 bài học / tri thức đắt giá nhất có thể ứng dụng thực tế."
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[video_file, prompt]
    )

    print("\n" + "="*60)
    print("KẾT QUẢ BÓC TÁCH TRI THỨC TỪ VIDEO:")
    print("="*60 + "\n")
    print(response.text)

    # Lưu kết quả ra file markdown
    out_file = os.path.splitext(video_path)[0] + "_summary.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"\n[+] Đã lưu bản phân tích chi tiết vào: {out_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách dùng: python video_analyzer.py <duong_dan_file_video.mp4>")
    else:
        analyze_video(sys.argv[1])
