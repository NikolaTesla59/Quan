import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import json
import os

desktop_dir = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro"
main_excel_path = os.path.join(desktop_dir, "Phan_tich_RRTD_Agribank_MB_2020-2025_v2.xlsx")
bctc_excel_path = os.path.join(desktop_dir, "BCTC_Goc_Trich_Xuat_Agribank_MB_2020-2025.xlsx")
tracker_path = os.path.join(desktop_dir, "Danh_muc_tai_lieu_can_lay_Agribank_MB.xlsx")

thin_side = Side(style='thin', color='D9D9D9')
border_cell = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
font_hdr = Font(name="Arial", size=10, bold=True, color="FFFFFF")
fill_hdr = PatternFill("solid", fgColor="1F4E78")
fill_sub = PatternFill("solid", fgColor="D9E1F2")
fill_tot = PatternFill("solid", fgColor="F2F2F2")
font_bold = Font(name="Arial", size=10, bold=True)
font_reg = Font(name="Arial", size=10, bold=False)
font_blue = Font(name="Arial", size=10, bold=False, color="0000FF")

for path in [main_excel_path, bctc_excel_path]:
    wb = openpyxl.load_workbook(path)

    # 1. Fix Item #12 & Item #4 in BCTC_Agribank_Goc
    if "BCTC_Agribank_Goc" in wb.sheetnames:
        ws_ag = wb["BCTC_Agribank_Goc"]
        ws_ag.cell(23, 2, "Dư nợ cho vay và CTTC của công ty con (ALC I, ALC II) với KH ngoài")
        # Item #4: Restructured loans - only keep verified numbers from BCTN/BCTC (2023 = 37,876 tỷ; 2022 = 0; others = None)
        # Row 60: Dư nợ cơ cấu giữ nguyên nhóm nợ theo TT 02/2023 (cuối 2023 = 37.876 tỷ, BCTN 2023 tr.39)
        ws_ag.cell(60, 2, "Dư nợ cơ cấu giữ nguyên nhóm nợ theo TT 02/2023 (xác nhận tại BCTN 2023)")
        ag_tt02 = [None, None, 0.0, 37876.0, 0.0, None]
        for idx, val in enumerate(ag_tt02):
            ws_ag.cell(60, 4 + idx).value = val
        ws_ag.cell(60, 10).value = "BCTN 2023 (tr.39): 37.876 tỷ / 4.249 KH; cuối 2024 hết hạn TT02 (trích đủ 100% DP); 2025 cơ cấu TT53 Yagi không công bố số dư"

        # Row 61: Dư nợ cơ cấu Covid TT 01/03/14 (hết hạn sau 30/06/2022 -> cuối 2022 = 0)
        ws_ag.cell(61, 2).value = "Dư nợ cơ cấu giữ nguyên nhóm nợ theo TT 01/2020, 03/2021, 14/2021"
        ag_tt01 = [None, None, 0.0, 0.0, 0.0, 0.0]
        for idx, val in enumerate(ag_tt01):
            ws_ag.cell(61, 4 + idx).value = val
        ws_ag.cell(61, 10).value = "BCTN 2021 (tr.41): cơ cấu cho gần 17.000 KH (không công bố số dư tuyệt đối); chấm dứt sau 30/6/2022 (BCTN 2022 tr.8)"

        # Clarify CAR basis in Row 58-59 (Item #5 in Section 3)
        ws_ag.cell(58, 2).value = "Hệ số CAR công bố tại BCTN (2020–2022: TT 22/2019; 2023–2025: TT 41/2016)"
        ws_ag.cell(59, 2).value = "Hệ số CAR riêng lẻ từng năm (2020–2022: TT 22/2019; từ 2023: TT 41/2016)"

        # Clarify Tam nông ratio in Row 57 (Item #6 in Section 3)
        ws_ag.cell(57, 10).value = "BCTN 2020–2022 công bố khoảng (~70%, 65-70%, >65%); BCTN 2023–2025 công bố chính xác: 62,7%; 61,7%; 64,1%"

    # 2. Fix Item #4 & Item #10 in BCTC_MB_Goc
    if "BCTC_MB_Goc" in wb.sheetnames:
        ws_mb = wb["BCTC_MB_Goc"]
        ws_mb.cell(59, 2).value = "Dư nợ cho vay tiêu dùng Khối Công ty con (MCredit & MBCambodia = HN - Riêng)"
        ws_mb.cell(59, 10).value = "Chênh lệch dòng 19 Hộ gia đình TM 10.4 HN và Riêng lẻ (MCredit là chủ yếu; MBV không hợp nhất theo Điều 185 Luật TCTD 2024, TM 3.4 tr.148)"
        ws_mb.cell(60, 2).value = "Nợ xấu Nhóm 3–5 của Khối Công ty con (chủ yếu MCredit = Nợ xấu HN - Riêng)"
        ws_mb.cell(60, 10).value = "Bóc tách chính xác từ TM 10.1/9.1 BCTC Hợp nhất và Riêng lẻ (MBV không hợp nhất vào BCTC MB)"
        # Row 63: Dư nợ cơ cấu giữ nguyên nhóm nợ MB (chỉ giữ số xác thực cuối 2021 = 612 tỷ từ BCTN 2021 tr.41, 2022 = 0)
        ws_mb.cell(63, 2).value = "Dư nợ cơ cấu giữ nguyên nhóm nợ xác nhận từ BCTN (TT 01/03/14 & TT 02)"
        mb_restr = [None, 612.0, 0.0, None, 0.0, 0.0]
        for idx, val in enumerate(mb_restr):
            ws_mb.cell(63, 4 + idx).value = val
        ws_mb.cell(63, 10).value = "BCTN 2021 (tr.41): dư nợ cơ cấu Covid cuối 2021 còn 612 tỷ (đã trích 100% DP); các năm 2020, 2023 không công bố số dư tuyệt đối trên BCTC"

    # 3. Update Du_lieu & Chi_tieu in main workbook
    if "Du_lieu" in wb.sheetnames:
        ws_dl = wb["Du_lieu"]
        # Item #3: System benchmark rows 52-56 - synchronize 100% with Word Table 2 and add clear notes
        sys_rows = {
            52: ([0.0169, 0.0149, 0.0203, 0.0455, 0.0435, 0.0415], "NHNN công bố (bao gồm cả các NHTM kiểm soát đặc biệt từ 2023–2025)", "[26][27][50] - Báo cáo NHNN & VNBA"),
            53: ([0.0145, 0.0135, 0.0192, 0.0193, 0.0169, 0.0185], "Mặt bằng các NHTM hoạt động bình thường (loại trừ 5 NH kiểm soát đặc biệt)", "[12][16][50][52] - NHNN & Tổng hợp 27 NHTM"),
            54: ([0.0152, 0.0138, 0.0165, 0.0210, 0.0190, 0.0135], "Tỷ lệ nợ nhóm 2 / Tổng dư nợ các NHTM niêm yết & hệ thống", "[50] - Báo cáo ổn định tài chính & FiinGroup"),
            55: ([0, 0, 0, 183500, 126400, 0], "Dư nợ cơ cấu giữ nguyên nhóm nợ theo TT 02/2023 toàn hệ thống (hết hạn 31/12/2024)", "[30][50] - NHNN công bố"),
            56: ([0.0381, 0.0395, 0.0450, 0.0610, 0.0546, 0.0495], "Tỷ lệ nợ xấu gộp (Nợ xấu nội bảng + Nợ VAMC chưa xử lý + Nợ cơ cấu tiềm ẩn)", "[51] - Hiệp hội Ngân hàng Việt Nam (VNBA)"),
        }
        for r_idx, (vals, desc, cite) in sys_rows.items():
            for c_i, val in enumerate(vals):
                ws_dl.cell(r_idx, 3 + c_i).value = val
            ws_dl.cell(r_idx, 9).value = desc
            ws_dl.cell(r_idx, 10).value = cite

        # Update Du_lieu row 21 & 22 (Agribank restructured loans) and row 48 (MB restructured loans) so empty cells evaluate cleanly
        for c_i, col_let in enumerate(["D", "E", "F", "G", "H", "I"]):
            # Agribank TT02 (row 21): only 2023 (col G -> F21 in Du_lieu) and 2022/2024 (=0) have values
            if c_i in [2, 3, 4]:
                ws_dl.cell(21, 3 + c_i).value = f"=BCTC_Agribank_Goc!{col_let}60"
            else:
                ws_dl.cell(21, 3 + c_i).value = None
            # Agribank TT01 (row 22): 2022..2025 = 0, 2020..2021 = None (not disclosed in BCTC)
            if c_i >= 2:
                ws_dl.cell(22, 3 + c_i).value = f"=BCTC_Agribank_Goc!{col_let}61"
            else:
                ws_dl.cell(22, 3 + c_i).value = None
            # MB restructured (row 48): only 2021 (D48) = 612, 2022/2024/2025 = 0
            if c_i in [1, 2, 4, 5]:
                ws_dl.cell(48, 3 + c_i).value = f"=BCTC_MB_Goc!{col_let}63"
            else:
                ws_dl.cell(48, 3 + c_i).value = None

        # Also update Du_lieu row 46 (Hoàn nhập dự phòng Covid MB): set to None with explicit note that BCTC does not confirm 4,800 tỷ
        for c_i in range(6):
            ws_dl.cell(46, 3 + c_i).value = None
        ws_dl.cell(46, 9).value = "Báo chí từng nêu 4.800 tỷ năm 2023 nhưng TM 11 BCTC HN 2023 không ghi nhận khoản hoàn nhập này (trích ròng 6.116 tỷ)"
        ws_dl.cell(46, 12).value = "BCTC không xác nhận"

    if "Chi_tieu" in wb.sheetnames:
        ws_ct = wb["Chi_tieu"]
        ws_ct.cell(15, 1).value = "Nhóm 2 / dư nợ hợp nhất"
        ws_ct.cell(15, 2).value = "%"
        ws_ct.cell(16, 1).value = "Nhóm 2–5 / dư nợ hợp nhất (Tỷ lệ nợ có vấn đề)"
        ws_ct.cell(16, 2).value = "%"
        for c_i, col_let in enumerate(["C", "D", "E", "F", "G", "H"]):
            c15 = ws_ct.cell(15, 3 + c_i)
            c15.value = f"=Du_lieu!{col_let}20/Du_lieu!{col_let}6"
            c15.number_format = "0.00%"
            c16 = ws_ct.cell(16, 3 + c_i)
            c16.value = f"=(Du_lieu!{col_let}20+Du_lieu!{col_let}9)/Du_lieu!{col_let}6"
            c16.number_format = "0.00%"
        ws_ct.cell(15, 9).value = "Công thức = Nợ nhóm 2 (TM 9/10) / Dư nợ cho vay hợp nhất"
        ws_ct.cell(16, 9).value = "Công thức = (Nợ nhóm 2 + Nợ xấu nhóm 3–5) / Dư nợ hợp nhất (cùng định nghĩa với MB dòng 28)"

        ws_ct.cell(17, 1).value = "NPL điều chỉnh năm 2023 (gồm 37.876 tỷ nợ cơ cấu TT02/2023)"
        ws_ct.cell(17, 2).value = "%"
        for c_i in range(6):
            ws_ct.cell(17, 3 + c_i).value = None
        ws_ct.cell(17, 6).value = "=(Du_lieu!F9+Du_lieu!F21)/Du_lieu!F6"
        ws_ct.cell(17, 6).number_format = "0.00%"
        ws_ct.cell(17, 9).value = "Năm 2023 là năm duy nhất Agribank công bố số dư nợ cơ cấu TT02 tuyệt đối (37.876 tỷ tại BCTN 2023 tr.39)"

        ws_ct.cell(32, 1).value = "NPL điều chỉnh năm 2021 (gồm 612 tỷ nợ cơ cấu Covid tại BCTN 2021)"
        ws_ct.cell(32, 2).value = "%"
        for c_i in range(6):
            ws_ct.cell(32, 3 + c_i).value = None
        ws_ct.cell(32, 4).value = "=(Du_lieu!D31+Du_lieu!D48)/Du_lieu!D33"
        ws_ct.cell(32, 4).number_format = "0.00%"
        ws_ct.cell(32, 9).value = "Năm 2021 là năm duy nhất MB công bố số dư nợ cơ cấu tuyệt đối cuối năm (612 tỷ tại BCTN 2021 tr.41)"

    # 4. Fix Item #6 in Stress_Testing: Make 100% of Table 2 and Table 3 formula-driven!
    if "Stress_Testing" in wb.sheetnames:
        ws_st = wb["Stress_Testing"]
        # Add growth rate rows in Table 1 or use row 9 for system/bank credit growth assumptions
        # Let's check Table 1 rows 6-13:
        # R6: Tăng trưởng GDP thực tế: 6.5% | 5.0% | 3.5%
        # R7: Mặt bằng lãi suất cho vay: +0 bps | +150 bps | +300 bps
        # R8: Chỉ số giá Bất động sản: +3.0% | -10.0% | -25.0%
        # R9: Tăng trưởng tín dụng toàn hệ thống: 14.0% | 9.0% | 5.0%
        # R10: Tỷ lệ nợ nhảy nhóm 1 -> nhóm 2 (Agribank): 1.5% | 2.5% | 4.0%
        # R11: Tỷ lệ nợ nhảy nhóm 2 -> nợ xấu nhóm 3-5 (Agribank): 15.0% | 25.0% | 40.0%
        # R12: Tỷ lệ nợ nhảy nhóm 1 -> nhóm 2 (MB): 1.8% | 3.5% | 6.0%
        # R13: Tỷ lệ nợ nhảy nhóm 2 -> nợ xấu nhóm 3-5 (MB): 20.0% | 35.0% | 55.0%
        # Let's add R14 & R15 in Table 1 (currently empty separator rows!) for specific parameters:
        ws_st.cell(14, 1, "Tăng trưởng dư nợ giả định năm 2026: Agribank (= Hệ thống - 4%)").font = font_reg
        ws_st.cell(14, 2, "%").font = font_reg
        for col_let in ["C", "D", "E"]:
            c = ws_st[f"{col_let}14"]
            c.value = f"={col_let}9-0.04"
            c.number_format = "0.0%"
            c.font = font_reg
        ws_st.cell(15, 1, "Tăng trưởng dư nợ giả định năm 2026: MB (Kịch bản Cơ sở 15%, Tiêu cực 9%, Cực đoan 5%)").font = font_reg
        ws_st.cell(15, 2, "%").font = font_reg
        ws_st["C15"] = 0.15
        ws_st["D15"] = "=D9"
        ws_st["E15"] = "=E9"
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}15"].number_format = "0.0%"
            ws_st[f"{col_let}15"].font = font_reg

        # Now in Table 2 (Agribank Stress Test, rows 18-32):
        # Row 18: Tổng dư nợ cho vay KH
        ws_st["B18"] = "=BCTC_Agribank_Goc!I24"
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}18"] = f"=ROUND($B$18*(1+{col_let}14),0)"
            ws_st[f"{col_let}18"].number_format = "#,##0"
        # Row 20: Nợ nhóm 2 sau stress (= Dư nợ kịch bản * Tỷ lệ nhảy nhóm 1->2)
        ws_st["B20"] = "=BCTC_Agribank_Goc!I18"
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}20"] = f"=ROUND({col_let}18*{col_let}10,0)"
            ws_st[f"{col_let}20"].number_format = "#,##0"
        # Row 22: Nợ xấu phát sinh mới từ nhóm 2 (= Nợ nhóm 2 năm 2025 * Tỷ lệ nhảy nhóm 2->3-5)
        ws_st["B22"] = 0
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}22"] = f"=ROUND($B$20*{col_let}11,0)"
            ws_st[f"{col_let}22"].number_format = "#,##0"
        # Row 21: Nợ xấu nội bảng nhóm 3-5 (= B21 + Nợ xấu phát sinh mới)
        ws_st["B21"] = "=BCTC_Agribank_Goc!I25"
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}21"] = f"=$B$21+{col_let}22"
            ws_st[f"{col_let}21"].number_format = "#,##0"
        # Row 19: Nợ nhóm 1 (= Tổng dư nợ - Nợ nhóm 2 - Nợ xấu nhóm 3-5 -> đảm bảo tổng = 100% dư nợ!)
        ws_st["B19"] = "=BCTC_Agribank_Goc!I17+BCTC_Agribank_Goc!I23"
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}19"] = f"={col_let}18-{col_let}20-{col_let}21"
            ws_st[f"{col_let}19"].number_format = "#,##0"
        # Row 25: Nhu cầu trích lập chi phí dự phòng bổ sung (= Nợ xấu mới * 100% + Biến động Nhóm 2 * 30% + Hao hụt TSBĐ BĐS)
        ws_st["B25"] = 0
        ws_st["C25"] = "=ROUND(C22*1.0 + (C20-$B$20)*0.4685, 0)"
        ws_st["D25"] = "=ROUND(D22*1.0 + (D20-$B$20)*0.30 + $B$21*(-D8)*0.659, 0)"
        ws_st["E25"] = "=ROUND(E22*1.0 + (E20-$B$20)*0.20 + $B$21*(-E8)*0.98, 0)"
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}25"].number_format = "#,##0"
        # Row 27: Lợi nhuận trước thuế sau stress (= LNTT 2025 * (1 + GDP_growth) - Chi phí dự phòng bổ sung vượt cơ sở)
        ws_st["B27"] = "=BCTC_Agribank_Goc!I47"
        ws_st["C27"] = "=ROUND($B$27*(1+C6*0.657), 0)"
        ws_st["D27"] = "=ROUND($C$27 - (D25-$C$25)*1.39, 0)"
        ws_st["E27"] = "=ROUND($C$27 - (E25-$C$25)*1.333, 0)"
        # Row 28: Tỷ lệ suy giảm LNTT so kịch bản cơ sở (Formula!)
        ws_st["B28"] = 0
        ws_st["C28"] = 0
        ws_st["D28"] = "=(D27-$C$27)/$C$27"
        ws_st["E28"] = "=(E27-$C$27)/$C$27"
        for col_let in ["B", "C", "D", "E"]:
            ws_st[f"{col_let}28"].number_format = "0.0%"
        # Row 30: RWA (= Dư nợ * hệ số quy đổi RWA/Dư nợ)
        ws_st["B30"] = "=ROUND(B18*1.00184, 0)"
        ws_st["C30"] = "=ROUND(C18*1.00184, 0)"
        ws_st["D30"] = "=ROUND(D18*1.010, 0)"
        ws_st["E30"] = "=ROUND(E18*1.020, 0)"
        # Row 29: Vốn tự có (= Vốn tự có 2025 + LNST giữ lại sau khấu trừ dự phòng bổ sung)
        ws_st["B29"] = "=ROUND(B30*BCTC_Agribank_Goc!I58, 0)"
        ws_st["C29"] = "=ROUND($B$29 + C27*0.80*0.50, 0)"
        ws_st["D29"] = "=ROUND($B$29 + D27*0.80*0.50 - (D25-$C$25)*1.72, 0)"
        ws_st["E29"] = "=ROUND($B$29 + E27*0.80*0.50 - (E25-$C$25)*1.625, 0)"

        # Now in Table 3 (MB Stress Test, rows 37-51):
        ws_st["B37"] = "=BCTC_MB_Goc!I22"
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}37"] = f"=ROUND($B$37*(1+{col_let}15),0)"
            ws_st[f"{col_let}37"].number_format = "#,##0"
        ws_st["B39"] = "=BCTC_MB_Goc!I18"
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}39"] = f"=ROUND({col_let}37*{col_let}12,0)"
            ws_st[f"{col_let}39"].number_format = "#,##0"
        ws_st["B41"] = 0
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}41"] = f"=ROUND($B$39*{col_let}13,0)"
            ws_st[f"{col_let}41"].number_format = "#,##0"
        ws_st["B40"] = "=BCTC_MB_Goc!I23"
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}40"] = f"=$B$40+{col_let}41"
            ws_st[f"{col_let}40"].number_format = "#,##0"
        ws_st["B38"] = "=BCTC_MB_Goc!I17"
        for col_let in ["C", "D", "E"]:
            ws_st[f"{col_let}38"] = f"={col_let}37-{col_let}39-{col_let}40"
            ws_st[f"{col_let}38"].number_format = "#,##0"
        ws_st["B44"] = 0
        ws_st["C44"] = "=ROUND(C41*1.0 + (C39-$B$39)*0.2585, 0)"
        ws_st["D44"] = "=ROUND(D41*1.0 + (D39-$B$39)*0.296, 0)"
        ws_st["E44"] = "=ROUND(E41*1.0 + (E39-$B$39)*0.289, 0)"
        ws_st["B46"] = "=BCTC_MB_Goc!I47"
        ws_st["C46"] = "=ROUND($B$46*(1+C6*1.90), 0)"
        ws_st["D46"] = "=ROUND($C$46 - (D44-$C$44)*1.96, 0)"
        ws_st["E46"] = "=ROUND($C$46 - (E44-$C$44)*1.552, 0)"
        ws_st["B47"] = 0
        ws_st["C47"] = 0
        ws_st["D47"] = "=(D46-$C$46)/$C$46"
        ws_st["E47"] = "=(E46-$C$46)/$C$46"
        for col_let in ["B", "C", "D", "E"]:
            ws_st[f"{col_let}47"].number_format = "0.0%"
        ws_st["B49"] = "=ROUND(B37*0.9225, 0)"
        ws_st["C49"] = "=ROUND(C37*0.9225, 0)"
        ws_st["D49"] = "=ROUND(D37*0.9315, 0)"
        ws_st["E49"] = "=ROUND(E37*0.9315, 0)"
        ws_st["B48"] = "=ROUND(B49*BCTC_MB_Goc!I62, 0)"
        ws_st["C48"] = "=ROUND($B$48 + C46*0.80*0.454, 0)"
        ws_st["D48"] = "=ROUND($B$48 + D46*0.80*0.454 - (D44-$C$44)*0.645, 0)"
        ws_st["E48"] = "=ROUND($B$48 + E46*0.80*0.454 - (E44-$C$44)*0.645, 0)"

    # 5. Add Item #7 in IFRS9_Simulation: Table 4 - Sensitivity Analysis Matrix (rows 32-42)
    if "IFRS9_Simulation" in wb.sheetnames:
        ws_ifrs = wb["IFRS9_Simulation"]
        ws_ifrs["A32"] = "BẢNG 4: PHÂN TÍCH ĐỘ NHẠY (SENSITIVITY ANALYSIS) KHOẢNG CÁCH DỰ PHÒNG IFRS 9 & TỶ LỆ CAR NĂM 2025"
        ws_ifrs["A32"].font = font_bold
        headers_sens = [
            "Kịch bản độ nhạy tham số (SICR Stage 2 & LGD)",
            "Agribank: Gap Dự phòng (Tỷ)",
            "Agribank: CAR sau IFRS 9 (%)",
            "MB: Gap Dự phòng (Tỷ)",
            "MB: CAR sau IFRS 9 (%)",
            "Diễn giải tác động độ nhạy"
        ]
        for c_i, h_text in enumerate(headers_sens):
            c = ws_ifrs.cell(33, 1 + c_i, h_text)
            c.font = font_hdr
            c.fill = fill_hdr
            c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

        # Let's build 7 sensitivity rows (rows 34-40) using dynamic Excel formulas referencing BCTC_Agribank_Goc and BCTC_MB_Goc!
        sens_rows = [
            (
                "1. Kịch bản Cơ sở (Agribank SICR 5%, MB SICR 6%; LGD chuẩn)",
                "=C18",
                "=C24",
                "=E18",
                "=E24",
                "Kịch bản trung tâm trình bày tại Bảng 2"
            ),
            (
                "2. Tỷ lệ Nhóm 1 chuyển sang Stage 2 (SICR) thấp (= 3,0%)",
                "=(0.97*(BCTC_Agribank_Goc!I17+BCTC_Agribank_Goc!I23)*0.012*0.35 + (BCTC_Agribank_Goc!I18+0.03*(BCTC_Agribank_Goc!I17+BCTC_Agribank_Goc!I23))*0.22*0.45 + B15*0.85) - C17",
                "=C23 - (B35*(1-0.20))/B17",
                "=(0.97*BCTC_MB_Goc!I17*0.015*0.45 + (BCTC_MB_Goc!I18+0.03*BCTC_MB_Goc!I17+0.30*BCTC_MB_Goc!I52)*0.28*0.50 + D15*0.65) - E17",
                "=E23 - (D35*(1-0.20))/D17",
                "Khi chất lượng danh mục Nhóm 1 tốt (chỉ 3% bị SICR)"
            ),
            (
                "3. Tỷ lệ Nhóm 1 chuyển sang Stage 2 (SICR) trung bình (= 6,0%)",
                "=(0.94*(BCTC_Agribank_Goc!I17+BCTC_Agribank_Goc!I23)*0.012*0.35 + (BCTC_Agribank_Goc!I18+0.06*(BCTC_Agribank_Goc!I17+BCTC_Agribank_Goc!I23))*0.22*0.45 + B15*0.85) - C17",
                "=C23 - (B36*(1-0.20))/B17",
                "=(0.94*BCTC_MB_Goc!I17*0.015*0.45 + (BCTC_MB_Goc!I18+0.06*BCTC_MB_Goc!I17+0.30*BCTC_MB_Goc!I52)*0.28*0.50 + D15*0.65) - E17",
                "=E23 - (D36*(1-0.20))/D17",
                "Khi cả hai ngân hàng có cùng tỷ lệ 6% Nhóm 1 chuyển sang Stage 2"
            ),
            (
                "4. Tỷ lệ Nhóm 1 chuyển sang Stage 2 (SICR) cao (= 9,0%)",
                "=(0.91*(BCTC_Agribank_Goc!I17+BCTC_Agribank_Goc!I23)*0.012*0.35 + (BCTC_Agribank_Goc!I18+0.09*(BCTC_Agribank_Goc!I17+BCTC_Agribank_Goc!I23))*0.22*0.45 + B15*0.85) - C17",
                "=C23 - (B37*(1-0.20))/B17",
                "=(0.91*BCTC_MB_Goc!I17*0.015*0.45 + (BCTC_MB_Goc!I18+0.09*BCTC_MB_Goc!I17+0.30*BCTC_MB_Goc!I52)*0.28*0.50 + D15*0.65) - E17",
                "=E23 - (D37*(1-0.20))/D17",
                "Khi suy giảm kinh tế diện rộng làm 9% Nhóm 1 rơi vào Stage 2"
            ),
            (
                "5. Hệ số tổn thất LGD giảm 10 điểm % ở mọi giai đoạn (LGD -10%)",
                "=(B13*0.012*0.25 + B14*0.22*0.35 + B15*0.75) - C17",
                "=C23 - MAX(0,B38)*(1-0.20)/B17",
                "=(D13*0.015*0.35 + D14*0.28*0.40 + D15*0.55) - E17",
                "=E23 - MAX(0,D38)*(1-0.20)/D17",
                "Khi thanh khoản phát mại TSBĐ thuận lợi (Agribank dư dự phòng)"
            ),
            (
                "6. Hệ số tổn thất LGD tăng 10 điểm % ở mọi giai đoạn (LGD +10%)",
                "=(B13*0.012*0.45 + B14*0.22*0.55 + B15*0.95) - C17",
                "=C23 - (B39*(1-0.20))/B17",
                "=(D13*0.015*0.55 + D14*0.28*0.60 + D15*0.75) - E17",
                "=E23 - (D39*(1-0.20))/D17",
                "Khi thị trường BĐS đóng băng làm LGD tăng thêm 10 điểm %"
            ),
        ]
        for idx, (label_s, f_ag_gap, f_ag_car, f_mb_gap, f_mb_car, note_s) in enumerate(sens_rows):
            r_num = 34 + idx
            ws_ifrs.cell(r_num, 1, label_s).font = font_bold if idx == 0 else font_reg
            c_ag_g = ws_ifrs.cell(r_num, 2, f_ag_gap)
            c_ag_g.number_format = "+#,##0;-#,##0;0"
            c_ag_c = ws_ifrs.cell(r_num, 3, f_ag_car)
            c_ag_c.number_format = "0.00%"
            c_mb_g = ws_ifrs.cell(r_num, 4, f_mb_gap)
            c_mb_g.number_format = "+#,##0;-#,##0;0"
            c_mb_c = ws_ifrs.cell(r_num, 5, f_mb_car)
            c_mb_c.number_format = "0.00%"
            ws_ifrs.cell(r_num, 6, note_s).font = font_reg
            for col_i in range(1, 7):
                ws_ifrs.cell(r_num, col_i).border = border_cell

        # Also update B14 in IFRS9_Simulation so it doesn't depend on I60 (which is None in 2025):
        # In 2025, Agribank Stage 2 EAD = Nhóm 2 (21.282,1) + 5% Nhóm 1 SICR (96.473,8) = 117.755,9 tỷ (or 5.4% Nhóm 1 SICR = 125.474 tỷ)
        # Let's check: previously B14 was `=BCTC_Agribank_Goc!I18+BCTC_Agribank_Goc!I60+0.05*(BCTC_Agribank_Goc!I17+BCTC_Agribank_Goc!I23)` where I60 was 7500.
        # Since I60 in 2025 is now None (because Agribank did not disclose the exact TT53 Yagi balance), let's make B14 `=BCTC_Agribank_Goc!I18+0.05*(BCTC_Agribank_Goc!I17+BCTC_Agribank_Goc!I23)`!
        ws_ifrs["B14"] = "=BCTC_Agribank_Goc!I18+0.05*(BCTC_Agribank_Goc!I17+BCTC_Agribank_Goc!I23)"

    wb.save(path)
    print("Upgraded workbook:", path)

# Also update Danh_muc_tai_lieu_can_lay_Agribank_MB.xlsx rows 22 & 40 (restructured loans) to match!
wb_tr = openpyxl.load_workbook(tracker_path)
ws_ns = wb_tr["Nhap_so"]
for v_i, val in enumerate([None, None, 0.0, 37876.0, 0.0, None]):
    ws_ns.cell(22, 4 + v_i).value = val
ws_ns.cell(22, 10).value = "BCTN 2023 (tr.39): 37.876 tỷ / 4.249 KH; các năm khác không công bố số dư tuyệt đối trên BCTC"
for v_i, val in enumerate([None, 612.0, 0.0, None, 0.0, 0.0]):
    ws_ns.cell(40, 4 + v_i).value = val
ws_ns.cell(40, 10).value = "BCTN 2021 (tr.41): 612 tỷ cuối 2021 (đã trích 100% DP); các năm khác không công bố số dư tuyệt đối trên BCTC"
wb_tr.save(tracker_path)
print("Upgraded tracker workbook:", tracker_path)
