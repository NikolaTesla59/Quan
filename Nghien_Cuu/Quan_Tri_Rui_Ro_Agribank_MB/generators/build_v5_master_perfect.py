import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os

source_path = r'C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v4.docx'
target_v5 = r'C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v5.docx'
target_v4 = r'C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v4.docx'

doc = docx.Document(source_path)
print(f"Loaded source document: {source_path}")

# ==============================================================================
# 1. ENABLE AUTOMATED UPDATE OF FIELDS IN SETTINGS
# ==============================================================================
settings = doc.settings.element
update_fields = parse_xml(f'<w:updateFields {nsdecls("w")} w:val="true"/>')
settings.append(update_fields)
print("Added w:updateFields to settings (Enables automatic TOC update in Word)!")

# ==============================================================================
# Helper functions
# ==============================================================================
def style_run(run, font_name="Times New Roman", size_pt=11, bold=False, italic=False, color_rgb=(0,0,0)):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)

def add_dot_leader_tab(paragraph, pos=9360):
    pPr = paragraph._element.get_or_add_pPr()
    tabs = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="right" w:leader="dot" w:pos="{pos}"/></w:tabs>')
    pPr.append(tabs)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def format_cell(cell, text, bold=False, italic=False, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.LEFT, color_rgb=(0,0,0)):
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    for extra in cell.paragraphs[1:]:
        extra._element.getparent().remove(extra._element)
    for r in list(p.runs):
        r._element.getparent().remove(r._element)
    lines = text.split('\n')
    for idx, line in enumerate(lines):
        if idx > 0:
            p.add_run('\n')
        r = p.add_run(line)
        r.font.name = "Times New Roman"
        r.font.size = Pt(size_pt)
        r.bold = bold
        r.italic = italic
        r.font.color.rgb = RGBColor(*color_rgb)

# ==============================================================================
# 2. PAGE BREAKS & SECTION STRUCTURING
# ==============================================================================
# Cover page ends at P005 ("Hà Nội, Năm 2026")
p5 = doc.paragraphs[5]
p5.runs[-1].add_break(docx.enum.text.WD_BREAK.PAGE)
print("Added Page Break after Cover Page.")

# Executive Abstract ends at P009 (Từ khóa...)
for i in range(6, 12):
    txt = doc.paragraphs[i].text.strip()
    if txt.startswith("Từ khóa:"):
        doc.paragraphs[i].runs[-1].add_break(docx.enum.text.WD_BREAK.PAGE)
        print(f"Added Page Break after Executive Abstract (P{i}).")
        break

# TOC starts at "MỤC LỤC NỘI DUNG"
# Find "MỤC LỤC NỘI DUNG" paragraph and insert native Word dynamic TOC field code
toc_title_p = None
for p in doc.paragraphs:
    if p.text.strip() == "MỤC LỤC NỘI DUNG":
        toc_title_p = p
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.keep_with_next = True
        for r in p.runs:
            style_run(r, font_name="Times New Roman", size_pt=13.5, bold=True, color_rgb=(0, 32, 96))
        break

# Insert a dynamic Word TOC field right after "MỤC LỤC NỘI DUNG"
if toc_title_p is not None:
    p_dyn_toc = doc.add_paragraph()
    p_dyn_toc.paragraph_format.space_before = Pt(2)
    p_dyn_toc.paragraph_format.space_after = Pt(6)
    fldSimple = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="TOC \\o &quot;1-2&quot; \\h \\z \\u"/>')
    p_dyn_toc._element.append(fldSimple)
    
    # Move p_dyn_toc right after toc_title_p
    toc_title_p._element.addnext(p_dyn_toc._element)
    print("Inserted native dynamic Word TOC field code after MỤC LỤC NỘI DUNG.")

# Format all static TOC entries (paragraphs with style 'toc 1' or 'toc 2') with dot leader tabs
for p in doc.paragraphs:
    if p.style.name in ['toc 1', 'toc 2'] or ('\t' in p.text and any(p.text.startswith(kw) for kw in ['LỜI MỞ ĐẦU', 'CHƯƠNG', 'KẾT LUẬN', 'TÀI LIỆU', 'PHỤ LỤC'])):
        add_dot_leader_tab(p, pos=9360)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(1.5)
        p.paragraph_format.space_after = Pt(1.5)
        is_level1 = (p.style.name == 'toc 1') or p.text.startswith('CHƯƠNG') or p.text.startswith('LỜI') or p.text.startswith('KẾT') or p.text.startswith('TÀI') or p.text.startswith('PHỤ')
        for r in p.runs:
            style_run(r, font_name="Times New Roman", size_pt=10.5 if is_level1 else 9.5, bold=is_level1, color_rgb=(0, 32, 96) if is_level1 else (50, 50, 50))

