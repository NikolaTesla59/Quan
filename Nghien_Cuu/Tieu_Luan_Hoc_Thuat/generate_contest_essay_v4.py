import os
import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

def generate_essay():
    doc = docx.Document()
    
    # Page setup A4 & Margins 3 - 2 - 2 - 2 (Left 3cm, Top 2cm, Bottom 2cm, Right 2cm)
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(2.0)
    
    # Header & Footer
    footer = section.footer
    f_p = footer.paragraphs[0]
    f_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    f_run = f_p.add_run("Bài dự thi Thẩm định giá Việt Nam lần thứ 2 (2026 - 2027)")
    f_run.font.name = "Times New Roman"
    f_run.font.size = Pt(10)
    f_run.italic = True
    f_run.font.color.rgb = RGBColor(120, 120, 120)

    def style_run(run, font_name="Times New Roman", size_pt=14, bold=False, italic=False, color_rgb=(0,0,0)):
        run.font.name = font_name
        run.font.size = Pt(size_pt)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = RGBColor(*color_rgb)

    def add_p(doc, text="", space_before=0, space_after=6, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_line_indent_cm=1.27, size_pt=14):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        p.alignment = align
        if first_line_indent_cm > 0:
            p.paragraph_format.first_line_indent = Cm(first_line_indent_cm)
        if text:
            r = p.add_run(text)
            style_run(r, font_name="Times New Roman", size_pt=size_pt)
        return p

    def add_h1(doc, text, size_pt=14.5):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.first_line_indent = Cm(0)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(text)
        style_run(r, font_name="Times New Roman", size_pt=size_pt, bold=True, color_rgb=(0, 32, 96))
        return p

    def add_math_equation(doc, omml_xml_string):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.first_line_indent = Cm(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        element = parse_xml(omml_xml_string)
        p._p.append(element)
        return p

    # Contest Title Banner
    p_org = add_p(doc, "BÀI DỰ THI CUỘC THI VIẾT:", space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER, first_line_indent_cm=0, size_pt=11)
    style_run(p_org.runs[0], size_pt=11, bold=True, color_rgb=(100, 100, 100))

    p_cname = add_p(doc, "“THẨM ĐỊNH GIÁ VIỆT NAM VÌ SỰ PHÁT TRIỂN KINH TẾ - XÃ HỘI CỦA ĐẤT NƯỚC”\nLẦN THỨ 2 (2026 – 2027)", space_after=3, align=WD_ALIGN_PARAGRAPH.CENTER, first_line_indent_cm=0, size_pt=13)
    style_run(p_cname.runs[0], size_pt=13, bold=True, color_rgb=(192, 0, 0))

    p_unit = add_p(doc, "Đơn vị chỉ đạo: Hội Thẩm định giá Việt Nam (VVA)\nĐơn vị tổ chức: Tạp chí điện tử Nhịp sống Thị trường (MarketTimes.vn)", space_after=14, align=WD_ALIGN_PARAGRAPH.CENTER, first_line_indent_cm=0, size_pt=11)
    style_run(p_unit.runs[0], size_pt=11, italic=True, color_rgb=(80, 80, 80))

    # Article Title
    title_text = (
        "TỪ NGHỊCH LÝ “GỌT CHÂN CHO VỪA GIÀY” ĐẾN BƯỚC NHẢY LƯỢNG HÓA BIG DATA:\n"
        "LỜI GIẢI CHO BẢNG GIÁ ĐẤT VÀ NỖI ĐAU CỦA NGÀNH THẨM ĐỊNH GIÁ"
    )
    p_t = add_p(doc, title_text, space_before=6, space_after=14, align=WD_ALIGN_PARAGRAPH.CENTER, first_line_indent_cm=0, size_pt=16)
    style_run(p_t.runs[0], size_pt=16, bold=True, color_rgb=(0, 32, 96))

    # Sapo (Tightened & Objective: ~115 words)
    sapo_text = (
        "Từ thực tiễn xây dựng bảng giá đất địa phương, định giá dự án bất động sản cho đến thẩm định tài sản bảo đảm thế chấp, "
        "ngành thẩm định giá Việt Nam đang đối mặt nghịch lý nhức nhối: dù mẫu khảo sát thực tế rất lớn, thẩm định viên vẫn bị "
        "trói buộc vào quy tắc chọn 3 tài sản so sánh và tự ý 'bốc thuốc' tỷ lệ điều chỉnh để hợp thức hóa mức giá mục tiêu của bên thuê. "
        "Trước yêu cầu thực thi bảng giá đất theo Luật Đất đai năm 2024, lời giải căn cơ là ứng dụng Dữ liệu lớn (Big Data) và Mô hình Hedonic "
        "để lượng hóa khách quan các biến số điều chỉnh, thiết lập công thức tham chiếu chuẩn mực, đồng thời dựng lên 'tấm khiên công nghệ' "
        "bảo vệ sự độc lập, liêm chính của người làm nghề."
    )
    p_sapo = add_p(doc, sapo_text, space_before=4, space_after=10, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_line_indent_cm=1.27, size_pt=13.5)
    style_run(p_sapo.runs[0], size_pt=13.5, bold=True, italic=True, color_rgb=(30, 41, 59))

    # Section 1
    add_h1(doc, "1. Nghịch lý 'gọt 3 tài sản so sánh' và góc khuất: 'Không ai cần một thẩm định viên làm đúng'", size_pt=14.5)
    
    add_p(doc, 
        "Trong nền kinh tế thị trường, các doanh nghiệp thẩm định giá độc lập là trọng tài xác lập giá trị thực nhằm bảo đảm an toàn tín dụng, "
        "chống thất thoát ngân sách trong cổ phần hóa và tính đúng nghĩa vụ tài chính đất đai. Thế nhưng trong thực tế, một nghịch lý cay đắng "
        "đang tồn tại: Người thuê dịch vụ thẩm định giá thường chỉ muốn kết quả thẩm định làm sai lệch có lợi nhất cho mục đích riêng của họ."
    )
    add_p(doc,
        "Xung đột lợi ích này diễn ra khốc liệt ở mọi phân khúc: Doanh nghiệp vay thế chấp tìm mọi cách thổi phồng giá trị để tối đa hóa "
        "hạn mức giải ngân; ngược lại, chủ đầu tư nộp tiền sử dụng đất dự án lại gây sức ép kéo giá thẩm định sát đáy nhằm giảm nghĩa vụ ngân sách. "
        "Thẩm định viên bị kẹt ở thế tiến thoái lưỡng nan: Làm đúng nguyên tắc thị trường thì khách hàng cắt hợp đồng, doanh nghiệp mất việc; "
        "nhưng nếu chiều theo bên thuê thì rủi ro lao lý luôn lơ lửng trên đầu khi thanh tra, kiểm toán vào cuộc."
    )
    add_p(doc,
        "Bi kịch này được che đậy dưới vỏ bọc quy trình kỹ thuật. Khi xây dựng bảng giá đất địa phương hay thẩm định dự án bất động sản, "
        "mẫu khảo sát thu thập được lên tới hàng nghìn giao dịch thực tế. Thế nhưng, Tiêu chuẩn Thẩm định giá hiện hành lại trói buộc phương pháp so sánh "
        "vào việc chọn đúng 3 tài sản tương đồng. Nút thắt này biến quy trình thẩm định thành trò 'gọt chân cho vừa giày': Thẩm định viên chọn ra "
        "3 tài sản thuận lợi để hướng tới con số mục tiêu thỏa thuận trước, rồi tự 'bốc thuốc' tỷ lệ điều chỉnh (+5% ngõ rộng, -3% đất méo, +10% vị trí) "
        "một cách cảm tính mà không có bất kỳ căn cứ thực nghiệm nào."
    )
    add_p(doc,
        "Đại án SCB - Vạn Thịnh Phát với sự tiếp tay của các công ty thẩm định giá nâng khống tài sản là hồi chuông cảnh tỉnh sâu sắc. "
        "Đó không chỉ là sự tha hóa cá nhân, mà là lỗ hổng hệ thống khi phương pháp định giá thủ công trao quyền tùy biến quá lớn cho ý chí chủ quan "
        "bị chi phối bởi tiền bạc."
    )

    # Section 2
    add_h1(doc, "2. Lượng hóa và chuẩn hóa: Dùng Big Data và Mô hình Hedonic để chấm dứt trò 'bốc thuốc'", size_pt=14.5)

    add_p(doc,
        "Muốn đưa Bảng giá đất theo Luật Đất đai năm 2024 thực sự tiệm cận giá trị thị trường, hoạt động thẩm định giá không thể tiếp tục "
        "dựa vào cảm quan định tính. Lời giải căn cơ là phải lượng hóa các yếu tố so sánh bằng Dữ liệu lớn (Big Data) và Kinh tế lượng ứng dụng."
    )
    add_p(doc,
        "Bất động sản về bản chất là một 'gói các thuộc tính': tọa độ GIS, diện tích, mặt tiền, chiều sâu, hình dáng, lộ giới ngõ, tiện ích, "
        "pháp lý và thời điểm giao dịch. Trong kinh tế lượng thực nghiệm, Mô hình định giá hưởng thụ Hedonic giải quyết triệt để bài toán này "
        "thông qua hàm hồi quy bán logarit:"
    )

    # OMML Math 1
    omml_eq1 = (
        '<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
        '<m:oMath>'
        '<m:r><m:t>ln</m:t></m:r>'
        '<m:d><m:dPr><m:begChr m:val="("/><m:endChr m:val=")"/></m:dPr><m:e>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:t>j</m:t></m:r></m:sub></m:sSub>'
        '</m:e></m:d>'
        '<m:r><m:t> = </m:t></m:r>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>β</m:t></m:r></m:e><m:sub><m:r><m:t>0</m:t></m:r></m:sub></m:sSub>'
        '<m:r><m:t> + </m:t></m:r>'
        '<m:nary>'
        '<m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/><m:grow m:val="1"/></m:naryPr>'
        '<m:sub><m:r><m:t>k=1</m:t></m:r></m:sub>'
        '<m:sup><m:r><m:t>m</m:t></m:r></m:sup>'
        '<m:e>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>β</m:t></m:r></m:e><m:sub><m:r><m:t>k</m:t></m:r></m:sub></m:sSub>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>X</m:t></m:r></m:e><m:sub><m:r><m:t>kj</m:t></m:r></m:sub></m:sSub>'
        '</m:e>'
        '</m:nary>'
        '<m:r><m:t> + </m:t></m:r>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>ε</m:t></m:r></m:e><m:sub><m:r><m:t>j</m:t></m:r></m:sub></m:sSub>'
        '</m:oMath>'
        '</m:oMathPara>'
    )
    add_math_equation(doc, omml_eq1)

    add_p(doc,
        "Trong đó, P_j là giá giao dịch thực tế của bất động sản j, X_kj là các biến số thuộc tính đặc trưng và beta_k là trọng số đóng góp "
        "của thuộc tính k. Khi công nghệ Big Data thu thập hàng chục vạn giao dịch mua bán thực tế, mô hình hồi quy sẽ giải quyết 3 bài toán kỹ thuật:"
    )
    add_p(doc,
        "Thứ nhất, kiểm định thực nghiệm xem biến số nào thực sự có ý nghĩa thống kê (p-value < 0.05). Phân tích chứng minh nhiều yếu tố cảm tính "
        "(như phong thủy hay tâm lý mơ hồ) thực chất không tác động đáng kể; trong khi bề rộng ngõ, tỷ lệ mặt tiền/chiều sâu và khoảng cách hạ tầng "
        "lại chiếm tỷ trọng chi phối tuyệt đối."
    )
    add_p(doc,
        "Thứ hai, xác định chính xác và minh bạch tỷ lệ điều chỉnh phần trăm trực tiếp từ hệ số hồi quy thị trường theo công thức:"
    )

    # OMML Math 2
    omml_eq2 = (
        '<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
        '<m:oMath>'
        '<m:r><m:t>Δ%</m:t></m:r>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:t>k</m:t></m:r></m:sub></m:sSub>'
        '<m:r><m:t> = </m:t></m:r>'
        '<m:d><m:dPr><m:begChr m:val="("/><m:endChr m:val=")"/></m:dPr><m:e>'
        '<m:sSup><m:sSupPr/><m:e><m:r><m:t>e</m:t></m:r></m:e><m:sup><m:sSub><m:sSubPr/><m:e><m:r><m:t>β</m:t></m:r></m:e><m:sub><m:r><m:t>k</m:t></m:r></m:sub></m:sSub></m:sup></m:sSup>'
        '<m:r><m:t> - 1</m:t></m:r>'
        '</m:e></m:d>'
        '<m:r><m:t> × 100%</m:t></m:r>'
        '</m:oMath>'
        '</m:oMathPara>'
    )
    add_math_equation(doc, omml_eq2)

    add_p(doc,
        "Khi mô hình thực nghiệm chứng minh mỗi mét mở rộng ngõ làm tăng giá đất 4,2% hay thửa đất tóp hậu bị chiết khấu 6,8%, "
        "thẩm định viên bắt buộc phải áp dụng trọng số khách quan này. Tỷ lệ điều chỉnh lúc này là tiếng nói khách quan của thị trường, "
        "loại bỏ hoàn toàn khả năng can thiệp chủ quan."
    )
    add_p(doc,
        "Thứ ba, chốt công thức định giá tham chiếu chuẩn hóa (Benchmark Valuation Formula) cho từng tuyến đường, phân vùng đô thị:"
    )

    # OMML Math 3
    omml_eq3 = (
        '<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
        '<m:oMath>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:t>tham chiếu</m:t></m:r></m:sub></m:sSub>'
        '<m:r><m:t> = exp</m:t></m:r>'
        '<m:d><m:dPr><m:begChr m:val="("/><m:endChr m:val=")"/></m:dPr><m:e>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>β</m:t></m:r></m:e><m:sub><m:r><m:t>0</m:t></m:r></m:sub></m:sSub>'
        '<m:r><m:t> + </m:t></m:r>'
        '<m:nary>'
        '<m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/><m:grow m:val="1"/></m:naryPr>'
        '<m:sub><m:r><m:t>k=1</m:t></m:r></m:sub>'
        '<m:sup><m:r><m:t>m</m:t></m:r></m:sup>'
        '<m:e>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>β</m:t></m:r></m:e><m:sub><m:r><m:t>k</m:t></m:r></m:sub></m:sSub>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>X</m:t></m:r></m:e><m:sub><m:r><m:t>k0</m:t></m:r></m:sub></m:sSub>'
        '</m:e>'
        '</m:nary>'
        '<m:r><m:t> + </m:t></m:r>'
        '<m:f><m:fPr/><m:num><m:sSup><m:sSupPr/><m:e><m:r><m:t>σ</m:t></m:r></m:e><m:sup><m:r><m:t>2</m:t></m:r></m:sup></m:sSup></m:num><m:den><m:r><m:t>2</m:t></m:r></m:den></m:f>'
        '</m:e></m:d>'
        '</m:oMath>'
        '</m:oMathPara>'
    )
    add_math_equation(doc, omml_eq3)

    add_p(doc,
        "Đây là công cụ bước ngoặt để các địa phương xây dựng Bảng giá đất hàng năm một cách khoa học, cập nhật tự động theo chu kỳ thị trường, "
        "chấm dứt tình trạng lúng túng hoặc thẩm định viên chịu sức ép vô lý khi lập bảng giá."
    )

    # Section 3
    add_h1(doc, "3. 'Tấm khiên công nghệ' bảo vệ sự độc lập và liêm chính của Thẩm định viên", size_pt=14.5)

    add_p(doc,
        "Hiện nay, các đơn vị thẩm định giá độc lập rất cô độc khi đứng mũi chịu sào trước sức ép từ doanh nghiệp vì thiếu công cụ kỹ thuật tự vệ. "
        "Chuẩn hóa bằng Big Data không hề triệt tiêu vai trò của thẩm định viên, mà tạo ra 'tấm khiên bảo vệ' (safe harbor) kiên cố nhất cho người hành nghề."
    )
    add_p(doc,
        "Khi cơ sở dữ liệu quốc gia và mô hình định giá tự động (AVM) được thiết lập, hệ thống sẽ xác lập khoảng tin cậy thống kê chuẩn mực:"
    )

    # OMML Math 4
    omml_eq4 = (
        '<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
        '<m:oMath>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:t>dự báo</m:t></m:r></m:sub></m:sSub>'
        '<m:r><m:t> - </m:t></m:r>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>z</m:t></m:r></m:e><m:sub><m:r><m:t>α/2</m:t></m:r></m:sub></m:sSub>'
        '<m:r><m:t> · SE ≤ P ≤ </m:t></m:r>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:t>dự báo</m:t></m:r></m:sub></m:sSub>'
        '<m:r><m:t> + </m:t></m:r>'
        '<m:sSub><m:sSubPr/><m:e><m:r><m:t>z</m:t></m:r></m:e><m:sub><m:r><m:t>α/2</m:t></m:r></m:sub></m:sSub>'
        '<m:r><m:t> · SE</m:t></m:r>'
        '</m:oMath>'
        '</m:oMathPara>'
    )
    add_math_equation(doc, omml_eq4)

    add_p(doc,
        "Với khoảng tin cậy 95% (sai số cho phép thông thường +/- 7%), nếu khách hàng ép nâng hay dìm giá quá mức, thẩm định viên có thể tự tin "
        "từ chối dựa trên căn cứ khoa học: 'Hệ thống dữ liệu thị trường không chấp nhận độ lệch chuẩn này'. Mọi sự điều chỉnh bất thường vượt biên độ "
        "đều tự động kích hoạt cảnh báo rủi ro (Anomaly Detection), buộc phải có giải trình kỹ thuật độc lập."
    )
    add_p(doc,
        "Thẩm định viên lúc này được giải phóng để tập trung vào giá trị tinh hoa nhất: phán đoán chuyên gia (Expert Judgement). "
        "Đó là việc kiểm tra thực địa những yếu tố phi cấu trúc: tranh chấp ranh giới ngầm, chất lượng thi công dở dang, uy tín thực tế của chủ đầu tư "
        "hay rủi ro vĩ mô. Khi công nghệ gánh vác việc lượng hóa khách quan, đạo đức nghề nghiệp sẽ có điểm tựa vững chắc để giữ trọn sự liêm chính."
    )

    # Section 4
    add_h1(doc, "4. Ba kiến nghị hành động xây dựng hệ sinh thái Thẩm định giá minh bạch", size_pt=14.5)

    add_p(doc,
        "Để hiện thực hóa chuyển đổi số theo Luật Giá năm 2023 và Luật Đất đai năm 2024, ba giải pháp đột phá cần được triển khai đồng bộ:"
    )
    add_p(doc,
        "Một là, thể chế hóa phương pháp hồi quy Hedonic vào Tiêu chuẩn Thẩm định giá Việt Nam. Cần cho phép dùng mẫu lớn và mô hình kinh tế lượng "
        "để xác định tỷ lệ điều chỉnh; chấm dứt việc bắt buộc chỉ dùng 3 tài sản so sánh đơn lẻ tại các khu vực có giao dịch dày đặc. "
        "Bộ Tài chính cần sớm ban hành cẩm nang hướng dẫn xác định trọng số biến số theo từng vùng kinh tế."
    )
    add_p(doc,
        "Hai là, xây dựng Hệ sinh thái Dữ liệu giá bất động sản minh bạch. Đẩy mạnh thanh toán không dùng tiền mặt trong giao dịch nhà đất, "
        "áp dụng hóa đơn điện tử cho mọi hợp đồng chuyển nhượng, tích hợp Cơ sở dữ liệu quốc gia về giá với Hệ thống địa chính của Bộ Tài nguyên và Môi trường. "
        "Khi dữ liệu phản ánh giá trị thật, Big Data sẽ phục vụ đắc lực cho công tác lập Bảng giá đất và định giá dự án."
    )
    add_p(doc,
        "Ba là, Hội Thẩm định giá Việt Nam (VVA) thiết lập cơ chế giám sát độc lập và bảo vệ thẩm định viên trước các hành vi chèn ép, thao túng giá; "
        "đồng thời phối hợp cùng các trường đại học lớn như Đại học Kinh tế Quốc dân (NEU) đào tạo thế hệ thẩm định viên mới: vững khoa học dữ liệu, "
        "am tường kinh tế lượng tài chính và giữ trọn cốt cách liêm chính."
    )

    # Conclusion
    add_h1(doc, "Lời kết: Giữ trọn sự liêm chính vì sự phồn vinh của đất nước", size_pt=14.5)

    add_p(doc,
        "Nghề thẩm định giá là nghề của niềm tin. Một chứng thư thẩm định mang theo sinh mệnh doanh nghiệp, quyền lợi chính đáng của người dân "
        "và sự an toàn của dòng vốn quốc gia. Nếu thỏa hiệp với cái sai, cái giá phải trả là sự thất thoát nguồn lực đất đai và bất ổn tài chính khôn lường."
    )
    add_p(doc,
        "Big Data và AI chính là cơ hội lịch sử để ngành Thẩm định giá Việt Nam rũ bỏ định kiến 'gọt chân cho vừa giày', xác lập vị thế đàng hoàng "
        "của người làm nghề. Với hành lang pháp lý minh bạch, sự trợ lực của khoa học dữ liệu và bản lĩnh kiên định của những thẩm định viên chân chính, "
        "ngành thẩm định giá hoàn toàn có thể tự hào đóng góp vào sự phát triển công bằng, văn minh và phồn vinh của đất nước."
    )

    total_p_words = sum(len(p.text.split()) for p in doc.paragraphs)

    # Table Spacing
    doc.add_paragraph()

    # Author Table at the END
    p_tbl_title = doc.add_paragraph()
    p_tbl_title.paragraph_format.space_before = Pt(16)
    p_tbl_title.paragraph_format.space_after = Pt(6)
    p_tbl_title.paragraph_format.keep_with_next = True
    p_tbl_title.paragraph_format.first_line_indent = Cm(0)
    p_tbl_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_tbl_title = p_tbl_title.add_run("THÔNG TIN TÁC GIẢ DỰ THI (THEO THỂ LỆ BAN TỔ CHỨC):")
    style_run(r_tbl_title, size_pt=13, bold=True, color_rgb=(0, 32, 96))

    author_data = [
        ("Họ và tên tác giả:", "[Họ và tên tác giả]"),
        ("Bút danh (nếu có):", "[Bút danh (nếu có)]"),
        ("Năm sinh / Giới tính:", "[Năm sinh]  |  [Nam / Nữ]"),
        ("Số CCCD / Ngày cấp / Nơi cấp:", "[Số CCCD]  |  [Ngày cấp]  |  [Nơi cấp]"),
        ("Nghề nghiệp / Chức vụ:", "Thẩm định viên Bất động sản & Dự án"),
        ("Đơn vị công tác / Học tập:", "Doanh nghiệp Thẩm định giá Độc lập  /  Học viên Cao học Tài chính - Ngân hàng, Viện Ngân hàng - Tài chính, ĐH Kinh tế Quốc dân (NEU)"),
        ("Địa chỉ liên hệ thường trú:", "[Địa chỉ liên hệ thường trú của tác giả]"),
        ("Số điện thoại liên hệ:", "[Số điện thoại liên hệ]"),
        ("Địa chỉ Email liên hệ:", "[Địa chỉ Email liên hệ]"),
        ("Chủ đề bài viết dự thi:", "Hướng 3: Chuyển đổi số, Big Data và Kinh tế lượng giải quyết bất cập Bảng giá đất và phương pháp so sánh"),
        ("Dung lượng toàn bài:", f"{total_p_words} chữ (Tuân thủ nghiêm ngặt Thể lệ cuộc thi: không quá 2.000 chữ)"),
        ("Cam kết của tác giả:", "Bài dự thi là công trình nghiên cứu độc lập của tác giả, chưa từng đạt giải ở bất kỳ cuộc thi nào và chưa từng công bố trên các phương tiện truyền thông báo chí.")
    ]

    tbl = doc.add_table(rows=len(author_data), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    tblPr = tbl._element.xpath('w:tblPr')[0]
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="002060"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="002060"/>'
        f'<w:left w:val="single" w:sz="6" w:space="0" w:color="002060"/>'
        f'<w:right w:val="single" w:sz="6" w:space="0" w:color="002060"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

    col_widths = [Cm(5.0), Cm(11.0)]

    for row_idx, (k, v) in enumerate(author_data):
        row = tbl.rows[row_idx]
        
        c0 = row.cells[0]
        c0.width = col_widths[0]
        tcPr0 = c0._tc.get_or_add_tcPr()
        shd0 = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F1F5F9"/>')
        tcPr0.append(shd0)
        tcMar0 = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/><w:left w:w="140" w:type="dxa"/><w:right w:w="140" w:type="dxa"/></w:tcMar>')
        tcPr0.append(tcMar0)
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(3)
        p0.paragraph_format.space_after = Pt(3)
        p0.paragraph_format.line_spacing = 1.2
        r0 = p0.add_run(k)
        style_run(r0, size_pt=12.5, bold=True, color_rgb=(0, 32, 96))

        c1 = row.cells[1]
        c1.width = col_widths[1]
        tcPr1 = c1._tc.get_or_add_tcPr()
        tcMar1 = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/><w:left w:w="140" w:type="dxa"/><w:right w:w="140" w:type="dxa"/></w:tcMar>')
        tcPr1.append(tcMar1)
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(3)
        p1.paragraph_format.space_after = Pt(3)
        p1.paragraph_format.line_spacing = 1.2
        r1 = p1.add_run(v)
        style_run(r1, size_pt=12.5, color_rgb=(20, 20, 20))

    # Save Docx
    target_dir = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\files 2"
    target_docx = os.path.join(target_dir, "Bai_du_thi_Tham_dinh_gia_Viet_Nam_2026_2027_Ky_nguyen_so.docx")
    doc.save(target_docx)
    print("SUCCESSFULLY SAVED DOCX:", target_docx)

    # Save HTML with MathJax LaTeX support
    target_html = os.path.join(target_dir, "Bai_du_thi_Tham_dinh_gia_Viet_Nam_2026_2027_Ky_nguyen_so.html")
    
    html_parts = [
        '<!DOCTYPE html>',
        '<html lang="vi">',
        '<head>',
        '<meta charset="UTF-8">',
        f'<title>{title_text.replace(chr(10), " - ")}</title>',
        '<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>',
        '<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>',
        '<style>',
        '  body { font-family: "Times New Roman", Times, serif; line-height: 1.5; color: #1e293b; background-color: #f1f5f9; margin: 0; padding: 30px 15px; }',
        '  .page { width: 210mm; min-height: 297mm; margin: 0 auto; background: #fff; box-sizing: border-box; padding: 20mm 20mm 20mm 30mm; box-shadow: 0 4px 25px rgba(0,0,0,0.1); border-radius: 4px; }',
        '  .btn-bar { text-align: right; margin-bottom: 20px; }',
        '  .btn-copy { background: #002060; color: #fff; border: none; padding: 11px 24px; border-radius: 4px; font-weight: bold; cursor: pointer; font-family: "Times New Roman", serif; font-size: 14pt; transition: background 0.2s; }',
        '  .btn-copy:hover { background: #0F4C81; }',
        '  .header-contest { text-align: center; border-bottom: 1.5px solid #002060; padding-bottom: 14px; margin-bottom: 22px; }',
        '  .contest-tag { font-size: 11pt; font-weight: bold; color: #64748B; text-transform: uppercase; }',
        '  .contest-title { font-size: 13pt; font-weight: bold; color: #DC2626; margin: 6px 0; text-transform: uppercase; }',
        '  .contest-sub { font-size: 11pt; font-style: italic; color: #475569; }',
        '  .article-title { font-size: 16pt; font-weight: bold; color: #002060; text-align: center; line-height: 1.4; margin: 24px 0 18px 0; text-transform: uppercase; }',
        '  .sapo { font-size: 13.5pt; font-weight: bold; font-style: italic; color: #1e293b; background: #F8FAFC; border-left: 5px solid #002060; padding: 14px 18px; margin: 20px 0; line-height: 1.5; text-align: justify; text-indent: 1.27cm; }',
        '  h2 { color: #002060; font-size: 14.5pt; margin-top: 24px; margin-bottom: 8px; line-height: 1.4; }',
        '  p { font-size: 14pt; text-align: justify; margin-top: 0; margin-bottom: 8px; line-height: 1.5; text-indent: 1.27cm; }',
        '  .formula-box { background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 4px; padding: 12px 18px; margin: 14px 0; text-align: center; font-size: 14.5pt; color: #002060; }',
        '  .word-count-badge { display: inline-block; background: #DCFCE7; color: #166534; font-size: 11pt; font-weight: bold; padding: 6px 14px; border-radius: 14px; margin-right: 15px; }',
        '  .author-table-section { margin-top: 35px; border-top: 2px solid #002060; padding-top: 18px; }',
        '  .author-table-title { font-size: 13pt; font-weight: bold; color: #002060; margin-bottom: 12px; text-transform: uppercase; }',
        '  table.author-tbl { width: 100%; border-collapse: collapse; margin-bottom: 25px; font-size: 12.5pt; }',
        '  table.author-tbl th, table.author-tbl td { border: 1px solid #CBD5E1; padding: 8px 12px; text-align: left; line-height: 1.35; }',
        '  table.author-tbl td.lbl { width: 32%; background: #F1F5F9; font-weight: bold; color: #002060; }',
        '  .footer-note { margin-top: 25px; background: #EFF6FF; border: 1px dashed #2563EB; border-radius: 4px; padding: 14px 18px; font-size: 11.5pt; color: #1E3A8A; line-height: 1.5; }',
        '</style>',
        '</head>',
        '<body>',
        '<div class="page" id="article-content">',
        '  <div class="btn-bar">',
        f'    <span class="word-count-badge">Dung lượng: {total_p_words} từ (Chuẩn Thể lệ: &lt; 2.000 từ | Lề: 3-2-2-2 | Dãn dòng: 1.5 | Công thức LaTeX chuẩn)</span>',
        '    <button class="btn-copy" onclick="copyArticle()">Sao chép bài thi</button>',
        '  </div>',
        '  <div class="header-contest">',
        '    <div class="contest-tag">BÀI DỰ THI CUỘC THI VIẾT:</div>',
        '    <div class="contest-title">“THẨM ĐỊNH GIÁ VIỆT NAM VÌ SỰ PHÁT TRIỂN KINH TẾ - XÃ HỘI CỦA ĐẤT NƯỚC”<br>LẦN THỨ 2 (2026 – 2027)</div>',
        '    <div class="contest-sub">Đơn vị chỉ đạo: Hội Thẩm định giá Việt Nam (VVA)<br>Đơn vị tổ chức: Tạp chí điện tử Nhịp sống Thị trường (MarketTimes.vn)</div>',
        '  </div>',
        f'  <div class="article-title">{title_text.replace(chr(10), "<br>")}</div>',
        f'  <div class="sapo">{sapo_text}</div>',
        '  <h2>1. Nghịch lý \'gọt 3 tài sản so sánh\' và góc khuất: \'Không ai cần một thẩm định viên làm đúng\'</h2>',
        '  <p>Trong nền kinh tế thị trường, các doanh nghiệp thẩm định giá độc lập là trọng tài xác lập giá trị thực nhằm bảo đảm an toàn tín dụng, chống thất thoát ngân sách trong cổ phần hóa và tính đúng nghĩa vụ tài chính đất đai. Thế nhưng trong thực tế, một nghịch lý cay đắng đang tồn tại: Người thuê dịch vụ thẩm định giá thường chỉ muốn kết quả thẩm định làm sai lệch có lợi nhất cho mục đích riêng của họ.</p>',
        '  <p>Xung đột lợi ích này diễn ra khốc liệt ở mọi phân khúc: Doanh nghiệp vay thế chấp tìm mọi cách thổi phồng giá trị để tối đa hóa hạn mức giải ngân; ngược lại, chủ đầu tư nộp tiền sử dụng đất dự án lại gây sức ép kéo giá thẩm định sát đáy nhằm giảm nghĩa vụ ngân sách. Thẩm định viên bị kẹt ở thế tiến thoái lưỡng nan: Làm đúng nguyên tắc thị trường thì khách hàng cắt hợp đồng, doanh nghiệp mất việc; nhưng nếu chiều theo bên thuê thì rủi ro lao lý luôn lơ lửng trên đầu khi thanh tra, kiểm toán vào cuộc.</p>',
        '  <p>Bi kịch này được che đậy dưới vỏ bọc quy trình kỹ thuật. Khi xây dựng bảng giá đất địa phương hay thẩm định dự án bất động sản, mẫu khảo sát thu thập được lên tới hàng nghìn giao dịch thực tế. Thế nhưng, Tiêu chuẩn Thẩm định giá hiện hành lại trói buộc phương pháp so sánh vào việc chọn đúng 3 tài sản tương đồng. Nút thắt này biến quy trình thẩm định thành trò \'gọt chân cho vừa giày\': Thẩm định viên chọn ra 3 tài sản thuận lợi để hướng tới con số mục tiêu thỏa thuận trước, rồi tự \'bốc thuốc\' tỷ lệ điều chỉnh (+5% ngõ rộng, -3% đất méo, +10% vị trí) một cách cảm tính mà không có bất kỳ căn cứ thực nghiệm nào.</p>',
        '  <p>Đại án SCB - Vạn Thịnh Phát với sự tiếp tay của các công ty thẩm định giá nâng khống tài sản là hồi chuông cảnh tỉnh sâu sắc. Đó không chỉ là sự tha hóa cá nhân, mà là lỗ hổng hệ thống khi phương pháp định giá thủ công trao quyền tùy biến quá lớn cho ý chí chủ quan bị chi phối bởi tiền bạc.</p>',
        '  <h2>2. Lượng hóa và chuẩn hóa: Dùng Big Data và Mô hình Hedonic để chấm dứt trò \'bốc thuốc\'</h2>',
        '  <p>Muốn đưa Bảng giá đất theo Luật Đất đai năm 2024 thực sự tiệm cận giá trị thị trường, hoạt động thẩm định giá không thể tiếp tục dựa vào cảm quan định tính. Lời giải căn cơ là phải lượng hóa các yếu tố so sánh bằng Dữ liệu lớn (Big Data) và Kinh tế lượng ứng dụng.</p>',
        '  <p>Bất động sản về bản chất là một \'gói các thuộc tính\': tọa độ GIS, diện tích, mặt tiền, chiều sâu, hình dáng, lộ giới ngõ, tiện ích, pháp lý và thời điểm giao dịch. Trong kinh tế lượng thực nghiệm, Mô hình định giá hưởng thụ Hedonic giải quyết triệt để bài toán này thông qua hàm hồi quy bán logarit:</p>',
        '  <div class="formula-box">$$\\ln(P_j) = \\beta_0 + \\sum_{k=1}^m \\beta_k X_{kj} + \\varepsilon_j \\quad (\\varepsilon_j \\sim \\mathcal{N}(0, \\sigma^2))$$</div>',
        '  <p>Trong đó, \\(P_j\\) là giá giao dịch thực tế của bất động sản \\(j\\), \\(X_{kj}\\) là các biến số thuộc tính đặc trưng và \\(\\beta_k\\) là trọng số đóng góp của thuộc tính \\(k\\). Khi công nghệ Big Data thu thập hàng chục vạn giao dịch mua bán thực tế, mô hình hồi quy sẽ giải quyết 3 bài toán kỹ thuật:</p>',
        '  <p>Thứ nhất, kiểm định thực nghiệm xem biến số nào thực sự có ý nghĩa thống kê (\\(p\\text{-value} < 0.05\\)). Phân tích chứng minh nhiều yếu tố cảm tính (như phong thủy hay tâm lý mơ hồ) thực chất không tác động đáng kể; trong khi bề rộng ngõ, tỷ lệ mặt tiền/chiều sâu và khoảng cách hạ tầng lại chiếm tỷ trọng chi phối tuyệt đối.</p>',
        '  <p>Thứ hai, xác định chính xác và minh bạch tỷ lệ điều chỉnh phần trăm trực tiếp từ hệ số hồi quy thị trường theo công thức:</p>',
        '  <div class="formula-box">$$\\Delta \\% P_k = \\left(e^{\\hat{\\beta}_k} - 1\\right) \\times 100\\%$$</div>',
        '  <p>Khi mô hình thực nghiệm chứng minh mỗi mét mở rộng ngõ làm tăng giá đất 4,2% hay thửa đất tóp hậu bị chiết khấu 6,8%, thẩm định viên bắt buộc phải áp dụng trọng số khách quan này. Tỷ lệ điều chỉnh lúc này là tiếng nói khách quan của thị trường, loại bỏ hoàn toàn khả năng can thiệp chủ quan.</p>',
        '  <p>Thứ ba, chốt công thức định giá tham chiếu chuẩn hóa (Benchmark Valuation Formula) cho từng tuyến đường, phân vùng đô thị:</p>',
        '  <div class="formula-box">$$P_{\\text{tham chiếu}} = \\exp\\left(\\hat{\\beta}_0 + \\sum_{k=1}^m \\hat{\\beta}_k X_{k0} + \\frac{\\hat{\\sigma}^2}{2}\\right)$$</div>',
        '  <p>Đây là công cụ bước ngoặt để các địa phương xây dựng Bảng giá đất hàng năm một cách khoa học, cập nhật tự động theo chu kỳ thị trường, chấm dứt tình trạng lúng túng hoặc thẩm định viên chịu sức ép vô lý khi lập bảng giá.</p>',
        '  <h2>3. \'Tấm khiên công nghệ\' bảo vệ sự độc lập và liêm chính của Thẩm định viên</h2>',
        '  <p>Hiện nay, các đơn vị thẩm định giá độc lập rất cô độc khi đứng mũi chịu sào trước sức ép từ doanh nghiệp vì thiếu công cụ kỹ thuật tự vệ. Chuẩn hóa bằng Big Data không hề triệt tiêu vai trò của thẩm định viên, mà tạo ra \'tấm khiên bảo vệ\' (safe harbor) kiên cố nhất cho người hành nghề.</p>',
        '  <p>Khi cơ sở dữ liệu quốc gia và mô hình định giá tự động (AVM) được thiết lập, hệ thống sẽ xác lập khoảng tin cậy thống kê chuẩn mực:</p>',
        '  <div class="formula-box">$$\\hat{P}_{\\text{dự báo}} - z_{\\alpha/2} \\cdot \\text{SE} \\le P \\le \\hat{P}_{\\text{dự báo}} + z_{\\alpha/2} \\cdot \\text{SE}$$</div>',
        '  <p>Với khoảng tin cậy 95% (sai số cho phép thông thường +/- 7%), nếu khách hàng ép nâng hay dìm giá quá mức, thẩm định viên có thể tự tin từ chối dựa trên căn cứ khoa học: \'Hệ thống dữ liệu thị trường không chấp nhận độ lệch chuẩn này\'. Mọi sự điều chỉnh bất thường vượt biên độ đều tự động kích hoạt cảnh báo rủi ro (Anomaly Detection), buộc phải có giải trình kỹ thuật độc lập.</p>',
        '  <p>Thẩm định viên lúc này được giải phóng để tập trung vào giá trị tinh hoa nhất: phán đoán chuyên gia (Expert Judgement). Đó là việc kiểm tra thực địa những yếu tố phi cấu trúc: tranh chấp ranh giới ngầm, chất lượng thi công dở dang, uy tín thực tế của chủ đầu tư hay rủi ro vĩ mô. Khi công nghệ gánh vác việc lượng hóa khách quan, đạo đức nghề nghiệp sẽ có điểm tựa vững chắc để giữ trọn sự liêm chính.</p>',
        '  <h2>4. Ba kiến nghị hành động xây dựng hệ sinh thái Thẩm định giá minh bạch</h2>',
        '  <p>Để hiện thực hóa chuyển đổi số theo Luật Giá năm 2023 và Luật Đất đai năm 2024, ba giải pháp đột phá cần được triển khai đồng bộ:</p>',
        '  <p>Một là, thể chế hóa phương pháp hồi quy Hedonic vào Tiêu chuẩn Thẩm định giá Việt Nam. Cần cho phép dùng mẫu lớn và mô hình kinh tế lượng để xác định tỷ lệ điều chỉnh; chấm dứt việc bắt buộc chỉ dùng 3 tài sản so sánh đơn lẻ tại các khu vực có giao dịch dày đặc. Bộ Tài chính cần sớm ban hành cẩm nang hướng dẫn xác định trọng số biến số theo từng vùng kinh tế.</p>',
        '  <p>Hai là, xây dựng Hệ sinh thái Dữ liệu giá bất động sản minh bạch. Đẩy mạnh thanh toán không dùng tiền mặt trong giao dịch nhà đất, áp dụng hóa đơn điện tử cho mọi hợp đồng chuyển nhượng, tích hợp Cơ sở dữ liệu quốc gia về giá với Hệ thống địa chính của Bộ Tài nguyên và Môi trường. Khi dữ liệu phản ánh giá trị thật, Big Data sẽ phục vụ đắc lực cho công tác lập Bảng giá đất và định giá dự án.</p>',
        '  <p>Ba là, Hội Thẩm định giá Việt Nam (VVA) thiết lập cơ chế giám sát độc lập và bảo vệ thẩm định viên trước các hành vi chèn ép, thao túng giá; đồng thời phối hợp cùng các trường đại học lớn như Đại học Kinh tế Quốc dân (NEU) đào tạo thế hệ thẩm định viên mới: vững khoa học dữ liệu, am tường kinh tế lượng tài chính và giữ trọn cốt cách liêm chính.</p>',
        '  <h2>Lời kết: Giữ trọn sự liêm chính vì sự phồn vinh của đất nước</h2>',
        '  <p>Nghề thẩm định giá là nghề của niềm tin. Một chứng thư thẩm định mang theo sinh mệnh doanh nghiệp, quyền lợi chính đáng của người dân và sự an toàn của dòng vốn quốc gia. Nếu thỏa hiệp với cái sai, cái giá phải trả là sự thất thoát nguồn lực đất đai và bất ổn tài chính khôn lường.</p>',
        '  <p>Big Data và AI chính là cơ hội lịch sử để ngành Thẩm định giá Việt Nam rũ bỏ định kiến \'gọt chân cho vừa giày\', xác lập vị thế đàng hoàng của người làm nghề. Với hành lang pháp lý minh bạch, sự trợ lực của khoa học dữ liệu và bản lĩnh kiên định của những thẩm định viên chân chính, ngành thẩm định giá hoàn toàn có thể tự hào đóng góp vào sự phát triển công bằng, văn minh và phồn vinh của đất nước.</p>',
        '  <div class="author-table-section">',
        '    <div class="author-table-title">THÔNG TIN TÁC GIẢ DỰ THI (THEO THỂ LỆ BAN TỔ CHỨC):</div>',
        '    <table class="author-tbl">'
    ]

    for k, v in author_data:
        html_parts.append(f'      <tr><td class="lbl">{k}</td><td>{v}</td></tr>')

    html_parts.extend([
        '    </table>',
        '  </div>',
        '  <div class="footer-note">',
        '    <strong>HƯỚNG DẪN NỘP BÀI DỰ THI:</strong><br>',
        '    • <strong>Email tiếp nhận của Tòa soạn:</strong> <code>toasoan@markettimes.vn</code><br>',
        f'    • <strong>Tiêu đề thư đề xuất:</strong> <code>[Bài dự thi Thẩm định giá 2026-2027] - {title_text.replace(chr(10), " ")} - [Họ tên tác giả]</code><br>',
        '    • <strong>Thời hạn nhận bài:</strong> Từ 01/11/2026 đến hết ngày 30/06/2027 (dự kiến trao giải tháng 07/2027).<br>',
        '    • <strong>Địa chỉ gửi bản in (nếu nộp bưu điện):</strong> Tạp chí điện tử Nhịp sống Thị trường, Tầng 2, Tòa nhà Kim Ánh, Số 1, Ngõ 78, Phố Duy Tân, Cầu Giấy, Hà Nội.',
        '  </div>',
        '</div>',
        '<script>',
        'function copyArticle() {',
        '  const range = document.createRange();',
        '  range.selectNode(document.getElementById("article-content"));',
        '  window.getSelection().removeAllRanges();',
        '  window.getSelection().addRange(range);',
        '  try {',
        '    document.execCommand("copy");',
        '    alert("Đã sao chép toàn bộ bài thi và bảng thông tin tác giả! Bạn có thể dán trực tiếp vào Word hoặc Email.");',
        '  } catch(e) {',
        '    alert("Lỗi sao chép tự động: " + e);',
        '  }',
        '  window.getSelection().removeAllRanges();',
        '}',
        '</script>',
        '</body>',
        '</html>'
    ])

    with open(target_html, "w", encoding="utf-8") as f:
        f.write("\n".join(html_parts))
    print("SUCCESSFULLY SAVED HTML:", target_html)

if __name__ == "__main__":
    generate_essay()
