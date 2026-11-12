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

def add_image_figure(doc, img_path, caption_title, source_text):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(8)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=Inches(6.4))
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(2)
    p_cap.paragraph_format.keep_with_next = True
    r_cap = p_cap.add_run(caption_title)
    style_run(r_cap, font_name="Times New Roman", size_pt=9.5, bold=True, color_rgb=(0, 32, 96))
    
    p_src = doc.add_paragraph()
    p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_src.paragraph_format.space_before = Pt(0)
    p_src.paragraph_format.space_after = Pt(8)
    r_src = p_src.add_run(source_text)
    style_run(r_src, font_name="Times New Roman", size_pt=8.5, italic=True, color_rgb=(100, 100, 100))

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
# ASSEMBLE DOCUMENT
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
r_head = p_head.add_run("Học phần Quản trị Rủi ro — Chuyên đề: Khoản mục Dự phòng cho Rủi ro Quy hoạch Thần tốc")
style_run(r_head, size_pt=8.5, italic=True, color_rgb=(120, 120, 120))

# Configure Footer
footer = section.footer
p_foot = footer.paragraphs[0]
p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_foot = p_foot.add_run("Tài liệu Phân tích Chuyên sâu — Nhóm 2 Cao học Khóa 34 NEU")
style_run(r_foot, size_pt=8.5, italic=True, color_rgb=(120, 120, 120))

# Title Block
p_top = add_p(doc, "TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN (NEU) — VIỆN NGÂN HÀNG - TÀI CHÍNH\nCHƯƠNG TRÌNH CAO HỌC KHÓA 34 (LỚP K34_3_NH8) — HỌC PHẦN: QUẢN TRỊ RỦI RO", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=6)
for r in p_top.runs:
    style_run(r, size_pt=9.5, bold=True, color_rgb=(0, 32, 96))

p_title = add_p(doc, "BÁO CÁO NGHIÊN CỨU CHUYÊN ĐỀ:\nCƠ CHẾ KHOẢN MỤC DỰ PHÒNG & MÔ HÌNH QUẢN TRỊ KHI TÀI SẢN BẢO ĐẢM BỊ 'ĐÁNH ÚP' BỞI QUY HOẠCH HẠ TẦNG THẦN TỐC", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=4)
for r in p_title.runs:
    style_run(r, size_pt=13, bold=True, color_rgb=(192, 0, 0))

p_sub = add_p(doc, "Bóc tách câu hỏi: Khoản mục nào trong hệ thống kế toán - quản trị ngân hàng chịu trách nhiệm hấp thụ rủi ro thu hồi đất khẩn cấp không có dữ liệu quy hoạch trước?\nNhóm thực hiện: Nhóm 2 | Giảng viên hướng dẫn: TS. Khúc Thế Anh", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=12)
for r in p_sub.runs:
    style_run(r, size_pt=9.5, italic=True, color_rgb=(80, 80, 80))

# BLUF Callout
add_callout(doc, "TỔNG LUẬN ĐIỀU HÀNH (BLUF): ",
            "1. Xác nhận thực tiễn: Thông tin người nêu đưa ra là HOÀN TOÀN CHÍNH XÁC. Dưới phương châm điều hành thần tốc của Tổng Bí thư Tô Lâm ('Hạ tầng là đột phá của đột phá', 'Không bàn lùi, chỉ bàn làm'), các dự án hạ tầng chiến lược được phê duyệt theo cơ chế đặc thù, khiến cả người dân lẫn ngân hàng đều bị 'đánh úp' do dữ liệu quy hoạch trước đó hoàn toàn không hiển thị.\n"
            "2. Khoản mục chịu trách nhiệm: Không có khoản mục mang tên riêng 'Dự phòng quy hoạch đột xuất', nhưng hệ thống ngân hàng thiết kế sẵn 3 TẦNG KHOẢN MỤC ĐÍCH DANH để hấp thụ rủi ro này:\n"
            "   • Tầng 1 (Chi phí P&L): DỰ PHÒNG CHUNG (0,75% dư nợ Nhóm 1–4 theo Thông tư 11/2021) — Quỹ luật định cho các tổn thất 'chưa xác định được'.\n"
            "   • Tầng 2 (Chuẩn mực quốc tế): MANAGEMENT OVERLAY (IFRS 9 ECL) — Dự phòng bổ sung theo phán đoán chính trị của Ban Điều hành.\n"
            "   • Tầng 3 (Vốn chủ sở hữu): QUÝ DỰ PHÒNG TÀI CHÍNH (10% LNST) & ĐỆM VỐN KINH TẾ (CAR 10–11% theo Basel II Trụ cột 2).",
            rgb_prefix=(192, 0, 0), bg_hex="FDF2F2", border_color="C00000")