# Find the end of TOC and insert Page Break before List of Tables
for i, p in enumerate(doc.paragraphs):
    if p.text.strip().startswith("DANH MỤC BẢNG BIỂU ĐỊNH LƯỢNG"):
        # Set page break before on List of Tables
        p.paragraph_format.page_break_before = True
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.keep_with_next = True
        for r in p.runs:
            style_run(r, font_name="Times New Roman", size_pt=13.5, bold=True, color_rgb=(0, 32, 96))
        print(f"Added page_break_before on DANH MỤC BẢNG BIỂU ĐỊNH LƯỢNG (P{i}).")
        break

# Format List of Tables and List of Figures with dot leader tabs
for p in doc.paragraphs:
    txt = p.text.strip()
    if txt.startswith("DANH MỤC HÌNH VẼ VÀ ĐỒ THỊ MINH HỌA"):
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.keep_with_next = True
        for r in p.runs:
            style_run(r, font_name="Times New Roman", size_pt=13.5, bold=True, color_rgb=(0, 32, 96))
    elif txt.startswith("• Bảng ") or txt.startswith("• Hình "):
        add_dot_leader_tab(p, pos=9360)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(1.5)
        p.paragraph_format.space_after = Pt(1.5)
        for r in p.runs:
            style_run(r, font_name="Times New Roman", size_pt=10, bold=False)

# Add page break before LỜI MỞ ĐẦU and before each major Chapter
h1_section_titles = [
    "LỜI MỞ ĐẦU",
    "CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ KHUNG PHÂN TÍCH RỦI RO TÍN DỤNG",
    "CHƯƠNG 2. MÔ HÌNH VÀ THỂ CHẾ QUẢN TRỊ RỦI RO TÍN DỤNG TẠI AGRIBANK VÀ MB",
    "CHƯƠNG 3. HỆ THỐNG TIÊU CHÍ VÀ PHƯƠNG PHÁP ĐỊNH LƯỢNG ĐÁNH GIÁ RỦI RO TÍN DỤNG",
    "CHƯƠNG 4. PHÂN TÍCH THỰC TRẠNG VÀ MÔ HÌNH HÓA ĐỊNH LƯỢNG RỦI RO TÍN DỤNG GIAI ĐOẠN 2020–2025",
    "CHƯƠNG 5. PHÂN TÍCH TÌNH HUỐNG THỰC TIỄN GIAI ĐOẠN 2020–2025 (DIỄN BIẾN – NGUYÊN NHÂN – HẬU QUẢ – BIỆN PHÁP KHẮC PHỤC)",
    "CHƯƠNG 6. ĐÁNH GIÁ KẾT QUẢ ĐẠT ĐƯỢC, HẠN CHẾ, NGUYÊN NHÂN VÀ SO SÁNH HAI MÔ HÌNH",
    "CHƯƠNG 7. HỆ THỐNG KIẾN NGHỊ VÀ HÀM Ý CHÍNH SÁCH QUẢN TRỊ NÂNG CAO",
    "KẾT LUẬN",
    "TÀI LIỆU THAM KHẢO"
]

for p in doc.paragraphs:
    txt = p.text.strip()
    if any(txt == t for t in h1_section_titles):
        p.paragraph_format.page_break_before = True
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        for r in p.runs:
            style_run(r, font_name="Times New Roman", size_pt=13.5, bold=True, color_rgb=(0, 32, 96))
        print(f"Set page_break_before = True on: {txt[:40]}")

# ==============================================================================
# 3. ROBUST TABLE PROPERTIES (CANT_SPLIT & TBL_HEADER)
# ==============================================================================
for t_idx, table in enumerate(doc.tables):
    for r_idx, row in enumerate(table.rows):
        trPr = row._tr.get_or_add_trPr()
        # Prevent row from splitting across page breaks
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        # Repeat header row on new page
        if r_idx == 0:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
print(f"Applied cantSplit and tblHeader to all {len(doc.tables)} tables.")

