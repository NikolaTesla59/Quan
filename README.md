# Kho Lưu Trữ Cá Nhân & Đồng Bộ Dự Án - NikolaTesla59 (Quân)

Hệ thống lưu trữ, quản lý mã nguồn và tài liệu nghiên cứu cá nhân được đồng bộ hóa và sao lưu an toàn tự động.

---

## 📂 Cấu Trúc Thư Mục

### 📚 1. Nghiên Cứu (`Nghien_Cuu/`)
- **`Quan_Tri_Rui_Ro_Agribank_MB/`**: Công trình nghiên cứu Thạc sĩ NEU Quản trị rủi ro tín dụng tại Agribank và MBBank giai đoạn 2020–2025: luận văn hoàn chỉnh học thuật chuẩn mực (`.docx`), mô hình tài chính định lượng kiểm định 2 ngân hàng 6 năm với dữ liệu sạch 100% (`.xlsx`), danh mục tài liệu cần thu thập (`.xlsx`) và hệ thống kịch bản Python tự động hóa xây dựng tài liệu, chuẩn hóa dữ liệu (`build_full_thesis.py`, `build_advanced_excel.py`, `sync_v2.py`, `update_danh_muc.py`, `final_sanity_check.py`).
- **`Kinh_Te_Hoc_He_Thong/`**: Chuyên khảo hoàn chỉnh Kinh tế học hệ thống (bản thảo Word, PDF, LaTeX, HTML, Markdown và sơ đồ hệ thống Mermaid).
- **`Laos_BoP_Research/`**: Công trình nghiên cứu, phân tích chuyên sâu về Cán cân thanh toán Lào (BoP) qua các phiên bản v3, v4 và tài liệu pháp lý đầu tư nước ngoài.
- **`Tieu_Luan_Hoc_Thuat/`**: Tập hợp các bản thảo bài tiểu luận học thuật hoàn thiện.
- **`Du_An_Nha_Khoa_Pakse/`**: Hồ sơ dự án đầu tư phòng khám nha khoa tại Pakse, Lào (Slide thuyết trình, mô hình tài chính Excel Lite/Full, kế hoạch đầu tư chi tiết và tóm tắt điều hành).
- **`So_Tay_Nghe_Thuat/`**: Chuyên khảo "Sổ Tay Nghệ Thuật Toàn Tập - Từ Nhập Môn Đến Chuyên Sâu" (hướng dẫn chi tiết phương pháp đọc tranh, ngôn ngữ thị giác và lịch sử mỹ thuật phương Tây từ Phục Hưng đến Siêu Thực - định dạng .docx và .pdf).
- **`Tuyen_Tap_Thi_Ca_Viet_Trung/`**: Hệ thống nghiên cứu, số hóa văn bản học và tự động hóa biên soạn tuyển tập thi ca cổ điển Đường - Tống, thơ Nôm trung đại (Hồ Xuân Hương, Bà Huyện Thanh Quan, Nguyễn Trãi, Nguyễn Du) và phong trào Thơ Mới Việt Nam (`poetry_builder`, `poetry_anthology`, cùng các kịch bản biên dịch và phụ lục dữ liệu JSON).
- **`NEU_Textbook_Builder/`**: Hệ thống kỹ thuật số hóa & tự động hóa biên soạn toàn diện 10 bộ giáo trình kinh tế & tài chính trọng điểm Đại học Kinh tế Quốc dân (NEU): Nguyên lý kế toán, Kế toán tài chính 1-2, Kinh tế đầu tư, Thị trường chứng khoán, Tài chính doanh nghiệp, Tài chính tiền tệ, Định giá tài sản, Kinh doanh bảo hiểm, Ngân hàng thương mại, Tài chính quốc tế, Thanh toán quốc tế, Giao dịch đàm phán; gồm lõi `neu_engine.py`, 10 generators độc lập, batch builders song song và hệ thống báo cáo kiểm toán chất lượng JSON.
- **`Tai_Lieu_Hoc_Tap/`**: Cẩm nang CNTT Semi-Pro, quy trình Agent Process Diagram, báo cáo đánh giá công cụ AI, quy chuẩn tư duy phản biện Fabric Patterns & Shannon Alpha (`rules_cognitive.md`), quy chuẩn kỹ thuật lập trình senior (`rules_tech_stack.md`) và công cụ phân tích kỹ năng agent (`analyze_skills.py`).

### 💻 2. Dự Án & Công Cụ Kỹ Thuật (`Du_An/`)
- **`NhaKhoa_LaoViet_Pakse/`**: Giao diện website đầy đủ cho phòng khám nha khoa Lào - Việt tại Pakse (trang chủ, bảng giá, đội ngũ bác sĩ, dịch vụ răng sứ, implant, liên hệ).
- **`Vietstock_Screener/`**: Hệ thống bộ lọc cổ phiếu theo khung tiêu chí cổng chặn, độ nhạy chu kỳ kinh doanh và đạo đức ban lãnh đạo kèm script cập nhật tự động hàng ngày, bộ phân tích top cổ phiếu (`analyze_top.py`), trích xuất tổng hợp (`get_summary.py`), cơ sở dữ liệu định chế (`stocks.db`) và công cụ chẩn đoán (`diagnostic.py`, `import_to_sqlite.py`).
- **`Video_AI_Tools/`**: Bộ công cụ tự động hóa sáng tạo video ngắn (Shorts/Reels) và phân tích kịch bản video AI.
- **`LLM_Orchestrator/`**: Khung điều phối đa mô hình ngôn ngữ lớn (LLM Orchestration) linh hoạt.
- **`Doc2Slide_App/`**: Ứng dụng tự động chuyển đổi tài liệu văn bản (.docx) thành slide thuyết trình PowerPoint (.pptx).
- **`System_Maintenance/`**: Kịch bản PowerShell tự động dọn dẹp rác hệ thống, xóa cache DNS, chẩn đoán sức khỏe RAM/CPU và xuất báo cáo JSON đo lường chi tiết (`system_maintenance.ps1`, `maintenance.ps1`, `sys_maintenance.ps1`, `run_maintenance.ps1`).

---

## 🔒 Chính Sách An Toàn & Bảo Mật (Safe Backup Policy)
- Toàn bộ tệp chứa khóa bí mật (`.env`, private keys, API tokens) đều được kiểm tra nghiêm ngặt và loại trừ qua `.gitignore`.
- Môi trường ảo (`venv/`), cache (`__pycache__/`, `node_modules/`) và file khóa tạm thời của MS Office (`~$*`) được tự động loại bỏ để tối ưu dung lượng kho lưu trữ.
- Chi tiết lịch sử các phiên đồng bộ được lưu trữ tại file [NHAT_KY_SAO_LUU.md](NHAT_KY_SAO_LUU.md).