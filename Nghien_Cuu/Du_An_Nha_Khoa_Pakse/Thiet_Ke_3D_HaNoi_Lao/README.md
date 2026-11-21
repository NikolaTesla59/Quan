# Hồ Sơ Thiết Kế Phối Cảnh 3D - Nha Khoa Hà Nội Lào (Pakse)

Tài liệu kỹ thuật và toàn bộ hình ảnh thiết kế phối cảnh kiến trúc 3D, mặt bằng công năng và bố trí nội thất phòng khám Nha khoa Hà Nội - Lào tại Pakse (Cộng hòa Dân chủ Nhân dân Lào).

---

## 🏛️ Tổng Quan Kiến Trúc & Công Năng

Hồ sơ thiết kế 3D toàn diện gồm 46 trang bản vẽ phối cảnh chi tiết:
1. **Khu vực Đón tiếp & Sảnh chờ**: Quầy lễ tân nhận diện thương hiệu Hà Nội - Lào, khu ghế ngồi chờ bệnh nhân cao cấp, màn hình hiển thị tư vấn nha khoa.
2. **Khu vực Khám & Điều trị Tổng quát**: Bố trí cụm ghế nha khoa hiện đại, hệ thống đèn chiếu, tủ dụng cụ nha khoa âm tường, luồng di chuyển thuận tiện cho bác sĩ và trợ thủ.
3. **Phòng Phẫu thuật & Cấy ghép Implant**: Thiết kế phòng phẫu thuật chuẩn vô trùng một chiều, trang bị đèn mổ trần, hệ thống máy cấy ghép chuyên dụng.
4. **Phòng Chẩn đoán Hình ảnh (X-Quang / CT ConeBeam 3D)**: Phòng ốp chì bảo vệ an toàn bức xạ, đặt máy chụp toàn cảnh kỹ thuật số.
5. **Khu vực Tiệt trùng & Hấp sấy (Sterilization)**: Quy trình khử khuẩn 4 bước khép kín (Phân loại -> Rửa siêu âm -> Đóng gói -> Hấp tiệt trùng Autoclave).
6. **Khu vực Nội bộ & Điều hành**: Phòng họp chuyên môn, phòng nghỉ bác sĩ, phòng labo nha khoa tinh gọn.

---

## 📁 Cấu Trúc Dữ Liệu & Giải Pháp Tối Ưu Git

Tệp hồ sơ PDF gốc (`hstk 3D nk HA NOI LAO 18-11.pdf`) có kích thước ~133 MB (vượt quá ngưỡng giới hạn 100 MB của GitHub). Do đó, hệ thống tự động áp dụng giải pháp tối ưu hóa dữ liệu:
- **`ban_ve_3d/` (46 tệp ảnh .jpg, ~12.8 MB)**: Trích xuất độ phân giải cao toàn bộ 46 trang bản vẽ phối cảnh chi tiết phục vụ kiểm tra chuyên sâu.
- **`collages/` (5 bảng tiếp xúc 3x3 .jpg, ~948 KB)**: Bảng tổng quan 9 hình/trang giúp xem nhanh toàn bộ không gian phòng khám mà không cần duyệt từng ảnh.
- **Tập lệnh tự động hóa (`.py`)**: Bộ công cụ phân tích cấu trúc PDF (`inspect_pdf.py`), kiểm tra trang (`check_pages.py`), trích xuất ảnh (`render_pages.py`) và tạo contact sheet (`make_collages.py`).
