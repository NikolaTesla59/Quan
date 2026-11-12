import os
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def style_run(run, font_name="Times New Roman", size_pt=10.5, bold=False, italic=False, color_rgb=(0,0,0)):
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
        style_run(r, font_name="Times New Roman", size_pt=10.5)
    return p

def add_h1(doc, text, page_break_before=False):
    p = doc.add_paragraph()
    p.paragraph_format.page_break_before = page_break_before
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    style_run(r, font_name="Times New Roman", size_pt=12.5, bold=True, color_rgb=(0, 32, 96))
    return p

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    style_run(r, font_name="Times New Roman", size_pt=11, bold=True, color_rgb=(15, 76, 129))
    return p

def add_callout(doc, text_prefix, text_body, rgb_prefix=(192, 0, 0), bg_hex="F2F5F9"):
    """
    Creates a 1x1 table callout which is 100% compatible with Google Docs, LibreOffice, and Word.
    Does NOT use raw w:pBdr which crashes Google Docs' importer.
    """
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    tblPr = tbl._element.xpath('w:tblPr')[0]
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="002060"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideH w:val="none"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblLook = tblPr.find(qn('w:tblLook'))
    if tblLook is not None:
        tblLook.addprevious(borders)
    else:
        tblPr.append(borders)
        
    cell = tbl.rows[0].cells[0]
    cell.width = Inches(6.67)
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_hex}"/>')
    tcPr.append(shd)
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="80" w:type="dxa"/><w:bottom w:w="80" w:type="dxa"/><w:left w:w="120" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    
    r1 = p.add_run(text_prefix)
    style_run(r1, font_name="Times New Roman", size_pt=10, bold=True, color_rgb=rgb_prefix)
    r2 = p.add_run(text_body)
    style_run(r2, font_name="Times New Roman", size_pt=10, bold=False, italic=False)
    
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(2)

def format_table(table, col_widths, col_alignments):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    tblPr = table._element.xpath('w:tblPr')[0]
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="8" w:space="0" w:color="002060"/>'
        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="002060"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="D3D3D3"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblLook = tblPr.find(qn('w:tblLook'))
    if tblLook is not None:
        tblLook.addprevious(borders)
    else:
        tblPr.append(borders)
    
    for r_idx, row in enumerate(table.rows):
        trPr = row._tr.get_or_add_trPr()
        # ECMA-376 schema: cantSplit MUST come before tblHeader
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        is_header = (r_idx == 0)
        if is_header:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths[c_idx]
            tcPr = cell._tc.get_or_add_tcPr()
            if is_header:
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="002060"/>')
                tcPr.append(shd)
            elif r_idx % 2 == 1:
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8F9FA"/>')
                tcPr.append(shd)
            
            tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="60" w:type="dxa"/><w:bottom w:w="60" w:type="dxa"/><w:left w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>')
            tcPr.append(tcMar)
            
            for p in cell.paragraphs:
                p.alignment = col_alignments[c_idx]
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    if is_header:
                        style_run(r, font_name="Times New Roman", size_pt=9, bold=True, color_rgb=(255, 255, 255))
                    else:
                        style_run(r, font_name="Times New Roman", size_pt=8.5, bold=False, color_rgb=(0, 0, 0))

# ==============================================================================
# 1. BUILD 100% CLEAN DOCX
# ==============================================================================
doc = docx.Document()
section = doc.sections[0]
section.page_width = Inches(8.27)
section.page_height = Inches(11.69)
section.top_margin = Inches(0.8)
section.bottom_margin = Inches(0.8)
section.left_margin = Inches(0.8)
section.right_margin = Inches(0.8)

# Configure Header
header = section.header
p_head = header.paragraphs[0]
p_head.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r_head = p_head.add_run("Học phần Quản trị Rủi ro — Cẩm nang Phản biện Thuyết trình Agribank vs MB")
style_run(r_head, size_pt=8.5, italic=True, color_rgb=(120, 120, 120))

# Configure Footer
footer = section.footer
p_foot = footer.paragraphs[0]
p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_foot = p_foot.add_run("Tài liệu Báo cáo & Phản biện Thuyết trình — Nhóm 2 Cao học Khóa 34 NEU")
style_run(r_foot, size_pt=8.5, italic=True, color_rgb=(120, 120, 120))

# HEADER BLOCK
p_top = add_p(doc, "TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN (NEU) — VIỆN NGÂN HÀNG - TÀI CHÍNH\nCHƯƠNG TRÌNH CAO HỌC KHÓA 34 (LỚP K34_3_NH8) — HỌC PHẦN: QUẢN TRỊ RỦI RO", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=6)
for r in p_top.runs:
    style_run(r, size_pt=9.5, bold=True, color_rgb=(0, 32, 96))

p_title = add_p(doc, "CẨM NANG HỎI ĐÁP PHẢN BIỆN THUYẾT TRÌNH (DEFENSE HANDBOOK)\nGIẢI ĐÁP 5 CÂU HỎI TRỌNG TÂM CỦA KHÁN GIẢ VÀ HỘI ĐỒNG", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=4)
for r in p_title.runs:
    style_run(r, size_pt=14, bold=True, color_rgb=(192, 0, 0))

p_sub = add_p(doc, "Chuyên đề: So sánh Mô hình & Thực trạng Quản trị Rủi ro Tín dụng giữa Agribank và MB (2020–2025)\nNhóm thực hiện: Nhóm 2 | Giảng viên hướng dẫn: TS. Khúc Thế Anh", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=12)
for r in p_sub.runs:
    style_run(r, size_pt=10, italic=True, color_rgb=(80, 80, 80))

# SECTION 0: QUICK REFERENCE MATRIX
add_h1(doc, "TỔNG HỢP NHANH MA TRẬN 5 CÂU HỎI PHẢN BIỆN & SỐ LIỆU CHỐT")

headers_ref = ["Người hỏi & Câu hỏi", "Slide", "Luận điểm chốt hạ (BLUF)", "Số liệu kiểm toán cốt lõi", "Căn cứ pháp lý"]
rows_ref = [
    [
        "1. Lan\nDư nợ Nông nghiệp vs Mục tiêu Lợi nhuận",
        "Slide 02, 04,\nSlide 09, 13",
        "Có mâu thuẫn (Nghịch lý kép). Cân bằng qua tài trợ chéo 65/35, số hóa giảm CIR, vốn rẻ CASA và cấp vốn NSNN.",
        "Dư nợ Tam nông 61,7%–70%; NIM 2,5% (vs MB 5%); CIR 35-40%; RORAC 10,8%-16,7% (MB 31,6%-49,3%).",
        "NĐ 55/2015/NĐ-CP\nNĐ 116/2018/NĐ-CP\nLuật 69/2014/QH13"
    ],
    [
        "2. Linh\nKhó khăn nợ nhóm 5 & TSBĐ Bất động sản",
        "Slide 08, 18",
        "BĐS nông nghiệp thanh khoản thứ cấp cực thấp; vướng thủ tục nhận chuyển nhượng; mất quyền thu giữ TSBĐ (NQ 42 hết hạn).",
        "Nợ nhóm 5 chiếm 79,0% nợ xấu (20.220 tỷ); 88%-92% TSBĐ là đất nông thôn; nợ ngoại bảng 278.372 tỷ.",
        "Luật Đất đai 2013/2024\nHết hiệu lực NQ 42\nLuật 96/2025/QH15"
    ],
    [
        "3. Hồng Hà\nMB ít trích nợ nhóm 2 theo TT11 & Rủi ro IFRS 9",
        "Slide 15, 16,\nSlide 20",
        "TT11 cho khấu trừ TSBĐ nên DP cụ thể = 0. Sang IFRS 9 bị sốc Lifetime ECL Stage 2 (MCredit, TPDN).",
        "Dư nợ nhóm 2 MB đỉnh 13.918 tỷ (2023). IFRS 9 thiếu hụt 14.006 tỷ (+106,5%), CAR giảm 103 bps.",
        "Thông tư 11/2021\nIFRS 9 (SICR / Stage 2)\nThông tư 41/2016"
    ],
    [
        "4. Kiệt\nSlide 08 Tử/Mẫu; El Nino & Rủi ro khí hậu ESG",
        "Slide 08, 12,\nSlide 24",
        "Agri giảm thực chất cả tử (-22,9%) và mẫu (+27,7%). MB tử tăng (+514 tỷ), tỷ lệ giảm do tín dụng tăng nóng (+77,4%).",
        "MB tín dụng tăng 39,6% năm 2025. Agri xóa nợ 32.621 tỷ. El Nino làm mất 30-50% dòng tiền nông hộ ĐBSCL.",
        "Thông tư 17/2022/TT-NHNN\nKhung NGFS Climate Risk\nQĐ 1604/QĐ-NHNN"
    ],
    [
        "5. Q. Khánh\nAgri 100% vốn NN: Tại sao nợ nhóm 5 lớn kéo dài?",
        "Slide 08, 18",
        "Bẫy bảo toàn vốn Nhà nước (Điều 219 BLHS sợ trách nhiệm thất thoát nếu miễn giảm gốc/bán nợ chiết khấu); tồn đọng đại án.",
        "Nợ nhóm 5 neo 67%-79% suốt 6 năm. Dự phòng cụ thể đã trích 100% nhưng nợ đọng chờ thi hành án.",
        "Luật 69/2014/QH13\nĐiều 219 BLHS 2015\nTồn đọng ALC II, Lifepro"
    ]
]

table_ref = doc.add_table(rows=len(rows_ref) + 1, cols=5)
col_widths_ref = [Inches(1.2), Inches(0.8), Inches(2.1), Inches(1.6), Inches(1.0)]
col_align_ref = [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]

for c_idx, h in enumerate(headers_ref):
    table_ref.rows[0].cells[c_idx].paragraphs[0].text = h
for r_idx, row in enumerate(rows_ref):
    for c_idx, val in enumerate(row):
        table_ref.rows[r_idx + 1].cells[c_idx].paragraphs[0].text = val
format_table(table_ref, col_widths_ref, col_align_ref)

