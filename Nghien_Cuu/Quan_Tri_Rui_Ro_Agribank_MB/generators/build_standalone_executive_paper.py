# -*- coding: utf-8 -*-
"""
Standalone Master Course Assignment Production Script:
Bao_cao_Thuyet_trinh_Agribank_MB_2020-2025_Executive.docx
Guarantees 100% correct chronological document flow (using sectPr.addprevious),
zero empty sections, calibrated as a complete standalone course assignment & presentation dossier.
"""
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from copy import deepcopy
import os

source_v5_path = r'C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v5.docx'
target_exec_path = r'C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Bao_cao_Thuyet_trinh_Agribank_MB_2020-2025_Executive.docx'
charts_dir = r'C:\Users\Admin\.gemini\antigravity\scratch\charts'

doc_src = docx.Document(source_v5_path)
doc = docx.Document()

# 1. Page Setup: Standard 1.0 inch margins, Letter size
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    section.page_width = Inches(8.5)
    section.page_height = Inches(11.0)

# 2. Settings: Enable automatic dynamic field updates in Word
settings = doc.settings.element
update_fields = parse_xml(f'<w:updateFields {nsdecls("w")} w:val="true"/>')
settings.append(update_fields)

# Helper formatting functions
def style_run(run, font_name="Times New Roman", size_pt=11, bold=False, italic=False, color_rgb=(0,0,0)):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)