# SECTION 1
add_h1(doc, "1. BỐI CẢNH THỂ CHẾ: HIỆN TƯỢNG 'QUY HOẠCH THẦN TỐC / QUYẾT LÀ LÀM LUÔN'")
add_p(doc, "Trong các lý thuyết kinh tế tài chính và quản trị rủi ro truyền thống, các mô hình chấm điểm tín dụng và thẩm định tài sản bảo đảm (TSBĐ) đều dựa trên giả định môi trường quy hoạch tĩnh: Quy hoạch sử dụng đất và quy hoạch phát triển giao thông được lập theo chu kỳ 5–10 năm, công khai qua bản đồ phân khu 1/2000 và 1/500 tại các cơ quan chức năng.")
add_p(doc, "Tuy nhiên, bối cảnh quản trị quốc gia hiện nay tại Việt Nam đã có sự chuyển dịch mang tính đột phá:")
points_s1 = [
    ("Thông điệp hành động của Tổng Bí thư Tô Lâm & Chính phủ: ", "'Tháo gỡ điểm nghẽn thể chế là đột phá của đột phá', 'Hạ tầng đi trước mở đường', 'Chỉ bàn làm, không bàn lùi'. Các đại dự án chiến lược quốc gia (Đường sắt tốc độ cao Bắc - Nam 67 tỷ USD, các tuyến đường sắt kết nối biên giới phía Bắc, Vành đai 4 Hà Nội, Vành đai 3 TP.HCM, sân bay, cảng biển) được chuyển sang trạng thái khẩn cấp."),
    ("Cơ chế đặc thù rút ngắn quy trình lập quy hoạch: ", "Quốc hội và Chính phủ ban hành hàng loạt nghị quyết thí điểm cơ chế đặc thù: Cho phép điều chỉnh cục bộ quy hoạch không cần chờ điều chỉnh quy hoạch tổng thể; tách riêng công tác bồi thường, tái định cư thành dự án độc lập làm trước thần tốc; rút ngắn thời gian chuẩn bị từ vài năm xuống vài tuần."),
    ("Thực tế 'bị đánh úp': ", "Khi ngân hàng thẩm định cho vay vào năm 2022–2023, căn nhà của khách hàng hoàn toàn nằm trong khu dân cư hiện hữu ổn định, không có bất kỳ thông tin quy hoạch nào. Đến năm 2025–2026, hướng tuyến đại dự án được phê duyệt khẩn cấp đi xuyên qua khu đất. Ngân hàng và người dân bị động 100% trước quyết định này.")
]
for pfx, bdy in points_s1:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"• {pfx}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

# SECTION 2
add_h1(doc, "2. CƠ CHẾ 3 TẦNG KHOẢN MỤC DỰ PHÒNG HẤP THỤ RỦI RO QUY HOẠCH ĐỘT XUẤT", page_break_before=True)
add_p(doc, "Để bảo vệ hệ thống ngân hàng không bị sụp đổ trước các cú sốc sự kiện (Event Risk / Tail Risk), hệ thống kế toán và chuẩn mực an toàn vốn đã phân bổ rủi ro này vào 3 tầng khoản mục cụ thể:")

# INSERT DIAGRAM 1
img1_path = r'C:\Users\Admin\.gemini\antigravity\scratch\diagrams\So_do_1_Ba_tang_khoan_muc_du_phong.png'
add_image_figure(doc, img1_path, 
                 "Sơ đồ 1. Mô hình 3 tầng khoản mục dự phòng hấp thụ rủi ro quy hoạch giải tỏa đột xuất", 
                 "Nguồn: Thiết kế và hệ thống hóa bởi Nhóm 2 dựa trên Thông tư 11/2021/TT-NHNN, IFRS 9 và Khung ICAAP Basel II.")

