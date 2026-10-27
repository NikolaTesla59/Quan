# -*- coding: utf-8 -*-
import sys
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = docx.Document()

# Page Margins (Standard Academic A4)
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.2)
    section.right_margin = Inches(1.0)

# Colors
COLOR_NAVY = RGBColor(27, 54, 93)      # #1B365D
COLOR_SLATE = RGBColor(51, 92, 141)    # #335C8D
COLOR_CHARCOAL = RGBColor(38, 38, 38)
COLOR_MUTED = RGBColor(89, 89, 89)

def format_paragraph(p, space_before=0, space_after=4, line_spacing=1.25, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    p.alignment = align

def add_title(text, level=1):
    p = doc.add_paragraph()
    if level == 1:
        format_paragraph(p, space_before=14, space_after=6, align=WD_ALIGN_PARAGRAPH.LEFT)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(13.5)
        run.font.bold = True
        run.font.color.rgb = COLOR_NAVY
    elif level == 2:
        format_paragraph(p, space_before=10, space_after=4, align=WD_ALIGN_PARAGRAPH.LEFT)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = COLOR_SLATE
    elif level == 3:
        format_paragraph(p, space_before=6, space_after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = COLOR_CHARCOAL
    return p

def add_body(text, bold_prefix=None, italic=False):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=0, space_after=4, line_spacing=1.25, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_CHARCOAL
    r_body = p.add_run(text)
    r_body.font.name = 'Times New Roman'
    r_body.font.size = Pt(11)
    r_body.font.italic = italic
    r_body.font.color.rgb = COLOR_CHARCOAL
    return p

def add_caption(text):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=6, space_after=3, align=WD_ALIGN_PARAGRAPH.LEFT)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10)
    run.font.bold = True
    run.font.color.rgb = COLOR_NAVY
    return p

def set_cell_background(cell, hex_color):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=70, bottom=70, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_styled_table(rows, cols, col_widths=None):
    tbl = doc.add_table(rows=rows, cols=cols)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tblPr = tbl._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="1B365D"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="1B365D"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)
    if col_widths:
        for r in tbl.rows:
            for idx, w in enumerate(col_widths):
                r.cells[idx].width = Inches(w)
    return tbl

def populate_row(row, values, is_header=False, bg_color=None, align_right_start=1):
    for idx, val in enumerate(values):
        cell = row.cells[idx]
        set_cell_margins(cell)
        if bg_color:
            set_cell_background(cell, bg_color)
        elif is_header:
            set_cell_background(cell, "1B365D")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if (idx >= align_right_start and not is_header and idx != 0) else (WD_ALIGN_PARAGRAPH.CENTER if is_header else WD_ALIGN_PARAGRAPH.LEFT)
        format_paragraph(p, space_before=2, space_after=2, line_spacing=1.0)
        run = p.add_run(str(val))
        run.font.name = 'Times New Roman'
        run.font.size = Pt(9.0 if not is_header else 9.5)
        run.font.bold = is_header or (idx == 0 and not is_header and any(w in str(val) for w in ["Tổng", "CAR", "NPL", "RAROC", "LLCR"]))
        run.font.color.rgb = RGBColor(255, 255, 255) if is_header else COLOR_CHARCOAL

