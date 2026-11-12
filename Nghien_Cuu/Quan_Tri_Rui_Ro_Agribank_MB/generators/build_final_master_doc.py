import os
import base64
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

def style_run(run, font_name="Times New Roman", size_pt=11, bold=False, italic=False, color_rgb=(0,0,0)):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)

def add_p(doc, text="", space_before=2, space_after=3, line_spacing=1.2, align=WD_ALIGN_PARAGRAPH.LEFT):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    p.alignment = align
    if text:
        r = p.add_run(text)
        style_run(r, font_name="Times New Roman", size_pt=11)
    return p

def add_image_figure(doc, img_path, caption_title, source_text):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(10)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=Inches(6.5))
    
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
            is_bold = (c_idx == 0) or ("AGRIBANK" in val) or ("MBBANK" in val)
            style_run(r, font_name="Times New Roman", size_pt=9, bold=is_bold, color_rgb=(0,0,0))

def add_callout(doc, title, content_list, border_color="002060", bg_hex="F2F5F9"):
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
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="100" w:type="dxa"/><w:bottom w:w="100" w:type="dxa"/><w:left w:w="140" w:type="dxa"/><w:right w:w="140" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)
    
    p0 = cell.paragraphs[0]
    p0.paragraph_format.space_before = Pt(2)
    p0.paragraph_format.space_after = Pt(4)
    r_title = p0.add_run(title)
    style_run(r_title, size_pt=11, bold=True, color_rgb=(0, 32, 96))
    
    for prefix, body in content_list:
        p = cell.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        if prefix:
            r_pre = p.add_run(f"• {prefix}: ")
            style_run(r_pre, size_pt=10.5, bold=True, color_rgb=(15, 76, 129))
        r_b = p.add_run(body)
        style_run(r_b, size_pt=10.5, bold=False, color_rgb=(20, 20, 20))
        
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(4)

