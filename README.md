# Kho Lưu Trữ Cá Nhân & Đồng Bộ Dự Án - NikolaTesla59 (Quân)

Hệ thống lưu trữ, quản lý mã nguồn và tài liệu nghiên cứu cá nhân được đồng bộ hóa và sao lưu an toàn tự động.

---

## 📂 Cấu Trúc Thư Mục

### 📚 1. Nghiên Cứu (`Nghien_Cuu/`)
- **`Quan_Tri_Rui_Ro_Agribank_MB/`**: Công trình nghiên cứu Thạc sĩ NEU Quản trị rủi ro tín dụng tại Agribank và MBBank giai đoạn 2020–2025:
  - Bản thảo luận văn hoàn chỉnh học thuật V5 (`Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v5.docx`), Bài tập lớn Thạc sĩ QTRR (`Bai_tap_lon_QTRR_Agribank_MB_2020-2025.docx`), Báo cáo thuyết trình điều hành (`Bao_cao_Thuyet_trinh_Agribank_MB_2020-2025_Executive.docx`), cùng các bản v2-v4.
  - Mô hình tài chính định lượng kiểm định 2 ngân hàng 6 năm với dữ liệu sạch 100%, tích hợp chuẩn IFRS 9 ECL và kịch bản Stress Testing 2026 (`Phan_tich_RRTD_Agribank_MB_2020-2025_v4.xlsx`, bản v3, v2) và BCTC gốc trích xuất (`.xlsx`).
  - Danh mục tài liệu cần thu thập (`.xlsx`), Báo cáo phản biện học thuật ThS-TS (`.docx`, `.md`), Báo cáo soát xét hoàn tất v4-v5.
  - Thư mục biểu đồ phân tích (`charts/`): 6 đồ thị trực quan phân tích chuyên sâu NPL, nhóm 2, CAR, LLCR, Stress Testing và IFRS 9.
  - Thư mục dữ liệu trích xuất (`extracted_bctc/`): Dữ liệu trích xuất BCTC MBBank kiểm toán định dạng Markdown, JSON và kịch bản bóc tách.
  - Bộ kịch bản sinh tài liệu & tự động hóa (`generators/`): `build_standalone_executive_paper.py`, `build_complete_executive_paper.py`, `build_v5_master_perfect.py`, `upgrade_all_excel_v3.py`, `upgrade_word_v3.py`, `build_full_thesis.py`, `build_advanced_excel.py`.
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
- **`Vietstock_Screener/`**: Hệ thống bộ lọc cổ phiếu theo khung tiêu chí cổng chặn, độ nhạy chu kỳ kinh doanh và đạo đức ban lãnh đạo:
  - Bản PRO Excel tự động cập nhật (`Bo_Loc_Co_Phieu_Vietstock_Khung_Tieu_Chi_PRO.xlsx`) chuẩn 169 mã cổ phiếu tinh hoa & biên an toàn upside.
  - Công cụ tìm kiếm & truy vấn mã chứng khoán (`find_tickers.py`, `query_stocks.py`).
  - Script cập nhật tự động hàng ngày (`auto_update_screener.py`), phân tích top cổ phiếu (`analyze_top.py`), trích xuất tổng hợp (`get_summary.py`), cơ sở dữ liệu định chế (`stocks.db`) và công cụ chẩn đoán (`diagnostic.py`, `import_to_sqlite.py`).
- **`Video_AI_Tools/`**: Bộ công cụ tự động hóa sáng tạo video ngắn (Shorts/Reels) và phân tích kịch bản video AI.
- **`LLM_Orchestrator/`**: Khung điều phối đa mô hình ngôn ngữ lớn (LLM Orchestration) linh hoạt.
- **`Doc2Slide_App/`**: Ứng dụng tự động chuyển đổi tài liệu văn bản (.docx) thành slide thuyết trình PowerPoint (.pptx).
- **`System_Maintenance/`**: Bộ kịch bản PowerShell tự động bảo trì, tối ưu hóa hệ điều hành, dọn dẹp rác, xóa cache DNS, chẩn đoán sức khỏe phần cứng CPU/RAM/Disk:
  - `system_maintenance.ps1`: Kịch bản bảo trì tổng thể đa chức năng.
  - `optimize_system.ps1`: Tối ưu hóa hệ thống, tinh chỉnh dịch vụ và giải phóng RAM.
  - `diagnose_perf.ps1`: Chẩn đoán hiệu năng và nghẽn tài nguyên.
  - `get_system_specs.ps1`: Trích xuất thông số kỹ thuật phần cứng và hệ điều hành chi tiết.
  - `run_maintenance.ps1`, `maintenance.ps1`, `sys_maintenance.ps1`.

---

## 🔒 Chính Sách An Toàn & Bảo Mật (Safe Backup Policy)
- Toàn bộ tệp chứa khóa bí mật (`.env`, private keys, API tokens) đều được kiểm tra nghiêm ngặt và loại trừ qua `.gitignore`.
- Môi trường ảo (`venv/`), cache (`__pycache__/`, `node_modules/`), file khóa tạm thời của MS Office (`~$*`), tệp driver nhị phân (`.dll`, `usb_driver.zip`) và tệp scan PDF gốc BCTC nặng (>200MB) được tự động loại bỏ để tối ưu dung lượng kho lưu trữ.
- Chi tiết lịch sử các phiên đồng bộ được lưu trữ tại file [NHAT_KY_SAO_LUU.md](NHAT_KY_SAO_LUU.md).