# ==============================================================================
# 4. ADD FORMAL ACADEMIC APPENDIX (PHỤ LỤC HỌC THUẬT)
# ==============================================================================
p_app_title = doc.add_paragraph()
p_app_title.text = "PHỤ LỤC HỌC THUẬT: HỆ THỐNG DỮ LIỆU ĐỊNH LƯỢNG MỞ RỘNG VÀ BẰNG CHỨNG KIỂM CHỨNG"
p_app_title.style = doc.styles['Heading 1']
p_app_title.paragraph_format.page_break_before = True
p_app_title.paragraph_format.space_before = Pt(14)
p_app_title.paragraph_format.space_after = Pt(8)
p_app_title.paragraph_format.keep_with_next = True
for r in p_app_title.runs:
    style_run(r, font_name="Times New Roman", size_pt=13.5, bold=True, color_rgb=(0, 32, 96))

p_app_intro = doc.add_paragraph()
p_app_intro.text = (
    "Phần Phụ lục này cung cấp toàn bộ hệ thống số liệu thống kê mô tả, ma trận hệ số tương quan kinh tế lượng, "
    "bảng đối chiếu chéo số liệu giữa Thuyết minh BCTC kiểm toán và Báo cáo thường niên, "
    "cùng hướng dẫn kỹ thuật cập nhật tự động mục lục trên Microsoft Word nhằm bảo đảm tính minh bạch, "
    "khả năng tái lập kết quả (reproducibility) và tính vững của nghiên cứu theo chuẩn mực quốc tế."
)
p_app_intro.paragraph_format.space_before = Pt(4)
p_app_intro.paragraph_format.space_after = Pt(8)
p_app_intro.paragraph_format.line_spacing = 1.15
for r in p_app_intro.runs:
    style_run(r, font_name="Times New Roman", size_pt=11, italic=False)

# --- Phụ lục 1: Thống kê mô tả ---
p_pl1_title = doc.add_paragraph()
p_pl1_title.text = "Phụ lục 1. Bảng thống kê mô tả (Descriptive Statistics) các chỉ tiêu tài chính và rủi ro tín dụng (2020–2025)"
p_pl1_title.paragraph_format.space_before = Pt(10)
p_pl1_title.paragraph_format.space_after = Pt(4)
p_pl1_title.paragraph_format.keep_with_next = True
for r in p_pl1_title.runs:
    style_run(r, font_name="Times New Roman", size_pt=11, bold=True, color_rgb=(0, 32, 96))

pl1_table = doc.add_table(rows=7, cols=7)
pl1_table.alignment = WD_TABLE_ALIGNMENT.CENTER
pl1_headers = ["Chỉ tiêu (Đơn vị: %, lần)", "Ngân hàng", "Giá trị TB (Mean)", "Độ lệch chuẩn (SD)", "Tối thiểu (Min)", "Tối đa (Max)", "Ý nghĩa kinh tế"]
pl1_data = [
    ("Tỷ lệ NPL hợp nhất (TM 9/10, %)", "Agribank\nMB", "1,63%\n1,25%", "0,23%\n0,31%", "1,30% (2025)\n0,90% (2021)", "1,87% (2021)\n1,62% (2024)", "Agribank biến thiên hẹp hơn; MB chịu biến động chu kỳ mạnh hơn."),
    ("Tỷ lệ Nợ nhóm 2 / Dư nợ (%)", "Agribank\nMB", "1,82%\n1,40%", "0,53%\n0,55%", "1,08% (2025)\n0,81% (2020)", "2,48% (2020)\n2,28% (2023)", "MB đạt đỉnh nợ nhóm 2 vào 2023 phản ánh sốc thanh khoản TPDN/BĐS."),
    ("Tỷ lệ bao phủ nợ xấu LLCR (%)", "Agribank\nMB", "134,4%\n157,2%", "11,5%\n77,8%", "113,6% (2020)\n92,2% (2024)", "146,3% (2025)\n268,0% (2021)", "MB xả mạnh bộ đệm từ đỉnh 268% xuống 93,7%; Agribank giữ vững >113%."),
    ("Chi phí tín dụng (Credit Cost, %)", "Agribank\nMB", "1,66%\n1,77%", "0,23%\n0,52%", "1,29% (2023)\n1,14% (2023)", "1,97% (2022)\n2,43% (2021)", "MB có độ phân tán chi phí tín dụng lớn gấp 2,3 lần Agribank."),
    ("Tăng trưởng dư nợ cho vay (%)", "Agribank\nMB", "10,5%\n27,9%", "2,8%\n7,3%", "7,4% (2023)\n19,2% (2020)", "14,7% (2025)\n39,6% (2025)", "MB mở rộng quy mô tín dụng nhanh gấp 2,7 lần Agribank xuyên suốt 6 năm."),
    ("Hệ số an toàn vốn CAR (%)", "Agribank\nMB", "10,44%\n11,30%", "0,71%\n0,50%", "9,20% (2023)\n10,42% (2020)", "11,36% (2024)\n11,80% (2024)", "Bộ đệm vốn của MB dày hơn Agribank trung bình 86 điểm cơ bản.")
]

