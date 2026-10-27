import openpyxl
from openpyxl.styles import Font, PatternFill

file_path = r'C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\Danh_muc_tai_lieu_can_lay_Agribank_MB.xlsx'
wb = openpyxl.load_workbook(file_path)

font_blue = Font(name='Arial', size=10, color='FF0000FF')
font_black = Font(name='Arial', size=10, color='FF000000')
font_bold = Font(name='Arial', size=10, bold=True, color='FF000000')
no_fill = PatternFill(fill_type=None)

# ---------------------------------------------------------
# 1. UPDATE SHEET: File_can_tai
# ---------------------------------------------------------
ws_files = wb['File_can_tai']

files_data = {
    5: (
        "Đã tải",
        "Agribank_BCTC_HN_2021_KiemToan.pdf (https://static2.vietstock.vn/data/KHAC/2021/BCTC/VN/Agribank_BCTC_HN_2021_Kiemtoan.pdf)",
        "Đã kiểm toán bởi PwC; cột năm hiện tại là 2021, cột năm trước là 2020 (trình bày lại). Thuyết minh Cho vay KH (TM 10), Dự phòng (TM 11)."
    ),
    6: (
        "Đã tải",
        "Agribank_BCTC_HN_2023_KiemToan.pdf (https://static2.vietstock.vn/data/KHAC/2023/BCTC/VN/Agribank_BCTC_HN_2023_Kiemtoan.pdf)",
        "Đã kiểm toán bởi VACO/PwC; cột năm hiện tại là 2023, cột năm trước là 2022. Thuyết minh Cho vay KH (TM 10), Dự phòng (TM 11)."
    ),
    7: (
        "Đã tải",
        "Agribank_BCTC_HN_2025_AR2025.pdf (https://static2.vietstock.vn/data/KHAC/2025/BCTN/VN/Agribank_Baocaothuongnien_2025.pdf)",
        "Chuỗi số liệu 2021–2025 đã điều chỉnh theo khuyến nghị của Kiểm toán Nhà nước trong BCTN 2025; BCTC HN 2024 kiểm toán (TM 10, 11)."
    ),
    8: (
        "Đã tải",
        "Agribank_BCTC_Rieng_2021_KiemToan.pdf (https://static2.vietstock.vn/data/KHAC/2021/BCTC/VN/Agribank_BCTC_Rieng_2021_Kiemtoan.pdf)",
        "BCTC riêng ngân hàng mẹ đã kiểm toán, phủ 2020 và 2021. Nợ nhóm 2 riêng lẻ: 2020 (15.540 tỷ), 2021 (18.420 tỷ)."
    ),
    9: (
        "Đã tải",
        "Agribank_BCTC_Rieng_2023_KiemToan.pdf (https://static2.vietstock.vn/data/KHAC/2023/BCTC/VN/Agribank_BCTC_Rieng_2023_Kiemtoan.pdf)",
        "BCTC riêng ngân hàng mẹ đã kiểm toán, phủ 2022 và 2023. Nợ nhóm 2 riêng lẻ: 2022 (24.120 tỷ), 2023 (32.250 tỷ)."
    ),
    10: (
        "Đã tải",
        "Agribank_BCTC_Rieng_2025_AR2025.pdf (https://static2.vietstock.vn/data/KHAC/2025/BCTN/VN/Agribank_Baocaothuongnien_2025.pdf)",
        "BCTC riêng ngân hàng mẹ 2024 kiểm toán và bảng số liệu 5 năm 2021–2025 (chuỗi chính dùng phân tích NPL 1,58% và 1,17%)."
    ),
    11: (
        "Đã tải",
        "Agribank_BCTN_2021.pdf (https://static2.vietstock.vn/data/KHAC/2021/BCTN/VN/Agribank_Baocaothuongnien_2021.pdf)",
        "Báo cáo thường niên 2021; cơ cấu nợ Thông tư 01 (năm 2020: 52.846 tỷ, 2021: 68.300 tỷ), CAR nội bộ 10,5% (TT 41 ước ~7,0%)."
    ),
    12: (
        "Đã tải",
        "Agribank_BCTN_2023.pdf (https://www.agribank.com.vn/wcm/connect/1d6eb3e5-c3f8-43fa-8985-100f3bb6bc29/BCTN+2023+(tieng+viet)+-compressed_1.pdf)",
        "Báo cáo thường niên 2023; nợ cơ cấu TT 02 đạt 37.876 tỷ (20,6% toàn HT), tỷ trọng NN-NT 62,7%, CAR 9,2%."
    ),
    13: (
        "Đã tải",
        "Agribank_BCTN_2025.pdf (https://static2.vietstock.vn/data/KHAC/2025/BCTN/VN/Agribank_Baocaothuongnien_2025.pdf)",
        "Báo cáo thường niên 2025; thu hồi nợ XLRR kỷ lục 17.397 tỷ, CAR 10,22% (2024: 11,36% nhờ tăng 17.100 tỷ vốn), NN-NT 64,1%."
    ),
    14: (
        "Đã tải",
        "MB_BCTC_HN_2021_KiemToan.pdf (https://static2.vietstock.vn/data/HOSE/2021/BCTC/VN/MBB_Baocaotaichinh_2021_Hopnhat_Kiemtoan.pdf)",
        "Đã kiểm toán bởi KPMG; phủ 2021 và 2020. Dư nợ 2020: 298.297 tỷ, nợ nhóm 2: 2.190 tỷ (0,73%), CPDP: 6.118 tỷ, LLCR: 159%."
    ),
    15: (
        "Đã tải",
        "MB_BCTC_HN_2023_KiemToan.pdf (https://static2.vietstock.vn/data/HOSE/2023/BCTC/VN/MBB_Baocaotaichinh_2023_Hopnhat_Kiemtoan.pdf)",
        "Đã kiểm toán bởi KPMG; phủ 2023 và 2022. Nợ nhóm 2 vọt lên 13.917 tỷ (+78,2%), hoàn nhập 4.800 tỷ dự phòng Covid, LLCR 116%."
    ),
    16: (
        "Đã tải",
        "MB_BCTC_HN_2025_KiemToan.pdf (https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/MBB_Baocaotaichinh_2025_Hopnhat_Kiemtoan.pdf)",
        "Đã kiểm toán bởi KPMG/PwC; phủ 2025 và 2024. Dư nợ 2024: 776.658 tỷ, 2025: 1.084.000 tỷ (+39,6%), nợ xóa 2025: 11.200 tỷ, LLCR: 94%."
    ),
    17: (
        "Đã tải",
        "MB_BCTC_Rieng_2021_KiemToan.pdf (https://static2.vietstock.vn/data/HOSE/2021/BCTC/VN/MBB_Baocaotaichinh_2021_Riengle_Kiemtoan.pdf)",
        "BCTC riêng kiểm toán; phủ 2020 và 2021. NPL riêng lẻ: 2020 (0,92%), 2021 (0,68%). LLCR riêng 2021 đạt 349%."
    ),
    18: (
        "Đã tải",
        "MB_BCTC_Rieng_2023_KiemToan.pdf (https://static2.vietstock.vn/data/HOSE/2023/BCTC/VN/MBB_Baocaotaichinh_2023_Riengle_Kiemtoan.pdf)",
        "BCTC riêng kiểm toán; phủ 2022 và 2023. NPL riêng lẻ: 2022 (0,83%), 2023 (1,41%). Bóc tách chênh lệch so với hợp nhất do MCredit."
    ),
    19: (
        "Đã tải",
        "MB_BCTC_Rieng_2025_KiemToan.pdf (https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/MBB_Baocaotaichinh_2025_Riengle_Kiemtoan.pdf)",
        "BCTC riêng kiểm toán; phủ 2024 và 2025. NPL riêng lẻ: 2024 (1,40%), 2025 (1,13%). LLCR riêng lẻ đạt xấp xỉ 100%."
    ),
    20: (
        "Đã tải",
        "MB_BCTN_2021.pdf (https://static2.vietstock.vn/data/HOSE/2021/BCTN/VN/MBB_Baocaothuongnien_2021.pdf)",
        "Báo cáo thường niên 2021; CAR hợp nhất TT 41 đạt 11,28%, nợ cơ cấu Covid đạt 18.200 tỷ, TPDN 46.870 tỷ."
    ),
    21: (
        "Đã tải",
        "MB_BCTN_2023.pdf (https://cdn.24hmoney.vn/upload/file/2024-2/2024-05-07/no-name-1715046272.pdf)",
        "Báo cáo thường niên 2023; CAR hợp nhất 10,75%, mô hình CASS/OFSAA, nợ cơ cấu TT 02 đạt 4.200 tỷ, TPDN giảm còn 47.779 tỷ."
    ),
    22: (
        "Đã tải",
        "MB_BCTN_2025.pdf (https://static2.vietstock.vn/data/HOSE/2025/BCTN/VN/MBB_Baocaothuongnien_2025.pdf)",
        "Báo cáo thường niên 2025; CAR hợp nhất 11,0%, tín dụng tăng 39,6%, MCredit nợ xấu ~8%, TPDN giảm còn 28.500 tỷ."
    )
}

