import os
import shutil
import base64
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
    p_cap.paragraph_format.space_after = Pt(1)
    p_cap.paragraph_format.keep_with_next = True
    r_cap = p_cap.add_run(caption_title)
    style_run(r_cap, font_name="Times New Roman", size_pt=9.5, bold=True, color_rgb=(0, 32, 96))
    
    p_src = doc.add_paragraph()
    p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_src.paragraph_format.space_before = Pt(0)
    p_src.paragraph_format.space_after = Pt(6)
    r_src = p_src.add_run(source_text)
    style_run(r_src, font_name="Times New Roman", size_pt=8.5, italic=True, color_rgb=(80, 80, 80))

def format_custom_table(tbl, col_widths, headers, data, header_bg="002060", alt_bg="F9FBFD"):
    tblPr = tbl._element.xpath('w:tblPr')[0]
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="002060"/>'
        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="002060"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="D3D3D3"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblLook = tblPr.find(qn('w:tblLook'))
    if tblLook is not None:
        tblLook.addprevious(borders)
    else:
        tblPr.append(borders)
        
    hdr_row = tbl.rows[0]
    trPr = hdr_row._tr.get_or_add_trPr()
    cantSplit = parse_xml(f'<w:cantSplit {nsdecls("w")}/>')
    tblHeader = parse_xml(f'<w:tblHeader {nsdecls("w")}/>')
    trPr.append(cantSplit)
    trPr.append(tblHeader)
    
    for c_idx, cell in enumerate(hdr_row.cells):
        cell.width = Inches(col_widths[c_idx])
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{header_bg}"/>')
        tcPr.append(shd)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(headers[c_idx])
        style_run(r, font_name="Times New Roman", size_pt=9.5, bold=True, color_rgb=(255, 255, 255))
        
    for r_idx, row_data in enumerate(data):
        row = tbl.rows[r_idx + 1]
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        bg_color = alt_bg if (r_idx % 2 == 1) else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.width = Inches(col_widths[c_idx])
            tcPr = cell._tc.get_or_add_tcPr()
            if bg_color != "FFFFFF":
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>')
                tcPr.append(shd)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if (c_idx >= 1 and len(val) <= 12) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.1
            r = p.add_run(val)
            is_bold = (c_idx == 0) or ("AGRIBANK" in val) or ("MBBANK" in val) or ("TỔNG" in val)
            style_run(r, font_name="Times New Roman", size_pt=9, bold=is_bold, color_rgb=(0,0,0))