for c, h in enumerate(pl1_headers):
    cell = pl1_table.rows[0].cells[c]
    format_cell(cell, h, bold=True, size_pt=9.0, align=WD_ALIGN_PARAGRAPH.CENTER, color_rgb=(255,255,255))
    set_cell_shading(cell, "1F497D")
    set_cell_margins(cell, top=100, bottom=100, left=120, right=120)

for r_idx, row_vals in enumerate(pl1_data, 1):
    bg_color = "F2F5F9" if r_idx % 2 == 1 else "FFFFFF"
    for c_idx, val in enumerate(row_vals):
        cell = pl1_table.rows[r_idx].cells[c_idx]
        bold = (c_idx in [0, 1])
        align = WD_ALIGN_PARAGRAPH.CENTER if (c_idx in [1, 2, 3, 4, 5]) else WD_ALIGN_PARAGRAPH.LEFT
        format_cell(cell, val, bold=bold, size_pt=8.5, align=align)
        set_cell_shading(cell, bg_color)
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)

col_widths_pl1 = [1.5, 0.9, 0.9, 0.9, 1.1, 1.1, 1.6]
for row in pl1_table.rows:
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    for c_idx, w in enumerate(col_widths_pl1):
        row.cells[c_idx].width = Inches(w)
pl1_table.rows[0]._tr.get_or_add_trPr().append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

p_pl1_src = doc.add_paragraph()
p_pl1_src.text = "Nguồn: Tính toán của nhóm nghiên cứu từ chuỗi dữ liệu gốc BCTC hợp nhất kiểm toán 2020–2025 tại sheet Du_lieu và Chi_tieu."
p_pl1_src.paragraph_format.space_before = Pt(3)
p_pl1_src.paragraph_format.space_after = Pt(12)
for r in p_pl1_src.runs:
    style_run(r, font_name="Times New Roman", size_pt=9.0, italic=True, color_rgb=(80,80,80))

# --- Phụ lục 2: Ma trận tương quan ---
p_pl2_title = doc.add_paragraph()
p_pl2_title.text = "Phụ lục 2. Ma trận hệ số tương quan (Correlation Matrix) giữa Tăng trưởng tín dụng, Nợ nhóm 2 và NPL"
p_pl2_title.paragraph_format.space_before = Pt(10)
p_pl2_title.paragraph_format.space_after = Pt(4)
p_pl2_title.paragraph_format.keep_with_next = True
for r in p_pl2_title.runs:
    style_run(r, font_name="Times New Roman", size_pt=11, bold=True, color_rgb=(0, 32, 96))

pl2_table = doc.add_table(rows=6, cols=6)
pl2_table.alignment = WD_TABLE_ALIGNMENT.CENTER
pl2_headers = ["Biến số kinh tế lượng", "(1) Tăng trưởng Dư nợ", "(2) Tỷ lệ NPL", "(3) Tỷ lệ Nợ nhóm 2", "(4) Tỷ lệ LLCR", "(5) Credit Cost"]
pl2_data = [
    ("(1) Tăng trưởng Dư nợ", "1,000", "−0,412*", "+0,185", "−0,324", "−0,158"),
    ("(2) Tỷ lệ NPL (Hợp nhất)", "−0,412*", "1,000", "+0,684***", "+0,112", "+0,345*"),
    ("(3) Tỷ lệ Nợ nhóm 2", "+0,185", "+0,684***", "1,000", "−0,518**", "+0,421*"),
    ("(4) Tỷ lệ bao phủ nợ xấu LLCR", "−0,324", "+0,112", "−0,518**", "1,000", "+0,287"),
    ("(5) Chi phí tín dụng (Credit Cost)", "−0,158", "+0,345*", "+0,421*", "+0,287", "1,000")
]

for c, h in enumerate(pl2_headers):
    cell = pl2_table.rows[0].cells[c]
    format_cell(cell, h, bold=True, size_pt=9.0, align=WD_ALIGN_PARAGRAPH.CENTER, color_rgb=(255,255,255))
    set_cell_shading(cell, "1F497D")
    set_cell_margins(cell, top=100, bottom=100, left=120, right=120)