add_h2(doc, "Tầng 1: Khoản mục DỰ PHÒNG CHUNG (0,75% Dư nợ) — Khoản mục Chi phí P&L")
points_t1 = [
    ("Căn cứ pháp lý: ", "Điều 7 Thông tư 11/2021/TT-NHNN và Thông tư 31/2024/TT-NHNN quy định rõ: 'Dự phòng chung là số tiền được trích lập để dự phòng cho những tổn thất có thể xảy ra nhưng chưa xác định được khi trích lập dự phòng cụ thể'."),
    ("Quy mô vốn: ", "Bắt buộc trích lập 0,75% trên tổng dư nợ từ Nhóm 1 đến Nhóm 4. Tại các ngân hàng lớn như Agribank (dư nợ 1,97 triệu tỷ) hay MB (dư nợ 1,08 triệu tỷ), khoản mục Dự phòng chung nằm sẵn trên bảng cân đối kế toán từ 8.000 đến 15.000 tỷ đồng."),
    ("Vai trò thực tế: ", "Đây chính là 'quỹ bảo hiểm rủi ro bất khả kháng'. Vì ngân hàng không thể biết trước nhà nào sẽ bị giải tỏa khẩn cấp, số tiền 0,75% thu từ toàn bộ danh mục cho vay được gộp lại thành một tấm đệm khổng lồ để sẵn sàng bù đắp cho phần giá trị tài sản bị hụt khi biến cố xảy ra.")
]
for pfx, bdy in points_t1:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  - {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_h2(doc, "Tầng 2: Khoản mục MANAGEMENT OVERLAY / POST-MODEL ADJUSTMENTS (PMA) — Chuẩn mực IFRS 9")
points_t2 = [
    ("Bản chất: ", "Các thuật toán thống kê (Machine Learning / Logistic Regression) để tính PD và LGD trong IFRS 9 hoàn toàn bị 'mù' trước các quyết sách chính trị hoặc dự án thần tốc vì dữ liệu quá khứ không chứa các biến cố này."),
    ("Cơ chế hạch toán: ", "IFRS 9 cho phép Ban Điều hành ngân hàng thiết lập khoản mục 'Management Overlay' — một khoản dự phòng bổ sung dựa trên phán đoán chuyên gia, hạch toán thẳng vào Báo cáo Kết quả Kinh doanh (P&L)."),
    ("Ứng dụng khi bị 'đánh úp': ", "Khi Chính phủ công bố một hành lang hạ tầng mới, Khối Quản trị Rủi ro ước tính ngay tổng giá trị tài sản bị ảnh hưởng và trích bổ sung ngay một khoản mục dự phòng riêng (ví dụ 500 – 1.000 tỷ đồng) vào chi phí của kỳ đó, phân bổ cho Stage 2 để bao phủ tổn thất trước khi phương án bồi thường được duyệt.")
]
for pfx, bdy in points_t2:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  - {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

add_h2(doc, "Tầng 3: Khoản mục QUỸ DỰ PHÒNG TÀI CHÍNH & ĐỆM VỐN KINH TẾ (CAR) — Vốn Chủ Sở Hữu")
points_t3 = [
    ("Quỹ dự phòng tài chính (Luật Các TCTD & Nghị định 93/2017): ", "Hàng năm ngân hàng bắt buộc trích 10% Lợi nhuận sau thuế vào Quỹ dự phòng tài chính (tối đa bằng 25% vốn điều lệ). Mục đích luật định: Bù đắp phần tổn thất tài sản kinh doanh vượt quá khả năng của quỹ dự phòng trích trong chi phí hoạt động."),
    ("Đệm Vốn kinh tế (Economic Capital for Event Risk - Trụ cột 2 Basel II/III ICAAP): ", "Agribank và MB đều duy trì hệ số an toàn vốn CAR từ 10%–11%, cao hơn mức sàn 8,0%. Khoảng dôi dư 2%–3% (hàng chục nghìn tỷ đồng) chính là đệm vốn tự có để đảm bảo khả năng thanh toán khi xảy ra các cú sốc sự kiện bất khả kháng.")
]
for pfx, bdy in points_t3:
    p = add_p(doc, space_before=1.5, space_after=2)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"  - {pfx}")
    style_run(r1, bold=True, color_rgb=(15, 76, 129))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

# SECTION 3
add_h1(doc, "3. QUY TRÌNH 4 BƯỚC ỨNG PHÓ KẾ TOÁN & PHÁP LÝ KHI BỊ 'ĐÁNH ÚP' QUY HOẠCH", page_break_before=True)
add_p(doc, "Khi một dự án thần tốc bất ngờ được phê duyệt và công bố hướng tuyến đi qua tài sản thế chấp, ngân hàng lập tức kích hoạt quy trình tác nghiệp 4 bước khép kín:")

# INSERT DIAGRAM 2
img2_path = r'C:\Users\Admin\.gemini\antigravity\scratch\diagrams\So_do_2_Quy_trinh_ung_pho_ngan_hang.png'
add_image_figure(doc, img2_path, 
                 "Sơ đồ 2. Quy trình 4 bước ứng phó kế toán & pháp lý của Ngân hàng khi bị 'đánh úp' quy hoạch", 
                 "Nguồn: Xây dựng bởi Nhóm 2 từ quy trình quản trị rủi ro tín dụng và thu hồi nợ thực tế tại các NHTM Việt Nam.")

steps_text = [
    ("Bước 1: Cách ly & Giám sát đặc biệt (Watchlist): ", 
     "Ngay khi có thông tin hướng tuyến, hệ thống Core Banking quét toàn bộ các khoản vay có tọa độ/địa chỉ nằm trong bán kính giải tỏa. Chuyển toàn bộ các khoản vay này vào danh sách Giám sát đặc biệt (Watchlist), dừng ngay việc cấp thêm hạn mức tín dụng."),
     
    ("Bước 2: Tái định giá theo giá bồi thường dự kiến & Trích lập Dự phòng cụ thể: ", 
     "Định giá viên không dùng giá thị trường nữa mà áp dụng giá bồi thường dự kiến của dự án (V_GPMB). Giá trị khấu trừ C bị ép giảm xuống 50% của giá đền bù -> Phần chênh lệch thiếu hụt (A - C) tăng vọt -> Kích hoạt trích lập Dự phòng cụ thể bổ sung, dàn trải chi phí vào các quý gần nhất."),
     
    ("Bước 3: Ràng buộc hợp đồng (Covenants & Event of Default): ", 
     "Gửi văn bản thông báo khách hàng: Việc tài sản dính thu hồi đất là vi phạm cam kết duy trì TSBĐ. Yêu cầu khách hàng trong 15–30 ngày phải: (1) Nộp TSBĐ bổ sung (sổ tiết kiệm, BĐS khác); hoặc (2) Nộp tiền mặt trả bớt nợ gốc để đưa LTV về mức an toàn."),
     
    ("Bước 4: Thu hồi tiền bồi thường trực tiếp & Xóa nợ nội bảng (Write-off): ", 
     "Ngân hàng gửi văn bản đăng ký quyền ưu tiên thanh toán đến Ban Bồi thường GPMB và Kho bạc Nhà nước. Toàn bộ tiền đền bù chuyển thẳng vào tài khoản phong tỏa để cấn trừ nợ. Nếu tiền đền bù không đủ nợ gốc, ngân hàng dùng Quỹ dự phòng rủi ro đã trích lập để Xóa nợ nội bảng (Write-off), chuyển nợ ra ngoại bảng để tiếp tục truy đòi các nguồn tài sản khác của người vay.")
]
for pfx, bdy in steps_text:
    p = add_p(doc, space_before=2, space_after=3)
    p.paragraph_format.left_indent = Inches(0.15)
    r1 = p.add_run(f"• {pfx}")
    style_run(r1, bold=True, color_rgb=(0, 32, 96))
    r2 = p.add_run(bdy)
    style_run(r2, bold=False)

# SECTION 4
add_h1(doc, "4. MA TRẬN ĐỐI CHIẾU 3 CẤP ĐỘ PHÒNG VỆ CỦA NGÂN HÀNG", page_break_before=True)

headers_mat = ["Cấp độ phòng vệ", "Khoản mục trích lập / Cơ chế", "Nguồn trích lập", "Mục tiêu ứng phó rủi ro quy hoạch"]
rows_mat = [
    [
        "Tầng 1: Chi phí hoạt động\n(Thông tư 11/2021/TT-NHNN)",
        "DỰ PHÒNG CHUNG\n(Tỷ lệ 0,75% dư nợ Nhóm 1–4)",
        "Chi phí hoạt động kinh doanh (P&L)",
        "Tạo tấm đệm thanh khoản thường trực để bù đắp các khoản tổn thất bất ngờ, chưa xác định được nguyên nhân tại thời điểm cho vay."
    ],
    [
        "Tầng 2: Chuẩn mực Quốc tế\n(Chuẩn mực IFRS 9 ECL)",
        "MANAGEMENT OVERLAY\n(Post-Model Adjustments - PMA)",
        "Chi phí dự phòng bổ sung trên P&L",
        "Bù đắp điểm mù của mô hình thống kê; Ban Điều hành chủ động trích lập dự phòng đón đầu theo phán đoán chính sách và hướng tuyến dự án."
    ],
    [
        "Tầng 3: Vốn chủ sở hữu\n(Luật TCTD & Basel II/III)",
        "QUỸ DỰ PHÒNG TÀI CHÍNH (10% LNST)\n& ĐỆM VỐN KINH TẾ (CAR 10–11%)",
        "Lợi nhuận sau thuế & Vốn tự có (Tier 1 & Tier 2)",
        "Cứu cánh cuối cùng: Hấp thụ các khoản lỗ thực tế vượt quá khả năng của chi phí dự phòng, bảo đảm an toàn hệ thống và không vi phạm CAR."
    ]
]
table_mat = doc.add_table(rows=len(rows_mat) + 1, cols=4)
col_widths_mat = [Inches(1.6), Inches(1.8), Inches(1.4), Inches(1.87)]
col_align_mat = [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
for c_idx, h in enumerate(headers_mat):
    table_mat.rows[0].cells[c_idx].paragraphs[0].text = h
for r_idx, row in enumerate(rows_mat):
    for c_idx, val in enumerate(row):
        table_mat.rows[r_idx + 1].cells[c_idx].paragraphs[0].text = val
format_table(table_mat, col_widths_mat, col_align_mat)

# SECTION 5: SPEAKER SCRIPT
add_h1(doc, "5. KỊCH BẢN THUYẾT TRÌNH & TRẢ LỜI PHẢN BIỆN MẪU (SPEAKER SCRIPT)", page_break_before=True)
add_callout(doc, "LỜI THOẠI TRẢ LỜI MẪU DÀNH CHO BẠN KHI ĐƯỢC CHẤT VẤN TRÊN BỤC: ",
            "'Thưa Thầy và các bạn, đây là một câu hỏi mang tính thời sự rất nóng bỏng phản ánh đúng phong cách điều hành hạ tầng thần tốc hiện nay!\n\n"
            "Thứ nhất, việc người dân và ngân hàng bị 'đánh úp' quy hoạch là hoàn toàn có thật. Khi các đại dự án chiến lược được triển khai theo tinh thần 'chỉ bàn làm không bàn lùi' của Tổng Bí thư Tô Lâm, quy hoạch được điều chỉnh cục bộ khẩn cấp, hệ thống dữ liệu đất đai tại thời điểm cho vay 1-2 năm trước hoàn toàn không có thông tin.\n\n"
            "Thứ hai, để đối phó với rủi ro này, hệ thống ngân hàng không thể có một khoản mục riêng mang tên 'dự phòng giải tỏa đột xuất', nhưng đã thiết lập sẵn 3 TẦNG KHOẢN MỤC CHUYÊN BIỆT:\n"
            "1. Tầng 1 (Chi phí P&L): Khoản mục DỰ PHÒNG CHUNG (0,75% dư nợ) theo Thông tư 11 chính là khoản tiền luật định dành riêng cho những 'tổn thất chưa thể xác định được' như các cú sốc quy hoạch bất ngờ.\n"
            "2. Tầng 2 (Chuẩn mực quốc tế): Khoản mục MANAGEMENT OVERLAY theo IFRS 9 cho phép Ban Điều hành chủ động trích lập một cục dự phòng bổ sung vào P&L khi phát hiện hướng tuyến dự án đi qua khu vực cho vay.\n"
            "3. Tầng 3 (Vốn chủ sở hữu): Nếu khoản lỗ vượt quá dự phòng, ngân hàng sẽ kích hoạt QUỸ DỰ PHÒNG TÀI CHÍNH (trích 10% LNST hàng năm) và ĐỆM VỐN KINH TẾ CAR (10-11%) để hấp thụ hoàn toàn tổn thất mà không làm đe dọa khả năng thanh toán.\n\n"
            "Đồng thời, ngân hàng áp dụng quy trình 4 bước: Lập danh sách Watchlist, tái định giá theo giá đền bù, yêu cầu khách hàng bổ sung TSBĐ khác và phong tỏa trực tiếp nguồn tiền bồi thường từ Kho bạc để thu hồi nợ.'",
            rgb_prefix=(0, 32, 96), bg_hex="F2F5F9", border_color="002060")

# Save DOCX
target_docx = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Khoan_muc_Du_phong_Rui_ro_Giai_toa_Than_toc.docx"
doc.save(target_docx)
print("SUCCESSFULLY SAVED STANDALONE DOCX:", target_docx)

# ==============================================================================
# BUILD GOOGLE-DOCS-READY HTML FILE (WITH EMBEDDED BASE64 DIAGRAMS)
# ==============================================================================
import base64

with open(img1_path, "rb") as f:
    b64_img1 = base64.b64encode(f.read()).decode('utf-8')
with open(img2_path, "rb") as f:
    b64_img2 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Khoản mục Dự phòng & Quy trình Ứng phó Rủi ro Quy hoạch Thần tốc</title>
<style>
  body {{
    background-color: #f0f2f5;
    font-family: 'Times New Roman', Times, serif;
    color: #202124;
    line-height: 1.5;
    margin: 0;
    padding: 20px;
  }}
  .page {{
    background-color: #ffffff;
    max-width: 820px;
    margin: 20px auto;
    padding: 60px 70px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    border-radius: 4px;
    box-sizing: border-box;
  }}
  .header-block {{
    text-align: center;
    border-bottom: 2px solid #002060;
    padding-bottom: 15px;
    margin-bottom: 25px;
  }}
  .univ-title {{
    font-size: 11pt;
    font-weight: bold;
    color: #002060;
    margin-bottom: 6px;
    text-transform: uppercase;
  }}
  .doc-title {{
    font-size: 14.5pt;
    font-weight: bold;
    color: #c00000;
    margin: 12px 0 6px 0;
  }}
  .doc-sub {{
    font-size: 10.5pt;
    font-style: italic;
    color: #555555;
    margin-bottom: 4px;
  }}
  h1 {{
    font-size: 13pt;
    color: #002060;
    border-bottom: 1.5px solid #002060;
    padding-bottom: 4px;
    margin-top: 26px;
    margin-bottom: 12px;
  }}
  h2 {{
    font-size: 11.5pt;
    color: #0f4c81;
    margin-top: 16px;
    margin-bottom: 6px;
  }}
  p {{
    font-size: 11pt;
    margin: 6px 0;
    text-align: justify;
  }}
  .callout-bluf {{
    background-color: #fdf2f2;
    border-left: 4px solid #c00000;
    padding: 12px 16px;
    margin: 14px 0;
    border-radius: 0 4px 4px 0;
    font-size: 10.5pt;
  }}
  .callout-bluf strong {{
    color: #c00000;
  }}
  .callout-script {{
    background-color: #f2f5f9;
    border-left: 4px solid #002060;
    padding: 14px 18px;
    margin: 16px 0;
    border-radius: 0 4px 4px 0;
    font-size: 10.5pt;
    font-style: italic;
  }}
  .callout-script strong {{
    color: #002060;
    font-style: normal;
  }}
  .figure-box {{
    text-align: center;
    margin: 20px 0;
  }}
  .figure-box img {{
    max-width: 100%;
    height: auto;
    border: 1px solid #d3d3d3;
    border-radius: 4px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  }}
  .figure-caption {{
    font-size: 10pt;
    font-weight: bold;
    color: #002060;
    margin-top: 8px;
  }}
  .figure-source {{
    font-size: 8.5pt;
    font-style: italic;
    color: #666666;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 9.5pt;
  }}
  th {{
    background-color: #002060;
    color: #ffffff;
    font-weight: bold;
    padding: 8px 10px;
    text-align: left;
    border: 1px solid #002060;
  }}
  td {{
    padding: 7px 10px;
    border: 1px solid #d3d3d3;
    vertical-align: top;
  }}
  tr:nth-child(even) td {{
    background-color: #f8f9fa;
  }}
  .btn-copy {{
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
  }}
  .btn-copy:hover {{
    background-color: #0f4c81;
  }}
</style>
<script>
function copyAll() {{
  const range = document.createRange();
  range.selectNode(document.querySelector('.page'));
  window.getSelection().removeAllRanges();
  window.getSelection().addRange(range);
  document.execCommand('copy');
  alert('Đã copy toàn bộ nội dung (bao gồm cả bảng và sơ đồ)! Bạn chỉ cần mở Google Docs (docs.new) và nhấn Ctrl+V để dán.');
}}
</script>
</head>
<body>

<button class="btn-copy" onclick="copyAll()">📋 Copy để Dán vào Google Docs</button>

<div class="page">
  <div class="header-block">
    <div class="univ-title">TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN (NEU) — VIỆN NGÂN HÀNG - TÀI CHÍNH</div>
    <div style="font-size: 10pt; font-weight: bold; color: #333;">CHƯƠNG TRÌNH CAO HỌC KHÓA 34 (LỚP K34_3_NH8) — HỌC PHẦN: QUẢN TRỊ RỦI RO</div>
    <div class="doc-title">BÁO CÁO NGHIÊN CỨU CHUYÊN ĐỀ:</div>
    <div style="font-size: 12pt; font-weight: bold; color: #002060; margin-bottom: 6px;">CƠ CHẾ KHOẢN MỤC DỰ PHÒNG & MÔ HÌNH QUẢN TRỊ KHI TÀI SẢN BẢO ĐẢM BỊ 'ĐÁNH ÚP' BỞI QUY HOẠCH HẠ TẦNG THẦN TỐC</div>
    <div class="doc-sub">Bóc tách câu hỏi: Khoản mục nào trong hệ thống kế toán - quản trị ngân hàng chịu trách nhiệm hấp thụ rủi ro thu hồi đất khẩn cấp không có dữ liệu quy hoạch trước?</div>
    <div class="doc-sub">Nhóm thực hiện: Nhóm 2 | Giảng viên hướng dẫn: TS. Khúc Thế Anh</div>
  </div>

  <div class="callout-bluf">
    <strong>TỔNG LUẬN ĐIỀU HÀNH (BLUF):</strong><br>
    <strong>1. Xác nhận thực tiễn:</strong> Thông tin người nêu đưa ra là <em>HOÀN TOÀN CHÍNH XÁC</em>. Dưới phương châm điều hành thần tốc của Tổng Bí thư Tô Lâm ('Hạ tầng là đột phá của đột phá', 'Không bàn lùi, chỉ bàn làm'), các dự án hạ tầng chiến lược được phê duyệt theo cơ chế đặc thù, khiến cả người dân lẫn ngân hàng đều bị 'đánh úp' do dữ liệu quy hoạch trước đó hoàn toàn không hiển thị.<br>
    <strong>2. Khoản mục chịu trách nhiệm:</strong> Không có khoản mục mang tên riêng 'Dự phòng quy hoạch đột xuất', nhưng hệ thống ngân hàng thiết lập sẵn <em>3 TẦNG KHOẢN MỤC ĐÍCH DANH</em> để hấp thụ rủi ro này:<br>
    &nbsp;&nbsp;• <em>Tầng 1 (Chi phí P&L):</em> DỰ PHÒNG CHUNG (0,75% dư nợ Nhóm 1–4 theo Thông tư 11/2021) — Quỹ luật định cho các tổn thất 'chưa xác định được'.<br>
    &nbsp;&nbsp;• <em>Tầng 2 (Chuẩn mực quốc tế):</em> MANAGEMENT OVERLAY (IFRS 9 ECL) — Dự phòng bổ sung theo phán đoán chính trị của Ban Điều hành.<br>
    &nbsp;&nbsp;• <em>Tầng 3 (Vốn chủ sở hữu):</em> QUỸ DỰ PHÒNG TÀI CHÍNH (10% LNST) & ĐỆM VỐN KINH TẾ (CAR 10–11% theo Basel II Trụ cột 2).
  </div>

  <h1>1. BỐI CẢNH THỂ CHẾ: HIỆN TƯỢNG 'QUY HOẠCH THẦN TỐC / QUYẾT LÀ LÀM LUÔN'</h1>
  <p>Trong các lý thuyết kinh tế tài chính và quản trị rủi ro truyền thống, các mô hình chấm điểm tín dụng và thẩm định tài sản bảo đảm (TSBĐ) đều dựa trên giả định môi trường quy hoạch tĩnh: Quy hoạch sử dụng đất và quy hoạch phát triển giao thông được lập theo chu kỳ 5–10 năm, công khai qua bản đồ phân khu 1/2000 và 1/500 tại các cơ quan chức năng.</p>
  <p>Tuy nhiên, bối cảnh quản trị quốc gia hiện nay tại Việt Nam đã có sự chuyển dịch mang tính đột phá:</p>
  <p>• <strong>Thông điệp hành động của Tổng Bí thư Tô Lâm & Chính phủ:</strong> 'Tháo gỡ điểm nghẽn thể chế là đột phá của đột phá', 'Hạ tầng đi trước mở đường', 'Chỉ bàn làm, không bàn lùi'. Các đại dự án chiến lược quốc gia (Đường sắt tốc độ cao Bắc - Nam 67 tỷ USD, các tuyến đường sắt kết nối biên giới phía Bắc, Vành đai 4 Hà Nội, Vành đai 3 TP.HCM, sân bay, cảng biển) được chuyển sang trạng thái khẩn cấp.</p>
  <p>• <strong>Cơ chế đặc thù rút ngắn quy trình lập quy hoạch:</strong> Quốc hội và Chính phủ ban hành hàng loạt nghị quyết thí điểm cơ chế đặc thù: Cho phép điều chỉnh cục bộ quy hoạch không cần chờ điều chỉnh quy hoạch tổng thể; tách riêng công tác bồi thường, tái định cư thành dự án độc lập làm trước thần tốc; rút ngắn thời gian chuẩn bị từ vài năm xuống vài tuần.</p>
  <p>• <strong>Thực tế 'bị đánh úp':</strong> Khi ngân hàng thẩm định cho vay vào năm 2022–2023, căn nhà của khách hàng hoàn toàn nằm trong khu dân cư hiện hữu ổn định, không có bất kỳ thông tin quy hoạch nào. Đến năm 2025–2026, hướng tuyến đại dự án được phê duyệt khẩn cấp đi xuyên qua khu đất. Ngân hàng và người dân bị động 100% trước quyết định này.</p>

  <h1>2. CƠ CHẾ 3 TẦNG KHOẢN MỤC DỰ PHÒNG HẤP THỤ RỦI RO QUY HOẠCH ĐỘT XUẤT</h1>
  <p>Để bảo vệ hệ thống ngân hàng không bị sụp đổ trước các cú sốc sự kiện (Event Risk / Tail Risk), hệ thống kế toán và chuẩn mực an toàn vốn đã phân bổ rủi ro này vào 3 tầng khoản mục cụ thể:</p>

  <div class="figure-box">
    <img src="data:image/png;base64,{b64_img1}" alt="Sơ đồ 1. Mô hình 3 tầng khoản mục dự phòng">
    <div class="figure-caption">Sơ đồ 1. Mô hình 3 tầng khoản mục dự phòng hấp thụ rủi ro quy hoạch giải tỏa đột xuất</div>
    <div class="figure-source">Nguồn: Thiết kế và hệ thống hóa bởi Nhóm 2 dựa trên Thông tư 11/2021/TT-NHNN, IFRS 9 và Khung ICAAP Basel II.</div>
  </div>

  <h2>Tầng 1: Khoản mục DỰ PHÒNG CHUNG (0,75% Dư nợ) — Khoản mục Chi phí P&L</h2>
  <p>- <strong>Căn cứ pháp lý:</strong> Điều 7 Thông tư 11/2021/TT-NHNN và Thông tư 31/2024/TT-NHNN quy định rõ: 'Dự phòng chung là số tiền được trích lập để dự phòng cho những tổn thất có thể xảy ra nhưng chưa xác định được khi trích lập dự phòng cụ thể'.</p>
  <p>- <strong>Quy mô vốn:</strong> Bắt buộc trích lập 0,75% trên tổng dư nợ từ Nhóm 1 đến Nhóm 4. Tại các ngân hàng lớn như Agribank (dư nợ 1,97 triệu tỷ) hay MB (dư nợ 1,08 triệu tỷ), khoản mục Dự phòng chung nằm sẵn trên bảng cân đối kế toán từ 8.000 đến 15.000 tỷ đồng.</p>
  <p>- <strong>Vai trò thực tế:</strong> Đây chính là 'quỹ bảo hiểm rủi ro bất khả kháng'. Vì ngân hàng không thể biết trước nhà nào sẽ bị giải tỏa khẩn cấp, số tiền 0,75% thu từ toàn bộ danh mục cho vay được gộp lại thành một tấm đệm khổng lồ để sẵn sàng bù đắp cho phần giá trị tài sản bị hụt khi biến cố xảy ra.</p>

  <h2>Tầng 2: Khoản mục MANAGEMENT OVERLAY / POST-MODEL ADJUSTMENTS (PMA) — Chuẩn mực IFRS 9</h2>
  <p>- <strong>Bản chất:</strong> Các thuật toán thống kê (Machine Learning / Logistic Regression) để tính PD và LGD trong IFRS 9 hoàn toàn bị 'mù' trước các quyết sách chính trị hoặc dự án thần tốc vì dữ liệu quá khứ không chứa các biến cố này.</p>
  <p>- <strong>Cơ chế hạch toán:</strong> IFRS 9 cho phép Ban Điều hành ngân hàng thiết lập khoản mục 'Management Overlay' — một khoản dự phòng bổ sung dựa trên phán đoán chuyên gia, hạch toán thẳng vào Báo cáo Kết quả Kinh doanh (P&L).</p>
  <p>- <strong>Ứng dụng khi bị 'đánh úp':</strong> Khi Chính phủ công bố một hành lang hạ tầng mới, Khối Quản trị Rủi ro ước tính ngay tổng giá trị tài sản bị ảnh hưởng và trích bổ sung ngay một khoản mục dự phòng riêng (ví dụ 500 – 1.000 tỷ đồng) vào chi phí của kỳ đó, phân bổ cho Stage 2 để bao phủ tổn thất trước khi phương án bồi thường được duyệt.</p>

  <h2>Tầng 3: Khoản mục QUỸ DỰ PHÒNG TÀI CHÍNH & ĐỆM VỐN KINH TẾ (CAR) — Vốn Chủ Sở Hữu</h2>
  <p>- <strong>Quỹ dự phòng tài chính (Luật Các TCTD & Nghị định 93/2017):</strong> Hàng năm ngân hàng bắt buộc trích 10% Lợi nhuận sau thuế vào Quỹ dự phòng tài chính (tối đa bằng 25% vốn điều lệ). Mục đích luật định: Bù đắp phần tổn thất tài sản kinh doanh vượt quá khả năng của quỹ dự phòng trích trong chi phí hoạt động.</p>
  <p>- <strong>Đệm Vốn kinh tế (Economic Capital for Event Risk - Trụ cột 2 Basel II/III ICAAP):</strong> Agribank và MB đều duy trì hệ số an toàn vốn CAR từ 10%–11%, cao hơn mức sàn 8,0%. Khoảng dôi dư 2%–3% (hàng chục nghìn tỷ đồng) chính là đệm vốn tự có để đảm bảo khả năng thanh toán khi xảy ra các cú sốc sự kiện bất khả kháng.</p>

  <h1>3. QUY TRÌNH 4 BƯỚC ỨNG PHÓ KẾ TOÁN & PHÁP LÝ KHI BỊ 'ĐÁNH ÚP' QUY HOẠCH</h1>
  <p>Khi một dự án thần tốc bất ngờ được phê duyệt và công bố hướng tuyến đi qua tài sản thế chấp, ngân hàng lập tức kích hoạt quy trình tác nghiệp 4 bước khép kín:</p>

  <div class="figure-box">
    <img src="data:image/png;base64,{b64_img2}" alt="Sơ đồ 2. Quy trình 4 bước ứng phó của Ngân hàng">
    <div class="figure-caption">Sơ đồ 2. Quy trình 4 bước ứng phó kế toán & pháp lý của Ngân hàng khi bị 'đánh úp' quy hoạch</div>
    <div class="figure-source">Nguồn: Xây dựng bởi Nhóm 2 từ quy trình quản trị rủi ro tín dụng và thu hồi nợ thực tế tại các NHTM Việt Nam.</div>
  </div>

  <p>• <strong>Bước 1: Cách ly & Giám sát đặc biệt (Watchlist):</strong> Ngay khi có thông tin hướng tuyến, hệ thống Core Banking quét toàn bộ các khoản vay có tọa độ/địa chỉ nằm trong bán kính giải tỏa. Chuyển toàn bộ các khoản vay này vào danh sách Giám sát đặc biệt (Watchlist), dừng ngay việc cấp thêm hạn mức tín dụng.</p>
  <p>• <strong>Bước 2: Tái định giá theo giá bồi thường dự kiến & Trích lập Dự phòng cụ thể:</strong> Định giá viên không dùng giá thị trường nữa mà áp dụng giá bồi thường dự kiến của dự án (V_GPMB). Giá trị khấu trừ C bị ép giảm xuống 50% của giá đền bù -> Phần chênh lệch thiếu hụt (A - C) tăng vọt -> Kích hoạt trích lập Dự phòng cụ thể bổ sung, dàn trải chi phí vào các quý gần nhất.</p>
  <p>• <strong>Bước 3: Ràng buộc hợp đồng (Covenants & Event of Default):</strong> Gửi văn bản thông báo khách hàng: Việc tài sản dính thu hồi đất là vi phạm cam kết duy trì TSBĐ. Yêu cầu khách hàng trong 15–30 ngày phải: (1) Nộp TSBĐ bổ sung (sổ tiết kiệm, BĐS khác); hoặc (2) Nộp tiền mặt trả bớt nợ gốc để đưa LTV về mức an toàn.</p>
  <p>• <strong>Bước 4: Thu hồi tiền bồi thường trực tiếp & Xóa nợ nội bảng (Write-off):</strong> Ngân hàng gửi văn bản đăng ký quyền ưu tiên thanh toán đến Ban Bồi thường GPMB và Kho bạc Nhà nước. Toàn bộ tiền đền bù chuyển thẳng vào tài khoản phong tỏa để cấn trừ nợ. Nếu tiền đền bù không đủ nợ gốc, ngân hàng dùng Quỹ dự phòng rủi ro đã trích lập để Xóa nợ nội bảng (Write-off), chuyển nợ ra ngoại bảng để tiếp tục truy đòi các nguồn tài sản khác của người vay.</p>

  <h1>4. MA TRẬN ĐỐI CHIẾU 3 CẤP ĐỘ PHÒNG VỆ CỦA NGÂN HÀNG</h1>
  <table>
    <thead>
      <tr>
        <th style="width:23%;">Cấp độ phòng vệ</th>
        <th style="width:27%;">Khoản mục trích lập / Cơ chế</th>
        <th style="width:22%;">Nguồn trích lập</th>
        <th style="width:28%;">Mục tiêu ứng phó rủi ro quy hoạch</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Tầng 1: Chi phí hoạt động</strong><br>(Thông tư 11/2021/TT-NHNN)</td>
        <td><strong>DỰ PHÒNG CHUNG</strong><br>(Tỷ lệ 0,75% dư nợ Nhóm 1–4)</td>
        <td>Chi phí hoạt động kinh doanh (P&L)</td>
        <td>Tạo tấm đệm thanh khoản thường trực để bù đắp các khoản tổn thất bất ngờ, chưa xác định được nguyên nhân tại thời điểm cho vay.</td>
      </tr>
      <tr>
        <td><strong>Tầng 2: Chuẩn mực Quốc tế</strong><br>(Chuẩn mực IFRS 9 ECL)</td>
        <td><strong>MANAGEMENT OVERLAY</strong><br>(Post-Model Adjustments - PMA)</td>
        <td>Chi phí dự phòng bổ sung trên P&L</td>
        <td>Bù đắp điểm mù của mô hình thống kê; Ban Điều hành chủ động trích lập dự phòng đón đầu theo phán đoán chính sách và hướng tuyến dự án.</td>
      </tr>
      <tr>
        <td><strong>Tầng 3: Vốn chủ sở hữu</strong><br>(Luật TCTD & Basel II/III)</td>
        <td><strong>QUỸ DỰ PHÒNG TÀI CHÍNH (10% LNST)</strong><br>& ĐỆM VỐN KINH TẾ (CAR 10–11%)</td>
        <td>Lợi nhuận sau thuế & Vốn tự có (Tier 1 & Tier 2)</td>
        <td>Cứu cánh cuối cùng: Hấp thụ các khoản lỗ thực tế vượt quá khả năng của chi phí dự phòng, bảo đảm an toàn hệ thống và không vi phạm CAR.</td>
      </tr>
    </tbody>
  </table>

  <h1>5. KỊCH BẢN THUYẾT TRÌNH & TRẢ LỜI PHẢN BIỆN MẪU (SPEAKER SCRIPT)</h1>
  <div class="callout-script">
    <strong>LỜI THOẠI TRẢ LỜI MẪU DÀNH CHO BẠN KHI ĐƯỢC CHẤT VẤN TRÊN BỤC:</strong><br><br>
    'Thưa Thầy và các bạn, đây là một câu hỏi mang tính thời sự rất nóng bỏng phản ánh đúng phong cách điều hành hạ tầng thần tốc hiện nay!<br><br>
    Thứ nhất, việc người dân và ngân hàng bị 'đánh úp' quy hoạch là hoàn toàn có thật. Khi các đại dự án chiến lược được triển khai theo tinh thần 'chỉ bàn làm không bàn lùi' của Tổng Bí thư Tô Lâm, quy hoạch được điều chỉnh cục bộ khẩn cấp, hệ thống dữ liệu đất đai tại thời điểm cho vay 1-2 năm trước hoàn toàn không có thông tin.<br><br>
    Thứ hai, để đối phó với rủi ro này, hệ thống ngân hàng không thể có một khoản mục riêng mang tên 'dự phòng giải tỏa đột xuất', nhưng đã thiết lập sẵn 3 TẦNG KHOẢN MỤC CHUYÊN BIỆT:<br>
    1. Tầng 1 (Chi phí P&L): Khoản mục DỰ PHÒNG CHUNG (0,75% dư nợ) theo Thông tư 11 chính là khoản tiền luật định dành riêng cho những 'tổn thất chưa thể xác định được' như các cú sốc quy hoạch bất ngờ.<br>
    2. Tầng 2 (Chuẩn mực quốc tế): Khoản mục MANAGEMENT OVERLAY theo IFRS 9 cho phép Ban Điều hành chủ động trích lập một cục dự phòng bổ sung vào P&L khi phát hiện hướng tuyến dự án đi qua khu vực cho vay.<br>
    3. Tầng 3 (Vốn chủ sở hữu): Nếu khoản lỗ vượt quá dự phòng, ngân hàng sẽ kích hoạt QUỸ DỰ PHÒNG TÀI CHÍNH (trích 10% LNST hàng năm) và ĐỆM VỐN KINH TẾ CAR (10-11%) để hấp thụ hoàn toàn tổn thất mà không làm đe dọa khả năng thanh toán.<br><br>
    Đồng thời, ngân hàng áp dụng quy trình 4 bước: Lập danh sách Watchlist, tái định giá theo giá đền bù, yêu cầu khách hàng bổ sung TSBĐ khác và phong tỏa trực tiếp nguồn tiền bồi thường từ Kho bạc để thu hồi nợ.'
  </div>
</div>

</body>
</html>
"""

target_html = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Khoan_muc_Du_phong_Rui_ro_Giai_toa_Than_toc.html"
with open(target_html, "w", encoding="utf-8") as f:
    f.write(html_content)
print("SUCCESSFULLY SAVED STANDALONE HTML WITH BASE64 DIAGRAMS:", target_html)