# ==============================================================================
# COVER PAGE
# ==============================================================================
p_cov1 = doc.add_paragraph()
format_paragraph(p_cov1, space_before=10, space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
r = p_cov1.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO — TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN (NEU)\nVIỆN ĐÀO TẠO SAU ĐẠI HỌC — VIỆN NGÂN HÀNG - TÀI CHÍNH")
r.font.name = 'Times New Roman'
r.font.size = Pt(11.5)
r.font.bold = True
r.font.color.rgb = COLOR_NAVY

p_cov2 = doc.add_paragraph()
format_paragraph(p_cov2, space_before=36, space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
r = p_cov2.add_run("TIỂU LUẬN KHOA HỌC HỌC PHẦN: QUẢN TRỊ RỦI RO NGÂN HÀNG")
r.font.name = 'Times New Roman'
r.font.size = Pt(14)
r.font.bold = True
r.font.color.rgb = COLOR_SLATE

p_cov3 = doc.add_paragraph()
format_paragraph(p_cov3, space_before=16, space_after=8, align=WD_ALIGN_PARAGRAPH.CENTER)
r = p_cov3.add_run("SO SÁNH MÔ HÌNH VÀ THỰC TRẠNG QUẢN TRỊ RỦI RO TÍN DỤNG\nGIỮA AGRIBANK VÀ MB GIAI ĐOẠN 2020–2025")
r.font.name = 'Times New Roman'
r.font.size = Pt(17)
r.font.bold = True
r.font.color.rgb = COLOR_NAVY

p_cov4 = doc.add_paragraph()
format_paragraph(p_cov4, space_before=6, space_after=36, align=WD_ALIGN_PARAGRAPH.CENTER)
r = p_cov4.add_run("ĐỐI THOẠI HỌC THUẬT VỀ THỂ CHẾ SỞ HỮU, KHẨU VỊ RỦI RO, KHOAN DUNG PHÁP LÝ,\nKIỂM TRA SỨC CHỊU ĐỰNG (STRESS TEST) VÀ MÔ PHỎNG CHUẨN MỰC IFRS 9")
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r.font.italic = True
r.font.color.rgb = COLOR_SLATE

p_cov5 = doc.add_paragraph()
format_paragraph(p_cov5, space_before=40, space_after=4, align=WD_ALIGN_PARAGRAPH.LEFT)
r = p_cov5.add_run("Học viên thực hiện:\tNhóm Nghiên cứu Quản trị Rủi ro Ngân hàng (Khóa Cao học 32/33)\nChuyên ngành:\t\tTài chính - Ngân hàng\nGiảng viên phụ trách:\tPGS.TS. Giảng viên cao cấp Bộ môn Quản trị NHTM\nHồ sơ số liệu kèm theo:\tPhan_tich_RRTD_Agribank_MB_2020-2025_v2.xlsx (7 Sheet, 261 công thức, Stress Test & IFRS 9)")
r.font.name = 'Times New Roman'
r.font.size = Pt(10.5)

p_cov6 = doc.add_paragraph()
format_paragraph(p_cov6, space_before=30, space_after=10, align=WD_ALIGN_PARAGRAPH.CENTER)
r = p_cov6.add_run("Hà Nội, Năm 2026")
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r.font.bold = True

doc.add_page_break()

# ==============================================================================
# TÓM TẮT HỌC THUẬT (EXECUTIVE ABSTRACT)
# ==============================================================================
add_title("TÓM TẮT NGHIÊN CỨU (EXECUTIVE ABSTRACT)")
add_body(
    "Nghiên cứu này thực hiện phân tích so sánh chuyên sâu về mô hình và thực trạng quản trị rủi ro tín dụng (RRTD) giữa Ngân hàng Nông nghiệp và Phát triển Nông thôn Việt Nam (Agribank - đại diện cho mô hình NHTM 100% vốn Nhà nước với định hướng chính sách) và Ngân hàng TMCP Quân đội (MB - đại diện cho mô hình tập đoàn tài chính đa năng có sở hữu quân đội và tư nhân) xuyên suốt giai đoạn 2020–2025. Dựa trên bộ dữ liệu tài chính kiểm toán chuẩn hóa 6 năm liên tục (với 18 báo cáo tài chính và thường niên gốc), nghiên cứu áp dụng khung lý thuyết kinh điển về Bất cân xứng thông tin (Stiglitz & Weiss, 1981), Lý thuyết Chi phí đại diện (Jensen & Meckling, 1976), Khung an toàn vốn Basel II/III và Mô hình tổn thất tín dụng kỳ vọng (IFRS 9 ECL). Nghiên cứu giải quyết 4 phát hiện học thuật cốt lõi: (1) Xu hướng đảo chiều NPL bề mặt nhưng phân kỳ sâu sắc về chất lượng: Agribank giảm bền vững từ 1,85% (2023) về 1,17% (2025) nhờ chiến lược phòng thủ và xóa nợ thực chất; MB giảm từ 1,60% về 1,29% nhờ đợt xóa nợ kỹ thuật 11.200 tỷ đồng và hiệu ứng pha loãng mẫu số từ tăng trưởng tín dụng kỷ lục 39,6%; (2) Kỹ thuật làm mượt lợi nhuận qua dự phòng (Cookie Jar Accounting): MB trích lập mạnh trong giai đoạn 2021-2022 (LLCR đạt đỉnh 268%) rồi hoàn nhập 4.800 tỷ đồng nợ cơ cấu Covid-19 năm 2023, khiến chi phí tín dụng gộp thực chất lên tới 2,03% (thay vì 1,24% số ròng); (3) Sự phân hóa khẩu vị rủi ro qua chỉ số RAROC: MB duy trì RAROC vượt trội 34%–50% nhưng đánh đổi bằng bộ đệm LLCR sụt giảm dưới 100% và nợ nhóm 2 tăng vọt, trong khi Agribank duy trì RAROC ổn định 10%–16% với danh mục nông nghiệp phân tán cao; (4) Kết quả Stress Test và Mô phỏng IFRS 9: Trong kịch bản vĩ mô Cực đoan 2026, CAR của Agribank bị suy giảm sát ngưỡng 8,5% do bộ đệm vốn mỏng; trong khi MB đối mặt với khoảng cách dự phòng trích thiếu lên tới 12.278 tỷ đồng dưới chuẩn IFRS 9, khiến tỷ lệ CAR sụt giảm gần 100 bps do rủi ro tập trung BĐS, TPDN và cho vay tiêu dùng tín chấp MCredit."
)
add_body(
    "Từ khóa: Quản trị rủi ro tín dụng; Bất cân xứng thông tin; Thể chế sở hữu; Khoan dung pháp lý; Kiểm tra sức chịu đựng (Stress Testing); IFRS 9 ECL; RAROC; Agribank; MB.",
    bold_prefix="Từ khóa học thuật: "
)

# ==============================================================================
# MỤC LỤC CHI TIẾT
# ==============================================================================
add_title("MỤC LỤC NỘI DUNG")
toc_items = [
    ("LỜI MỞ ĐẦU", "3"),
    ("CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ KHUNG PHÂN TÍCH RỦI RO TÍN DỤNG", "4"),
    ("  1.1. Các lý thuyết kinh tế tài chính kinh điển về rủi ro tín dụng ngân hàng", "4"),
    ("  1.2. Khung phân tích (Analytical Framework) và Cơ chế Khoan dung pháp lý", "6"),
    ("  1.3. Khung pháp lý điều chỉnh và chu kỳ can thiệp chính sách 2020–2025", "7"),
    ("  1.4. Thực trạng rủi ro tín dụng toàn hệ thống ngân hàng", "8"),
    ("CHƯƠNG 2. MÔ HÌNH VÀ THỂ CHẾ QUẢN TRỊ RỦI RO TÍN DỤNG TẠI AGRIBANK VÀ MB", "9"),
    ("  2.1. Agribank: Thể chế NHTM Nhà nước và Quản trị rủi ro phân tán", "9"),
    ("  2.2. MB: Thể chế Tập đoàn Tài chính và Quản trị tập trung", "10"),
    ("  2.3. Ma trận đối chiếu chuyên sâu hai mô hình quản trị rủi ro", "11"),
    ("CHƯƠNG 3. HỆ THỐNG TIÊU CHÍ VÀ PHƯƠNG PHÁP ĐỊNH LƯỢNG ĐÁNH GIÁ RỦI RO TÍN DỤNG", "12"),
    ("CHƯƠNG 4. PHÂN TÍCH THỰC TRẠNG VÀ MÔ HÌNH HÓA ĐỊNH LƯỢNG RỦI RO TÍN DỤNG GIAI ĐOẠN 2020–2025", "13"),
    ("  4.1. Quy mô tín dụng, nợ xấu và phân rã tốc độ tăng trưởng (Decomposition)", "13"),
    ("  4.2. Bộ đệm dự phòng, chi phí tín dụng và cơ chế Cookie Jar Accounting", "15"),
    ("  4.3. Nợ nhóm 2, nợ cơ cấu và áp lực nợ xấu tiềm ẩn", "17"),
    ("  4.4. Đo lường hiệu quả tài chính điều chỉnh theo rủi ro (RAROC)", "18"),
    ("  4.5. Cơ cấu danh mục, mức độ tập trung ngành và an toàn vốn (CAR)", "19"),
    ("  4.6. Kiểm tra sức chịu đựng vĩ mô (Macroeconomic Stress Testing 2026)", "20"),
    ("  4.7. Mô phỏng định lượng tác động chuyển đổi Chuẩn mực Quốc tế IFRS 9 ECL", "22"),
    ("CHƯƠNG 5. PHÂN TÍCH TÌNH HUỐNG THỰC TIỄN DƯỚI KHUNG COSO 2013 VÀ TAM GIÁC GIAN LẬN", "24"),
    ("  5.1. Agribank – Vụ án Lifepro (Chi nhánh Nam Hà Nội): Lỗ hổng kiểm soát kép và bẫy TSBĐ", "24"),
    ("  5.2. MB – Vụ án cán bộ Chi nhánh Gia Lai: Tam giác gian lận và sự suy giảm tuyến 2-3", "25"),
    ("  5.3. MB – Cú sốc chất lượng tài sản năm 2023: Khủng hoảng thanh khoản TPDN và hiệu ứng CIC", "26"),
    ("  5.4. MB – Đỉnh nợ xấu Quý III/2025 và Chiến dịch làm sạch danh mục Quý IV/2025", "27"),
    ("CHƯƠNG 6. ĐÁNH GIÁ, ĐỐI THOẠI HỌC THUẬT VÀ SO SÁNH HAI MÔ HÌNH", "28"),
    ("CHƯƠNG 7. HỆ THỐNG KIẾN NGHỊ VÀ HÀM Ý CHÍNH SÁCH QUẢN TRỊ NÂNG CAO", "30"),
    ("  7.1. Đối với Ngân hàng Nhà nước", "30"),
    ("  7.2. Đối với Agribank", "31"),
    ("  7.3. Đối với Ngân hàng TMCP Quân đội (MB)", "32"),
    ("KẾT LUẬN", "33"),
    ("TÀI LIỆU THAM KHẢO", "34"),
    ("PHỤ LỤC. BẢNG TỔNG HỢP VÀ ĐỐI CHIẾU THÔNG TIN", "36"),
]

for title, page in toc_items:
    p_toc = doc.add_paragraph()
    format_paragraph(p_toc, space_before=1, space_after=1, line_spacing=1.1)
    r1 = p_toc.add_run(title)
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(10)
    r1.font.bold = not title.startswith("  ")
    r2 = p_toc.add_run(f"\t{page}")
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(10)

doc.add_page_break()

# ==============================================================================
# LỜI MỞ ĐẦU
# ==============================================================================
add_title("LỜI MỞ ĐẦU")
add_body(
    "1. Tính cấp thiết của đề tài. Rủi ro tín dụng (RRTD) là rủi ro trọng yếu nhất đe dọa trực tiếp đến sự an toàn, tính thanh khoản và khả năng duy trì hoạt động liên tục của hệ thống ngân hàng thương mại. Giai đoạn 2020–2025 chứng kiến những biến động kinh tế vĩ mô chưa từng có tiền lệ tại Việt Nam: đại dịch Covid-19 làm đứt gãy chuỗi cung ứng; thị trường bất động sản và trái phiếu doanh nghiệp (TPDN) rơi vào khủng hoảng thanh khoản năm 2022–2023; và hàng loạt cơ chế khoan dung pháp lý (regulatory forbearance) thông qua các Thông tư 01/2020/TT-NHNN, Thông tư 02/2023/TT-NHNN nhằm hoãn ghi nhận nợ xấu. Trong bối cảnh đó, việc so sánh mô hình quản trị rủi ro giữa Agribank (NHTM 100% vốn Nhà nước) và MB (NHTMCP đa năng hàng đầu) không chỉ mang ý nghĩa thực tiễn đối với công tác điều hành ngân hàng mà còn cung cấp một điển cứu học thuật đắt giá về sự tương tác giữa thể chế sở hữu, hàm mục tiêu tối ưu hóa, và hành vi quản trị rủi ro tín dụng.",
    bold_prefix="Tính cấp thiết học thuật: "
)
add_body(
    "2. Mục tiêu nghiên cứu và Câu hỏi nghiên cứu. Mục tiêu tổng quát của đề tài là bóc tách bản chất, cơ chế vận hành và hiệu quả thực chất của mô hình quản trị RRTD tại Agribank và MB giai đoạn 2020–2025, từ đó đề xuất hệ thống giải pháp nâng cao năng lực an toàn vốn và phòng ngừa rủi ro theo chuẩn mực quốc tế. Đề tài tập trung giải quyết 3 câu hỏi nghiên cứu (Research Questions):",
    bold_prefix="Mục tiêu nghiên cứu: "
)
add_body(
    "  • RQ1: Cơ cấu sở hữu và định vị chiến lược (NHTM Nhà nước tập trung tam nông vs NHTMCP đa năng theo đuổi ROE) tạo ra sự khác biệt như thế nào về khẩu vị rủi ro tín dụng và cấu trúc danh mục tài sản?\n"
    "  • RQ2: Các chính sách khoan dung pháp lý (Thông tư 01, Thông tư 02) và kỹ thuật kế toán (quản trị dự phòng, xóa nợ kỹ thuật, phân loại liên đới CIC) đã tác động như thế nào đến tính xác thực của các chỉ số nợ xấu bề mặt giai đoạn 2020–2025?\n"
    "  • RQ3: Dưới các cú sốc vĩ mô giả định (Stress Testing 2026) và khi chuyển đổi bắt buộc sang Chuẩn mực Kế toán Quốc tế IFRS 9 (ECL), mô hình quản trị rủi ro nào bộc lộ tính dễ bị tổn thương cao hơn về an toàn vốn và chi phí dự phòng?"
)
add_body(
    "3. Phương pháp nghiên cứu và Đóng góp mới. Đề tài áp dụng phương pháp nghiên cứu định tính kết hợp phân tích định lượng chuyên sâu: (i) Phương pháp kế toán tài chính pháp y (Forensic Accounting) để bóc tách các khoản hoàn nhập dự phòng, nợ xóa nội bảng và nợ cơ cấu; (ii) Phương pháp phân rã toán học (Decomposition Analysis) để định lượng hiệu ứng quy mô tín dụng và hiệu ứng chất lượng tài sản đối với NPL; (iii) Phương pháp kiểm tra sức chịu đựng vĩ mô (Macroeconomic Stress Testing) theo khuyến nghị Basel II/III; và (iv) Phương pháp mô phỏng tổn thất tín dụng kỳ vọng (IFRS 9 Simulation). Toàn bộ dữ liệu được trích xuất trực tiếp từ 18 báo cáo tài chính kiểm toán và báo cáo thường niên gốc của hai ngân hàng.",
    bold_prefix="Phương pháp tiếp cận: "
)

# ==============================================================================
# CHƯƠNG 1
# ==============================================================================
add_title("CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ KHUNG PHÂN TÍCH RỦI RO TÍN DỤNG")

add_title("1.1. Các lý thuyết kinh tế tài chính kinh điển về rủi ro tín dụng ngân hàng", level=2)
add_body(
    "Trong kinh tế học tài chính hiện đại, rủi ro tín dụng không chỉ đơn thuần là xác suất khách hàng vi phạm nghĩa vụ trả nợ, mà là kết quả của sự tương tác phức tạp giữa các bên tham gia thị trường trong điều kiện thông tin không hoàn hảo và cấu trúc khuyến khích bất cân xứng. Nghiên cứu này thiết lập cơ sở phân tích dựa trên bốn trụ cột lý thuyết kinh điển:",
    bold_prefix="Khung lý thuyết nền tảng: "
)
add_body(
    "1. Lý thuyết Bất cân xứng thông tin (Information Asymmetry Theory - Stiglitz & Weiss, 1981). Stiglitz và Weiss chứng minh rằng trong thị trường tín dụng, lãi suất cho vay không thể đóng vai trò cân bằng thị trường theo cách thông thường do tồn tại hai hiện tượng: Nghịch tuyển (Adverse Selection) và Rủi ro đạo đức (Moral Hazard). Khi ngân hàng nâng lãi suất cho vay để bù đắp rủi ro, những người vay có dự án an toàn sẽ chủ động rút lui, chỉ còn lại những người vay có dự án rủi ro cao sẵn sàng chấp nhận lãi suất lớn (Nghịch tuyển). Đồng thời, lãi suất cao thúc đẩy người vay chuyển dịch vốn sang các dự án có độ mạo hiểm cao hơn để kỳ vọng lợi nhuận bù đắp chi phí lãi (Rủi ro đạo đức). Do đó, ngân hàng tối ưu hóa lợi nhuận bằng cách áp dụng cơ chế Giới hạn hạn mức tín dụng (Credit Rationing) thay vì tăng lãi suất. Lý thuyết này giải thích sâu sắc sự khác biệt giữa Agribank (sử dụng tài sản bảo đảm truyền thống là đất đai để triệt tiêu nghịch tuyển) và MB (áp dụng mô hình chấm điểm tự động và khai thác hệ sinh thái số để giảm thiểu bất cân xứng thông tin).",
    bold_prefix="a. Lý thuyết Bất cân xứng thông tin: "
)
add_body(
    "2. Lý thuyết Chi phí đại diện và Cấu trúc sở hữu (Agency Theory - Jensen & Meckling, 1976). Lý thuyết Người đại diện phân tích sự xung đột lợi ích giữa Người quản lý (Ban điều hành) và Chủ sở hữu (Cổ đông). Trong ngành ngân hàng, cấu trúc sở hữu quyết định trực tiếp đến hàm mục tiêu của nhà quản trị. Tại Ngân hàng 100% vốn Nhà nước như Agribank, Ban điều hành chịu sự ràng buộc bởi các mục tiêu kép: vừa bảo toàn vốn Nhà nước, vừa thực thi chính sách an sinh xã hội và tài trợ phát triển nông nghiệp theo chỉ đạo của Chính phủ. Do nguy cơ chịu trách nhiệm hành chính và hình sự khi để xảy ra thất thoát tài sản công là cực kỳ nghiêm trọng, ban điều hành và cán bộ tín dụng Agribank có xu hướng bài xích rủi ro (Risk-averse), tạo ra sức ì trong phê duyệt tín dụng và dựa dẫm tuyệt đối vào tài sản thế chấp. Ngược lại, tại NHTMCP có sở hữu tư nhân và quân đội như MB, ban điều hành chịu áp lực gay gắt từ cổ đông và thị trường chứng khoán về tỷ suất sinh lời trên vốn (ROE), tăng trưởng lợi nhuận và định giá cổ phiếu (P/B). Áp lực này thúc đẩy MB thiết lập các gói đãi ngộ gắn liền với KPI tăng trưởng tín dụng, kích thích khẩu vị rủi ro chấp nhận đầu tư vào các phân khúc lợi nhuận cao như cho vay tiêu dùng (MCredit) và trái phiếu bất động sản.",
    bold_prefix="b. Lý thuyết Chi phí đại diện: "
)
add_body(
    "3. Khung Hiệp ước Vốn Basel (Basel Capital Accord - Basel II & Basel III). Khung an toàn vốn Basel thiết lập ba trụ cột tương hỗ: Trụ cột 1 (Minimum Capital Requirements) quy định tỷ lệ an toàn vốn tối thiểu (CAR >= 8%) tính trên Tài sản có rủi ro (RWA). Basel II cho phép ngân hàng lựa chọn giữa Phương pháp Tiêu chuẩn (Standardized Approach - SA) với hệ số rủi ro cố định theo quy định của nhà điều hành, hoặc Phương pháp Xếp hạng nội bộ (Internal Ratings-Based - IRB: Foundation IRB và Advanced IRB), trong đó ngân hàng tự lượng hóa Xác suất vỡ nợ (Probability of Default - PD), Tỷ lệ tổn thất khi vỡ nợ (Loss Given Default - LGD) và Dư nợ tại thời điểm vỡ nợ (Exposure at Default - EAD). Trụ cột 2 (Supervisory Review Process - ICAAP) yêu cầu ngân hàng tự đánh giá mức đủ vốn nội bộ thông qua việc thực hiện Kiểm tra sức chịu đựng (Stress Testing) định kỳ đối với các cú sốc vĩ mô. Trụ cột 3 (Market Discipline) bắt buộc minh bạch hóa thông tin về chất lượng danh mục và mức độ an toàn vốn nhằm tạo áp lực giám sát từ thị trường.",
    bold_prefix="c. Khung Hiệp ước Vốn Basel: "
)
add_body(
    "4. Chuẩn mực Kế toán Quốc tế IFRS 9 vs Chuẩn mực Việt Nam (VAS / Thông tư 11/2021). Đây là sự chuyển dịch mô hình mang tính bước ngoặt từ Mô hình tổn thất đã phát sinh (Incurred Loss Model) sang Mô hình tổn thất tín dụng kỳ vọng (Expected Credit Loss - ECL). Theo VAS và Thông tư 11/2021/TT-NHNN, dự phòng chỉ được trích lập khi khoản nợ đã phát sinh dấu hiệu quá hạn hoặc bằng chứng khách quan về vi phạm hợp đồng (nợ nhóm 2 trích 5%, nhóm 3 trích 20%, nhóm 4 trích 50%, nhóm 5 trích 100% sau khi trừ giá trị TSBĐ; dự phòng chung 0,75% cho nhóm 1-4). Ngược lại, IFRS 9 phân loại toàn bộ tài sản tài chính thành 3 giai đoạn (Three Stages):",
    bold_prefix="d. Mô hình Tổn thất kỳ vọng IFRS 9 ECL: "
)
add_body(
    "  • Stage 1 (Performing): Các khoản nợ không có gia tăng rủi ro tín dụng đáng kể (SICR) kể từ khi khởi tạo -> Trích lập dự phòng tổn thất kỳ vọng 12 tháng: ECL(12m) = EAD x PD(12m) x LGD.\n"
    "  • Stage 2 (Underperforming - SICR): Các khoản nợ có sự gia tăng rủi ro tín dụng đáng kể (như quá hạn trên 30 ngày, nợ được cơ cấu lại, hoặc suy giảm xếp hạng tín dụng nội bộ) -> Bắt buộc trích lập dự phòng tổn thất trọn vòng đời: Lifetime ECL = EAD x PD(lifetime) x LGD.\n"
    "  • Stage 3 (Credit-impaired): Nợ xấu / suy giảm giá trị (quá hạn trên 90 ngày) -> Trích lập Lifetime ECL: ECL(lifetime) = EAD x 100% x LGD.\n"
    "Sự khác biệt cốt lõi nằm ở Stage 2: IFRS 9 yêu cầu trích lập toàn bộ tổn thất trọn đời ngay khi rủi ro gia tăng, trong khi Thông tư 11 chỉ trích 5% sau khi đã khấu trừ tài sản bảo đảm. Đây là nguyên nhân tạo ra khoảng cách trích lập khổng lồ (Provisioning Gap) giữa chuẩn mực trong nước và quốc tế."
)

add_title("1.2. Khung phân tích (Analytical Framework) và Cơ chế Khoan dung pháp lý", level=2)
add_body(
    "Để đánh giá toàn diện mô hình quản trị RRTD, nghiên cứu thiết lập Khung phân tích đa tầng (Multi-layered Analytical Framework) kết nối quan hệ nhân quả: Thể chế sở hữu và Khung pháp lý vĩ mô -> Xác định Khẩu vị rủi ro và Cấu trúc danh mục -> Quyết định mức độ tổn thương trước Cú sốc kinh tế -> Dẫn đến Biểu hiện nợ xấu nội bảng và Nhu cầu trích lập dự phòng -> Tác động cuối cùng đến An toàn vốn (CAR) và Hiệu quả hoạt động điều chỉnh theo rủi ro (RAROC).",
    bold_prefix="Khung phân tích đa tầng: "
)
add_body(
    "Đặc biệt, nghiên cứu đưa vào khái niệm Khoan dung pháp lý (Regulatory Forbearance). Về mặt bản chất kinh tế, các văn bản như Thông tư 01/2020 và Thông tư 02/2023 cho phép các TCTD cơ cấu lại thời hạn trả nợ và giữ nguyên nhóm nợ thực chất là sự can thiệp hành chính tạm thời nhằm hoãn ghi nhận tổn thất tín dụng. Cơ chế này giúp doanh nghiệp tránh bị rơi vào nhóm nợ xấu trên hệ thống thông tin tín dụng quốc gia (CIC), nhưng đồng thời tạo ra hiện tượng Đảo nợ kỹ thuật (Loan Evergreening) và làm sai lệch số liệu nợ xấu nội bảng, biến các khoản nợ thực tế đã mất khả năng thanh toán thành nợ tiềm ẩn.",
    bold_prefix="Bản chất kinh tế của Khoan dung pháp lý: "
)

add_title("1.3. Khung pháp lý điều chỉnh và chu kỳ can thiệp chính sách 2020–2025", level=2)
add_caption("Bảng 1. Hệ thống văn bản quy phạm pháp luật điều chỉnh rủi ro tín dụng giai đoạn 2020–2025")

tbl1 = create_styled_table(rows=9, cols=3, col_widths=[2.0, 1.4, 3.2])
tbl1_data = [
    ["Văn bản quy phạm", "Hiệu lực & Hết hạn", "Tác động kinh tế và cơ chế điều chỉnh số liệu"],
    ["Thông tư 01/2020/TT-NHNN", "13/3/2020 → 17/5/2021", "Cơ cấu lại thời hạn trả nợ, miễn giảm lãi và giữ nguyên nhóm nợ cho khách hàng chịu ảnh hưởng bởi Covid-19."],
    ["Thông tư 03/2021/TT-NHNN", "17/5/2021 → 07/9/2021", "Yêu cầu bắt đầu trích lập dự phòng cho nợ cơ cấu Covid theo lộ trình 3 năm: tối thiểu 30% (2021), 60% (2022) và 100% (2023)."],
    ["Thông tư 14/2021/TT-NHNN", "07/9/2021 → 30/6/2022", "Kéo dài thời gian cơ cấu nợ Covid đến 30/6/2022, duy trì cơ chế giữ nguyên nhóm nợ."],
    ["Thông tư 11/2021/TT-NHNN", "Từ 15/3/2022 (Thay thế TT 02/2013)", "Quy chuẩn phân loại tài sản có, mức trích, phương pháp trích lập dự phòng rủi ro và sử dụng dự phòng để xử lý rủi ro."],
    ["Thông tư 02/2023/TT-NHNN", "24/4/2023 → 31/12/2024", "Cơ cấu lại thời hạn trả nợ và giữ nguyên nhóm nợ hỗ trợ khách hàng gặp khó khăn kinh tế; lộ trình trích dự phòng 50% (2023) và 100% (2024)."],
    ["Thông tư 41/2016/TT-NHNN", "Từ 01/01/2020", "Quy định tỷ lệ an toàn vốn (CAR) tối thiểu 8% đối với ngân hàng theo phương pháp chuẩn hóa (Basel II Standardized Approach)."],
    ["Nghị quyết 42/2017/QH14", "15/8/2017 → 31/12/2023", "Thí điểm xử lý nợ xấu, cho phép quyền thu giữ tài sản bảo đảm của TCTD; sau 31/12/2023 hết hiệu lực tạo khoảng trống pháp lý."],
    ["Luật Các TCTD 2024", "Hiệu lực từ 01/7/2024", "Luật hóa một số cơ chế xử lý nợ nhưng không kế thừa trọn vẹn quyền thu giữ TSBĐ của NQ 42; siết tỷ lệ sở hữu và giới hạn cấp tín dụng."],
]
for idx, rdata in enumerate(tbl1_data):
    populate_row(tbl1.rows[idx], rdata, is_header=(idx==0), align_right_start=3)

add_title("1.4. Thực trạng rủi ro tín dụng toàn hệ thống ngân hàng", level=2)
add_body(
    "Giai đoạn 2020–2025 ghi nhận sự biến động dữ dội của chu kỳ chất lượng tài sản toàn hệ thống. Tỷ lệ nợ xấu nội bảng toàn hệ thống tăng từ 1,69% (2020) lên đỉnh điểm 4,55% (cuối 2023) khi tính cả các ngân hàng thương mại thuộc diện kiểm soát đặc biệt (SCB, Đông Á, CBBank, OceanBank, GPBank). Nếu loại trừ các ngân hàng yếu kém, mặt bằng nợ xấu nội bảng của các ngân hàng bình thường duy trì quanh mức 1,8% – 2,2%. Đáng chú ý, nợ xấu gộp (bao gồm nợ nội bảng, nợ bán cho VAMC chưa xử lý và nợ cơ cấu tiềm ẩn nguy cơ chuyển nhóm) đã vượt ngưỡng 6,0% vào cuối năm 2023 trước khi giảm nhẹ về quanh 4,5% vào cuối năm 2025.",
    bold_prefix="Bức tranh rủi ro hệ thống: "
)
add_caption("Bảng 2. Diễn biến nợ xấu và nợ tiềm ẩn toàn hệ thống ngân hàng (2020–2025)")

tbl2 = create_styled_table(rows=5, cols=7, col_widths=[2.4, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
tbl2_data = [
    ["Chỉ tiêu toàn hệ thống (%)", "2020", "2021", "2022", "2023", "2024", "2025"],
    ["NPL nội bảng (toàn hệ thống theo NHNN)", "1,69%", "1,49%", "2,00%", "4,55%", "4,20%", "3,80%"],
    ["NPL mặt bằng ngân hàng bình thường", "1,52%", "1,35%", "1,60%", "1,95%", "1,88%", "1,85%"],
    ["Nợ nhóm 2 / Tổng dư nợ", "1,45%", "1,20%", "1,80%", "2,35%", "1,90%", "1,35%"],
    ["Nợ xấu gộp (bao gồm nợ cơ cấu & VAMC)", "3,81%", "3,75%", "4,50%", "6,15%", "5,40%", "4,50%"],
]
for idx, rdata in enumerate(tbl2_data):
    populate_row(tbl2.rows[idx], rdata, is_header=(idx==0), align_right_start=1)

# ==============================================================================
# CHƯƠNG 2
# ==============================================================================
add_title("CHƯƠNG 2. MÔ HÌNH VÀ THỂ CHẾ QUẢN TRỊ RỦI RO TÍN DỤNG TẠI AGRIBANK VÀ MB")

add_title("2.1. Agribank: Thể chế NHTM Nhà nước và Quản trị rủi ro phân tán", level=2)
add_body(
    "Agribank là định chế tài chính lớn nhất Việt Nam xét về mạng lưới hoạt động với hơn 2.200 chi nhánh và phòng giao dịch trải rộng khắp cả nước. Định vị chiến lược của Agribank gắn liền với sứ mệnh chính trị phục vụ phát triển 'Tam nông' (Nông nghiệp, Nông dân, Nông thôn), với tỷ trọng tín dụng nông nghiệp luôn duy trì từ 61,7% đến 64,1% tổng dư nợ trong suốt giai đoạn 2020–2025. Về mặt thể chế sở hữu, là ngân hàng 100% vốn Nhà nước, cơ chế ra quyết định của Agribank mang tính thủ tục hành chính cao, chịu sự giám sát trực tiếp của Ngân hàng Nhà nước, Bộ Tài chính và Kiểm toán Nhà nước.",
    bold_prefix="Định vị thể chế và Danh mục: "
)
add_body(
    "Mô hình tổ chức quản trị rủi ro của Agribank vận hành theo cơ chế phân tán: Hội đồng thành viên phê chuẩn chính sách quản lý rủi ro thông qua Ủy ban Quản lý rủi ro; Khối Quản lý rủi ro tại Hội sở đóng vai trò tham mưu và ban hành hạn mức; tuy nhiên, quyền thẩm định và phê duyệt tín dụng phần lớn vẫn được phân cấp mạnh cho các Giám đốc chi nhánh loại 1 và loại 2 theo hạn mức thẩm quyền. Do mạng lưới quá rộng lớn và tính chất địa bàn nông thôn phân tán, việc kiểm soát nội bộ tập trung gặp nhiều rào cản công nghệ. Đặc biệt, tài sản bảo đảm của Agribank chiếm tới 89%–92% là bất động sản nông nghiệp và đất ở nông thôn, tạo ra một danh mục có tính thanh khoản tài sản bảo đảm rất thấp và phụ thuộc nặng nề vào các thủ tục thi hành án tư pháp kéo dài.",
    bold_prefix="Mô hình tổ chức và Công cụ quản trị: "
)

add_title("2.2. MB: Thể chế Tập đoàn Tài chính và Quản trị tập trung", level=2)
add_body(
    "Ngược lại hoàn toàn với Agribank, Ngân hàng TMCP Quân đội (MB) vận hành theo mô hình Tập đoàn Tài chính đa năng (Universal Financial Conglomerate), với ngân hàng mẹ đóng vai trò hạt nhân kết nối chặt chẽ với các công ty con chuyên doanh: MCredit (Tài chính tiêu dùng), MBS (Chứng khoán & Ngân hàng đầu tư), MIC (Bảo hiểm phi nhân thọ), MB Ageas Life (Bảo hiểm nhân thọ) và MBAMC (Quản lý nợ và khai thác tài sản). Cấu trúc sở hữu của MB có sự kết hợp đặc thù giữa các cổ đông quân đội (Viettel, Tổng Công ty Trực thăng, Tổng Công ty Tân Cảng Sài Gòn) và các quỹ đầu tư tài chính tư nhân, tạo ra một động lực tối đa hóa lợi nhuận và hiệu quả vốn (ROE) cực kỳ mạnh mẽ.",
    bold_prefix="Cấu trúc tập đoàn và Khẩu vị mở rộng: "
)
add_body(
    "Về mặt công cụ quản trị, MB là một trong những ngân hàng thương mại tiên phong áp dụng sớm các thông lệ Basel II và triển khai nền tảng ICAAP dựa trên hệ thống công nghệ Oracle Financial Services Analytical Applications (OFSAA). Mô hình phê duyệt tín dụng của MB được tái cấu trúc triệt để theo hướng tập trung hóa: tách rời hoàn toàn Khối Thẩm định và Trung tâm Phê duyệt tín dụng khỏi các Chi nhánh kinh doanh; áp dụng các mô hình chấm điểm tín dụng tự động (Scorecard) và phê duyệt luồng tự động cho các khoản vay cá nhân và bán lẻ. Khẩu vị rủi ro của MB chấp nhận mở rộng mạnh mẽ sang các phân khúc có biên lợi nhuận cao (NIM cao) như cho vay mua nhà dự án, tài trợ chuỗi cung ứng cho các tập đoàn lớn, đầu tư trái phiếu doanh nghiệp (chứng khoán nợ TCKT đạt đỉnh 66.279 tỷ đồng năm 2022) và tín dụng tiêu dùng tín chấp thông qua MCredit.",
    bold_prefix="Công nghệ tập trung và Đánh đổi rủi ro: "
)

add_title("2.3. Ma trận đối chiếu chuyên sâu hai mô hình quản trị rủi ro", level=2)
add_caption("Bảng 3. Ma trận đối chiếu cấu trúc thể chế và mô hình 3 tuyến phòng vệ giữa Agribank và MB")

tbl3 = create_styled_table(rows=9, cols=3, col_widths=[1.8, 2.5, 2.5])
tbl3_data = [
    ["Tiêu chí đối chiếu", "Agribank (Mô hình NHTM Nhà nước)", "MB (Mô hình Tập đoàn Tài chính Đa năng)"],
    ["1. Thể chế sở hữu & Hàm mục tiêu", "100% vốn Nhà nước; hàm mục tiêu kép: chính sách tam nông + bảo toàn vốn công.", "Sở hữu hỗn hợp Quân đội & Tư nhân; hàm mục tiêu tối đa hóa ROE và giá trị vốn hóa."],
    ["2. Khẩu vị rủi ro (Risk Appetite)", "Bảo thủ, phân tán cao (Granular); bài xích rủi ro pháp lý; biên lãi mỏng (NIM thấp).", "Chấp nhận rủi ro cao để tối ưu NIM; tập trung vào bán lẻ, BĐS, TPDN và cho vay tiêu dùng."],
    ["3. Tuyến phòng vệ 1 (Kinh doanh)", "Chi nhánh vừa bán hàng vừa thẩm định thực tế; phân cấp hạn mức tín dụng theo địa bàn.", "Tách rời bán hàng (RM) và thẩm định độc lập; phê duyệt tập trung tại Hội sở & Hub."],
    ["4. Tuyến phòng vệ 2 (Quản trị rủi ro)", "Khối QLRR giám sát theo hạn mức hành chính; mô hình chấm điểm nội bộ mang tính bổ trợ.", "Khối QLRR do CRO phụ trách; vận hành ICAAP/OFSAA; tự động hóa phê duyệt bằng scorecard."],
    ["5. Tuyến phòng vệ 3 (Kiểm toán nội bộ)", "Kiểm toán nội bộ trực thuộc Ban Kiểm soát; mạng rộng khiến tần suất kiểm tra tại chỗ thấp.", "Kiểm toán nội bộ dựa trên rủi ro (Risk-based Audit); ứng dụng phân tích dữ liệu lớn (Audit Analytics)."],
    ["6. Bản chất Tài sản bảo đảm", "Chiếm 89%–92% là BĐS nông nghiệp, đất ở nông thôn; thanh khoản thị trường thứ cấp thấp.", "Đa dạng: BĐS dự án đô thị, cổ phiếu niêm yết, dòng tiền dự án; tỷ lệ tín chấp cao tại MCredit."],
    ["7. Cơ chế khuyến khích (Incentives)", "Chế độ lương hành chính nhà nước; trách nhiệm cá nhân hình sự nặng nề nếu nợ xấu phát sinh.", "Lương thưởng gắn chặt KPI doanh số và ROE; chấp nhận chi phí dự phòng như chi phí kinh doanh."],
]
for idx, rdata in enumerate(tbl3_data):
    populate_row(tbl3.rows[idx], rdata, is_header=(idx==0), align_right_start=3)

# ==============================================================================
# CHƯƠNG 3
# ==============================================================================
add_title("CHƯƠNG 3. HỆ THỐNG TIÊU CHÍ VÀ PHƯƠNG PHÁP ĐỊNH LƯỢNG ĐÁNH GIÁ RỦI RO TÍN DỤNG")
add_body(
    "Để thực hiện đối chiếu định lượng khoa học và nhất quán giữa hai ngân hàng có quy mô và cấu trúc sở hữu khác biệt, nghiên cứu xây dựng hệ thống 15 chỉ tiêu định lượng phân tầng theo 5 nhóm rủi ro chuẩn tắc của Basel Committee on Banking Supervision (BCBS):",
    bold_prefix="Khung chỉ tiêu chuẩn hóa: "
)
add_caption("Bảng 4. Hệ thống tiêu chí định lượng đánh giá rủi ro tín dụng ngân hàng thương mại")

tbl4 = create_styled_table(rows=10, cols=3, col_widths=[1.5, 2.5, 2.8])
tbl4_data = [
    ["Nhóm tiêu chí", "Chỉ tiêu định lượng", "Công thức và Ý nghĩa học thuật"],
    ["I. Chất lượng tài sản bề mặt", "1. Tỷ lệ nợ xấu nội bảng (NPL)\n2. Tỷ lệ nợ nhóm 2 (Watchlist)", "• NPL = Nợ nhóm 3-5 / Tổng dư nợ. Đo lường tỷ lệ nợ vi phạm hợp đồng.\n• Nhóm 2 / Dư nợ: Chỉ báo cảnh báo sớm rủi ro chuyển nhóm."],
    ["II. Chất lượng tài sản thực chất", "3. NPL điều chỉnh toàn diện\n4. Tỷ lệ nợ xấu gộp", "• NPL điều chỉnh = (Nợ xấu + Nợ cơ cấu TT02) / Dư nợ.\n• NPL gộp = (Nợ xấu + Nợ cơ cấu + Nợ VAMC + Nợ đã xóa) / Dư nợ."],
    ["III. Bộ đệm phòng thủ & Chi phí", "5. Tỷ lệ bao phủ nợ xấu (LLCR)\n6. Chi phí tín dụng (Credit Cost)\n7. Tỷ lệ xóa nợ rủi ro (Write-off)", "• LLCR = (Dự phòng cụ thể + chung) / Nợ xấu. Đo khả năng hấp thụ tổn thất.\n• Credit Cost = Chi phí dự phòng / Dư nợ bình quân (đối chiếu gộp và ròng).\n• Write-off rate = Nợ xóa bằng quỹ dự phòng / Dư nợ bình quân."],
    ["IV. Hiệu quả vốn rủi ro", "8. Lợi nhuận điều chỉnh rủi ro (RAROC)\n9. Hệ số an toàn vốn (CAR Basel II)", "• RAROC = (Lợi nhuận ròng - Tổn thất dự kiến) / Vốn kinh tế (RWA x 8%).\n• CAR = Vốn tự có hợp lệ / Tổng tài sản có rủi ro (RWA) theo TT 41."],
    ["V. Rủi ro tập trung danh mục", "10. Tỷ trọng Bất động sản\n11. Dư nợ Trái phiếu DN (TPDN)", "• Dư nợ BĐS / Tổng dư nợ: Đo lường rủi ro tập trung ngành chu kỳ.\n• Dư nợ TPDN / Dư nợ tín dụng: Đo lường rủi ro tín dụng danh mục đầu tư."],
]
for idx, rdata in enumerate(tbl4_data):
    populate_row(tbl4.rows[idx], rdata, is_header=(idx==0), align_right_start=3)

# ==============================================================================
# CHƯƠNG 4
# ==============================================================================
add_title("CHƯƠNG 4. PHÂN TÍCH THỰC TRẠNG VÀ MÔ HÌNH HÓA ĐỊNH LƯỢNG RỦI RO TÍN DỤNG GIAI ĐOẠN 2020–2025")

add_title("4.1. Quy mô tín dụng, nợ xấu và phân rã tốc độ tăng trưởng (Decomposition)", level=2)
add_body(
    "Giai đoạn 2020–2025 ghi nhận sự phân kỳ rõ nét về tốc độ tăng trưởng quy mô tín dụng giữa hai ngân hàng. Dư nợ cho vay khách hàng của Agribank tăng từ 1,21 triệu tỷ đồng (2020) lên 1,98 triệu tỷ đồng (2025), tương ứng tốc độ tăng trưởng kép hàng năm (CAGR) đạt 10,2%/năm. Trong khi đó, MB ghi nhận tốc độ mở rộng tín dụng bùng nổ, đưa dư nợ cho vay từ 298.297 tỷ đồng (2020) lên 1.084.000 tỷ đồng (2025), đạt tốc độ tăng trưởng bình quân 29,4%/năm (riêng năm 2025 tăng kỷ lục 39,6% nhờ tiếp nhận chuyển giao bắt buộc OceanBank và được cấp hạn mức tín dụng vượt trội).",
    bold_prefix="Quy mô và Tốc độ mở rộng: "
)
add_caption("Bảng 5. Quy mô dư nợ, nợ xấu và tỷ lệ NPL của Agribank và MB (2020–2025) (Tỷ đồng, %)")

tbl5 = create_styled_table(rows=12, cols=7, col_widths=[2.4, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
tbl5_data = [
    ["Chỉ tiêu phân tích", "2020", "2021", "2022", "2023", "2024", "2025"],
    ["Agribank: Dư nợ cho vay KH", "1.213.958", "1.316.473", "1.444.802", "1.547.468", "1.720.000", "1.976.369"],
    ["Agribank: Tăng trưởng dư nợ (%)", "8,1%", "8,4%", "9,7%", "7,1%", "11,1%", "14,7%"],
    ["Agribank: Nợ xấu (chuỗi chính)", "21.500", "23.433", "24.706", "28.628", "27.229", "23.124"],
    ["Agribank: NPL chuỗi chính (%)", "1,77%", "1,78%", "1,71%", "1,85%", "1,58%", "1,17%"],
    ["Agribank: NPL hợp nhất ban đầu (%)", "1,77%", "1,87%", "1,81%", "1,90%", "1,72%", "1,25%"],
    ["MB: Dư nợ cho vay KH", "298.297", "363.555", "460.574", "611.049", "776.658", "1.084.000"],
    ["MB: Tăng trưởng dư nợ (%)", "19,2%", "21,9%", "26,7%", "32,7%", "27,1%", "39,6%"],
    ["MB: Nợ xấu hợp nhất", "3.248", "3.272", "5.031", "9.805", "12.580", "14.027"],
    ["MB: NPL hợp nhất (%)", "1,09%", "0,90%", "1,09%", "1,60%", "1,62%", "1,29%"],
    ["MB: NPL riêng ngân hàng mẹ (%)", "0,92%", "0,68%", "0,83%", "1,40%", "1,45%", "1,13%"],
    ["Chênh lệch NPL (Agribank - MB HN)", "+0,68%", "+0,88%", "+0,62%", "+0,25%", "-0,04%", "-0,12%"],
]
for idx, rdata in enumerate(tbl5_data):
    populate_row(tbl5.rows[idx], rdata, is_header=(idx==0), align_right_start=1)

add_body(
    "Năm 2025 ghi nhận một bước ngoặt lịch sử: Tỷ lệ NPL công bố của Agribank lần đầu tiên thấp hơn NPL hợp nhất của MB (1,17% so với 1,29%, chênh lệch -0,12 điểm %). Tuy nhiên, để trả lời câu hỏi liệu chất lượng tài sản của MB có thực sự được cải thiện hay không, nghiên cứu áp dụng Phương pháp Phân rã Toán học (Decomposition Analysis) đối với biến động NPL của MB năm 2025:",
    bold_prefix="Phân tích Phân rã Toán học mức giảm NPL của MB năm 2025: "
)
add_body(
    "Ta có công thức phân rã biến động tỷ lệ nợ xấu:\n"
    "$$\\Delta NPL = NPL_t - NPL_{t-1} = \\frac{NPD_t}{Loan_t} - \\frac{NPD_{t-1}}{Loan_{t-1}} = \\underbrace{\\frac{\\Delta NPD_t}{Loan_t}}_{\\text{Hiệu ứng Tử số (Chất lượng tài sản)}} - \\underbrace{NPL_{t-1} \\times \\frac{\\Delta Loan_t}{Loan_t}}_{\\text{Hiệu ứng Mẫu số (Tăng trưởng quy mô)}}$$\n"
    "Trong năm 2025 của MB:\n"
    "  • Tỷ lệ NPL giảm từ 1,62% về 1,29% (mức giảm ròng \\(\\Delta NPL = -0,33\\) điểm %).\n"
    "  • Hiệu ứng Mẫu số: Do dư nợ tăng trưởng bùng nổ 39,6%, hiệu ứng pha loãng mẫu số đã tự động kéo giảm NPL một lượng bằng: \\(1,62\\% \\times \\frac{307.342}{1.084.000} = -0,46\\) điểm %.\n"
    "  • Hiệu ứng Tử số: Nợ xấu tuyệt đối vẫn tăng ròng từ 12.580 tỷ lên 14.027 tỷ (tăng +1.447 tỷ), đóng góp làm tăng NPL: \\(\\frac{+1.447}{1.084.000} = +0,13\\) điểm %.\n"
    "  • Đặc biệt, nếu MB không thực hiện xóa nợ kỹ thuật 11.200 tỷ đồng trong năm 2025 bằng quỹ dự phòng, số dư nợ xấu thực tế cuối năm sẽ là 25.227 tỷ đồng, tương ứng tỷ lệ NPL chưa xử lý lên tới 2,33%.\n"
    "Kết luận học thuật: Mức giảm NPL của MB năm 2025 hoàn toàn là kết quả của việc 'pha loãng quy mô tín dụng' và 'xóa nợ kỹ thuật', chứ không phản ánh sự cải thiện chất lượng tín dụng tự thân."
)

add_title("4.2. Bộ đệm dự phòng, chi phí tín dụng và cơ chế Cookie Jar Accounting", level=2)
add_caption("Bảng 6. Bộ đệm dự phòng (LLCR), chi phí dự phòng và bóc tách Credit Cost (2020–2025)")

tbl6 = create_styled_table(rows=10, cols=7, col_widths=[2.4, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
tbl6_data = [
    ["Chỉ tiêu phân tích", "2020", "2021", "2022", "2023", "2024", "2025"],
    ["Agribank: Tỷ lệ bao phủ nợ xấu (LLCR)", "111,0%", "139,0%", "138,9%", "129,0%", "132,0%", "144,3%"],
    ["Agribank: Chi phí dự phòng RRTD (tỷ)", "18.416", "21.676", "27.172", "24.363", "25.800", "31.808"],
    ["Agribank: Credit Cost (CPDP / Dư nợ BQ)", "1,58%", "1,71%", "1,97%", "1,63%", "1,58%", "1,72%"],
    ["Agribank: Nợ xóa bằng quỹ DP trong năm (tỷ)", "16.500", "18.200", "21.400", "17.800", "24.500", "29.800"],
    ["Agribank: Thu hồi nợ đã xóa ngoại bảng (tỷ)", "8.500", "9.200", "10.317", "11.167", "11.662", "17.397"],
    ["MB: Tỷ lệ bao phủ nợ xấu (LLCR)", "158,9%", "268,0%", "238,0%", "116,0%", "92,0%", "94,0%"],
    ["MB: Chi phí dự phòng RRTD công bố (tỷ)", "6.118", "8.030", "8.048", "6.087", "9.450", "13.744"],
    ["MB: Credit Cost công bố (số ròng)", "2,23%", "2,43%", "1,95%", "1,24%", "1,36%", "1,48%"],
    ["MB: Credit Cost gộp thực chất (sau hoàn nhập)", "2,23%", "2,43%", "1,95%", "2,03%", "1,52%", "1,58%"],
]
for idx, rdata in enumerate(tbl6_data):
    populate_row(tbl6.rows[idx], rdata, is_header=(idx==0), align_right_start=1)

add_body(
    "Nghiên cứu phát hiện bằng chứng điển hình về hành vi Quản trị lợi nhuận qua quỹ dự phòng (Cookie Jar Accounting / Earnings Smoothing) tại MB trong giai đoạn 2021–2023. Trong năm 2021, khi kết quả kinh doanh thuận lợi, MB chủ động trích lập dự phòng vượt mức yêu cầu của NHNN, đẩy tỷ lệ bao phủ nợ xấu (LLCR) lên mức kỷ lục toàn hệ thống 268% và trích trước hạn 100% nợ cơ cấu Covid-19 (vượt lộ trình 3 năm của TT 03). Đến năm 2023, khi thị trường TPDN và BĐS rơi vào đóng băng, MB tiến hành hoàn nhập tới 4.800 tỷ đồng dự phòng từ danh mục cơ cấu Covid. Khoản hoàn nhập này được ghi giảm trực tiếp vào chi phí dự phòng trên báo cáo kết quả kinh doanh, giúp chi phí dự phòng ròng chỉ còn 6.087 tỷ đồng (giảm 24,4%), qua đó 'cứu vãn' lợi nhuận trước thuế năm 2023 đạt 26.306 tỷ đồng. Nếu không có kỹ thuật hoàn nhập này, chi phí dự phòng thực chất của MB năm 2023 lên tới 10.887 tỷ đồng và Credit Cost gộp là 2,03% (thay vì 1,24%). Hệ quả tất yếu là bộ đệm dự phòng LLCR của MB bị sụt giảm thê thảm từ 268% (2021) xuống 116% (2023), và tiếp tục rớt xuống dưới 100% trong hai năm 2024–2025 (92% và 94%).",
    bold_prefix="Bóc tách Kỹ thuật 'Cookie Jar Accounting' của MB: "
)
add_body(
    "Ngược lại, Agribank duy trì một chiến lược phòng thủ kiên định: LLCR luôn được giữ vững trong biên độ an toàn 129%–144%. Đáng chú ý, công tác thu hồi nợ đã xử lý rủi ro ngoại bảng của Agribank đạt hiệu quả phi thường, tăng liên tục từ 8.500 tỷ (2020) lên mức kỷ lục 17.397 tỷ đồng (2025), tương đương bù đắp tới 55% chi phí dự phòng phát sinh trong năm. Điều này cho thấy nợ xấu của Agribank dù tồn đọng lâu năm nhưng có khả năng hoàn nhập tiền mặt thực chất nhờ tài sản bảo đảm là đất đai.",
    bold_prefix="Hiệu quả thu hồi nợ ngoại bảng của Agribank: "
)

add_title("4.3. Nợ nhóm 2, nợ cơ cấu và áp lực nợ xấu tiềm ẩn", level=2)
add_caption("Bảng 7. Nợ nhóm 2, nợ cơ cấu theo thông tư và NPL điều chỉnh toàn diện (2020–2025)")

tbl7 = create_styled_table(rows=8, cols=7, col_widths=[2.4, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
tbl7_data = [
    ["Chỉ tiêu phân tích (Tỷ đồng, %)", "2020", "2021", "2022", "2023", "2024", "2025"],
    ["Agribank: Nợ nhóm 2 (Cần chú ý)", "15.600", "18.500", "24.200", "32.363", "37.914", "27.669"],
    ["Agribank: Tỷ lệ nợ nhóm 2 / Dư nợ", "1,29%", "1,41%", "1,67%", "2,09%", "2,20%", "1,40%"],
    ["Agribank: Dư nợ cơ cấu còn lại (TT01/TT02)", "52.846", "68.300", "21.500", "37.876", "28.450", "7.500"],
    ["Agribank: NPL điều chỉnh (Nợ xấu + Cơ cấu)", "6,12%", "6,97%", "3,20%", "4,30%", "3,24%", "1,55%"],
    ["MB: Nợ nhóm 2 (Cần chú ý)", "2.190", "1.593", "7.809", "13.917", "12.197", "10.210"],
    ["MB: Tỷ lệ nợ nhóm 2 / Dư nợ", "0,73%", "0,44%", "1,70%", "2,28%", "1,57%", "0,94%"],
    ["MB: NPL điều chỉnh (Nợ xấu + Cơ cấu)", "5,28%", "5,91%", "2,09%", "2,39%", "2,03%", "1,40%"],
]
for idx, rdata in enumerate(tbl7_data):
    populate_row(tbl7.rows[idx], rdata, is_header=(idx==0), align_right_start=1)

add_body(
    "Nợ nhóm 2 là hàn thử biểu nhạy bén nhất phản ánh sức khỏe dòng tiền của khách hàng vay. Trong năm 2023, nợ nhóm 2 của MB tăng đột biến 78,2% từ 7.809 tỷ lên 13.917 tỷ đồng (chiếm 2,28% dư nợ), phản ánh áp lực đứt gãy thanh khoản của nhóm khách hàng vay mua nhà và các doanh nghiệp phát hành trái phiếu. Về phía Agribank, nợ nhóm 2 duy trì ở mức cao trong năm 2023–2024 (đỉnh điểm 37.914 tỷ đồng) do ảnh hưởng của bão lũ, hạn hán và dịch bệnh trong ngành nông nghiệp. Tuy nhiên, điểm đặc thù nhất của Agribank là cơ cấu nợ nhóm 5 (nợ có khả năng mất vốn) chiếm tỷ trọng thâm căn cố đế từ 72% đến 78% tổng nợ xấu qua các năm. Nguyên nhân cốt lõi là do tài sản bảo đảm là đất nông nghiệp, đất rừng, việc xử lý thông qua tòa án và thi hành án kéo dài trung bình 3–5 năm khiến các khoản nợ quá hạn lâu ngày chuyển thẳng thành nợ nhóm 5 mà không thể thanh lý dứt điểm.",
    bold_prefix="Bản chất nợ nhóm 2 và Nợ nhóm 5 thâm căn cố đế: "
)

add_title("4.4. Đo lường hiệu quả tài chính điều chỉnh theo rủi ro (RAROC)", level=2)
add_caption("Bảng 8. Lợi nhuận điều chỉnh rủi ro trên vốn kinh tế (RAROC) giai đoạn 2020–2025")

tbl8 = create_styled_table(rows=8, cols=7, col_widths=[2.4, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
tbl8_data = [
    ["Chỉ tiêu RAROC (Tỷ đồng, %)", "2020", "2021", "2022", "2023", "2024", "2025"],
    ["Agribank: Vốn kinh tế ước tính (EC = RWA x 8%)", "97.116", "105.317", "115.584", "123.797", "137.600", "158.400"],
    ["Agribank: Lợi nhuận sau thuế (PAT)", "10.389", "11.624", "17.657", "20.387", "20.800", "24.936"],
    ["Agribank: Tỷ số RAROC = PAT / EC (%)", "10,7%", "11,0%", "15,3%", "16,5%", "15,1%", "15,7%"],
    ["MB: Vốn kinh tế ước tính (EC = RWA x 8%)", "23.863", "29.084", "36.845", "41.881", "62.132", "80.000"],
    ["MB: Lợi nhuận sau thuế (PAT)", "8.606", "13.218", "18.155", "21.053", "23.072", "27.414"],
    ["MB: Tỷ số RAROC = PAT / EC (%)", "36,1%", "45,4%", "49,3%", "50,3%", "37,1%", "34,3%"],
    ["Chênh lệch RAROC (MB − Agribank)", "+25,4%", "+34,4%", "+34,0%", "+33,8%", "+22,0%", "+18,6%"],
]
for idx, rdata in enumerate(tbl8_data):
    populate_row(tbl8.rows[idx], rdata, is_header=(idx==0), align_right_start=1)

add_body(
    "Chỉ số RAROC phơi bày sự khác biệt bản chất giữa hai triết lý ngân hàng: MB đạt tỷ suất RAROC vượt trội (đạt đỉnh 50,3% năm 2023) nhờ tối ưu hóa mô hình kinh doanh tập đoàn và khai thác tối đa đòn bẩy tài chính; tuy nhiên, mức chênh lệch RAROC giữa MB và Agribank có xu hướng thu hẹp nhanh chóng từ 34,4% (2021) xuống còn 18,6% (2025). Sự sụt giảm RAROC của MB phản ánh việc ngân hàng phải gia tăng tài sản có rủi ro (RWA) và tiêu hao vốn kinh tế nhanh hơn tốc độ sinh lời thuần túy khi rủi ro danh mục bắt đầu phát tác.",
    bold_prefix="Đánh giá học thuật về RAROC: "
)

add_title("4.5. Cơ cấu danh mục, mức độ tập trung ngành và an toàn vốn (CAR)", level=2)
add_caption("Bảng 9. Cơ cấu danh mục rủi ro tập trung và Hệ số an toàn vốn (CAR) giai đoạn 2020–2025")

tbl9 = create_styled_table(rows=7, cols=7, col_widths=[2.4, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
tbl9_data = [
    ["Chỉ tiêu tập trung & Vốn", "2020", "2021", "2022", "2023", "2024", "2025"],
    ["Agribank: Tỷ trọng cho vay nông nghiệp", "63,5%", "62,8%", "63,1%", "62,7%", "61,7%", "64,1%"],
    ["Agribank: CAR theo Thông tư 41 (ước tính)", "9,2%", "8,9%", "8,7%", "8,6%", "8,5%", "8,9%"],
    ["MB: Dư nợ Bất động sản & Xây dựng (%)", "12,5%", "13,8%", "15,2%", "16,8%", "17,5%", "18,2%"],
    ["MB: Dư nợ Trái phiếu doanh nghiệp (tỷ)", "25.800", "46.870", "66.279", "47.779", "34.342", "28.500"],
    ["MB: CAR hợp nhất theo Thông tư 41", "10,50%", "11,15%", "11,50%", "11,20%", "11,35%", "11,50%"],
    ["Khoảng cách CAR (MB − Agribank)", "+1,30%", "+2,25%", "+2,80%", "+2,60%", "+2,85%", "+2,60%"],
]
for idx, rdata in enumerate(tbl9_data):
    populate_row(tbl9.rows[idx], rdata, is_header=(idx==0), align_right_start=1)

add_body(
    "Về an toàn vốn (CAR), MB duy trì bộ đệm vững chắc trên 11% nhờ lợi thế tự tích lũy vốn từ nguồn lợi nhuận giữ lại hàng năm và khả năng phát hành cổ phiếu tăng vốn thuận lợi trên thị trường chứng khoán. Ngược lại, Agribank luôn trong tình trạng 'khát vốn', CAR thực tế theo chuẩn Thông tư 41 chỉ dao động quanh mức 8,5% – 9,1% (sát ngưỡng tối thiểu quy định 8,0%). Dù được Quốc hội và Chính phủ phê duyệt bổ sung 17.100 tỷ đồng vốn điều lệ từ ngân sách trong giai đoạn 2023–2024, tốc độ tăng trưởng dư nợ 10–14%/năm đã nhanh chóng tiêu hao bộ đệm vốn này.",
    bold_prefix="Khoảng cách an toàn vốn: "
)

add_title("4.6. Kiểm tra sức chịu đựng vĩ mô (Macroeconomic Stress Testing 2026)", level=2)
add_body(
    "Để đánh giá khả năng chống chịu của hai ngân hàng trước các cú sốc tương lai, nghiên cứu xây dựng mô hình Stress Testing cho năm 2026 theo khuyến nghị Pillar 2 (ICAAP) của Basel II với 3 kịch bản: Cơ sở (GDP 6,5%, Lãi suất ổn định), Tiêu cực (GDP 5,0%, Lãi suất tăng 150 bps, BĐS giảm 10%) và Cực đoan (GDP 3,5%, Lãi suất tăng 300 bps, BĐS đóng băng và giảm 25%).",
    bold_prefix="Thiết kế mô hình Stress Testing: "
)
add_caption("Bảng 10. Kết quả Kiểm tra sức chịu đựng vĩ mô năm 2026 đối với Agribank và MB")

tbl10 = create_styled_table(rows=9, cols=5, col_widths=[2.6, 1.1, 1.1, 1.1, 1.1])
tbl10_data = [
    ["Chỉ tiêu sau Stress Test (Năm 2026)", "Hiện tại 2025", "Kịch bản Cơ sở", "Kịch bản Tiêu cực", "Kịch bản Cực đoan"],
    ["Agribank: NPL dự báo (%)", "1,17%", "1,25%", "1,45%", "1,71%"],
    ["Agribank: Chi phí dự phòng bổ sung (tỷ)", "0", "8.500", "16.200", "26.500"],
    ["Agribank: CAR sau stress (%)", "9,10%", "8,86%", "8,80%", "8,54%"],
    ["Agribank: Thặng dư vốn so với 8,0%", "+1,10%", "+0,86%", "+0,80%", "+0,54%"],
    ["MB: NPL dự báo (%)", "1,29%", "1,29%", "1,49%", "1,73%"],
    ["MB: Chi phí dự phòng bổ sung (tỷ)", "0", "5.200", "12.800", "22.400"],
    ["MB: CAR sau stress (%)", "11,00%", "10,78%", "10,33%", "9,83%"],
    ["MB: Tỷ lệ suy giảm LNTT so kịch bản cơ sở", "0,0%", "0,0%", "-38,7%", "-69,4%"],
]
for idx, rdata in enumerate(tbl10_data):
    populate_row(tbl10.rows[idx], rdata, is_header=(idx==0), align_right_start=1)

add_body(
    "Kết quả Stress Test chỉ ra hai nghịch lý mang tính cấu trúc: (1) Agribank có mức độ tổn thương vốn cao hơn: trong kịch bản Cực đoan, thặng dư vốn của Agribank chỉ còn 0,54 điểm % (sát ngưỡng vi phạm 8,0%), đòi hỏi sự can thiệp khẩn cấp từ ngân sách nhà nước; (2) MB có mức độ nhạy cảm lợi nhuận cao hơn gấp nhiều lần: chi phí dự phòng bổ sung của MB trong kịch bản Cực đoan lên tới 22.400 tỷ đồng, bào mòn tới 69,4% lợi nhuận trước thuế do danh mục BĐS và cho vay tiêu dùng tín chấp chịu cú sốc kép từ lãi suất cao và giá tài sản sụt giảm.",
    bold_prefix="Ý nghĩa học thuật từ Stress Testing: "
)

add_title("4.7. Mô phỏng định lượng tác động chuyển đổi Chuẩn mực Quốc tế IFRS 9 ECL", level=2)
add_caption("Bảng 11. Kết quả mô phỏng tác động chuyển đổi sang Chuẩn mực Quốc tế IFRS 9 năm 2025")

tbl11 = create_styled_table(rows=9, cols=5, col_widths=[2.8, 1.1, 1.1, 1.1, 1.1])
tbl11_data = [
    ["Khoản mục mô phỏng (Tỷ đồng, %)", "Agribank (VAS)", "Agribank (IFRS 9)", "MB (VAS)", "MB (IFRS 9)"],
    ["Dự phòng Stage 1 (Performing)", "14.442", "8.087", "7.948", "7.153"],
    ["Dự phòng Stage 2 (Underperforming - SICR)", "1.383", "22.156", "511", "11.296"],
    ["Dự phòng Stage 3 (Credit-impaired)", "17.542", "9.250", "4.726", "7.014"],
    ["TỔNG DỰ PHÒNG YÊU CẦU", "33.367", "39.493", "13.185", "25.463"],
    ["Khoảng cách dự phòng trích thiếu (Gap)", "—", "6.126", "—", "12.278"],
    ["Tỷ lệ thiếu hụt so với dự phòng hiện hành (%)", "—", "18,4%", "—", "93,1%"],
    ["Tác động khấu trừ trực tiếp vào Vốn CSH", "—", "-4.901", "—", "-9.822"],
    ["Tỷ lệ CAR sau chuyển đổi IFRS 9 (%)", "9,10%", "8,85%", "11,00%", "10,02%"],
]
for idx, rdata in enumerate(tbl11_data):
    populate_row(tbl11.rows[idx], rdata, is_header=(idx==0), align_right_start=1)

add_body(
    "Mô phỏng IFRS 9 chứng minh một phát hiện quan trọng: MB chịu tác động tiêu cực nặng nề hơn Agribank rất nhiều khi chuyển đổi sang chuẩn mực quốc tế. Quy mô dự phòng của MB phải tăng thêm tới 12.278 tỷ đồng (tương ứng mức thiếu hụt 93,1% so với số liệu hiện hành), làm bốc hơi 8,9% vốn chủ sở hữu và kéo tụt CAR gần 100 điểm cơ bản (từ 11,0% xuống 10,02%). Nguyên nhân là do MB có danh mục cho vay tiêu dùng tín chấp tại MCredit và danh mục TPDN có hệ số tổn thất khi vỡ nợ (LGD) rất cao (45%–85%). Ngược lại, Agribank chỉ phải bổ sung 6.126 tỷ đồng (thiếu hụt 18,4%) và CAR chỉ giảm 25 bps, nhờ 89%–92% dư nợ được bảo đảm bằng bất động sản giúp giảm mạnh hệ số LGD ước tính xuống mức 35%.",
    bold_prefix="Bản chất cú sốc IFRS 9: "
)

# ==============================================================================
# CHƯƠNG 5
# ==============================================================================
add_title("CHƯƠNG 5. PHÂN TÍCH TÌNH HUỐNG THỰC TIỄN DƯỚI KHUNG COSO 2013 VÀ TAM GIÁC GIAN LẬN")

add_title("5.1. Agribank – Vụ án Lifepro (Chi nhánh Nam Hà Nội): Lỗ hổng kiểm soát kép và bẫy TSBĐ", level=2)
add_body(
    "1. Diễn biến và Thiệt hại. Giai đoạn 2008–2012, Agribank Chi nhánh Nam Hà Nội đã giải ngân cho Liên doanh Lifepro Việt Nam số tiền vay và phát hành thư tín dụng (L/C) khổng lồ, gây thiệt hại thực tế được tòa án xác định gần 2.500 tỷ đồng. Vụ án đã khiến nguyên Giám đốc chi nhánh và hàng loạt cán bộ tín dụng bị tuyên án hình sự với mức án lên tới 30 năm tù.",
    bold_prefix="Bối cảnh vụ việc: "
)
add_body(
    "2. Phân tích dưới Khung Kiểm soát Nội bộ COSO 2013:\n"
    "  • Môi trường kiểm soát (Control Environment): Bị tê liệt do sự tha hóa quyền lực của người đứng đầu chi nhánh; nguyên tắc 'Tone at the Top' bị phá vỡ hoàn toàn khi ban lãnh đạo chi nhánh chỉ đạo thuộc cấp làm sai lệch hồ sơ.\n"
    "  • Đánh giá rủi ro (Risk Assessment): Bỏ qua hoàn toàn các cảnh báo đỏ (Red Flags) về năng lực tài chính yếu kém của doanh nghiệp có vốn FDI và hồ sơ nhập khẩu máy móc thiết bị có dấu hiệu khai khống.\n"
    "  • Hoạt động kiểm soát (Control Activities): Vi phạm nghiêm trọng nguyên tắc phê duyệt kép (Dual Authorization); giải ngân vượt quyền hạn mức tín dụng; định giá khống tài sản bảo đảm (quyền sử dụng thương hiệu và thiết bị may mặc ngoại nhập).\n"
    "  • Thông tin và Truyền thông: Bưng bít thông tin giữa chi nhánh và Hội sở, không báo cáo kịp thời sự cố tín dụng về hệ thống giám sát tập trung.\n"
    "  • Giám sát (Monitoring): Hoạt động kiểm toán nội bộ của Tuyến 3 hoàn toàn thụ động, chỉ phát hiện sai phạm khi doanh nghiệp đã tẩu tán tài sản ra nước ngoài.\n"
    "Bài học học thuật: Vụ Lifepro là minh chứng kinh điển cho thấy sự phân cấp quản trị quá mức kết hợp với việc dựa dẫm vào TSBĐ không có thanh khoản thực chất sẽ tạo ra những khoản nợ nhóm 5 tồn đọng kéo dài hàng thập kỷ, tiêu hao nguồn lực dự phòng của ngân hàng nhà nước.",
    bold_prefix="Bóc tách Lỗ hổng COSO: "
)

add_title("5.2. MB – Vụ án cán bộ Chi nhánh Gia Lai: Tam giác gian lận và sự suy giảm tuyến 2-3", level=2)
add_body(
    "1. Diễn biến. Giai đoạn 2022–2023, một cán bộ tín dụng tại Chi nhánh Gia Lai của MB đã lợi dụng chức vụ để lập khống hồ sơ vay vốn, giả mạo chữ ký khách hàng và chiếm đoạt hàng chục tỷ đồng của ngân hàng.",
    bold_prefix="Bối cảnh vụ việc: "
)
add_body(
    "2. Phân tích dưới Mô hình Tam giác Gian lận (Fraud Triangle - Cressey, 1953):\n"
    "  • Áp lực (Pressure): Áp lực hoàn thành chỉ tiêu KPI tăng trưởng tín dụng bán lẻ quá gay gắt từ Hội sở thúc đẩy cán bộ tìm kiếm mọi thủ thuật để giải ngân nhanh.\n"
    "  • Cơ hội (Opportunity): Lỗ hổng trong quy trình xác thực thực địa tại các phòng giao dịch xa xôi; việc quản lý mẫu dấu và đối chiếu công chứng bị buông lỏng; cơ chế kiểm tra chéo giữa người lập hồ sơ và người kiểm soát bị hình thức hóa.\n"
    "  • Hợp lý hóa hành vi (Rationalization): Cán bộ tự biện minh rằng khoản vay chỉ là 'đảo nợ tạm thời' để giúp khách hàng duy trì nhóm nợ và sẽ bù đắp khi giải ngân khoản mới.\n"
    "Bài học học thuật: Sự cố này vạch trần mặt trái của chiến lược tăng trưởng nóng tại các NHTMCP: khi mô hình kinh doanh đặt nặng chỉ tiêu doanh số bán lẻ, các chốt chặn của Tuyến phòng vệ 2 (Giám sát tuân thủ) và Tuyến 3 (Kiểm toán nội bộ) rất dễ bị vô hiệu hóa tại cấp cơ sở.",
    bold_prefix="Bóc tách Tam giác Gian lận: "
)

add_title("5.3. MB – Cú sốc chất lượng tài sản năm 2023: Khủng hoảng thanh khoản TPDN và hiệu ứng CIC", level=2)
add_body(
    "Năm 2023, MB đối mặt với cuộc khủng hoảng chất lượng tài sản lớn nhất trong một thập kỷ: Nợ xấu hợp nhất tăng vọt 94,9% lên 9.805 tỷ đồng; Nợ nhóm 2 tăng 78,2% lên 13.917 tỷ đồng. Cú sốc này bắt nguồn từ việc thị trường TPDN đóng băng sau các đại án Tân Hoàng Minh và Vạn Thịnh Phát. MB với quy mô nắm giữ chứng khoán nợ TCKT lên tới 66.279 tỷ đồng (trong đó ~47.100 tỷ đồng thuộc nhóm BĐS và năng lượng) đã chịu áp lực lan truyền thanh khoản cực lớn. Hơn nữa, quy tắc phân loại nợ liên đới theo hệ thống CIC (Khoản 3 Điều 10 Thông tư 11) đã buộc MB phải hạ nhóm nợ của nhiều tập đoàn bất động sản lớn khi các doanh nghiệp này quá hạn tại các ngân hàng khác, làm tăng tỷ lệ NPL của MB thêm 0,37 điểm %.",
    bold_prefix="Cú sốc Lan truyền Thanh khoản: "
)

add_title("5.4. MB – Đỉnh nợ xấu Quý III/2025 và Chiến dịch làm sạch danh mục Quý IV/2025", level=2)
add_body(
    "Tại thời điểm cuối Quý III/2025, nợ xấu của MB đạt đỉnh lịch sử 17.423 tỷ đồng (tương ứng NPL 1,87%, LLCR giảm xuống mức báo động 80%). Tuy nhiên, chỉ trong vòng 3 tháng cuối năm, MB đã thực hiện một chiến dịch 'làm sạch bảng cân đối kế toán' ngoạn mục: giảm ròng 3.396 tỷ đồng nợ xấu, đưa NPL về 1,29%. Nghiên cứu bóc tách cho thấy đợt cải thiện thần tốc này không đến từ sự phục hồi tự nhiên của khách hàng, mà là kết quả của việc MB đẩy mạnh xóa nợ kỹ thuật khoảng 3.500 tỷ đồng trong riêng Quý IV (nâng tổng nợ xóa cả năm lên 11.200 tỷ đồng), kết hợp thu hồi nợ nhóm năng lượng và đẩy mạnh tăng trưởng tín dụng bùng nổ cuối năm.",
    bold_prefix="Chiến dịch Xóa nợ Kỹ thuật Quý IV/2025: "
)

add_caption("Bảng 12. Ma trận đánh giá lỗ hổng Kiểm soát Nội bộ COSO 2013 qua các tình huống thực tiễn")
tbl12 = create_styled_table(rows=6, cols=3, col_widths=[1.8, 2.5, 2.5])
tbl12_data = [
    ["Thành tố COSO 2013", "Agribank (Vụ Lifepro)", "MB (Vụ Gia Lai & Cú sốc 2023)"],
    ["1. Môi trường kiểm soát", "Băng hoại văn hóa tuân thủ; lạm quyền người đứng đầu chi nhánh.", "Áp lực KPI doanh số quá tải; hạ chuẩn thẩm định để tăng trưởng."],
    ["2. Đánh giá rủi ro", "Bỏ qua rủi ro gian lận FDI; không lượng hóa rủi ro dòng tiền.", "Đánh giá thấp rủi ro thanh khoản lan truyền TPDN và hiệu ứng CIC."],
    ["3. Hoạt động kiểm soát", "Phê duyệt kép bị vô hiệu hóa; thẩm định TSBĐ khống.", "Kiểm soát thực địa lỏng lẻo; phụ thuộc mô hình chấm điểm tự động."],
    ["4. Thông tin & Truyền thông", "Báo cáo nội bộ bị bóp méo; thông tin tắc nghẽn giữa CN và Hội sở.", "Dữ liệu CIC cập nhật có độ trễ; cảnh báo sớm EWS chưa phủ hết TPDN."],
    ["5. Hoạt động giám sát", "Kiểm toán nội bộ thụ động; thiếu kiểm tra chuyên đề đột xuất.", "Tuyến 2-3 phát hiện muộn; xử lý rủi ro chủ yếu dựa vào xóa nợ kỹ thuật."],
]
for idx, rdata in enumerate(tbl12_data):
    populate_row(tbl12.rows[idx], rdata, is_header=(idx==0), align_right_start=3)

# ==============================================================================
# CHƯƠNG 6
# ==============================================================================
add_title("CHƯƠNG 6. ĐÁNH GIÁ, ĐỐI THOẠI HỌC THUẬT VÀ SO SÁNH HAI MÔ HÌNH")
add_body(
    "Từ các phân tích thực chứng và mô hình hóa định lượng, nghiên cứu đúc kết cuộc đối thoại học thuật giữa hai mô hình quản trị rủi ro tín dụng đại diện cho hai triết lý ngân hàng tại Việt Nam:",
    bold_prefix="Tổng hợp Đối thoại Học thuật: "
)
add_caption("Bảng 13. So sánh đối chiếu toàn diện hai triết lý quản trị rủi ro tín dụng (Agribank vs MB)")

tbl13 = create_styled_table(rows=8, cols=3, col_widths=[2.0, 2.4, 2.4])
tbl13_data = [
    ["Khía cạnh học thuật", "Agribank (Mô hình Phòng thủ Thể chế)", "MB (Mô hình Đổi mới Thị trường)"],
    ["1. Triết lý quản trị cốt lõi", "Bảo toàn vốn và tuân thủ; chấp nhận chi phí vận hành cao để duy trì mạng lưới.", "Tối đa hóa giá trị cổ đông (ROE); chấp nhận rủi ro tín dụng để đạt lợi nhuận biên."],
    ["2. Cấu trúc danh mục", "Phân tán cao (Granular); 64% nông nghiệp; TSBĐ là đất đai tính thanh khoản chậm.", "Tập trung vào hệ sinh thái bán lẻ, chuỗi BĐS và TPDN; danh mục nhạy cảm vĩ mô."],
    ["3. Hành vi trích lập dự phòng", "Duy trì bộ đệm LLCR ổn định >130%; thu hồi nợ ngoại bảng tạo dòng tiền thật.", "Cookie Jar Accounting: tích lũy dự phòng khi thuận lợi và hoàn nhập khi khó khăn."],
    ["4. Cơ chế hấp thụ cú sốc", "Danh mục phân tán giúp giảm vỡ nợ diện rộng, nhưng CAR thấp là điểm nghẽn sinh tử.", "Bộ đệm vốn CAR vững chắc (>11%), nhưng lợi nhuận bị bào mòn nặng khi sốc xảy ra."],
    ["5. Độ nhạy trước IFRS 9", "Ít bị ảnh hưởng (CAR giảm 25 bps) nhờ TSBĐ đất đai giúp hạ thấp hệ số LGD.", "Chịu tác động rất lớn (CAR giảm gần 100 bps, thiếu 12.278 tỷ DP) do nợ tín chấp cao."],
    ["6. Đánh đổi chiến lược (Trade-off)", "Hy sinh hiệu quả vốn (RAROC thấp 10-16%) để đổi lấy sự ổn định danh mục dài hạn.", "Đạt RAROC cao (34-50%) nhưng đánh đổi bằng việc suy giảm bộ đệm an toàn LLCR."],
    ["7. Rủi ro mô hình lớn nhất", "Rủi ro thanh khoản tài sản bảo đảm và rủi ro chậm trễ công nghệ số hóa.", "Rủi ro tập trung ngành chu kỳ và rủi ro vỡ nợ dây chuyền tại các công ty con."],
]
for idx, rdata in enumerate(tbl13_data):
    populate_row(tbl13.rows[idx], rdata, is_header=(idx==0), align_right_start=3)

# ==============================================================================
# CHƯƠNG 7
# ==============================================================================
add_title("CHƯƠNG 7. HỆ THỐNG KIẾN NGHỊ VÀ HÀM Ý CHÍNH SÁCH QUẢN TRỊ NÂNG CAO")

add_title("7.1. Đối với Ngân hàng Nhà nước", level=2)
add_body(
    "1. Ban hành Lộ trình Bắt buộc áp dụng IFRS 9: Cần khẩn trương ban hành thông tư hướng dẫn triển khai chuẩn mực IFRS 9 đối với các TCTD quy mô lớn, chấm dứt tình trạng trì hoãn nhận diện rủi ro theo mô hình tổn thất đã phát sinh (Incurred Loss).\n"
    "2. Hoàn thiện Khung pháp lý Xử lý Nợ xấu sau Nghị quyết 42: Bổ sung quy định rõ ràng trong Luật Các TCTD về quyền thu giữ hợp pháp tài sản bảo đảm của bên cho vay khi khách hàng vi phạm hợp đồng tín dụng, nhằm tháo gỡ điểm nghẽn thi hành án nợ nhóm 5 của các NHTM Nhà nước.\n"
    "3. Giám sát Rủi ro Tập trung Đa chiều (Multi-dimensional Concentration Limits): Quy định giới hạn cấp tín dụng chặt chẽ hơn đối với nhóm khách hàng lớn có liên quan (Group of Connected Clients), bao gồm cả danh mục cho vay, đầu tư TPDN, bảo lãnh và ủy thác thanh toán."
)

add_title("7.2. Đối với Agribank", level=2)
add_body(
    "1. Xây dựng Hệ thống Cảnh báo sớm (Early Warning System - EWS) bằng Trí tuệ Nhân tạo: Ứng dụng Machine Learning trên dữ liệu lớn dòng tiền chu kỳ nông nghiệp để phát hiện sớm dấu hiệu suy giảm khả năng trả nợ trước khi chuyển nhóm 2.\n"
    "2. Kiểm tra Sức chịu đựng Rủi ro Khí hậu và Thiên tai (Climate Stress Testing): Tích hợp kịch bản biến đổi khí hậu (hạn hán, xâm nhập mặn, bão lũ) vào mô hình định giá tín dụng nông nghiệp theo tiêu chuẩn ESG.\n"
    "3. Đẩy mạnh Áp dụng Phương pháp Xếp hạng Nội bộ (Basel II FIRB/AIRB): Từng bước chuyển đổi từ phương pháp chuẩn hóa sang IRB nhằm tối ưu hóa trọng số rủi ro RWA cho danh mục nông nghiệp phân tán, giải tỏa áp lực tiêu hao vốn tự có.\n"
    "4. Thành lập Trung tâm Khai thác và Bán đấu giá Tài sản Chuyên biệt: Số hóa toàn bộ danh mục tài sản bảo đảm là đất nông nghiệp, liên kết với các sàn giao dịch bất động sản để rút ngắn thời gian phát mại nợ nhóm 5."
)

add_title("7.3. Đối với Ngân hàng TMCP Quân đội (MB)", level=2)
add_body(
    "1. Tái thiết lập Khẩu vị Rủi ro Tập trung đối với Bất động sản và TPDN: Áp dụng trần tỷ trọng cứng cho danh mục TPDN phi ngân hàng (không vượt quá 5% tổng tài sản sinh lời) và danh mục tài trợ dự án BĐS.\n"
    "2. Hoàn thiện Mô hình Định giá Bù đắp Rủi ro (Risk-based Pricing) tại MCredit: Tăng biên lãi suất tương ứng với xác suất vỡ nợ thực tế của từng phân khúc khách hàng tiêu dùng tín chấp, kiểm soát chặt chẽ tỷ lệ chuyển nhóm từ Stage 1 sang Stage 2.\n"
    "3. Nâng cấp Bộ đệm Dự phòng LLCR trở lại trên 120%: Chấm dứt hành vi hoàn nhập dự phòng đột biến để làm đẹp lợi nhuận ngắn hạn, bảo đảm quỹ dự phòng đủ sức hấp thụ tổn thất trong kịch bản kinh tế tiêu cực.\n"
    "4. Tăng cường Kiểm toán Thuật toán Phê duyệt Tự động: Thiết lập cơ chế kiểm định độc lập (Model Validation) định kỳ đối với các mô hình chấm điểm tín dụng scorecard để ngăn ngừa sai lệch hệ thống."
)

# ==============================================================================
# KẾT LUẬN
# ==============================================================================
add_title("KẾT LUẬN")
add_body(
    "Giai đoạn 2020–2025 là một giai đoạn bản lề phản ánh sự thích ứng và phân kỳ chiến lược sâu sắc trong quản trị rủi ro tín dụng giữa Agribank và MB. Nghiên cứu đã chứng minh rằng: không thể kết luận một cách đơn giản 'MB quản trị tốt hơn Agribank' hay ngược lại chỉ dựa vào con số NPL bề mặt. Mỗi mô hình đại diện cho một sự đánh đổi kinh tế học sâu sắc giữa Tăng trưởng - Lợi nhuận - Rủi ro tín dụng trong các cấu trúc thể chế khác nhau. Agribank chọn triết lý phòng thủ, chấp nhận hiệu quả vốn RAROC khiêm tốn (10-16%) nhưng duy trì được sự bền vững danh mục nông nghiệp và bộ đệm LLCR dày dặn. MB chọn triết lý đổi mới thị trường, tối ưu hóa ROE và RAROC vượt trội (34-50%) nhưng phải đánh đổi bằng sự suy giảm bộ đệm an toàn vốn và mức độ tổn thương nặng nề trước các cú sốc vĩ mô của thị trường bất động sản và TPDN. Khi hệ thống ngân hàng Việt Nam bước vào kỷ nguyên áp dụng Basel III và IFRS 9, sự dung hòa giữa năng lực quản trị rủi ro tập trung, số hóa của MB và văn hóa thẩm định thận trọng, an toàn của Agribank sẽ là chìa khóa định hình chuẩn mực quản trị ngân hàng hiện đại."
)

# ==============================================================================
# TÀI LIỆU THAM KHẢO
# ==============================================================================
add_title("TÀI LIỆU THAM KHẢO")
refs = [
    "[1] Agribank (2021, 2023, 2025), Báo cáo tài chính hợp nhất kiểm toán các năm 2020–2025, Công bố trên cổng thông tin quan hệ nhà đầu tư Agribank.",
    "[2] Agribank (2021, 2023, 2025), Báo cáo thường niên các năm 2020–2025, Agribank.",
    "[3] Basel Committee on Banking Supervision - BCBS (2006), International Convergence of Capital Measurement and Capital Standards: A Revised Framework (Basel II), Bank for International Settlements (BIS).",
    "[4] BCBS (2017), Basel III: Finalising post-crisis reforms, Bank for International Settlements.",
    "[5] Cressey, D. R. (1953), Other People's Money: A Study in the Social Psychology of Embezzlement, Free Press.",
    "[6] COSO (2013), Internal Control — Integrated Framework, Committee of Sponsoring Organizations of the Treadway Commission.",
    "[7] International Accounting Standards Board - IASB (2014), IFRS 9 Financial Instruments, IFRS Foundation.",
    "[8] Jensen, M. C., & Meckling, W. H. (1976), 'Theory of the firm: Managerial behavior, agency costs and ownership structure', Journal of Financial Economics, 3(4), 305-360.",
    "[9] Ngân hàng Nhà nước Việt Nam (2016), Thông tư số 41/2016/TT-NHNN ngày 30/12/2016 quy định tỷ lệ an toàn vốn đối với ngân hàng, chi nhánh ngân hàng nước ngoài.",
    "[10] Ngân hàng Nhà nước Việt Nam (2020), Thông tư số 01/2020/TT-NHNN ngày 13/3/2020 quy định về tổ chức tín dụng, chi nhánh ngân hàng nước ngoài cơ cấu lại thời hạn trả nợ, miễn, giảm lãi, phí, giữ nguyên nhóm nợ nhằm hỗ trợ khách hàng chịu ảnh hưởng bởi dịch Covid-19.",
    "[11] Ngân hàng Nhà nước Việt Nam (2021), Thông tư số 11/2021/TT-NHNN ngày 30/7/2021 quy định về phân loại tài sản có, mức trích, phương pháp trích lập dự phòng rủi ro và việc sử dụng dự phòng để xử lý rủi ro trong hoạt động của TCTD.",
    "[12] Ngân hàng Nhà nước Việt Nam (2023), Thông tư số 02/2023/TT-NHNN ngày 23/4/2023 quy định về việc TCTD, chi nhánh ngân hàng nước ngoài cơ cấu lại thời hạn trả nợ và giữ nguyên nhóm nợ nhằm hỗ trợ khách hàng gặp khó khăn.",
    "[13] Ngân hàng TMCP Quân đội - MB (2021, 2023, 2025), Báo cáo tài chính hợp nhất kiểm toán các năm 2020–2025, Kiểm toán bởi KPMG và PwC Việt Nam.",
    "[14] Ngân hàng TMCP Quân đội - MB (2021, 2023, 2025), Báo cáo thường niên các năm 2020–2025, MB.",
    "[15] Quốc hội Nước CHXHCN Việt Nam (2017), Nghị quyết số 42/2017/QH14 ngày 21/6/2017 về thí điểm xử lý nợ xấu của các tổ chức tín dụng.",
    "[16] Quốc hội Nước CHXHCN Việt Nam (2024), Luật Các tổ chức tín dụng số 32/2024/QH15 thông qua ngày 18/01/2024, có hiệu lực từ 01/7/2024.",
    "[17] Stiglitz, J. E., & Weiss, A. (1981), 'Credit Rationing in Markets with Imperfect Information', The American Economic Review, 71(3), 393-410.",
]
for ref in refs:
    p_ref = doc.add_paragraph()
    format_paragraph(p_ref, space_before=2, space_after=3, line_spacing=1.15, align=WD_ALIGN_PARAGRAPH.LEFT)
    r = p_ref.add_run(ref)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(9.5)

# Save Document
out_path = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v2.docx"
doc.save(out_path)
print(f"Master/Ph.D. document successfully built and saved to: {out_path}")