# ----------------- MAIN BUILD FUNCTION -----------------
def generate_docx(target_docx, img1_path, img2_path, img3_path):
    doc = docx.Document()
    
    # Page setup
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)
        
    # Header block
    p_uni = add_p(doc, "TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN (NEU) — VIỆN NGÂN HÀNG - TÀI CHÍNH", space_after=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_uni.runs[0], size_pt=9.5, bold=True, color_rgb=(80, 80, 80))
    p_sub = add_p(doc, "CHƯƠNG TRÌNH CAO HỌC KHÓA 34 (LỚP K34_3_NH8) — HỌC PHẦN: QUẢN TRỊ RỦI RO", space_after=6, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_sub.runs[0], size_pt=9, italic=True, color_rgb=(100, 100, 100))
    
    # Title
    p_title = add_p(doc, "BÁO CÁO NGHIỆP VỤ & GIẢI TRÌNH CHUYÊN SÂU:", space_before=4, space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_title.runs[0], size_pt=12, bold=True, color_rgb=(0, 32, 96))
    p_title2 = add_p(doc, "HỆ THỐNG KHOẢN MỤC DỰ PHÒNG & MÔ HÌNH QUY TRÌNH ỨNG PHÓ KHI TÀI SẢN THẾ CHẤP BỊ 'ĐÁNH ÚP' BỞI QUY HOẠCH HẠ TẦNG THẦN TỐC", space_before=2, space_after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_title2.runs[0], size_pt=13.5, bold=True, color_rgb=(192, 0, 0))
    
    p_meta = add_p(doc, "Chuyên đề: Quản trị rủi ro khoản vay dính giải tỏa mặt bằng & Phân tích so sánh Agribank vs MBBank | Người thực hiện: Nhóm 2", space_after=8, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_meta.runs[0], size_pt=9.5, italic=True, color_rgb=(60, 60, 60))
    
    # Callout BLUF
    bluf_body = (
        " 1. Xác thực thực tế: Nhận định của Anh/Chị về hiện tượng người dân lẫn ngân hàng bị 'đánh úp' bởi các quyết sách hạ tầng triển khai thần tốc "
        "theo phong cách điều hành mới là HOÀN TOÀN CHUẨN XÁC 100%. Tại thời điểm cấp tín dụng, dữ liệu quy hoạch hoàn toàn là 'đất ở sạch', nhưng "
        "khi cơ chế đặc thù được Quốc hội phê duyệt, tài sản thế chấp bị thu hồi khẩn cấp.\n"
        "2. Hệ thống Khoản mục Dự phòng chịu trách nhiệm (3 Tầng nấc): Tầng 1 là DỰ PHÒNG CHUNG (0,75% dư nợ) theo Thông tư 11/2021; "
        "Tầng 2 là MANAGEMENT OVERLAY (IFRS 9) do Ban Điều hành chủ động trích lập; Tầng 3 là QUỸ DỰ PHÒNG TÀI CHÍNH (10% LNST theo Luật Các TCTD) "
        "và ĐỆM VỐN KINH TẾ (CAR 10-11%) thuộc Vốn chủ sở hữu.\n"
        "3. So sánh chuyên sâu Agribank vs MB: Cả hai ngân hàng đều trích 10% LNST vào Quỹ dự phòng tài chính. Tuy nhiên, MB liên tục chia cổ tức bằng cổ phiếu "
        "giúp vốn điều lệ tăng vọt lên 61.643 tỷ, nới trần quỹ lên 15.411 tỷ và sở hữu đệm CAR dày (+3% RWA); trong khi Agribank bị nghẽn trần quỹ nhiều năm "
        "ở mức 7.600-8.600 tỷ và đệm CAR mỏng (9,2%-10,2%), phụ thuộc nguồn cấp vốn từ Ngân sách Nhà nước."
    )
    add_callout(doc, "TỔNG LUẬN ĐIỀU HÀNH (BOTTOM LINE UP FRONT - BLUF):", bluf_body)
    
    # SECTION 1
    add_h1(doc, "1. XÁC THỰC THÔNG TIN & BỐI CẢNH QUẢN TRỊ RỦI RO ĐỘT XUẤT")
    add_p(doc, "1.1. Hiện tượng 'Bị đánh úp quy hoạch' là hoàn toàn có thật trong kỷ nguyên mới:")
    add_p(doc, "• Chính sách hạ tầng thần tốc: Dưới sự chỉ đạo quyết liệt của Tổng Bí thư Tô Lâm và Thủ tướng Chính phủ Phạm Minh Chính, chủ trương 'chỉ bàn làm, không bàn lùi' được quán triệt xuyên suốt. Hàng loạt đại dự án hạ tầng giao thông động lực quốc gia (Đường sắt tốc độ cao Bắc - Nam 67 tỷ USD, các tuyến đường sắt kết nối phía Bắc, mạng lưới cao tốc Bắc - Nam giai đoạn 2, đường Vành đai 4 Hà Nội, Vành đai 3 TP.HCM...) đều áp dụng cơ chế đặc thù được Quốc hội phê chuẩn:")
    add_p(doc, "  - Tách công tác Bồi thường, Hỗ trợ, Tái định cư thành dự án độc lập để thực hiện trước.")
    add_p(doc, "  - Cho phép điều chỉnh cục bộ quy hoạch khẩn cấp mà không cần chờ điều chỉnh quy hoạch tổng thể cấp tỉnh/thành phố.")
    add_p(doc, "• Hệ quả đối với Ngân hàng và Người dân: Tại thời điểm thẩm định cấp tín dụng (1–3 năm trước), cán bộ ngân hàng kiểm tra quy hoạch tại Sở Quy hoạch - Kiến trúc, Sở Tài nguyên và Môi trường đều xác nhận thửa đất là 'đất ở đô thị sạch', không có tranh chấp hay quy hoạch. Khi hướng tuyến đại dự án được chốt và cắm mốc khẩn cấp, cả khách hàng vay vốn và ngân hàng thương mại đều rơi vào thế bị động hoàn toàn (Unanticipated Event Shock).")
    add_p(doc, "1.2. Bản chất tài chính: Dự phòng là bút toán ghi nhận tổn thất (Loss Recognition), không tự sinh ra dòng tiền để bù lỗ nếu tiền đền bù thấp hơn nợ gốc. Vì vậy, hệ thống ngân hàng thiết lập mô hình đa tầng nấc để hấp thụ rủi ro này.")
    
    # SECTION 2
    add_h1(doc, "2. HỆ THỐNG 3 TẦNG KHOẢN MỤC DỰ PHÒNG CHỊU TRÁCH NHIỆM HẤP THỤ RỦI RO")
    add_p(doc, "Trong nguyên lý kế toán ngân hàng quốc tế và Việt Nam, không có một khoản mục riêng biệt mang tên 'Dự phòng rủi ro giải tỏa mặt bằng đột xuất'. Thay vào đó, toàn bộ rủi ro này được chia thành 3 TẦNG KHOẢN MỤC CHUYÊN BIỆT hấp thụ theo thứ tự từ thấp lên cao:")
    
    add_image_figure(doc, img1_path, 
                     "Sơ đồ 1. Mô hình 3 tầng khoản mục dự phòng hấp thụ rủi ro quy hoạch / giải tỏa đột xuất",
                     "Nguồn: Nhóm 2 tổng hợp từ Thông tư 11/2021/TT-NHNN, Chuẩn mực IFRS 9 và Luật Các TCTD 2024.")
    
    add_h2(doc, "Tầng 1: Khoản mục DỰ PHÒNG CHUNG (0,75%) — Chi phí P&L (Thông tư 11 & Thông tư 31)")
    add_p(doc, "• Cơ sở pháp lý: Điều 7 Thông tư 11/2021/TT-NHNN và Thông tư 31/2024/TT-NHNN. Bắt buộc trích 0,75% trên tổng dư nợ từ Nhóm 1 đến Nhóm 4.")
    add_p(doc, "• Định nghĩa luật định: 'Dự phòng chung là số tiền dự phòng được trích lập để dự phòng cho những tổn thất có thể xảy ra nhưng chưa xác định được khi trích lập dự phòng cụ thể.'")
    add_p(doc, "• Vai trò thực tế: Đây chính là chiếc 'áo giáp tập thể' của toàn bộ danh mục. Vì ngân hàng không thể biết trước chính xác căn nhà nào sẽ bị quy hoạch cắt ngang, số tiền 0,75% thu từ toàn bộ danh mục hàng trăm nghìn khách hàng được gộp lại thành một quỹ dự phòng khổng lồ (tại MBBank đạt hơn 4.500 tỷ đồng, Agribank đạt gần 12.000 tỷ đồng) để sẵn sàng bù đắp cho các khoản hụt giá trị tài sản đột xuất.")
    
    add_h2(doc, "Tầng 2: Khoản mục MANAGEMENT OVERLAY / POST-MODEL ADJUSTMENTS (PMA) — Chuẩn mực IFRS 9")
    add_p(doc, "• Bản chất kỹ thuật: Các thuật toán thống kê định lượng của IFRS 9 (tính xác suất vỡ nợ PD và tỷ lệ tổn thất khi vỡ nợ LGD) hoàn toàn bị 'mù' trước các quyết sách chính trị hoặc điều chỉnh hạ tầng thần tốc vì dữ liệu quá khứ không hề có tiền lệ.")
    add_p(doc, "• Cơ chế hạch toán: IFRS 9 cho phép Ban Điều hành ngân hàng thiết lập khoản mục 'Management Overlay' — một khoản chi phí dự phòng bổ sung dựa trên phán đoán chuyên gia (Expert Judgement), ghi nhận thẳng vào Báo cáo P&L.")
    add_p(doc, "• Ứng dụng khi bị 'đánh úp': Khi Chính phủ công bố một hành lang hạ tầng khẩn cấp, Khối Quản trị Rủi ro ước tính ngay tổng giá trị tài sản bị ảnh hưởng và trích bổ sung ngay một khoản mục dự phòng riêng (ví dụ 500 – 1.000 tỷ đồng) vào chi phí của kỳ đó, phân bổ cho Stage 2 để bao phủ tổn thất trước khi phương án bồi thường được duyệt.")
    
    add_h2(doc, "Tầng 3: Khoản mục QUỸ DỰ PHÒNG TÀI CHÍNH & ĐỆM VỐN KINH TẾ (CAR) — Vốn Chủ Sở Hữu")
    add_p(doc, "• Quỹ dự phòng tài chính: Theo Điều 149 Luật Các TCTD 2024 và Nghị định 93/2017/NĐ-CP, hàng năm ngân hàng trích 10% LNST vào Quỹ dự phòng tài chính (tối đa bằng 25% vốn điều lệ). Mục đích luật định: Bù đắp phần tổn thất tài sản kinh doanh xảy ra trong quá trình hoạt động vượt quá số dư của quỹ dự phòng rủi ro trích trong chi phí.")
    add_p(doc, "• Đệm Vốn kinh tế (Economic Capital Buffer - Basel II/III ICAAP): Agribank và MB duy trì hệ số an toàn vốn CAR từ 10%–11%, cao hơn mức sàn 8,0%. Khoảng dôi dư 2%–3% (hàng chục nghìn tỷ đồng vốn tự có) đóng vai trò là 'lớp khiên phòng vệ tối thượng' để bảo đảm thanh toán ngay cả khi toàn bộ danh mục tài sản bảo đảm tại một khu vực bị xóa sổ giá trị thương mại.")
    
    # SECTION 3 - EXPANDED COMPARISON AGRIBANK VS MB
    add_h1(doc, "3. LÀM RÕ CƠ CHẾ KHOẢN MỤC 3: PHÂN TÍCH SO SÁNH AGRIBANK vs MBBANK")
    add_p(doc, "Khi đặt câu hỏi: 'Nếu xảy ra cú sốc giải tỏa thần tốc trên diện rộng vượt quá khả năng của chi phí dự phòng P&L, Khoản mục 3 trích lập và vận hành như thế nào tại Agribank và MBBank?', chúng ta thấy rõ sự phân hóa sâu sắc giữa hai mô hình sở hữu:")
    
    add_image_figure(doc, img3_path,
                     "Sơ đồ 3. Cơ chế trích lập & Vận hành Khoản mục 3 (Vốn chủ sở hữu): Agribank vs MBBank",
                     "Nguồn: Xây dựng bởi Nhóm 2 từ Luật Các TCTD 2024, Nghị định 93/2017/NĐ-CP và BCTC kiểm toán 2020–2025.")
    
    add_p(doc, "Bảng dưới đây tổng hợp chuỗi số liệu thực tế được kiểm toán (KPMG, Deloitte, E&Y) phản ánh dung lượng và năng lực của Khoản mục 3 tại hai ngân hàng giai đoạn 2020–2025:")
    
    tbl_data_headers = ["Chỉ tiêu tài chính (tỷ đồng / %)", "2020", "2021", "2022", "2023", "2024", "2025"]
    tbl_data_rows = [
        ["[1] AGRIBANK (100% VỐN NHÀ NƯỚC)", "", "", "", "", "", ""],
        ["- Lợi nhuận sau thuế (LNST Hợp nhất)", "10.517", "12.261", "18.043", "20.696", "22.067", "24.955"],
        ["- Số trích Quỹ dự phòng tài chính (10% LNST)", "1.052", "1.226", "1.804", "2.070", "2.207", "2.496"],
        ["- Vốn điều lệ cuối năm", "30.710", "34.328", "34.447", "41.269", "51.639", "51.639"],
        ["- Mức trần Quỹ tối đa luật định (25% VĐL)", "7.678", "8.582", "8.612", "10.317", "12.910", "12.910"],
        ["- Tổng Vốn chủ sở hữu (Hợp nhất)", "73.084", "76.087", "86.998", "100.536", "124.068", "131.191"],
        ["- Hệ số an toàn vốn CAR (TT 22 -> TT 41)", "10,58%", "10,50%", "10,80%", "9,20%", "11,36%", "10,22%"],
        ["[2] MBBANK (NHTMCP QUÂN ĐỘI)", "", "", "", "", "", ""],
        ["- Lợi nhuận sau thuế (LNST Hợp nhất)", "8.606", "13.221", "18.155", "21.054", "22.951", "27.383"],
        ["- Số trích Quỹ dự phòng tài chính (10% LNST)", "861", "1.322", "1.816", "2.105", "2.295", "2.738"],
        ["- Vốn điều lệ cuối năm", "27.988", "37.783", "45.340", "52.141", "61.643", "61.643"],
        ["- Mức trần Quỹ tối đa luật định (25% VĐL)", "6.997", "9.446", "11.335", "13.035", "15.411", "15.411"],
        ["- Tổng Vốn chủ sở hữu (Hợp nhất)", "50.099", "62.486", "79.613", "96.711", "117.060", "142.023"],
        ["- Hệ số an toàn vốn CAR (Thông tư 41)", "10,42%", "11,28%", "11,53%", "10,75%", "11,80%", "11,00%"]
    ]
    tbl_comp = doc.add_table(rows=len(tbl_data_rows) + 1, cols=7)
    tbl_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    format_custom_table(tbl_comp, [2.4, 0.7, 0.7, 0.7, 0.7, 0.7, 0.77], tbl_data_headers, tbl_data_rows, header_bg="002060")
    
    add_p(doc, "3.1. Phân tích điểm nghẽn trần quỹ của Agribank vs Nới trần liên tục của MBBank:")
    add_p(doc, "• Tại Agribank: Do 100% vốn thuộc sở hữu Nhà nước, vốn điều lệ không thể tự tăng bằng cách phát hành cổ phiếu mà phải trải qua quy trình biểu quyết của Quốc hội để được cấp vốn từ ngân sách (như Nghị quyết 101/2023/QH15 bổ sung 17.100 tỷ). Do đó, giai đoạn 2020–2022 vốn điều lệ dậm chân quanh 30.700 – 34.400 tỷ, khiến mức trần Quỹ dự phòng tài chính bị nghẽn ở mức 7.600 – 8.600 tỷ đồng dù mỗi năm ngân hàng có thể trích tới 1.800 – 2.000 tỷ đồng từ LNST.")
    add_p(doc, "• Tại MBBank: MB liên tục chi trả cổ tức bằng cổ phiếu từ nguồn lợi nhuận giữ lại khổng lồ. Vốn điều lệ tăng hơn gấp đôi từ gần 28.000 tỷ (2020) lên hơn 61.600 tỷ đồng (2024–2025). Nhờ đó, trần Quỹ dự phòng tài chính của MB tự động nới rộng từ 7.000 tỷ lên 15.411 tỷ đồng, cho phép MB tích lũy quỹ dự phòng tài chính vượt trội.")
    
    add_p(doc, "3.2. Quy trình kích hoạt 2 nấc của Khoản mục 3 khi xảy ra tổn thất tài sản vượt chi phí P&L:")
    add_p(doc, "• Nấc 1: Rút số dư Quỹ dự phòng tài chính để bù đắp tổn thất tài sản kinh doanh (Điều 149 Luật Các TCTD):")
    add_p(doc, "  - Khi cú sốc giải tỏa trên diện rộng làm tổn thất thực tế vượt quá toàn bộ số dư Quỹ dự phòng rủi ro P&L, ngân hàng ghi giảm Quỹ dự phòng tài chính (ghi Nợ Quỹ / Ghi Có Khoản nợ tổn thất).")
    add_p(doc, "  - Tại Agribank: Thủ tục mang tính hành chính nhà nước chặt chẽ. HĐTV Agribank phải lập hồ sơ phương án tổn thất, chứng minh nguyên nhân khách quan do quy hoạch hạ tầng của Nhà nước, trình Thống đốc NHNN và Bộ Tài chính thẩm định phê duyệt để bảo đảm không làm thất thoát vốn Nhà nước trước Kiểm toán Nhà nước.")
    add_p(doc, "  - Tại MBBank: Thẩm quyền thuộc về ĐHĐCĐ và được ủy quyền cho Hội đồng Quản trị quyết định xử lý thương mại theo Điều lệ ngân hàng, thủ tục nhanh gọn và phản ứng linh hoạt hơn.")
    add_p(doc, "• Nấc 2: Hấp thụ vào Đệm Vốn kinh tế (CAR) theo Chuẩn mực Basel II / ICAAP:")
    add_p(doc, "  - Khoản lỗ sau khi xóa nợ sẽ trực tiếp làm xói mòn Vốn tự có Cấp 1, kéo giảm hệ số CAR.")
    add_p(doc, "  - Tại MBBank: Sở hữu tấm đệm CAR dày dặn 11,0% – 11,8% (dôi dư gần +3% RWA so với mức sàn 8,0%), MB có thể hấp thụ cú sốc hàng nghìn tỷ đồng mà CAR vẫn duy trì an toàn trên 10%, sau đó nhanh chóng bù đắp lại nhờ LNST hàng năm trên 23.000 – 27.000 tỷ đồng.")
    add_p(doc, "  - Tại Agribank: CAR năm 2023 từng tụt xuống 9,20% khi chuyển đổi sang Thông tư 41 (chỉ cách mức sàn 8% đúng 1,2% RWA). Đệm vốn kinh tế của Agribank mỏng hơn, nếu bị cú sốc giải tỏa lớn ăn vào vốn tự có, ngân hàng sẽ đối mặt nguy cơ chạm trần sàn an toàn vốn và buộc phải trông chờ vào nguồn cấp vốn bổ sung từ Ngân sách.")
    
    # SECTION 4 - WORKFLOW
    add_h1(doc, "4. QUY TRÌNH 4 BƯỚC ỨNG PHÓ KẾ TOÁN & PHÁP LÝ KHI BỊ 'ĐÁNH ÚP' QUY HOẠCH")
    add_p(doc, "Khi một dự án thần tốc bất ngờ được phê duyệt và công bố hướng tuyến đi qua tài sản thế chấp, ngân hàng lập tức kích hoạt quy trình tác nghiệp 4 bước khép kín:")
    
    add_image_figure(doc, img2_path,
                     "Sơ đồ 2. Quy trình 4 bước ứng phó kế toán & pháp lý của Ngân hàng khi bị 'đánh úp' quy hoạch",
                     "Nguồn: Xây dựng bởi Nhóm 2 từ quy trình quản trị rủi ro tín dụng và thu hồi nợ thực tế tại các NHTM Việt Nam.")
    
    add_p(doc, "• Bước 1: Cách ly & Giám sát đặc biệt (Watchlist): Ngay khi có thông tin hướng tuyến, hệ thống Core Banking quét toàn bộ các khoản vay có tọa độ/địa chỉ nằm trong bán kính giải tỏa. Chuyển toàn bộ các khoản vay này vào danh sách Giám sát đặc biệt (Watchlist), dừng ngay việc cấp thêm hạn mức tín dụng.")
    add_p(doc, "• Bước 2: Tái định giá theo giá bồi thường dự kiến & Trích lập Dự phòng cụ thể: Định giá viên không dùng giá thị trường nữa mà áp dụng giá bồi thường dự kiến của dự án (V_GPMB). Giá trị khấu trừ C bị ép giảm xuống 50% của giá đền bù -> Phần chênh lệch thiếu hụt (A - C) tăng vọt -> Kích hoạt trích lập Dự phòng cụ thể bổ sung, dàn trải chi phí vào các quý gần nhất.")
    add_p(doc, "• Bước 3: Ràng buộc hợp đồng (Covenants & Event of Default): Gửi văn bản thông báo khách hàng: Việc tài sản dính thu hồi đất là vi phạm cam kết duy trì TSBĐ. Yêu cầu khách hàng trong 15–30 ngày phải: (1) Nộp TSBĐ bổ sung (sổ tiết kiệm, BĐS khác); hoặc (2) Nộp tiền mặt trả bớt nợ gốc để đưa LTV về mức an toàn.")
    add_p(doc, "• Bước 4: Thu hồi tiền bồi thường trực tiếp & Xóa nợ nội bảng (Write-off): Ngân hàng gửi văn bản đăng ký quyền ưu tiên thanh toán đến Ban Bồi thường GPMB và Kho bạc Nhà nước. Toàn bộ tiền đền bù chuyển thẳng vào tài khoản phong tỏa để cấn trừ nợ. Nếu tiền đền bù không đủ nợ gốc, ngân hàng dùng Quỹ dự phòng rủi ro đã trích lập để Xóa nợ nội bảng (Write-off), chuyển nợ ra ngoại bảng để tiếp tục truy đòi các nguồn tài sản khác của người vay.")
    
    # SECTION 5 - MATRIX
    add_h1(doc, "5. MA TRẬN ĐỐI CHIẾU CHUYÊN SÂU GIỮA AGRIBANK VÀ MBBANK")
    
    tbl_mat_headers = ["Tiêu chí so sánh", "Agribank (NHTM 100% Vốn Nhà nước)", "MBBank (NHTMCP Quân đội)"]
    tbl_mat_rows = [
        ["1. Cơ sở trích lập hàng năm", "Trích cứng 10% LNST theo NĐ 93/2017 & TT hướng dẫn của Bộ Tài chính.", "Trích 10% LNST theo NĐ 93/2017 & Điều lệ tổ chức hoạt động của MB."],
        ["2. Mức trần Quỹ (25% VĐL)", "12.910 tỷ đồng (bị chặn trần bởi vốn ĐL 51.639 tỷ, trước 2023 chỉ 8.600 tỷ).", "15.411 tỷ đồng (nới rộng liên tục theo đà tăng vốn ĐL lên 61.643 tỷ)."],
        ["3. Cơ chế tăng vốn nới trần", "Bị động: Phụ thuộc vào Ngân sách Nhà nước & Nghị quyết phê chuẩn của Quốc hội.", "Chủ động: Tự động hóa qua chia cổ tức bằng cổ phiếu từ lợi nhuận giữ lại."],
        ["4. Thẩm quyền quyết định dùng Quỹ", "HĐTV Agribank lập hồ sơ -> Trình NHNN và Bộ Tài chính phê duyệt.", "ĐHĐCĐ ủy quyền cho Hội đồng Quản trị MBBank chủ động phê duyệt."],
        ["5. Trách nhiệm giải trình kiểm toán", "Rất nghiêm ngặt: Thanh tra NHNN, Kiểm toán Nhà nước, Thanh tra Chính phủ.", "Kiểm toán độc lập Big 4 (KPMG) & Ban Kiểm soát theo chuẩn niêm yết."],
        ["6. Đệm Vốn kinh tế CAR dôi dư", "Mỏng: CAR 9,20% - 10,22% (chỉ dôi dư 1,2% - 2,2% RWA so với mức sàn 8%).", "Dày dặn: CAR 10,75% - 11,80% (dôi dư 2,7% - 3,8% RWA so với mức sàn 8%)."],
        ["7. Khả năng tự bù đắp cú sốc", "Chậm, phụ thuộc vào cơ chế phân bổ và hỗ trợ từ Ngân sách Nhà nước.", "Rất nhanh nhờ ROE cao (20-25%/năm) và thị trường vốn đa kênh linh hoạt."]
    ]
    tbl_mat = doc.add_table(rows=len(tbl_mat_rows) + 1, cols=3)
    tbl_mat.alignment = WD_TABLE_ALIGNMENT.CENTER
    format_custom_table(tbl_mat, [1.8, 2.4, 2.47], tbl_mat_headers, tbl_mat_rows, header_bg="002060")
    
    # SECTION 6 - SPEAKER SCRIPT
    add_h1(doc, "6. KỊCH BẢN THUYẾT TRÌNH & TRẢ LỜI PHẢN BIỆN MẪU (SPEAKER SCRIPT)")
    script_content = (
        " 'Kính thưa Thầy và các bạn, đây là một câu hỏi mang tính thời sự rất nóng bỏng phản ánh đúng thực tiễn điều hành hạ tầng thần tốc hiện nay!\n\n"
        "Thứ nhất, việc người dân và ngân hàng bị 'đánh úp' quy hoạch là hoàn toàn có thật. Khi các đại dự án chiến lược được triển khai theo tinh thần "
        "'chỉ bàn làm không bàn lùi' của Tổng Bí thư Tô Lâm, quy hoạch được điều chỉnh cục bộ khẩn cấp, hệ thống dữ liệu đất đai tại thời điểm cho vay 1-2 năm trước hoàn toàn không có thông tin.\n\n"
        "Thứ hai, để đối phó với rủi ro này, hệ thống ngân hàng thiết lập sẵn 3 TẦNG KHOẢN MỤC CHUYÊN BIỆT:\n"
        "1. Tầng 1 (Chi phí P&L): Khoản mục DỰ PHÒNG CHUNG (0,75% dư nợ) theo Thông tư 11 chính là khoản tiền luật định dành riêng cho những 'tổn thất chưa thể xác định được'.\n"
        "2. Tầng 2 (Chuẩn mực quốc tế): Khoản mục MANAGEMENT OVERLAY theo IFRS 9 cho phép Ban Điều hành chủ động trích lập một cục dự phòng bổ sung vào P&L khi phát hiện hướng tuyến dự án đi qua khu vực cho vay.\n"
        "3. Tầng 3 (Vốn chủ sở hữu): Nếu khoản lỗ vượt quá dự phòng, ngân hàng sẽ kích hoạt QUỸ DỰ PHÒNG TÀI CHÍNH (trích 10% LNST hàng năm) và ĐỆM VỐN KINH TẾ CAR (10-11%) để hấp thụ hoàn toàn tổn thất.\n\n"
        "Thứ ba, sự phân hóa giữa Agribank và MBBank tại Khoản mục 3 thể hiện ở 2 điểm mấu chốt:\n"
        "- MBBank có trần Quỹ dự phòng tài chính lên tới hơn 15.400 tỷ đồng và đệm CAR dày (+3% RWA), thẩm quyền xử lý do HĐQT linh hoạt quyết định và khả năng tự bù đắp cực nhanh nhờ ROE 20-25%.\n"
        "- Trong khi đó, Agribank bị nghẽn trần quỹ ở mức 12.900 tỷ (trước 2023 chỉ 8.600 tỷ) do vốn điều lệ tăng chậm phụ thuộc ngân sách; việc rút quỹ bắt buộc phải trình qua NHNN và Bộ Tài chính phê duyệt; đồng thời đệm CAR mỏng (9,2%-10,2%) nên nếu chịu cú sốc lớn sẽ phải kiến nghị Nhà nước tiếp tục cấp bù vốn điều lệ.'"
    )
    add_callout(doc, "LỜI THOẠI TRẢ LỜI MẪU DÀNH CHO BẠN KHI ĐƯỢC CHẤT VẤN TRÊN BỤC:", script_content, rgb_prefix=(0, 32, 96), bg_hex="F0F4F8", border_color="002060")
    
    doc.save(target_docx)
    print("SUCCESSFULLY SAVED COMPLETE ENRICHED DOCX:", target_docx)

