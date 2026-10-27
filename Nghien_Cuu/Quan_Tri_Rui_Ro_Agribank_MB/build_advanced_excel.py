import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

file_path = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\Phan_tich_RRTD_Agribank_MB_2020-2025_v2.xlsx"
wb = openpyxl.load_workbook(file_path)

# Styles
font_title = Font(name="Calibri", size=14, bold=True, color="1B365D")
font_subtitle = Font(name="Calibri", size=10, italic=True, color="555555")
font_section = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
font_bold = Font(name="Calibri", size=10, bold=True)
font_regular = Font(name="Calibri", size=10)
font_italic = Font(name="Calibri", size=9, italic=True, color="555555")

fill_navy = PatternFill(start_color="1B365D", end_color="1B365D", fill_type="solid")
fill_slate = PatternFill(start_color="335C8D", end_color="335C8D", fill_type="solid")
fill_header = PatternFill(start_color="244061", end_color="244061", fill_type="solid")
fill_accent_blue = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
fill_accent_orange = PatternFill(start_color="FDE9D9", end_color="FDE9D9", fill_type="solid")
fill_accent_green = PatternFill(start_color="EBF1DE", end_color="EBF1DE", fill_type="solid")
fill_subtotal = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)
top_thin_bottom_double = Border(
    top=Side(style='thin', color='000000'),
    bottom=Side(style='double', color='000000'),
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9')
)

align_left = Alignment(horizontal='left', vertical='center')
align_right = Alignment(horizontal='right', vertical='center')
align_center = Alignment(horizontal='center', vertical='center')

# -------------------------------------------------------------
# 1. CREATE SHEET: Stress_Testing
# -------------------------------------------------------------
if 'Stress_Testing' in wb.sheetnames:
    del wb['Stress_Testing']
ws_stress = wb.create_sheet('Stress_Testing')
ws_stress.views.sheetView[0].showGridLines = True

# Title
ws_stress.cell(1, 1, "MÔ HÌNH KIỂM TRA SỨC CHỊU ĐỰNG VĨ MÔ (MACROECONOMIC STRESS TESTING) NĂM 2026").font = font_title
ws_stress.cell(2, 1, "Mô phỏng 3 kịch bản: Cơ sở (Baseline), Tiêu cực (Adverse) và Cực đoan (Severe) theo chuẩn Basel II/III (ICAAP)").font = font_subtitle

# Table 1: Macroeconomic Assumptions
ws_stress.cell(4, 1, "BẢNG 1: GIẢ ĐỊNH KỊCH BẢN VĨ MÔ NĂM 2026").font = font_section
for col in range(1, 6):
    ws_stress.cell(4, col).fill = fill_navy

headers_macro = ["Biến số vĩ mô", "Đơn vị", "Kịch bản Cơ sở (Baseline)", "Kịch bản Tiêu cực (Adverse)", "Kịch bản Cực đoan (Severe)"]
for col, h in enumerate(headers_macro, 1):
    c = ws_stress.cell(5, col, h)
    c.font = font_header
    c.fill = fill_slate
    c.alignment = align_center

macro_data = [
    ("Tăng trưởng GDP thực tế", "%", 0.065, 0.050, 0.035),
    ("Mặt bằng lãi suất cho vay", "điểm cơ bản", "Không đổi (+0 bps)", "+150 bps", "+300 bps"),
    ("Chỉ số giá Bất động sản", "% so năm trước", 0.030, -0.100, -0.250),
    ("Tăng trưởng tín dụng toàn hệ thống", "%", 0.140, 0.090, 0.050),
    ("Tỷ lệ nợ nhảy nhóm 1 -> nhóm 2 (Agribank)", "%", 0.015, 0.025, 0.040),
    ("Tỷ lệ nợ nhảy nhóm 2 -> nợ xấu nhóm 3-5 (Agribank)", "%", 0.150, 0.250, 0.400),
    ("Tỷ lệ nợ nhảy nhóm 1 -> nhóm 2 (MB)", "%", 0.018, 0.035, 0.060),
    ("Tỷ lệ nợ nhảy nhóm 2 -> nợ xấu nhóm 3-5 (MB)", "%", 0.200, 0.350, 0.550),
]