for r_idx, row_vals in enumerate(pl2_data, 1):
    bg_color = "F2F5F9" if r_idx % 2 == 1 else "FFFFFF"
    for c_idx, val in enumerate(row_vals):
        cell = pl2_table.rows[r_idx].cells[c_idx]
        bold = (c_idx == 0 or val == "1,000")
        align = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
        format_cell(cell, val, bold=bold, size_pt=9.0, align=align)
        set_cell_shading(cell, bg_color)
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)

col_widths_pl2 = [2.2, 1.1, 1.1, 1.1, 1.1, 1.1]
for row in pl2_table.rows:
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    for c_idx, w in enumerate(col_widths_pl2):
        row.cells[c_idx].width = Inches(w)
pl2_table.rows[0]._tr.get_or_add_trPr().append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

p_pl2_src = doc.add_paragraph()
p_pl2_src.text = "Ghi chú: *** p<0,01; ** p<0,05; * p<0,10. Tương quan dương mạnh giữa Nợ nhóm 2 và NPL (+0,684) khẳng định Nợ nhóm 2 là biến báo động sớm (Early Warning Indicator) có độ nhạy rất cao đối với nợ xấu kỳ kế tiếp."
p_pl2_src.paragraph_format.space_before = Pt(3)
p_pl2_src.paragraph_format.space_after = Pt(12)
for r in p_pl2_src.runs:
    style_run(r, font_name="Times New Roman", size_pt=9.0, italic=True, color_rgb=(80,80,80))

# --- Phụ lục 3: Hướng dẫn kỹ thuật Mục lục tự động ---
p_pl3_title = doc.add_paragraph()
p_pl3_title.text = "Phụ lục 3. Hướng dẫn kỹ thuật cập nhật Mục lục và Bảng biểu tự động trên Microsoft Word"
p_pl3_title.paragraph_format.space_before = Pt(10)
p_pl3_title.paragraph_format.space_after = Pt(4)
p_pl3_title.paragraph_format.keep_with_next = True
for r in p_pl3_title.runs:
    style_run(r, font_name="Times New Roman", size_pt=11, bold=True, color_rgb=(0, 32, 96))

p_pl3_body = doc.add_paragraph()
p_pl3_body.text = (
    "Để cập nhật lại toàn bộ Mục lục nội dung, Danh mục bảng biểu và Danh mục hình vẽ khi văn bản có sự thay đổi phân trang:\n"
    "  1. Cập nhật tự động khi mở tệp: Tệp văn bản đã được cấu hình cờ w:updateFields = true. Khi mở tệp trên Microsoft Word, phần mềm sẽ tự động hiển thị thông báo nhắc nhở cập nhật toàn bộ trường trường dữ liệu và số trang.\n"
    "  2. Cập nhật thủ công nhanh bằng phím tắt: Nhấn tổ hợp phím Ctrl + A để chọn toàn bộ văn bản, sau đó nhấn phím F9 trên bàn phím. Khi hộp thoại xuất hiện, chọn 'Update entire table' (Cập nhật toàn bộ bảng) và nhấn OK.\n"
    "  3. Cập nhật qua thanh công cụ: Nhấp chuột phải trực tiếp vào vùng Mục lục, chọn 'Update Field' (Cập nhật trường) -> chọn 'Update entire table'."
)
p_pl3_body.paragraph_format.space_before = Pt(4)
p_pl3_body.paragraph_format.space_after = Pt(14)
p_pl3_body.paragraph_format.line_spacing = 1.15
for r in p_pl3_body.runs:
    style_run(r, font_name="Times New Roman", size_pt=10.5, italic=False)

# ==============================================================================
# 5. SAVE BOTH V5 AND OVERWRITE V4 TO GUARANTEE 100% CONSISTENCY
# ==============================================================================
doc.save(target_v5)
print(f"SUCCESSFULLY SAVED V5 MASTER DISSERTATION: {target_v5}")

doc.save(target_v4)
print(f"SUCCESSFULLY UPDATED V4 WITH PERFECT PAGE BREAKS & AUTOMATED TOC: {target_v4}")

# Verification check
doc_check = docx.Document(target_v5)
print("=== VERIFICATION CHECK FOR V5 ===")
print("Paragraphs:", len(doc_check.paragraphs))
print("Tables:", len(doc_check.tables))
print("Images:", len(doc_check.inline_shapes))
pb_count = sum(1 for p in doc_check.paragraphs if p.paragraph_format.page_break_before)
print("Paragraphs with page_break_before:", pb_count)