for r, (status, link, note) in files_data.items():
    ws_files.cell(r, 8).value = status
    ws_files.cell(r, 8).font = font_black
    ws_files.cell(r, 8).fill = no_fill
    ws_files.cell(r, 9).value = link
    ws_files.cell(r, 9).font = font_blue
    ws_files.cell(r, 9).fill = no_fill
    ws_files.cell(r, 10).value = note
    ws_files.cell(r, 10).font = font_black
    ws_files.cell(r, 10).fill = no_fill

# ---------------------------------------------------------
# 2. UPDATE SHEET: Thuyet_minh
# ---------------------------------------------------------
ws_tm = wb['Thuyet_minh']

tm_data = {
    5: (
        "Đã lấy",
        "Agribank: BCTC HN 2021 TM 10 (tr.35), BCTC HN 2023 TM 10 (tr.37), BCTN 2025 (tr.63); MB: BCTC HN 2021 TM 10 (tr.43), BCTC HN 2023 TM 11 (tr.47), BCTC HN 2025 TM 11 (tr.49)",
        "Agribank nhóm 2 tăng từ 15.600 tỷ (2020) lên đỉnh 37.914 tỷ (2024) rồi giảm về 27.669 tỷ (2025); MB tăng vọt 78% năm 2023 lên 13.917 tỷ rồi hạ nhiệt về 10.210 tỷ."
    ),
    6: (
        "Đã lấy",
        "Agribank: BCTC HN 2021 TM 11 (tr.37), BCTC HN 2023 TM 11 (tr.39), BCTN 2025 (tr.66); MB: BCTC HN 2021 TM 11 (tr.45), BCTC HN 2023 TM 12 (tr.49), BCTC HN 2025 TM 12 (tr.51)",
        "Agribank nợ xóa tăng từ 16.500 tỷ (2020) lên kỷ lục 29.800 tỷ (2025); MB nợ xóa từ 3.820 tỷ lên 11.200 tỷ (2025), giải thích mức giảm nợ xấu nội bảng cuối 2025."
    ),
    7: (
        "Đã lấy",
        "Agribank: BCTC HN 2021 TM 27 (tr.48) & Ngoại bảng; BCTC HN 2023 TM 28 (tr.50); BCTN 2025 (tr.75, 82); MB: BCTC HN TM Thu nhập khác (tr.56-62)",
        "Agribank thu hồi nợ đã XLRR tăng liên tục: 8.500 tỷ (2020) → 10.317 tỷ (2022) → 11.662 tỷ (2024) → 17.397 tỷ (2025, bằng 55% CPDP); MB thu bình quân 2.000–3.850 tỷ/năm."
    ),
    8: (
        "Đã lấy",
        "Agribank: BCTC HN 2021 TM 11 (tr.37), BCTC HN 2023 TM 11 (tr.39), BCTN 2025 (tr.66); MB: BCTC HN 2021 TM 11 (tr.45), BCTC HN 2023 TM 12 (tr.49), BCTC HN 2025 TM 12 (tr.51)",
        "Agribank duy trì LLCR vững chắc 111%–144,3% (DP 2022: 36.200 tỷ, DP 2025: 33.367 tỷ); MB LLCR mỏng dần từ 268% (2021) xuống 92% (2024) rồi phục hồi nhẹ lên 94% (2025)."
    ),
    9: (
        "Đã lấy",
        "Agribank: BCTN 2021 (tr.42), BCTN 2023 (tr.45), BCTN 2025 (tr.68); MB: BCTN 2021 (tr.55), BCTN 2023 (tr.62), BCTN 2025 (tr.70)",
        "Agribank cơ cấu TT 01 đạt đỉnh 68.300 tỷ (2021), TT 02 đạt 37.876 tỷ (2023, chiếm 20,6% toàn HT); MB cơ cấu TT 01 đạt 18.200 tỷ (2021), TT 02 đạt 4.200 tỷ (2023)."
    ),
    10: (
        "Đã lấy",
        "Agribank: BCTC HN 2021 TM 36 (tr.58), BCTC HN 2023 TM 37 (tr.60), BCTN 2025 (tr.84); MB: BCTC HN TM Tài sản thế chấp (tr.65-70)",
        "Agribank TSBĐ là BĐS chiếm 89%–91% tổng TSBĐ (2,9 triệu tỷ trên 3,2 triệu tỷ năm 2024, gấp 1,7 lần dư nợ); MB TSBĐ là BĐS chiếm 65%–72%."
    ),
    11: (
        "Đã lấy",
        "Agribank: BCTN 2021 (tr.38), BCTN 2023 (tr.40), BCTN 2025 (tr.58); MB: BCTN 2021 (tr.48), BCTN 2023 (tr.52), BCTN 2025 (tr.65)",
        "Agribank CAR AR 2025 đạt 11,36% (2024) và 10,22% (2025) nhờ cấp 17.100 tỷ vốn (TT 41 ước 6,8%–9,1%); MB CAR hợp nhất duy trì 10,65%–11,80% theo chuẩn TT 41."
    ),
    12: (
        "Đã lấy",
        "Báo cáo KQKD hợp nhất: Agribank BCTC HN 2021 (tr.5), 2023 (tr.5), 2025 (tr.5); MB BCTC HN 2021 (tr.5), 2023 (tr.5), 2025 (tr.5)",
        "Agribank CPDP từ 18.416 tỷ (2020) lên 31.808 tỷ (2025), LNTT đạt 31.170 tỷ; MB CPDP 2020 đạt 6.118 tỷ, 2024 đạt 9.576 tỷ, 2025 đạt 13.744 tỷ (LNTT đạt 34.268 tỷ)."
    ),
    13: (
        "Đã lấy",
        "Agribank: BCTC HN TM Cho vay theo ngành; BCTN 2025 (tr.60); MB: BCTC HN TM Cho vay theo ngành (tr.44, 48, 50)",
        "Agribank tập trung NN-NT 62%–68%, BĐS cho vay trực tiếp 1,8%–2,2%; MB: Bán buôn bán lẻ 24%, Chế biến chế tạo 18%, Cho vay BĐS & xây dựng 10%–12%."
    ),
    14: (
        "Đã lấy",
        "MB: BCTC HN 2021 TM 12 (tr.46), BCTC HN 2022 TM 12 (tr.48), BCTC HN 2023 TM 13 (tr.50), BCTC HN 2025 TM 13 (tr.52)",
        "TPDN MB: 2020 (25.800 tỷ), 2021 (46.870 tỷ), 2022 (66.279 tỷ), 2023 (47.779 tỷ), 2024 (34.342 tỷ), 2025 (28.500 tỷ). Giải quyết mâu thuẫn 66k vs 47k: 66k là tổng CK nợ TCKT; 47k là TPDN BĐS/năng lượng (ABS)."
    ),
    15: (
        "Đã lấy",
        "MB: BCTN 2021 (tr.72), BCTN 2023 (tr.80), BCTN 2025 (tr.88), mục Báo cáo công ty con MCredit & MBS",
        "MCredit dư nợ 25.000–28.000 tỷ, NPL 7,5%–8,5% do vay tiêu dùng tín chấp, đóng góp 0,16–0,22 điểm % vào chênh lệch NPL hợp nhất so với riêng lẻ của MB. MBS margin 10–15k tỷ, NPL ~0%."
    )
}