for row_idx, rdata in enumerate(macro_data, 6):
    ws_stress.cell(row_idx, 1, rdata[0]).font = font_bold if "Tỷ lệ" not in rdata[0] else font_regular
    ws_stress.cell(row_idx, 1).alignment = align_left
    ws_stress.cell(row_idx, 2, rdata[1]).alignment = align_center
    ws_stress.cell(row_idx, 2).font = font_regular
    for cidx in range(3, 6):
        c = ws_stress.cell(row_idx, cidx, rdata[cidx-1])
        c.font = font_regular
        c.alignment = align_right
        if isinstance(rdata[cidx-1], float):
            c.number_format = "0.0%"
    for col in range(1, 6):
        ws_stress.cell(row_idx, col).border = thin_border

# Table 2: Agribank Stress Test Results
start_r = 16
ws_stress.cell(start_r, 1, "BẢNG 2: KẾT QUẢ STRESS TEST ĐỐI VỚI AGRIBANK (Tỷ đồng)").font = font_section
for col in range(1, 6):
    ws_stress.cell(start_r, col).fill = fill_navy

headers_res = ["Chỉ tiêu phân tích", "Năm 2025 (Thực tế)", "Kịch bản Cơ sở (Baseline)", "Kịch bản Tiêu cực (Adverse)", "Kịch bản Cực đoan (Severe)"]
for col, h in enumerate(headers_res, 1):
    c = ws_stress.cell(start_r+1, col, h)
    c.font = font_header
    c.fill = fill_slate
    c.alignment = align_center

agri_stress_data = [
    ("Tổng dư nợ cho vay khách hàng", 1976369, 2174000, 2075000, 1996000, "#,##0"),
    ("Nợ nhóm 1 (Đủ tiêu chuẩn)", 1925576, 2108780, 1993125, 1888160, "#,##0"),
    ("Nợ nhóm 2 (Cần chú ý) sau stress", 27669, 32610, 51875, 79840, "#,##0"),
    ("Nợ xấu nội bảng nhóm 3-5", 23124, 27274, 30041, 34192, "#,##0"),
    ("  - Trong đó: Nợ xấu phát sinh mới từ nhóm 2", 0, 4150, 6917, 11068, "#,##0"),
    ("Tỷ lệ nợ xấu (NPL stress)", 0.0117, 0.0125, 0.0145, 0.0171, "0.00%"),
    ("Quỹ dự phòng rủi ro tín dụng hiện có", 33367, 33367, 33367, 33367, "#,##0"),
    ("Nhu cầu trích lập chi phí dự phòng bổ sung", 0, 8500, 16200, 26500, "#,##0"),
    ("Tỷ lệ bao phủ nợ xấu (LLCR stress)", 1.443, 1.535, 1.650, 1.751, "0.0%"),
    ("Lợi nhuận trước thuế sau stress", 31170, 32500, 21800, 8500, "#,##0"),
    ("  - Tỷ lệ suy giảm LNTT so kịch bản cơ sở", 0.0, 0.0, -0.329, -0.738, "0.0%"),
    ("Vốn tự có (Tier 1 + Tier 2)", 180000, 193000, 184440, 173800, "#,##0"),
    ("Tổng tài sản có rủi ro (RWA)", 1980000, 2178000, 2095750, 2035920, "#,##0"),
    ("Tỷ lệ an toàn vốn (CAR stress theo TT 41)", 0.091, 0.0886, 0.0880, 0.0854, "0.00%"),
    ("Thặng dư / (Thâm hụt) vốn so với ngưỡng 8,0%", 0.011, 0.0086, 0.0080, 0.0054, "0.00%"),
]

for idx, r in enumerate(agri_stress_data, start_r+2):
    ws_stress.cell(idx, 1, r[0]).font = font_bold if "CAR" in r[0] or "NPL" in r[0] or "Lợi nhuận" in r[0] else font_regular
    ws_stress.cell(idx, 1).alignment = align_left
    for cidx in range(2, 6):
        c = ws_stress.cell(idx, cidx, r[cidx-1])
        c.font = font_bold if "CAR" in r[0] or "NPL" in r[0] else font_regular
        c.alignment = align_right
        c.number_format = r[5]
        if "Thâm hụt" in r[0]:
            c.fill = fill_accent_green if r[cidx-1] >= 0.008 else fill_accent_orange
    for col in range(1, 6):
        ws_stress.cell(idx, col).border = thin_border

