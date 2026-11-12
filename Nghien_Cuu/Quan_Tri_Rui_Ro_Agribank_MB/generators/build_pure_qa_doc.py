import os
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

def add_question(doc, q_num, q_title, q_context=""):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    
    r_tag = p.add_run(f"CÂU HỎI {q_num}: ")
    style_run(r_tag, size_pt=12, bold=True, color_rgb=(192, 0, 0))
    
    r_title = p.add_run(q_title)
    style_run(r_title, size_pt=12, bold=True, color_rgb=(0, 32, 96))
    
    if q_context:
        p_sub = doc.add_paragraph()
        p_sub.paragraph_format.space_before = Pt(0)
        p_sub.paragraph_format.space_after = Pt(4)
        p_sub.paragraph_format.keep_with_next = True
        r_ctx = p_sub.add_run(f"Bối cảnh: {q_context}")
        style_run(r_ctx, size_pt=10, italic=True, color_rgb=(100, 100, 100))

def add_answer_box(doc, core_answer, detailed_points):
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
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F2F5F9"/>')
    tcPr.append(shd)
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="100" w:type="dxa"/><w:bottom w:w="100" w:type="dxa"/><w:left w:w="140" w:type="dxa"/><w:right w:w="140" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)
    
    # Core answer
    p0 = cell.paragraphs[0]
    p0.paragraph_format.space_before = Pt(2)
    p0.paragraph_format.space_after = Pt(4)
    p0.paragraph_format.line_spacing = 1.2
    r_ans_tag = p0.add_run("TRẢ LỜI NGẮN GỌN (BẢN CHẤT CỐT LÕI):\n")
    style_run(r_ans_tag, size_pt=10.5, bold=True, color_rgb=(0, 32, 96))
    r_ans_core = p0.add_run(core_answer)
    style_run(r_ans_core, size_pt=11, bold=True, color_rgb=(192, 0, 0))
    
    # Detailed bullet points
    for pt_title, pt_desc in detailed_points:
        p = cell.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        
        r_bullet = p.add_run(f"• {pt_title}: ")
        style_run(r_bullet, size_pt=10.5, bold=True, color_rgb=(15, 76, 129))
        
        r_desc = p.add_run(pt_desc)
        style_run(r_desc, size_pt=10.5, bold=False, color_rgb=(20, 20, 20))
        
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(4)

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