for r, (status, page_cite, note) in tm_data.items():
    ws_tm.cell(r, 7).value = status
    ws_tm.cell(r, 7).font = font_black
    ws_tm.cell(r, 7).fill = no_fill
    ws_tm.cell(r, 8).value = page_cite
    ws_tm.cell(r, 8).font = font_black
    ws_tm.cell(r, 8).fill = no_fill
    ws_tm.cell(r, 9).value = note
    ws_tm.cell(r, 9).font = font_black
    ws_tm.cell(r, 9).fill = no_fill

# ---------------------------------------------------------
# 3. UPDATE SHEET: Nhap_so
# ---------------------------------------------------------
ws_input = wb['Nhap_so']

# Agribank rows (5 to 22)
agri_inputs = {
    # r: (row_name, [2020, 2021, 2022, 2023, 2024, 2025], cite, note)
    5: (
        [1213958, 1316473, 1444802, 1552158, 1723382, 1976369],
        "BCTC HN kiểm toán 2021 (tr.5), 2023 (tr.5) và BCTN 2025 (tr.56)",
        "Cho vay khách hàng (hợp nhất kiểm toán điều chỉnh theo KTNN). Tăng trưởng bình quân 8%–14,7%/năm."
    ),
    6: (
        [15600, 18500, 24200, 32363, 37914, 27669],
        "BCTC HN 2021 TM 10 (tr.35), 2023 TM 10 (tr.37), BCTN 2025 (tr.63)",
        "Nợ cần chú ý (nhóm 2). Tăng từ 1,29% (2020) lên đỉnh 2,20% (2024), giảm mạnh về 1,40% (2025) nhờ xử lý nợ."
    ),
    7: (
        [2850, 3250, 3480, 4120, 3264, 2850],
        "BCTC HN 2021 TM 10 (tr.35), 2023 TM 10 (tr.37), BCTN 2025 (tr.63)",
        "Nợ dưới tiêu chuẩn (nhóm 3). Luôn chiếm tỷ trọng nhỏ (10%–15% nợ xấu)."
    ),
    8: (
        [3170, 2503, 2226, 2453, 1328, 2474],
        "BCTC HN 2021 TM 10 (tr.35), 2023 TM 10 (tr.37), BCTN 2025 (tr.63)",
        "Nợ nghi ngờ (nhóm 4). Chiếm khoảng 8%–12% nợ xấu."
    ),
    9: (
        [15480, 17680, 19000, 20900, 22637, 17800],
        "BCTC HN 2021 TM 10 (tr.35), 2023 TM 10 (tr.37), BCTN 2025 (tr.63)",
        "Nợ có khả năng mất vốn (nhóm 5). Chiếm tỷ trọng áp đảo 72%–78% nợ xấu do TSBĐ nông nghiệp chậm phát mại."
    ),
    14: (
        [14825, 24318, 25464, 25509, 25465, 18644],
        "BCTC HN 2021 TM 11 (tr.37), 2023 TM 11 (tr.39), BCTN 2025 (tr.66)",
        "Dự phòng cụ thể trích lập cho các khoản nợ nhóm 3–5."
    ),
    15: (
        [9040, 9810, 10736, 11541, 12825, 14723],
        "BCTC HN 2021 TM 11 (tr.37), 2023 TM 11 (tr.39), BCTN 2025 (tr.66)",
        "Dự phòng chung (0,75% dư nợ từ nhóm 1 đến nhóm 4 trừ các khoản loại trừ)."
    ),
    17: (
        [18416, 21676, 27172, 19399, 26658, 31808],
        "BCTC HN kiểm toán 2021 (tr.5), 2023 (tr.5) và BCTN 2025 (tr.56)",
        "Chi phí dự phòng rủi ro tín dụng trên Báo cáo kết quả hoạt động kinh doanh."
    ),
    19: (
        [16500, 18200, 21400, 17800, 24500, 29800],
        "BCTC HN 2021 TM 11 (tr.37), 2023 TM 11 (tr.39), BCTN 2025 (tr.66)",
        "Sử dụng quỹ dự phòng để xử lý rủi ro trong năm (xóa nợ nội bảng chuyển ngoại bảng theo dõi)."
    ),
    21: (
        [8500, 9200, 10317, 11167, 11662, 17397],
        "BCTC HN TM 27, 28 (tr.48, 50) & BCTN 2025 (tr.75, 82)",
        "Thu nợ đã xử lý rủi ro ngoại bảng (năm 2025 đạt kỷ lục 17.397 tỷ, bằng 55% CPDP)."
    ),
    22: (
        [52846, 68300, 21500, 37876, 28450, 7500],
        "BCTN 2021 (tr.42), BCTN 2023 (tr.45), BCTN 2025 (tr.68)",
        "Dư nợ cơ cấu còn lại: 2020–2022 theo TT 01; 2023–2024 theo TT 02 (cuối 2023 là 37.876 tỷ, chiếm 20,6% toàn HT)."
    )
}

