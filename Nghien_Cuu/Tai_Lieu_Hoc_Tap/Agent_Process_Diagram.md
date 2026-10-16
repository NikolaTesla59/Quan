# 🧠 Sơ đồ Tư duy & Xử lý của Hệ thống AI (Antigravity)

Dưới đây là sơ đồ chi tiết giải thích quá trình từ lúc bạn gõ một câu lệnh (nhấn Enter) cho đến khi nhận được dòng phản hồi trên màn hình. 

```mermaid
flowchart TD
    %% Định nghĩa các kiểu dáng (Styling)
    classDef user fill:#3b82f6,stroke:#1d4ed8,stroke-width:2px,color:#fff;
    classDef system fill:#8b5cf6,stroke:#6d28d9,stroke-width:2px,color:#fff;
    classDef ai fill:#10b981,stroke:#047857,stroke-width:2px,color:#fff;
    classDef tools fill:#f59e0b,stroke:#b45309,stroke-width:2px,color:#fff;

    %% Các node chính
    A([Người dùng nhập lệnh]):::user
    B[Hệ thống gom thông tin<br/><i>(Lệnh của bạn + Mục lục Skills đang bật)</i>]:::system
    C{AI phân tích & Suy nghĩ}:::ai
    
    %% Nhánh sử dụng công cụ
    D[AI gọi Công cụ (Tools)]:::tools
    E[Hệ thống thực thi Tool<br/><i>(Vd: Đọc file, chạy code, tìm Google)</i>]:::system
    F[Trả kết quả về cho AI]:::system
    
    %% Nhánh trả lời
    G[AI tổng hợp thông tin]:::ai
    H([Phản hồi hiển thị cho Người dùng]):::user

    %% Kết nối
    A -->|Nhấn Enter| B
    B -->|Gửi gói dữ liệu (Token)| C
    
    C -->|Cần dùng Tool| D
    D --> E
    E -->|Hoàn tất| F
    F -->|Đọc kết quả| C
    
    C -->|Đã đủ thông tin / Không cần Tool| G
    G --> H
```

> [!NOTE]
> **Giải thích về câu chuyện "Token và Skill":**
> Bước **"Hệ thống gom thông tin"** (Màu tím) chính là lúc hệ thống nhét cái *"Mục lục 108 Skill"* vào chung với câu lệnh của bạn. Nếu mục lục quá dài, nó sẽ chiếm hết chỗ, khiến phần lưu trữ câu lệnh và lịch sử chat của bạn bị ép nhỏ lại. Đó là lý do ta phải chuyển các Plugin thừa đi để tối ưu bước này!

> [!TIP]
> **Khả năng tự xoay vòng (Loop):** 
> Chú ý vòng lặp màu xanh lá và vàng (AI -> Gọi Tool -> Kết quả -> AI). Tôi có thể tự động lặp lại vòng lặp này hàng chục lần ngầm bên trong để tự sửa lỗi code hoặc tự tìm kiếm trước khi quyết định viết câu trả lời cuối cùng ra màn hình cho bạn.