# QUESTION 1: LAN
add_h1(doc, "CÂU HỎI 1 (LAN): DƯ NỢ NÔNG NGHIỆP VS MỤC TIÊU LỢI NHUẬN TẠI AGRIBANK — XUNG ĐỘT THỂ CHẾ VÀ GIẢI PHÁP CÂN BẰNG", page_break_before=True)
add_p(doc, "Slide liên quan: Slide 02 (Mô hình Agribank), Slide 04 (Đối chiếu quản trị), Slide 09 (Hiệu quả RORAC), Slide 13 (Stress test CAR).", space_before=1, space_after=4)
doc.paragraphs[-1].runs[0].font.italic = True

add_callout(doc, "KẾT LUẬN TRỰC DIỆN (BLUF): ", 
            "Có xung đột nội tại sâu sắc (Dual-Mandate Conflict) giữa sứ mệnh chính trị - xã hội và mục tiêu thương mại. Để hóa giải, Agribank không thể bỏ nông nghiệp mà phải dùng chiến lược 'Tài trợ chéo nội bộ', số hóa hạ CIR và tối ưu nguồn vốn CASA rẻ từ mạng lưới nông thôn.")

add_h2(doc, "1. Bản chất xung đột toán học & tài chính:")
points_q1 = [
    ("Nghịch lý biên lãi thuần (NIM): ", "Dư nợ Tam nông chiếm 61,7%–70% (1,2–1,4 triệu tỷ đồng) bị áp trần lãi suất ưu đãi của NHNN (4,0%–4,5%/năm), khiến NIM Agribank chỉ đạt 2,5%–2,8%, trong khi MB đạt 4,5%–5,5% nhờ tự do đẩy mạnh bán lẻ và tiêu dùng."),
    ("Gánh nặng chi phí vận hành (CIR): ", "Để phục vụ hàng triệu nông hộ phân tán vùng sâu vùng xa, Agribank phải vận hành mạng lưới >2.200 chi nhánh/PGD với gần 40.000 nhân sự, đẩy CIR lên 35%–40%."),
    ("Chi phí tín dụng (Credit Cost) bào mòn lợi nhuận: ", "Chi phí trích lập dự phòng bình quân 1,66%/năm ngốn tới 42,8%–59,1% lợi nhuận thuần trước dự phòng (PPOP). Hệ quả là tỷ suất RORAC proxy của Agribank chỉ đạt 10,8%–16,7% (thấp hơn MB từ 15,8–33,8 điểm %)."),
    ("Áp lực bảo toàn vốn công: ", "Là DNNN 100% vốn, Agribank phải bảo toàn vốn Nhà nước theo Luật 69/2014 và đảm bảo CAR ≥ 8,0%. Nếu chỉ theo đuổi chính sách xã hội, khả năng tự tích tụ vốn từ lợi nhuận giữ lại suy kiệt, đẩy CAR về ngưỡng nguy hiểm (8,67% trong Stress test cực đoan).")
]
for pfx, bdy in points_q1:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"• {pfx}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_h2(doc, "2. Bốn giải pháp chiến lược cân bằng hai mục tiêu:")
sol_q1 = [
    ("Tái cấu trúc danh mục theo tỷ lệ 65/35 (Tài trợ chéo): ", "Giữ 60%–65% cho Tam nông cốt lõi; dành 35%–40% còn lại cho các phân khúc biên lãi cao: Tài trợ chuỗi giá trị chế biến xuất khẩu (Agribusiness), SME đô thị và bán lẻ thị trấn để bù đắp biên lãi (cross-subsidize)."),
    ("Đột phá thu nhập ngoài lãi (Non-interest Income): ", "Khai thác tệp 20 triệu khách hàng nông thôn bán chéo bảo hiểm liên kết (ABIC), dịch vụ thanh toán công. Triển khai Agribank Digital / Ngân hàng số để hạ CIR từ 40% xuống <32%."),
    ("Tối ưu chi phí vốn (CoF) từ tiền gửi nông thôn: ", "Nguồn tiền gửi dân cư nông thôn có độ trung thành cao, ít nhạy cảm lãi suất, mang lại nguồn vốn đầu vào rẻ nhất hệ thống, giữ vững biên lợi nhuận."),
    ("Cơ chế cấp bù lãi suất & Tăng vốn NSNN: ", "Chính phủ cấp bù lãi suất theo Nghị định 55/2015 và Quốc hội định kỳ cấp bổ sung vốn điều lệ từ NSNN (như khoản 17.100 tỷ đồng) hoặc cho phép giữ lại 100% lợi nhuận sau thuế.")
]
for idx, (pfx, bdy) in enumerate(sol_q1):
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  {idx+1}. {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_callout(doc, "LỜI THOẠI TRẢ LỜI MẪU (SPEAKER SCRIPT): ", 
            "'Thưa bạn Lan, đây là nghịch lý kép điển hình của một NHTM Nhà nước. Agribank không thể từ bỏ sứ mệnh Tam nông vì đó là lý do tồn tại thể chế của ngân hàng. Để vừa bảo toàn vốn Nhà nước vừa hoàn thành nhiệm vụ chính trị, Agribank áp dụng chiến lược tài trợ chéo: Dùng nguồn vốn huy động giá rẻ từ mạng lưới 2.200 chi nhánh và lợi nhuận từ mảng doanh nghiệp xuất khẩu/bán lẻ đô thị để bù đắp cho mảng nông nghiệp ưu đãi, kết hợp với việc Nhà nước định kỳ tăng vốn điều lệ từ ngân sách.'",
            rgb_prefix=(0, 32, 96))

# QUESTION 2: LINH
add_h1(doc, "CÂU HỎI 2 (LINH): SLIDE 08 — NỢ NHÓM 5 NĂM 2025 CAO, KHÓ KHĂN XỬ LÝ TSBĐ BẤT ĐỘNG SẢN & RỦI RO PHÁP LÝ", page_break_before=True)
add_p(doc, "Slide liên quan: Slide 08 (Nợ nhóm 2, nợ cơ cấu & nợ nhóm 5), Slide 18 (Tình huống Yagi, nợ nhóm 5 và Lifepro).", space_before=1, space_after=4)
doc.paragraphs[-1].runs[0].font.italic = True

add_callout(doc, "KẾT LUẬN TRỰC DIỆN (BLUF): ", 
            "Nợ nhóm 5 của Agribank chiếm tới 79,0% nợ xấu do 88%-92% TSBĐ là đất nông thôn có thanh khoản thứ cấp cực thấp, vướng điều kiện nhận chuyển nhượng của Luật Đất đai, và đặc biệt là bị mất quyền thu giữ TSBĐ khi Nghị quyết 42 hết hiệu lực (khiến thủ tục kiện tụng kéo dài 3-7 năm).")

add_h2(doc, "1. Dữ liệu thực chứng & Bản chất khó khăn với BĐS nông nghiệp:")
points_q2 = [
    ("Dữ liệu nợ nhóm 5 tại Slide 08: ", "Năm 2025, nợ nhóm 5 của Agribank là 20.220 tỷ đồng trên 25.610 tỷ nợ xấu (chiếm 79,0%, trong khi MB chỉ chiếm ~40%). Số dư nợ ngoại bảng lũy kế chờ thu hồi lên tới 278.372 tỷ đồng."),
    ("Thanh khoản thứ cấp đóng băng: ", "TSBĐ chủ yếu là đất nông nghiệp, đất rừng, đất nuôi trồng thủy sản, nhà xưởng nông thôn. Thị trường thứ cấp gần như không có giao dịch; tâm lý làng xã kiêng kỵ mua đất phát mại của người cùng quê, còn nhà đầu tư thành phố không có nhu cầu mua đất phân tán vùng sâu vùng xa."),
    ("Chu kỳ đấu giá hạ giá kéo dài: ", "Quy trình phát mại đất nông thôn thường phải tổ chức đấu giá hạ giá từ 5 đến 10 lần (mỗi lần giảm 5%–10%) mà vẫn không có người đăng ký mua, kéo dài 2–3 năm khiến tài sản hoang hóa, suy giảm giá trị.")
]
for pfx, bdy in points_q2:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"• {pfx}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_h2(doc, "2. Rủi ro pháp lý & Khoảng trống thể chế nghiêm trọng:")
legal_q2 = [
    ("Rào cản đối tượng nhận chuyển nhượng đất nông nghiệp: ", "Theo Luật Đất đai 2013, tổ chức kinh tế và cá nhân không trực tiếp sản xuất nông nghiệp không được nhận chuyển nhượng đất trồng lúa. Luật Đất đai 2024 (hiệu lực 01/08/2024) đã nới lỏng nhưng vẫn yêu cầu lập phương án sử dụng đất được UBND huyện phê duyệt, loại bỏ phần lớn người mua tiềm năng."),
    ("Khoảng trống pháp lý khi Nghị quyết 42 hết hiệu lực (Rủi ro lớn nhất 2024–2025): ", "Nghị quyết 42 hết hiệu lực từ 31/12/2023 nhưng quyền thu giữ TSBĐ không được đưa đầy đủ vào Luật Các TCTD 2024. Khi bên vay bất hợp tác, Agribank không có quyền cưỡng chế thu giữ đất, buộc phải kiện ra Tòa án dân sự."),
    ("Điểm nghẽn thi hành án kéo dài 3–7 năm: ", "Quy trình khởi kiện sơ thẩm, phúc thẩm và thi hành án dân sự huyện kéo dài nhiều năm. Cơ quan thi hành án huyện thường ngần ngại cưỡng chế trục xuất người nông dân vì e ngại an ninh trật tự xã hội địa phương, khiến nợ nhóm 5 bị 'đóng băng' nội bảng."),
    ("Lối thoát thể chế từ 2026: ", "Nút thắt này chỉ được gỡ khi Quốc hội thông qua Luật số 96/2025/QH15 khôi phục lại quyền thu giữ TSBĐ cho TCTD, có hiệu lực từ đầu năm 2026.")
]
for pfx, bdy in legal_q2:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  - {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_callout(doc, "LỜI THOẠI TRẢ LỜI MẪU (SPEAKER SCRIPT): ", 
            "'Thưa bạn Linh, nợ nhóm 5 của Agribank cao tới 79,0% không phải vì ngân hàng không muốn xử lý, mà vì vướng điểm nghẽn kép: Thứ nhất, 90% TSBĐ là đất nông nghiệp vùng sâu vùng xa không có thanh khoản thị trường thứ cấp. Thứ hai và nguy hiểm nhất là khoảng trống pháp lý khi Nghị quyết 42 hết hiệu lực cuối năm 2023 làm ngân hàng mất quyền chủ động thu giữ TSBĐ. Mọi vụ việc đều phải qua Tòa án và thi hành án kéo dài 3–7 năm. Phải chờ Luật số 96/2025 có hiệu lực từ năm 2026 thì nút thắt thu giữ TSBĐ này mới được tháo gỡ triệt để.'",
            rgb_prefix=(0, 32, 96))

# QUESTION 3: HONG HA
add_h1(doc, "CÂU HỎI 3 (HỒNG HÀ): IFRS 9 VS THÔNG TƯ 11 — TẠI SAO MB KHÔNG TRÍCH LẬP MẤY CHO NỢ NHÓM 2? RỦI RO NẾU CHỈ THEO THÔNG TƯ", page_break_before=True)
add_p(doc, "Slide liên quan: Slide 15 (Phương pháp & Tham số IFRS 9), Slide 16 (Kết quả mô phỏng IFRS 9), Slide 20 (Cú sốc chất lượng tài sản MB 2023).", space_before=1, space_after=4)
doc.paragraphs[-1].runs[0].font.italic = True

add_callout(doc, "KẾT LUẬN TRỰC DIỆN (BLUF): ", 
            "Theo Thông tư 11, cơ chế khấu trừ giá trị TSBĐ khiến Dự phòng cụ thể của nợ nhóm 2 bằng 0 đồng (chỉ trích 0,75% DP chung). Nhưng sang IFRS 9, nợ nhóm 2 bị xếp vào Stage 2 (SICR) bắt buộc tính Lifetime ECL, khiến MB lộ khoảng cách trích thiếu tới 14.006 tỷ đồng (+106,5%) do rủi ro từ MCredit và Trái phiếu DN.")

add_h2(doc, "1. Tại sao MB 'không trích lập mấy' cho nợ nhóm 2 theo quy định hiện hành?")
points_q3 = [
    ("Công thức khấu trừ TSBĐ theo Thông tư 11/2021: ", "Dự phòng cụ thể (DPCT) nợ nhóm 2 tính theo công thức: R = max(0, A - C) × 5%. Trong đó A là dư nợ, C là giá trị khấu trừ TSBĐ (BĐS chiết khấu 50%). Khi giá trị TSBĐ sau chiết khấu lớn hơn dư nợ (C ≥ A), phần chênh lệch (A - C) ≤ 0, dẫn tới DPCT = 0 đồng!"),
    ("Thực tế danh mục cho vay MB: ", "Các khoản vay cá nhân, hộ kinh doanh và doanh nghiệp BĐS tại MB đều có tỷ lệ LTV từ 50%–70%. Do đó, với 13.918 tỷ nợ nhóm 2 năm 2023, MB gần như chỉ phải trích 0,75% Dự phòng chung (~104 tỷ đồng), hoàn toàn không phải trích DPCT."),
    ("Động cơ kinh tế của NHTMCP niêm yết: ", "MB tận dụng quy định này để không phải ghi nhận chi phí dự phòng lớn, giúp bảo vệ con số lợi nhuận trước thuế theo cam kết với cổ đông (kế hoạch PBT >26.000 tỷ năm 2023).")
]
for pfx, bdy in points_q3:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"• {pfx}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_h2(doc, "2. Cú sốc chuyển đổi IFRS 9 và 4 rủi ro lớn nếu chỉ áp dụng Thông tư 11:")
risks_q3 = [
    ("Cú sốc Lifetime ECL tại Stage 2 (Slide 15, 16): ", "IFRS 9 xóa bỏ mô hình tổn thất đã phát sinh (Incurred Loss). Nợ nhóm 2 là diện gia tăng rủi ro tín dụng đáng kể (SICR - Stage 2), bắt buộc tính Lifetime ECL = EAD × PD_lifetime × LGD. Với PD trọn vòng đời lên tới 15%–25%, cộng với danh mục MCredit (tín chấp 100%, LGD 80%-90%) và 30% danh mục TPDN (7.023 tỷ) rơi vào Stage 2, MB bị thiếu hụt dự phòng tới 14.006 tỷ (+106,5%), ăn mòn 7,9% vốn CSH và giảm 103 bps hệ số CAR."),
    ("Rủi ro Lợi nhuận ảo (Paper Profits): ", "Ghi nhận lợi nhuận cao giả tạo, chi trả cổ tức tiền mặt và thưởng ban điều hành trên những đồng lợi nhuận chưa trừ đủ chi phí rủi ro thực tế."),
    ("Cú sốc vách đá trích lập (Cliff Effect): ", "Khi nợ nhóm 2 không phục hồi mà rơi xuống nhóm 3 (trích 20%), nhóm 4 (50%), nhóm 5 (100%), chi phí dự phòng sẽ bùng nổ đột ngột hàng nghìn tỷ, xóa sạch lợi nhuận quý."),
    ("Ảo tưởng thanh lý TSBĐ & Hạ bậc tín nhiệm quốc tế: ", "Thông tư 11 giả định TSBĐ bán được ngay, nhưng thực tế xử lý BĐS mất 3–5 năm với mức chiết khấu 30%–50%. Các tổ chức xếp hạng (Moody's, S&P) sẽ tự động chiết trừ vốn tự có khi thấy LLCR của MB tụt xuống dưới 100% (93,7% năm 2025).")
]
for pfx, bdy in risks_q3:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  - {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_callout(doc, "LỜI THOẠI TRẢ LỜI MẪU (SPEAKER SCRIPT): ", 
            "'Thưa bạn Hồng Hà, MB không trích lập nhiều cho nợ nhóm 2 vì họ hoàn toàn tuân thủ Thông tư 11: Khi khoản vay có TSBĐ đầy đủ thì dự phòng cụ thể được khấu trừ về 0, chỉ mất 0,75% dự phòng chung. Nhưng đó chính là lỗ hổng của mô hình tổn thất đã phát sinh! Khi chuyển sang IFRS 9, nợ nhóm 2 bị kích hoạt Stage 2 tính tổn thất trọn vòng đời. Vì MB có khối tín dụng tiêu dùng tín chấp MCredit và 30% trái phiếu doanh nghiệp rủi ro, khoảng cách dự phòng trích thiếu vọt lên hơn 14.000 tỷ đồng. Nếu chỉ chạy theo Thông tư, ngân hàng sẽ rơi vào bẫy 'lợi nhuận ảo' và đối mặt cú sốc vách đá khi nợ xấu thực tế bùng phát.'",
            rgb_prefix=(0, 32, 96))

# QUESTION 4: KIET
add_h1(doc, "CÂU HỎI 4 (KIỆT): SLIDE 08 PHÂN RÃ TỬ/MẪU; HIỆN TƯỢNG EL NINO, DỰ BÁO VĨ MÔ & ESG TẠI AGRIBANK", page_break_before=True)
add_p(doc, "Slide liên quan: Slide 08 (Tỷ lệ nợ nhóm 2–5 / Dư nợ), Slide 12 (Tham số kịch bản Stress test), Slide 24 (Kiến nghị ESG & Stress test khí hậu cho Agribank).", space_before=1, space_after=4)
doc.paragraphs[-1].runs[0].font.italic = True

add_callout(doc, "KẾT LUẬN TRỰC DIỆN (BLUF): ", 
            "Tại Slide 08, Agribank giảm tỷ lệ nợ nhóm 2-5 là nhờ Tử số giảm thực chất (-22,9%) kết hợp Mẫu số tăng ổn định (+27,7%). Ngược lại, tại MB, Tử số không giảm mà còn tăng (+514 tỷ), tỷ lệ giảm 100% do Mẫu số tăng trưởng nóng làm loãng (+77,4%). Về El Nino, rủi ro thiên tai làm đứt gãy dòng tiền nông hộ nghiêm trọng nhưng Agribank mới chỉ dự báo vĩ mô truyền thống, cần tích hợp kịch bản khí hậu NGFS vào thẩm định ESG.")

add_h2(doc, "1. Bóc tách toán học Slide 08: Tử số (Nợ có vấn đề) vs Mẫu số (Dư nợ cho vay) giai đoạn 2023–2025:")
points_q4_1 = [
    ("Agribank (Giảm thực chất cả hai vế): ", "Tử số giảm từ 60.844 tỷ (2023: Nhóm 2 32.179 tỷ + Nợ xấu 28.665 tỷ) xuống 46.892 tỷ năm 2025 (Nhóm 2 21.282 tỷ + Nợ xấu 25.610 tỷ), tức giảm thực chất -13.952 tỷ đồng (-22,9%) nhờ mạnh tay dùng dự phòng xóa nợ 32.621 tỷ đồng năm 2025. Mẫu số tăng ổn định +27,7% (từ 1,54 lên 1,97 triệu tỷ đồng). Tỷ lệ giảm từ 3,93% về 2,37% (-1,56 điểm %) là giảm lành mạnh."),
    ("MBBank (Hiệu ứng mẫu số làm loãng 100%): ", "Tử số tăng từ 23.723 tỷ (2023: Nhóm 2 13.918 tỷ + Nợ xấu 9.805 tỷ) lên 24.237 tỷ năm 2025 (Nhóm 2 10.210 tỷ + Nợ xấu 14.027 tỷ), tức tử số tăng thêm +514 tỷ đồng (nợ xấu nhóm 3-5 tăng +43,1%)! Tỷ lệ nợ nhóm 2-5 giảm từ 3,88% về 2,24% (-1,64 điểm %) hoàn toàn do Mẫu số bùng nổ tăng +77,4% (từ 611.047 tỷ lên 1.084.025 tỷ, riêng năm 2025 tăng tới 39,6%) làm loãng nợ xấu.")
]
for pfx, bdy in points_q4_1:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"• {pfx}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_h2(doc, "2. Hiện tượng El Nino, Rủi ro tín dụng và Chỉ tiêu Môi trường (ESG) tại Agribank:")
points_q4_2 = [
    ("Tác động của El Nino đến rủi ro tín dụng: ", "El Nino gây hạn mặn lịch sử tại ĐBSCL và Tây Nguyên (hai vựa tín dụng lớn nhất của Agribank), làm giảm 30%–50% sản lượng nông sản, đứt gãy dòng tiền trả nợ của nông dân, biến các khoản vay mùa vụ thành nợ nhóm 2 và nhóm 3–5. Đồng thời, đất nhiễm mặn làm sụt giảm giá trị TSBĐ, đẩy LGD tăng vọt."),
    ("Agribank có tính đến yếu tố này vào dự báo không? ", "Có nhận diện chính sách (khoanh nợ, giãn nợ theo thông tư NHNN), nhưng trong mô hình định lượng Stress test hiện hành (Slide 12), Agribank chỉ dùng biến số vĩ mô truyền thống (GDP, lãi suất, tỷ giá), CHƯA lượng hóa chính thức các biến số khí hậu (Climate variables: nhiệt độ, lượng mưa, độ mặn) thành tham số PD/LGD."),
    ("Ba giải pháp đưa chỉ tiêu ESG/Khí hậu vào dự án và kiểm tra sức chịu đựng: ", "1. Thẩm định ESMS: Áp dụng Thông tư 17/2022/TT-NHNN, bổ sung điểm rủi ro khí hậu vào phê duyệt tín dụng; 2. Bảo hiểm thời tiết chỉ số (Parametric Insurance): Liên kết bồi thường tự động khi hạn mặn vượt ngưỡng; 3. Stress test khí hậu NGFS (Slide 24): Mô phỏng kịch bản El Nino cực đoan (+2°C) để trích lập đệm dự phòng đón đầu.")
]
for pfx, bdy in points_q4_2:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  - {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_callout(doc, "LỜI THOẠI TRẢ LỜI MẪU (SPEAKER SCRIPT): ", 
            "'Thưa bạn Kiệt, phân tích toán học tại Slide 08 chỉ ra sự tương phản ngoạn mục: Agribank giảm tỷ lệ nợ có vấn đề là giảm thực chất cả tử số (-22,9% nhờ xóa nợ 32.600 tỷ) và mẫu số tăng vững. Còn MB thì tử số tuyệt đối vẫn tăng +514 tỷ, tỷ lệ giảm thuần túy nhờ mẫu số tăng nóng 39,6% trong năm 2025 làm loãng nợ xấu. Về El Nino, đây là rủi ro vật chất hệ thống đe dọa trực tiếp dòng tiền nông nghiệp. Nhóm khuyến nghị tại Slide 24 rằng Agribank bắt buộc phải đưa kịch bản biến đổi khí hậu NGFS và bảo hiểm chỉ số thời tiết vào mô hình ICAAP thay vì chỉ dự báo GDP và lãi suất đơn thuần.'",
            rgb_prefix=(0, 32, 96))

# QUESTION 5: Q KHANH
add_h1(doc, "CÂU HỎI 5 (Q. KHÁNH): AGRIBANK 100% VỐN NHÀ NƯỚC — TẠI SAO NỢ NHÓM 5 LỚN KÉO DÀI VÀ TỶ LỆ XỬ LÝ THỰC TẾ THẤP?", page_break_before=True)
add_p(doc, "Slide liên quan: Slide 08 (Nợ nhóm 5 chiếm 67%-79%), Slide 18 (Cú sốc Yagi, nợ nhóm 5 và bài học đại án Lifepro).", space_before=1, space_after=4)
doc.paragraphs[-1].runs[0].font.italic = True

add_callout(doc, "KẾT LUẬN TRỰC DIỆN (BLUF): ", 
            "Nguyên nhân sâu xa nhất khiến nợ nhóm 5 của Agribank neo cao (67%-79%) là 'Bẫy bảo toàn vốn Nhà nước' và Điều 219 Bộ luật Hình sự: Cán bộ ngân hàng sợ trách nhiệm làm thất thoát vốn công nếu miễn giảm nợ gốc hay bán nợ chiết khấu, nên chọn cách trích lập 100% dự phòng để 'đóng băng' khoản nợ an toàn về mặt kế toán, cộng với điểm nghẽn thi hành án kéo dài 3-7 năm.")

add_h2(doc, "1. Bốn nguyên nhân bóc tách chuyên sâu:")
points_q5 = [
    ("Bẫy bảo toàn vốn Nhà nước & Trách nhiệm hình sự (Điều 219 BLHS): ", "Agribank chịu sự giám sát tối cao của Thanh tra Chính phủ, Kiểm toán Nhà nước theo Luật 69/2014. Nguyên tắc bất di bất dịch là 'Bảo toàn và phát triển vốn'. Nếu cán bộ ngân hàng thỏa thuận miễn giảm nợ gốc hoặc bán nợ chiết khấu theo giá thị trường, họ đối mặt nguy cơ bị khởi tố tội 'Làm thất thoát tài sản Nhà nước' (Điều 219 BLHS). Giải pháp an toàn nhất là xếp nợ vào nhóm 5, trích lập 100% dự phòng (đúng luật kế toán), nhưng 'đóng băng' nợ trên sổ sách."),
    ("Thanh khoản thị trường TSBĐ đất nông nghiệp đóng băng: ", "88%–92% TSBĐ là đất nông thôn, đấu giá 5–10 lần không người mua do vướng quy định Luật Đất đai và thị trường thứ cấp hẹp."),
    ("Tắc nghẽn tố tụng và thi hành án dân sự kéo dài: ", "Mất quyền thu giữ TSBĐ từ khi Nghị quyết 42 hết hiệu lực, buộc Agribank kiện ra tòa. Trình tự thi hành án kéo dài 3–7 năm do cơ quan thi hành án huyện ngần ngại cưỡng chế trục xuất người nông dân vì vấn đề trật tự an sinh xã hội."),
    ("Gánh nặng nợ tồn đọng lịch sử từ các đại án cũ: ", "Agribank vẫn đang theo dõi xử lý các khoản nợ tồn đọng từ đại án lịch sử (Cho thuê tài chính ALC II, vụ án Lifepro Việt Nam... tại Slide 18). Dù đã trích dự phòng 100%, việc tất toán dứt điểm phải chờ phán quyết thi hành án của cơ quan tư pháp kéo dài hàng chục năm.")
]
for idx, (pfx, bdy) in enumerate(points_q5):
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  {idx+1}. {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_callout(doc, "LỜI THOẠI TRẢ LỜI MẪU (SPEAKER SCRIPT): ", 
            "'Thưa bạn Quốc Khánh, một nghịch lý thể chế là chính cơ chế 100% vốn Nhà nước lại làm tỷ lệ xử lý nợ nhóm 5 của Agribank bị chậm! Bởi vì cán bộ ngân hàng Nhà nước chịu sự điều chỉnh của Điều 219 Bộ luật Hình sự về tội làm thất thoát vốn công. Nếu bán nợ chiết khấu theo giá thị trường như ngân hàng tư nhân, họ rất dễ bị quy trách nhiệm hình sự. Do đó, ngân hàng chọn phương án an toàn nhất: Trích lập đủ 100% dự phòng để bảo vệ an toàn tài chính, nhưng đóng băng khoản nợ lại và chờ đợi quy trình thi hành án dân sự kéo dài nhiều năm.'",
            rgb_prefix=(0, 32, 96))

# APPENDIX
add_h1(doc, "PHỤ LỤC: BẢNG TRA CỨU 10 CHỈ SỐ RỦI RO TÍN DỤNG CỐT LÕI (2020–2025)", page_break_before=True)

headers_app = ["Chỉ số tài chính / Rủi ro tín dụng", "Agribank", "MBBank", "Bản chất rủi ro & Hàm ý so sánh"]
rows_app = [
    ["1. Tăng trưởng tín dụng bình quân (2020–2025)", "10,2% / năm", "26,8% / năm (2025: 39,6%)", "MB tăng trưởng tín dụng nóng gấp 2,6 lần Agribank."],
    ["2. Tỷ lệ NPL Like-for-like năm 2025 (Thuyết minh BCTC)", "1,30% (BCTN: 1,17%)", "1,29% (BCTN: 1,29%)", "Hai ngân hàng hội tụ NPL bề mặt ở mức ~1,30%."],
    ["3. Tỷ lệ Nợ nhóm 2 trên dư nợ (Đỉnh 2023 -> 2025)", "2,44% -> 1,08%", "2,28% -> 0,94%", "Nợ nhóm 2 là chỉ báo sớm (EWI) phản ánh đứt gãy dòng tiền."],
    ["4. Tỷ lệ Nợ có vấn đề (Nhóm 2–5 / Dư nợ) năm 2025", "2,37% (46.892 tỷ)", "2,24% (24.237 tỷ)", "Agri giảm thực chất cả tử và mẫu; MB tử tăng nhưng mẫu loãng."],
    ["5. Tỷ lệ bao phủ nợ xấu (LLCR) năm 2025", "146,3% (Vững chắc)", "93,7% (Rơi dưới 100%)", "MB xả đệm dự phòng từ đỉnh 268% để bảo vệ lợi nhuận."],
    ["6. Chi phí tín dụng (Credit Cost) bình quân", "1,66% dư nợ", "1,75% dư nợ", "Agribank chấp nhận chi phí dự phòng cao để giữ đệm an toàn."],
    ["7. Tỷ trọng Cho vay BĐS & Xây dựng năm 2025", "~4,5% dư nợ", "15,4% dư nợ", "MB rủi ro tập trung ngành cao gấp hơn 3 lần Agribank."],
    ["8. Hệ số an toàn vốn CAR (2025 -> Stress test 2026)", "10,22% -> 8,67%", "11,00% -> 9,73%", "Agri tổn thương vốn (sát sàn 8%); MB tổn thương LNTT (-69,3%)."],
    ["9. Khoảng cách trích thiếu dự phòng IFRS 9", "+3.660 tỷ (+9,8%)", "+14.006 tỷ (+106,5%)", "MB chịu cú sốc lớn tại Stage 2 do MCredit và Trái phiếu DN."],
    ["10. Hiệu quả sinh lời điều chỉnh rủi ro (RORAC proxy)", "10,8% – 16,7%", "31,6% – 49,3%", "MB đánh đổi rủi ro cao để tối đa hóa hiệu suất cổ đông."]
]

table_app = doc.add_table(rows=len(rows_app) + 1, cols=4)
col_widths_app = [Inches(2.4), Inches(1.2), Inches(1.4), Inches(2.2)]
col_align_app = [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT]

for c_idx, h in enumerate(headers_app):
    table_app.rows[0].cells[c_idx].paragraphs[0].text = h
for r_idx, row in enumerate(rows_app):
    for c_idx, val in enumerate(row):
        table_app.rows[r_idx + 1].cells[c_idx].paragraphs[0].text = val
format_table(table_app, col_widths_app, col_align_app)

# SAVE FIXED DOCX
target_docx = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Cam_nang_Tra_loi_Phan_bien_Thuyet_trinh_Agribank_MB.docx"
doc.save(target_docx)
print("SUCCESSFULLY SAVED FIXED DOCX:", target_docx)

# ==============================================================================
# 2. BUILD GOOGLE-DOCS-READY HTML FILE
# ==============================================================================
html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Cẩm nang Hỏi đáp Phản biện Thuyết trình Agribank vs MB</title>
<style>
  body {
    background-color: #f0f2f5;
    font-family: 'Times New Roman', Times, serif;
    color: #202124;
    line-height: 1.5;
    margin: 0;
    padding: 20px;
  }
  .page {
    background-color: #ffffff;
    max-width: 820px;
    margin: 20px auto;
    padding: 60px 70px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    border-radius: 4px;
    box-sizing: border-box;
  }
  .header-block {
    text-align: center;
    border-bottom: 2px solid #002060;
    padding-bottom: 15px;
    margin-bottom: 25px;
  }
  .univ-title {
    font-size: 11pt;
    font-weight: bold;
    color: #002060;
    margin-bottom: 6px;
    text-transform: uppercase;
  }
  .doc-title {
    font-size: 16pt;
    font-weight: bold;
    color: #c00000;
    margin: 12px 0 6px 0;
  }
  .doc-sub {
    font-size: 11pt;
    font-style: italic;
    color: #555555;
    margin-bottom: 4px;
  }
  h1 {
    font-size: 13.5pt;
    color: #002060;
    border-bottom: 1.5px solid #002060;
    padding-bottom: 4px;
    margin-top: 30px;
    margin-bottom: 12px;
  }
  h2 {
    font-size: 11.5pt;
    color: #0f4c81;
    margin-top: 16px;
    margin-bottom: 6px;
  }
  p {
    font-size: 11pt;
    margin: 6px 0;
    text-align: justify;
  }
  .slide-ref {
    font-size: 10pt;
    font-style: italic;
    color: #666666;
    margin-bottom: 10px;
  }
  .callout-bluf {
    background-color: #fdf2f2;
    border-left: 4px solid #c00000;
    padding: 10px 14px;
    margin: 12px 0;
    border-radius: 0 4px 4px 0;
    font-size: 10.5pt;
  }
  .callout-bluf strong {
    color: #c00000;
  }
  .callout-script {
    background-color: #f2f5f9;
    border-left: 4px solid #002060;
    padding: 12px 16px;
    margin: 14px 0;
    border-radius: 0 4px 4px 0;
    font-size: 10.5pt;
    font-style: italic;
  }
  .callout-script strong {
    color: #002060;
    font-style: normal;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 9.5pt;
  }
  th {
    background-color: #002060;
    color: #ffffff;
    font-weight: bold;
    padding: 8px 10px;
    text-align: left;
    border: 1px solid #002060;
  }
  td {
    padding: 7px 10px;
    border: 1px solid #d3d3d3;
    vertical-align: top;
  }
  tr:nth-child(even) td {
    background-color: #f8f9fa;
  }
  .btn-copy {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #002060;
    color: white;
    border: none;
    padding: 12px 20px;
    font-size: 12pt;
    font-weight: bold;
    border-radius: 30px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    cursor: pointer;
    z-index: 999;
  }
  .btn-copy:hover {
    background-color: #0f4c81;
  }
</style>
<script>
function copyAll() {
  const range = document.createRange();
  range.selectNode(document.querySelector('.page'));
  window.getSelection().removeAllRanges();
  window.getSelection().addRange(range);
  document.execCommand('copy');
  alert('Đã copy toàn bộ nội dung! Bạn chỉ cần mở Google Docs (docs.new) và nhấn Ctrl+V để dán.');
}
</script>
</head>
<body>

<button class="btn-copy" onclick="copyAll()">📋 Copy để Dán vào Google Docs</button>

<div class="page">
  <div class="header-block">
    <div class="univ-title">TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN (NEU) — VIỆN NGÂN HÀNG - TÀI CHÍNH</div>
    <div style="font-size: 10pt; font-weight: bold; color: #333;">CHƯƠNG TRÌNH CAO HỌC KHÓA 34 (LỚP K34_3_NH8) — HỌC PHẦN: QUẢN TRỊ RỦI RO</div>
    <div class="doc-title">CẨM NANG HỎI ĐÁP PHẢN BIỆN THUYẾT TRÌNH (DEFENSE HANDBOOK)</div>
    <div style="font-size: 12pt; font-weight: bold; color: #002060; margin-bottom: 6px;">GIẢI ĐÁP 5 CÂU HỎI TRỌNG TÂM CỦA KHÁN GIẢ VÀ HỘI ĐỒNG</div>
    <div class="doc-sub">Chuyên đề: So sánh Mô hình & Thực trạng Quản trị Rủi ro Tín dụng giữa Agribank và MB (2020–2025)</div>
    <div class="doc-sub">Nhóm thực hiện: Nhóm 2 | Giảng viên hướng dẫn: TS. Khúc Thế Anh</div>
  </div>

  <h1>TỔNG HỢP NHANH MA TRẬN 5 CÂU HỎI PHẢN BIỆN & SỐ LIỆU CHỐT</h1>
  <table>
    <thead>
      <tr>
        <th style="width:20%;">Người hỏi & Câu hỏi</th>
        <th style="width:12%; text-align:center;">Slide</th>
        <th style="width:33%;">Luận điểm chốt hạ (BLUF)</th>
        <th style="width:23%;">Số liệu kiểm toán cốt lõi</th>
        <th style="width:12%;">Căn cứ pháp lý</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Lan</strong><br>Dư nợ Nông nghiệp vs Mục tiêu Lợi nhuận</td>
        <td style="text-align:center;">Slide 02, 04,<br>Slide 09, 13</td>
        <td>Có mâu thuẫn (Nghịch lý kép). Cân bằng qua tài trợ chéo 65/35, số hóa giảm CIR, vốn rẻ CASA và cấp vốn NSNN.</td>
        <td>Dư nợ Tam nông 61,7%–70%; NIM 2,5% (vs MB 5%); CIR 35-40%; RORAC 10,8%-16,7% (MB 31,6%-49,3%).</td>
        <td>NĐ 55/2015/NĐ-CP<br>NĐ 116/2018/NĐ-CP<br>Luật 69/2014/QH13</td>
      </tr>
      <tr>
        <td><strong>2. Linh</strong><br>Khó khăn nợ nhóm 5 & TSBĐ Bất động sản</td>
        <td style="text-align:center;">Slide 08, 18</td>
        <td>BĐS nông nghiệp thanh khoản thứ cấp cực thấp; vướng thủ tục nhận chuyển nhượng; mất quyền thu giữ TSBĐ (NQ 42 hết hạn).</td>
        <td>Nợ nhóm 5 chiếm 79,0% nợ xấu (20.220 tỷ); 88%-92% TSBĐ là đất nông thôn; nợ ngoại bảng 278.372 tỷ.</td>
        <td>Luật Đất đai 2013/2024<br>Hết hiệu lực NQ 42<br>Luật 96/2025/QH15</td>
      </tr>
      <tr>
        <td><strong>3. Hồng Hà</strong><br>MB ít trích nợ nhóm 2 theo TT11 & Rủi ro IFRS 9</td>
        <td style="text-align:center;">Slide 15, 16,<br>Slide 20</td>
        <td>TT11 cho khấu trừ TSBĐ nên DP cụ thể = 0. Sang IFRS 9 bị sốc Lifetime ECL Stage 2 (MCredit, TPDN).</td>
        <td>Dư nợ nhóm 2 MB đỉnh 13.918 tỷ (2023). IFRS 9 thiếu hụt 14.006 tỷ (+106,5%), CAR giảm 103 bps.</td>
        <td>Thông tư 11/2021<br>IFRS 9 (SICR / Stage 2)<br>Thông tư 41/2016</td>
      </tr>
      <tr>
        <td><strong>4. Kiệt</strong><br>Slide 08 Tử/Mẫu; El Nino & Rủi ro khí hậu ESG</td>
        <td style="text-align:center;">Slide 08, 12,<br>Slide 24</td>
        <td>Agri giảm thực chất cả tử (-22,9%) và mẫu (+27,7%). MB tử tăng (+514 tỷ), tỷ lệ giảm do tín dụng tăng nóng (+77,4%).</td>
        <td>MB tín dụng tăng 39,6% năm 2025. Agri xóa nợ 32.621 tỷ. El Nino làm mất 30-50% dòng tiền nông hộ ĐBSCL.</td>
        <td>Thông tư 17/2022/TT-NHNN<br>Khung NGFS Climate Risk<br>QĐ 1604/QĐ-NHNN</td>
      </tr>
      <tr>
        <td><strong>5. Q. Khánh</strong><br>Agri 100% vốn NN: Tại sao nợ nhóm 5 lớn kéo dài?</td>
        <td style="text-align:center;">Slide 08, 18</td>
        <td>Bẫy bảo toàn vốn Nhà nước (Điều 219 BLHS sợ trách nhiệm thất thoát nếu miễn giảm gốc/bán nợ chiết khấu); tồn đọng đại án.</td>
        <td>Nợ nhóm 5 neo 67%-79% suốt 6 năm. Dự phòng cụ thể đã trích 100% nhưng nợ đọng chờ thi hành án.</td>
        <td>Luật 69/2014/QH13<br>Điều 219 BLHS 2015<br>Tồn đọng ALC II, Lifepro</td>
      </tr>
    </tbody>
  </table>

  <h1>CÂU HỎI 1 (LAN): DƯ NỢ NÔNG NGHIỆP VS MỤC TIÊU LỢI NHUẬN TẠI AGRIBANK — XUNG ĐỘT THỂ CHẾ VÀ GIẢI PHÁP CÂN BẰNG</h1>
  <div class="slide-ref">Slide liên quan: Slide 02 (Mô hình Agribank), Slide 04 (Đối chiếu quản trị), Slide 09 (Hiệu quả RORAC), Slide 13 (Stress test CAR).</div>
  <div class="callout-bluf">
    <strong>KẾT LUẬN TRỰC DIỆN (BLUF): </strong> Có xung đột nội tại sâu sắc (Dual-Mandate Conflict) giữa sứ mệnh chính trị - xã hội và mục tiêu thương mại. Để hóa giải, Agribank không thể bỏ nông nghiệp mà phải dùng chiến lược 'Tài trợ chéo nội bộ', số hóa hạ CIR và tối ưu nguồn vốn CASA rẻ từ mạng lưới nông thôn.
  </div>
  <h2>1. Bản chất xung đột toán học & tài chính:</h2>
  <p>• <strong>Nghịch lý biên lãi thuần (NIM):</strong> Dư nợ Tam nông chiếm 61,7%–70% (1,2–1,4 triệu tỷ đồng) bị áp trần lãi suất ưu đãi của NHNN (4,0%–4,5%/năm), khiến NIM Agribank chỉ đạt 2,5%–2,8%, trong khi MB đạt 4,5%–5,5% nhờ tự do đẩy mạnh bán lẻ và tiêu dùng.</p>
  <p>• <strong>Gánh nặng chi phí vận hành (CIR):</strong> Để phục vụ hàng triệu nông hộ phân tán vùng sâu vùng xa, Agribank phải vận hành mạng lưới >2.200 chi nhánh/PGD với gần 40.000 nhân sự, đẩy CIR lên 35%–40%.</p>
  <p>• <strong>Chi phí tín dụng (Credit Cost) bào mòn lợi nhuận:</strong> Chi phí trích lập dự phòng bình quân 1,66%/năm ngốn tới 42,8%–59,1% lợi nhuận thuần trước dự phòng (PPOP). Hệ quả là tỷ suất RORAC proxy của Agribank chỉ đạt 10,8%–16,7% (thấp hơn MB từ 15,8–33,8 điểm %).</p>
  <p>• <strong>Áp lực bảo toàn vốn công:</strong> Là DNNN 100% vốn, Agribank phải bảo toàn vốn Nhà nước theo Luật 69/2014 và đảm bảo CAR ≥ 8,0%. Nếu chỉ theo đuổi chính sách xã hội, khả năng tự tích tụ vốn từ lợi nhuận giữ lại suy kiệt, đẩy CAR về ngưỡng nguy hiểm (8,67% trong Stress test cực đoan).</p>
  <h2>2. Bốn giải pháp chiến lược cân bằng hai mục tiêu:</h2>
  <p>1. <strong>Tái cấu trúc danh mục theo tỷ lệ 65/35 (Tài trợ chéo):</strong> Giữ 60%–65% cho Tam nông cốt lõi; dành 35%–40% còn lại cho các phân khúc biên lãi cao: Tài trợ chuỗi giá trị chế biến xuất khẩu (Agribusiness), SME đô thị và bán lẻ thị trấn để bù đắp biên lãi (cross-subsidize).</p>
  <p>2. <strong>Đột phá thu nhập ngoài lãi (Non-interest Income):</strong> Khai thác tệp 20 triệu khách hàng nông thôn bán chéo bảo hiểm liên kết (ABIC), dịch vụ thanh toán công. Triển khai Agribank Digital / Ngân hàng số để hạ CIR từ 40% xuống &lt;32%.</p>
  <p>3. <strong>Tối ưu chi phí vốn (CoF) từ tiền gửi nông thôn:</strong> Nguồn tiền gửi dân cư nông thôn có độ trung thành cao, ít nhạy cảm lãi suất, mang lại nguồn vốn đầu vào rẻ nhất hệ thống, giữ vững biên lợi nhuận.</p>
  <p>4. <strong>Cơ chế cấp bù lãi suất & Tăng vốn NSNN:</strong> Chính phủ cấp bù lãi suất theo Nghị định 55/2015 và Quốc hội định kỳ cấp bổ sung vốn điều lệ từ NSNN (như khoản 17.100 tỷ đồng) hoặc cho phép giữ lại 100% lợi nhuận sau thuế.</p>
  <div class="callout-script">
    <strong>LỜI THOẠI TRẢ LỜI MẪU (SPEAKER SCRIPT): </strong> 'Thưa bạn Lan, đây là nghịch lý kép điển hình của một NHTM Nhà nước. Agribank không thể từ bỏ sứ mệnh Tam nông vì đó là lý do tồn tại thể chế của ngân hàng. Để vừa bảo toàn vốn Nhà nước vừa hoàn thành nhiệm vụ chính trị, Agribank áp dụng chiến lược tài trợ chéo: Dùng nguồn vốn huy động giá rẻ từ mạng lưới 2.200 chi nhánh và lợi nhuận từ mảng doanh nghiệp xuất khẩu/bán lẻ đô thị để bù đắp cho mảng nông nghiệp ưu đãi, kết hợp với việc Nhà nước định kỳ tăng vốn điều lệ từ ngân sách.'
  </div>

  <h1>CÂU HỎI 2 (LINH): SLIDE 08 — NỢ NHÓM 5 NĂM 2025 CAO, KHÓ KHĂN XỬ LÝ TSBĐ BẤT ĐỘNG SẢN & RỦI RO PHÁP LÝ</h1>
  <div class="slide-ref">Slide liên quan: Slide 08 (Nợ nhóm 2, nợ cơ cấu & nợ nhóm 5), Slide 18 (Tình huống Yagi, nợ nhóm 5 và Lifepro).</div>
  <div class="callout-bluf">
    <strong>KẾT LUẬN TRỰC DIỆN (BLUF): </strong> Nợ nhóm 5 của Agribank chiếm tới 79,0% nợ xấu do 88%-92% TSBĐ là đất nông thôn có thanh khoản thứ cấp cực thấp, vướng điều kiện nhận chuyển nhượng của Luật Đất đai, và đặc biệt là bị mất quyền thu giữ TSBĐ khi Nghị quyết 42 hết hiệu lực (khiến thủ tục kiện tụng kéo dài 3-7 năm).
  </div>
  <h2>1. Dữ liệu thực chứng & Bản chất khó khăn với BĐS nông nghiệp:</h2>
  <p>• <strong>Dữ liệu nợ nhóm 5 tại Slide 08:</strong> Năm 2025, nợ nhóm 5 của Agribank là 20.220 tỷ đồng trên 25.610 tỷ nợ xấu (chiếm 79,0%, trong khi MB chỉ chiếm ~40%). Số dư nợ ngoại bảng lũy kế chờ thu hồi lên tới 278.372 tỷ đồng.</p>
  <p>• <strong>Thanh khoản thứ cấp đóng băng:</strong> TSBĐ chủ yếu là đất nông nghiệp, đất rừng, đất nuôi trồng thủy sản, nhà xưởng nông thôn. Thị trường thứ cấp gần như không có giao dịch; tâm lý làng xã kiêng kỵ mua đất phát mại của người cùng quê, còn nhà đầu tư thành phố không có nhu cầu mua đất phân tán vùng sâu vùng xa.</p>
  <p>• <strong>Chu kỳ đấu giá hạ giá kéo dài:</strong> Quy trình phát mại đất nông thôn thường phải tổ chức đấu giá hạ giá từ 5 đến 10 lần (mỗi lần giảm 5%–10%) mà vẫn không có người đăng ký mua, kéo dài 2–3 năm khiến tài sản hoang hóa, suy giảm giá trị.</p>
  <h2>2. Rủi ro pháp lý & Khoảng trống thể chế nghiêm trọng:</h2>
  <p>- <strong>Rào cản đối tượng nhận chuyển nhượng đất nông nghiệp:</strong> Theo Luật Đất đai 2013, tổ chức kinh tế và cá nhân không trực tiếp sản xuất nông nghiệp không được nhận chuyển nhượng đất trồng lúa. Luật Đất đai 2024 (hiệu lực 01/08/2024) đã nới lỏng nhưng vẫn yêu cầu lập phương án sử dụng đất được UBND huyện phê duyệt, loại bỏ phần lớn người mua tiềm năng.</p>
  <p>- <strong>Khoảng trống pháp lý khi Nghị quyết 42 hết hiệu lực (Rủi ro lớn nhất 2024–2025):</strong> Nghị quyết 42 hết hiệu lực từ 31/12/2023 nhưng quyền thu giữ TSBĐ không được đưa đầy đủ vào Luật Các TCTD 2024. Khi bên vay bất hợp tác, Agribank không có quyền cưỡng chế thu giữ đất, buộc phải kiện ra Tòa án dân sự.</p>
  <p>- <strong>Điểm nghẽn thi hành án kéo dài 3–7 năm:</strong> Quy trình khởi kiện sơ thẩm, phúc thẩm và thi hành án dân sự huyện kéo dài nhiều năm. Cơ quan thi hành án huyện thường ngần ngại cưỡng chế trục xuất người nông dân vì e ngại an ninh trật tự xã hội địa phương, khiến nợ nhóm 5 bị 'đóng băng' nội bảng.</p>
  <p>- <strong>Lối thoát thể chế từ 2026:</strong> Nút thắt này chỉ được gỡ khi Quốc hội thông qua Luật số 96/2025/QH15 khôi phục lại quyền thu giữ TSBĐ cho TCTD, có hiệu lực từ đầu năm 2026.</p>
  <div class="callout-script">
    <strong>LỜI THOẠI TRẢ LỜI MẪU (SPEAKER SCRIPT): </strong> 'Thưa bạn Linh, nợ nhóm 5 của Agribank cao tới 79,0% không phải vì ngân hàng không muốn xử lý, mà vì vướng điểm nghẽn kép: Thứ nhất, 90% TSBĐ là đất nông nghiệp vùng sâu vùng xa không có thanh khoản thị trường thứ cấp. Thứ hai và nguy hiểm nhất là khoảng trống pháp lý khi Nghị quyết 42 hết hiệu lực cuối năm 2023 làm ngân hàng mất quyền chủ động thu giữ TSBĐ. Mọi vụ việc đều phải qua Tòa án và thi hành án kéo dài 3–7 năm. Phải chờ Luật số 96/2025 có hiệu lực từ năm 2026 thì nút thắt thu giữ TSBĐ này mới được tháo gỡ triệt để.'
  </div>

  <h1>CÂU HỎI 3 (HỒNG HÀ): IFRS 9 VS THÔNG TƯ 11 — TẠI SAO MB KHÔNG TRÍCH LẬP MẤY CHO NỢ NHÓM 2? RỦI RO NẾU CHỈ THEO THÔNG TƯ</h1>
  <div class="slide-ref">Slide liên quan: Slide 15 (Phương pháp & Tham số IFRS 9), Slide 16 (Kết quả mô phỏng IFRS 9), Slide 20 (Cú sốc chất lượng tài sản MB 2023).</div>
  <div class="callout-bluf">
    <strong>KẾT LUẬN TRỰC DIỆN (BLUF): </strong> Theo Thông tư 11, cơ chế khấu trừ giá trị TSBĐ khiến Dự phòng cụ thể của nợ nhóm 2 bằng 0 đồng (chỉ trích 0,75% DP chung). Nhưng sang IFRS 9, nợ nhóm 2 bị xếp vào Stage 2 (SICR) bắt buộc tính Lifetime ECL, khiến MB lộ khoảng cách trích thiếu tới 14.006 tỷ đồng (+106,5%) do rủi ro từ MCredit và Trái phiếu DN.
  </div>
  <h2>1. Tại sao MB 'không trích lập mấy' cho nợ nhóm 2 theo quy định hiện hành?</h2>
  <p>• <strong>Công thức khấu trừ TSBĐ theo Thông tư 11/2021:</strong> Dự phòng cụ thể (DPCT) nợ nhóm 2 tính theo công thức: R = max(0, A - C) × 5%. Trong đó A là dư nợ, C là giá trị khấu trừ TSBĐ (BĐS chiết khấu 50%). Khi giá trị TSBĐ sau chiết khấu lớn hơn dư nợ (C ≥ A), phần chênh lệch (A - C) ≤ 0, dẫn tới DPCT = 0 đồng!</p>
  <p>• <strong>Thực tế danh mục cho vay MB:</strong> Các khoản vay cá nhân, hộ kinh doanh và doanh nghiệp BĐS tại MB đều có tỷ lệ LTV từ 50%–70%. Do đó, với 13.918 tỷ nợ nhóm 2 năm 2023, MB gần như chỉ phải trích 0,75% Dự phòng chung (~104 tỷ đồng), hoàn toàn không phải trích DPCT.</p>
  <p>• <strong>Động cơ kinh tế của NHTMCP niêm yết:</strong> MB tận dụng quy định này để không phải ghi nhận chi phí dự phòng lớn, giúp bảo vệ con số lợi nhuận trước thuế theo cam kết với cổ đông (kế hoạch PBT >26.000 tỷ năm 2023).</p>
  <h2>2. Cú sốc chuyển đổi IFRS 9 và 4 rủi ro lớn nếu chỉ áp dụng Thông tư 11:</h2>
  <p>- <strong>Cú sốc Lifetime ECL tại Stage 2 (Slide 15, 16):</strong> IFRS 9 xóa bỏ mô hình tổn thất đã phát sinh (Incurred Loss). Nợ nhóm 2 là diện gia tăng rủi ro tín dụng đáng kể (SICR - Stage 2), bắt buộc tính Lifetime ECL = EAD × PD_lifetime × LGD. Với PD trọn vòng đời lên tới 15%–25%, cộng với danh mục MCredit (tín chấp 100%, LGD 80%-90%) và 30% danh mục TPDN (7.023 tỷ) rơi vào Stage 2, MB bị thiếu hụt dự phòng tới 14.006 tỷ (+106,5%), ăn mòn 7,9% vốn CSH và giảm 103 bps hệ số CAR.</p>
  <p>- <strong>Rủi ro Lợi nhuận ảo (Paper Profits):</strong> Ghi nhận lợi nhuận cao giả tạo, chi trả cổ tức tiền mặt và thưởng ban điều hành trên những đồng lợi nhuận chưa trừ đủ chi phí rủi ro thực tế.</p>
  <p>- <strong>Cú sốc vách đá trích lập (Cliff Effect):</strong> Khi nợ nhóm 2 không phục hồi mà rơi xuống nhóm 3 (trích 20%), nhóm 4 (50%), nhóm 5 (100%), chi phí dự phòng sẽ bùng nổ đột ngột hàng nghìn tỷ, xóa sạch lợi nhuận quý.</p>
  <p>- <strong>Ảo tưởng thanh lý TSBĐ & Hạ bậc tín nhiệm quốc tế:</strong> Thông tư 11 giả định TSBĐ bán được ngay, nhưng thực tế xử lý BĐS mất 3–5 năm với mức chiết khấu 30%–50%. Các tổ chức xếp hạng (Moody's, S&P) sẽ tự động chiết trừ vốn tự có khi thấy LLCR của MB tụt xuống dưới 100% (93,7% năm 2025).</p>
  <div class="callout-script">
    <strong>LỜI THOẠI TRẢ LỜI MẪU (SPEAKER SCRIPT): </strong> 'Thưa bạn Hồng Hà, MB không trích lập nhiều cho nợ nhóm 2 vì họ hoàn toàn tuân thủ Thông tư 11: Khi khoản vay có TSBĐ đầy đủ thì dự phòng cụ thể được khấu trừ về 0, chỉ mất 0,75% dự phòng chung. Nhưng đó chính là lỗ hổng của mô hình tổn thất đã phát sinh! Khi chuyển sang IFRS 9, nợ nhóm 2 bị kích hoạt Stage 2 tính tổn thất trọn vòng đời. Vì MB có khối tín dụng tiêu dùng tín chấp MCredit và 30% trái phiếu doanh nghiệp rủi ro, khoảng cách dự phòng trích thiếu vọt lên hơn 14.000 tỷ đồng. Nếu chỉ chạy theo Thông tư, ngân hàng sẽ rơi vào bẫy 'lợi nhuận ảo' và đối mặt cú sốc vách đá khi nợ xấu thực tế bùng phát.'
  </div>

  <h1>CÂU HỎI 4 (KIỆT): SLIDE 08 PHÂN RÃ TỬ/MẪU; HIỆN TƯỢNG EL NINO, DỰ BÁO VĨ MÔ & ESG TẠI AGRIBANK</h1>
  <div class="slide-ref">Slide liên quan: Slide 08 (Tỷ lệ nợ nhóm 2–5 / Dư nợ), Slide 12 (Tham số kịch bản Stress test), Slide 24 (Kiến nghị ESG & Stress test khí hậu cho Agribank).</div>
  <div class="callout-bluf">
    <strong>KẾT LUẬN TRỰC DIỆN (BLUF): </strong> Tại Slide 08, Agribank giảm tỷ lệ nợ nhóm 2-5 là nhờ Tử số giảm thực chất (-22,9%) kết hợp Mẫu số tăng ổn định (+27,7%). Ngược lại, tại MB, Tử số không giảm mà còn tăng (+514 tỷ), tỷ lệ giảm 100% do Mẫu số tăng trưởng nóng làm loãng (+77,4%). Về El Nino, rủi ro thiên tai làm đứt gãy dòng tiền nông hộ nghiêm trọng nhưng Agribank mới chỉ dự báo vĩ mô truyền thống, cần tích hợp kịch bản khí hậu NGFS vào thẩm định ESG.
  </div>
  <h2>1. Bóc tách toán học Slide 08: Tử số (Nợ có vấn đề) vs Mẫu số (Dư nợ cho vay) giai đoạn 2023–2025:</h2>
  <p>• <strong>Agribank (Giảm thực chất cả hai vế):</strong> Tử số giảm từ 60.844 tỷ (2023: Nhóm 2 32.179 tỷ + Nợ xấu 28.665 tỷ) xuống 46.892 tỷ năm 2025 (Nhóm 2 21.282 tỷ + Nợ xấu 25.610 tỷ), tức giảm thực chất -13.952 tỷ đồng (-22,9%) nhờ mạnh tay dùng dự phòng xóa nợ 32.621 tỷ đồng năm 2025. Mẫu số tăng ổn định +27,7% (từ 1,54 lên 1,97 triệu tỷ đồng). Tỷ lệ giảm từ 3,93% về 2,37% (-1,56 điểm %) là giảm lành mạnh.</p>
  <p>• <strong>MBBank (Hiệu ứng mẫu số làm loãng 100%):</strong> Tử số tăng từ 23.723 tỷ (2023: Nhóm 2 13.918 tỷ + Nợ xấu 9.805 tỷ) lên 24.237 tỷ năm 2025 (Nhóm 2 10.210 tỷ + Nợ xấu 14.027 tỷ), tức tử số tăng thêm +514 tỷ đồng (nợ xấu nhóm 3-5 tăng +43,1%)! Tỷ lệ nợ nhóm 2-5 giảm từ 3,88% về 2,24% (-1,64 điểm %) hoàn toàn do Mẫu số bùng nổ tăng +77,4% (từ 611.047 tỷ lên 1.084.025 tỷ, riêng năm 2025 tăng tới 39,6%) làm loãng nợ xấu.</p>
  <h2>2. Hiện tượng El Nino, Rủi ro tín dụng và Chỉ tiêu Môi trường (ESG) tại Agribank:</h2>
  <p>- <strong>Tác động của El Nino đến rủi ro tín dụng:</strong> El Nino gây hạn mặn lịch sử tại ĐBSCL và Tây Nguyên (hai vựa tín dụng lớn nhất của Agribank), làm giảm 30%–50% sản lượng nông sản, đứt gãy dòng tiền trả nợ của nông dân, biến các khoản vay mùa vụ thành nợ nhóm 2 và nhóm 3–5. Đồng thời, đất nhiễm mặn làm sụt giảm giá trị TSBĐ, đẩy LGD tăng vọt.</p>
  <p>- <strong>Agribank có tính đến yếu tố này vào dự báo không?</strong> Có nhận diện chính sách (khoanh nợ, giãn nợ theo thông tư NHNN), nhưng trong mô hình định lượng Stress test hiện hành (Slide 12), Agribank chỉ dùng biến số vĩ mô truyền thống (GDP, lãi suất, tỷ giá), CHƯA lượng hóa chính thức các biến số khí hậu (Climate variables: nhiệt độ, lượng mưa, độ mặn) thành tham số PD/LGD.</p>
  <p>- <strong>Ba giải pháp đưa chỉ tiêu ESG/Khí hậu vào dự án và kiểm tra sức chịu đựng:</strong> 1. Thẩm định ESMS: Áp dụng Thông tư 17/2022/TT-NHNN, bổ sung điểm rủi ro khí hậu vào phê duyệt tín dụng; 2. Bảo hiểm thời tiết chỉ số (Parametric Insurance): Liên kết bồi thường tự động khi hạn mặn vượt ngưỡng; 3. Stress test khí hậu NGFS (Slide 24): Mô phỏng kịch bản El Nino cực đoan (+2°C) để trích lập đệm dự phòng đón đầu.</p>
  <div class="callout-script">
    <strong>LỜI THOẠI TRẢ LỜI MẪU (SPEAKER SCRIPT): </strong> 'Thưa bạn Kiệt, phân tích toán học tại Slide 08 chỉ ra sự tương phản ngoạn mục: Agribank giảm tỷ lệ nợ có vấn đề là giảm thực chất cả tử số (-22,9% nhờ xóa nợ 32.600 tỷ) và mẫu số tăng vững. Còn MB thì tử số tuyệt đối vẫn tăng +514 tỷ, tỷ lệ giảm thuần túy nhờ mẫu số tăng nóng 39,6% trong năm 2025 làm loãng nợ xấu. Về El Nino, đây là rủi ro vật chất hệ thống đe dọa trực tiếp dòng tiền nông nghiệp. Nhóm khuyến nghị tại Slide 24 rằng Agribank bắt buộc phải đưa kịch bản biến đổi khí hậu NGFS và bảo hiểm chỉ số thời tiết vào mô hình ICAAP thay vì chỉ dự báo GDP và lãi suất đơn thuần.'
  </div>

  <h1>CÂU HỎI 5 (Q. KHÁNH): AGRIBANK 100% VỐN NHÀ NƯỚC — TẠI SAO NỢ NHÓM 5 LỚN KÉO DÀI VÀ TỶ LỆ XỬ LÝ THỰC TẾ THẤP?</h1>
  <div class="slide-ref">Slide liên quan: Slide 08 (Nợ nhóm 5 chiếm 67%-79%), Slide 18 (Cú sốc Yagi, nợ nhóm 5 và bài học đại án Lifepro).</div>
  <div class="callout-bluf">
    <strong>KẾT LUẬN TRỰC DIỆN (BLUF): </strong> Nguyên nhân sâu xa nhất khiến nợ nhóm 5 của Agribank neo cao (67%-79%) là 'Bẫy bảo toàn vốn Nhà nước' và Điều 219 Bộ luật Hình sự: Cán bộ ngân hàng sợ trách nhiệm làm thất thoát vốn công nếu miễn giảm nợ gốc hay bán nợ chiết khấu, nên chọn cách trích lập 100% dự phòng để 'đóng băng' khoản nợ an toàn về mặt kế toán, cộng với điểm nghẽn thi hành án kéo dài 3-7 năm.
  </div>
  <h2>1. Bốn nguyên nhân bóc tách chuyên sâu:</h2>
  <p>1. <strong>Bẫy bảo toàn vốn Nhà nước & Trách nhiệm hình sự (Điều 219 BLHS):</strong> Agribank chịu sự giám sát tối cao của Thanh tra Chính phủ, Kiểm toán Nhà nước theo Luật 69/2014. Nguyên tắc bất di bất dịch là 'Bảo toàn và phát triển vốn'. Nếu cán bộ ngân hàng thỏa thuận miễn giảm nợ gốc hoặc bán nợ chiết khấu theo giá thị trường, họ đối mặt nguy cơ bị khởi tố tội 'Làm thất thoát tài sản Nhà nước' (Điều 219 BLHS). Giải pháp an toàn nhất là xếp nợ vào nhóm 5, trích lập 100% dự phòng (đúng luật kế toán), nhưng 'đóng băng' nợ trên sổ sách.</p>
  <p>2. <strong>Thanh khoản thị trường TSBĐ đất nông nghiệp đóng băng:</strong> 88%–92% TSBĐ là đất nông thôn, đấu giá 5–10 lần không người mua do vướng quy định Luật Đất đai và thị trường thứ cấp hẹp.</p>
  <p>3. <strong>Tắc nghẽn tố tụng và thi hành án dân sự kéo dài:</strong> Mất quyền thu giữ TSBĐ từ khi Nghị quyết 42 hết hiệu lực, buộc Agribank kiện ra tòa. Trình tự thi hành án kéo dài 3–7 năm do cơ quan thi hành án huyện ngần ngại cưỡng chế trục xuất người nông dân vì vấn đề trật tự an sinh xã hội.</p>
  <p>4. <strong>Gánh nặng nợ tồn đọng lịch sử từ các đại án cũ:</strong> Agribank vẫn đang theo dõi xử lý các khoản nợ tồn đọng từ đại án lịch sử (Cho thuê tài chính ALC II, vụ án Lifepro Việt Nam... tại Slide 18). Dù đã trích dự phòng 100%, việc tất toán dứt điểm phải chờ phán quyết thi hành án của cơ quan tư pháp kéo dài hàng chục năm.</p>
  <div class="callout-script">
    <strong>LỜI THOẠI TRẢ LỜI MẪU (SPEAKER SCRIPT): </strong> 'Thưa bạn Quốc Khánh, một nghịch lý thể chế là chính cơ chế 100% vốn Nhà nước lại làm tỷ lệ xử lý nợ nhóm 5 của Agribank bị chậm! Bởi vì cán bộ ngân hàng Nhà nước chịu sự điều chỉnh của Điều 219 Bộ luật Hình sự về tội làm thất thoát vốn công. Nếu bán nợ chiết khấu theo giá thị trường như ngân hàng tư nhân, họ rất dễ bị quy trách nhiệm hình sự. Do đó, ngân hàng chọn phương án an toàn nhất: Trích lập đủ 100% dự phòng để bảo vệ an toàn tài chính, nhưng đóng băng khoản nợ lại và chờ đợi quy trình thi hành án dân sự kéo dài nhiều năm.'
  </div>

  <h1>PHỤ LỤC: BẢNG TRA CỨU 10 CHỈ SỐ RỦI RO TÍN DỤNG CỐT LÕI (2020–2025)</h1>
  <table>
    <thead>
      <tr>
        <th style="width:30%;">Chỉ số tài chính / Rủi ro tín dụng</th>
        <th style="width:16%; text-align:center;">Agribank</th>
        <th style="width:18%; text-align:center;">MBBank</th>
        <th style="width:36%;">Bản chất rủi ro & Hàm ý so sánh</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1. Tăng trưởng tín dụng bình quân (2020–2025)</td>
        <td style="text-align:center;">10,2% / năm</td>
        <td style="text-align:center;">26,8% / năm (2025: 39,6%)</td>
        <td>MB tăng trưởng tín dụng nóng gấp 2,6 lần Agribank.</td>
      </tr>
      <tr>
        <td>2. Tỷ lệ NPL Like-for-like năm 2025 (Thuyết minh BCTC)</td>
        <td style="text-align:center;">1,30% (BCTN: 1,17%)</td>
        <td style="text-align:center;">1,29% (BCTN: 1,29%)</td>
        <td>Hai ngân hàng hội tụ NPL bề mặt ở mức ~1,30%.</td>
      </tr>
      <tr>
        <td>3. Tỷ lệ Nợ nhóm 2 trên dư nợ (Đỉnh 2023 -> 2025)</td>
        <td style="text-align:center;">2,44% -> 1,08%</td>
        <td style="text-align:center;">2,28% -> 0,94%</td>
        <td>Nợ nhóm 2 là chỉ báo sớm (EWI) phản ánh đứt gãy dòng tiền.</td>
      </tr>
      <tr>
        <td>4. Tỷ lệ Nợ có vấn đề (Nhóm 2–5 / Dư nợ) năm 2025</td>
        <td style="text-align:center;">2,37% (46.892 tỷ)</td>
        <td style="text-align:center;">2,24% (24.237 tỷ)</td>
        <td>Agri giảm thực chất cả tử và mẫu; MB tử tăng nhưng mẫu loãng.</td>
      </tr>
      <tr>
        <td>5. Tỷ lệ bao phủ nợ xấu (LLCR) năm 2025</td>
        <td style="text-align:center;">146,3% (Vững chắc)</td>
        <td style="text-align:center;">93,7% (Rơi dưới 100%)</td>
        <td>MB xả đệm dự phòng từ đỉnh 268% để bảo vệ lợi nhuận.</td>
      </tr>
      <tr>
        <td>6. Chi phí tín dụng (Credit Cost) bình quân</td>
        <td style="text-align:center;">1,66% dư nợ</td>
        <td style="text-align:center;">1,75% dư nợ</td>
        <td>Agribank chấp nhận chi phí dự phòng cao để giữ đệm an toàn.</td>
      </tr>
      <tr>
        <td>7. Tỷ trọng Cho vay BĐS & Xây dựng năm 2025</td>
        <td style="text-align:center;">~4,5% dư nợ</td>
        <td style="text-align:center;">15,4% dư nợ</td>
        <td>MB rủi ro tập trung ngành cao gấp hơn 3 lần Agribank.</td>
      </tr>
      <tr>
        <td>8. Hệ số an toàn vốn CAR (2025 -> Stress test 2026)</td>
        <td style="text-align:center;">10,22% -> 8,67%</td>
        <td style="text-align:center;">11,00% -> 9,73%</td>
        <td>Agri tổn thương vốn (sát sàn 8%); MB tổn thương LNTT (-69,3%).</td>
      </tr>
      <tr>
        <td>9. Khoảng cách trích thiếu dự phòng IFRS 9</td>
        <td style="text-align:center;">+3.660 tỷ (+9,8%)</td>
        <td style="text-align:center;">+14.006 tỷ (+106,5%)</td>
        <td>MB chịu cú sốc lớn tại Stage 2 do MCredit và Trái phiếu DN.</td>
      </tr>
      <tr>
        <td>10. Hiệu quả sinh lời điều chỉnh rủi ro (RORAC proxy)</td>
        <td style="text-align:center;">10,8% – 16,7%</td>
        <td style="text-align:center;">31,6% – 49,3%</td>
        <td>MB đánh đổi rủi ro cao để tối đa hóa hiệu suất cổ đông.</td>
      </tr>
    </tbody>
  </table>
</div>

</body>
</html>
"""

target_html = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Cam_nang_Tra_loi_Phan_bien_Thuyet_trinh_Agribank_MB.html"
with open(target_html, "w", encoding="utf-8") as f:
    f.write(html_content)
print("SUCCESSFULLY SAVED GOOGLE-DOCS-READY HTML:", target_html)