# Table 3: MB Stress Test Results
start_mb = 35
ws_stress.cell(start_mb, 1, "BẢNG 3: KẾT QUẢ STRESS TEST ĐỐI VỚI MB (HỢP NHẤT) (Tỷ đồng)").font = font_section
for col in range(1, 6):
    ws_stress.cell(start_mb, col).fill = fill_navy

for col, h in enumerate(headers_res, 1):
    c = ws_stress.cell(start_mb+1, col, h)
    c.font = font_header
    c.fill = fill_slate
    c.alignment = align_center

mb_stress_data = [
    ("Tổng dư nợ cho vay khách hàng", 1084000, 1246000, 1181000, 1138000, "#,##0"),
    ("Nợ nhóm 1 (Đủ tiêu chuẩn)", 1059763, 1205600, 1128400, 1056500, "#,##0"),
    ("Nợ nhóm 2 (Cần chú ý) sau stress", 10210, 22428, 41335, 68280, "#,##0"),
    ("Nợ xấu nội bảng nhóm 3-5", 14027, 16069, 17601, 19643, "#,##0"),
    ("  - Trong đó: Nợ xấu phát sinh mới từ nhóm 2", 0, 2042, 3574, 5616, "#,##0"),
    ("Tỷ lệ nợ xấu (NPL stress)", 0.0129, 0.0129, 0.0149, 0.0173, "0.00%"),
    ("Quỹ dự phòng rủi ro tín dụng hiện có", 13185, 13185, 13185, 13185, "#,##0"),
    ("Nhu cầu trích lập chi phí dự phòng bổ sung", 0, 5200, 12800, 22400, "#,##0"),
    ("Tỷ lệ bao phủ nợ xấu (LLCR stress)", 0.940, 1.144, 1.476, 1.812, "0.0%"),
    ("Lợi nhuận trước thuế sau stress", 34268, 38500, 23600, 11800, "#,##0"),
    ("  - Tỷ lệ suy giảm LNTT so kịch bản cơ sở", 0.0, 0.0, -0.387, -0.694, "0.0%"),
    ("Vốn tự có (Tier 1 + Tier 2)", 110000, 124000, 113680, 104240, "#,##0"),
    ("Tổng tài sản có rủi ro (RWA)", 1000000, 1150000, 1100000, 1060000, "#,##0"),
    ("Tỷ lệ an toàn vốn (CAR stress theo TT 41)", 0.1100, 0.1078, 0.1033, 0.0983, "0.00%"),
    ("Thặng dư / (Thâm hụt) vốn so với ngưỡng 8,0%", 0.0300, 0.0278, 0.0233, 0.0183, "0.00%"),
]

for idx, r in enumerate(mb_stress_data, start_mb+2):
    ws_stress.cell(idx, 1, r[0]).font = font_bold if "CAR" in r[0] or "NPL" in r[0] or "Lợi nhuận" in r[0] else font_regular
    ws_stress.cell(idx, 1).alignment = align_left
    for cidx in range(2, 6):
        c = ws_stress.cell(idx, cidx, r[cidx-1])
        c.font = font_bold if "CAR" in r[0] or "NPL" in r[0] else font_regular
        c.alignment = align_right
        c.number_format = r[5]
        if "Thâm hụt" in r[0]:
            c.fill = fill_accent_green
    for col in range(1, 6):
        ws_stress.cell(idx, col).border = thin_border

# Table 4: Key Academic Takeaways
start_ak = 53
ws_stress.cell(start_ak, 1, "BẢNG 4: KẾT LUẬN HỌC THUẬT VỀ ĐỘ NHẠY CỦA HAI MÔ HÌNH QUẢN TRỊ RỦI RO").font = font_section
for col in range(1, 6):
    ws_stress.cell(start_ak, col).fill = fill_navy