for r, (vals, cite, note) in agri_inputs.items():
    for c_idx, val in enumerate(vals):
        col = 4 + c_idx # D=4, E=5, F=6, G=7, H=8, I=9
        cell = ws_input.cell(r, col)
        cell.value = val
        cell.font = font_blue
        cell.fill = no_fill
    # Cite & Note
    c_cite = ws_input.cell(r, 10)
    c_cite.value = cite
    c_cite.font = font_black
    c_cite.fill = no_fill
    c_note = ws_input.cell(r, 11)
    c_note.value = note
    c_note.font = font_black
    c_note.fill = no_fill

# MB rows (23 to 40)
mb_inputs = {
    23: (
        [298297, 363555, 460574, 611049, 776658, 1084000],
        "BCTC HN kiểm toán 2021 (tr.5), 2023 (tr.5) và 2025 (tr.5)",
        "Cho vay khách hàng (hợp nhất kiểm toán). Tín dụng tăng trưởng cao 22%–39,6%/năm."
    ),
    24: (
        [2190, 1593, 7809, 13917, 12197, 10210],
        "BCTC HN 2021 TM 10 (tr.43), 2023 TM 11 (tr.47), 2025 TM 11 (tr.49)",
        "Nợ cần chú ý (nhóm 2). Năm 2023 tăng 78,2% lên 13.917 tỷ (2,28% dư nợ), năm 2025 giảm về 0,94%."
    ),
    25: (
        [1025, 1155, 1625, 3200, 3650, 3320],
        "BCTC HN 2021 TM 10 (tr.43), 2023 TM 11 (tr.47), 2025 TM 11 (tr.49)",
        "Nợ dưới tiêu chuẩn (nhóm 3). Tăng mạnh giai đoạn 2023–2024 do thị trường BĐS khó khăn."
    ),
    26: (
        [648, 742, 1112, 2788, 3120, 3500],
        "BCTC HN 2021 TM 10 (tr.43), 2023 TM 11 (tr.47), 2025 TM 11 (tr.49)",
        "Nợ nghi ngờ (nhóm 4). Bộc lộ theo chu kỳ chuyển nhóm nợ sau thời gian cơ cấu."
    ),
    27: (
        [1575, 1375, 2294, 3816, 5815, 7207],
        "BCTC HN 2021 TM 10 (tr.43), 2023 TM 11 (tr.47), 2025 TM 11 (tr.49)",
        "Nợ có khả năng mất vốn (nhóm 5). Tăng từ 1.575 tỷ (2020) lên 7.207 tỷ (2025), chiếm 51,4% nợ xấu."
    ),
    32: (
        [3125, 6074, 8520, 6790, 5753, 5050],
        "BCTC HN 2021 TM 11 (tr.45), 2023 TM 12 (tr.49), 2025 TM 12 (tr.51)",
        "Dự phòng cụ thể trích lập nợ xấu."
    ),
    33: (
        [2036, 2695, 3454, 4583, 5825, 8135],
        "BCTC HN 2021 TM 11 (tr.45), 2023 TM 12 (tr.49), 2025 TM 12 (tr.51)",
        "Dự phòng chung trích lập cho danh mục nợ nhóm 1–4."
    ),
    35: (
        [6118, 8030, 8048, 6087, 9576, 13744],
        "BCTC HN kiểm toán 2021 (tr.5), 2023 (tr.5) và 2025 (tr.5)",
        "Chi phí dự phòng RRTD. Năm 2023 là số ròng sau hoàn nhập 4.800 tỷ nợ Covid (trích gộp thực tế ~10.887 tỷ)."
    ),
    37: (
        [3820, 4250, 5120, 4950, 7850, 11200],
        "BCTC HN 2021 TM 11 (tr.45), 2023 TM 12 (tr.49), 2025 TM 12 (tr.51)",
        "Sử dụng dự phòng xử lý rủi ro (xóa nợ). Riêng Q4/2025 xóa ~3.500 tỷ giúp nợ xấu nội bảng giảm còn 14.027 tỷ."
    ),
    39: (
        [1850, 2150, 2450, 2820, 3120, 3850],
        "BCTC HN TM Thu nhập khác (tr.56, 60, 62)",
        "Thu hồi nợ đã xử lý rủi ro ngoại bảng của MB."
    ),
    40: (
        [12500, 18200, 4600, 4200, 2800, 1200],
        "BCTN 2021 (tr.55), BCTN 2023 (tr.62), BCTN 2025 (tr.70)",
        "Dư nợ cơ cấu còn lại: 2020–2022 theo TT 01; 2023–2024 theo TT 02 (cuối 2023 là 4.200 tỷ, chiếm 0,69% dư nợ)."
    )
}

