# Kho Lưu Trữ Cá Nhân & Đồng Bộ Dự Án - NikolaTesla59 (Quân)

Hệ thống lưu trữ, quản lý mã nguồn và tài liệu nghiên cứu cá nhân được đồng bộ hóa và sao lưu an toàn tự động.

---

## 📂 Cấu Trúc Thư Mục

### 📚 1. Nghiên Cứu (`Nghien_Cuu/`)
- **`Kinh_Te_Hoc_He_Thong/`**: Chuyên khảo hoàn chỉnh Kinh tế học hệ thống (bản thảo Word, PDF, LaTeX, HTML, Markdown và sơ đồ hệ thống Mermaid).
- **`Laos_BoP_Research/`**: Công trình nghiên cứu, phân tích chuyên sâu về Cán cân thanh toán Lào (BoP) qua các phiên bản v3, v4 và tài liệu pháp lý đầu tư nước ngoài.
- **`Tieu_Luan_Hoc_Thuat/`**: Tập hợp các bản thảo bài tiểu luận học thuật hoàn thiện.
- **`Du_An_Nha_Khoa_Pakse/`**: Hồ sơ dự án đầu tư phòng khám nha khoa tại Pakse, Lào (Slide thuyết trình, mô hình tài chính Excel Lite/Full, kế hoạch đầu tư chi tiết và tóm tắt điều hành).
- **`Tai_Lieu_Hoc_Tap/`**: Cẩm nang CNTT Semi-Pro, quy trình Agent Process Diagram, báo cáo đánh giá và hướng dẫn công cụ AI.

### 💻 2. Dự Án & Công Cụ Kỹ Thuật (`Du_An/`)
- **`NhaKhoa_LaoViet_Pakse/`**: Giao diện website đầy đủ cho phòng khám nha khoa Lào - Việt tại Pakse (trang chủ, bảng giá, đội ngũ bác sĩ, dịch vụ răng sứ, implant, liên hệ).
- **`Vietstock_Screener/`**: Hệ thống bộ lọc cổ phiếu theo khung tiêu chí cổng chặn, độ nhạy chu kỳ kinh doanh và đạo đức ban lãnh đạo kèm script cập nhật tự động hàng ngày.
- **`Video_AI_Tools/`**: Bộ công cụ tự động hóa sáng tạo video ngắn (Shorts/Reels) và phân tích kịch bản video AI.
- **`LLM_Orchestrator/`**: Khung điều phối đa mô hình ngôn ngữ lớn (LLM Orchestration) linh hoạt.
- **`Doc2Slide_App/`**: Ứng dụng tự động chuyển đổi tài liệu văn bản (.docx) thành slide thuyết trình PowerPoint (.pptx).

---

## 🔒 Chính Sách An Toàn & Bảo Mật (Safe Backup Policy)
- Toàn bộ tệp chứa khóa bí mật (`.env`, private keys, API tokens) đều được kiểm tra nghiêm ngặt và loại trừ qua `.gitignore`.
- Môi trường ảo (`venv/`), cache (`__pycache__/`, `node_modules/`) và file khóa tạm thời của MS Office (`~$*`) được tự động loại bỏ để tối ưu dung lượng kho lưu trữ.
- Chi tiết lịch sử các phiên đồng bộ được lưu trữ tại file [NHAT_KY_SAO_LUU.md](NHAT_KY_SAO_LUU.md).