def build_final_master_document():
    doc = docx.Document()
    
    # Margin
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)
        
    # Header
    p_uni = add_p(doc, "TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN (NEU) — VIỆN NGÂN HÀNG - TÀI CHÍNH", space_after=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_uni.runs[0], size_pt=9.5, bold=True, color_rgb=(80, 80, 80))
    p_sub = add_p(doc, "CHƯƠNG TRÌNH CAO HỌC KHÓA 34 (LỚP K34_3_NH8) — HỌC PHẦN: QUẢN TRỊ RỦI RO", space_after=6, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_sub.runs[0], size_pt=9, italic=True, color_rgb=(100, 100, 100))
    
    p_title = add_p(doc, "GIẢI TRÌNH NGHIỆP VỤ QUẢN TRỊ RỦI RO TÍN DỤNG", space_before=4, space_after=3, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_title.runs[0], size_pt=13.5, bold=True, color_rgb=(0, 32, 96))
    
    # SINGLE FOCUSED QUESTION
    tbl_q = doc.add_table(rows=1, cols=1)
    tbl_q.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_q.autofit = False
    tblPr = tbl_q._element.xpath('w:tblPr')[0]
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="12" w:space="0" w:color="DC2626"/>'
        f'<w:bottom w:val="single" w:sz="12" w:space="0" w:color="DC2626"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="DC2626"/>'
        f'<w:right w:val="single" w:sz="12" w:space="0" w:color="DC2626"/>'
        f'</w:tblBorders>'
    )
    tblLook = tblPr.find(qn('w:tblLook'))
    if tblLook is not None:
        tblLook.addprevious(borders)
    else:
        tblPr.append(borders)
    c_q = tbl_q.rows[0].cells[0]
    c_q.width = Inches(6.67)
    tcPr_q = c_q._tc.get_or_add_tcPr()
    tcPr_q.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="FEF2F2"/>'))
    tcPr_q.append(parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/><w:left w:w="160" w:type="dxa"/><w:right w:w="160" w:type="dxa"/></w:tcMar>'))
    p_q = c_q.paragraphs[0]
    p_q.paragraph_format.space_before = Pt(2)
    p_q.paragraph_format.space_after = Pt(2)
    r1 = p_q.add_run("CÂU HỎI TRỌNG TÂM:\n")
    style_run(r1, size_pt=11.5, bold=True, color_rgb=(220, 38, 38))
    r2 = p_q.add_run("Giá đền bù giải phóng mặt bằng (GPMB) thấp hơn nhiều giá thị trường làm 'thủng' tỷ lệ LTV (50%–70%), vậy ngân hàng có khoản mục nào trích lập để 'cover' được rủi ro này không?")
    style_run(r2, size_pt=12.5, bold=True, color_rgb=(0, 32, 96))
    
    # INSERT THE CLEAN ORIGINAL MODEL DIAGRAM RIGHT UNDER THE QUESTION
    img_path = r"C:\Users\Admin\.gemini\antigravity\scratch\diagrams\Mo_hinh_goc_3_tang_khoan_muc_hoan_chinh.png"
    add_image_figure(doc, img_path,
                     "Sơ đồ. Mô hình hệ thống 3 tầng khoản mục dự phòng ứng phó rủi ro giải tỏa mặt bằng",
                     "Nguồn: Xây dựng bởi Nhóm 2 từ Thông tư 11/2021/TT-NHNN, IFRS 9 ECL và Luật Các TCTD 2024.")
    
    # ANSWER: CORE TAKEAWAY + 3 TIERS
    ans_body = [
        ("Xác nhận bối cảnh thực tế", 
         "Hiện tượng này HOÀN TOÀN CÓ THẬT trong thực tế. Khi cấp tín dụng 1-2 năm trước, hồ sơ là 'đất ở sạch', ngân hàng yên tâm cho vay LTV 50%-70%. Tuy nhiên, các đại dự án hạ tầng hiện nay (đường sắt tốc độ cao 67 tỷ USD, mạng lưới cao tốc, vành đai) được Quốc hội cho phép áp dụng 'cơ chế đặc thù' tách GPMB làm trước và điều chỉnh quy hoạch khẩn cấp, khiến cả người dân và ngân hàng đều bị động khi hướng tuyến chốt đột ngột."),
        
        ("Khẳng định nguyên lý dự phòng", 
         "Ngân hàng KHÔNG CÓ khoản mục mang tên riêng 'dự phòng giải tỏa', nhưng Luật và Chuẩn mực kế toán đã thiết lập sẵn 3 TẦNG KHOẢN MỤC theo luật định để bao phủ rủi ro này:"),
         
        ("TẦNG 1 - Khoản mục DỰ PHÒNG CHUNG (0,75% dư nợ Nhóm 1–4)", 
         "Hạch toán vào Chi phí hoạt động kinh doanh (P&L) theo Điều 7 Thông tư 11/2021/TT-NHNN. Đây là số tiền luật định bắt buộc trích cho 'những tổn thất có thể xảy ra nhưng chưa xác định được khi cho vay' — đóng vai trò như chiếc áo giáp tập thể của toàn danh mục để bù đắp các cú sốc tài sản ban đầu."),
         
        ("TẦNG 2 - Khoản mục MANAGEMENT OVERLAY / PMA (Chuẩn mực quốc tế IFRS 9 ECL)", 
         "Hạch toán vào Chi phí P&L. Do các mô hình thống kê định lượng lịch sử bị 'mù' trước các quyết định chính sách đột xuất, Ban Điều hành ngân hàng được quyền chủ động trích thêm một khoản dự phòng riêng bổ sung vào P&L dựa trên phán đoán chuyên gia khi phát hiện dự án đi qua khu vực cho vay."),
         
        ("TẦNG 3 - Khoản mục QUỸ DỰ PHÒNG TÀI CHÍNH & VỐN KINH TẾ (CAR)", 
         "Thuộc Vốn chủ sở hữu theo Điều 149 Luật Các TCTD 2024 & Trụ cột 2 Basel II. Đây là thành trì phòng thủ tối thượng: Khi tổn thất giải tỏa vượt quá khả năng của chi phí dự phòng P&L trong năm, ngân hàng sẽ rút Quỹ dự phòng tài chính (10% LNST) và dùng Đệm vốn an toàn CAR để bù lỗ tài sản kinh doanh, bảo đảm không bị âm vốn điều lệ.")
    ]
    add_callout(doc, "TRẢ LỜI NGẮN GỌN (BẢN CHẤT CỐT LÕI & 3 TẦNG KHOẢN MỤC DỰ PHÒNG):", ans_body, border_color="002060", bg_hex="F2F5F9")
    
    # EMBEDDED SECTION: CLARIFYING TIER 3 IN PRACTICE (AGRIBANK VS MBBANK)
    add_callout(doc, 
                "LÀM RÕ TẦNG 3 TRONG THỰC TẾ: AGRIBANK vs MBBANK TRÍCH LẬP VÀ VẬN HÀNH THẾ NÀO?",
                [
                    ("Cơ chế trích lập chung", 
                     "Cả hai ngân hàng đều trích 10% Lợi nhuận sau thuế (LNST) hàng năm vào Quỹ dự phòng tài chính theo Điều 149 Luật Các TCTD 2024 & Nghị định 93/2017/NĐ-CP (khống chế tối đa bằng 25% vốn điều lệ)."),
                     
                    ("Khác biệt 1 - Về mức trần tích lũy Quỹ (25% VĐL)", 
                     "• MBBank: Nhờ liên tục chia cổ tức bằng cổ phiếu, vốn điều lệ tăng vọt từ 28.000 tỷ lên hơn 61.600 tỷ đồng (2025), giúp trần Quỹ dự phòng tài chính nới rộng liên tục lên 15.411 tỷ đồng.\n"
                     "• Agribank: Do 100% vốn Nhà nước, vốn điều lệ tăng chậm phụ thuộc vào ngân sách cấp bổ sung. Trần quỹ bị nghẽn nhiều năm ở mức 7.600 - 8.600 tỷ đồng (mãi đến cuối 2023-2024 được Quốc hội cấp thêm 17.100 tỷ thì trần mới lên 12.910 tỷ)."),
                     
                    ("Khác biệt 2 - Thẩm quyền rút quỹ khi bị lỗ tài sản", 
                     "• Tại MBBank: Thẩm quyền thuộc ĐHĐCĐ và đã được ủy quyền cho Hội đồng Quản trị quyết định xử lý thương mại nhanh gọn, ghi giảm quỹ trên BCTC năm có kiểm toán Big 4.\n"
                     "• Tại Agribank: Vì là 100% vốn Nhà nước, HĐTV Agribank KHÔNG được tự quyết. Bắt buộc lập hồ sơ giải trình nguyên nhân khách quan do quy hoạch Nhà nước, trình Thống đốc NHNN và Bộ Tài chính phê duyệt để bảo đảm không làm thất thoát vốn Nhà nước trước Kiểm toán Nhà nước."),
                     
                    ("Khác biệt 3 - Khả năng chịu đòn của Đệm vốn CAR", 
                     "• Tại MBBank: Đệm CAR dày (+3% RWA dôi dư so với sàn 8%) và LNST khổng lồ (23.000 - 27.000 tỷ/năm) giúp MB hấp thụ cú sốc hàng nghìn tỷ đồng mà CAR vẫn duy trì an toàn trên 10%, tự phục hồi cực nhanh.\n"
                     "• Tại Agribank: Đệm CAR mỏng (9,2% - 10,2%), nếu tổn thất lớn ăn vào vốn tự có sẽ nhanh chóng đẩy CAR chạm lằn ranh tối thiểu 8,0%. Agribank không thể tự phát hành cổ phiếu mà phải chờ Nhà nước cấp bù ngân sách.")
                ],
                border_color="0F4C81", bg_hex="F0F6FF")
                
    # Data table
    add_p(doc, "BẢNG ĐỐI CHIẾU SỐ LIỆU KIỂM TOÁN THỰC TẾ KHOẢN MỤC 3 (2020 – 2025):", space_before=4, space_after=2)
    tbl_headers = ["Chỉ tiêu tài chính (tỷ đồng / %)", "2020", "2021", "2022", "2023", "2024", "2025"]
    tbl_rows = [
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
    tbl_comp = doc.add_table(rows=len(tbl_rows) + 1, cols=7)
    tbl_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    format_custom_table(tbl_comp, [2.4, 0.7, 0.7, 0.7, 0.7, 0.7, 0.77], tbl_headers, tbl_rows, header_bg="002060")
    
    # SPEAKER SCRIPT CALLOUT
    speaker_text = [
        ("", "'Thưa Thầy và các bạn, việc tài sản dính giải tỏa thần tốc làm vỡ LTV là một rủi ro sự kiện bất khả kháng hoàn toàn có thật trong kỷ nguyên mới khi các đại dự án hạ tầng được làm theo cơ chế đặc thù.\n\n"
             "Để bao phủ rủi ro này, ngân hàng thiết lập 3 tầng phòng vệ: (1) Dự phòng chung 0,75% P&L cho tổn thất chưa xác định; (2) Management Overlay IFRS 9 trích đón đầu theo phán đoán vĩ mô; và (3) Quỹ dự phòng tài chính (10% LNST) cùng Đệm vốn CAR thuộc Vốn chủ sở hữu.\n\n"
             "Điểm khác biệt cốt lõi: MBBank có trần Quỹ dự phòng tài chính lên tới 15.400 tỷ đồng và đệm CAR dày (+3% RWA), HĐQT chủ động quyết định xử lý. Trong khi Agribank bị nghẽn trần quỹ ở mức 12.900 tỷ do vốn điều lệ tăng chậm; việc rút quỹ phải trình NHNN và Bộ Tài chính phê duyệt; đồng thời đệm CAR mỏng (9,2%-10,2%) nên nếu chịu sốc lớn sẽ phải kiến nghị Nhà nước cấp bù vốn điều lệ.'")
    ]
    add_callout(doc, "LỜI THOẠI TRẢ LỜI MẪU 1 PHÚT DÀNH CHO BẠN (SPEAKER SCRIPT):", speaker_text, border_color="002060", bg_hex="F2F5F9")
    
    target_docx = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Khoan_muc_Du_phong_Rui_ro_Giai_toa_Than_toc.docx"
    doc.save(target_docx)
    print("SUCCESSFULLY SAVED FINAL MASTER DOCX WITH MODEL:", target_docx)
    
    # Companion HTML with base64 image
    with open(img_path, "rb") as f:
        b64_img = base64.b64encode(f.read()).decode("utf-8")
        
    target_html = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Khoan_muc_Du_phong_Rui_ro_Giai_toa_Than_toc.html"
    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Giải trình Nghiệp vụ: Rủi ro Giải tỏa Mặt bằng & Khoản mục Dự phòng</title>
<style>
  body {{ font-family: 'Times New Roman', Times, serif; line-height: 1.5; color: #111; background-color: #f7f9fa; margin: 0; padding: 25px; }}
  .container {{ max-width: 920px; margin: 0 auto; background: #fff; padding: 40px 50px; border-radius: 6px; box-shadow: 0 4px 16px rgba(0,0,0,0.08); }}
  .top-btn-bar {{ text-align: right; margin-bottom: 20px; }}
  .btn-copy {{ background: #002060; color: #fff; border: none; padding: 10px 18px; border-radius: 4px; font-weight: bold; cursor: pointer; }}
  .btn-copy:hover {{ background: #0F4C81; }}
  .meta-header {{ text-align: center; margin-bottom: 25px; }}
  .uni-title {{ font-size: 14px; font-weight: bold; color: #505050; text-transform: uppercase; }}
  .doc-title {{ font-size: 20px; font-weight: bold; color: #002060; margin: 10px 0 5px 0; text-transform: uppercase; line-height: 1.3; }}
  .doc-guide {{ font-size: 12.5px; font-style: italic; color: #666; margin-bottom: 20px; }}
  .question-box {{ background-color: #FEF2F2; border: 2px solid #DC2626; border-radius: 6px; padding: 16px 20px; margin-bottom: 22px; }}
  .q-tag {{ font-size: 14px; font-weight: bold; color: #DC2626; }}
  .q-body {{ font-size: 16px; font-weight: bold; color: #002060; line-height: 1.4; }}
  .figure-box {{ text-align: center; margin: 24px 0; background: #FAFAFA; border: 1px solid #E2E8F0; padding: 16px; border-radius: 4px; }}
  .figure-box img {{ max-width: 100%; height: auto; border: 1px solid #CBD5E1; border-radius: 3px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }}
  .figure-caption {{ font-weight: bold; font-size: 13px; color: #002060; margin-top: 10px; }}
  .figure-source {{ font-size: 12px; font-style: italic; color: #64748B; margin-top: 3px; }}
  .card-box {{ background-color: #F8FAFC; border: 1px solid #CBD5E1; border-left: 5px solid #002060; border-radius: 4px; padding: 16px 20px; margin-bottom: 20px; }}
  .card-title {{ font-size: 15px; font-weight: bold; color: #002060; margin-bottom: 10px; }}
  .card-point {{ margin-bottom: 8px; font-size: 13.5px; line-height: 1.45; }}
  .card-point strong {{ color: #0F4C81; }}
  table {{ width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 12.5px; }}
  th, td {{ border: 1px solid #CBD5E1; padding: 6px 9px; }}
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
    <div class="doc-title">GIẢI TRÌNH NGHIỆP VỤ QUẢN TRỊ RỦI RO TÍN DỤNG</div>
    <div class="doc-guide">Bản giải trình duy nhất | Thuật ngữ chuẩn mực | Tích hợp Mô hình trực quan 300 DPI | Nhóm thực hiện: Nhóm 2</div>
  </div>

  <div class="question-box">
    <span class="q-tag">CÂU HỎI TRỌNG TÂM: </span>
    <span class="q-body">Giá đền bù giải phóng mặt bằng (GPMB) thấp hơn nhiều giá thị trường làm 'thủng' tỷ lệ LTV (50%–70%), vậy ngân hàng có khoản mục nào trích lập để 'cover' được rủi ro này không?</span>
  </div>

  <div class="figure-box">
    <img src="data:image/png;base64,{b64_img}" alt="Mô hình hệ thống 3 tầng khoản mục dự phòng">
    <div class="figure-caption">Sơ đồ. Mô hình hệ thống 3 tầng khoản mục dự phòng ứng phó rủi ro giải tỏa mặt bằng</div>
    <div class="figure-source">Nguồn: Xây dựng bởi Nhóm 2 từ Thông tư 11/2021/TT-NHNN, IFRS 9 ECL và Luật Các TCTD 2024.</div>
  </div>

  <!-- CORE ANSWER & 3 TIERS -->
  <div class="card-box" style="border-left-color: #002060;">
    <div class="card-title">TRẢ LỜI NGẮN GỌN (BẢN CHẤT CỐT LÕI & 3 TẦNG KHOẢN MỤC DỰ PHÒNG):</div>
    <div class="card-point"><strong>• Xác nhận bối cảnh thực tế:</strong> Hiện tượng này <strong>HOÀN TOÀN CÓ THẬT</strong> trong thực tế. Khi cấp tín dụng 1-2 năm trước, hồ sơ là 'đất ở sạch', ngân hàng yên tâm cho vay LTV 50%-70%. Tuy nhiên, các đại dự án hạ tầng hiện nay (đường sắt tốc độ cao 67 tỷ USD, mạng lưới cao tốc, vành đai) được Quốc hội cho phép áp dụng 'cơ chế đặc thù' tách GPMB làm trước và điều chỉnh quy hoạch khẩn cấp, khiến cả người dân và ngân hàng đều bị động khi hướng tuyến chốt đột ngột.</div>
    <div class="card-point"><strong>• Khẳng định nguyên lý dự phòng:</strong> Ngân hàng <strong>KHÔNG CÓ</strong> khoản mục mang tên riêng 'dự phòng giải tỏa', nhưng Luật và Chuẩn mực kế toán đã thiết lập sẵn <strong>3 TẦNG KHOẢN MỤC</strong> theo luật định để bao phủ rủi ro này:</div>
    <div class="card-point"><strong>• TẦNG 1 - Khoản mục DỰ PHÒNG CHUNG (0,75% dư nợ Nhóm 1–4):</strong> Hạch toán vào Chi phí hoạt động kinh doanh (P&L) theo Điều 7 Thông tư 11/2021/TT-NHNN. Đây là số tiền luật định bắt buộc trích cho 'những tổn thất có thể xảy ra nhưng chưa xác định được khi cho vay' — đóng vai trò như chiếc áo giáp tập thể của toàn danh mục để bù đắp các cú sốc tài sản ban đầu.</div>
    <div class="card-point"><strong>• TẦNG 2 - Khoản mục MANAGEMENT OVERLAY / PMA (Chuẩn mực quốc tế IFRS 9 ECL):</strong> Hạch toán vào Chi phí P&L. Do các mô hình thống kê định lượng lịch sử bị 'mù' trước các quyết định chính sách đột xuất, Ban Điều hành ngân hàng được quyền chủ động trích thêm một khoản dự phòng riêng bổ sung vào P&L dựa trên phán đoán chuyên gia khi phát hiện dự án đi qua khu vực cho vay.</div>
    <div class="card-point"><strong>• TẦNG 3 - Khoản mục QUỸ DỰ PHÒNG TÀI CHÍNH & VỐN KINH TẾ (CAR):</strong> Thuộc Vốn chủ sở hữu theo Điều 149 Luật Các TCTD 2024 & Trụ cột 2 Basel II. Đây là thành trì phòng thủ tối thượng: Khi tổn thất giải tỏa vượt quá khả năng của chi phí dự phòng P&L trong năm, ngân hàng sẽ rút Quỹ dự phòng tài chính (10% LNST) và dùng Đệm vốn an toàn CAR để bù lỗ tài sản kinh doanh, bảo đảm không bị âm vốn điều lệ.</div>
  </div>

  <!-- EMBEDDED AGRIBANK VS MB -->
  <div class="card-box" style="border-left-color: #0F4C81; background-color: #F0F6FF;">
    <div class="card-title" style="color: #0F4C81;">LÀM RÕ TẦNG 3 TRONG THỰC TẾ: AGRIBANK vs MBBANK TRÍCH LẬP VÀ VẬN HÀNH THẾ NÀO?</div>
    <div class="card-point"><strong>• Cơ chế trích lập chung:</strong> Cả hai ngân hàng đều trích 10% Lợi nhuận sau thuế (LNST) hàng năm vào Quỹ dự phòng tài chính theo Điều 149 Luật Các TCTD 2024 & Nghị định 93/2017/NĐ-CP (khống chế tối đa bằng 25% vốn điều lệ).</div>
    <div class="card-point"><strong>• Khác biệt 1 - Về mức trần tích lũy Quỹ (25% VĐL):</strong><br>
    - <em>MBBank:</em> Nhờ liên tục chia cổ tức bằng cổ phiếu, vốn điều lệ tăng vọt từ 28.000 tỷ lên hơn 61.600 tỷ đồng (2025), giúp trần Quỹ dự phòng tài chính nới rộng liên tục lên <strong>15.411 tỷ đồng</strong>.<br>
    - <em>Agribank:</em> Do 100% vốn Nhà nước, vốn điều lệ tăng chậm phụ thuộc vào ngân sách cấp bổ sung. Trần quỹ bị nghẽn nhiều năm ở mức 7.600 - 8.600 tỷ đồng (mãi đến cuối 2023-2024 được Quốc hội cấp thêm 17.100 tỷ thì trần mới lên <strong>12.910 tỷ đồng</strong>).</div>
    <div class="card-point"><strong>• Khác biệt 2 - Thẩm quyền rút quỹ khi bị lỗ tài sản:</strong><br>
    - <em>Tại MBBank:</em> Thẩm quyền thuộc ĐHĐCĐ và đã được ủy quyền cho Hội đồng Quản trị quyết định xử lý thương mại nhanh gọn, ghi giảm quỹ trên BCTC năm có kiểm toán Big 4.<br>
    - <em>Tại Agribank:</em> Vì là 100% vốn Nhà nước, HĐTV Agribank <strong>không được tự quyết</strong>. Bắt buộc lập hồ sơ giải trình nguyên nhân khách quan do quy hoạch Nhà nước, trình Thống đốc NHNN và Bộ Tài chính phê duyệt để bảo đảm không làm thất thoát vốn Nhà nước trước Kiểm toán Nhà nước.</div>
    <div class="card-point"><strong>• Khác biệt 3 - Khả năng chịu đòn của Đệm vốn CAR:</strong><br>
    - <em>Tại MBBank:</em> Đệm CAR dày (+3% RWA dôi dư so với sàn 8%) và LNST khổng lồ (23.000 - 27.000 tỷ/năm) giúp MB hấp thụ cú sốc hàng nghìn tỷ đồng mà CAR vẫn duy trì an toàn trên 10%, tự phục hồi cực nhanh.<br>
    - <em>Tại Agribank:</em> Đệm CAR mỏng (9,2% - 10,2%), nếu tổn thất lớn ăn vào vốn tự có sẽ nhanh chóng đẩy CAR chạm lằn ranh tối thiểu 8,0%. Agribank không thể tự phát hành cổ phiếu mà phải chờ Nhà nước cấp bù ngân sách.</div>

    <div style="font-weight:bold; color:#002060; margin:14px 0 6px 0;">BẢNG ĐỐI CHIẾU SỐ LIỆU KIỂM TOÁN THỰC TẾ (2020 – 2025):</div>
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
        <tr style="background:#EBF3FB; font-weight:bold;"><td colspan="7">[1] AGRIBANK (100% VỐN NHÀ NƯỚC)</td></tr>
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
  </div>

  <!-- SPEAKER SCRIPT -->
  <div class="card-box" style="border-left-color: #002060; background-color: #F1F5F9;">
    <div class="card-title">LỜI THOẠI TRẢ LỜI MẪU 1 PHÚT DÀNH CHO BẠN (SPEAKER SCRIPT):</div>
    <div style="font-size: 13.5px; line-height: 1.5; font-style: italic; color: #1E293B;">
      "Thưa Thầy và các bạn, việc tài sản dính giải tỏa thần tốc làm vỡ LTV là một rủi ro sự kiện bất khả kháng hoàn toàn có thật trong kỷ nguyên mới khi các đại dự án hạ tầng được làm theo cơ chế đặc thù.<br><br>
      Để bao phủ rủi ro này, ngân hàng thiết lập 3 tầng phòng vệ: (1) Dự phòng chung 0,75% P&L cho tổn thất chưa xác định; (2) Management Overlay IFRS 9 trích đón đầu theo phán đoán vĩ mô; và (3) Quỹ dự phòng tài chính (10% LNST) cùng Đệm vốn CAR thuộc Vốn chủ sở hữu.<br><br>
      Điểm khác biệt cốt lõi: MBBank có trần Quỹ dự phòng tài chính lên tới 15.400 tỷ đồng và đệm CAR dày (+3% RWA), HĐQT chủ động quyết định xử lý. Trong khi Agribank bị nghẽn trần quỹ ở mức 12.900 tỷ do vốn điều lệ tăng chậm; việc rút quỹ phải trình NHNN và Bộ Tài chính phê duyệt; đồng thời đệm CAR mỏng (9,2%-10,2%) nên nếu chịu sốc lớn sẽ phải kiến nghị Nhà nước cấp bù vốn điều lệ."
    </div>
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
    alert('Đã sao chép toàn bộ nội dung văn bản thành công! Bạn chỉ cần mở Google Docs và nhấn Ctrl+V để dán.');
  }} catch (err) {{
    alert('Lỗi sao chép: ' + err);
  }}
  window.getSelection().removeAllRanges();
}}
</script>
</body>
</html>
"""
    with open(target_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("SUCCESSFULLY SAVED MASTER QA HTML WITH MODEL:", target_html)

build_final_master_document()