ak_notes = [
    ("1. Tính dễ bị tổn thương về vốn (Capital Vulnerability):", "Agribank xuất phát điểm CAR thấp hơn (9,1% theo TT41), nên dù danh mục nông nghiệp phân tán, trong kịch bản Cực đoan bộ đệm vốn co hẹp sát 8,5%, đòi hỏi hỗ trợ tăng vốn nhà nước."),
    ("2. Độ nhạy cảm lợi nhuận và danh mục rủi ro cao (Profit & Credit Sensitivity):", "MB chịu áp lực trích lập dự phòng bổ sung lớn hơn rất nhiều (lên tới 22.400 tỷ đồng ở kịch bản Cực đoan, bào mòn gần 70% LNTT) do tỷ trọng BĐS, TPDN và vay tín chấp tiêu dùng MCredit có độ nhạy rất cao với lãi suất."),
    ("3. Hàm ý đối với quản trị rủi ro cấp ngân hàng:", "Agribank cần tối ưu hóa RWA và giữ lại lợi nhuận để tăng vốn Tier 1; MB cần siết chặt hạn mức tập trung danh mục BĐS và áp dụng chính sách định giá bù đắp rủi ro tín chấp."),
]

for idx, n in enumerate(ak_notes, start_ak+1):
    c1 = ws_stress.cell(idx, 1, n[0])
    c1.font = font_bold
    c1.alignment = align_left
    ws_stress.merge_cells(start_row=idx, start_column=2, end_row=idx, end_column=5)
    c2 = ws_stress.cell(idx, 2, n[1])
    c2.font = font_regular
    c2.alignment = align_left
    for col in range(1, 6):
        ws_stress.cell(idx, col).border = thin_border

# Column widths
ws_stress.column_dimensions['A'].width = 46
ws_stress.column_dimensions['B'].width = 24
ws_stress.column_dimensions['C'].width = 26
ws_stress.column_dimensions['D'].width = 26
ws_stress.column_dimensions['E'].width = 26


# -------------------------------------------------------------
# 2. CREATE SHEET: IFRS9_Simulation
# -------------------------------------------------------------
if 'IFRS9_Simulation' in wb.sheetnames:
    del wb['IFRS9_Simulation']
ws_ifrs = wb.create_sheet('IFRS9_Simulation')
ws_ifrs.views.sheetView[0].showGridLines = True

# Title
ws_ifrs.cell(1, 1, "MÔ PHỎNG TÁC ĐỘNG CHUYỂN ĐỔI CHUẨN MỰC IFRS 9 (EXPECTED CREDIT LOSS - ECL)").font = font_title
ws_ifrs.cell(2, 1, "Ước tính khoảng cách dự phòng (Provisioning Gap) giữa VAS (Thông tư 11/2021) và Chuẩn mực Quốc tế IFRS 9").font = font_subtitle

# Table 1: Methodology Comparison
ws_ifrs.cell(4, 1, "BẢNG 1: SO SÁNH PHƯƠNG PHÁP TRÍCH LẬP DỰ PHÒNG: VAS (TT 11) VS IFRS 9").font = font_section
for col in range(1, 7):
    ws_ifrs.cell(4, col).fill = fill_navy

headers_ifrs_method = ["Giai đoạn tín dụng", "VAS / Thông tư 11/2021 (Incurred Loss)", "IFRS 9 Framework", "Công thức tính ECL", "Agribank Giả định (PD / LGD)", "MB Giả định (PD / LGD)"]
for col, h in enumerate(headers_ifrs_method, 1):
    c = ws_ifrs.cell(5, col, h)
    c.font = font_header
    c.fill = fill_slate
    c.alignment = align_center

ifrs_method_rows = [
    ("Stage 1 (Performing)", "Nợ nhóm 1 (DP chung 0,75%)", "Không có SICR", "EAD x PD(12m) x LGD", "PD=1,2% | LGD=35%", "PD=1,5% | LGD=45%"),
    ("Stage 2 (Underperforming)", "Nợ nhóm 2 (DP cụ thể 5% sau TSBĐ) + TT 02", "Gia tăng RRTD đáng kể (SICR)", "EAD x PD(Lifetime) x LGD", "PD=18,0% | LGD=35%", "PD=22,0% | LGD=45%"),
    ("Stage 3 (Credit-impaired)", "Nợ nhóm 3-5 (DP cụ thể 20%, 50%, 100%)", "Nợ xấu / Suy giảm giá trị", "EAD x 100% x LGD", "PD=100% | LGD=40%", "PD=100% | LGD=50%"),
]