# ----------------- MAIN EXECUTION -----------------
target_dir = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2"
target_docx = os.path.join(target_dir, "Khoan_muc_Du_phong_Rui_ro_Giai_toa_Than_toc.docx")
target_html = os.path.join(target_dir, "Khoan_muc_Du_phong_Rui_ro_Giai_toa_Than_toc.html")

img1_path = r"C:\Users\Admin\.gemini\antigravity\scratch\diagrams\So_do_1_Ba_tang_khoan_muc_du_phong.png"
img2_path = r"C:\Users\Admin\.gemini\antigravity\scratch\diagrams\So_do_2_Quy_trinh_ung_pho_ngan_hang.png"
img3_path = r"C:\Users\Admin\.gemini\antigravity\scratch\diagrams\So_do_3_Co_che_Khoan_muc_3_Agribank_MB.png"

generate_docx(target_docx, img1_path, img2_path, img3_path)

# Generate Companion HTML
with open(img1_path, "rb") as f:
    b64_1 = base64.b64encode(f.read()).decode("utf-8")
with open(img2_path, "rb") as f:
    b64_2 = base64.b64encode(f.read()).decode("utf-8")
with open(img3_path, "rb") as f:
    b64_3 = base64.b64encode(f.read()).decode("utf-8")

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Chuyên đề: Quản trị Rủi ro Giải tỏa Mặt bằng & Khoản mục 3 (Agribank vs MBBank)</title>
<style>
  body {{ font-family: 'Times New Roman', Times, serif; line-height: 1.45; color: #111; background-color: #f7f9fa; margin: 0; padding: 25px; }}
  .container {{ max-width: 950px; margin: 0 auto; background: #fff; padding: 45px 55px; border-radius: 6px; box-shadow: 0 4px 16px rgba(0,0,0,0.08); }}
  .top-btn-bar {{ text-align: right; margin-bottom: 20px; }}
  .btn-copy {{ background: #002060; color: #fff; border: none; padding: 10px 18px; border-radius: 4px; font-weight: bold; cursor: pointer; }}
  .btn-copy:hover {{ background: #0F4C81; }}
  h1 {{ color: #002060; font-size: 19px; border-bottom: 2px solid #002060; padding-bottom: 5px; margin-top: 32px; text-transform: uppercase; }}
  h2 {{ color: #0F4C81; font-size: 15px; margin-top: 20px; }}
  .meta-header {{ text-align: center; margin-bottom: 22px; }}
  .uni-title {{ font-size: 14px; font-weight: bold; color: #505050; text-transform: uppercase; }}
  .doc-title {{ font-size: 21px; font-weight: bold; color: #C00000; margin: 10px 0; text-transform: uppercase; line-height: 1.3; }}
  .doc-sub {{ font-size: 13.5px; font-style: italic; color: #555; }}
  .callout-bluf {{ background-color: #F2F5F9; border-left: 5px solid #002060; padding: 14px 18px; margin: 18px 0; font-size: 13.5px; }}
  .callout-script {{ background-color: #F0F4F8; border-left: 5px solid #0F4C81; padding: 14px 18px; margin: 18px 0; font-size: 13.5px; }}
  .figure-box {{ text-align: center; margin: 24px 0; background: #FAFAFA; border: 1px solid #E5E5E5; padding: 16px; border-radius: 4px; }}
  .figure-box img {{ max-width: 100%; height: auto; border: 1px solid #DDD; border-radius: 3px; }}
  .figure-caption {{ font-weight: bold; font-size: 13px; color: #002060; margin-top: 8px; }}
  .figure-source {{ font-size: 12px; font-style: italic; color: #666; margin-top: 3px; }}
  table {{ width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 13px; }}
  th, td {{ border: 1px solid #CBD5E1; padding: 7px 10px; }}
  th {{ background-color: #002060; color: #fff; text-align: center; }}
  tr:nth-child(even) {{ background-color: #F8FAFC; }}
</style>
</head>
<body>
<div class="container" id="content-to-copy">
  <div class="top-btn-bar">
    <button class="btn-copy" onclick="copyDocument()">Sao chép toàn bộ để dán vào Google Docs</button>
  </div>
  <div class="meta-header">
    <div class="uni-title">Trường Đại học Kinh tế Quốc dân (NEU) — Viện Ngân hàng - Tài chính</div>
    <div style="font-size:12px; color:#666;">Chương trình Cao học Khóa 34 (Lớp K34_3_NH8) — Học phần: Quản trị Rủi ro</div>
    <div class="doc-title">BÁO CÁO NGHIỆP VỤ & GIẢI TRÌNH CHUYÊN SÂU:<br>HỆ THỐNG KHOẢN MỤC DỰ PHÒNG & MÔ HÌNH QUY TRÌNH ỨNG PHÓ KHI TSBĐ BỊ 'ĐÁNH ÚP' BỞI QUY HOẠCH HẠ TẦNG THẦN TỐC</div>
    <div class="doc-sub">Chuyên đề: Quản trị rủi ro khoản vay dính giải tỏa mặt bằng & Phân tích so sánh Agribank vs MBBank | Người thực hiện: Nhóm 2</div>
  </div>

  <div class="callout-bluf">
    <strong>TỔNG LUẬN ĐIỀU HÀNH (BOTTOM LINE UP FRONT - BLUF):</strong><br>
    1. <strong>Xác thực thực tế:</strong> Nhận định về hiện tượng người dân lẫn ngân hàng bị 'đánh úp' bởi các quyết sách hạ tầng triển khai thần tốc là HOÀN TOÀN CHUẨN XÁC 100%. Tại thời điểm cấp tín dụng, dữ liệu quy hoạch hoàn toàn là 'đất ở sạch', nhưng khi cơ chế đặc thù được phê duyệt, tài sản thế chấp bị thu hồi khẩn cấp.<br>
    2. <strong>Hệ thống Khoản mục Dự phòng chịu trách nhiệm:</strong> Gồm 3 tầng nấc: Tầng 1 (Dự phòng chung 0,75% P&L theo Thông tư 11); Tầng 2 (Management Overlay theo IFRS 9 trên P&L); Tầng 3 (Quỹ dự phòng tài chính 10% LNST và Đệm vốn kinh tế CAR 10-11% thuộc Vốn chủ sở hữu).<br>
    3. <strong>So sánh chuyên sâu Agribank vs MBBank:</strong> Cả hai ngân hàng đều trích 10% LNST vào Quỹ dự phòng tài chính. Tuy nhiên, MB liên tục chia cổ tức bằng cổ phiếu giúp vốn điều lệ tăng vọt lên 61.643 tỷ, nới trần quỹ lên 15.411 tỷ và sở hữu đệm CAR dày (+3% RWA); trong khi Agribank bị nghẽn trần quỹ nhiều năm ở mức 7.600-8.600 tỷ và đệm CAR mỏng (9,2%-10,2%), phụ thuộc nguồn cấp vốn từ Ngân sách Nhà nước.
  </div>

  <h1>1. XÁC THỰC THÔNG TIN & BỐI CẢNH QUẢN TRỊ RỦI RO ĐỘT XUẤT</h1>
  <p><strong>1.1. Hiện tượng 'Bị đánh úp quy hoạch' là hoàn toàn có thật trong kỷ nguyên mới:</strong></p>
  <p>• Dưới sự chỉ đạo quyết liệt của Tổng Bí thư Tô Lâm và Thủ tướng Chính phủ Phạm Minh Chính, chủ trương 'chỉ bàn làm, không bàn lùi' được quán triệt xuyên suốt. Hàng loạt đại dự án hạ tầng giao thông động lực quốc gia (Đường sắt tốc độ cao Bắc - Nam 67 tỷ USD, các tuyến đường sắt kết nối phía Bắc, mạng lưới cao tốc Bắc - Nam giai đoạn 2, đường Vành đai 4 Hà Nội, Vành đai 3 TP.HCM...) đều áp dụng cơ chế đặc thù được Quốc hội phê chuẩn: Tách công tác Bồi thường GPMB thành dự án độc lập làm trước; và cho phép điều chỉnh cục bộ quy hoạch khẩn cấp.</p>
  <p>• Tại thời điểm thẩm định tín dụng, cán bộ ngân hàng kiểm tra quy hoạch đều xác nhận là đất ở đô thị sạch. Khi hướng tuyến đại dự án được chốt và cắm mốc khẩn cấp, cả khách hàng vay vốn và ngân hàng thương mại đều rơi vào thế bị động hoàn toàn (Unanticipated Event Shock).</p>

  <h1>2. HỆ THỐNG 3 TẦNG KHOẢN MỤC DỰ PHÒNG CHỊU TRÁCH NHIỆM HẤP THỤ RỦI RO</h1>
  <div class="figure-box">
    <img src="data:image/png;base64,{b64_1}" alt="Sơ đồ 1. Mô hình 3 tầng khoản mục dự phòng">
    <div class="figure-caption">Sơ đồ 1. Mô hình 3 tầng khoản mục dự phòng hấp thụ rủi ro quy hoạch / giải tỏa đột xuất</div>
    <div class="figure-source">Nguồn: Nhóm 2 tổng hợp từ Thông tư 11/2021/TT-NHNN, Chuẩn mực IFRS 9 và Luật Các TCTD 2024.</div>
  </div>
  <p>• <strong>Tầng 1: Khoản mục DỰ PHÒNG CHUNG (0,75% dư nợ Nhóm 1–4):</strong> Chi phí hoạt động kinh doanh (P&L) theo Điều 7 Thông tư 11/2021/TT-NHNN. Túi đệm luật định cho các tổn thất 'chưa xác định được khi trích lập dự phòng cụ thể'.</p>
  <p>• <strong>Tầng 2: Khoản mục MANAGEMENT OVERLAY / PMA:</strong> Chi phí dự phòng bổ sung trên P&L theo chuẩn IFRS 9 ECL. Bù đắp 'điểm mù' của mô hình thống kê định lượng lịch sử trước các quyết định chính trị đột xuất.</p>
  <p>• <strong>Tầng 3: Khoản mục QUỸ DỰ PHÒNG TÀI CHÍNH & ĐỆM VỐN KINH TẾ (CAR):</strong> Thuộc Vốn Chủ Sở Hữu (Equity) theo Điều 149 Luật Các TCTD 2024 và Trụ cột 2 Basel II/III ICAAP. Hấp thụ phần tổn thất tài sản kinh doanh vượt quá khả năng của chi phí dự phòng P&L.</p>

  <h1>3. LÀM RÕ CƠ CHẾ KHOẢN MỤC 3: PHÂN TÍCH SO SÁNH AGRIBANK vs MBBANK</h1>
  <div class="figure-box">
    <img src="data:image/png;base64,{b64_3}" alt="Sơ đồ 3. Cơ chế trích lập & Vận hành Khoản mục 3: Agribank vs MBBank">
    <div class="figure-caption">Sơ đồ 3. Cơ chế trích lập & Vận hành Khoản mục 3 (Vốn chủ sở hữu): Agribank vs MBBank</div>
    <div class="figure-source">Nguồn: Xây dựng bởi Nhóm 2 từ Luật Các TCTD 2024, Nghị định 93/2017/NĐ-CP và BCTC kiểm toán 2020–2025.</div>
  </div>

  <table>
    <thead>
      <tr>
        <th style="width:34%;">Chỉ tiêu tài chính (tỷ đồng / %)</th>
        <th style="width:11%;">2020</th>
        <th style="width:11%;">2021</th>
        <th style="width:11%;">2022</th>
        <th style="width:11%;">2023</th>
        <th style="width:11%;">2024</th>
        <th style="width:11%;">2025</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:#EBF3FB; font-weight:bold;"><td colspan="7">[1] AGRIBANK (NHTM 100% VỐN NHÀ NƯỚC)</td></tr>
      <tr><td>- Lợi nhuận sau thuế (LNST Hợp nhất)</td><td align="center">10.517</td><td align="center">12.261</td><td align="center">18.043</td><td align="center">20.696</td><td align="center">22.067</td><td align="center">24.955</td></tr>
      <tr><td>- Số trích Quỹ dự phòng tài chính (10% LNST)</td><td align="center">1.052</td><td align="center">1.226</td><td align="center">1.804</td><td align="center">2.070</td><td align="center">2.207</td><td align="center">2.496</td></tr>
      <tr><td>- Vốn điều lệ cuối năm</td><td align="center">30.710</td><td align="center">34.328</td><td align="center">34.447</td><td align="center">41.269</td><td align="center">51.639</td><td align="center">51.639</td></tr>
      <tr><td>- Mức trần Quỹ tối đa luật định (25% VĐL)</td><td align="center">7.678</td><td align="center">8.582</td><td align="center">8.612</td><td align="center">10.317</td><td align="center">12.910</td><td align="center">12.910</td></tr>
      <tr><td>- Tổng Vốn chủ sở hữu (Hợp nhất)</td><td align="center">73.084</td><td align="center">76.087</td><td align="center">86.998</td><td align="center">100.536</td><td align="center">124.068</td><td align="center">131.191</td></tr>
      <tr><td>- Hệ số an toàn vốn CAR (TT 22 -> TT 41)</td><td align="center">10,58%</td><td align="center">10,50%</td><td align="center">10,80%</td><td align="center">9,20%</td><td align="center">11,36%</td><td align="center">10,22%</td></tr>
      <tr style="background:#EBF3FB; font-weight:bold;"><td colspan="7">[2] MBBANK (NHTMCP QUÂN ĐỘI)</td></tr>
      <tr><td>- Lợi nhuận sau thuế (LNST Hợp nhất)</td><td align="center">8.606</td><td align="center">13.221</td><td align="center">18.155</td><td align="center">21.054</td><td align="center">22.951</td><td align="center">27.383</td></tr>
      <tr><td>- Số trích Quỹ dự phòng tài chính (10% LNST)</td><td align="center">861</td><td align="center">1.322</td><td align="center">1.816</td><td align="center">2.105</td><td align="center">2.295</td><td align="center">2.738</td></tr>
      <tr><td>- Vốn điều lệ cuối năm</td><td align="center">27.988</td><td align="center">37.783</td><td align="center">45.340</td><td align="center">52.141</td><td align="center">61.643</td><td align="center">61.643</td></tr>
      <tr><td>- Mức trần Quỹ tối đa luật định (25% VĐL)</td><td align="center">6.997</td><td align="center">9.446</td><td align="center">11.335</td><td align="center">13.035</td><td align="center">15.411</td><td align="center">15.411</td></tr>
      <tr><td>- Tổng Vốn chủ sở hữu (Hợp nhất)</td><td align="center">50.099</td><td align="center">62.486</td><td align="center">79.613</td><td align="center">96.711</td><td align="center">117.060</td><td align="center">142.023</td></tr>
      <tr><td>- Hệ số an toàn vốn CAR (Thông tư 41)</td><td align="center">10,42%</td><td align="center">11,28%</td><td align="center">11,53%</td><td align="center">10,75%</td><td align="center">11,80%</td><td align="center">11,00%</td></tr>
    </tbody>
  </table>

  <p>• <strong>Nấc 1: Rút Quỹ dự phòng tài chính bù đắp tổn thất tài sản kinh doanh (Đ.149 Luật Các TCTD):</strong> Tại Agribank, HĐTV phải lập hồ sơ trình Thống đốc NHNN và Bộ Tài chính thẩm định phê duyệt để chứng minh nguyên nhân khách quan và bảo toàn vốn Nhà nước; tại MBBank, thẩm quyền thuộc về ĐHĐCĐ và được ủy quyền cho HĐQT xử lý thương mại linh hoạt.</p>
  <p>• <strong>Nấc 2: Hấp thụ vào Đệm Vốn kinh tế CAR (Trụ cột 2 Basel II/III):</strong> MBBank có đệm CAR dày dặn (+3% RWA), hấp thụ trọn vẹn cú sốc mà CAR vẫn trên 10%; trong khi Agribank có CAR mỏng (9,2%-10,2%), nếu chịu cú sốc lớn sẽ dễ chạm ngưỡng sàn 8% và phải chờ Nhà nước cấp bù ngân sách.</p>

  <h1>4. QUY TRÌNH 4 BƯỚC ỨNG PHÓ KẾ TOÁN & PHÁP LÝ KHI BỊ 'ĐÁNH ÚP' QUY HOẠCH</h1>
  <div class="figure-box">
    <img src="data:image/png;base64,{b64_2}" alt="Sơ đồ 2. Quy trình 4 bước ứng phó của Ngân hàng">
    <div class="figure-caption">Sơ đồ 2. Quy trình 4 bước ứng phó kế toán & pháp lý của Ngân hàng khi bị 'đánh úp' quy hoạch</div>
    <div class="figure-source">Nguồn: Xây dựng bởi Nhóm 2 từ quy trình quản trị rủi ro tín dụng và thu hồi nợ thực tế tại các NHTM Việt Nam.</div>
  </div>
  <p>• <strong>Bước 1: Cách ly & Giám sát đặc biệt (Watchlist):</strong> Quét tọa độ GIS / Core Banking, cách ly danh mục, dừng giải ngân hạn mức.</p>
  <p>• <strong>Bước 2: Tái định giá theo giá bồi thường dự kiến & Trích lập Dự phòng cụ thể:</strong> Cưỡng bức hạ định giá về V_GPMB, ép giá trị khấu trừ C = 50% GPMB, trích lập dự phòng cụ thể bổ sung trên P&L.</p>
  <p>• <strong>Bước 3: Ràng buộc hợp đồng (Covenants & Event of Default):</strong> Kích hoạt điều khoản vi phạm nghĩa vụ TSBĐ, yêu cầu khách hàng bổ sung TSBĐ khác hoặc nộp tiền mặt trả bớt nợ gốc trong 15–30 ngày.</p>
  <p>• <strong>Bước 4: Thu hồi tiền bồi thường trực tiếp & Xóa nợ nội bảng (Write-off):</strong> Đăng ký quyền thụ hưởng trực tiếp từ Kho bạc Nhà nước cấn trừ nợ gốc; phần thiếu hụt kích hoạt Quỹ dự phòng để Xóa nợ nội bảng (Write-off) và tiếp tục truy đòi ngoại bảng.</p>

  <h1>5. MA TRẬN ĐỐI CHIẾU CHUYÊN SÂU GIỮA AGRIBANK VÀ MBBANK</h1>
  <table>
    <thead>
      <tr>
        <th style="width:25%;">Tiêu chí so sánh</th>
        <th style="width:37%;">Agribank (NHTM 100% Vốn Nhà nước)</th>
        <th style="width:38%;">MBBank (NHTMCP Quân đội & Tư nhân)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>1. Cơ sở trích lập hàng năm</strong></td><td>Trích cứng 10% LNST theo NĐ 93/2017 & TT hướng dẫn của Bộ Tài chính.</td><td>Trích 10% LNST theo NĐ 93/2017 & Điều lệ tổ chức hoạt động của MB.</td></tr>
      <tr><td><strong>2. Mức trần Quỹ (25% VĐL)</strong></td><td>12.910 tỷ đồng (bị chặn trần bởi vốn ĐL 51.639 tỷ, trước 2023 chỉ 8.600 tỷ).</td><td>15.411 tỷ đồng (nới rộng liên tục theo đà tăng vốn ĐL lên 61.643 tỷ).</td></tr>
      <tr><td><strong>3. Cơ chế tăng vốn nới trần</strong></td><td>Bị động: Phụ thuộc vào Ngân sách Nhà nước & Nghị quyết phê chuẩn của Quốc hội.</td><td>Chủ động: Tự động hóa qua chia cổ tức bằng cổ phiếu từ lợi nhuận giữ lại.</td></tr>
      <tr><td><strong>4. Thẩm quyền quyết định dùng Quỹ</strong></td><td>HĐTV Agribank lập hồ sơ -> Trình NHNN và Bộ Tài chính phê duyệt.</td><td>ĐHĐCĐ ủy quyền cho Hội đồng Quản trị MBBank chủ động phê duyệt.</td></tr>
      <tr><td><strong>5. Trách nhiệm giải trình kiểm toán</strong></td><td>Rất nghiêm ngặt: Thanh tra NHNN, Kiểm toán Nhà nước, Thanh tra Chính phủ.</td><td>Kiểm toán độc lập Big 4 (KPMG) & Ban Kiểm soát theo chuẩn niêm yết.</td></tr>
      <tr><td><strong>6. Đệm Vốn kinh tế CAR dôi dư</strong></td><td>Mỏng: CAR 9,20% - 10,22% (chỉ dôi dư 1,2% - 2,2% RWA so với mức sàn 8%).</td><td>Dày dặn: CAR 10,75% - 11,80% (dôi dư 2,7% - 3,8% RWA so với mức sàn 8%).</td></tr>
      <tr><td><strong>7. Khả năng tự bù đắp cú sốc</strong></td><td>Chậm, phụ thuộc vào cơ chế phân bổ và hỗ trợ từ Ngân sách Nhà nước.</td><td>Rất nhanh nhờ ROE cao (20-25%/năm) và thị trường vốn đa kênh linh hoạt.</td></tr>
    </tbody>
  </table>

  <h1>6. KỊCH BẢN THUYẾT TRÌNH & TRẢ LỜI PHẢN BIỆN MẪU (SPEAKER SCRIPT)</h1>
  <div class="callout-script">
    <strong>LỜI THOẠI TRẢ LỜI SẮC BẢN DÀNH CHO BẠN KHI ĐƯỢC CHẤT VẤN TRÊN BỤC:</strong><br><br>
    'Kính thưa Thầy và các bạn, đây là một câu hỏi mang tính thời sự rất nóng bỏng phản ánh đúng thực tiễn điều hành hạ tầng thần tốc hiện nay!<br><br>
    Thứ nhất, việc người dân và ngân hàng bị 'đánh úp' quy hoạch là hoàn toàn có thật. Khi các đại dự án chiến lược được triển khai theo tinh thần 'chỉ bàn làm không bàn lùi' của Tổng Bí thư Tô Lâm, quy hoạch được điều chỉnh cục bộ khẩn cấp, hệ thống dữ liệu đất đai tại thời điểm cho vay 1-2 năm trước hoàn toàn không có thông tin.<br><br>
    Thứ hai, để đối phó với rủi ro này, hệ thống ngân hàng thiết lập sẵn 3 TẦNG KHOẢN MỤC CHUYÊN BIỆT:<br>
    1. Tầng 1 (Chi phí P&L): Khoản mục DỰ PHÒNG CHUNG (0,75% dư nợ) theo Thông tư 11 chính là khoản tiền luật định dành riêng cho những 'tổn thất chưa thể xác định được'.<br>
    2. Tầng 2 (Chuẩn mực quốc tế): Khoản mục MANAGEMENT OVERLAY theo IFRS 9 cho phép Ban Điều hành chủ động trích lập một cục dự phòng bổ sung vào P&L khi phát hiện hướng tuyến dự án đi qua khu vực cho vay.<br>
    3. Tầng 3 (Vốn chủ sở hữu): Nếu khoản lỗ vượt quá dự phòng, ngân hàng sẽ kích hoạt QUỸ DỰ PHÒNG TÀI CHÍNH (trích 10% LNST hàng năm) và ĐỆM VỐN KINH TẾ CAR (10-11%) để hấp thụ hoàn toàn tổn thất.<br><br>
    Thứ ba, sự phân hóa giữa Agribank và MBBank tại Khoản mục 3 thể hiện ở 2 điểm mấu chốt:<br>
    - MBBank có trần Quỹ dự phòng tài chính lên tới hơn 15.400 tỷ đồng và đệm CAR dày (+3% RWA), thẩm quyền xử lý do HĐQT linh hoạt quyết định và khả năng tự bù đắp cực nhanh nhờ ROE 20-25%.<br>
    - Trong khi đó, Agribank bị nghẽn trần quỹ ở mức 12.900 tỷ (trước 2023 chỉ 8.600 tỷ) do vốn điều lệ tăng chậm phụ thuộc ngân sách; việc rút quỹ bắt buộc phải trình qua NHNN và Bộ Tài chính phê duyệt; đồng thời đệm CAR mỏng (9,2%-10,2%) nên nếu chịu cú sốc lớn sẽ phải kiến nghị Nhà nước tiếp tục cấp bù vốn điều lệ.'
  </div>
</div>

<script>
function copyDocument() {{
  const el = document.getElementById('content-to-copy');
  const range = document.createRange();
  range.selectNode(el);
  window.getSelection().removeAllRanges();
  window.getSelection().addRange(range);
  try {{
    document.execCommand('copy');
    alert('Đã sao chép toàn bộ nội dung văn bản kèm định dạng thành công! Bạn chỉ cần mở Google Docs và nhấn Ctrl+V để dán.');
  }} catch (err) {{
    alert('Lỗi sao chép tự động: ' + err);
  }}
  window.getSelection().removeAllRanges();
}}
</script>
</body>
</html>
"""

with open(target_html, "w", encoding="utf-8") as f:
    f.write(html_content)
print("SUCCESSFULLY SAVED COMPANION HTML:", target_html)

# ----------------- ARCHIVE OLD DRAFTS -----------------
archive_dir = os.path.join(target_dir, "_Luu_tru_Ban_nhap_cu")
os.makedirs(archive_dir, exist_ok=True)

files_to_archive = [
    "New Text Document.txt",
    "Phan_tich_RRTD_Agribank_MB_2020-2025_v3 - Copy.xlsx",
    "Phan_tich_RRTD_Agribank_MB_2020-2025_v3_backup_truoc_bo_sung.xlsx",
    "Phan_tich_RRTD_Agribank_MB_2020-2025_v2.xlsx",
    "BCTC_Goc_Trich_Xuat_Agribank_MB_2020-2025.xlsx",
    "Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v2.docx",
    "Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v3.docx",
    "Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v4.docx",
    "Bao_cao_Soat_lai_Feedback_Agribank_MB_v4_Hoan_Tat.docx",
    "Bao_cao_Soat_xet_Agribank_MB_v5.docx",
    "Quan_tri_Rui_ro_Khoan_vay_Dinh_Giai_toa_Mat_bang.docx",
    "Quan_tri_Rui_ro_Khoan_vay_Dinh_Giai_toa_Mat_bang.html"
]

archived_count = 0
for fname in files_to_archive:
    src_path = os.path.join(target_dir, fname)
    if os.path.exists(src_path):
        dst_path = os.path.join(archive_dir, fname)
        shutil.move(src_path, dst_path)
        archived_count += 1
        print(f"Moved draft to archive: {fname}")

print(f"Archived {archived_count} obsolete draft files successfully.")
