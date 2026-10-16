import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Tải các biến môi trường (API Keys) từ file .env
load_dotenv()

# 2. Cấu hình Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def step1_gemini_compression(raw_text, task_instruction):
    """
    Sử dụng Gemini Flash (Rẻ, Nhanh, Đọc được nhiều) để tóm tắt và lọc dữ liệu thô.
    """
    print("🤖 Đang gọi Gemini (Flash) để nén dữ liệu và xử lý thô...")
    
    # Sử dụng model flash siêu tốc và tiết kiệm
    model = genai.GenerativeModel('gemini-3.6-flash')
    
    prompt = f"""
    Nhiệm vụ của bạn là đọc đoạn dữ liệu thô dưới đây và thực hiện các yêu cầu xử lý cơ bản.
    Yêu cầu: {task_instruction}
    
    Dữ liệu thô:
    {raw_text}
    
    Chỉ trả về kết quả đã được lọc/tóm tắt, không giải thích dài dòng.
    """
    
    response = model.generate_content(prompt)
    return response.text

def step2_gemini_pro_reasoning(gemini_output, complex_task_instruction):
    """
    Sử dụng Gemini Pro để xử lý các logic phức tạp, viết code kiến trúc, v.v., dựa trên dữ liệu đã nén.
    """
    print("🧠 Đang gọi Gemini (Pro) để suy luận sâu dựa trên dữ liệu đã nén từ Flash...")
    
    model = genai.GenerativeModel('gemini-3.6-flash')
    
    prompt = f"""
    Dưới đây là thông tin đã được làm sạch và tóm tắt:
    <thông_tin>
    {gemini_output}
    </thông_tin>
    
    Nhiệm vụ của bạn:
    {complex_task_instruction}
    """
    
    response = model.generate_content(prompt)
    return response.text

def main():
    # Ví dụ: Một đoạn tài liệu thô, dài dòng (Bạn có thể nhét cả file PDF, hàng chục trang code vào đây)
    raw_data = """
    Báo cáo lỗi hệ thống ngày 22/08:
    - User ID 1092 phàn nàn rằng khi nhấn vào nút thanh toán thì bị văng app.
    - Log server ghi nhận: Out of Memory (OOM) ở file payment_gateway.js dòng 402.
    - RAM tăng đột biến từ 1GB lên 4GB trong vòng 3 phút khi gọi API của ngân hàng đối tác.
    - Database query ở bảng Transactions không có index nên mất 5 giây để lưu.
    - Code cũ do dev thực tập sinh viết, dùng vòng lặp while(true) sai logic ở hàm kiểm tra trạng thái.
    """
    
    # ---------------------------------------------------------
    # BƯỚC 1: Dùng GEMINI FLASH để gánh việc mệt nhọc (Đọc dữ liệu dài và trích xuất)
    # ---------------------------------------------------------
    gemini_task = "Hãy đọc báo cáo lỗi hệ thống này và liệt kê các nguyên nhân cốt lõi về mặt kỹ thuật dưới dạng JSON hoặc danh sách gạch đầu dòng ngắn gọn nhất. Lược bỏ các thông tin râu ria."
    
    compressed_data = ""
    try:
        compressed_data = step1_gemini_compression(raw_data, gemini_task)
        print("\n--- 🟢 KẾT QUẢ TỪ GEMINI FLASH (Dữ liệu đã nén gọn) ---")
        print(compressed_data)
    except Exception as e:
        print(f"Lỗi khi gọi Gemini Flash: {e}")
        return

    print("\n" + "="*60 + "\n")

    # ---------------------------------------------------------
    # BƯỚC 2: Dùng GEMINI PRO để suy luận, thiết kế kiến trúc và giải quyết vấn đề
    # ---------------------------------------------------------
    pro_task = "Dựa vào danh sách lỗi kỹ thuật này, hãy đóng vai trò là một System Architect lão luyện. Viết ra một kế hoạch (Action Plan) chi tiết từng bước để team Dev fix triệt để. Yêu cầu có đề xuất refactor code nếu cần."
    
    try:
        final_result = step2_gemini_pro_reasoning(compressed_data, pro_task)
        print("\n--- 🔵 KẾT QUẢ TỪ GEMINI PRO (Kế hoạch chuyên sâu) ---")
        print(final_result)
    except Exception as e:
        print(f"Lỗi khi gọi Gemini Pro: {e}")

if __name__ == "__main__":
    main()
