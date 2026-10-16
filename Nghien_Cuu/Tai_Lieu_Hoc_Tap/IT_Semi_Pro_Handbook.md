# 📘 Sổ Tay IT Bán Chuyên (Dành Cho Dân Văn Phòng)

Chúc mừng bạn đã quyết định bước ra khỏi vùng an toàn của Tin học văn phòng (Word, Excel) để tiến lên cấp độ **"IT Bán Chuyên" (Semi-Pro IT)**! 

Cuốn sổ tay này tổng hợp những kiến thức cốt lõi nhất, không quá hàn lâm, đủ để bạn tự động hóa công việc và làm chủ các công cụ mạnh mẽ.

---

## 1. Tư duy Lập trình cơ bản (Logic & Python)
Để sai bảo máy tính làm việc tự động, bạn không cần học toán cao cấp, bạn chỉ cần học **Python** - ngôn ngữ lập trình dễ tiếp cận nhất. (Hệ thống của bạn đã cài sẵn Python rồi!)
*   **Biến (Variables):** Cách máy tính lưu trữ thông tin (VD: `doanh_thu = 50000`).
*   **Câu lệnh điều kiện (If/Else):** Tư duy rẽ nhánh (VD: Nếu doanh thu > 50000 thì in ra "Thưởng", ngược lại in ra "Phạt").
*   **Vòng lặp (For/While):** Bí quyết để xử lý 1000 file Excel mà không mỏi tay. Máy tính sẽ lặp đi lặp lại một hành động cho bạn trong tích tắc.
*   *Thực hành nhanh:* Làm quen với thư viện `pandas` trong Python để tự động hóa bảng tính thay vì dùng chuột kéo công thức trong Excel.

## 2. Làm chủ Dữ Liệu (SQL & Database)
Dân văn phòng quen với bảng tính Excel, nhưng khi dữ liệu lên tới hàng triệu dòng, Excel sẽ bị chậm hoặc treo. Đó là lúc bạn cần **Cơ sở dữ liệu (Database)** và ngôn ngữ **SQL**.
*   **Database là gì:** Có thể coi là một "siêu Excel" ẩn giấu trong hệ thống máy chủ, chứa hàng chục bảng dữ liệu liên kết logic với nhau.
*   **Câu lệnh SELECT:** Lấy dữ liệu ra (Ví dụ: Kéo cột Tên khách hàng từ bảng Khách hàng).
*   **Câu lệnh WHERE:** Lọc dữ liệu (Ví dụ: Chỉ lấy những khách mua hàng tháng 7).
*   **Câu lệnh JOIN:** Ghép nối các bảng (Ví dụ: Ghép mã khách hàng với bảng hóa đơn mua hàng).

## 3. Giao tiếp với Máy tính (Dòng lệnh - Command Line/Terminal)
Thay vì dùng chuột click vào các biểu tượng (icon), dân IT Bán chuyên biết cách ra lệnh trực tiếp bằng bàn phím.
*   **PowerShell / Command Prompt (Windows):** Màn hình đen chữ trắng (Terminal).
*   **Lệnh cơ bản cần biết:** `cd` (di chuyển giữa các thư mục), `dir` hoặc `ls` (xem danh sách file), `mkdir` (tạo thư mục mới).
*   **Lợi ích:** Ra lệnh siêu tốc, cài đặt phần mềm, chạy script Python chỉ bằng một dòng chữ (như cách tôi vừa tải SDK về cho bạn).

## 4. Quản lý Phiên bản (Git)
Dân văn phòng thường lưu file kiểu: `baocao_cuoicung.docx`, `baocao_cuoicung_thatsu.docx`, `baocao_cuoicung_sua_lan_3.docx`. Rất dễ nhầm lẫn!
IT dùng hệ thống **Git** để quản lý lịch sử file (chủ yếu là file code và văn bản thô).
*   **Commit:** Giống như "Chụp ảnh" lại trạng thái của file ở thời điểm hiện tại. Bạn có thể quay ngược thời gian về bất kỳ bức ảnh nào.
*   **Branch (Nhánh):** Tạo một bản sao để bạn thoải mái chỉnh sửa thử nghiệm. Nếu làm hỏng thì vứt nhánh đó đi, bản chính không bị ảnh hưởng.
*   **GitHub:** Mạng xã hội/Đám mây để lưu trữ lịch sử code và chia sẻ cho người khác.

## 5. Kỹ năng "Làm sếp" AI (Prompt Engineering)
Kỹ năng quan trọng nhất trong kỷ nguyên này là **biết cách ra lệnh cho AI** (như cách bạn đang nói chuyện với Antigravity).
*   **Quy tắc rõ ràng:** Cung cấp Ngữ cảnh (Context) + Mục tiêu (Goal) + Định dạng đầu ra (Format).
*   **Phân rã vấn đề:** Thay vì bảo "Làm cho tôi phần mềm quản lý kho", hãy chia nhỏ: "Bước 1: Hướng dẫn tôi tạo cấu trúc file Excel lưu hàng hóa. Bước 2: Viết script trừ kho tự động khi có đơn hàng...".
*   **Tận dụng Hệ sinh thái:** Bạn đã có Antigravity IDE, hãy tập cách giao phần việc thô cho AI làm (viết code, truy vấn SQL), và bạn chỉ đóng vai trò người lên ý tưởng và duyệt kết quả cuối cùng (Reviewer).

---

> [!TIP]
> **Lời khuyên chân thành:** 
> Đừng cố học thuộc lòng tất cả mớ lý thuyết này cùng lúc! Hãy bắt đầu bằng cách **đặt ra một bài toán thực tế trong công việc hàng ngày của bạn** (Ví dụ: "Làm sao để tự động gộp 5 file báo cáo chấm công hàng tuần?"). 
> Sau đó, đưa bài toán đó cho tôi, tôi sẽ hướng dẫn bạn dùng Python hoặc SQL để giải quyết nó. Thông qua thực hành thực tế, bạn sẽ "tiến hóa" thành IT Bán chuyên lúc nào không hay!