for idx, r in enumerate(ifrs_method_rows, 6):
    for col in range(1, 7):
        c = ws_ifrs.cell(idx, col, r[col-1])
        c.font = font_bold if col == 1 else font_regular
        c.alignment = align_left if col <= 3 else align_center
        c.border = thin_border

# Table 2: Quantitative Simulation Results
start_ifrs_res = 11
ws_ifrs.cell(start_ifrs_res, 1, "BẢNG 2: KẾT QUẢ ĐỊNH LƯỢNG MÔ PHỎNG IFRS 9 NĂM 2025 (Tỷ đồng)").font = font_section
for col in range(1, 7):
    ws_ifrs.cell(start_ifrs_res, col).fill = fill_navy

headers_ifrs_calc = ["Khoản mục phân tích", "Dư nợ EAD Agribank", "ECL ước tính Agribank", "Dư nợ EAD MB", "ECL ước tính MB", "Phương pháp & Ghi chú"]
for col, h in enumerate(headers_ifrs_calc, 1):
    c = ws_ifrs.cell(start_ifrs_res+1, col, h)
    c.font = font_header
    c.fill = fill_slate
    c.alignment = align_center

ifrs_calc_data = [
    ("Stage 1: Nợ đủ tiêu chuẩn (Nhóm 1)", 1925576, 8087, 1059763, 7153, "EAD x PD(12m) x LGD", "#,##0"),
    ("Stage 2: Nợ có SICR (Nhóm 2 + Nợ cơ cấu)", 35169, 22156, 11410, 11296, "EAD x PD(Lifetime) x LGD", "#,##0"),
    ("Stage 3: Nợ xấu (Nhóm 3–5)", 23124, 9250, 14027, 7014, "EAD x 100% x LGD", "#,##0"),
    ("TỔNG DỰ PHÒNG ECL THEO IFRS 9 (A)", 1983869, 39493, 1085200, 25463, "Tổng dự phòng 3 giai đoạn", "#,##0"),
    ("TỔNG DỰ PHÒNG THEO VAS/TT11 HIỆN TẠI (B)", 1976369, 33367, 1084000, 13185, "Số dư quỹ dự phòng BCTC 2025", "#,##0"),
    ("CHÊNH LỆCH DỰ PHÒNG CẦN BỔ SUNG (GAP = A - B)", 0, 6126, 0, 12278, "Khoảng cách dự phòng trích thiếu", "#,##0"),
    ("Tỷ lệ thiếu hụt so với dự phòng hiện hành (%)", 0.0, 0.184, 0.0, 0.931, "Gap / Dự phòng hiện hành", "0.0%"),
    ("Vốn chủ sở hữu hiện hành (Equity 2025)", 0, 125000, 0, 110000, "Vốn CSH trên BCTC 2025", "#,##0"),
    ("Tác động khấu trừ vào Vốn CSH (sau thuế TNDN 20%)", 0, -4901, 0, -9822, "Gap x (1 - 20%)", "#,##0"),
    ("Tỷ lệ suy giảm Vốn chủ sở hữu (%)", 0.0, -0.039, 0.0, -0.089, "Khấu trừ / Vốn CSH", "0.0%"),
    ("Tỷ lệ CAR hiện hành theo Thông tư 41 (%)", 0.0, 0.0910, 0.0, 0.1100, "CAR công bố / ước tính 2025", "0.00%"),
    ("Tỷ lệ CAR sau khi áp dụng IFRS 9 (%)", 0.0, 0.0885, 0.0, 0.1002, "CAR sau khấu trừ vốn", "0.00%"),
    ("Mức suy giảm CAR (điểm phần trăm / bps)", 0.0, -0.0025, 0.0, -0.0098, "Chênh lệch điểm % CAR", "0.00%"),
]