def build_qa_document():
    doc = docx.Document()
    
    # Margin setup
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
    
    # Document Title
    p_title = add_p(doc, "BẢN HỎI - ĐÁP CHUYÊN NGÀNH QUẢN TRỊ RỦI RO TÍN DỤNG", space_before=4, space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_title.runs[0], size_pt=14, bold=True, color_rgb=(0, 32, 96))
    p_sub_title = add_p(doc, "ỨNG PHÓ RỦI RO QUY HOẠCH GIẢI TỎA MẶT BẰNG & CƠ CHẾ KHOẢN MỤC 3 DỰ PHÒNG TÀI CHÍNH (AGRIBANK vs MBBANK)", space_before=1, space_after=6, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_sub_title.runs[0], size_pt=11.5, bold=True, color_rgb=(192, 0, 0))
    
    p_guide = add_p(doc, "Hình thức trình bày: Hỏi và Trả lời trực tiếp | Thuật ngữ chuẩn mực | Dễ hiểu, không phức tạp hóa | Nhóm thực hiện: Nhóm 2", space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    style_run(p_guide.runs[0], size_pt=9.5, italic=True, color_rgb=(80, 80, 80))
    
    # Q1
    add_question(doc, 1, 
                 "Thông tin người dân và ngân hàng bị 'đánh úp' bởi các quyết định quy hoạch hạ tầng thần tốc có chính xác không?",
                 "Các dự án hạ tầng lớn triển khai quyết liệt theo chỉ đạo mới, không có dữ liệu quy hoạch từ trước.")
    add_answer_box(doc, 
                   "HOÀN TOÀN CHÍNH XÁC 100%. Cả người vay và ngân hàng đều rơi vào thế bị động hoàn toàn.",
                   [
                       ("Cơ chế giải thích dễ hiểu", "Khi cấp tín dụng 1-2 năm trước, ngân hàng tra cứu tại Sở Tài nguyên & Môi trường thì đây là 'đất ở sạch', hợp pháp 100%, nên tự tin giải ngân 50%-70% giá trị."),
                       ("Yếu tố 'thần tốc'", "Hiện nay, các đại dự án chiến lược (Đường sắt tốc độ cao 67 tỷ USD, mạng lưới cao tốc, vành đai) được Quốc hội cho phép áp dụng 'cơ chế đặc thù': tách riêng giải phóng mặt bằng làm trước và điều chỉnh cục bộ quy hoạch khẩn cấp."),
                       ("Hệ quả pháp lý & tài chính", "Hướng tuyến chốt đến đâu, cắm mốc giải tỏa đến đó. Ngân hàng và khách hàng hoàn toàn không được biết trước trong dữ liệu lịch sử.")
                   ])
                   
    # Q2
    add_question(doc, 2, 
                 "Giá đền bù thấp hơn nhiều giá thị trường làm 'thủng' tỷ lệ LTV (50%-70%), vậy ngân hàng có khoản mục nào trích lập để 'cover' được rủi ro này không?",
                 "Bất động sản thế chấp bị giải tỏa với giá đền bù thấp, không đủ trả nợ gốc.")
    add_answer_box(doc,
                   "CÓ. Ngân hàng không có khoản mục mang tên 'dự phòng giải tỏa', nhưng Luật và Chuẩn mực kế toán đã thiết lập sẵn 3 TẦNG KHOẢN MỤC theo thứ tự hấp thụ tổn thất:",
                   [
                       ("Tầng 1 - Khoản mục DỰ PHÒNG CHUNG (0,75% dư nợ)", "Hạch toán vào Chi phí hoạt động (P&L) theo Thông tư 11/2021/TT-NHNN. Đây là túi tiền luật định bắt buộc trích để dự phòng cho 'những tổn thất chưa xác định được khi cho vay' — đóng vai trò như quỹ bảo hiểm chung của toàn bộ danh mục."),
                       ("Tầng 2 - Khoản mục MANAGEMENT OVERLAY (IFRS 9)", "Hạch toán vào Chi phí P&L. Các mô hình máy tính lịch sử bị 'mù' trước quy hoạch đột xuất, nên Ban Điều hành chủ động trích thêm một cục dự phòng bổ sung dựa trên phán đoán chuyên gia khi phát hiện dự án đi qua khu vực cho vay."),
                       ("Tầng 3 - QUỸ DỰ PHÒNG TÀI CHÍNH & VỐN KINH TẾ (CAR)", "Thuộc Vốn chủ sở hữu. Nếu tổn thất quá lớn vượt quá chi phí dự phòng P&L trong năm, ngân hàng sẽ rút Quỹ dự phòng tài chính (10% LNST) và dùng Đệm vốn an toàn CAR để bù lỗ, không để bị âm vốn điều lệ.")
                   ])
                   
    # Q3
    add_question(doc, 3, 
                 "Khoản mục 3 (Quỹ dự phòng tài chính & Vốn kinh tế) được trích lập như thế nào tại Agribank và MBBank?",
                 "So sánh nguồn trích, tỷ lệ trích và mức trần khống chế giữa hai ngân hàng.")
    add_answer_box(doc,
                   "CẢ HAI NGÂN HÀNG ĐỀU TRÍCH 10% LỢI NHUẬN SAU THUẾ (LNST) HÀNG NĂM VÀO QUỸ DỰ PHÒNG TÀI CHÍNH (Theo Điều 149 Luật Các TCTD 2024 & Nghị định 93/2017). Mức trần tối đa của quỹ bằng 25% Vốn điều lệ.",
                   [
                       ("Điểm khác biệt cốt lõi 1 - Trần tích lũy Quỹ", "MBBank liên tục chia cổ tức bằng cổ phiếu, vốn điều lệ tăng vọt từ 28.000 tỷ lên hơn 61.600 tỷ đồng (2025), giúp trần Quỹ dự phòng tài chính của MB nới rộng liên tục lên 15.411 tỷ đồng. Ngược lại, Agribank là ngân hàng 100% vốn Nhà nước, vốn điều lệ tăng chậm do phải chờ Quốc hội phê duyệt, khiến trần quỹ bị nghẽn nhiều năm ở mức 7.600 - 8.600 tỷ đồng (mãi đến 2024 được cấp thêm 17.100 tỷ vốn ĐL thì trần mới lên 12.910 tỷ)."),
                       ("Điểm khác biệt cốt lõi 2 - Đệm Vốn kinh tế CAR", "MBBank duy trì CAR rất cao (10,75% - 11,80%), dôi dư khoảng +3% RWA so với mức sàn 8,0% (tương đương hơn 30.000 tỷ vốn tự có dôi dư). Agribank duy trì CAR mỏng hơn (9,20% - 10,22%), phụ thuộc nguồn cấp vốn từ ngân sách Nhà nước.")
                   ])
                   
    # Insert Table of Figures
    add_p(doc, "BẢNG ĐỐI CHIẾU SỐ LIỆU KIỂM TOÁN THỰC TẾ (2020 – 2025):", space_before=4, space_after=2)
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
    
    # Q4
    add_question(doc, 4, 
                 "Khi xảy ra cú sốc giải tỏa thần tốc diện rộng khiến tổn thất vượt quá chi phí dự phòng P&L, Agribank và MBBank xử lý Khoản mục 3 khác nhau như thế nào?",
                 "Phân tích cơ chế rút quỹ bù lỗ tài sản và tác động đến hệ số an toàn vốn CAR.")
    add_answer_box(doc,
                   "KHÁC BIỆT CỐT TỬ Ở 2 KHÍA CẠNH: THẨM QUYỀN RÚT QUỸ VÀ KHẢ NĂNG CHỊU ĐÒN CỦA ĐỆM VỐN CAR.",
                   [
                       ("1. Về thẩm quyền rút Quỹ dự phòng tài chính bù lỗ tài sản (Điều 149 Luật Các TCTD)", 
                        "• Tại MBBank: Thẩm quyền thuộc Đại hội đồng Cổ đông và đã được ủy quyền cho Hội đồng Quản trị. Thủ tục nhanh gọn, xử lý thương mại dứt điểm, ghi giảm quỹ trên BCTC năm có kiểm toán Big 4.\n"
                        "• Tại Agribank: Vì là 100% vốn Nhà nước, HĐTV Agribank KHÔNG được tự quyết. Bắt buộc lập hồ sơ giải trình nguyên nhân khách quan do quy hoạch Nhà nước, trình Thống đốc NHNN và Bộ Tài chính phê duyệt để bảo đảm không làm thất thoát vốn Nhà nước trước Kiểm toán Nhà nước."),
                       ("2. Về Đệm Vốn kinh tế (CAR) khi bị tổn thất ăn vào vốn tự có", 
                        "• Tại MBBank: Đệm CAR dày (+3% RWA dôi dư) và lợi nhuận giữ lại khổng lồ (23.000 - 27.000 tỷ/năm) giúp MB hấp thụ cú sốc hàng nghìn tỷ đồng mà CAR vẫn duy trì an toàn trên 10%, tự phục hồi cực nhanh.\n"
                        "• Tại Agribank: Đệm CAR mỏng (9,2% - 10,2%), nếu tổn thất lớn ăn vào vốn tự có sẽ nhanh chóng đẩy CAR chạm lằn ranh tối thiểu 8,0%. Agribank không thể tự phát hành cổ phiếu mà phải chờ Nhà nước cấp bù ngân sách.")
                   ])
                   
    # Q5
    add_question(doc, 5, 
                 "Quy trình tác nghiệp thực tế của ngân hàng khi tài sản dính giải tỏa gồm những bước nào?",
                 "Các bước khép kín từ khi phát hiện quy hoạch đến lúc thu hồi tiền đền bù.")
    add_answer_box(doc,
                   "QUY TRÌNH 4 BƯỚC KHÉP KÍN ĐỂ BẢO VỆ VỐN VÀ THU HỒI NỢ:",
                   [
                       ("Bước 1: Giám sát đặc biệt (Watchlist)", "Quét tọa độ địa chính trên Core Banking, đưa ngay toàn bộ các khoản vay trong vùng giải tỏa vào danh sách Giám sát đặc biệt, dừng ngay việc giải ngân hạn mức mới."),
                       ("Bước 2: Tái định giá theo giá đền bù & Trích dự phòng cụ thể", "Hạ giá trị tài sản từ giá thị trường xuống Giá bồi thường dự kiến của dự án (V_GPMB), ép giá trị khấu trừ C = 50% V_GPMB -> Trích lập bổ sung Dự phòng cụ thể ngay trên chi phí P&L."),
                       ("Bước 3: Ràng buộc hợp đồng (Event of Default)", "Gửi văn bản thông báo khách hàng vi phạm cam kết duy trì TSBĐ. Yêu cầu trong 15-30 ngày phải: (1) Nộp TSBĐ bổ sung; hoặc (2) Nộp tiền mặt trả bớt nợ gốc."),
                       ("Bước 4: Thu hồi tiền trực tiếp từ Kho bạc & Xóa nợ nội bảng (Write-off)", "Đăng ký quyền ưu tiên thanh toán tại Ban GPMB và Kho bạc Nhà nước để tiền đền bù chuyển thẳng vào tài khoản ngân hàng cấn trừ nợ. Nếu còn thiếu, dùng Quỹ dự phòng rủi ro để xóa nợ nội bảng (Write-off) và tiếp tục truy đòi ngoại bảng.")
                   ])
                   
    # Q6 (Bonus Speaker Script)
    add_question(doc, 6, 
                 "Kịch bản phát biểu mẫu (Speaker Script) súc tích, đắt giá nhất để trả lời Thầy cô trên bục bảo vệ?",
                 "Tóm tắt 1 phút trả lời thẳng thắn, thể hiện đẳng cấp Thạc sĩ Tài chính - Ngân hàng.")
    add_answer_box(doc,
                   "LỜI THOẠI TRẢ LỜI MẪU 1 PHÚT DÀNH CHO BẠN:",
                   [
                       ("Đoạn 1 - Xác thực bối cảnh", "'Thưa Thầy và các bạn, việc người dân và ngân hàng bị đánh úp quy hoạch là hoàn toàn có thật do các đại dự án hạ tầng hiện nay áp dụng cơ chế đặc thù: tách riêng GPMB làm trước và điều chỉnh quy hoạch khẩn cấp.'"),
                       ("Đoạn 2 - Cơ chế 3 tầng khoản mục", "'Để bù đắp rủi ro khi giá đền bù thấp hơn nợ vay, ngân hàng có 3 tầng phòng vệ: Tầng 1 là Dự phòng chung 0,75% P&L (cho tổn thất chưa xác định); Tầng 2 là Management Overlay theo IFRS 9 (trích trước theo phán đoán vĩ mô); và Tầng 3 là Quỹ dự phòng tài chính (10% LNST) cùng Đệm vốn CAR thuộc Vốn chủ sở hữu.'"),
                       ("Đoạn 3 - So sánh Agribank vs MBBank", "'Tại Khoản mục 3, MBBank có lợi thế vượt trội nhờ trần quỹ lên tới hơn 15.400 tỷ đồng và đệm CAR dày (+3% RWA), HĐQT chủ động quyết định xử lý. Trong khi Agribank bị nghẽn trần quỹ ở mức 12.900 tỷ do vốn điều lệ tăng chậm; việc rút quỹ phải trình NHNN và Bộ Tài chính phê duyệt; đồng thời đệm CAR mỏng (9,2%-10,2%) nên nếu chịu sốc lớn sẽ phải kiến nghị Nhà nước tiếp tục cấp bù vốn điều lệ.'")
                   ])
                   
    target_docx = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Khoan_muc_Du_phong_Rui_ro_Giai_toa_Than_toc.docx"
    doc.save(target_docx)
    print("SUCCESSFULLY SAVED CLEAN PURE Q&A DOCX:", target_docx)
    
    # Generate companion HTML
    target_html = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2\Khoan_muc_Du_phong_Rui_ro_Giai_toa_Than_toc.html"
    html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Hỏi - Đáp: Quản trị Rủi ro Giải tỏa Mặt bằng & Khoản mục 3 (Agribank vs MBBank)</title>
<style>
  body { font-family: 'Times New Roman', Times, serif; line-height: 1.5; color: #111; background-color: #f7f9fa; margin: 0; padding: 25px; }
  .container { max-width: 900px; margin: 0 auto; background: #fff; padding: 40px 50px; border-radius: 6px; box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
  .top-btn-bar { text-align: right; margin-bottom: 20px; }
  .btn-copy { background: #002060; color: #fff; border: none; padding: 10px 18px; border-radius: 4px; font-weight: bold; cursor: pointer; }
  .btn-copy:hover { background: #0F4C81; }
  .meta-header { text-align: center; margin-bottom: 25px; }
  .uni-title { font-size: 14px; font-weight: bold; color: #505050; text-transform: uppercase; }
  .doc-title { font-size: 20px; font-weight: bold; color: #002060; margin: 10px 0 5px 0; text-transform: uppercase; line-height: 1.3; }
  .doc-sub { font-size: 14px; font-weight: bold; color: #C00000; margin-bottom: 5px; }
  .doc-guide { font-size: 12.5px; font-style: italic; color: #666; }
  .qa-card { background-color: #F8FAFC; border: 1px solid #E2E8F0; border-left: 5px solid #002060; border-radius: 4px; padding: 18px 22px; margin-bottom: 22px; }
  .q-tag { font-weight: bold; color: #C00000; font-size: 15px; }
  .q-title { font-weight: bold; color: #002060; font-size: 15px; }
  .q-context { font-size: 13px; font-style: italic; color: #64748B; margin: 4px 0 12px 0; }
  .ans-core-box { background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 4px; padding: 10px 14px; margin-bottom: 12px; }
  .ans-core-tag { font-size: 12px; font-weight: bold; color: #1E40AF; text-transform: uppercase; }
  .ans-core-text { font-size: 14px; font-weight: bold; color: #DC2626; margin-top: 2px; }
  .ans-point { margin-bottom: 8px; font-size: 13.5px; line-height: 1.45; }
  .ans-point strong { color: #0F4C81; }
  table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 12.5px; }
  th, td { border: 1px solid #CBD5E1; padding: 6px 9px; }
  th { background-color: #002060; color: #fff; text-align: center; }
  tr:nth-child(even) { background-color: #F8FAFC; }
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
    <div class="doc-title">BẢN HỎI - ĐÁP CHUYÊN NGÀNH QUẢN TRỊ RỦI RO TÍN DỤNG</div>
    <div class="doc-sub">ỨNG PHÓ RỦI RO QUY HOẠCH GIẢI TỎA MẶT BẰNG & CƠ CHẾ KHOẢN MỤC 3 DỰ PHÒNG TÀI CHÍNH (AGRIBANK vs MBBANK)</div>
    <div class="doc-guide">Hình thức trình bày: Hỏi và Trả lời trực tiếp | Thuật ngữ chuẩn mực | Dễ hiểu, không phức tạp hóa | Nhóm thực hiện: Nhóm 2</div>
  </div>

  <!-- Q1 -->
  <div class="qa-card">
    <div><span class="q-tag">CÂU HỎI 1: </span><span class="q-title">Thông tin người dân và ngân hàng bị 'đánh úp' bởi các quyết định quy hoạch hạ tầng thần tốc có chính xác không?</span></div>
    <div class="q-context">Bối cảnh: Các dự án hạ tầng lớn triển khai quyết liệt theo chỉ đạo mới, không có dữ liệu quy hoạch từ trước.</div>
    <div class="ans-core-box">
      <div class="ans-core-tag">Bản chất cốt lõi:</div>
      <div class="ans-core-text">HOÀN TOÀN CHÍNH XÁC 100%. Cả người vay và ngân hàng đều rơi vào thế bị động hoàn toàn.</div>
    </div>
    <div class="ans-point"><strong>• Cơ chế giải thích dễ hiểu:</strong> Khi cấp tín dụng 1-2 năm trước, ngân hàng tra cứu tại Sở Tài nguyên & Môi trường thì đây là 'đất ở sạch', hợp pháp 100%, nên tự tin giải ngân 50%-70% giá trị.</div>
    <div class="ans-point"><strong>• Yếu tố 'thần tốc':</strong> Hiện nay, các đại dự án chiến lược (Đường sắt tốc độ cao 67 tỷ USD, mạng lưới cao tốc, vành đai) được Quốc hội cho phép áp dụng 'cơ chế đặc thù': tách riêng giải phóng mặt bằng làm trước và điều chỉnh cục bộ quy hoạch khẩn cấp.</div>
    <div class="ans-point"><strong>• Hệ quả pháp lý & tài chính:</strong> Hướng tuyến chốt đến đâu, cắm mốc giải tỏa đến đó. Ngân hàng và khách hàng hoàn toàn không được biết trước trong dữ liệu lịch sử.</div>
  </div>

  <!-- Q2 -->
  <div class="qa-card">
    <div><span class="q-tag">CÂU HỎI 2: </span><span class="q-title">Giá đền bù thấp hơn nhiều giá thị trường làm 'thủng' tỷ lệ LTV (50%-70%), vậy ngân hàng có khoản mục nào trích lập để 'cover' được rủi ro này không?</span></div>
    <div class="q-context">Bối cảnh: Bất động sản thế chấp bị giải tỏa với giá đền bù thấp, không đủ trả nợ gốc.</div>
    <div class="ans-core-box">
      <div class="ans-core-tag">Bản chất cốt lõi:</div>
      <div class="ans-core-text">CÓ. Ngân hàng không có khoản mục mang tên 'dự phòng giải tỏa', nhưng Luật và Chuẩn mực kế toán đã thiết lập sẵn 3 TẦNG KHOẢN MỤC theo thứ tự hấp thụ tổn thất:</div>
    </div>
    <div class="ans-point"><strong>• Tầng 1 - Khoản mục DỰ PHÒNG CHUNG (0,75% dư nợ):</strong> Hạch toán vào Chi phí hoạt động (P&L) theo Thông tư 11/2021/TT-NHNN. Đây là túi tiền luật định bắt buộc trích để dự phòng cho 'những tổn thất chưa xác định được khi cho vay' — đóng vai trò như quỹ bảo hiểm chung của toàn bộ danh mục.</div>
    <div class="ans-point"><strong>• Tầng 2 - Khoản mục MANAGEMENT OVERLAY (IFRS 9):</strong> Hạch toán vào Chi phí P&L. Các mô hình máy tính lịch sử bị 'mù' trước quy hoạch đột xuất, nên Ban Điều hành chủ động trích thêm một cục dự phòng bổ sung dựa trên phán đoán chuyên gia khi phát hiện dự án đi qua khu vực cho vay.</div>
    <div class="ans-point"><strong>• Tầng 3 - QUỸ DỰ PHÒNG TÀI CHÍNH & VỐN KINH TẾ (CAR):</strong> Thuộc Vốn chủ sở hữu. Nếu tổn thất quá lớn vượt quá chi phí dự phòng P&L trong năm, ngân hàng sẽ rút Quỹ dự phòng tài chính (10% LNST) và dùng Đệm vốn an toàn CAR để bù lỗ, không để bị âm vốn điều lệ.</div>
  </div>

  <!-- Q3 -->
  <div class="qa-card">
    <div><span class="q-tag">CÂU HỎI 3: </span><span class="q-title">Khoản mục 3 (Quỹ dự phòng tài chính & Vốn kinh tế) được trích lập như thế nào tại Agribank và MBBank?</span></div>
    <div class="q-context">Bối cảnh: So sánh nguồn trích, tỷ lệ trích và mức trần khống chế giữa hai ngân hàng.</div>
    <div class="ans-core-box">
      <div class="ans-core-tag">Bản chất cốt lõi:</div>
      <div class="ans-core-text">CẢ HAI NGÂN HÀNG ĐỀU TRÍCH 10% LỢI NHUẬN SAU THUẾ (LNST) HÀNG NĂM VÀO QUỸ DỰ PHÒNG TÀI CHÍNH (Theo Điều 149 Luật Các TCTD 2024 & Nghị định 93/2017). Mức trần tối đa của quỹ bằng 25% Vốn điều lệ.</div>
    </div>
    <div class="ans-point"><strong>• Điểm khác biệt cốt lõi 1 - Trần tích lũy Quỹ:</strong> MBBank liên tục chia cổ tức bằng cổ phiếu, vốn điều lệ tăng vọt từ 28.000 tỷ lên hơn 61.600 tỷ đồng (2025), giúp trần Quỹ dự phòng tài chính của MB nới rộng liên tục lên 15.411 tỷ đồng. Ngược lại, Agribank là ngân hàng 100% vốn Nhà nước, vốn điều lệ tăng chậm do phải chờ Quốc hội phê duyệt, khiến trần quỹ bị nghẽn nhiều năm ở mức 7.600 - 8.600 tỷ đồng (mãi đến 2024 được cấp thêm 17.100 tỷ vốn ĐL thì trần mới lên 12.910 tỷ).</div>
    <div class="ans-point"><strong>• Điểm khác biệt cốt lõi 2 - Đệm Vốn kinh tế CAR:</strong> MBBank duy trì CAR rất cao (10,75% - 11,80%), dôi dư khoảng +3% RWA so với mức sàn 8,0% (tương đương hơn 30.000 tỷ vốn tự có dôi dư). Agribank duy trì CAR mỏng hơn (9,20% - 10,22%), phụ thuộc nguồn cấp vốn từ ngân sách Nhà nước.</div>
    
    <div style="font-weight:bold; color:#002060; margin:12px 0 4px 0;">BẢNG ĐỐI CHIẾU SỐ LIỆU KIỂM TOÁN THỰC TẾ (2020 – 2025):</div>
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
  </div>

  <!-- Q4 -->
  <div class="qa-card">
    <div><span class="q-tag">CÂU HỎI 4: </span><span class="q-title">Khi xảy ra cú sốc giải tỏa thần tốc diện rộng khiến tổn thất vượt quá chi phí dự phòng P&L, Agribank và MBBank xử lý Khoản mục 3 khác nhau như thế nào?</span></div>
    <div class="q-context">Bối cảnh: Phân tích cơ chế rút quỹ bù lỗ tài sản và tác động đến hệ số an toàn vốn CAR.</div>
    <div class="ans-core-box">
      <div class="ans-core-tag">Bản chất cốt lõi:</div>
      <div class="ans-core-text">KHÁC BIỆT CỐT TỬ Ở 2 KHÍA CẠNH: THẨM QUYỀN RÚT QUỸ VÀ KHẢ NĂNG CHỊU ĐÒN CỦA ĐỆM VỐN CAR.</div>
    </div>
    <div class="ans-point"><strong>1. Về thẩm quyền rút Quỹ dự phòng tài chính bù lỗ tài sản (Điều 149 Luật Các TCTD):</strong><br>
    • <em>Tại MBBank:</em> Thẩm quyền thuộc Đại hội đồng Cổ đông và đã được ủy quyền cho Hội đồng Quản trị. Thủ tục nhanh gọn, xử lý thương mại dứt điểm, ghi giảm quỹ trên BCTC năm có kiểm toán Big 4.<br>
    • <em>Tại Agribank:</em> Vì là 100% vốn Nhà nước, HĐTV Agribank KHÔNG được tự quyết. Bắt buộc lập hồ sơ giải trình nguyên nhân khách quan do quy hoạch Nhà nước, trình Thống đốc NHNN và Bộ Tài chính phê duyệt để bảo đảm không làm thất thoát vốn Nhà nước trước Kiểm toán Nhà nước.</div>
    <div class="ans-point"><strong>2. Về Đệm Vốn kinh tế (CAR) khi bị tổn thất ăn vào vốn tự có:</strong><br>
    • <em>Tại MBBank:</em> Đệm CAR dày (+3% RWA dôi dư) và lợi nhuận giữ lại khổng lồ (23.000 - 27.000 tỷ/năm) giúp MB hấp thụ cú sốc hàng nghìn tỷ đồng mà CAR vẫn duy trì an toàn trên 10%, tự phục hồi cực nhanh.<br>
    • <em>Tại Agribank:</em> Đệm CAR mỏng (9,2% - 10,2%), nếu tổn thất lớn ăn vào vốn tự có sẽ nhanh chóng đẩy CAR chạm lằn ranh tối thiểu 8,0%. Agribank không thể tự phát hành cổ phiếu mà phải chờ Nhà nước cấp bù ngân sách.</div>
  </div>

  <!-- Q5 -->
  <div class="qa-card">
    <div><span class="q-tag">CÂU HỎI 5: </span><span class="q-title">Quy trình tác nghiệp thực tế của ngân hàng khi tài sản dính giải tỏa gồm những bước nào?</span></div>
    <div class="q-context">Bối cảnh: Các bước khép kín từ khi phát hiện quy hoạch đến lúc thu hồi tiền đền bù.</div>
    <div class="ans-core-box">
      <div class="ans-core-tag">Bản chất cốt lõi:</div>
      <div class="ans-core-text">QUY TRÌNH 4 BƯỚC KHÉP KÍN ĐỂ BẢO VỆ VỐN VÀ THU HỒI NỢ:</div>
    </div>
    <div class="ans-point"><strong>• Bước 1: Giám sát đặc biệt (Watchlist):</strong> Quét tọa độ địa chính trên Core Banking, đưa ngay toàn bộ các khoản vay trong vùng giải tỏa vào danh sách Giám sát đặc biệt, dừng ngay việc giải ngân hạn mức mới.</div>
    <div class="ans-point"><strong>• Bước 2: Tái định giá theo giá đền bù & Trích dự phòng cụ thể:</strong> Hạ giá trị tài sản từ giá thị trường xuống Giá bồi thường dự kiến của dự án (V_GPMB), ép giá trị khấu trừ C = 50% V_GPMB -> Trích lập bổ sung Dự phòng cụ thể ngay trên chi phí P&L.</div>
    <div class="ans-point"><strong>• Bước 3: Ràng buộc hợp đồng (Event of Default):</strong> Gửi văn bản thông báo khách hàng vi phạm cam kết duy trì TSBĐ. Yêu cầu trong 15-30 ngày phải: (1) Nộp TSBĐ bổ sung; hoặc (2) Nộp tiền mặt trả bớt nợ gốc.</div>
    <div class="ans-point"><strong>• Bước 4: Thu hồi tiền trực tiếp từ Kho bạc & Xóa nợ nội bảng (Write-off):</strong> Đăng ký quyền ưu tiên thanh toán tại Ban GPMB và Kho bạc Nhà nước để tiền đền bù chuyển thẳng vào tài khoản ngân hàng cấn trừ nợ. Nếu còn thiếu, dùng Quỹ dự phòng rủi ro để xóa nợ nội bảng (Write-off) và tiếp tục truy đòi ngoại bảng.</div>
  </div>

  <!-- Q6 -->
  <div class="qa-card">
    <div><span class="q-tag">CÂU HỎI 6: </span><span class="q-title">Kịch bản phát biểu mẫu (Speaker Script) súc tích, đắt giá nhất để trả lời Thầy cô trên bục bảo vệ?</span></div>
    <div class="q-context">Bối cảnh: Tóm tắt 1 phút trả lời thẳng thắn, thể hiện đẳng cấp Thạc sĩ Tài chính - Ngân hàng.</div>
    <div class="ans-core-box">
      <div class="ans-core-tag">LỜI THOẠI TRẢ LỜI MẪU 1 PHÚT DÀNH CHO BẠN:</div>
      <div class="ans-core-text" style="color:#002060; font-size:13.5px; font-weight:normal; line-height:1.5;">
        "Thưa Thầy và các bạn, việc người dân và ngân hàng bị đánh úp quy hoạch là hoàn toàn có thật do các đại dự án hạ tầng hiện nay áp dụng cơ chế đặc thù: tách riêng GPMB làm trước và điều chỉnh quy hoạch khẩn cấp.<br><br>
        Để bù đắp rủi ro khi giá đền bù thấp hơn nợ vay, ngân hàng có 3 tầng phòng vệ: Tầng 1 là Dự phòng chung 0,75% P&L (cho tổn thất chưa xác định); Tầng 2 là Management Overlay theo IFRS 9 (trích trước theo phán đoán vĩ mô); và Tầng 3 là Quỹ dự phòng tài chính (10% LNST) cùng Đệm vốn CAR thuộc Vốn chủ sở hữu.<br><br>
        Tại Khoản mục 3, MBBank có lợi thế vượt trội nhờ trần quỹ lên tới hơn 15.400 tỷ đồng và đệm CAR dày (+3% RWA), HĐQT chủ động quyết định xử lý. Trong khi Agribank bị nghẽn trần quỹ ở mức 12.900 tỷ do vốn điều lệ tăng chậm; việc rút quỹ phải trình NHNN và Bộ Tài chính phê duyệt; đồng thời đệm CAR mỏng (9,2%-10,2%) nên nếu chịu sốc lớn sẽ phải kiến nghị Nhà nước tiếp tục cấp bù vốn điều lệ."
      </div>
    </div>
  </div>
</div>

<script>
function copyDocument() {
  const el = document.getElementById('content-to-copy');
  const range = document.createRange();
  range.selectNode(el);
  window.getSelection().removeAllRanges();
  window.getSelection().addRange(range);
  try {
    document.execCommand('copy');
    alert('Đã sao chép toàn bộ nội dung văn bản kèm định dạng thành công! Bạn chỉ cần mở Google Docs và nhấn Ctrl+V để dán.');
  } catch (err) {
    alert('Lỗi sao chép tự động: ' + err);
  }
  window.getSelection().removeAllRanges();
}
</script>
</body>
</html>
"""
    with open(target_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("SUCCESSFULLY SAVED CLEAN PURE Q&A HTML:", target_html)

build_qa_document()
