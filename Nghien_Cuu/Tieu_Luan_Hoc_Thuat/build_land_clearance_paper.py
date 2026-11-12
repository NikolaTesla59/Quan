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

def add_callout(doc, text_prefix, text_body, rgb_prefix=(192, 0, 0), bg_hex="F2F5F9", border_color="002060"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    tblPr = tbl._element.xpath('w:tblPr')[0]
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>'
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
# BUILD STANDALONE DOCUMENT
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
r_head = p_head.add_run("Quản trị Rủi ro Tín dụng — Chuyên đề: BĐS Dính Giải tỏa Mặt bằng")
style_run(r_head, size_pt=8.5, italic=True, color_rgb=(120, 120, 120))

# Configure Footer
footer = section.footer
p_foot = footer.paragraphs[0]
p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_foot = p_foot.add_run("Tài liệu Phân tích Nghiệp vụ Ngân hàng — Cao học Khóa 34 NEU")
style_run(r_foot, size_pt=8.5, italic=True, color_rgb=(120, 120, 120))

# Title Block
p_top = add_p(doc, "TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN (NEU) — VIỆN NGÂN HÀNG - TÀI CHÍNH\nCHƯƠNG TRÌNH CAO HỌC KHÓA 34 (LỚP K34_3_NH8) — HỌC PHẦN: QUẢN TRỊ RỦI RO", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=6)
for r in p_top.runs:
    style_run(r, size_pt=9.5, bold=True, color_rgb=(0, 32, 96))

p_title = add_p(doc, "BÁO CÁO PHÂN TÍCH NGHIỆP VỤ & GIẢI TRÌNH CHUYÊN SÂU:\nCƠ CHẾ DỰ PHÒNG & QUẢN TRỊ RỦI RO ĐỐI VỚI KHOẢN VAY DÍNH GIẢI TỎA MẶT BẰNG", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=4)
for r in p_title.runs:
    style_run(r, size_pt=13.5, bold=True, color_rgb=(192, 0, 0))

p_sub = add_p(doc, "Giải quyết câu hỏi thực tế: Liệu trích lập dự phòng có cover được chênh lệch giữa giá thị trường và giá đền bù giải tỏa?\nNgười thực hiện: Nhóm 2 — K34_3_NH8 | Giảng viên hướng dẫn: TS. Khúc Thế Anh", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=12)
for r in p_sub.runs:
    style_run(r, size_pt=9.5, italic=True, color_rgb=(80, 80, 80))

# BLUF Callout
add_callout(doc, "TỔNG LUẬN ĐIỀU HÀNH (BOTTOM LINE UP FRONT - BLUF): ",
            "1. Dự phòng đơn thuần là bút toán kế toán ghi nhận trước tổn thất (Loss Recognition), KHÔNG THỂ sinh ra dòng tiền bù đắp khoản tiền bị mất nếu tiền đền bù thấp hơn nợ gốc.\n"
            "2. Về mặt kỹ thuật trích lập: Ngân hàng CÓ phương án tính toán để bao phủ trước rủi ro bằng cách TÁI ĐỊNH GIÁ TSBĐ VỀ GIÁ BỒI THƯỜNG DỰ KIẾN (ép giá trị khấu trừ C sụt giảm để trích đủ dự phòng cụ thể theo TT11) hoặc KÍCH HOẠT STAGE 2 THEO IFRS 9 với LGD tăng vọt.\n"
            "3. Về mặt bảo toàn vốn thực tế: Ngân hàng BẮT BUỘC phải dùng công cụ quản trị rủi ro ngay từ đầu (Cắt lộ giới định giá 0đ, Điều khoản Event of Default buộc bổ sung TSBĐ, và Phong tỏa tài khoản tiền đền bù từ Ban GPMB).",
            rgb_prefix=(192, 0, 0), bg_hex="FDF2F2", border_color="C00000")

# SECTION 1
add_h1(doc, "1. NGHỊCH LÝ SỐ HỌC: TẠI SAO LTV 50%–70% VẪN 'CHÁY TÀI KHOẢN' KHI DÍNH GIẢI TỎA?")
add_p(doc, "Trong thực tiễn cấp tín dụng, nhiều người lầm tưởng rằng mức khống chế tỷ lệ cho vay trên định giá (LTV) từ 50% đến 70% là một 'bộ đệm an toàn tuyệt đối' (30%–50% giá trị tài sản). Tuy nhiên, khi bất động sản bị Nhà nước thu hồi đất để phục vụ các dự án hạ tầng công cộng, bộ đệm này hoàn toàn có thể bị xuyên thủng do sự chênh lệch rất lớn giữa giá thị trường giao dịch tự do và giá bồi thường giải phóng mặt bằng (GPMB).")

# Simulation Table
headers_sim = ["Chỉ tiêu tài chính / Thẩm định", "Giá trị ghi nhận", "Bản chất rủi ro & Cơ chế phát sinh"]
rows_sim = [
    ["1. Giá trị thị trường thẩm định ban đầu (V_market)", "10,0 tỷ đồng", "Định giá theo phương pháp so sánh thị trường tại thời điểm vay thuận lợi."],
    ["2. Tỷ lệ cho vay trên định giá (LTV 70%)", "70%", "Ngân hàng giả định có đệm an toàn vốn 30% (3,0 tỷ đồng)."],
    ["3. Dư nợ gốc giải ngân ban đầu (L_0)", "7,0 tỷ đồng", "Khoản vay thế chấp bằng quyền sử dụng đất và nhà ở."],
    ["4. Dư nợ gốc + Lãi dồn tích sau 2 năm quá hạn (A)", "8,5 tỷ đồng", "Khách hàng gặp khó khăn, lãi mẹ đẻ lãi con, chuyển thành nợ xấu."],
    ["5. Giá bồi thường GPMB được phê duyệt (V_GPMB)", "4,5 tỷ đồng", "Áp theo bảng giá đất & hệ số bồi thường (chỉ bằng 45% giá thị trường)."],
    ["6. TỔN THẤT THỰC TẾ KHÔNG THỂ THU HỒI (LOSS)", "-4,0 tỷ đồng", "8,5 tỷ - 4,5 tỷ = 4,0 tỷ đồng (Mất trắng 47% tổng dư nợ và 57% nợ gốc!)."]
]
table_sim = doc.add_table(rows=len(rows_sim) + 1, cols=3)
col_widths_sim = [Inches(2.5), Inches(1.3), Inches(2.87)]
col_align_sim = [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT]
for c_idx, h in enumerate(headers_sim):
    table_sim.rows[0].cells[c_idx].paragraphs[0].text = h
for r_idx, row in enumerate(rows_sim):
    for c_idx, val in enumerate(row):
        table_sim.rows[r_idx + 1].cells[c_idx].paragraphs[0].text = val
format_table(table_sim, col_widths_sim, col_align_sim)

add_h2(doc, "Lỗ hổng của mô hình trích lập dự phòng Thông tư 11 hiện hành:")
points_s1 = [
    ("Công thức dự phòng cụ thể Thông tư 11: ", "R = max(0, A - C) × r. Trong đó giá trị khấu trừ C = V_định_giá × 50% (đối với BĐS)."),
    ("Hiện tượng 'bị mù' trước rủi ro quy hoạch: ", "Nếu ngân hàng không kịp thời cập nhật thông tin quy hoạch và vẫn giữ nguyên giá trị định giá cũ V = 10 tỷ đồng trên hệ thống, giá trị khấu trừ C = 5 tỷ đồng. Nếu khoản nợ ở nhóm 1 hoặc nhóm 2 (trích 5% trên phần chênh lệch), ngân hàng chỉ trích vài chục triệu đồng dự phòng chung (0,75%)."),
    ("Hậu quả cú sốc vách đá (Cliff Effect): ", "Ngân hàng duy trì trạng thái 'an toàn ảo' cho tới khi có quyết định thu hồi đất và phương án bồi thường 4,5 tỷ đồng được công bố. Khi đó, khoản nợ rơi tự do xuống nhóm 5, ngân hàng phải ghi nhận một khoản chi phí dự phòng bổ sung đột ngột tới 4,0 tỷ đồng trong một quý, xóa sạch lợi nhuận chi nhánh.")
]
for pfx, bdy in points_s1:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"• {pfx}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

# SECTION 2
add_h1(doc, "2. PHƯƠNG ÁN KỸ THUẬT TRÍCH LẬP DỰ PHÒNG NÀO CÓ THỂ 'COVER' ĐƯỢC RỦI RO NÀY?")
add_p(doc, "Để tài chính hóa và phản ánh trung thực rủi ro này lên báo cáo tài chính trước khi việc bồi thường diễn ra, các ngân hàng tiên tiến áp dụng 3 phương án kỹ thuật trích lập sau:")

add_h2(doc, "Phương án 1: Tái định giá cưỡng bức theo 'Giá bồi thường dự kiến' (Chuẩn Thông tư 11 & Thông tư 31)")
add_p(doc, "Theo Điều 12 Thông tư 11/2021/TT-NHNN, TCTD có trách nhiệm định giá lại TSBĐ khi có biến động bất thường. Ngay khi khu vực có Thông báo thu hồi đất hoặc văn bản phê duyệt quy hoạch dự án:")
points_opt1 = [
    ("Hạ giá định giá về giá bồi thường: ", "Định giá viên không được dùng giá thị trường tự do nữa, mà chuyển sang dùng Giá bồi thường dự kiến: V_định_giá_mới = V_GPMB = 4,5 tỷ đồng."),
    ("Ép giá trị khấu trừ C sụt giảm: ", "Giá trị khấu trừ hợp lệ sau chiết khấu 50% chỉ còn: C = 4,5 tỷ × 50% = 2,25 tỷ đồng."),
    ("Kích hoạt trích lập Dự phòng cụ thể ngay lập tức: ", "Phần dư nợ không có bảo đảm vọt lên: (A - C) = 8,5 - 2,25 = 6,25 tỷ đồng. Khi nợ chuyển nhóm 3 (trích 20%), nhóm 4 (trích 50%), hoặc nhóm 5 (trích 100%), ngân hàng trích lập dự phòng đầy đủ theo từng kỳ, chia nhỏ cú sốc chi phí ra nhiều quý thay vì bị động chịu trận ở thời điểm cuối.")
]
for pfx, bdy in points_opt1:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  - {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_h2(doc, "Phương án 2: Mô phỏng theo Chuẩn mực Quốc tế IFRS 9 ECL (Tổn thất trọn vòng đời)")
add_p(doc, "IFRS 9 xóa bỏ hoàn toàn mô hình tổn thất đã phát sinh (Incurred Loss) và cơ chế né trích lập bằng TSBĐ:")
points_opt2 = [
    ("Kích hoạt SICR chuyển sang Stage 2: ", "Sự kiện tài sản thế chấp bị quy hoạch giải tỏa được xếp vào diện Gia tăng rủi ro tín dụng đáng kể (Significant Increase in Credit Risk - SICR), đẩy khoản vay từ Stage 1 sang Stage 2."),
    ("Tính toán Lifetime ECL: ", "Công thức bắt buộc là: ECL = EAD × PD_lifetime × LGD_adjusted."),
    ("Điều chỉnh trực tiếp tham số LGD (Loss Given Default): ", "LGD không còn áp dụng tỷ lệ cố định (như 45% của Basel), mà tính toán dựa trên hiện tại hóa dòng tiền thu hồi kỳ vọng: LGD_adjusted = 1 - (Tiền bồi thường GPMB / Dư nợ) = 1 - (4,5 / 8,5) ≈ 47%. Nhân với PD trọn đời của Stage 2 (từ 20%–30%), số dự phòng phải trích lập tự động tăng vọt gấp 5 đến 8 lần, tạo ra bộ đệm vốn bao phủ toàn diện trước khi sự việc diễn ra.")
]
for pfx, bdy in points_opt2:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  - {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_h2(doc, "Phương án 3: Trích lập đệm dự phòng danh mục (Management Overlay Buffer)")
add_p(doc, "Đối với các chi nhánh ngân hàng nằm trên địa bàn có các đại dự án hạ tầng đi qua (Vành đai 4 Hà Nội, Vành đai 3 TP.HCM, Sân bay Long Thành...): Khối Quản trị Rủi ro Hội sở rà soát toàn bộ các khoản vay có TSBĐ nằm trong hành lang quy hoạch, trích lập một khoản dự phòng bổ sung chung (Management Overlay Buffer) trừ trực tiếp vào kết quả kinh doanh của chi nhánh đó để hấp thụ trước rủi ro sụt giảm giá trị tài sản.")

# SECTION 3
add_h1(doc, "3. GIỚI HẠN BẢN CHẤT: TẠI SAO DỰ PHÒNG KHÔNG THỂ LÀ 'CÂY GẬY THẦN' DUY NHẤT?")
add_callout(doc, "PHÂN BIỆT GIỮA KẾ TOÁN DỰ PHÒNG VÀ DÒNG TIỀN THỰC TẾ: ",
            "Dự phòng chỉ là một chi phí kế toán giúp ngân hàng 'chuẩn bị tâm lý và làm sạch bảng cân đối' trước khoản lỗ. Dù ngân hàng có trích đủ 100% dự phòng (4,0 tỷ đồng) thì ngân hàng vẫn MẤT ĐỨT 4,0 TỶ ĐỒNG VỐN TỰ CÓ (Lợi nhuận lũy kế bị giảm đúng 4,0 tỷ đồng). Do đó, dự phòng không thể thay thế cho các biện pháp quản trị rủi ro thực tế nhằm bảo toàn dòng tiền mặt!",
            rgb_prefix=(0, 32, 96), bg_hex="F2F5F9", border_color="002060")

# SECTION 4
add_h1(doc, "4. HỆ THỐNG BIỆN PHÁP QUẢN TRỊ RỦI RO THỰC TẾ CỦA CÁC NHTM HIỆN NAY")
add_p(doc, "Để bảo vệ đồng vốn thực tế, các ngân hàng thương mại triển khai quy trình kiểm soát đa tầng nghiêm ngặt:")

add_h2(doc, "1. Bộ lọc thẩm định quy hoạch ngay từ đầu (Ex-ante Underwriting Filter):")
points_uw = [
    ("Quy tắc 'Cắt lộ giới định giá 0 đồng': ", "Khi nhận thế chấp nhà phố/đất nền, ngân hàng tra cứu bản đồ quy hoạch 1/2000 và 1/500 tại Phòng Tài nguyên & Môi trường. Phần diện tích nằm trong chỉ giới đường đỏ / lộ giới mở đường được định giá = 0 đồng. Ngân hàng chỉ tính toán hạn mức cho vay (LTV 50%–70%) trên phần diện tích đất phù hợp quy hoạch."),
    ("Từ chối nhận thế chấp tuyệt đối: ", "Từ chối 100% đối với các bất động sản nằm hoàn toàn trong quy hoạch công viên cây xanh, công trình công cộng, hành lang lưới điện, hoặc quy hoạch ga đường sắt.")
]
for pfx, bdy in points_uw:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"• {pfx}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_h2(doc, "2. Ràng buộc Hợp đồng tín dụng (Covenants & Event of Default):")
add_p(doc, "Trong Hợp đồng thế chấp luôn cài cắm điều khoản bảo vệ tối cao: Khi tài sản thế chấp bị Nhà nước thu hồi đất hoặc giải phóng mặt bằng, đây được coi là một 'Sự kiện vi phạm nghĩa vụ hợp đồng'. Ngân hàng kích hoạt ngay các quyền sau:")
points_cov = [
    ("Buộc bổ sung TSBĐ khác: ", "Bên vay có nghĩa vụ bổ sung TSBĐ khác (bất động sản khác, sổ tiết kiệm, cổ phiếu) có giá trị tương đương trong vòng 15–30 ngày."),
    ("Buộc trả nợ trước hạn: ", "Nếu không có TSBĐ bổ sung, bên vay phải nộp tiền mặt để trả bớt nợ gốc, hạ dư nợ về mức an toàn tương ứng với số tiền bồi thường dự kiến."),
    ("Chuyển nợ quá hạn và khởi kiện: ", "Nếu bên vay bất hợp tác, ngân hàng chấm dứt cho vay, chuyển toàn bộ dư nợ sang nợ quá hạn để tiến hành xử lý tài sản.")
]
for pfx, bdy in points_cov:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  - {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_h2(doc, "3. Cơ chế Ủy quyền & Phong tỏa trực tiếp dòng tiền bồi thường GPMB:")
points_gpmb = [
    ("Văn bản thông báo quyền ưu tiên thanh toán: ", "Ngân hàng gửi thông báo bằng văn bản kèm hợp đồng thế chấp đã đăng ký giao dịch bảo đảm đến Hội đồng Bồi thường GPMB quận/huyện và Kho bạc Nhà nước. Theo Bộ luật Dân sự, ngân hàng là bên nhận bảo đảm có quyền ưu tiên thanh toán số 1 trước khi chi trả cho chủ đất."),
    ("Tài khoản phong tỏa chuyên dụng: ", "Toàn bộ số tiền bồi thường đất và tài sản trên đất phải được chuyển khoản trực tiếp vào tài khoản phong tỏa của bên vay mở tại ngân hàng. Hệ thống tự động trích thu nợ gốc và lãi, khách hàng không được quyền rút tiền mặt."),
    ("Thế chấp quyền tài sản tái định cư: ", "Nếu khách hàng được đền bù bằng Suất đất tái định cư hoặc Căn hộ tái định cư, ngân hàng bắt buộc khách hàng ký thỏa thuận thế chấp quyền tài sản phát sinh từ hợp đồng tái định cư đó để tiếp tục bảo đảm cho phần nợ còn lại.")
]
for pfx, bdy in points_gpmb:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"• {pfx}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

# SECTION 5
add_h1(doc, "5. ĐỘT PHÁ TỪ LUẬT ĐẤT ĐAI 2024: KHOẢNG TRỐNG NÀY ĐANG ĐƯỢC THU HẸP RA SAO?")
add_p(doc, "Trước ngày 01/08/2024 (thời kỳ Luật Đất đai 2013), rủi ro này cực kỳ khốc liệt vì Nhà nước áp dụng Khung giá đất cố định 5 năm (giá đền bù thường chỉ bằng 30%–40% giá thị trường). Tuy nhiên, Luật Đất đai 2024 có hiệu lực đã mang lại 2 đột phá thể chế quan trọng giúp bảo vệ hệ thống ngân hàng:")
points_land2024 = [
    ("Bãi bỏ Khung giá đất (Điều 158, 159): ", "Bảng giá đất hiện nay được xây dựng định kỳ hàng năm và xác định theo nguyên tắc thị trường, thu hẹp khoảng cách chênh lệch giữa giá đền bù và giá thị trường thực tế."),
    ("Nguyên tắc bồi thường bảo đảm sinh kế (Điều 91): ", "Quy định phương án bồi thường, hỗ trợ, tái định cư phải bảo đảm người có đất bị thu hồi có chỗ ở, thu nhập và điều kiện sống bằng hoặc tốt hơn nơi ở cũ. Giá đất bồi thường là giá đất cụ thể được định giá sát thị trường tại thời điểm thu hồi (thường đạt 75%–85% giá giao dịch thực tế)."),
    ("Hệ quả đối với ngân hàng: ", "Khoảng chênh lệch (spread) rủi ro bị thu hẹp đáng kể. Với mức LTV khống chế 50%–60%, số tiền bồi thường GPMB theo Luật Đất đai 2024 cơ bản đã đủ để chi trả toàn bộ nợ gốc cho ngân hàng.")
]
for pfx, bdy in points_land2024:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"• {pfx}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

# SECTION 6: SPEAKER SCRIPT
add_h1(doc, "6. KỊCH BẢN THUYẾT TRÌNH & TRẢ LỜI PHẢN BIỆN MẪU (SPEAKER SCRIPT)")
add_callout(doc, "LỜI THOẠI TRẢ LỜI MẪU DÀNH CHO BẠN KHI PHẢN BIỆN TRÊN BỤC: ",
            "'Thưa Thầy và các bạn, đây là một câu hỏi nghiệp vụ cực kỳ sắc bén! Về bản chất, trích lập dự phòng chỉ là một công cụ kế toán để ghi nhận trước tổn thất chứ không tạo ra tiền mặt để bù đắp phần vốn bị hụt nếu tiền đền bù thấp hơn nợ gốc.\n\n"
            "Về mặt kỹ thuật trích lập, ngân hàng có phương án bao phủ trước bằng cách: Ngay khi có thông báo quy hoạch, ngân hàng sẽ tái định giá TSBĐ về bằng đúng giá bồi thường dự kiến (hạ giá trị khấu trừ C theo Thông tư 11) hoặc đẩy sang Stage 2 tính Lifetime ECL theo IFRS 9 với LGD tăng vọt, buộc chi nhánh phải trích lập dự phòng đầy đủ đón đầu rủi ro.\n\n"
            "Tuy nhiên, để bảo toàn vốn thực tế, ngân hàng không bao giờ chỉ dựa vào dự phòng! Các ngân hàng áp dụng quy tắc phòng ngừa ngay từ đầu: Thứ nhất, khi thẩm định chỉ định giá phần diện tích phù hợp quy hoạch, phần dính lộ giới quy hoạch định giá 0 đồng. Thứ hai, hợp đồng thế chấp quy định việc dính giải tỏa là 'Sự kiện vi phạm' buộc khách hàng phải bổ sung TSBĐ khác hoặc trả nợ trước hạn. Thứ ba, ngân hàng đăng ký quyền ưu tiên thanh toán với Hội đồng GPMB và Kho bạc để phong tỏa trực tiếp nguồn tiền bồi thường chuyển thẳng vào tài khoản thu nợ tự động của ngân hàng.\n\n"
            "Đặc biệt, từ khi Luật Đất đai 2024 có hiệu lực bỏ khung giá đất và đền bù sát giá thị trường, khoảng cách chênh lệch này đã được thu hẹp rất nhiều, giúp hạn mức LTV 50-60% của ngân hàng thực sự phát huy tác dụng bảo vệ an toàn vốn.'",
            rgb_prefix=(0, 32, 96), bg_hex="F2F5F9", border_color="002060")

# Save DOCX
target_docx = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Quan_tri_Rui_ro_Khoan_vay_Dinh_Giai_toa_Mat_bang.docx"
doc.save(target_docx)
print("SUCCESSFULLY SAVED STANDALONE DOCX:", target_docx)

# ==============================================================================
# BUILD GOOGLE-DOCS-READY HTML FILE
# ==============================================================================
html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Quản trị Rủi ro Khoản vay có TSBĐ Dính Giải tỏa Mặt bằng</title>
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
    font-size: 15pt;
    font-weight: bold;
    color: #c00000;
    margin: 12px 0 6px 0;
  }
  .doc-sub {
    font-size: 10.5pt;
    font-style: italic;
    color: #555555;
    margin-bottom: 4px;
  }
  h1 {
    font-size: 13pt;
    color: #002060;
    border-bottom: 1.5px solid #002060;
    padding-bottom: 4px;
    margin-top: 26px;
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
  .callout-bluf {
    background-color: #fdf2f2;
    border-left: 4px solid #c00000;
    padding: 12px 16px;
    margin: 14px 0;
    border-radius: 0 4px 4px 0;
    font-size: 10.5pt;
  }
  .callout-bluf strong {
    color: #c00000;
  }
  .callout-script {
    background-color: #f2f5f9;
    border-left: 4px solid #002060;
    padding: 14px 18px;
    margin: 16px 0;
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
    <div class="doc-title">BÁO CÁO PHÂN TÍCH NGHIỆP VỤ & GIẢI TRÌNH CHUYÊN SÂU:</div>
    <div style="font-size: 12.5pt; font-weight: bold; color: #002060; margin-bottom: 6px;">CƠ CHẾ DỰ PHÒNG & QUẢN TRỊ RỦI RO ĐỐI VỚI KHOẢN VAY DÍNH GIẢI TỎA MẶT BẰNG</div>
    <div class="doc-sub">Chuyên đề: Giải quyết bài toán chênh lệch giữa giá thị trường và giá bồi thường giải phóng mặt bằng</div>
    <div class="doc-sub">Người thực hiện: Nhóm 2 — K34_3_NH8 | Giảng viên hướng dẫn: TS. Khúc Thế Anh</div>
  </div>

  <div class="callout-bluf">
    <strong>TỔNG LUẬN ĐIỀU HÀNH (BOTTOM LINE UP FRONT - BLUF):</strong><br>
    <strong>1. Bản chất tài chính:</strong> Dự phòng chỉ là bút toán kế toán ghi nhận trước tổn thất (Loss Recognition), <em>KHÔNG THỂ sinh ra dòng tiền bù đắp khoản tiền bị mất nếu tiền đền bù thấp hơn nợ gốc</em>.<br>
    <strong>2. Về mặt kỹ thuật trích lập:</strong> Ngân hàng CÓ phương án tính toán để bao phủ trước rủi ro bằng cách <em>TÁI ĐỊNH GIÁ TSBĐ VỀ GIÁ BỒI THƯỜNG DỰ KIẾN</em> (hạ giá trị khấu trừ C để trích đủ dự phòng cụ thể theo Thông tư 11) hoặc <em>KÍCH HOẠT STAGE 2 THEO IFRS 9</em> với LGD tăng vọt.<br>
    <strong>3. Về mặt bảo toàn vốn thực tế:</strong> Ngân hàng BẮT BUỘC phải dùng công cụ quản trị rủi ro ngay từ đầu (Cắt lộ giới định giá 0đ, Điều khoản Event of Default buộc bổ sung TSBĐ, và Phong tỏa tài khoản tiền đền bù từ Ban GPMB).
  </div>

  <h1>1. NGHỊCH LÝ SỐ HỌC: TẠI SAO LTV 50%–70% VẪN 'CHÁY TÀI KHOẢN' KHI DÍNH GIẢI TỎA?</h1>
  <p>Trong thực tiễn cấp tín dụng, mức khống chế tỷ lệ cho vay trên định giá (LTV) từ 50% đến 70% thường được xem là bộ đệm an toàn. Tuy nhiên, khi bất động sản bị Nhà nước thu hồi đất để phục vụ dự án công cộng, bộ đệm này hoàn toàn bị xuyên thủng do sự chênh lệch rất lớn giữa giá thị trường giao dịch tự do và giá bồi thường GPMB:</p>

  <table>
    <thead>
      <tr>
        <th style="width:38%;">Chỉ tiêu tài chính / Thẩm định</th>
        <th style="width:20%; text-align:center;">Giá trị ghi nhận</th>
        <th style="width:42%;">Bản chất rủi ro & Cơ chế phát sinh</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1. Giá trị thị trường thẩm định ban đầu (V_market)</td>
        <td style="text-align:center;">10,0 tỷ đồng</td>
        <td>Định giá theo phương pháp so sánh thị trường tại thời điểm thuận lợi.</td>
      </tr>
      <tr>
        <td>2. Tỷ lệ cho vay trên định giá (LTV 70%)</td>
        <td style="text-align:center;">70%</td>
        <td>Ngân hàng giả định có đệm an toàn vốn 30% (3,0 tỷ đồng).</td>
      </tr>
      <tr>
        <td>3. Dư nợ gốc giải ngân ban đầu (L_0)</td>
        <td style="text-align:center;">7,0 tỷ đồng</td>
        <td>Khoản vay thế chấp bằng quyền sử dụng đất và nhà ở.</td>
      </tr>
      <tr>
        <td>4. Dư nợ gốc + Lãi dồn tích sau 2 năm quá hạn (A)</td>
        <td style="text-align:center;">8,5 tỷ đồng</td>
        <td>Khách hàng gặp khó khăn, lãi mẹ đẻ lãi con, chuyển thành nợ xấu.</td>
      </tr>
      <tr>
        <td>5. Giá bồi thường GPMB được phê duyệt (V_GPMB)</td>
        <td style="text-align:center;">4,5 tỷ đồng</td>
        <td>Áp theo bảng giá đất & hệ số bồi thường (chỉ bằng 45% giá thị trường).</td>
      </tr>
      <tr style="background-color: #fdf2f2; font-weight: bold;">
        <td style="color: #c00000;">6. TỔN THẤT THỰC TẾ KHÔNG THỂ THU HỒI (LOSS)</td>
        <td style="text-align:center; color: #c00000;">-4,0 tỷ đồng</td>
        <td style="color: #c00000;">8,5 tỷ - 4,5 tỷ = 4,0 tỷ đồng (Mất trắng 47% tổng dư nợ và 57% nợ gốc!).</td>
      </tr>
    </tbody>
  </table>

  <h2>Lỗ hổng của mô hình trích lập dự phòng Thông tư 11 hiện hành:</h2>
  <p>• <strong>Công thức dự phòng cụ thể:</strong> R = max(0, A - C) × r, trong đó giá trị khấu trừ C = V_định_giá × 50% (đối với BĐS).</p>
  <p>• <strong>Hiện tượng 'bị mù' trước rủi ro quy hoạch:</strong> Nếu ngân hàng không kịp thời cập nhật thông tin quy hoạch và vẫn giữ nguyên giá định giá cũ V = 10 tỷ đồng trên hệ thống, giá trị khấu trừ C = 5 tỷ đồng. Nếu khoản nợ ở nhóm 1 hoặc nhóm 2 (trích 5% trên phần chênh lệch), ngân hàng chỉ trích vài chục triệu đồng dự phòng chung (0,75%).</p>
  <p>• <strong>Hậu quả cú sốc vách đá (Cliff Effect):</strong> Ngân hàng duy trì trạng thái 'an toàn ảo' cho tới khi có quyết định thu hồi đất và phương án bồi thường 4,5 tỷ đồng được công bố. Khoản nợ rơi tự do xuống nhóm 5, ngân hàng phải ghi nhận chi phí dự phòng bổ sung đột ngột 4,0 tỷ đồng trong một quý, xóa sạch lợi nhuận chi nhánh.</p>

  <h1>2. PHƯƠNG ÁN KỸ THUẬT TRÍCH LẬP DỰ PHÒNG NÀO CÓ THỂ 'COVER' ĐƯỢC RỦI RO NÀY?</h1>
  <p>Để phản ánh trung thực rủi ro này lên báo cáo tài chính trước khi việc bồi thường diễn ra, các ngân hàng áp dụng 3 phương án kỹ thuật sau:</p>

  <h2>Phương án 1: Tái định giá cưỡng bức theo 'Giá bồi thường dự kiến' (Chuẩn Thông tư 11 & Thông tư 31)</h2>
  <p>Theo Điều 12 Thông tư 11/2021/TT-NHNN, TCTD có trách nhiệm định giá lại TSBĐ khi có biến động bất thường. Ngay khi khu vực có Thông báo thu hồi đất hoặc văn bản phê duyệt quy hoạch dự án:</p>
  <p>- <strong>Hạ giá định giá về giá bồi thường:</strong> Định giá viên không dùng giá thị trường nữa, mà chuyển sang dùng Giá bồi thường dự kiến: V_định_giá_mới = V_GPMB = 4,5 tỷ đồng.</p>
  <p>- <strong>Ép giá trị khấu trừ C sụt giảm:</strong> Giá trị khấu trừ hợp lệ sau chiết khấu 50% chỉ còn: C = 4,5 tỷ × 50% = 2,25 tỷ đồng.</p>
  <p>- <strong>Kích hoạt trích lập Dự phòng cụ thể ngay lập tức:</strong> Phần dư nợ không có bảo đảm vọt lên: (A - C) = 8,5 - 2,25 = 6,25 tỷ đồng. Khi nợ chuyển nhóm 3 (trích 20%), nhóm 4 (trích 50%), hoặc nhóm 5 (trích 100%), ngân hàng trích lập dự phòng đầy đủ theo từng kỳ, chia nhỏ cú sốc chi phí ra nhiều quý thay vì bị động chịu trận ở thời điểm cuối.</p>

  <h2>Phương án 2: Mô phỏng theo Chuẩn mực Quốc tế IFRS 9 ECL (Tổn thất trọn vòng đời)</h2>
  <p>IFRS 9 xóa bỏ hoàn toàn mô hình tổn thất đã phát sinh (Incurred Loss):</p>
  <p>- <strong>Kích hoạt SICR chuyển sang Stage 2:</strong> Sự kiện tài sản thế chấp bị quy hoạch giải tỏa được xếp vào diện Gia tăng rủi ro tín dụng đáng kể (Significant Increase in Credit Risk - SICR), đẩy khoản vay từ Stage 1 sang Stage 2.</p>
  <p>- <strong>Tính toán Lifetime ECL:</strong> Bắt buộc áp dụng công thức: ECL = EAD × PD_lifetime × LGD_adjusted.</p>
  <p>- <strong>Điều chỉnh trực tiếp tham số LGD (Loss Given Default):</strong> LGD không áp dụng tỷ lệ cố định, mà tính toán dựa trên dòng tiền thu hồi kỳ vọng: LGD_adjusted = 1 - (Tiền bồi thường GPMB / Dư nợ) = 1 - (4,5 / 8,5) ≈ 47%. Nhân với PD trọn đời của Stage 2 (từ 20%–30%), số dự phòng phải trích lập tự động tăng vọt gấp 5 đến 8 lần, tạo ra bộ đệm vốn bao phủ toàn diện trước khi sự việc diễn ra.</p>

  <h2>Phương án 3: Trích lập đệm dự phòng danh mục (Management Overlay Buffer)</h2>
  <p>Đối với các chi nhánh nằm trên địa bàn có các đại dự án hạ tầng đi qua (Vành đai 4 Hà Nội, Vành đai 3 TP.HCM, Sân bay Long Thành...): Khối Quản trị Rủi ro Hội sở rà soát toàn bộ các khoản vay có TSBĐ nằm trong hành lang quy hoạch, trích lập một khoản dự phòng bổ sung chung (Management Overlay Buffer) trừ trực tiếp vào kết quả kinh doanh của chi nhánh đó để hấp thụ trước rủi ro sụt giảm giá trị tài sản.</p>

  <h1>3. GIỚI HẠN BẢN CHẤT: TẠI SAO DỰ PHÒNG KHÔNG THỂ LÀ 'CÂY GẬY THẦN' DUY NHẤT?</h1>
  <div class="callout-script">
    <strong>PHÂN BIỆT GIỮA KẾ TOÁN DỰ PHÒNG VÀ DÒNG TIỀN THỰC TẾ:</strong><br>
    Dự phòng chỉ là một chi phí kế toán giúp ngân hàng 'chuẩn bị tâm lý và làm sạch bảng cân đối' trước khoản lỗ. Dù ngân hàng có trích đủ 100% dự phòng (4,0 tỷ đồng) thì ngân hàng vẫn MẤT ĐỨT 4,0 TỶ ĐỒNG VỐN TỰ CÓ (Lợi nhuận lũy kế bị giảm đúng 4,0 tỷ đồng). Do đó, dự phòng không thể thay thế cho các biện pháp quản trị rủi ro thực tế nhằm bảo toàn dòng tiền mặt!
  </div>

  <h1>4. HỆ THỐNG BIỆN PHÁP QUẢN TRỊ RỦI RO THỰC TẾ CỦA CÁC NHTM HIỆN NAY</h1>
  <p>Để bảo vệ đồng vốn thực tế, các ngân hàng thương mại triển khai quy trình kiểm soát đa tầng nghiêm ngặt:</p>

  <h2>1. Bộ lọc thẩm định quy hoạch ngay từ đầu (Ex-ante Underwriting Filter):</h2>
  <p>• <strong>Quy tắc 'Cắt lộ giới định giá 0 đồng':</strong> Khi nhận thế chấp nhà phố/đất nền, ngân hàng tra cứu bản đồ quy hoạch 1/2000 và 1/500 tại Phòng Tài nguyên & Môi trường. Phần diện tích nằm trong chỉ giới đường đỏ / lộ giới mở đường được định giá = 0 đồng. Ngân hàng chỉ tính toán hạn mức cho vay (LTV 50%–70%) trên phần diện tích đất phù hợp quy hoạch.</p>
  <p>• <strong>Từ chối nhận thế chấp tuyệt đối:</strong> Từ chối 100% đối với các bất động sản nằm hoàn toàn trong quy hoạch công viên cây xanh, công trình công cộng, hành lang lưới điện, hoặc quy hoạch ga đường sắt.</p>

  <h2>2. Ràng buộc Hợp đồng tín dụng (Covenants & Event of Default):</h2>
  <p>Trong Hợp đồng thế chấp luôn cài cắm điều khoản bảo vệ tối cao: Khi tài sản thế chấp bị Nhà nước thu hồi đất hoặc giải phóng mặt bằng, đây được coi là một 'Sự kiện vi phạm nghĩa vụ hợp đồng'. Ngân hàng kích hoạt ngay các quyền sau:</p>
  <p>- <strong>Buộc bổ sung TSBĐ khác:</strong> Bên vay có nghĩa vụ bổ sung TSBĐ khác (bất động sản khác, sổ tiết kiệm, cổ phiếu) có giá trị tương đương trong vòng 15–30 ngày.</p>
  <p>- <strong>Buộc trả nợ trước hạn:</strong> Nếu không có TSBĐ bổ sung, bên vay phải nộp tiền mặt để trả bớt nợ gốc, hạ dư nợ về mức an toàn tương ứng với số tiền bồi thường dự kiến.</p>
  <p>- <strong>Chuyển nợ quá hạn và khởi kiện:</strong> Nếu bên vay bất hợp tác, ngân hàng chấm dứt cho vay, chuyển toàn bộ dư nợ sang nợ quá hạn để tiến hành xử lý tài sản.</p>

  <h2>3. Cơ chế Ủy quyền & Phong tỏa trực tiếp dòng tiền bồi thường GPMB:</h2>
  <p>• <strong>Văn bản thông báo quyền ưu tiên thanh toán:</strong> Ngân hàng gửi thông báo bằng văn bản kèm hợp đồng thế chấp đã đăng ký giao dịch bảo đảm đến Hội đồng Bồi thường GPMB quận/huyện và Kho bạc Nhà nước. Theo Bộ luật Dân sự, ngân hàng là bên nhận bảo đảm có quyền ưu tiên thanh toán số 1 trước khi chi trả cho chủ đất.</p>
  <p>• <strong>Tài khoản phong tỏa chuyên dụng:</strong> Toàn bộ số tiền bồi thường đất và tài sản trên đất phải được chuyển khoản trực tiếp vào tài khoản phong tỏa của bên vay mở tại ngân hàng. Hệ thống tự động trích thu nợ gốc và lãi, khách hàng không được quyền rút tiền mặt.</p>
  <p>• <strong>Thế chấp quyền tài sản tái định cư:</strong> Nếu khách hàng được đền bù bằng Suất đất tái định cư hoặc Căn hộ tái định cư, ngân hàng bắt buộc khách hàng ký thỏa thuận thế chấp quyền tài sản phát sinh từ hợp đồng tái định cư đó để tiếp tục bảo đảm cho phần nợ còn lại.</p>

  <h1>5. ĐỘT PHÁ TỪ LUẬT ĐẤT ĐAI 2024: KHOẢNG TRỐNG NÀY ĐANG ĐƯỢC THU HẸP RA SAO?</h1>
  <p>Trước ngày 01/08/2024 (thời kỳ Luật Đất đai 2013), rủi ro này cực kỳ khốc liệt vì Nhà nước áp dụng Khung giá đất cố định 5 năm (giá đền bù thường chỉ bằng 30%–40% giá thị trường). Tuy nhiên, Luật Đất đai 2024 có hiệu lực đã mang lại 2 đột phá thể chế quan trọng giúp bảo vệ hệ thống ngân hàng:</p>
  <p>• <strong>Bãi bỏ Khung giá đất (Điều 158, 159):</strong> Bảng giá đất hiện nay được xây dựng định kỳ hàng năm và xác định theo nguyên tắc thị trường, thu hẹp khoảng cách chênh lệch giữa giá đền bù và giá thị trường thực tế.</p>
  <p>• <strong>Nguyên tắc bồi thường bảo đảm sinh kế (Điều 91):</strong> Quy định phương án bồi thường, hỗ trợ, tái định cư phải bảo đảm người có đất bị thu hồi có chỗ ở, thu nhập và điều kiện sống bằng hoặc tốt hơn nơi ở cũ. Giá đất bồi thường là giá đất cụ thể được định giá sát thị trường tại thời điểm thu hồi (thường đạt 75%–85% giá giao dịch thực tế).</p>
  <p>• <strong>Hệ quả đối với ngân hàng:</strong> Khoảng chênh lệch (spread) rủi ro bị thu hẹp đáng kể. Với mức LTV khống chế 50%–60%, số tiền bồi thường GPMB theo Luật Đất đai 2024 cơ bản đã đủ để chi trả toàn bộ nợ gốc cho ngân hàng.</p>

  <h1>6. KỊCH BẢN THUYẾT TRÌNH & TRẢ LỜI PHẢN BIỆN MẪU (SPEAKER SCRIPT)</h1>
  <div class="callout-script">
    <strong>LỜI THOẠI TRẢ LỜI MẪU DÀNH CHO BẠN KHI PHẢN BIỆN TRÊN BỤC:</strong><br><br>
    'Thưa Thầy và các bạn, đây là một câu hỏi nghiệp vụ cực kỳ sắc bén! Về bản chất, trích lập dự phòng chỉ là một công cụ kế toán để ghi nhận trước tổn thất chứ không tạo ra tiền mặt để bù đắp phần vốn bị hụt nếu tiền đền bù thấp hơn nợ gốc.<br><br>
    Về mặt kỹ thuật trích lập, ngân hàng có phương án bao phủ trước bằng cách: Ngay khi có thông báo quy hoạch, ngân hàng sẽ tái định giá TSBĐ về bằng đúng giá bồi thường dự kiến (hạ giá trị khấu trừ C theo Thông tư 11) hoặc đẩy sang Stage 2 tính Lifetime ECL theo IFRS 9 với LGD tăng vọt, buộc chi nhánh phải trích lập dự phòng đầy đủ đón đầu rủi ro.<br><br>
    Tuy nhiên, để bảo toàn vốn thực tế, ngân hàng không bao giờ chỉ dựa vào dự phòng! Các ngân hàng áp dụng quy tắc phòng ngừa ngay từ đầu: Thứ nhất, khi thẩm định chỉ định giá phần diện tích phù hợp quy hoạch, phần dính lộ giới quy hoạch định giá 0 đồng. Thứ hai, hợp đồng thế chấp quy định việc dính giải tỏa là 'Sự kiện vi phạm' buộc khách hàng phải bổ sung TSBĐ khác hoặc trả nợ trước hạn. Thứ ba, ngân hàng đăng ký quyền ưu tiên thanh toán với Hội đồng GPMB và Kho bạc để phong tỏa trực tiếp nguồn tiền bồi thường chuyển thẳng vào tài khoản thu nợ tự động của ngân hàng.<br><br>
    Đặc biệt, từ khi Luật Đất đai 2024 có hiệu lực bỏ khung giá đất và đền bù sát giá thị trường, khoảng cách chênh lệch này đã được thu hẹp rất nhiều, giúp hạn mức LTV 50-60% của ngân hàng thực sự phát huy tác dụng bảo vệ an toàn vốn.'
  </div>
</div>

</body>
</html>
"""

target_html = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Quan_tri_Rui_ro_Khoan_vay_Dinh_Giai_toa_Mat_bang.html"
with open(target_html, "w", encoding="utf-8") as f:
    f.write(html_content)
print("SUCCESSFULLY SAVED STANDALONE HTML:", target_html)