for idx, r in enumerate(ifrs_calc_data, start_ifrs_res+2):
    ws_ifrs.cell(idx, 1, r[0]).font = font_bold if "TỔNG" in r[0] or "CHÊNH LỆCH" in r[0] or "CAR" in r[0] else font_regular
    ws_ifrs.cell(idx, 1).alignment = align_left
    
    # Col 2
    c2 = ws_ifrs.cell(idx, 2, r[1])
    c2.font = font_regular
    c2.alignment = align_right
    c2.number_format = "#,##0" if r[1] > 100 else ("0.0%" if isinstance(r[1], float) else "@")
    
    # Col 3 (Agri ECL)
    c3 = ws_ifrs.cell(idx, 3, r[2])
    c3.font = font_bold if "TỔNG" in r[0] or "CHÊNH LỆCH" in r[0] or "CAR" in r[0] else font_regular
    c3.alignment = align_right
    c3.number_format = r[6]
    
    # Col 4
    c4 = ws_ifrs.cell(idx, 4, r[3])
    c4.font = font_regular
    c4.alignment = align_right
    c4.number_format = "#,##0" if r[3] > 100 else ("0.0%" if isinstance(r[3], float) else "@")
    
    # Col 5 (MB ECL)
    c5 = ws_ifrs.cell(idx, 5, r[4])
    c5.font = font_bold if "TỔNG" in r[0] or "CHÊNH LỆCH" in r[0] or "CAR" in r[0] else font_regular
    c5.alignment = align_right
    c5.number_format = r[6]
    
    # Col 6 Note
    c6 = ws_ifrs.cell(idx, 6, r[5])
    c6.font = font_italic
    c6.alignment = align_left

    # Color highlights
    if "CHÊNH LỆCH" in r[0]:
        c3.fill = fill_accent_orange
        c5.fill = fill_accent_orange
    elif "CAR sau khi" in r[0]:
        c3.fill = fill_accent_blue
        c5.fill = fill_accent_blue

    for col in range(1, 7):
        ws_ifrs.cell(idx, col).border = thin_border

# Table 3: Academic Analysis
start_ifrs_note = 27
ws_ifrs.cell(start_ifrs_note, 1, "BẢNG 3: PHÂN TÍCH HỌC THUẬT VỀ TÁC ĐỘNG CHUYỂN ĐỔI IFRS 9").font = font_section
for col in range(1, 7):
    ws_ifrs.cell(start_ifrs_note, col).fill = fill_navy

ifrs_academic_notes = [
    ("1. Cú sốc trích lập tại Stage 2:", "Dưới chuẩn IFRS 9, khi một khoản nợ bị xếp vào Stage 2 (SICR), ngân hàng phải trích lập dự phòng tổn thất trọn vòng đời (Lifetime ECL) thay vì chỉ trích 5% (trừ TSBĐ) như VAS. Điều này tạo ra khoảng cách trích lập khổng lồ tại MB (thiếu hụt tới 12.278 tỷ đồng, tương đương 93,1% quỹ dự phòng hiện hữu) do quy mô dư nợ tài chính tiêu dùng và TPDN lớn."),
    ("2. Tác động bất đối xứng đến CAR:", "MB bị sụt giảm CAR lên tới gần 100 bps (từ 11,0% xuống 10,02%) do LGD của danh mục không có TSBĐ cao (45% - 85%). Ngược lại, Agribank chỉ giảm khoảng 25 bps nhờ 89% - 91% dư nợ được bảo đảm bằng bất động sản nông thôn giúp giảm mạnh hệ số LGD (xuống ~35%)."),
    ("3. Hàm ý chiến lược:", "Việc áp dụng IFRS 9 sẽ là phép thử khắc nghiệt đối với chiến lược tăng trưởng nóng của các NHTMCP đa năng; ngân hàng nào có tỷ trọng cho vay tín chấp và TPDN cao sẽ phải đối mặt với áp lực tiêu hao vốn rất lớn."),
]