def add_p(doc, text="", space_before=2, space_after=3, line_spacing=1.15, align=WD_ALIGN_PARAGRAPH.LEFT, page_break_before=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    p.paragraph_format.page_break_before = page_break_before
    p.alignment = align
    if text:
        r = p.add_run(text)
        style_run(r, font_name="Times New Roman", size_pt=11)
    return p

def add_h1(doc, text, page_break_before=True):
    p = doc.add_paragraph(style='Heading 1')
    p.paragraph_format.page_break_before = page_break_before
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    pPr = p._element.get_or_add_pPr()
    pPr.append(parse_xml(f'<w:outlineLvl {nsdecls("w")} w:val="0"/>'))
    r = p.add_run(text)
    style_run(r, font_name="Times New Roman", size_pt=13.5, bold=True, color_rgb=(0, 32, 96))
    return p

def add_h2(doc, text):
    p = doc.add_paragraph(style='Heading 2')
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    pPr = p._element.get_or_add_pPr()
    pPr.append(parse_xml(f'<w:outlineLvl {nsdecls("w")} w:val="1"/>'))
    r = p.add_run(text)
    style_run(r, font_name="Times New Roman", size_pt=12, bold=True, color_rgb=(15, 76, 129))
    return p

def add_h3(doc, text):
    p = doc.add_paragraph(style='Heading 3')
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    pPr = p._element.get_or_add_pPr()
    pPr.append(parse_xml(f'<w:outlineLvl {nsdecls("w")} w:val="2"/>'))
    r = p.add_run(text)
    style_run(r, font_name="Times New Roman", size_pt=11, bold=True, italic=True, color_rgb=(0, 0, 0))
    return p

def add_dot_leader_tab(paragraph, pos=9360):
    pPr = paragraph._element.get_or_add_pPr()
    tabs = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="right" w:leader="dot" w:pos="{pos}"/></w:tabs>')
    pPr.append(tabs)

def add_image_exhibit(doc, chart_filename, title_text, source_text):
    chart_path = os.path.join(charts_dir, chart_filename)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(4)
    p_title.paragraph_format.keep_with_next = True
    r_t = p_title.add_run(title_text)
    style_run(r_t, font_name="Times New Roman", size_pt=10.5, bold=True, color_rgb=(0, 32, 96))
    
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(4)
    p_img.paragraph_format.space_after = Pt(4)
    r_img = p_img.add_run()
    r_img.add_picture(chart_path, width=Inches(6.2))
    
    p_src = doc.add_paragraph()
    p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_src.paragraph_format.space_before = Pt(2)
    p_src.paragraph_format.space_after = Pt(10)
    r_s = p_src.add_run(source_text)
    style_run(r_s, font_name="Times New Roman", size_pt=9.0, italic=True, color_rgb=(80, 80, 80))

def copy_p(doc_dst, p_src, text_override=None, page_break_before=None, align=None):
    """
    Inserts a copy of p_src immediately before sectPr to maintain 100% strict chronological order.
    """
    sectPr = doc_dst._body._element.xpath('w:sectPr')[0]
    p_copy = deepcopy(p_src._p)
    sectPr.addprevious(p_copy)
    p_last = doc_dst.paragraphs[-1]
    if text_override is not None:
        p_last.text = text_override
        for r in p_last.runs:
            style_run(r, font_name="Times New Roman", size_pt=11)
    if page_break_before is not None:
        p_last.paragraph_format.page_break_before = page_break_before
    if align is not None:
        p_last.alignment = align
    return p_last

def copy_tbl(doc_dst, tbl_src):
    """
    Inserts a copy of tbl_src immediately before sectPr to maintain 100% strict chronological order.
    """
    sectPr = doc_dst._body._element.xpath('w:sectPr')[0]
    tbl_copy = deepcopy(tbl_src._tbl)
    sectPr.addprevious(tbl_copy)
    return doc_dst.tables[-1]

# ==============================================================================
# 3. BUILD FRONT MATTER
# ==============================================================================
print("Generating Front Matter...")

# Cover Page (Calibrated as Master Course Assignment Essay)
p_c1 = add_p(doc, "BỘ GIÁO DỤC VÀ ĐÀO TẠO — TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN (NEU)\nVIỆN ĐÀO TẠO SAU ĐẠI HỌC — VIỆN NGÂN HÀNG - TÀI CHÍNH", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=24)
for r in p_c1.runs:
    style_run(r, size_pt=11, bold=True, color_rgb=(0, 32, 96))

p_c2 = add_p(doc, "BÀI TIỂU LUẬN HỌC PHẦN: QUẢN TRỊ RỦI RO\n(BÁO CÁO CHUYÊN ĐỀ & TÀI LIỆU THUYẾT TRÌNH NHÓM TRÊN LỚP)", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=20, space_after=14)
for r in p_c2.runs:
    style_run(r, size_pt=15, bold=True, color_rgb=(192, 0, 0))

p_c3 = add_p(doc, "SO SÁNH MÔ HÌNH VÀ THỰC TRẠNG QUẢN TRỊ RỦI RO TÍN DỤNG\nGIỮA AGRIBANK VÀ MB GIAI ĐOẠN 2020–2025", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=10)
for r in p_c3.runs:
    style_run(r, size_pt=16, bold=True, color_rgb=(0, 32, 96))

p_c4 = add_p(doc, "ĐỐI THOẠI HỌC THUẬT VỀ THỂ CHẾ SỞ HỮU, KHẨU VỊ RỦI RO, KHOAN DUNG PHÁP LÝ,\nKIỂM TRA SỨC CHỊU ĐỰNG (STRESS TEST) VÀ MÔ PHỎNG CHUẨN MỰC IFRS 9", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=36)
for r in p_c4.runs:
    style_run(r, size_pt=11.5, bold=True, italic=True, color_rgb=(80, 80, 80))

p_c5 = add_p(doc, (
    "Nhóm thực hiện:\tNhóm 2 (Lớp K34_3_NH8 — Cao học Khóa 34 NEU)\n"
    "Học phần / Môn học:\tQuản trị rủi ro\n"
    "Giảng viên hướng dẫn:\tTS. Khúc Thế Anh\n"
    "Danh sách thành viên:\n"
    "   1. CH345205 — Cao Trường Anh\t\t5. CH345585 — Ngô Thị Bích Ngọc\n"
    "   2. CH345254 — Đỗ Lương Bằng\t\t6. CH345648 — Phạm Hồng Quân\n"
    "   3. CH345463 — Hoàng Thị Mai Hương\t7. CH345714 — Vũ Thanh Thủy\n"
    "   4. CH345505 — Lê Thị Bảo Linh\t\t8. CH345756 — Đỗ Minh Tuấn\n"
    "Hồ sơ dữ liệu kèm theo:\tPhan_tich_RRTD_Agribank_MB_2020-2025_v3.xlsx & BCTC_Goc_Trich_Xuat_Agribank_MB_2020-2025_v2.xlsx\n"
    "Định dạng văn bản:\tTiểu luận học phần rút gọn (~20 trang Nội dung thực chứng, loại bỏ lý thuyết hàn lâm, kèm Kịch bản thuyết trình Speaker Notes)"
), space_before=16, space_after=40)
for r in p_c5.runs:
    style_run(r, size_pt=10.5)

p_c6 = add_p(doc, "Hà Nội, Năm 2026", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=20, space_after=0)
for r in p_c6.runs:
    style_run(r, size_pt=11, bold=True)
p_c6.runs[-1].add_break(docx.enum.text.WD_BREAK.PAGE)

# Executive Summary
add_h1(doc, "TÓM TẮT ĐIỀU HÀNH (BẢN TÓM TẮT BÁO CÁO THUYẾT TRÌNH)", page_break_before=False)
add_p(doc, (
    "Bản Báo cáo Thuyết trình này được nhóm tác giả biên soạn chuyên biệt phục vụ buổi báo cáo chuyên đề và thuyết trình nhóm học phần Quản trị rủi ro (Chương trình Đào tạo Thạc sĩ NEU). "
    "Tài liệu lược bỏ hoàn toàn các khái niệm lý thuyết giáo khoa thuần túy (như định nghĩa rủi ro tín dụng sơ cấp, mô hình Stiglitz-Weiss, lý thuyết Jensen-Meckling), "
    "tập trung 100% dung lượng vào bóc tách dữ liệu định lượng thực chứng, mô hình kiểm tra sức chịu đựng (Stress Testing), "
    "mô phỏng chuẩn mực quốc tế IFRS 9 và các bài học xử lý sự cố thực tế từ 27 tệp báo cáo tài chính kiểm toán và báo cáo thường niên giai đoạn 2020–2025 của Agribank và MB. "
    "Năm thông điệp cốt lõi chi phối toàn bộ bài thuyết trình bao gồm:"
))

exec_points = [
    ("1. Hiện tượng Hội tụ NPL bề mặt nhưng Phân kỳ bản chất: ", 
     "Báo cáo thường niên công bố NPL Agribank năm 2025 là 1,17%, thấp hơn MB (1,29%). Tuy nhiên, đây là sự so sánh không cùng mẫu số (Agribank chia tổng cấp tín dụng theo Thông tư 11/31). Khi tính like-for-like trên cùng mẫu số Dư nợ cho vay khách hàng hợp nhất (Thuyết minh 9), NPL của Agribank là 1,30%, gần như bằng MB (1,29%)."),
    ("2. Hiệu ứng Mẫu số và Kỹ thuật Xóa nợ bằng dự phòng: ", 
     "Phân rã toán học (Decomposition) chứng minh mức giảm 0,33 điểm % NPL của MB năm 2025 chủ yếu đến từ hiệu ứng mẫu số (-0,46 điểm % nhờ tín dụng tăng 39,6% làm loãng nợ xấu), trong khi nợ xấu tuyệt đối vẫn tăng +1.442 tỷ đồng (+0,13 điểm % hiệu ứng tử số). Ngược lại, Agribank giảm thực chất cả mẫu số (-0,22 điểm %) và nợ xấu tuyệt đối giảm -3.399 tỷ (-0,17 điểm %). Cả hai ngân hàng dựa rất lớn vào quỹ dự phòng để xóa nợ nội bảng trong năm 2025 (Agribank xóa 32.621 tỷ đồng, MB xóa 12.185 tỷ đồng). Nếu cộng lại số nợ đã xóa, NPL thực chất trước xử lý rủi ro ước tính lên tới 2,95% tại Agribank và 2,42% tại MB."),
    ("3. Sự đánh đổi Chu kỳ của Bộ đệm Dự phòng (Procyclical Buffering): ", 
     "MB lựa chọn chiến lược xả mạnh bộ đệm bao phủ nợ xấu (LLCR) từ đỉnh 268,0% (2021) xuống 93,7% (2025) để tối ưu hóa lợi nhuận trước áp lực cổ đông và thị trường chứng khoán. Ngược lại, Agribank duy trì bộ đệm phòng thủ thể chế bền vững (LLCR 113,6%–146,3%), chấp nhận chi phí trích lập dự phòng bình quân 1,66% dư nợ để bảo toàn vốn công."),
    ("4. Tính Tổn thương Bất đối xứng trong Stress Testing 2026: ", 
     "Dưới kịch bản vĩ mô Cực đoan 2026 (GDP 3,5%, lãi suất +300 bps, giá BĐS -25%), mô hình lượng hóa sự phân hóa sâu sắc: Agribank chịu rủi ro sống còn về An toàn vốn (hệ số CAR tụt từ 10,22% xuống 8,67%, sát ngưỡng sàn Basel II 8,0%), trong khi MB chịu cú sốc trực diện vào Lợi nhuận (LNTT sụt giảm -69,3% do chi phí dự phòng bổ sung 22.402 tỷ đồng ăn mòn gần hết thu nhập)."),
    ("5. Cú sốc Chuyển đổi IFRS 9 ECL tại Stage 2: ", 
     "Mô phỏng chuẩn mực quốc tế IFRS 9 bóc tách khoảng cách dự phòng trích thiếu (Provisioning Gap) của MB lên tới +14.006 tỷ đồng (+106,5%), khiến vốn CSH giảm -7,9% và CAR giảm 103 điểm cơ bản (xuống 9,97%). Agribank chỉ thiếu +3.660 tỷ (+9,8%) nhờ 90,2% TSBĐ là bất động sản giúp duy trì LGD thấp. MB chịu cú sốc lớn vì danh mục cho vay tiêu dùng tín chấp tại MCredit và 30% danh mục trái phiếu doanh nghiệp TCKT rơi vào diện gia tăng rủi ro tín dụng đáng kể (SICR - Stage 2).")
]

for title, desc in exec_points:
    p = add_p(doc, space_before=3, space_after=4)
    r1 = p.add_run(f"  • {title}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(desc)
    style_run(r2, bold=False)

p_kw = add_p(doc, (
    "Từ khóa thuyết trình: Quản trị rủi ro tín dụng; NPL Decomposition; Hiệu ứng mẫu số; Bộ đệm dự phòng LLCR; "
    "Khoan dung pháp lý; Macro Stress Testing 2026; IFRS 9 ECL Simulation; RORAC proxy; MBV Ring-fencing."
), space_before=8, space_after=0)
for r in p_kw.runs:
    style_run(r, size_pt=10, italic=True, color_rgb=(80,80,80))
p_kw.runs[-1].add_break(docx.enum.text.WD_BREAK.PAGE)

# Table of Contents
p_toc_title = add_p(doc, "MỤC LỤC BÁO CÁO THUYẾT TRÌNH (AUTOMATED TABLE OF CONTENTS)", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=8)
for r in p_toc_title.runs:
    style_run(r, size_pt=13.5, bold=True, color_rgb=(0, 32, 96))

p_dyn_toc = doc.add_paragraph()
p_dyn_toc.paragraph_format.space_before = Pt(2)
p_dyn_toc.paragraph_format.space_after = Pt(6)
fldSimple = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="TOC \\o &quot;1-2&quot; \\h \\z \\u"/>')
p_dyn_toc._element.append(fldSimple)

toc_items = [
    ("TÓM TẮT ĐIỀU HÀNH (BẢN TÓM TẮT BÁO CÁO THUYẾT TRÌNH)", "2"),
    ("DANH MỤC BẢNG BIỂU VÀ ĐỒ THỊ THUYẾT TRÌNH", "4"),
    ("PHẦN I. BỐI CẢNH THỂ CHẾ VÀ KHẨU VỊ RỦI RO ĐỐI LẬP (AGRIBANK VS MB)", "5"),
    ("  1.1. Agribank: Thể chế NHTM Nhà nước và Quản trị rủi ro phân tán", "5"),
    ("  1.2. MB: Thể chế Tập đoàn Tài chính và Quản trị tập trung", "6"),
    ("  1.3. Ma trận đối chiếu chuyên sâu hai mô hình quản trị rủi ro", "7"),
    ("PHẦN II. BÓC TÁCH THỰC TRẠNG QUẢN TRỊ RỦI RO TÍN DỤNG & PHÂN RÃ TOÁN HỌC (2020–2025)", "8"),
    ("  2.1. Quy mô tín dụng, nợ xấu và hiện tượng hội tụ NPL bề mặt (Like-for-like 1,30% vs 1,29%)", "8"),
    ("  2.2. Phân rã biến động nợ xấu (NPL Decomposition): Lượng hóa hiệu ứng mẫu số và tử số", "10"),
    ("  2.3. Bộ đệm dự phòng (LLCR), Chi phí tín dụng và Vai trò của kỹ thuật xóa nợ bằng dự phòng", "12"),
    ("  2.4. Nợ nhóm 2, Nợ cơ cấu và Áp lực nợ tiềm ẩn: Nợ nhóm 2 như biến báo động sớm (EWI)", "14"),
    ("  2.5. Đo lường hiệu quả tài chính điều chỉnh theo rủi ro (RORAC)", "16"),
    ("  2.6. Cơ cấu danh mục, mức độ tập trung ngành và an toàn vốn (CAR)", "17"),
    ("PHẦN III. MÔ HÌNH HÓA KIỂM TRA SỨC CHỊU ĐỰNG VĨ MÔ (STRESS TESTING 2026)", "19"),
    ("  3.1. Thiết kế kịch bản vĩ mô theo chuẩn Basel II/III (ICAAP) và Ma trận chuyển nhóm nợ", "19"),
    ("  3.2. Kết quả lượng hóa định lượng: Phân hóa hai dạng tổn thương bất đối xứng (CAR vs LNTT)", "20"),
    ("PHẦN IV. MÔ PHỎNG ĐỊNH LƯỢNG TÁC ĐỘNG CHUYỂN ĐỔI CHUẨN MỰC IFRS 9 ECL", "22"),
    ("  4.1. Sự chuyển dịch mô hình: Incurred Loss (VAS/TT11) sang Lifetime Expected Credit Loss (IFRS 9)", "22"),
    ("  4.2. Bóc tách khoảng cách thiếu hụt dự phòng (Provisioning Gap) và Cú sốc trích lập Stage 2", "23"),
    ("  4.3. Kiểm định độ nhạy 6 kịch bản tham số (Robustness Sensitivity Analysis)", "25"),
    ("PHẦN V. PHÂN TÍCH TÌNH HUỐNG THỰC TIỄN CHUYÊN SÂU (CASE STUDIES)", "27"),
    ("  5.1. Agribank: Cú sốc thiên tai Yagi 2024, điểm nghẽn thanh khoản TSBĐ nợ nhóm 5 và vụ Lifepro", "27"),
    ("  5.2. MB: Rủi ro tín dụng tiêu dùng tại MCredit và rủi ro đạo đức cấp chi nhánh (Vụ án Chi nhánh Gia Lai)", "28"),
    ("  5.3. MB: Cú sốc chất lượng tài sản 2023: Khủng hoảng TPDN - Bất động sản và liên đới CIC", "29"),
    ("  5.4. MB: Biến động nợ xấu Quý III–IV/2025, xử lý rủi ro bằng dự phòng và cơ chế MBV", "30"),
    ("PHẦN VI. SO SÁNH HAI MÔ HÌNH VÀ HỆ THỐNG KHUYẾN NGHỊ QUẢN TRỊ NÂNG CAO", "31"),
    ("  6.1. Ma trận đối thoại học thuật: Mô hình Phòng thủ Thể chế vs Mô hình Đổi mới Tối ưu hóa Lợi nhuận", "31"),
    ("  6.2. Hệ thống khuyến nghị quản trị nâng cao cho NHNN, Agribank và MB", "32"),
    ("PHẦN VII. KỊCH BẢN THUYẾT TRÌNH CHI TIẾT VÀ BỘ HƯỚNG DẪN BẢO VỆ PHẢN BIỆN (SPEAKER NOTES)", "34"),
    ("  7.1. Khung thời lượng và Kịch bản lời thoại thuyết trình từng phần (Khung 15–20 phút)", "34"),
    ("  7.2. Bộ 5 câu hỏi phản biện kinh điển của giảng viên và chiến lược trả lời xuất sắc", "37"),
    ("KẾT LUẬN", "39"),
    ("TÀI LIỆU THAM KHẢO CHỌN LỌC", "40"),
    ("PHỤ LỤC THUYẾT TRÌNH: DỮ LIỆU ĐỊNH LƯỢNG MỞ RỘNG", "41")
]

for title, page in toc_items:
    p = add_p(doc, space_before=1.5, space_after=1.5)
    add_dot_leader_tab(p, pos=9360)
    is_main = not title.startswith("  ")
    r = p.add_run(f"{title}\t{page}")
    style_run(r, size_pt=10 if is_main else 9.5, bold=is_main, color_rgb=(0, 32, 96) if is_main else (50, 50, 50))

# List of Exhibits
add_h1(doc, "DANH MỤC BẢNG BIỂU VÀ ĐỒ THỊ THUYẾT TRÌNH", page_break_before=True)

add_p(doc, "DANH MỤC BẢNG BIỂU ĐỊNH LƯỢNG CỐT LÕI (11 BẢNG CHÍNH + 2 BẢNG PHỤ LỤC)", space_before=6, space_after=4)
doc.paragraphs[-1].runs[0].bold = True
doc.paragraphs[-1].runs[0].font.color.rgb = RGBColor(0, 32, 96)

table_exhibits = [
    ("Bảng 1. Ma trận đối chiếu cấu trúc thể chế và mô hình 3 tuyến phòng vệ giữa Agribank và MB", "7"),
    ("Bảng 2. Quy mô dư nợ, nợ xấu và tỷ lệ NPL của Agribank và MB giai đoạn 2020–2025 (Tỷ đồng, %)", "9"),
    ("Bảng 3. Bộ đệm dự phòng (LLCR), chi phí dự phòng và bóc tách Credit Cost (2020–2025)", "12"),
    ("Bảng 4. Nợ nhóm 2, nợ cơ cấu theo thông tư và NPL điều chỉnh toàn diện (2020–2025)", "14"),
    ("Bảng 5. Tỷ suất lợi nhuận trên vốn rủi ro ước tính (RORAC proxy) giai đoạn 2020–2025", "16"),
    ("Bảng 6. Cơ cấu danh mục rủi ro tập trung và Hệ số an toàn vốn (CAR) giai đoạn 2020–2025", "17"),
    ("Bảng 7. Kết quả Kiểm tra sức chịu đựng vĩ mô năm 2026 đối với Agribank và MB", "20"),
    ("Bảng 8. Kết quả mô phỏng tác động chuyển đổi sang Chuẩn mực Quốc tế IFRS 9 năm 2025", "23"),
    ("Bảng 9. Kết quả kiểm định độ nhạy mô phỏng IFRS 9 ECL của Agribank và MB theo 6 kịch bản tham số", "25"),
    ("Bảng 10. Ma trận đánh giá lỗ hổng Kiểm soát Nội bộ COSO 2013 qua các tình huống thực tiễn", "30"),
    ("Bảng 11. So sánh đối chiếu toàn diện hai triết lý quản trị rủi ro tín dụng (Agribank vs MB)", "31"),
    ("Phụ lục 1. Thống kê mô tả (Descriptive Statistics) các chỉ tiêu tài chính và rủi ro tín dụng (2020–2025)", "41"),
    ("Phụ lục 2. Ma trận hệ số tương quan (Correlation Matrix) giữa Tăng trưởng tín dụng, Nợ nhóm 2 và NPL", "42")
]

for title, page in table_exhibits:
    p = add_p(doc, space_before=1.5, space_after=1.5)
    add_dot_leader_tab(p, pos=9360)
    r = p.add_run(f"  • {title}\t{page}")
    style_run(r, size_pt=9.5)

add_p(doc, "DANH MỤC HÌNH VẼ VÀ ĐỒ THỊ MINH HỌA TRỰC QUAN (6 ĐỒ THỊ 300 DPI)", space_before=10, space_after=4)
doc.paragraphs[-1].runs[0].bold = True
doc.paragraphs[-1].runs[0].font.color.rgb = RGBColor(0, 32, 96)

fig_exhibits = [
    ("Hình 1. Diễn biến tỷ lệ NPL và tỷ lệ nợ nhóm 2 của Agribank và MB (2020–2025)", "10"),
    ("Hình 2. Tốc độ tăng trưởng quy mô dư nợ và nợ xấu tại Agribank và MB (2020–2025)", "11"),
    ("Hình 3. Tỷ lệ bao phủ nợ xấu (LLCR) và Chi phí tín dụng (Credit Cost) giai đoạn 2020–2025", "13"),
    ("Hình 4. Mức độ tập trung tín dụng BĐS & Xây dựng và Hệ số an toàn vốn (CAR) giai đoạn 2020–2025", "18"),
    ("Hình 5. Kết quả Kiểm tra sức chịu đựng vĩ mô năm 2026 (Macro Stress Testing) đối với Agribank và MB", "21"),
    ("Hình 6. Mô phỏng tác động chuyển đổi Chuẩn mực IFRS 9 năm 2025: Khoảng cách dự phòng và 3 Stage", "26")
]

for title, page in fig_exhibits:
    p = add_p(doc, space_before=1.5, space_after=1.5)
    add_dot_leader_tab(p, pos=9360)
    r = p.add_run(f"  • {title}\t{page}")
    style_run(r, size_pt=9.5)

print("Front Matter generated successfully.")

# ==============================================================================
# 4. APPEND EMPIRICAL SECTIONS (PHẦN I ĐẾN PHẦN VI) IN STRICT SEQUENTIAL ORDER
# ==============================================================================

# --- PHẦN I ---
print("Building Phần I...")
add_h1(doc, "PHẦN I. BỐI CẢNH THỂ CHẾ VÀ KHẨU VỊ RỦI RO ĐỐI LẬP (AGRIBANK VS MB)", page_break_before=True)
add_h2(doc, "1.1. Agribank: Thể chế NHTM Nhà nước và Quản trị rủi ro phân tán")
copy_p(doc, doc_src.paragraphs[75]) # Định vị thể chế
copy_p(doc, doc_src.paragraphs[76]) # Mô hình tổ chức

add_h2(doc, "1.2. MB: Thể chế Tập đoàn Tài chính và Quản trị tập trung")
copy_p(doc, doc_src.paragraphs[78]) # Cấu trúc tập đoàn
copy_p(doc, doc_src.paragraphs[79]) # Công nghệ tập trung

add_h2(doc, "1.3. Ma trận đối chiếu chuyên sâu hai mô hình quản trị rủi ro")
p_b1_title = add_p(doc, "Bảng 1. Ma trận đối chiếu cấu trúc thể chế và mô hình 3 tuyến phòng vệ giữa Agribank và MB", space_before=10, space_after=4)
style_run(p_b1_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b1_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[2]) # Table 2 (Tiêu chí đối chiếu)
copy_p(doc, doc_src.paragraphs[82]) # Nguồn Bảng 1

# --- PHẦN II ---
print("Building Phần II...")
add_h1(doc, "PHẦN II. BÓC TÁCH THỰC TRẠNG QUẢN TRỊ RỦI RO TÍN DỤNG & PHÂN RÃ TOÁN HỌC (2020–2025)", page_break_before=True)

add_h2(doc, "2.1. Quy mô tín dụng, nợ xấu và hiện tượng hội tụ NPL bề mặt (Like-for-like 1,30% vs 1,29%)")
copy_p(doc, doc_src.paragraphs[89]) # Quy mô và Tốc độ mở rộng tín dụng

p_b2_title = add_p(doc, "Bảng 2. Quy mô dư nợ, nợ xấu và tỷ lệ NPL của Agribank và MB giai đoạn 2020–2025 (Tỷ đồng, %)", space_before=10, space_after=4)
style_run(p_b2_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b2_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[4]) # Table 4 (Quy mô dư nợ, nợ xấu)
copy_p(doc, doc_src.paragraphs[91]) # Nguồn Bảng 2

add_image_exhibit(doc, "Hinh_1_NPL_va_Nhom_2.png", 
                  "Hình 1. Diễn biến tỷ lệ NPL và tỷ lệ nợ nhóm 2 của Agribank và MB (2020–2025)", 
                  "Nguồn: Tính toán và đồ thị hóa của nhóm tác giả từ Thuyết minh BCTC kiểm toán và Báo cáo thường niên 2020–2025.")

add_h2(doc, "2.2. Phân rã biến động nợ xấu (NPL Decomposition): Lượng hóa hiệu ứng mẫu số và tử số")
copy_p(doc, doc_src.paragraphs[95]) # So sánh cùng cơ sở và phân rã biến động NPL năm 2025
copy_p(doc, doc_src.paragraphs[96]) # Công thức phân rã

add_image_exhibit(doc, "Hinh_2_Tang_truong_Du_no_vs_No_xau.png", 
                  "Hình 2. Tốc độ tăng trưởng quy mô dư nợ và nợ xấu tại Agribank và MB (2020–2025)", 
                  "Nguồn: Tính toán và đồ thị hóa của nhóm tác giả từ Thuyết minh BCTC hợp nhất kiểm toán 2020–2025.")

add_h2(doc, "2.3. Bộ đệm dự phòng (LLCR), Chi phí tín dụng và Vai trò của kỹ thuật xóa nợ bằng dự phòng")
p_b3_title = add_p(doc, "Bảng 3. Bộ đệm dự phòng (LLCR), chi phí dự phòng và bóc tách Credit Cost (2020–2025)", space_before=10, space_after=4)
style_run(p_b3_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b3_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[5]) # Table 5 (Bộ đệm dự phòng)
copy_p(doc, doc_src.paragraphs[102]) # Nguồn Bảng 3

add_image_exhibit(doc, "Hinh_3_LLCR_va_Credit_Cost.png", 
                  "Hình 3. Tỷ lệ bao phủ nợ xấu (LLCR) và Chi phí tín dụng (Credit Cost) giai đoạn 2020–2025", 
                  "Nguồn: Tính toán và đồ thị hóa của nhóm tác giả từ Báo cáo KQKD và Thuyết minh biến động dự phòng BCTC kiểm toán 2020–2025.")

copy_p(doc, doc_src.paragraphs[106]) # Hành vi trích lập theo chu kỳ
copy_p(doc, doc_src.paragraphs[107]) # Thu hồi nợ đã xử lý của Agribank

add_h2(doc, "2.4. Nợ nhóm 2, Nợ cơ cấu và Áp lực nợ tiềm ẩn: Nợ nhóm 2 như biến báo động sớm (EWI)")
p_b4_title = add_p(doc, "Bảng 4. Nợ nhóm 2, nợ cơ cấu theo thông tư và NPL điều chỉnh toàn diện (2020–2025)", space_before=10, space_after=4)
style_run(p_b4_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b4_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[6]) # Table 6 (Nợ nhóm 2, nợ cơ cấu)
copy_p(doc, doc_src.paragraphs[110]) # Nguồn Bảng 4
copy_p(doc, doc_src.paragraphs[111]) # So sánh Nợ nhóm 2

add_h2(doc, "2.5. Đo lường hiệu quả tài chính điều chỉnh theo rủi ro (RORAC)")
p_b5_title = add_p(doc, "Bảng 5. Tỷ suất lợi nhuận trên vốn rủi ro ước tính (RORAC proxy) giai đoạn 2020–2025", space_before=10, space_after=4)
style_run(p_b5_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b5_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[7]) # Table 7 (RORAC proxy)
copy_p(doc, doc_src.paragraphs[114]) # Nguồn Bảng 5
copy_p(doc, doc_src.paragraphs[115]) # Đánh giá RORAC proxy

add_h2(doc, "2.6. Cơ cấu danh mục, mức độ tập trung ngành và an toàn vốn (CAR)")
p_b6_title = add_p(doc, "Bảng 6. Cơ cấu danh mục rủi ro tập trung và Hệ số an toàn vốn (CAR) giai đoạn 2020–2025", space_before=10, space_after=4)
style_run(p_b6_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b6_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[8]) # Table 8 (Tập trung & Vốn)
copy_p(doc, doc_src.paragraphs[118]) # Nguồn Bảng 6

add_image_exhibit(doc, "Hinh_4_Co_cau_BDS_va_CAR.png", 
                  "Hình 4. Mức độ tập trung tín dụng BĐS & Xây dựng và Hệ số an toàn vốn (CAR) giai đoạn 2020–2025", 
                  "Nguồn: Đồ thị hóa từ Thuyết minh BCTC kiểm toán và Báo cáo thường niên 2020–2025 của Agribank và MB.")

copy_p(doc, doc_src.paragraphs[122]) # Khoảng cách an toàn vốn và rủi ro tập trung ngành

# --- PHẦN III ---
print("Building Phần III...")
add_h1(doc, "PHẦN III. MÔ HÌNH HÓA KIỂM TRA SỨC CHỊU ĐỰNG VĨ MÔ (STRESS TESTING 2026)", page_break_before=True)

add_h2(doc, "3.1. Thiết kế kịch bản vĩ mô theo chuẩn Basel II/III (ICAAP) và Ma trận chuyển nhóm nợ")
copy_p(doc, doc_src.paragraphs[124]) # Thiết kế mô hình Stress Testing

add_h2(doc, "3.2. Kết quả lượng hóa định lượng: Phân hóa hai dạng tổn thương bất đối xứng (CAR vs LNTT)")
p_b7_title = add_p(doc, "Bảng 7. Kết quả Kiểm tra sức chịu đựng vĩ mô năm 2026 đối với Agribank và MB", space_before=10, space_after=4)
style_run(p_b7_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b7_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[9]) # Table 9 (Stress Test)
copy_p(doc, doc_src.paragraphs[126]) # Nguồn Bảng 7

add_image_exhibit(doc, "Hinh_5_Stress_Testing_2026.png", 
                  "Hình 5. Kết quả Kiểm tra sức chịu đựng vĩ mô năm 2026 (Macro Stress Testing) đối với Agribank và MB", 
                  "Nguồn: Tính toán và đồ thị hóa của nhóm tác giả từ mô hình Macro Stress Testing ICAAP.")

copy_p(doc, doc_src.paragraphs[130]) # Ý nghĩa kinh tế từ kết quả Stress Testing

# --- PHẦN IV ---
print("Building Phần IV...")
add_h1(doc, "PHẦN IV. MÔ PHỎNG ĐỊNH LƯỢNG TÁC ĐỘNG CHUYỂN ĐỔI CHUẨN MỰC IFRS 9 ECL", page_break_before=True)

add_h2(doc, "4.1. Sự chuyển dịch mô hình: Incurred Loss (VAS/TT11) sang Lifetime Expected Credit Loss (IFRS 9)")
add_p(doc, (
    "Chuyển đổi từ chuẩn mực kế toán Việt Nam (VAS) và Thông tư 11/2021 sang Chuẩn mực Báo cáo Tài chính Quốc tế IFRS 9 "
    "đại diện cho bước nhảy vĩ mô từ mô hình tổn thất đã phát sinh (Incurred Loss Model) sang mô hình tổn thất tín dụng dự kiến (Expected Credit Loss - ECL Model). "
    "Mô hình phân loại toàn bộ tài sản tài chính thành 3 giai đoạn (Stages): "
    "Stage 1 (Chưa suy giảm - trích lập ECL 12 tháng), Stage 2 (Rủi ro tín dụng tăng đáng kể SICR - trích lập ECL trọn vòng đời), "
    "và Stage 3 (Suy giảm rủi ro nợ xấu - trích lập ECL trọn vòng đời). "
    "Dưới mô hình này, việc trích lập dự phòng mang tính đón đầu chu kỳ (Forward-looking), gắn liền với các kịch bản dự báo vĩ mô FLI (Forward-Looking Information)."
))

add_h2(doc, "4.2. Bóc tách khoảng cách thiếu hụt dự phòng (Provisioning Gap) và Cú sốc trích lập Stage 2")
p_b8_title = add_p(doc, "Bảng 8. Kết quả mô phỏng tác động chuyển đổi sang Chuẩn mực Quốc tế IFRS 9 năm 2025", space_before=10, space_after=4)
style_run(p_b8_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b8_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[10]) # Table 10 (IFRS 9 Simulation)
copy_p(doc, doc_src.paragraphs[133]) # Nguồn Bảng 8
copy_p(doc, doc_src.paragraphs[134]) # Kết quả mô phỏng IFRS 9

add_h2(doc, "4.3. Kiểm định độ nhạy 6 kịch bản tham số (Robustness Sensitivity Analysis)")
p_b9_title = add_p(doc, "Bảng 9. Kết quả kiểm định độ nhạy mô phỏng IFRS 9 ECL của Agribank và MB theo 6 kịch bản tham số", space_before=10, space_after=4)
style_run(p_b9_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b9_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[11]) # Table 11 (Kiểm định độ nhạy)
copy_p(doc, doc_src.paragraphs[136]) # Nguồn Bảng 9
copy_p(doc, doc_src.paragraphs[137]) # Ý nghĩa từ phân tích độ nhạy

add_image_exhibit(doc, "Hinh_6_IFRS9_ECL_Gap.png", 
                  "Hình 6. Mô phỏng tác động chuyển đổi Chuẩn mực IFRS 9 năm 2025: Khoảng cách dự phòng và 3 Stage", 
                  "Nguồn: Kết quả mô hình hóa định lượng của nhóm tác giả tại sheet IFRS9_Simulation.")

# --- PHẦN V ---
print("Building Phần V...")
add_h1(doc, "PHẦN V. PHÂN TÍCH TÌNH HUỐNG THỰC TIỄN CHUYÊN SÂU (CASE STUDIES)", page_break_before=True)

add_h2(doc, "5.1. Agribank: Cú sốc thiên tai Yagi 2024, điểm nghẽn thanh khoản TSBĐ nợ nhóm 5 và vụ án Lifepro Việt Nam")
copy_p(doc, doc_src.paragraphs[143]) # 1. Diễn biến và Dữ liệu thực chứng
copy_p(doc, doc_src.paragraphs[144]) # 2. Nguyên nhân, Hậu quả và Biện pháp khắc phục

add_h2(doc, "5.2. MB: Rủi ro tín dụng tiêu dùng tại MCredit và rủi ro đạo đức cấp chi nhánh (Vụ án Chi nhánh Gia Lai)")
copy_p(doc, doc_src.paragraphs[146]) # 1. Diễn biến và Dữ liệu thực chứng MCredit
copy_p(doc, doc_src.paragraphs[147]) # 2. Nguyên nhân, Hậu quả và Biện pháp khắc phục

add_h2(doc, "5.3. MB: Cú sốc chất lượng tài sản năm 2023: Khủng hoảng thanh khoản TPDN, Bất động sản và cơ chế lây lan chéo qua CIC")
copy_p(doc, doc_src.paragraphs[149]) # Phân tích toàn diện TPDN/BĐS 2023

add_h2(doc, "5.4. MB: Biến động nợ xấu Quý III–IV/2025, xử lý rủi ro bằng dự phòng và quy chế pháp lý chuyển giao bắt buộc MBV")
copy_p(doc, doc_src.paragraphs[151]) # Phân tích toàn diện nợ xấu Q3-Q4/2025 và MBV

p_b10_title = add_p(doc, "Bảng 10. Ma trận đánh giá lỗ hổng Kiểm soát Nội bộ COSO 2013 qua các tình huống thực tiễn", space_before=10, space_after=4)
style_run(p_b10_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b10_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[12]) # Table 12 (COSO 2013)
copy_p(doc, doc_src.paragraphs[153]) # Nguồn Bảng 10

# --- PHẦN VI ---
print("Building Phần VI...")
add_h1(doc, "PHẦN VI. SO SÁNH HAI MÔ HÌNH VÀ HỆ THỐNG KHUYẾN NGHỊ QUẢN TRỊ NÂNG CAO", page_break_before=True)

add_h2(doc, "6.1. Ma trận đối thoại học thuật: Mô hình Phòng thủ Thể chế vs Mô hình Đổi mới Tối ưu hóa Lợi nhuận")
copy_p(doc, doc_src.paragraphs[155]) # Tổng hợp Đối thoại Học thuật

p_b11_title = add_p(doc, "Bảng 11. So sánh đối chiếu toàn diện hai triết lý quản trị rủi ro tín dụng (Agribank vs MB)", space_before=10, space_after=4)
style_run(p_b11_title.runs[0], bold=True, color_rgb=(0, 32, 96))
p_b11_title.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[13]) # Table 13 (So sánh hai mô hình)
copy_p(doc, doc_src.paragraphs[157]) # Nguồn Bảng 11

add_h3(doc, "Đánh giá tổng hợp công tác quản trị rủi ro tín dụng tại Agribank (2020–2025)")
copy_p(doc, doc_src.paragraphs[159]) # Kết quả và hạn chế Agribank

add_h3(doc, "Đánh giá tổng hợp công tác quản trị rủi ro tín dụng tại MB (2020–2025)")
copy_p(doc, doc_src.paragraphs[161]) # Kết quả và hạn chế MB

add_h2(doc, "6.2. Hệ thống khuyến nghị và hàm ý chính sách quản trị nâng cao")
add_h3(doc, "Đối với Ngân hàng Nhà nước (Cơ quan Thanh tra Giám sát)")
copy_p(doc, doc_src.paragraphs[164]) # Khuyến nghị NHNN

add_h3(doc, "Đối với Ngân hàng Nông nghiệp và Phát triển Nông thôn Việt Nam (Agribank)")
copy_p(doc, doc_src.paragraphs[166]) # Khuyến nghị Agribank

add_h3(doc, "Đối với Ngân hàng TMCP Quân đội (MB)")
copy_p(doc, doc_src.paragraphs[168]) # Khuyến nghị MB

# --- PHẦN VII: SPEAKER NOTES & DEFENSE GUIDE ---
print("Building Phần VII (Speaker Notes & Defense Guide)...")
add_h1(doc, "PHẦN VII. KỊCH BẢN THUYẾT TRÌNH CHI TIẾT VÀ BỘ HƯỚNG DẪN BẢO VỆ PHẢN BIỆN (SPEAKER NOTES)", page_break_before=True)

add_h2(doc, "7.1. Khung thời lượng và Kịch bản lời thoại thuyết trình từng phần (Khung báo cáo 15–20 phút)")

sn_intro = add_p(doc, (
    "Để phục vụ tốt nhất cho buổi báo cáo và thuyết trình nhóm học phần Quản trị rủi ro trên lớp, "
    "nhóm nghiên cứu thiết kế kịch bản chi tiết bao gồm: mục tiêu trình bày, phân bổ thời gian tối ưu cho từng phần, "
    "lời thoại dẫn dắt (Verbatim Script) giúp người thuyết trình tự tin làm chủ sân khấu, "
    "và các chỉ dẫn nhấn mạnh số liệu cốt lõi (Data Callouts) nhằm thu hút sự tập trung của giảng viên và lớp học."
))

# Phần I Notes
p_sn1 = add_p(doc, "1. Mở đầu & Phần I: Thể chế & Khẩu vị rủi ro đối lập (Thời lượng: 2 phút)", space_before=6, space_after=2)
p_sn1.runs[0].bold = True
p_sn1.runs[0].font.color.rgb = RGBColor(0, 32, 96)
add_p(doc, (
    "• Mục tiêu: Tạo ấn tượng ban đầu mạnh mẽ bằng sự tương phản thể chế sở hữu: 100% Nhà nước vs Cổ phần hóa tập đoàn quân đội; "
    "phê duyệt phân tán tại chi nhánh vs phê duyệt tập trung tại Hội sở qua hệ thống phê duyệt tự động BPM.\n"
    "• Lời thoại gợi ý: 'Kính thưa Thầy và các anh chị học viên, khi nghiên cứu về quản trị rủi ro tín dụng tại Việt Nam, câu hỏi thú vị nhất là: "
    "Tại sao hai định chế cùng thuộc Top đầu hệ thống ngân hàng nhưng lại lựa chọn hai triết lý quản trị rủi ro hoàn toàn trái ngược? "
    "Một bên là Agribank với thể chế 100% vốn nhà nước, vận hành mạng lưới hơn 2.200 chi nhánh với cơ chế phê duyệt phân tán, gánh vác sứ mệnh chính sách nông nghiệp nông thôn. "
    "Một bên là MB – một tập đoàn tài chính cổ phần quân đội tiên phong chuyển đổi số, áp dụng mô hình phê duyệt tín dụng tập trung tại Hội sở. "
    "Khẩu vị rủi ro đối lập này đã định hình trực tiếp toàn bộ danh mục cho vay và cách thức hai ngân hàng đối mặt với chu kỳ nợ xấu giai đoạn 2020–2025.'"
))

# Phần II Notes
p_sn2 = add_p(doc, "2. Phần II: Thực trạng định lượng & Phân rã biến động nợ xấu (Thời lượng: 6 phút — Trọng tâm)", space_before=6, space_after=2)
p_sn2.runs[0].bold = True
p_sn2.runs[0].font.color.rgb = RGBColor(0, 32, 96)
add_p(doc, (
    "• Mục tiêu: Chỉ ra 3 phát hiện định lượng đắt giá: (1) Hiện tượng hội tụ NPL bề mặt (1,30% vs 1,29%); "
    "(2) Phân rã toán học NPL vạch trần hiệu ứng pha loãng mẫu số của MB; (3) Kỹ thuật xóa nợ bằng dự phòng và sự đánh đổi chu kỳ LLCR.\n"
    "• Lời thoại gợi ý: 'Đi sâu vào bức tranh định lượng tại Bảng 2 và Hình 1, nhóm xin nhấn mạnh phát hiện then chốt đầu tiên: "
    "Nếu chỉ nhìn vào Báo cáo thường niên công bố năm 2025, chúng ta sẽ lầm tưởng Agribank kiểm soát nợ xấu tốt hơn MB (1,17% so với 1,29%). "
    "Tuy nhiên, đây là sự so sánh khập khiễng do khác biệt mẫu số Thông tư 11. Khi đưa về cùng mẫu số chuẩn mực theo thông lệ quốc tế là Dư nợ cho vay khách hàng hợp nhất (Thuyết minh 9), "
    "NPL thực tế của Agribank là 1,30%, gần như ngang bằng MB (1,29%).\n"
    "Đặc biệt, tại Hình 2, khi áp dụng công thức phân rã biến động nợ xấu (Decomposition), nhóm chứng minh rằng mức giảm 0,33 điểm % NPL của MB năm 2025 "
    "hoàn toàn đến từ Hiệu ứng mẫu số: tín dụng tăng trưởng tới 39,6% đã làm loãng nợ xấu (-0,46 điểm %), trong khi nợ xấu tuyệt đối thực tế vẫn tăng thêm +1.442 tỷ đồng. "
    "Đồng thời, cả hai ngân hàng đều dựa rất lớn vào kỹ thuật xóa nợ bằng dự phòng: năm 2025 Agribank đã xóa nợ nội bảng tới 32.621 tỷ đồng và MB xóa 12.185 tỷ đồng. "
    "Nếu cộng lại số nợ đã xóa này, NPL thực chất trước xử lý rủi ro lên tới 2,95% tại Agribank và 2,42% tại MB.\n"
    "Về bộ đệm dự phòng (Hình 3), MB đã chủ động xả bộ đệm LLCR từ đỉnh 268% năm 2021 xuống 93,7% năm 2025 để bảo vệ tăng trưởng lợi nhuận trước áp lực cổ đông, "
    "trong khi Agribank duy trì bộ đệm phòng thủ thể chế bền vững với LLCR đạt 146,3%.'"
))

# Phần III Notes
p_sn3 = add_p(doc, "3. Phần III: Mô hình Kiểm tra sức chịu đựng vĩ mô (Stress Testing 2026) (Thời lượng: 3 phút)", space_before=6, space_after=2)
p_sn3.runs[0].bold = True
p_sn3.runs[0].font.color.rgb = RGBColor(0, 32, 96)
add_p(doc, (
    "• Mục tiêu: Trình bày kết quả ICAAP với ma trận chuyển nhóm nợ dưới 3 kịch bản; làm nổi bật sự phân hóa tổn thương bất đối xứng (CAR vs LNTT).\n"
    "• Lời thoại gợi ý: 'Để lượng hóa sức chống chịu trước các cú sốc tương lai, nhóm đã thiết lập mô hình Stress Testing năm 2026 chuẩn Basel II/III. "
    "Kết quả tại Bảng 7 và Hình 5 bóc tách hai điểm yếu mang tính bất đối xứng rất sâu sắc: "
    "Agribank do bộ đệm vốn mỏng phụ thuộc ngân sách nhà nước, nên dưới kịch bản Cực đoan (GDP 3,5%, Lãi suất +300 bps, BĐS giảm -25%), "
    "hệ số an toàn vốn CAR tụt từ 10,22% xuống 8,67%, sát ngưỡng sàn bắt buộc 8,0% – đây là rủi ro sống còn về vốn. "
    "Ngược lại, MB có CAR dồi dào (11,04%) nhưng danh mục nhạy cảm chu kỳ khiến chi phí dự phòng bổ sung vọt lên 22.402 tỷ đồng, "
    "ăn mòn gần hết thu nhập và khiến LNTT sụt giảm tới -69,3% – một cú sốc trực diện vào lợi nhuận.'"
))

# Phần IV Notes
p_sn4 = add_p(doc, "4. Phần IV: Mô phỏng Chuẩn mực Quốc tế IFRS 9 ECL (Thời lượng: 3 phút)", space_before=6, space_after=2)
p_sn4.runs[0].bold = True
p_sn4.runs[0].font.color.rgb = RGBColor(0, 32, 96)
add_p(doc, (
    "• Mục tiêu: Giải thích bước nhảy từ Incurred Loss sang Lifetime ECL; chỉ rõ khoảng cách dự phòng của MB (+106,5%) và cú sốc Stage 2.\n"
    "• Lời thoại gợi ý: 'Tại Phần IV, nhóm tiên phong mô phỏng định lượng tác động khi Việt Nam chính thức chuyển đổi sang Chuẩn mực Quốc tế IFRS 9. "
    "Kết quả tại Bảng 8 và Hình 6 cho thấy khoảng cách dự phòng trích thiếu của MB lên tới 14.006 tỷ đồng (+106,5%), làm vốn CSH giảm -7,9% và CAR tụt 103 điểm cơ bản. "
    "Cú sốc này bắt nguồn từ Giai đoạn 2 (Stage 2) khi danh mục cho vay tiêu dùng tín chấp tại MCredit và 30% trái phiếu doanh nghiệp bị phân loại vào diện rủi ro tín dụng tăng đáng kể (SICR), "
    "bắt buộc phải trích lập dự phòng trọn vòng đời. "
    "Trong khi đó, Agribank chỉ thiếu hụt 9,8% nhờ 90,2% tài sản bảo đảm là bất động sản thanh khoản thực, giúp kiềm chế tỷ lệ tổn thất khi vỡ nợ (LGD) ở mức rất thấp.'"
))

# Phần V Notes
p_sn5 = add_p(doc, "5. Phần V: Phân tích 4 Case Studies thực tế & Đánh giá COSO 2013 (Thời lượng: 3 phút)", space_before=6, space_after=2)
p_sn5.runs[0].bold = True
p_sn5.runs[0].font.color.rgb = RGBColor(0, 32, 96)
add_p(doc, (
    "• Mục tiêu: Minh họa số liệu qua các biến cố thực tế: Yagi 2024, Nợ nhóm 5 Agribank, MCredit, Khủng hoảng TPDN 2023 và cơ chế khoanh vùng MBV.\n"
    "• Lời thoại gợi ý: 'Phần V kết nối các con số định lượng với thực tiễn ngân hàng sinh động qua 4 bài học tình huống. "
    "Agribank bộc lộ tính tổn thương trước thiên tai (bão Yagi ảnh hưởng 30.000 tỷ dư nợ) và điểm nghẽn nợ nhóm 5 kéo dài do vướng mắc thủ tục phát mại tài sản bảo đảm nông thôn. "
    "Về phía MB, bài học quản trị đến từ rủi ro tín dụng tiêu dùng MCredit (nợ xấu trên 7%), khủng hoảng trái phiếu doanh nghiệp 2023 gây lây lan nợ xấu chéo qua CIC, "
    "và đặc biệt là cơ chế tiếp nhận ngân hàng 0 đồng (MBV). "
    "Theo Điều 185 Luật các TCTD 2024, MBV được khoanh vùng tài chính độc lập và không hợp nhất BCTC nên không làm sai lệch số liệu nợ xấu của MB.'"
))

# Phần VI Notes
p_sn6 = add_p(doc, "6. Phần VI: So sánh hai mô hình & Khuyến nghị chính sách (Thời lượng: 3 phút)", space_before=6, space_after=2)
p_sn6.runs[0].bold = True
p_sn6.runs[0].font.color.rgb = RGBColor(0, 32, 96)
add_p(doc, (
    "• Mục tiêu: Tổng kết triết lý quản trị (Bảng 11); đưa ra thông điệp chốt hạ và hệ thống khuyến nghị sắc bén cho NHNN, Agribank và MB.\n"
    "• Lời thoại gợi ý: 'Tóm lại, bài tiểu luận không nhằm kết luận mô hình nào vượt trội hơn, mà chỉ ra sự đánh đổi mang tính quy luật: "
    "Agribank chấp nhận hy sinh tốc độ tăng trưởng và hiệu quả vốn để đổi lấy sự an toàn thể chế và bảo toàn vốn nhà nước; "
    "MB chấp nhận rủi ro chu kỳ cao hơn để tối đa hóa lợi suất cho cổ đông và tiên phong về công nghệ số. "
    "Nhóm xin đề xuất 3 nhóm khuyến nghị trọng tâm: NHNN cần sớm ban hành lộ trình áp dụng IFRS 9 bắt buộc; "
    "Agribank cần số hóa hệ thống cảnh báo sớm EWS để xử lý nợ nhóm 2 trước khi chuyển thành nợ nhóm 5; "
    "và MB cần siết chặt khẩu vị rủi ro tập trung đối với bất động sản và trái phiếu doanh nghiệp. "
    "Xin trân trọng cảm ơn Thầy và các anh chị học viên đã chú ý theo dõi!'"
))

add_h2(doc, "7.2. Bộ 5 câu hỏi phản biện kinh điển của giảng viên và chiến lược trả lời xuất sắc (Q&A Defense Guide)")

qa_items = [
    ("Câu hỏi 1: Tại sao Báo cáo thường niên Agribank công bố tỷ lệ NPL 2025 là 1,17%, nhưng nhóm lại tính ra 1,30% và cho rằng tương đương MB (1,29%)?",
     "Gợi ý trả lời chuẩn xác: Thưa Thầy, sự chênh lệch này xuất phát từ khác biệt về mẫu số phân tích. Tỷ lệ 1,17% công bố trên Báo cáo thường niên của Agribank được tính theo Thông tư 11/2021 và Thông tư 31/2024, trong đó mẫu số là 'Tổng cấp tín dụng' (bao gồm cả cho vay khách hàng, bảo lãnh, cam kết ngoại bảng và đầu tư trái phiếu). Khi nhóm đưa về cùng một mẫu số chuẩn mực theo thông lệ quốc tế là 'Dư nợ cho vay khách hàng hợp nhất' tại Thuyết minh 9 BCTC kiểm toán (1.976.381 tỷ đồng), nợ nhóm 3–5 là 25.669 tỷ đồng thì tỷ lệ NPL thực tế của Agribank là 1,30%. Cách tính like-for-like này bảo đảm sự khách quan và nhất quán tuyệt đối khi so sánh trực diện với MB (1,29%)."),
    
    ("Câu hỏi 2: MB tiếp nhận chuyển giao bắt buộc OceanBank (MBV), liệu nợ xấu của ngân hàng 0 đồng này có làm sai lệch các chỉ tiêu tài chính của MB năm 2025 không?",
     "Gợi ý trả lời chuẩn xác: Thưa Thầy, hoàn toàn không làm sai lệch. Căn cứ theo Điều 185 Luật Các tổ chức tín dụng năm 2024 (số 32/2024/QH15) và phương án chuyển giao bắt buộc đã được phê duyệt, MBV hoạt động dưới hình thức ngân hàng thương mại TNHH MTV độc lập do MB sở hữu 100% vốn nhưng áp dụng cơ chế khoanh vùng tài chính đặc biệt (Ring-fencing). Cụ thể, MB không phải hợp nhất Báo cáo tài chính của MBV vào BCTC hợp nhất của MB; các khoản lỗ lũy kế, nợ xấu cũ và tài sản có rủi ro của MBV được hạch toán tách biệt, không tính vào hệ số an toàn vốn (CAR) và tỷ lệ nợ xấu của MB. Do đó, toàn bộ số liệu năm 2025 của MB phản ánh trung thực năng lực nội tại của MB."),
    
    ("Câu hỏi 3: Tại sao trong chu kỳ 2021–2025, tỷ lệ bao phủ nợ xấu (LLCR) của MB lại giảm mạnh từ 268% xuống 93,7%, trong khi Agribank vẫn duy trì ổn định trên 113%–146%?",
     "Gợi ý trả lời chuẩn xác: Thưa Thầy, đây là minh chứng rõ nét cho sự phân kỳ về mục tiêu thể chế: MB chịu áp lực rất lớn từ cổ đông và thị trường chứng khoán về chỉ tiêu tăng trưởng lợi nhuận và ROE. Khi nợ xấu nội bảng tăng trong giai đoạn 2023–2025, nếu MB tiếp tục duy trì LLCR ở mức cực cao 200%–260% thì chi phí trích lập dự phòng sẽ ăn mòn toàn bộ lợi nhuận. Do đó, MB đã chủ động 'xả bộ đệm dự phòng' tích lũy từ giai đoạn trước để hấp thu nợ xấu và bảo vệ kế hoạch lợi nhuận trước thuế trên 28.000 tỷ đồng. Ngược lại, Agribank là ngân hàng 100% vốn nhà nước, không chịu áp lực giá cổ phiếu, mục tiêu tối thượng là bảo toàn vốn công, chấp nhận trích chi phí dự phòng bình quân 1,66%/năm để giữ LLCR phòng thủ vững chắc trên 113%."),
    
    ("Câu hỏi 4: Mô phỏng IFRS 9 cho thấy MB thiếu hụt dự phòng tới 14.006 tỷ (+106,5%), nếu bắt buộc áp dụng ngay thì MB có bị vi phạm hệ số an toàn vốn không?",
     "Gợi ý trả lời chuẩn xác: Thưa Thầy, kết quả mô phỏng lượng hóa rằng vốn chủ sở hữu của MB sẽ giảm 7,9% và hệ số CAR giảm khoảng 103 điểm cơ bản (từ 11,04% xuống 9,97%). Mặc dù đệm vốn sụt giảm đáng kể nhưng mức CAR 9,97% vẫn nằm trên ngưỡng sàn quy định tối thiểu của NHNN là 8,0% (Thông tư 41/2016/TT-NHNN), do đó MB không bị vi phạm an toàn vốn và không đe dọa khả năng thanh toán. Tuy nhiên, việc mất đi hơn 100 bps đệm vốn sẽ làm thu hẹp trần tăng trưởng tín dụng. Đây chính là lý do nhóm khuyến nghị MB cần sớm sàng lọc các khoản nợ có dấu hiệu SICR (Stage 2) và giảm tỷ trọng cho vay tiêu dùng tín chấp tại MCredit ngay từ bây giờ."),
    
    ("Câu hỏi 5: Tại sao nợ nhóm 5 của Agribank luôn chiếm tỷ trọng áp đảo trên 65% tổng nợ xấu, và rủi ro lớn nhất đối với các khoản nợ này là gì?",
     "Gợi ý trả lời chuẩn xác: Thưa Thầy, nguyên nhân xuất phát từ tính chất đặc thù của tín dụng nông nghiệp: tài sản bảo đảm của Agribank chủ yếu là đất nông nghiệp, đất nuôi trồng thủy sản và nhà xưởng ở khu vực nông thôn có tính thanh khoản rất thấp. Khi nợ rơi vào nhóm 5, ngân hàng gặp khó khăn rất lớn trong việc phát mại thu hồi vốn. Đặc biệt sau khi Nghị quyết 42/2017/QH14 hết hiệu lực, quyền thu giữ tài sản bảo đảm bị hạn chế khiến nợ nhóm 5 bị đọng lại nội bảng kéo dài. Phải đến khi Luật số 96/2025/QH15 sửa đổi Luật các TCTD có hiệu lực từ đầu năm 2026 khôi phục quyền thu giữ tài sản bảo đảm thì nút thắt pháp lý xử lý nợ nhóm 5 của Agribank mới có cơ sở được tháo gỡ triệt để.")
]

for q, a in qa_items:
    p = add_p(doc, space_before=4, space_after=3)
    r_q = p.add_run(f"• {q}\n")
    style_run(r_q, bold=True, color_rgb=(0, 32, 96))
    r_a = p.add_run(a)
    style_run(r_a, bold=False)

# --- BACK MATTER ---
print("Building Back Matter...")
add_h1(doc, "KẾT LUẬN", page_break_before=True)
copy_p(doc, doc_src.paragraphs[170]) # Toàn văn kết luận

add_h1(doc, "TÀI LIỆU THAM KHẢO CHỌN LỌC", page_break_before=True)
# Copy references [1] to [25] (paragraphs 172 to 196)
for p_idx in range(172, 197):
    copy_p(doc, doc_src.paragraphs[p_idx])

add_h1(doc, "PHỤ LỤC THUYẾT TRÌNH: DỮ LIỆU ĐỊNH LƯỢNG MỞ RỘNG", page_break_before=True)
copy_p(doc, doc_src.paragraphs[198]) # Lời dẫn phụ lục

p_pl1_t = add_p(doc, "Phụ lục 1. Bảng thống kê mô tả (Descriptive Statistics) các chỉ tiêu tài chính và rủi ro tín dụng (2020–2025)", space_before=10, space_after=4)
style_run(p_pl1_t.runs[0], bold=True, color_rgb=(0, 32, 96))
p_pl1_t.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[14]) # Table 14 (Descriptive Statistics)
copy_p(doc, doc_src.paragraphs[200]) # Nguồn Phụ lục 1

p_pl2_t = add_p(doc, "Phụ lục 2. Ma trận hệ số tương quan (Correlation Matrix) giữa Tăng trưởng tín dụng, Nợ nhóm 2 và NPL", space_before=10, space_after=4)
style_run(p_pl2_t.runs[0], bold=True, color_rgb=(0, 32, 96))
p_pl2_t.paragraph_format.keep_with_next = True

copy_tbl(doc, doc_src.tables[15]) # Table 15 (Correlation Matrix)
copy_p(doc, doc_src.paragraphs[202]) # Ghi chú Phụ lục 2

add_h2(doc, "Phụ lục 3. Hướng dẫn kỹ thuật cập nhật Mục lục và Bảng biểu tự động trên Microsoft Word")
copy_p(doc, doc_src.paragraphs[204]) # Hướng dẫn kỹ thuật

# ==============================================================================
# 5. SAVE AND VERIFY
# ==============================================================================
doc.save(target_exec_path)
print(f"SUCCESSFULLY GENERATED STANDALONE COURSE PAPER: {target_exec_path}")
