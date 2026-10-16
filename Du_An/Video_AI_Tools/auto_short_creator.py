import os
import sys
import asyncio
import edge_tts
import winreg
from google import genai

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

async def generate_voice(text, output_audio_path, voice="vi-VN-NamMinhNeural"):
    print(f"[*] Đang tổng hợp giọng đọc AI tiếng Việt ({voice})...")
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_audio_path)
    print(f"[+] Đã tạo file thuyết minh thành công: {output_audio_path}")

def generate_short_content(topic):
    api_key = get_gemini_api_key()
    if not api_key:
        print("[LỖI] Thiếu GEMINI_API_KEY. Vui lòng kiểm tra lại cấu hình.")
        return None

    client = genai.Client(api_key=api_key)
    prompt = f"""
    Bạn là biên kịch video ngắn viral (TikTok/YouTube Shorts/Reels) chuyên nghiệp.
    Hãy viết kịch bản 60 giây thật cuốn hút về chủ đề: "{topic}".
    Yêu cầu:
    1. Hook 3 giây đầu gây tò mò cực độ, giữ chân người xem.
    2. Thân bài giải thích sâu sắc, gãy gọn, không nói thừa.
    3. Call to Action (kêu gọi hành động) ở cuối.
    Chỉ trả về nội dung lời thoại thuyết minh (để AI đọc thành tiếng), không kèm chú thích hay biểu cảm trong ngoặc.
    """

    print(f"[*] Đang viết kịch bản video ngắn cho chủ đề: '{topic}'...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    script_text = response.text.strip()
    print("\n--- KỊCH BẢN THUYẾT MINH ---")
    print(script_text)
    print("----------------------------\n")
    return script_text

def main():
    if len(sys.argv) < 2:
        topic = "Bản chất của lạm phát và cách người giàu bảo vệ tài sản"
    else:
        topic = " ".join(sys.argv[1:])

    script_text = generate_short_content(topic)
    if not script_text:
        return

    os.makedirs("output", exist_ok=True)
    audio_file = os.path.join("output", "voiceover.mp3")
    script_file = os.path.join("output", "script.txt")

    with open(script_file, "w", encoding="utf-8") as f:
        f.write(script_text)

    # Chạy tạo giọng nói
    asyncio.run(generate_voice(script_text, audio_file))
    print(f"\n[🎉 HOÀN TẤT] File kịch bản và audio thuyết minh đã sẵn sàng trong thư mục 'output/'!")

if __name__ == "__main__":
    main()