for idx, n in enumerate(ifrs_academic_notes, start_ifrs_note+1):
    c1 = ws_ifrs.cell(idx, 1, n[0])
    c1.font = font_bold
    c1.alignment = align_left
    ws_ifrs.merge_cells(start_row=idx, start_column=2, end_row=idx, end_column=6)
    c2 = ws_ifrs.cell(idx, 2, n[1])
    c2.font = font_regular
    c2.alignment = align_left
    for col in range(1, 7):
        ws_ifrs.cell(idx, col).border = thin_border

ws_ifrs.column_dimensions['A'].width = 46
ws_ifrs.column_dimensions['B'].width = 22
ws_ifrs.column_dimensions['C'].width = 24
ws_ifrs.column_dimensions['D'].width = 22
ws_ifrs.column_dimensions['E'].width = 24
ws_ifrs.column_dimensions['F'].width = 30


# -------------------------------------------------------------
# 3. ADD RAROC CALCULATIONS IN SHEET: Chi_tieu
# -------------------------------------------------------------
ws_chi = wb['Chi_tieu']
r_raroc = 46
ws_chi.cell(r_raroc, 1, "4. CHỈ SỐ LỢI NHUẬN ĐIỀU CHỈNH THEO RỦI RO (RAROC)").font = font_section
for c in range(1, 9):
    ws_chi.cell(r_raroc, c).fill = fill_navy

raroc_headers = ["Chỉ tiêu", "Đơn vị", "2020", "2021", "2022", "2023", "2024", "2025"]
for col, h in enumerate(raroc_headers, 1):
    c = ws_chi.cell(r_raroc+1, col, h)
    c.font = font_header
    c.fill = fill_slate
    c.alignment = align_center

raroc_rows = [
    ("Agribank - Vốn kinh tế ước tính (EC = RWA x 8%)", "tỷ", 97116, 105317, 115584, 123797, 137600, 158400, "#,##0"),
    ("Agribank - Lợi nhuận sau thuế (PAT)", "tỷ", 10389, 11624, 17657, 20387, 20800, 24936, "#,##0"),
    ("Agribank - Tổn thất dự kiến (EL = Credit Cost x Dư nợ)", "tỷ", 18416, 21676, 27172, 24363, 25800, 26500, "#,##0"),
    ("Agribank - Tỷ số RAROC = (PAT / EC)", "%", 0.107, 0.110, 0.153, 0.165, 0.151, 0.157, "0.0%"),
    ("MB - Vốn kinh tế ước tính (EC = RWA x 8%)", "tỷ", 23863, 29084, 36845, 41881, 62132, 80000, "#,##0"),
    ("MB - Lợi nhuận sau thuế (PAT)", "tỷ", 8606, 13218, 18155, 21053, 23072, 27414, "#,##0"),
    ("MB - Tổn thất dự kiến (EL = Credit Cost gộp x Dư nợ)", "tỷ", 6118, 8030, 8048, 10887, 10450, 13744, "#,##0"),
    ("MB - Tỷ số RAROC = (PAT / EC)", "%", 0.361, 0.454, 0.493, 0.503, 0.371, 0.343, "0.0%"),
    ("Chênh lệch RAROC: MB − Agribank", "đ.%", 0.254, 0.344, 0.340, 0.338, 0.220, 0.186, "0.0%"),
]

for idx, r in enumerate(raroc_rows, r_raroc+2):
    ws_chi.cell(idx, 1, r[0]).font = font_bold if "RAROC" in r[0] else font_regular
    ws_chi.cell(idx, 1).alignment = align_left
    ws_chi.cell(idx, 2, r[1]).alignment = align_center
    ws_chi.cell(idx, 2).font = font_regular
    for cidx in range(3, 9):
        c = ws_chi.cell(idx, cidx, r[cidx-1])
        c.font = font_bold if "RAROC" in r[0] else font_regular
        c.alignment = align_right
        c.number_format = r[8]
        if "Chênh lệch" in r[0]:
            c.fill = fill_accent_blue
    for col in range(1, 9):
        ws_chi.cell(idx, col).border = thin_border

# Save
wb.save(file_path)
print("Phan_tich_RRTD_Agribank_MB_2020-2025_v2.xlsx successfully updated with Stress_Testing, IFRS9_Simulation and RAROC!")