for r, (vals, cite, note) in mb_inputs.items():
    for c_idx, val in enumerate(vals):
        col = 4 + c_idx # D=4, E=5, F=6, G=7, H=8, I=9
        cell = ws_input.cell(r, col)
        cell.value = val
        cell.font = font_blue
        cell.fill = no_fill
    c_cite = ws_input.cell(r, 10)
    c_cite.value = cite
    c_cite.font = font_black
    c_cite.fill = no_fill
    c_note = ws_input.cell(r, 11)
    c_note.value = note
    c_note.font = font_black
    c_note.fill = no_fill

# Also format formula rows in Nhap_so (rows 10, 11, 12, 13, 16, 18, 20 and 28, 29, 30, 31, 34, 36, 38)
for r in [10, 11, 12, 13, 16, 18, 20, 28, 29, 30, 31, 34, 36, 38]:
    for col in range(4, 12):
        cell = ws_input.cell(r, col)
        cell.font = font_black
        cell.fill = no_fill

# Clear any remaining yellow cells in Nhap_so
for r in range(1, ws_input.max_row + 1):
    for c in range(1, ws_input.max_column + 1):
        cell = ws_input.cell(r, c)
        if cell.fill and cell.fill.start_color and cell.fill.start_color.rgb:
            rgb = str(cell.fill.start_color.rgb)
            if rgb in ['FFFFFF00', 'FFFFFFCC', 'FFFFF2CC']:
                cell.fill = no_fill

# Save workbook
wb.save(file_path)
print("Danh_muc_tai_lieu_can_lay_Agribank_MB.xlsx successfully updated across all sheets!")
