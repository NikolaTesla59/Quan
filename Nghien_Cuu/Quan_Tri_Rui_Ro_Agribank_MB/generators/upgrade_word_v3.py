import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import copy
import os

desktop_dir = r"C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro"
doc_path = os.path.join(desktop_dir, "Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v2.docx")

doc = docx.Document(doc_path)
P = doc.paragraphs
T = doc.tables

def set_para(p, label, body, italic=False, size_pt=None, align=None):
    """Set paragraph with optional bold label + normal body, preserving font."""
    fn = "Times New Roman"
    fs = Pt(12)
    if p.runs:
        if p.runs[0].font.name:
            fn = p.runs[0].font.name
        if p.runs[0].font.size:
            fs = p.runs[0].font.size
    if size_pt is not None:
        fs = Pt(size_pt)
    for r in list(p.runs):
        r._element.getparent().remove(r._element)
    if align is not None:
        p.alignment = align
    if label:
        r1 = p.add_run(label)
        r1.bold = True
        r1.italic = italic
        r1.font.name = fn
        r1.font.size = fs
    if body:
        r2 = p.add_run(body)
        r2.bold = False
        r2.italic = italic
        r2.font.name = fn
        r2.font.size = fs

def insert_para_after(target_p, label, body, italic=False, size_pt=None):
    """Insert a new paragraph immediately after target_p and return it."""
    new_el = copy.deepcopy(target_p._element)
    target_p._element.addnext(new_el)
    new_p = docx.text.paragraph.Paragraph(new_el, target_p._parent)
    set_para(new_p, label, body, italic=italic, size_pt=size_pt)
    return new_p

def insert_para_after_table(tbl, label, body, italic=True, size_pt=10.5):
    """Insert a source/note paragraph immediately after a table."""
    # Find a template paragraph
    tmpl = doc.paragraphs[8]
    new_el = copy.deepcopy(tmpl._element)
    tbl._tbl.addnext(new_el)
    new_p = docx.text.paragraph.Paragraph(new_el, tbl._parent)
    set_para(new_p, label, body, italic=italic, size_pt=size_pt)
    return new_p

def cell_set(cell, text, bold=False):
    p = cell.paragraphs[0]
    for extra in cell.paragraphs[1:]:
        extra._element.getparent().remove(extra._element)
    fn = "Times New Roman"
    fs = Pt(10.5)
    if p.runs:
        if p.runs[0].font.name:
            fn = p.runs[0].font.name
        if p.runs[0].font.size:
            fs = p.runs[0].font.size
        p.runs[0].text = str(text)
        p.runs[0].bold = bold
        for r in p.runs[1:]:
            r.text = ""
    else:
        r = p.add_run(str(text))
        r.bold = bold
        r.font.name = fn
        r.font.size = fs

def row_set(table, r, vals, bold_first=False):
    for c, val in enumerate(vals):
        cell_set(table.rows[r].cells[c], val, bold=(bold_first and c == 0))

def add_row(table, vals, bold_first=False):
    new_tr = copy.deepcopy(table.rows[-1]._tr)
    table._tbl.append(new_tr)
    row_set(table, len(table.rows) - 1, vals, bold_first=bold_first)

# ==============================================================================
# ITEM #1: COVER PAGE (Nhóm 2, Lớp K34_3_NH8, Học phần Quản trị rủi ro, GV: TS. Khúc Thế Anh, 8 Học viên)
# ==============================================================================
set_para(P[1], "TIỂU LUẬN HỌC PHẦN: QUẢN TRỊ RỦI RO", "")
P[1].runs[0].bold = True

p4 = P[4]
fn4 = p4.runs[0].font.name if p4.runs else "Times New Roman"
fs4 = p4.runs[0].font.size if p4.runs else Pt(12)
for r in list(p4.runs):
    r._element.getparent().remove(r._element)

cover_lines = [
    ("Nhóm thực hiện:\t\t", "Nhóm 2"),
    ("Lớp:\t\t\t", "K34_3_NH8 (Cao học Khóa 34 – Viện Ngân hàng - Tài chính)"),
    ("Môn học / Học phần:\t", "Quản trị rủi ro"),
    ("Giảng viên hướng dẫn:\t", "TS. Khúc Thế Anh"),
    ("Danh sách thành viên Nhóm 2:\t", ""),
    ("   1. CH345205\t", "Cao Trường Anh"),
    ("   2. CH345254\t", "Đỗ Lương Bằng"),
    ("   3. CH345463\t", "Hoàng Thị Mai Hương"),
    ("   4. CH345505\t", "Lê Thị Bảo Linh"),
    ("   5. CH345585\t", "Ngô Thị Bích Ngọc"),
    ("   6. CH345648\t", "Phạm Hồng Quân"),
    ("   7. CH345714\t", "Vũ Thanh Thủy"),
    ("   8. CH345756\t", "Đỗ Minh Tuấn"),
    ("Hồ sơ dữ liệu kèm theo:\t", "Phan_tich_RRTD_Agribank_MB_2020-2025_v2.xlsx & BCTC_Goc_Trich_Xuat_Agribank_MB_2020-2025.xlsx")
]
for idx, (lbl, val) in enumerate(cover_lines):
    r_lbl = p4.add_run(lbl)
    r_lbl.bold = True
    r_lbl.font.name = fn4
    r_lbl.font.size = fs4
    r_val = p4.add_run(val + ("\n" if idx < len(cover_lines) - 1 else ""))
    r_val.bold = False
    r_val.font.name = fn4
    r_val.font.size = fs4

# ==============================================================================
# ITEM #7 IN ABSTRACT (P[8]): Update Agribank IFRS 9 Gap to +3.660 tỷ (+9,8%) & CAR -15 bps
# ==============================================================================
set_para(
    P[8],
    None,
    "Nghiên cứu so sánh mô hình và thực trạng quản trị rủi ro tín dụng (RRTD) giữa Ngân hàng Nông nghiệp và Phát triển Nông thôn Việt Nam (Agribank – NHTM 100% vốn Nhà nước, định hướng “tam nông”) và Ngân hàng TMCP Quân đội (MB – tập đoàn tài chính đa năng) giai đoạn 2020–2025. "
    "Dữ liệu được trích xuất từ 27 tệp báo cáo tài chính kiểm toán (hợp nhất, riêng lẻ) và báo cáo thường niên của hai ngân hàng; mọi chỉ tiêu được tính lại bằng công thức trong tệp Excel kèm theo. "
    "Khung phân tích dựa trên lý thuyết bất cân xứng thông tin (Stiglitz & Weiss, 1981), lý thuyết đại diện (Jensen & Meckling, 1976), Basel II và mô hình tổn thất tín dụng kỳ vọng IFRS 9. "
    "Bốn kết quả chính: (1) Khi tính cùng cơ sở (nợ nhóm 3–5 chia dư nợ cho vay khách hàng hợp nhất), tỷ lệ nợ xấu của hai ngân hàng hội tụ: Agribank giảm từ 1,85% (2023) về 1,30% (2025), MB từ 1,60% về 1,29%; mức 1,17% của Agribank trong báo cáo thường niên dùng mẫu số tổng cấp tín dụng nên không so sánh trực tiếp được với MB. "
    "(2) Cả hai ngân hàng dựa nhiều vào xóa nợ bằng dự phòng: năm 2025 Agribank sử dụng 32.621 tỷ đồng, MB 12.185 tỷ đồng; cộng lại số đã xóa, NPL trước xử lý năm 2025 là 2,95% (Agribank) và 2,42% (MB). Mức giảm NPL của MB chủ yếu đến từ hiệu ứng mẫu số khi dư nợ tăng 39,6% (mức tăng nội sinh của ngân hàng mẹ và 7 công ty con hợp nhất, do MBV không hợp nhất vào BCTC MB theo Điều 185 Luật Các TCTD 2024). "
    "(3) MB có tỷ suất lợi nhuận trên vốn rủi ro ước tính (RORAC proxy) 31,6%–49,3%, cao hơn Agribank (10,8%–16,7%), nhưng tỷ lệ bao phủ nợ xấu hợp nhất giảm từ 268,0% (2021) xuống 92,3%–93,8% (2024–2025), trong khi Agribank duy trì 113,6%–146,3%. "
    "(4) Trong kịch bản cực đoan 2026, CAR của Agribank giảm từ 10,22% về 8,67%, trong khi LNTT của MB giảm 69,3%; mô phỏng IFRS 9 năm 2025 cho thấy MB thiếu khoảng 14.006 tỷ đồng dự phòng (+106,5%) và CAR giảm khoảng 103 điểm cơ bản, còn Agribank thiếu khoảng 3.660 tỷ đồng (+9,8%, CAR giảm 15 điểm cơ bản). Kết quả kiểm định độ nhạy trên 6 kịch bản tham số xác nhận tính vững của nhận định này."
)

# ==============================================================================
# ITEM #14: UPDATE TABLE OF CONTENTS HEADINGS IN P[13], P[30]..P[35]
# ==============================================================================
set_para(P[13], None, "  1.1. Khái niệm, phân loại, nguyên nhân và các lý thuyết kinh tế về rủi ro tín dụng\t4")
set_para(P[30], "CHƯƠNG 5. PHÂN TÍCH TÌNH HUỐNG THỰC TIỄN GIAI ĐOẠN 2020–2025 (DIỄN BIẾN – NGUYÊN NHÂN – HẬU QUẢ – BIỆN PHÁP KHẮC PHỤC)\t24", "")
set_para(P[31], None, "  5.1. Agribank – Cú sốc thiên tai Yagi 2024, điểm nghẽn thanh khoản TSBĐ nợ nhóm 5 và bài học từ vụ Lifepro\t24")
set_para(P[32], None, "  5.2. MB – Rủi ro tín dụng tiêu dùng tại MCredit và rủi ro đạo đức cấp chi nhánh (Vụ Gia Lai 2022–2023)\t25")
set_para(P[33], None, "  5.3. MB – Cú sốc chất lượng tài sản năm 2023: Khủng hoảng thanh khoản TPDN, BĐS và hiệu ứng CIC\t26")
set_para(P[34], None, "  5.4. MB – Biến động nợ xấu Quý III–IV/2025, xử lý rủi ro bằng dự phòng và quy chế không hợp nhất MBV\t27")
set_para(P[35], "CHƯƠNG 6. ĐÁNH GIÁ KẾT QUẢ ĐẠT ĐƯỢC, HẠN CHẾ, NGUYÊN NHÂN VÀ SO SÁNH HAI MÔ HÌNH\t28", "")

# ==============================================================================
# ITEM #13: REMOVE DUPLICATE LABELS IN LỜI MỞ ĐẦU (P[45], P[46], P[48])
# ==============================================================================
set_para(
    P[45],
    "1. Tính cấp thiết của đề tài: ",
    "Rủi ro tín dụng (RRTD) là rủi ro trọng yếu nhất đe dọa trực tiếp đến sự an toàn, tính thanh khoản và khả năng duy trì hoạt động liên tục của hệ thống ngân hàng thương mại. Giai đoạn 2020–2025 chứng kiến những biến động kinh tế vĩ mô chưa từng có tiền lệ tại Việt Nam: đại dịch Covid-19 làm đứt gãy chuỗi cung ứng; thị trường bất động sản và trái phiếu doanh nghiệp (TPDN) rơi vào khủng hoảng thanh khoản năm 2022–2023; và hàng loạt cơ chế khoan dung pháp lý (regulatory forbearance) thông qua các Thông tư 01/2020/TT-NHNN, Thông tư 02/2023/TT-NHNN và Thông tư 53/2024/TT-NHNN. Trong bối cảnh đó, việc so sánh mô hình quản trị rủi ro giữa Agribank (NHTM 100% vốn Nhà nước) và MB (NHTMCP đa năng hàng đầu) không chỉ mang ý nghĩa thực tiễn đối với công tác điều hành ngân hàng mà còn cung cấp một tình huống nghiên cứu có giá trị về sự tương tác giữa thể chế sở hữu, hàm mục tiêu tối ưu hóa và hành vi quản trị rủi ro tín dụng."
)
set_para(
    P[46],
    "2. Mục tiêu nghiên cứu và Câu hỏi nghiên cứu: ",
    "Mục tiêu tổng quát của đề tài là bóc tách bản chất, cơ chế vận hành và hiệu quả thực chất của mô hình quản trị RRTD tại Agribank và MB giai đoạn 2020–2025, từ đó đề xuất hệ thống giải pháp nâng cao năng lực an toàn vốn và phòng ngừa rủi ro theo chuẩn mực quốc tế. Đề tài tập trung giải quyết 3 câu hỏi nghiên cứu (Research Questions):"
)
set_para(
    P[48],
    "3. Phương pháp nghiên cứu và Đóng góp mới: ",
    "Đề tài áp dụng phương pháp nghiên cứu định tính kết hợp phân tích định lượng chuyên sâu: (i) Phương pháp phân tích báo cáo tài chính chuyên sâu để bóc tách biến động dự phòng, nợ xóa nội bảng, nợ cơ cấu và chênh lệch giữa báo cáo hợp nhất với báo cáo riêng lẻ; (ii) Phương pháp phân rã toán học (Decomposition Analysis) để định lượng hiệu ứng quy mô tín dụng và hiệu ứng chất lượng tài sản đối với biến động NPL; (iii) Phương pháp kiểm tra sức chịu đựng vĩ mô (Macroeconomic Stress Testing) theo khuyến nghị Basel II/III; và (iv) Phương pháp mô phỏng tổn thất tín dụng kỳ vọng (IFRS 9 Simulation) kèm kiểm định độ nhạy tham số. Toàn bộ dữ liệu được trích xuất trực tiếp từ 27 tệp báo cáo tài chính kiểm toán (hợp nhất, riêng lẻ) và báo cáo thường niên giai đoạn 2020–2025 của hai ngân hàng."
)

# ==============================================================================
# ITEM #8 & #13: CHAPTER 1 — SECTION 1.1 (Foundational concepts, classification, causes, and clean numbering)
# ==============================================================================
set_para(P[50], "1.1. Khái niệm, phân loại, nguyên nhân và các lý thuyết kinh tế về rủi ro tín dụng", "")
P[50].runs[0].bold = True

set_para(
    P[51],
    "Khái niệm, phân loại và nguyên nhân gây ra rủi ro tín dụng: ",
    "Theo Ủy ban Basel về Giám sát Ngân hàng (BCBS, 2006) và quy định tại Thông tư 11/2021/TT-NHNN (nay là Thông tư 31/2024/TT-NHNN), rủi ro tín dụng trong hoạt động ngân hàng là khả năng xảy ra tổn thất về tài sản của tổ chức tín dụng do khách hàng không thực hiện hoặc không có khả năng thực hiện một phần hoặc toàn bộ nghĩa vụ trả nợ gốc và lãi theo hợp đồng hoặc thỏa thuận cấp tín dụng. "
    "Xét theo cấu trúc phát sinh, rủi ro tín dụng được phân loại thành hai cấp độ: (i) Rủi ro giao dịch (Transaction Risk), bao gồm rủi ro lựa chọn (thẩm định sai năng lực khách hàng), rủi ro bảo đảm (tài sản thế chấp mất giá hoặc vướng pháp lý không thể phát mại) và rủi ro nghiệp vụ (lỗ hổng giám sát sau cho vay); và (ii) Rủi ro danh mục (Portfolio Risk), bao gồm rủi ro nội tại của từng lĩnh vực kinh tế và rủi ro tập trung (Concentration Risk) khi ngân hàng dồn vốn quá lớn vào một nhóm khách hàng liên quan, một ngành chu kỳ (như bất động sản, xây dựng) hoặc một công cụ tài chính (như trái phiếu doanh nghiệp). "
    "Nguyên nhân gây ra rủi ro tín dụng xuất phát từ ba nhóm nhân tố tương tác lẫn nhau: (1) Nhóm nguyên nhân từ phía khách hàng vay (suy giảm năng lực quản trị, đứt gãy dòng tiền kinh doanh, sử dụng vốn sai mục đích hoặc gian lận cố ý); (2) Nhóm nguyên nhân nội tại từ phía ngân hàng (khẩu vị rủi ro tăng trưởng nóng, áp lực chỉ tiêu KPI làm nới lỏng tiêu chuẩn thẩm định, phụ thuộc quá mức vào tài sản thế chấp thay vì dòng tiền trả nợ, hoặc sự suy yếu của hệ thống kiểm soát nội bộ ba tuyến phòng vệ); và (3) Nhóm nguyên nhân từ môi trường vĩ mô và thể chế pháp lý (cú sốc dịch bệnh Covid-19, thiên tai bão lũ đối với nông nghiệp, biến động lãi suất – tỷ giá, sự đóng băng của thị trường bất động sản – trái phiếu doanh nghiệp và khoảng trống pháp lý trong thu giữ, xử lý tài sản bảo đảm). "
    "Trên nền tảng đó, nghiên cứu thiết lập cơ sở lý luận chuyên sâu dựa trên bốn trụ cột lý thuyết kinh điển:"
)

set_para(
    P[52],
    "1. Lý thuyết Bất cân xứng thông tin (Information Asymmetry Theory – Stiglitz & Weiss, 1981): ",
    "Stiglitz và Weiss chứng minh rằng trong thị trường tín dụng, lãi suất cho vay không thể đóng vai trò cân bằng thị trường theo cách thông thường do tồn tại hai hiện tượng: Nghịch tuyển (Adverse Selection) và Rủi ro đạo đức (Moral Hazard). Khi ngân hàng nâng lãi suất cho vay để bù đắp rủi ro, những người vay có dự án an toàn sẽ chủ động rút lui, chỉ còn lại những người vay có dự án rủi ro cao sẵn sàng chấp nhận lãi suất lớn (Nghịch tuyển). Đồng thời, lãi suất cao thúc đẩy người vay chuyển dịch vốn sang các dự án có độ mạo hiểm cao hơn để kỳ vọng lợi nhuận bù đắp chi phí lãi (Rủi ro đạo đức). Do đó, ngân hàng tối ưu hóa lợi nhuận bằng cách áp dụng cơ chế Giới hạn hạn mức tín dụng (Credit Rationing) thay vì tăng lãi suất. Lý thuyết này giải thích sâu sắc sự khác biệt giữa Agribank (sử dụng tài sản bảo đảm truyền thống là đất đai để giảm thiểu nghịch tuyển) và MB (áp dụng mô hình chấm điểm tự động và khai thác hệ sinh thái số để thu hẹp bất cân xứng thông tin)."
)
set_para(
    P[53],
    "2. Lý thuyết Chi phí đại diện và Cấu trúc sở hữu (Agency Theory – Jensen & Meckling, 1976): ",
    "Lý thuyết Người đại diện phân tích sự xung đột lợi ích giữa Người quản lý (Ban điều hành) và Chủ sở hữu (Cổ đông). Trong ngành ngân hàng, cấu trúc sở hữu quyết định trực tiếp đến hàm mục tiêu của nhà quản trị. Tại Ngân hàng 100% vốn Nhà nước như Agribank, Ban điều hành chịu sự ràng buộc bởi các mục tiêu kép: vừa bảo toàn vốn Nhà nước, vừa thực thi chính sách an sinh xã hội và tài trợ phát triển nông nghiệp theo chỉ đạo của Chính phủ. Do nguy cơ chịu trách nhiệm hành chính và hình sự khi để xảy ra thất thoát tài sản công là rất nghiêm trọng, ban điều hành và cán bộ tín dụng Agribank có xu hướng thận trọng cao (Risk-averse), ưu tiên cho vay có tài sản thế chấp là quyền sử dụng đất. Ngược lại, tại NHTMCP có sở hữu cổ phần hỗn hợp như MB, ban điều hành chịu áp lực từ cổ đông và thị trường chứng khoán về tỷ suất sinh lời trên vốn (ROE), tăng trưởng lợi nhuận và định giá cổ phiếu. Áp lực này thúc đẩy MB thiết lập cơ chế đãi ngộ gắn liền với KPI tăng trưởng tín dụng, mở rộng sang các phân khúc biên lợi nhuận cao như cho vay tiêu dùng (MCredit) và trái phiếu doanh nghiệp."
)
set_para(
    P[54],
    "3. Khung Hiệp ước Vốn Basel (Basel Capital Accord – Basel II & Basel III): ",
    "Khung an toàn vốn Basel thiết lập ba trụ cột tương hỗ: Trụ cột 1 (Minimum Capital Requirements) quy định tỷ lệ an toàn vốn tối thiểu (CAR >= 8%) tính trên Tài sản có rủi ro (RWA). Basel II cho phép ngân hàng lựa chọn giữa Phương pháp Tiêu chuẩn (Standardized Approach – SA) với hệ số rủi ro cố định theo quy định của cơ quan quản lý, hoặc Phương pháp Xếp hạng nội bộ (Internal Ratings-Based – IRB: Foundation IRB và Advanced IRB), trong đó ngân hàng tự lượng hóa Xác suất vỡ nợ (Probability of Default – PD), Tỷ lệ tổn thất khi vỡ nợ (Loss Given Default – LGD) và Dư nợ tại thời điểm vỡ nợ (Exposure at Default – EAD). Trụ cột 2 (Supervisory Review Process – ICAAP) yêu cầu ngân hàng tự đánh giá mức đủ vốn nội bộ thông qua việc thực hiện Kiểm tra sức chịu đựng (Stress Testing) định kỳ đối với các cú sốc vĩ mô. Trụ cột 3 (Market Discipline) yêu cầu minh bạch hóa thông tin về chất lượng danh mục và mức độ an toàn vốn nhằm tạo áp lực giám sát từ thị trường."
)
set_para(
    P[55],
    "4. Chuẩn mực Kế toán Quốc tế IFRS 9 vs Chuẩn mực Việt Nam (VAS / Thông tư 11/2021 & Nghị định 86/2024): ",
    "Đây là sự chuyển dịch mô hình mang tính bước ngoặt từ Mô hình tổn thất đã phát sinh (Incurred Loss Model) sang Mô hình tổn thất tín dụng kỳ vọng (Expected Credit Loss – ECL). Theo VAS, Thông tư 11/2021/TT-NHNN và nay là Thông tư 31/2024/TT-NHNN kết hợp Nghị định 86/2024/NĐ-CP, dự phòng cụ thể chủ yếu được trích lập khi khoản nợ đã phát sinh dấu hiệu quá hạn hoặc suy giảm khả năng trả nợ (nợ nhóm 2 trích 5%, nhóm 3 trích 20%, nhóm 4 trích 50%, nhóm 5 trích 100% trên phần dư nợ sau khi đã khấu trừ giá trị tài sản bảo đảm theo tỷ lệ quy định; dự phòng chung trích 0,75% tổng dư nợ nhóm 1 đến nhóm 4). Ngược lại, IFRS 9 phân loại toàn bộ tài sản tài chính thành 3 giai đoạn (Three Stages):"
)

# ==============================================================================
# ITEM #3: UPDATE TABLE 1 (Bảng 2) AND SECTION 1.4 PROSE (P[63]) TO MATCH EXCEL 100%
# ==============================================================================
# Currently Table 1 has 5 rows (R00..R04). Let's add 1 row so it has all 5 indicators matching Du_lieu rows 52-56!
add_row(T[1], ["", "", "", "", "", "", ""])
row_set(T[1], 0, ["Chỉ tiêu toàn hệ thống ngân hàng (%, nghìn tỷ đồng)", "2020", "2021", "2022", "2023", "2024", "2025"])
row_set(T[1], 1, ["NPL nội bảng toàn hệ thống (NHNN công bố, gồm NH kiểm soát đặc biệt)", "1,69%", "1,49%", "2,03%", "4,55%", "4,35%", "4,15%"])
row_set(T[1], 2, ["NPL nội bảng các NHTM hoạt động bình thường (loại trừ 5 NH KSĐB)", "1,45%", "1,35%", "1,92%", "1,93%", "1,69%", "1,85%"])
row_set(T[1], 3, ["Tỷ lệ nợ nhóm 2 / Tổng dư nợ (NHTM niêm yết & hệ thống)", "1,52%", "1,38%", "1,65%", "2,10%", "1,90%", "1,35%"])
row_set(T[1], 4, ["Dư nợ cơ cấu giữ nguyên nhóm nợ theo TT 02/2023 (nghìn tỷ đồng)", "0", "0", "0", "183,5", "126,4", "0"])
row_set(T[1], 5, ["Tỷ lệ nợ xấu gộp (Nợ xấu nội bảng + Nợ VAMC + Nợ cơ cấu tiềm ẩn)", "3,81%", "3,95%", "4,50%", "6,10%", "5,46%", "4,95%"])

set_para(
    P[63],
    "Bức tranh rủi ro hệ thống và hai mặt bằng thống kê nợ xấu: ",
    "Giai đoạn 2020–2025 ghi nhận sự biến động mạnh của chu kỳ chất lượng tài sản toàn ngành ngân hàng Việt Nam. Khi phân tích số liệu vĩ mô, cần phân biệt rõ hai mặt bằng thống kê: (i) Tỷ lệ nợ xấu nội bảng toàn hệ thống do Ngân hàng Nhà nước (NHNN) công bố tăng từ 1,69% (2020) và 1,49% (2021) lên 2,03% (2022), sau đó vọt lên 4,55% (cuối 2023), 4,35% (2024) và 4,15% (2025) do từ năm 2023 số liệu thống kê bao gồm cả 5 ngân hàng thương mại thuộc diện kiểm soát đặc biệt/chuyển giao bắt buộc (SCB, CBBank, OceanBank, GPBank, DongABank); (ii) Nếu tách riêng nhóm các NHTM hoạt động bình thường (loại trừ các ngân hàng kiểm soát đặc biệt), mặt bằng nợ xấu nội bảng chỉ dao động trong khoảng 1,35%–1,93% (năm 2023: 1,93%; năm 2024: 1,69%; năm 2025: 1,85%). "
    "Bên cạnh đó, tỷ lệ nợ nhóm 2 của hệ thống đạt đỉnh 2,10% năm 2023 trước khi hạ nhiệt về 1,35% năm 2025; dư nợ cơ cấu giữ nguyên nhóm nợ theo Thông tư 02/2023/TT-NHNN đạt 183,5 nghìn tỷ đồng cuối năm 2023, giảm về 126,4 nghìn tỷ đồng năm 2024 và chấm dứt hiệu lực vào cuối năm 2024. Nếu tính toàn diện tỷ lệ nợ xấu gộp (bao gồm nợ xấu nội bảng, nợ xấu bán cho VAMC chưa xử lý được và nợ cơ cấu tiềm ẩn theo công bố của NHNN và Hiệp hội Ngân hàng Việt Nam – VNBA), tỷ lệ này đã tăng từ 3,81% (2020) lên đỉnh 6,10% (2023), trước khi giảm về 5,46% (2024) và 4,95% (2025)."
)

# ==============================================================================
# ITEM #10: SECTION 4.1 PROSE (P[79]) — Cite TM 3.4 BCTC HN 2025 (tr. 148) & Điều 185 Luật TCTD 2024 on MBV
# ==============================================================================
set_para(
    P[79],
    "Quy mô và Tốc độ mở rộng tín dụng (kèm làm rõ phạm vi hợp nhất MBV): ",
    "Giai đoạn 2020–2025 ghi nhận sự phân kỳ rõ nét về tốc độ tăng trưởng quy mô tín dụng giữa hai ngân hàng. Dư nợ cho vay khách hàng hợp nhất của Agribank tăng từ 1.213.958 tỷ đồng (2020) lên 1.976.369 tỷ đồng (2025), tương ứng tốc độ tăng trưởng kép hàng năm (CAGR) đạt 10,2%/năm. Trong khi đó, MB ghi nhận tốc độ mở rộng tín dụng rất nhanh, đưa dư nợ cho vay hợp nhất từ 298.297 tỷ đồng (2020) lên 1.084.019 tỷ đồng (2025), đạt CAGR 29,4%/năm. "
    "Riêng năm 2025, dư nợ hợp nhất của MB tăng 39,6% (+307.361 tỷ đồng). Cần lưu ý một điểm kỹ thuật kế toán quan trọng tại Thuyết minh số 3.4 BCTC hợp nhất kiểm toán năm 2025 của MB (trang 148 PDF / trang 292 BCTN): căn cứ Điểm c Khoản 1 Điều 185 Luật Các tổ chức tín dụng số 32/2024/QH15, MB không hợp nhất báo cáo tài chính của Ngân hàng TNHH MTV Việt Nam Hiện Đại (MBV – tiền thân là OceanBank, đơn vị được MB nhận chuyển giao bắt buộc từ ngày 17/10/2024). Danh sách 7 công ty con được hợp nhất vào BCTC của MB chỉ bao gồm MB AMC, MBS, MB Cap, MCredit, MIC, MBLife và MB Cambodia. Do đó, mức tăng trưởng dư nợ 39,6% và số dư nợ xấu hợp nhất 14.027 tỷ đồng năm 2025 hoàn toàn là quy mô nội sinh của ngân hàng mẹ MB và 7 công ty con hiện hữu (khi MB được NHNN nới hạn mức tăng trưởng tín dụng nhờ tham gia nhận chuyển giao bắt buộc), chứ không bị cộng gộp bảng cân đối kế toán lịch sử của OceanBank."
)

# ==============================================================================
# ITEM #4 & #5: UPDATE TABLE 6 (Bảng 7) AND SECTION 4.3 PROSE (P[89])
# ==============================================================================
# Currently Table 6 has 8 rows (R00..R07). Let's add 2 rows so it has 10 rows (R00..R09) covering both banks symmetrically!
add_row(T[6], ["", "", "", "", "", "", ""])
add_row(T[6], ["", "", "", "", "", "", ""])
row_set(T[6], 0, ["Chỉ tiêu phân tích (Tỷ đồng, %)", "2020", "2021", "2022", "2023", "2024", "2025"])
row_set(T[6], 1, ["Agribank: Nợ nhóm 2 (TM 9/10 BCTC Kiểm toán)", "30.078", "28.446", "35.280", "32.340", "29.202", "21.282"])
row_set(T[6], 2, ["Agribank: Tỷ lệ nợ nhóm 2 / Dư nợ Hợp nhất (%)", "2,48%", "2,16%", "2,44%", "2,08%", "1,69%", "1,08%"])
row_set(T[6], 3, ["Agribank: Tỷ lệ Nợ có vấn đề (Nhóm 2 + Nhóm 3–5) / Dư nợ HN", "4,25%", "4,03%", "4,25%", "3,93%", "3,38%", "2,37%"])
row_set(T[6], 4, ["Agribank: Dư nợ cơ cấu giữ nguyên nhóm nợ công bố (BCTN, tỷ)", "n.a.", "n.a.", "0", "37.876", "0", "n.a."])
row_set(T[6], 5, ["Agribank: NPL điều chỉnh tại các năm có số công bố (%)", "n.a.", "n.a.", "1,80%", "4,29%", "1,68%", "n.a."])
row_set(T[6], 6, ["MB: Nợ nhóm 2 Hợp nhất (TM 10.1/9.1 BCTC)", "2.422", "3.913", "7.809", "13.918", "12.197", "10.210"])
row_set(T[6], 7, ["MB: Tỷ lệ nợ nhóm 2 / Dư nợ Hợp nhất (%)", "0,81%", "1,08%", "1,70%", "2,28%", "1,57%", "0,94%"])
row_set(T[6], 8, ["MB: Tỷ lệ Nợ có vấn đề (Nhóm 2 + Nhóm 3–5) / Dư nợ HN", "1,90%", "1,98%", "2,79%", "3,88%", "3,19%", "2,24%"])
row_set(T[6], 9, ["MB: Dư nợ cơ cấu công bố (tỷ) & NPL điều chỉnh (%)", "n.a.", "612 (1,07%)", "0 (1,09%)", "n.a.", "0 (1,62%)", "0 (1,29%)"])

set_para(
    P[89],
    "So sánh Nợ nhóm 2, Tỷ lệ nợ có vấn đề (Nhóm 2–5) và Nợ cơ cấu có kiểm chứng: ",
    "Nợ nhóm 2 (nợ cần chú ý) là chỉ báo cảnh báo sớm quan trọng về sự suy giảm dòng tiền trả nợ của khách hàng. Khi đặt cả hai ngân hàng lên cùng một thước đo chuẩn hóa là Tỷ lệ Nợ có vấn đề (tổng nợ nhóm 2 và nợ xấu nhóm 3–5 chia cho dư nợ cho vay hợp nhất – tương ứng dòng 16 và dòng 28 trên sheet Chi_tieu), bức tranh hội tụ rủi ro trong giai đoạn khủng hoảng 2022–2023 hiện lên rất rõ nét: tại Agribank, tỷ lệ nợ nhóm 2 đạt đỉnh 2,44% năm 2022 (35.280 tỷ đồng) và Tỷ lệ nợ có vấn đề duy trì quanh mức 4,25% (2020 và 2022), trước khi giảm dần về 3,93% (2023), 3,38% (2024) và 2,37% (2025). Ngược lại, tại MB, tỷ lệ nợ nhóm 2 hợp nhất tăng vọt từ 0,81% (2020) lên đỉnh 2,28% năm 2023 (13.918 tỷ đồng, cao hơn mức 2,08% của Agribank), đẩy Tỷ lệ nợ có vấn đề của MB từ 1,90% (2020) lên tới 3,88% năm 2023 – tiệm cận sát mức 3,93% của Agribank – trước khi hạ về 3,19% (2024) và 2,24% (2025). "
    "Đối với dư nợ cơ cấu lại thời hạn trả nợ và giữ nguyên nhóm nợ, để đảm bảo tính nghiêm ngặt học thuật, nghiên cứu chỉ đưa vào tính toán định lượng các con số tuyệt đối được công bố chính thức tại Báo cáo thường niên và BCTC kiểm toán: (i) Tại Agribank, Báo cáo thường niên 2023 (trang 39) xác nhận dư nợ cơ cấu theo Thông tư 02/2023/TT-NHNN đến 31/12/2023 là 37.876 tỷ đồng (với 4.249 khách hàng), qua đó đẩy tỷ lệ NPL điều chỉnh cận trên của Agribank năm 2023 từ 1,85% lên 4,29%; đến cuối năm 2024, Thông tư 02 hết hiệu lực và Agribank đã trích đủ 100% dự phòng theo quy định, trong khi số dư cơ cấu theo Thông tư 01/03/14 (giai đoạn 2020–2021) và Thông tư 53/2024 (bão Yagi năm 2025) không được thuyết minh số tuyệt đối trên BCTC nên được ký hiệu là 'n.a.'; (ii) Tại MB, Báo cáo thường niên 2021 (trang 41) công bố số dư nợ cơ cấu Covid cuối năm 2021 còn 612 tỷ đồng (đã trích đủ 100% dự phòng), tương ứng NPL điều chỉnh năm 2021 là 1,07%. "
    "Một đặc điểm cấu trúc cốt lõi của Agribank là nợ nhóm 5 (nợ có khả năng mất vốn) luôn chiếm từ 67,0% đến 79,0% tổng nợ xấu (năm 2025: 20.220 / 25.610 tỷ đồng, tương đương 79,0% theo Thuyết minh 9 BCTC hợp nhất 2025). Nguyên nhân là tài sản bảo đảm của Agribank chủ yếu là đất nông nghiệp và đất ở nông thôn có tính thanh khoản thứ cấp thấp, thủ tục khởi kiện và thi hành án kéo dài nhiều năm, đặc biệt trong giai đoạn khoảng trống pháp lý từ khi Nghị quyết 42 hết hiệu lực (31/12/2023) đến trước khi Luật số 96/2025/QH15 có hiệu lực (15/10/2025)."
)

# ==============================================================================
# ITEM #11: TABLE 8 (Bảng 9) — Clarify Subsidiary Consumer Loans & NPL (MCredit + MBCambodia)
# ==============================================================================
add_row(T[8], ["", "", "", "", "", "", ""])
row_set(T[8], 6, ["MB: Dư nợ tiêu dùng Khối Công ty con (MCredit, MBCambodia; tỷ)", "10.173", "15.118", "21.624", "21.388", "25.435", "29.622"])
row_set(T[8], 7, ["MB: Nợ xấu Nhóm 3–5 Khối Công ty con (HN − Riêng lẻ, tỷ)", "555", "892", "1.351", "1.662", "1.981", "2.509"])

# ==============================================================================
# ITEM #6: UPDATE TABLE 9 (Bảng 10) AND SECTION 4.6 PROSE (P[97], P[99])
# ==============================================================================
row_set(T[9], 1, ["Agribank: NPL dự báo (%)", "1,30%", "1,32%", "1,49%", "1,71%"])
row_set(T[9], 2, ["Agribank: Chi phí dự phòng bổ sung (tỷ)", "0", "8.499", "16.188", "26.500"])
row_set(T[9], 3, ["Agribank: CAR sau stress (%)", "10,22%", "9,89%", "9,44%", "8,67%"])
row_set(T[9], 4, ["Agribank: Thặng dư vốn so với ngưỡng 8,0%", "+2,22%", "+1,89%", "+1,44%", "+0,67%"])
row_set(T[9], 5, ["MB: NPL hợp nhất dự báo (%)", "1,29%", "1,29%", "1,49%", "1,73%"])
row_set(T[9], 6, ["MB: Chi phí dự phòng bổ sung (tỷ)", "0", "5.203", "12.793", "22.402"])
row_set(T[9], 7, ["MB: CAR sau stress (%)", "11,00%", "10,78%", "10,33%", "9,73%"])
row_set(T[9], 8, ["MB: Tỷ lệ suy giảm LNTT so kịch bản cơ sở", "0,0%", "0,0%", "-38,6%", "-69,3%"])

set_para(
    P[97],
    "Thiết kế mô hình và hệ thống công thức giả định Stress Testing 2026: ",
    "Để lượng hóa khả năng chống chịu của hai ngân hàng trước các cú sốc vĩ mô tương lai theo khuyến nghị Trụ cột 2 (ICAAP – Basel II), nghiên cứu thiết lập mô hình Stress Testing năm 2026 trên sheet Stress_Testing với 3 kịch bản: (1) Kịch bản Cơ sở (GDP tăng 6,5%, lãi suất ổn định +0 bps, giá BĐS tăng 3,0%, tín dụng hệ thống tăng 14,0%); (2) Kịch bản Tiêu cực (GDP tăng 5,0%, lãi suất tăng +150 bps, giá BĐS giảm 10,0%, tín dụng hệ thống tăng 9,0%); và (3) Kịch bản Cực đoan (GDP tăng 3,5%, lãi suất tăng +300 bps, giá BĐS giảm 25,0%, tín dụng hệ thống tăng 5,0%). "
    "Toàn bộ các dòng kết quả trong Bảng 10 được liên kết 100% bằng công thức toán học từ dữ liệu gốc năm 2025 theo bốn cơ chế truyền dẫn: "
    "(i) Tăng trưởng dư nợ năm 2026: Agribank tăng lần lượt 10,0%, 5,0% và 1,0% (= tăng trưởng hệ thống trừ 4 điểm %); MB tăng 15,0%, 9,0% và 5,0%; "
    "(ii) Chuyển dịch nhóm nợ (Transition Matrix): Tỷ lệ dư nợ chuyển sang Nhóm 2 ở 3 kịch bản của Agribank là 1,5%, 2,5% và 4,0% (MB là 1,8%, 3,5% và 6,0%); tỷ lệ Nợ nhóm 2 đầu kỳ (năm 2025: Agribank 21.282 tỷ đồng; MB 10.210 tỷ đồng) chuyển thành nợ xấu mới Nhóm 3–5 lần lượt là 15%, 25% và 40% đối với Agribank (tạo ra 3.192 tỷ, 5.321 tỷ và 8.513 tỷ đồng nợ xấu mới) và 20%, 35%, 55% đối với MB (tạo ra 2.042 tỷ, 3.574 tỷ và 5.616 tỷ đồng nợ xấu mới); "
    "(iii) Nhu cầu trích lập dự phòng bổ sung: Bằng 100% nợ xấu phát sinh mới cộng với dự phòng trích thêm cho phần tăng ròng nợ nhóm 2 và phần bù đắp sụt giảm giá trị khấu trừ tài sản bảo đảm bất động sản khi giá BĐS giảm 10%–25%; "
    "(iv) Tác động lên Lợi nhuận trước thuế (LNTT) và CAR: LNTT kịch bản tiêu cực và cực đoan giảm tương ứng theo phần chi phí dự phòng vượt kịch bản cơ sở và sự thu hẹp thu nhập lãi thuần; Tài sản có rủi ro (RWA) được ước tính theo hệ số quy đổi RWA/Dư nợ thực nghiệm năm 2025 (xấp xỉ 1,002–1,020 lần dư nợ tại Agribank và 0,923–0,932 lần dư nợ tại MB)."
)

set_para(
    P[99],
    "Ý nghĩa kinh tế từ kết quả Stress Testing: ",
    "Kết quả mô phỏng bóc tách hai dạng tổn thương cấu trúc hoàn toàn khác nhau giữa hai định chế: (1) Agribank nhạy cảm trọng yếu về an toàn vốn: mặc dù tỷ lệ NPL dự báo trong kịch bản cực đoan chỉ tăng từ 1,30% lên 1,71%, nhưng do bộ đệm CAR xuất phát điểm mỏng (10,22%) và chi phí dự phòng bổ sung lên tới 26.500 tỷ đồng (làm LNTT giảm 73,8% từ 32.501 tỷ xuống 8.506 tỷ đồng), hệ số CAR của Agribank bị kéo giảm xuống 8,67% – chỉ còn cách ngưỡng an toàn tối thiểu 8,0% đúng 0,67 điểm %; (2) MB nhạy cảm trọng yếu về lợi nhuận: nhờ bộ đệm CAR ban đầu 11,00% và khả năng sinh lời trước dự phòng cao, CAR của MB trong kịch bản cực đoan vẫn duy trì ở mức 9,73% (thặng dư +1,73 điểm % so với ngưỡng 8%), nhưng chi phí dự phòng bổ sung 22.402 tỷ đồng khiến LNTT của MB sụt giảm 69,3% so với kịch bản cơ sở (từ 38.501 tỷ xuống 11.808 tỷ đồng). Các tham số chuyển nhóm và hệ số RWA trong mô hình là giả định kịch bản của nhóm nghiên cứu nhằm kiểm định độ bền tương đối, không phải dự báo chính thức của ngân hàng."
)

# ==============================================================================
# ITEM #7: UPDATE TABLE 10 (Bảng 11) AND SECTION 4.7 PROSE (P[102]) + SENSITIVITY ANALYSIS
# ==============================================================================
row_set(T[10], 0, ["Khoản mục mô phỏng năm 2025 (Tỷ đồng, %)", "Agribank (VAS)", "Agribank (IFRS 9)", "MB (VAS)", "MB (IFRS 9)"])
row_set(T[10], 1, ["Dự phòng Stage 1 (Performing – 12m ECL)", "14.602", "7.699", "8.098", "6.724"])
row_set(T[10], 2, ["Dự phòng Stage 2 (Underperforming – SICR)", "1.064", "11.658", "511", "11.315"])
row_set(T[10], 3, ["Dự phòng Stage 3 (Credit-impaired Nhóm 3–5)", "21.799", "21.769", "4.542", "9.118"])
row_set(T[10], 4, ["TỔNG DỰ PHÒNG YÊU CẦU (TM 9/10 vs IFRS 9)", "37.465", "41.125", "13.151", "27.157"])
row_set(T[10], 5, ["Khoảng cách dự phòng trích thiếu (Provisioning Gap)", "—", "+3.660", "—", "+14.006"])
row_set(T[10], 6, ["Tỷ lệ thiếu hụt so với dự phòng hiện hành (%)", "—", "+9,8%", "—", "+106,5%"])
row_set(T[10], 7, ["Tác động khấu trừ vào Vốn CSH (sau thuế 20%)", "—", "-2.928 (-2,2%)", "—", "-11.205 (-7,9%)"])
row_set(T[10], 8, ["Tỷ lệ CAR sau chuyển đổi IFRS 9 (%)", "10,22%", "10,07% (-15 bps)", "11,00%", "9,97% (-103 bps)"])

set_para(
    P[102],
    "Kết quả mô phỏng IFRS 9 và Kiểm định độ nhạy tham số (Sensitivity Analysis): ",
    "Khi loại bỏ hoàn toàn các ước tính nợ cơ cấu không có thuyết minh kiểm toán năm 2025 và tính toán thuần túy theo công thức chuẩn \\(ECL = EAD \\times PD \\times LGD\\) trên số liệu BCTC hợp nhất 2025 (sheet IFRS9_Simulation), tổng dự phòng ECL theo IFRS 9 của MB lên tới 27.157 tỷ đồng, cao hơn 14.006 tỷ đồng (+106,5%) so với mức dự phòng 13.151 tỷ đồng hiện có trên BCTC hợp nhất 2025; sau khi trừ thuế TNDN 20%, vốn chủ sở hữu của MB giảm 11.205 tỷ đồng (-7,9%) và hệ số CAR giảm 103 điểm cơ bản (từ 11,00% xuống 9,97%). "
    "Ngược lại, tại Agribank, tổng dự phòng ECL theo IFRS 9 là 41.125 tỷ đồng (Stage 1: 7.699 tỷ; Stage 2 với EAD = 21.282 tỷ nợ nhóm 2 + 5% nợ nhóm 1 chuyển nhóm = 117.756 tỷ đồng, ECL = 11.658 tỷ; Stage 3: 21.769 tỷ), chỉ cao hơn 3.660 tỷ đồng (+9,8%) so với quỹ dự phòng 37.465 tỷ đồng hiện có (gồm 22.863 tỷ dự phòng cụ thể và 14.602 tỷ dự phòng chung); vốn chủ sở hữu của Agribank chỉ giảm 2.928 tỷ đồng (-2,2%) và CAR chỉ giảm nhẹ 15 điểm cơ bản (từ 10,22% xuống 10,07%). "
    "Nguyên nhân cốt lõi của sự phân kỳ này nằm ở hai yếu tố: (i) Agribank đã duy trì bộ đệm dự phòng cụ thể và dự phòng chung rất lớn theo VAS (LLCR đạt 146,3%), trong khi MB để LLCR hợp nhất giảm xuống 93,8% (dự phòng cụ thể chỉ có 5.052 tỷ đồng trên 14.027 tỷ đồng nợ xấu); và (ii) MB chịu cú sốc trích lập Lifetime ECL tại Stage 2 (11.315 tỷ đồng so với 511 tỷ đồng theo VAS) do ngoài 10.210 tỷ nợ nhóm 2 và 6% dư nợ nhóm 1 có dấu hiệu gia tăng rủi ro (SICR), MB còn phải tính cả rủi ro của 30% danh mục trái phiếu doanh nghiệp TCKT (7.023 tỷ đồng). Trong mô hình cơ sở, LGD của Agribank được đặt ở mức 35% (Stage 1) và 45% (Stage 2) nhờ 89,0% tài sản bảo đảm là bất động sản, nhưng lên tới 85% ở Stage 3 do nợ nhóm 5 chiếm 79,0% nợ xấu và thời gian xử lý phát mại tài sản kéo dài nhiều năm làm suy giảm giá trị hiện tại ròng (NPV) của dòng tiền thu hồi; LGD của MB tương ứng là 45%, 50% và 65%. "
    "Để kiểm chứng tính vững (robustness) của kết luận trước sự thay đổi của các tham số giả định, nghiên cứu thực hiện Phân tích độ nhạy (Sensitivity Analysis – Bảng 4 trên sheet IFRS9_Simulation) với 6 kịch bản biến thiên tỷ lệ chuyển nhóm SICR (3%, 6%, 9%) và hệ số tổn thất LGD (±10 điểm % ở mọi giai đoạn):\n"
    "  • Kịch bản 1 – Cơ sở (Agribank SICR 5%, MB SICR 6%; LGD chuẩn): Agribank thiếu +3.660 tỷ đồng (CAR sau IFRS 9: 10,07%); MB thiếu +14.006 tỷ đồng (CAR: 9,97%).\n"
    "  • Kịch bản 2 – Tỷ lệ Nhóm 1 chuyển sang Stage 2 thấp (SICR = 3,0% cho cả hai NH): Agribank gần như đủ dự phòng, chỉ thiếu +2 tỷ đồng (CAR giữ nguyên 10,22%); MB vẫn thiếu +9.770 tỷ đồng (CAR: 10,28%).\n"
    "  • Kịch bản 3 – Tỷ lệ Nhóm 1 chuyển sang Stage 2 đồng nhất trung bình (SICR = 6,0% cho cả hai NH): Agribank thiếu +5.489 tỷ đồng (CAR: 10,00%); MB thiếu +14.006 tỷ đồng (CAR: 9,97%).\n"
    "  • Kịch bản 4 – Tỷ lệ Nhóm 1 chuyển sang Stage 2 cao (SICR = 9,0% cho cả hai NH): Agribank thiếu +10.977 tỷ đồng (CAR: 9,78%); MB thiếu +18.243 tỷ đồng (CAR: 9,66%).\n"
    "  • Kịch bản 5 – Hệ số LGD giảm 10 điểm % ở mọi giai đoạn (thanh khoản phát mại TSBĐ thuận lợi): Agribank thặng dư 3.691 tỷ đồng dự phòng (Gap = -3.691 tỷ, CAR giữ nguyên 10,22%); MB vẫn thiếu +8.846 tỷ đồng (CAR: 10,35%).\n"
    "  • Kịch bản 6 – Hệ số LGD tăng 10 điểm % ở mọi giai đoạn (thị trường BĐS đóng băng sâu): Agribank thiếu +11.011 tỷ đồng (CAR: 9,77%); MB thiếu +19.166 tỷ đồng (CAR giảm xuống 9,59%).\n"
    "Như vậy, trong cả 6 kịch bản độ nhạy, khoảng cách thiếu hụt dự phòng IFRS 9 của MB luôn lớn hơn đáng kể so với Agribank (từ +8.846 tỷ đến +19.166 tỷ đồng), khẳng định kết luận về áp lực trích lập bổ sung tại Stage 2 và Stage 3 của MB là hoàn toàn vững chắc về mặt định lượng."
)

# ==============================================================================
# ITEM #2, #10, #11, #13: CHAPTER 5 — 2020-2025 EMPIRICAL CASES & 4-PART STRUCTURE
# (Diễn biến -> Nguyên nhân -> Hậu quả -> Biện pháp khắc phục đã triển khai)
# ==============================================================================
set_para(P[103], "CHƯƠNG 5. PHÂN TÍCH TÌNH HUỐNG THỰC TIỄN GIAI ĐOẠN 2020–2025 (DIỄN BIẾN – NGUYÊN NHÂN – HẬU QUẢ – BIỆN PHÁP KHẮC PHỤC)", "")
P[103].runs[0].bold = True

set_para(P[104], "5.1. Agribank – Cú sốc thiên tai Yagi 2024, điểm nghẽn thanh khoản TSBĐ nợ nhóm 5 và bài học từ vụ Lifepro", "")
P[104].runs[0].bold = True

set_para(
    P[105],
    "1. Diễn biến và Dữ liệu thực chứng (2020–2025): ",
    "Trong giai đoạn 2020–2025, thực tiễn rủi ro tín dụng tại Agribank nổi lên hai vấn đề đặc thù gắn liền với định vị ngân hàng phục vụ 'Tam nông' và thể chế NHTM Nhà nước: (i) Cú sốc rủi ro tín dụng nông nghiệp diện rộng do thiên tai bão số 3 (Yagi) tháng 9/2024 tàn phá nặng nề 26 tỉnh, thành phố phía Bắc, làm đứt gãy hoàn toàn dòng tiền của hàng chục nghìn hộ nuôi trồng thủy sản, trồng trọt và doanh nghiệp nông nghiệp vay vốn tại Agribank; và (ii) Tình trạng tồn đọng nợ nhóm 5 (nợ có khả năng mất vốn) ở mức rất cao xuyên suốt 6 năm: theo Thuyết minh 9 BCTC hợp nhất kiểm toán 2020–2025, nợ nhóm 5 của Agribank luôn chiếm từ 67,0% đến 79,0% tổng nợ xấu nội bảng (năm 2020: 15.399 / 21.527 tỷ đồng = 71,5%; năm 2023: 19.744 / 28.721 tỷ đồng = 68,7%; năm 2025: 20.220 / 25.610 tỷ đồng = 79,0%), bên cạnh 278.372 tỷ đồng nợ đã xử lý rủi ro đang theo dõi ngoại bảng (Thuyết minh 37 BCTC hợp nhất 2025, trang 58) và các tồn đọng lịch sử tại Công ty Cho thuê Tài chính II (ALC II – mất khả năng thanh toán từ 2018, được Kiểm toán Nhà nước và kiểm toán độc lập nhấn mạnh tại Thuyết minh 39 BCTC hợp nhất 2025, trang 69) hay điển cứu vụ án Lifepro tại Chi nhánh Nam Hà Nội (thiệt hại gần 2.500 tỷ đồng do giải ngân vượt thẩm quyền và nhận TSBĐ khống)."
)

set_para(
    P[106],
    "2. Nguyên nhân, Hậu quả và Biện pháp khắc phục Agribank đã triển khai:\n",
    "  • Nguyên nhân (Khách quan & Chủ quan theo khung COSO 2013): Về khách quan, danh mục tín dụng của Agribank có tới 61,7%–70,0% dư nợ tập trung vào nông nghiệp – nông thôn (Thuyết minh 9 BCTC hợp nhất 2025 ghi nhận dư nợ ngành Nông, lâm, thủy sản đạt 506.223 tỷ đồng và cho vay cá nhân, hộ gia đình đạt 1.477.696 tỷ đồng), chịu rủi ro thiên tai, dịch bệnh và biến động giá nông sản mang tính hệ thống. Hơn nữa, 89,0%–91,8% tài sản bảo đảm của Agribank là bất động sản (năm 2025: 3.371.568 / 3.739.943 tỷ đồng), phần lớn là đất nông nghiệp, đất ở nông thôn có tính thanh khoản thứ cấp rất thấp; khi Nghị quyết 42/2017/QH14 hết hiệu lực vào ngày 31/12/2023, ngân hàng mất quyền thu giữ TSBĐ và phải chờ thủ tục khởi kiện – thi hành án kéo dài nhiều năm. Về chủ quan (theo 5 thành tố COSO 2013 trong các vụ việc như Lifepro và ALC II), cơ chế phân cấp hạn mức tín dụng rộng cho hơn 2.200 chi nhánh/PGD trong khi hệ thống công nghệ giám sát tập trung chưa đồng bộ đã từng tạo kẽ hở cho sự lạm quyền của người đứng đầu chi nhánh (Môi trường kiểm soát), thẩm định dựa dẫm vào tài sản thế chấp thay vì dòng tiền (Đánh giá rủi ro), vô hiệu hóa nguyên tắc phê duyệt kép (Hoạt động kiểm soát), độ trễ báo cáo rủi ro (Thông tin & Truyền thông) và kiểm toán nội bộ hậu kiểm thụ động (Giám sát).\n"
    "  • Hậu quả định lượng: Làm đóng băng vốn trong các khoản nợ nhóm 5 kéo dài (20.220 tỷ đồng cuối năm 2025), buộc Agribank phải chi tới 145.765 tỷ đồng chi phí dự phòng rủi ro tín dụng lũy kế 6 năm (2020–2025) – chiếm từ 42,8% đến 59,0% lợi nhuận thuần trước dự phòng (PPOP) hằng năm – và sử dụng tổng cộng 127.831 tỷ đồng quỹ dự phòng để xóa nợ nội bảng, làm suy giảm khả năng tự tích lũy vốn tự có và khiến RORAC proxy chỉ đạt 10,8%–16,7%.\n"
    "  • Biện pháp khắc phục Agribank đã triển khai: (1) Đối với cú sốc bão Yagi và Covid-19: Kịp thời cơ cấu lại thời hạn trả nợ, giữ nguyên nhóm nợ theo Thông tư 02/2023/TT-NHNN (37.876 tỷ đồng năm 2023, trích đủ 100% dự phòng bổ sung cuối năm 2024) và Thông tư 53/2024/TT-NHNN (trích dự phòng bổ sung tối thiểu 35% năm 2024 và 70% năm 2025), kết hợp giảm lãi suất cho vay hỗ trợ phục hồi sản xuất nông nghiệp; (2) Về xử lý và thu hồi nợ xấu: Đẩy mạnh trích lập dự phòng (năm 2025 trích 31.808 tỷ đồng, đưa LLCR hợp nhất lên 146,3%) và sử dụng 32.621 tỷ đồng dự phòng để xử lý rủi ro; đồng thời thành lập Ban chỉ đạo xử lý nợ xấu từ Hội sở xuống từng chi nhánh, phối hợp cơ quan thi hành án và áp dụng Luật số 96/2025/QH15 (Điều 198a) để thu hồi nợ đã xử lý rủi ro đạt 12.123 tỷ đồng trên BCTC năm 2025 (16.305 tỷ đồng tính cả thu từ xử lý tài sản theo BCTN 2025); (3) Về tái cấu trúc quản trị nội bộ: Siết chặt hạn mức phán quyết tín dụng của Giám đốc chi nhánh, chuẩn hóa định giá TSBĐ độc lập và bổ sung 17.100 tỷ đồng vốn điều lệ từ ngân sách Nhà nước (nâng vốn điều lệ lên 51.639 tỷ đồng cuối năm 2025)."
)

set_para(P[107], "5.2. MB – Rủi ro tín dụng tiêu dùng tại MCredit và rủi ro đạo đức cấp chi nhánh (Vụ Gia Lai 2022–2023)", "")
P[107].runs[0].bold = True

set_para(
    P[108],
    "1. Diễn biến và Dữ liệu thực chứng (2020–2025): ",
    "Tại MB, chiến lược mở rộng sang phân khúc bán lẻ và tài chính tiêu dùng biên lợi nhuận cao trong giai đoạn 2020–2025 đã bộc lộ hai mặt rủi ro thực tiễn: (i) Ở cấp độ danh mục tập đoàn, khi bóc tách chênh lệch giữa BCTC Hợp nhất và BCTC Riêng lẻ ngân hàng mẹ (Thuyết minh 10.1 và 10.4), dư nợ cho vay tiêu dùng của khối công ty con (chủ yếu là Công ty Tài chính TNHH MB Shinsei – MCredit, cùng MBCambodia từ 2023) đã tăng gấp 2,9 lần từ 10.173 tỷ đồng (2020) lên 29.622 tỷ đồng (2025). Tuy nhiên, nợ xấu nhóm 3–5 của khối công ty con tăng vọt từ 555 tỷ đồng (2020) lên 1.351 tỷ (2022), 1.662 tỷ (2023), 1.981 tỷ (2024) và 2.509 tỷ đồng (2025) – tương ứng tỷ lệ NPL công ty con lên tới 6,2%–8,5% (cao gấp 5–7 lần NPL ngân hàng mẹ là 1,12% năm 2025), làm suy giảm lợi nhuận MCredit năm 2023–2024 trước khi phục hồi năm 2025; (ii) Ở cấp độ tác nghiệp chi nhánh, giai đoạn 2022–2023 phát sinh vụ việc cán bộ tín dụng tại MB Chi nhánh Gia Lai lợi dụng kẽ hở trong quy trình giải ngân bán lẻ và đảo nợ để lập khống hồ sơ vay vốn, giả mạo chữ ký khách hàng chiếm đoạt hàng chục tỷ đồng."
)

set_para(
    P[109],
    "2. Nguyên nhân, Hậu quả và Biện pháp khắc phục MB đã triển khai:\n",
    "  • Nguyên nhân (Theo Mô hình Tam giác Gian lận của Cressey, 1953 và Khẩu vị rủi ro tín chấp): (1) Áp lực (Pressure): Chỉ tiêu KPI tăng trưởng dư nợ bán lẻ và biên lãi thuần (NIM) rất cao giao xuống từng RM và công ty con tạo áp lực giải ngân nhanh; tại MCredit, tệp khách hàng chủ đạo là người lao động thu nhập trung bình – thấp vay tín chấp (không có TSBĐ), nên khi kinh tế suy giảm và lạm phát tăng năm 2022–2024, khả năng trả nợ lập tức suy sụp; (2) Cơ hội (Opportunity): Tại các phòng giao dịch địa phương xa Hội sở (như vụ Gia Lai), quy trình xác thực thực địa, quản lý hồ sơ giải ngân và kiểm tra chéo sau cho vay từng bị buông lỏng; (3) Hợp lý hóa hành vi (Rationalization): Cán bộ tín dụng tự biện minh rằng việc hỗ trợ khách hàng đảo nợ tạm thời sẽ được khắc phục khi giải ngân khoản vay mới.\n"
    "  • Hậu quả định lượng: Riêng khối công ty con (chủ yếu MCredit) đã tạo ra 2.509 tỷ đồng nợ xấu nội bảng cuối năm 2025 (chiếm 17,9% tổng nợ xấu hợp nhất của MB dù chỉ chiếm 2,7% tổng dư nợ), kéo tỷ lệ NPL hợp nhất của MB cao hơn NPL riêng lẻ từ 0,17 đến 0,26 điểm % mỗi năm (năm 2025: 1,29% so với 1,12%), đồng thời buộc khối công ty con phải sử dụng tới 4.362 tỷ đồng dự phòng để xóa nợ riêng trong năm 2025 (12.185 tỷ hợp nhất trừ 7.824 tỷ riêng lẻ).\n"
    "  • Biện pháp khắc phục MB đã triển khai: (1) Tái cấu trúc khẩu vị rủi ro và mô hình chấm điểm tại MCredit: Siết chặt tiêu chuẩn phê duyệt khoản vay tiền mặt (cash loan), tích hợp xác thực sinh trắc học eKYC kết nối cơ sở dữ liệu dân cư quốc gia (Đề án 06 – Bộ Công an) để triệt tiêu gian lận hồ sơ giả mạo; (2) Quyết liệt xử lý nợ xấu bằng dự phòng: Trong năm 2025, khối công ty con sử dụng 4.362 tỷ đồng dự phòng để xóa các khoản nợ tiêu dùng mất khả năng thu hồi, giúp MCredit làm sạch bảng cân đối và phục hồi lợi nhuận; (3) Kiện toàn 3 tuyến phòng vệ tại ngân hàng mẹ: Tách bạch hoàn toàn bộ phận quan hệ khách hàng (RM) tại chi nhánh với Trung tâm Thẩm định và Phê duyệt tín dụng tập trung (Hub/Hội sở), đồng thời áp dụng Kiểm toán nội bộ dựa trên dữ liệu lớn (Audit Analytics) để phát hiện sớm các giao dịch giải ngân bất thường."
)

set_para(P[110], "5.3. MB – Cú sốc chất lượng tài sản năm 2023: Khủng hoảng thanh khoản TPDN, BĐS và hiệu ứng CIC", "")
P[110].runs[0].bold = True

set_para(
    P[111],
    "Phân tích toàn diện (Diễn biến – Nguyên nhân – Hậu quả – Biện pháp khắc phục):\n",
    "  • 1. Diễn biến và Số liệu kiểm toán: Năm 2023 đánh dấu cú sốc chất lượng tài sản lớn nhất của MB trong giai đoạn 2020–2025: theo Thuyết minh 10.1 BCTC hợp nhất 2023, nợ xấu nội bảng hợp nhất của MB tăng vọt 94,9% từ 5.031 tỷ đồng (cuối 2022) lên 9.805 tỷ đồng (cuối 2023), đẩy tỷ lệ NPL hợp nhất từ 1,09% lên 1,60%; đồng thời nợ nhóm 2 tăng 78,2% từ 7.809 tỷ lên 13.918 tỷ đồng (chiếm 2,28% dư nợ), đưa Tỷ lệ nợ có vấn đề (Nhóm 2–5) lên đỉnh 3,88%.\n"
    "  • 2. Nguyên nhân: Xuất phát từ sự cộng hưởng của ba yếu tố: (i) Rủi ro tập trung vào chu kỳ Bất động sản – Xây dựng và Trái phiếu doanh nghiệp (TPDN): Đến cuối năm 2022, bên cạnh dư nợ cho vay BĐS & Xây dựng chiếm 10,7% dư nợ, MB còn nắm giữ 46.870 tỷ đồng trái phiếu do các tổ chức kinh tế (TCKT) phát hành (ngoài 66.307 tỷ đồng chứng khoán nợ do các TCTD phát hành theo Thuyết minh 12 BCTC hợp nhất 2022). Khi thị trường TPDN đóng băng sau các sự kiện Tân Hoàng Minh (4/2022) và Vạn Thịnh Phát (10/2022) cùng mặt bằng lãi suất tăng cao, dòng tiền của các chủ đầu tư BĐS và năng lượng tái tạo bị tắc nghẽn; (ii) Hiệu ứng phân loại nợ liên đới qua CIC theo Điều 10 Thông tư 11/2021/TT-NHNN: Nhiều khách hàng doanh nghiệp dù vẫn trả nợ đúng hạn tại MB nhưng phát sinh nợ quá hạn tại ngân hàng khác nên buộc phải chuyển nhóm nợ đồng loạt tại MB; và (iii) Hành vi giảm trích lập dự phòng trong năm cú sốc: Năm 2023, dù nợ xấu tăng 94,9%, chi phí dự phòng rủi ro tín dụng trên Báo cáo KQKD hợp nhất của MB lại giảm 24,4% (từ 8.048 tỷ xuống 6.087 tỷ đồng).\n"
    "  • 3. Hậu quả định lượng: Làm bào mòn nhanh chóng bộ đệm dự phòng mà MB đã tích lũy trong giai đoạn 2020–2022: tỷ lệ bao phủ nợ xấu (LLCR) hợp nhất của MB sụt giảm hơn một nửa từ 238,0% (cuối 2022) xuống 117,0% (cuối 2023) và rơi xuống dưới ngưỡng 100% trong hai năm tiếp theo (92,3% năm 2024 và 93,8% năm 2025).\n"
    "  • 4. Biện pháp khắc phục MB đã triển khai: (1) Chủ động thu hẹp mạnh danh mục TPDN: MB đã quyết liệt cơ cấu lại danh mục chứng khoán đầu tư, cắt giảm 50,1% số dư TPDN do TCKT phát hành từ mức đỉnh 46.870 tỷ đồng (cuối 2022) xuống 38.448 tỷ đồng (2023), 33.443 tỷ đồng (2024) và chỉ còn 23.410 tỷ đồng vào cuối năm 2025 (tương đương chỉ còn 2,1% tổng dư nợ tín dụng theo Thuyết minh 12/13 BCTC hợp nhất 2025); (2) Chuyển dịch cấu trúc tài trợ BĐS: Tập trung tài trợ theo chuỗi cung ứng khép kín (nhà thầu – chủ đầu tư – người mua nhà cuối cùng có nhu cầu ở thực), kiểm soát dòng tiền qua tài khoản chuyên thu tại MB và tăng tỷ lệ tài sản bảo đảm là bất động sản từ 46,8% (2022) lên 50,5% tổng giá trị TSBĐ năm 2025 (1.025.681 / 2.030.363 tỷ đồng)."
)

set_para(P[112], "5.4. MB – Biến động nợ xấu Quý III–IV/2025, xử lý rủi ro bằng dự phòng và quy chế không hợp nhất MBV", "")
P[112].runs[0].bold = True

set_para(
    P[113],
    "Phân tích toàn diện (Diễn biến – Nguyên nhân – Hậu quả – Biện pháp khắc phục):\n",
    "  • 1. Diễn biến và Số liệu kiểm toán: Theo số liệu BCTC Quý III/2025 được công bố, tổng nợ xấu nội bảng hợp nhất của MB tại thời điểm 30/9/2025 vọt lên mức đỉnh lịch sử 17.423 tỷ đồng, đẩy tỷ lệ NPL lên khoảng 1,87%. Tuy nhiên, chỉ trong vòng một quý (Quý IV/2025), báo cáo tài chính hợp nhất kiểm toán năm 2025 ghi nhận nợ xấu cuối năm giảm 3.396 tỷ đồng về mức 14.027 tỷ đồng, và tỷ lệ NPL hợp nhất giảm mạnh 0,58 điểm % về mức 1,29% (NPL riêng lẻ ngân hàng mẹ giảm về 1,12%).\n"
    "  • 2. Nguyên nhân: Biến động mạnh của nợ xấu trong năm 2025 bắt nguồn từ hai cơ chế: (i) Áp lực nhảy nhóm nợ tự nhiên sau khi Thông tư 02/2023/TT-NHNN hết hiệu lực từ ngày 01/01/2025 khiến các khoản nợ cơ cấu không phục hồi kịp dòng tiền trong 9 tháng đầu năm phải chuyển sang nhóm nợ xấu theo quy định tại Thông tư 31/2024/TT-NHNN; và (ii) Cơ chế xử lý kỹ thuật cuối năm thông qua sự kết hợp giữa xóa nợ bằng dự phòng và mở rộng quy mô mẫu số dư nợ. Đặc biệt, như đã chứng minh tại Mục 4.1 theo Thuyết minh 3.4 BCTC hợp nhất 2025 (trang 148 PDF), căn cứ Điểm c Khoản 1 Điều 185 Luật Các TCTD 2024, MB không hợp nhất BCTC của Ngân hàng TNHH MTV Việt Nam Hiện Đại (MBV / OceanBank), nên biến động nợ xấu và dư nợ Quý III–IV/2025 hoàn toàn phản ánh hoạt động của MB và 7 công ty con hợp nhất.\n"
    "  • 3. Hậu quả định lượng: Mặc dù tỷ lệ NPL bề mặt giảm đẹp về 1,29% cuối năm 2025, nhưng xét trên toàn năm 2025, nợ xấu nội bảng tuyệt đối của MB vẫn tăng thêm +1.442 tỷ đồng (+11,5% so với mức 12.585 tỷ đồng cuối năm 2024), và tỷ lệ bao phủ nợ xấu (LLCR) hợp nhất chỉ đạt 93,8% (13.151 tỷ dự phòng / 14.027 tỷ nợ xấu) – thấp hơn đáng kể so với mức 146,3% của Agribank.\n"
    "  • 4. Biện pháp khắc phục MB đã triển khai: (1) Tăng mạnh trích lập và sử dụng dự phòng để làm sạch bảng cân đối: Trong năm 2025, MB đã tăng chi phí dự phòng rủi ro tín dụng hợp nhất thêm 43,5% lên mức kỷ lục 13.744 tỷ đồng (tương đương 28,6% lợi nhuận trước dự phòng PPOP), đồng thời sử dụng 12.185 tỷ đồng dự phòng để xóa nợ nội bảng (Thuyết minh 10 BCTC hợp nhất 2025); (2) Tận dụng hạn mức tăng trưởng tín dụng cao (được NHNN cấp nhờ nhận chuyển giao bắt buộc MBV) để giải ngân 307.361 tỷ đồng dư nợ mới (+39,6%) vào các phân khúc khách hàng doanh nghiệp và bán lẻ chất lượng tốt (Nhóm 1 đạt 1.059.782 tỷ đồng), tạo hiệu ứng mẫu số kéo giảm NPL (-0,46 điểm %); và (3) Đẩy mạnh thu hồi nợ đã xử lý rủi ro ngoại bảng đạt 4.142 tỷ đồng trong năm 2025 (tăng 74,0% so với mức 2.381 tỷ đồng năm 2024 theo Thuyết minh KQKD BCTC hợp nhất 2025)."
)

# Update Table 11 (Bảng 12 - COSO 2013 Matrix) to reflect both 2020-2025 cases and historical cases
row_set(T[11], 0, ["Thành tố COSO 2013", "Agribank (Cú sốc Yagi, Nợ nhóm 5 & Vụ Lifepro)", "MB (MCredit, Cú sốc TPDN 2023 & Vụ Gia Lai)"])
row_set(T[11], 1, ["1. Môi trường kiểm soát", "Mạng lưới >2.200 CN/PGD phân cấp rộng; vụ Lifepro cho thấy nguy cơ lạm quyền cấp chi nhánh đã được khắc phục bằng siết hạn mức phán quyết.", "Áp lực KPI tăng trưởng tín dụng và ROE cao; tách bạch RM và Phê duyệt tập trung (Hub) giúp kiểm soát rủi ro đạo đức cấp cơ sở."])
row_set(T[11], 2, ["2. Đánh giá rủi ro", "Tập trung 61,7%–70% vào Tam nông nên nhạy cảm với cú sốc thiên tai (bão Yagi 2024); phụ thuộc cao vào TSBĐ đất nông nghiệp thanh khoản thấp.", "Giai đoạn 2020–2022 mở rộng nhanh vào TPDN (46.870 tỷ năm 2022) và tín chấp MCredit (NPL 6,2%–8,5%); đã cắt giảm 50,1% TPDN đến 2025."])
row_set(T[11], 3, ["3. Hoạt động kiểm soát", "Nợ nhóm 5 chiếm 67%–79% nợ xấu do thủ tục phát mại TSBĐ kéo dài; trích lập dự phòng dày (LLCR 146,3%) và xóa nợ 32.621 tỷ năm 2025.", "Tự động hóa chấm điểm Scorecard và eKYC tại MCredit; xóa nợ hợp nhất 12.185 tỷ năm 2025 nhưng để LLCR hợp nhất giảm về 92,3%–93,8%."])
row_set(T[11], 4, ["4. Thông tin & Truyền thông", "Hiện đại hóa hệ thống cảnh báo sớm nhưng dữ liệu khách hàng nông hộ nhỏ lẻ vẫn phân tán, chưa lượng hóa đầy đủ PD/LGD theo chuẩn IRB.", "Hệ thống OFSAA/ICAAP hiện đại; tuy nhiên năm 2023 chịu tác động mạnh từ hiệu ứng nhảy nhóm nợ liên đới qua hệ thống CIC."])
row_set(T[11], 5, ["5. Hoạt động giám sát", "Chịu sự giám sát chặt của NHNN và Kiểm toán Nhà nước (điều chỉnh hồi tố BCTC 2021–2024); thu hồi nợ ngoại bảng đạt 12.123–16.305 tỷ năm 2025.", "Kiểm toán nội bộ dựa trên dữ liệu (Audit Analytics); tận dụng cơ chế miễn hợp nhất MBV (Điều 185 Luật TCTD 2024) để giữ lành mạnh bảng cân đối."])

# ==============================================================================
# ITEM #7 & #9: UPDATE TABLE 12 (Bảng 13) AND CHAPTER 6 (P[115]..P[117])
# ==============================================================================
set_para(P[115], "CHƯƠNG 6. ĐÁNH GIÁ KẾT QUẢ ĐẠT ĐƯỢC, HẠN CHẾ, NGUYÊN NHÂN VÀ SO SÁNH HAI MÔ HÌNH", "")
P[115].runs[0].bold = True

row_set(
    T[12], 5,
    [
        "5. Độ nhạy trước IFRS 9",
        "Ít bị ảnh hưởng (thiếu hụt +9,8% tương đương +3.660 tỷ DP, CAR chỉ giảm 15 bps từ 10,22% về 10,07%) nhờ LLCR hiện hữu 146,3% và 88%–92% TSBĐ là bất động sản.",
        "Chịu tác động lớn (thiếu hụt +106,5% tương đương +14.006 tỷ DP, CAR giảm 103 bps từ 11,00% về 9,97%) do LLCR hiện hữu 93,8%, danh mục tín chấp MCredit và TPDN."
    ]
)

# Let's add the comprehensive evaluation of Kết quả đạt được – Hạn chế – Nguyên nhân for Agribank and MB right after Table 12 (Bảng 13)!
# Wait: let's also add the analytical paragraph for Section 1.3 right after Table 0 (Bảng 1), and source lines under all 13 tables!
# First, let's update Chapter 7 item 7.1 (P[120]) so it reflects that Luật số 96/2025/QH15 HAS ALREADY been enacted (effective 15/10/2025) and recommends guiding decrees for its implementation!
set_para(
    P[120],
    None,
    "1. Ban hành Lộ trình Bắt buộc áp dụng Chuẩn mực IFRS 9: NHNN và Bộ Tài chính cần ban hành thông tư hướng dẫn triển khai chuẩn mực IFRS 9 (mô hình tổn thất tín dụng kỳ vọng ECL) theo lộ trình phân tầng đối với các NHTM quy mô lớn, khắc phục độ trễ ghi nhận rủi ro tại Stage 2 của mô hình tổn thất đã phát sinh hiện hành.\n"
    "2. Hướng dẫn thực thi hiệu quả Luật số 96/2025/QH15 về thu giữ và xử lý tài sản bảo đảm: Sau khi Luật số 96/2025/QH15 (có hiệu lực từ 15/10/2025) chính thức luật hóa quyền thu giữ tài sản bảo đảm (Điều 198a) và cơ chế hoàn trả TSBĐ là vật chứng (Điều 198b, 198c), Chính phủ và NHNN cần sớm ban hành quy chế phối hợp liên ngành với Bộ Công an, Tòa án và Cơ quan Thi hành án địa phương để tháo gỡ triệt để khối nợ nhóm 5 tồn đọng (như 20.220 tỷ đồng nợ nhóm 5 và 278.372 tỷ đồng nợ ngoại bảng tại Agribank).\n"
    "3. Giám sát Rủi ro Tập trung Đa chiều và Lộ trình giảm giới hạn cấp tín dụng theo Luật Các TCTD 2024: Giám sát chặt chẽ lộ trình giảm giới hạn cấp tín dụng theo Điều 136 và Điều 210 Luật Các TCTD 2024 (từ 14%/23% vốn tự có năm 2024–2025 về 10%/15% năm 2029), đồng thời tính gộp cả dư nợ cho vay, đầu tư trái phiếu doanh nghiệp (TPDN) và cam kết ngoại bảng vào tổng mức phơi nhiễm rủi ro của một nhóm khách hàng liên quan."
)

# ==============================================================================
# ITEM #14: REORDER & STANDARDIZE REFERENCES (P[128]..P[148])
# ==============================================================================
sorted_refs = [
    # I. Tài liệu tiếng Việt (Văn bản pháp luật, Báo cáo ngành & Báo cáo ngân hàng - xếp theo ABC cơ quan ban hành)
    "[1] Agribank (2021, 2022, 2023, 2024, 2025, 2026), Báo cáo tài chính hợp nhất và Báo cáo tài chính riêng lẻ kiểm toán các năm 2020–2025 (đã kiểm toán bởi Ernst & Young Việt Nam và Deloitte Việt Nam).",
    "[2] Agribank (2021, 2022, 2023, 2024, 2025, 2026), Báo cáo thường niên các năm 2020–2025, Ngân hàng Nông nghiệp và Phát triển Nông thôn Việt Nam.",
    "[3] Chính phủ Nước CHXHCN Việt Nam (2024), Nghị định số 86/2024/NĐ-CP ngày 11/7/2024 quy định về mức trích, phương pháp trích lập dự phòng rủi ro và việc sử dụng dự phòng để xử lý rủi ro trong hoạt động của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài.",
    "[4] Hiệp hội Ngân hàng Việt Nam – VNBA & Ngân hàng Nhà nước Việt Nam (2023, 2024, 2025), Báo cáo tổng kết hoạt động kinh doanh ngân hàng và tình hình xử lý nợ xấu toàn hệ thống giai đoạn 2020–2025.",
    "[5] Ngân hàng Nhà nước Việt Nam (2016), Thông tư số 41/2016/TT-NHNN ngày 30/12/2016 quy định tỷ lệ an toàn vốn đối với ngân hàng, chi nhánh ngân hàng nước ngoài theo chuẩn mực Basel II.",
    "[6] Ngân hàng Nhà nước Việt Nam (2019), Thông tư số 22/2019/TT-NHNN ngày 15/11/2019 quy định các giới hạn, tỷ lệ bảo đảm an toàn trong hoạt động của ngân hàng, chi nhánh ngân hàng nước ngoài.",
    "[7] Ngân hàng Nhà nước Việt Nam (2020, 2021), Thông tư số 01/2020/TT-NHNN ngày 13/3/2020 (sửa đổi, bổ sung bởi Thông tư 03/2021/TT-NHNN và Thông tư 14/2021/TT-NHNN) quy định về cơ cấu lại thời hạn trả nợ, miễn, giảm lãi, phí, giữ nguyên nhóm nợ hỗ trợ khách hàng chịu ảnh hưởng bởi dịch Covid-19.",
    "[8] Ngân hàng Nhà nước Việt Nam (2021), Thông tư số 11/2021/TT-NHNN ngày 30/7/2021 quy định về phân loại tài sản có, mức trích, phương pháp trích lập dự phòng rủi ro và việc sử dụng dự phòng để xử lý rủi ro trong hoạt động của TCTD.",
    "[9] Ngân hàng Nhà nước Việt Nam (2023, 2024), Thông tư số 02/2023/TT-NHNN ngày 23/4/2023 (gia hạn bởi Thông tư 06/2024/TT-NHNN) quy định về việc cơ cấu lại thời hạn trả nợ và giữ nguyên nhóm nợ nhằm hỗ trợ khách hàng gặp khó khăn.",
    "[10] Ngân hàng Nhà nước Việt Nam (2024), Thông tư số 31/2024/TT-NHNN ngày 30/6/2024 quy định về phân loại tài sản có trong hoạt động của ngân hàng thương mại, tổ chức tín dụng phi ngân hàng, chi nhánh ngân hàng nước ngoài.",
    "[11] Ngân hàng Nhà nước Việt Nam (2024), Thông tư số 53/2024/TT-NHNN ngày 04/12/2024 quy định về việc cơ cấu lại thời hạn trả nợ đối với khách hàng gặp khó khăn do ảnh hưởng, thiệt hại của bão số 3 (Yagi).",
    "[12] Ngân hàng TMCP Quân đội – MB (2021, 2022, 2023, 2024, 2025, 2026), Báo cáo tài chính hợp nhất và Báo cáo tài chính riêng lẻ kiểm toán các năm 2020–2025 (đã kiểm toán bởi KPMG Việt Nam).",
    "[13] Ngân hàng TMCP Quân đội – MB (2021, 2022, 2023, 2024, 2025, 2026), Báo cáo thường niên và Báo cáo công bố thông tin tỷ lệ an toàn vốn (Basel II Pillar 3) các năm 2020–2025.",
    "[14] Quốc hội Nước CHXHCN Việt Nam (2017), Nghị quyết số 42/2017/QH14 ngày 21/6/2017 về thí điểm xử lý nợ xấu của các tổ chức tín dụng (gia hạn bởi Nghị quyết số 63/2022/QH15 đến 31/12/2023).",
    "[15] Quốc hội Nước CHXHCN Việt Nam (2024), Luật Các tổ chức tín dụng số 32/2024/QH15 thông qua ngày 18/01/2024, có hiệu lực thi hành từ ngày 01/7/2024.",
    "[16] Quốc hội Nước CHXHCN Việt Nam (2025), Luật số 96/2025/QH15 sửa đổi, bổ sung một số điều của Luật Các tổ chức tín dụng, có hiệu lực thi hành từ ngày 15/10/2025.",
    # II. Tài liệu tiếng Anh (Học thuật & Chuẩn mực quốc tế - xếp theo ABC tác giả)
    "[17] Basel Committee on Banking Supervision – BCBS (2006), International Convergence of Capital Measurement and Capital Standards: A Revised Framework (Basel II), Bank for International Settlements (BIS).",
    "[18] Basel Committee on Banking Supervision – BCBS (2017), Basel III: Finalising post-crisis reforms, Bank for International Settlements (BIS).",
    "[19] Committee of Sponsoring Organizations of the Treadway Commission – COSO (2013), Internal Control — Integrated Framework, AICPA.",
    "[20] Cressey, D. R. (1953), Other People's Money: A Study in the Social Psychology of Embezzlement, Glencoe, IL: Free Press.",
    "[21] International Accounting Standards Board – IASB (2014), IFRS 9 Financial Instruments, London: IFRS Foundation.",
    "[22] Jensen, M. C., & Meckling, W. H. (1976), 'Theory of the firm: Managerial behavior, agency costs and ownership structure', Journal of Financial Economics, 3(4), 305–360.",
    "[23] Laeven, L., & Majnoni, G. (2003), 'Loan loss provisioning and economic slowdowns: Too much, too late?', Journal of Financial Intermediation, 12(2), 178–197.",
    "[24] Stiglitz, J. E., & Weiss, A. (1981), 'Credit rationing in markets with imperfect information', The American Economic Review, 71(3), 393–410."
]

# Update P[128]..P[148] (21 paragraphs) and append 3 more for the 24 sorted references
for idx in range(21):
    set_para(P[128 + idx], None, sorted_refs[idx])
last_ref_p = P[148]
for extra_ref in sorted_refs[21:]:
    last_ref_p = insert_para_after(last_ref_p, None, extra_ref, italic=False)

# ==============================================================================
# INSERT NEW PARAGRAPHS AFTER TABLES (Done last so earlier paragraph indices P[...] never shifted!)
# 1. Analytical paragraph in Section 1.3 + Source lines for all 13 tables
# 2. Comprehensive Evaluation subsections 6.1 & 6.2 in Chapter 6 after Table 12 (Bảng 13)
# ==============================================================================
table_sources = {
    0: ("Nguồn: ", "Tổng hợp từ hệ thống văn bản quy phạm pháp luật của Quốc hội, Chính phủ và Ngân hàng Nhà nước Việt Nam giai đoạn 2016–2025."),
    1: ("Nguồn: ", "Tổng hợp từ Báo cáo của Ngân hàng Nhà nước Việt Nam (NHNN), Hiệp hội Ngân hàng Việt Nam (VNBA) và FiinGroup giai đoạn 2020–2025 (đồng bộ 100% với dòng 52–56 sheet Du_lieu)."),
    2: ("Nguồn: ", "Tổng hợp và đối chiếu từ Báo cáo thường niên, Báo cáo quản trị công ty và Báo cáo Basel II (Pillar 3) của Agribank và MB giai đoạn 2020–2025."),
    3: ("Nguồn: ", "Nhóm nghiên cứu thiết lập dựa trên Khung Basel II/III (BCBS, 2006, 2017) và Thông tư 11/2021/TT-NHNN, Thông tư 31/2024/TT-NHNN (tính toán tại sheet Chi_tieu)."),
    4: ("Nguồn: ", "Trích xuất và tính toán từ Thuyết minh 9/10 BCTC hợp nhất kiểm toán, BCTC riêng lẻ kiểm toán và Báo cáo thường niên 2020–2025 của Agribank và MB (sheet BCTC_Agribank_Goc, BCTC_MB_Goc, Du_lieu và Chi_tieu)."),
    5: ("Nguồn: ", "Trích xuất từ Báo cáo KQKD hợp nhất kiểm toán và Thuyết minh biến động dự phòng rủi ro cho vay khách hàng (TM 10/11 Agribank; TM 11/10 MB) giai đoạn 2020–2025."),
    6: ("Nguồn: ", "Trích xuất từ Thuyết minh phân tích chất lượng nợ cho vay (TM 9/10 Agribank; TM 10.1/9.1 MB) và Báo cáo thường niên 2021 (tr.41 MB), 2023 (tr.39 Agribank). Các năm không thuyết minh số dư nợ cơ cấu tuyệt đối trên BCTC được ghi nhận là 'n.a.'."),
    7: ("Nguồn: ", "Tính toán của nhóm nghiên cứu từ Báo cáo KQKD hợp nhất và Bảng CĐKT hợp nhất kiểm toán 2020–2025 của Agribank và MB trên cùng cơ sở mẫu số vốn tối thiểu ước tính = 8% × Dư nợ cho vay hợp nhất (sheet Chi_tieu, dòng 20–21 và 35–37)."),
    8: ("Nguồn: ", "Trích xuất từ Thuyết minh cho vay theo ngành kinh tế (TM 9/10 Agribank; TM 10.4 MB), Thuyết minh chứng khoán đầu tư (TM 12/13 MB) và Báo cáo thường niên / Pillar 3 2020–2025."),
    9: ("Nguồn: ", "Kết quả mô hình hóa của nhóm nghiên cứu tại sheet Stress_Testing dựa trên số liệu gốc năm 2025 từ BCTC hợp nhất kiểm toán của Agribank và MB."),
    10: ("Nguồn: ", "Kết quả mô phỏng định lượng của nhóm nghiên cứu tại sheet IFRS9_Simulation dựa trên số liệu phân nhóm nợ, dự phòng và tài sản bảo đảm cuối năm 2025 của Agribank và MB."),
    11: ("Nguồn: ", "Tổng hợp và phân tích của nhóm nghiên cứu theo Khung Kiểm soát Nội bộ COSO (2013) từ dữ liệu BCTC kiểm toán 2020–2025 và hồ sơ các vụ việc thực tiễn."),
    12: ("Nguồn: ", "Tổng hợp kết quả nghiên cứu thực chứng và mô hình hóa định lượng giai đoạn 2020–2025 của nhóm tác giả.")
}

# Insert source paragraphs right after each table, plus analytical text after Table 0 and Table 12
for t_idx in range(13):
    lbl_s, body_s = table_sources[t_idx]
    src_p = insert_para_after_table(T[t_idx], lbl_s, body_s, italic=True, size_pt=10.5)

    # ITEM #8: Add deep legal regime analysis in Section 1.3 right after Table 0 (Bảng 1) source line
    if t_idx == 0:
        insert_para_after(
            src_p,
            "Phân tích sự chuyển dịch chu kỳ chính sách pháp lý (2020–2025): ",
            "Hệ thống văn bản quy phạm pháp luật tại Bảng 1 phản ánh rõ nét hai giai đoạn điều hành trái ngược của cơ quan quản lý trong giai đoạn 2020–2025: "
            "(1) Giai đoạn 2020–2023 là giai đoạn Khoan dung pháp lý (Regulatory Forbearance) ứng phó với cú sốc đại dịch Covid-19 và khủng hoảng thanh khoản trái phiếu doanh nghiệp – bất động sản: Thông tư 01/2020/TT-NHNN (sửa đổi bởi Thông tư 03 và 14/2021) và sau đó là Thông tư 02/2023/TT-NHNN (gia hạn bởi Thông tư 06/2024 đến hết 31/12/2024) cho phép các TCTD cơ cấu lại thời hạn trả nợ và giữ nguyên nhóm nợ, đồng thời phân bổ chi phí trích lập dự phòng bổ sung theo lộ trình nhiều năm (30%–60%–100% đối với nợ cơ cấu Covid; 50% năm 2023 và 100% năm 2024 đối với nợ cơ cấu Thông tư 02). Cơ chế này giúp ngăn chặn cú sốc nhảy nhóm nợ hàng loạt trên hệ thống CIC nhưng tạo ra độ trễ giữa chất lượng tài sản thực tế và tỷ lệ nợ xấu nội bảng; "
            "(2) Giai đoạn 2024–2025 đánh dấu bước ngoặt siết kỷ cương pháp lý và chuẩn hóa toàn diện theo thông lệ quốc tế: Luật Các tổ chức tín dụng số 32/2024/QH15 (có hiệu lực từ 01/7/2024) đã siết chặt rủi ro tập trung thông qua việc thiết lập lộ trình giảm giới hạn cấp tín dụng tại Điều 136 và Điều 210 (tổng mức cấp tín dụng đối với một khách hàng giảm từ 15% vốn tự có xuống 14% trong giai đoạn 2024–2025 và giảm dần về 10% từ năm 2029; đối với một khách hàng và người có liên quan giảm từ 25% xuống 23% và về 15% từ năm 2029), đồng thời quy định cơ chế đặc thù miễn hợp nhất báo cáo tài chính đối với ngân hàng nhận chuyển giao bắt buộc tại Điều 185 (cơ sở pháp lý trực tiếp để MB không hợp nhất BCTC của MBV/OceanBank). Song song đó, từ ngày 01/7/2024, Thông tư 31/2024/TT-NHNN và Nghị định 86/2024/NĐ-CP chính thức thay thế Thông tư 11/2021/TT-NHNN, tách bạch quy định phân loại nợ (thuộc thẩm quyền NHNN) và quy định trích lập, sử dụng dự phòng xử lý rủi ro (thuộc thẩm quyền Chính phủ). Đặc biệt, sau khi Nghị quyết 42/2017/QH14 hết hiệu lực vào ngày 31/12/2023 gây ra khoảng trống pháp lý làm đình trệ công tác thu giữ tài sản bảo đảm trong gần hai năm 2024–2025, Quốc hội đã ban hành Luật số 96/2025/QH15 (có hiệu lực từ 15/10/2025) bổ sung Điều 198a, 198b và 198c vào Luật Các TCTD, chính thức luật hóa quyền thu giữ tài sản bảo đảm của khoản nợ xấu và tháo gỡ điểm nghẽn phát mại nợ nhóm 5 cho toàn hệ thống ngân hàng.",
            italic=False,
            size_pt=12
        )

    # ITEM #9: Add explicit sections 6.1 & 6.2 (Kết quả đạt được – Hạn chế – Nguyên nhân) right after Table 12 (Bảng 13) source line
    if t_idx == 12:
        p_61_hdr = insert_para_after(
            src_p,
            "6.1. Đánh giá tổng hợp công tác quản trị rủi ro tín dụng tại Agribank (2020–2025)",
            "",
            italic=False,
            size_pt=12
        )
        p_61_body = insert_para_after(
            p_61_hdr,
            None,
            "  • Kết quả đạt được: (1) Kiểm soát tỷ lệ nợ xấu nội bảng giảm thực chất về cuối chu kỳ: tính trên cùng cơ sở dư nợ cho vay hợp nhất, NPL của Agribank giảm từ 1,85% (2023) xuống 1,68% (2024) và 1,30% (2025 – tương ứng 1,17% theo chuẩn TT31 tại BCTN); tỷ lệ nợ nhóm 2 giảm mạnh từ đỉnh 2,44% (2022) về 1,08% (2025), đưa Tỷ lệ nợ có vấn đề (Nhóm 2–5) về mức thấp nhất 6 năm là 2,37%; (2) Xây dựng bộ đệm dự phòng vững chắc và nhất quán: Agribank duy trì tỷ lệ bao phủ nợ xấu (LLCR) hợp nhất luôn trên 113% suốt 6 năm và đạt đỉnh 146,3% năm 2025 (37.465 tỷ dự phòng / 25.610 tỷ nợ xấu), giúp ngân hàng chỉ thiếu hụt +9,8% dự phòng (+3.660 tỷ đồng) khi mô phỏng theo chuẩn IFRS 9; (3) Năng lực thu hồi nợ ngoại bảng tạo dòng tiền thực lớn: lũy kế 2020–2025, Agribank thu hồi được 59.453 tỷ đồng từ các khoản nợ đã xử lý rủi ro trên BCTC hợp nhất (riêng năm 2025 đạt 12.123 tỷ đồng trên BCTC và 16.305 tỷ đồng nếu tính cả thu từ xử lý tài sản tại BCTN).\n"
            "  • Hạn chế tồn tại: (1) Tỷ trọng nợ nhóm 5 (nợ có khả năng mất vốn) quá cao và kéo dài: nợ nhóm 5 luôn chiếm từ 67,0% đến 79,0% tổng nợ xấu nội bảng (năm 2025: 20.220 / 25.610 tỷ đồng), phản ánh tốc độ giải phóng nợ xấu qua phát mại tài sản rất chậm; (2) Gánh nặng chi phí dự phòng bào mòn hiệu quả sinh lời: chi phí dự phòng chiếm tới 42,8%–59,0% lợi nhuận thuần trước dự phòng (PPOP), khiến tỷ suất lợi nhuận trên vốn rủi ro ước tính (RORAC proxy) chỉ đạt 10,8%–16,7% (thấp hơn 15,8–33,8 điểm % so với MB); (3) Bộ đệm an toàn vốn (CAR) mỏng và nhạy cảm cao trước cú sốc: CAR theo Thông tư 41 của Agribank chỉ đạt 9,20%–11,36% (năm 2025: 10,22%) và giảm xuống 8,67% trong kịch bản Stress Test cực đoan 2026.\n"
            "  • Nguyên nhân (Khách quan & Chủ quan): Về khách quan, Agribank thực hiện sứ mệnh chính trị tài trợ 'Tam nông' (chiếm 61,7%–70% dư nợ), thường xuyên đối mặt với rủi ro thiên tai, dịch bệnh (như bão Yagi 2024); 89,0%–91,8% tài sản bảo đảm là đất nông nghiệp, đất ở nông thôn có thanh khoản thấp, lại bị vướng khoảng trống pháp lý khi Nghị quyết 42 hết hiệu lực (01/01/2024–14/10/2025); đồng thời cơ chế tăng vốn điều lệ phụ thuộc vào quy trình phê duyệt ngân sách Nhà nước. Về chủ quan, mạng lưới hơn 2.200 chi nhánh/PGD phân tán rộng làm tăng chi phí vận hành, tốc độ chuyển đổi số và tự động hóa chấm điểm tín dụng theo chuẩn Basel II IRB còn chậm hơn khối NHTMCP.",
            italic=False,
            size_pt=12
        )
        p_62_hdr = insert_para_after(
            p_61_body,
            "6.2. Đánh giá tổng hợp công tác quản trị rủi ro tín dụng tại MB (2020–2025)",
            "",
            italic=False,
            size_pt=12
        )
        insert_para_after(
            p_62_hdr,
            None,
            "  • Kết quả đạt được: (1) Đạt hiệu quả sinh lời điều chỉnh theo rủi ro (RORAC proxy) và khả năng tự tích lũy vốn vượt trội: RORAC proxy của MB đạt 31,6%–49,3% trong suốt giai đoạn 2020–2025, giúp ngân hàng tự bổ sung vốn tự có từ lợi nhuận giữ lại và duy trì hệ số CAR hợp nhất theo Thông tư 41 ổn định ở mức 10,42%–11,80% (ngay cả trong kịch bản Stress Test cực đoan 2026, CAR vẫn đạt 9,73%); (2) Tiên phong hiện đại hóa hạ tầng quản trị rủi ro tập trung: MB vận hành thành công mô hình 3 tuyến phòng vệ độc lập, tách bạch hoàn toàn bộ phận kinh doanh (RM) và phê duyệt tập trung (Hub/Hội sở), ứng dụng nền tảng OFSAA/ICAAP và chấm điểm tín dụng tự động; (3) Năng lực điều chỉnh danh mục linh hoạt sau cú sốc: MB đã chủ động cắt giảm 50,1% quy mô trái phiếu doanh nghiệp TCKT từ đỉnh 46.870 tỷ đồng (2022) về 23.410 tỷ đồng (2025) và giữ NPL riêng lẻ ngân hàng mẹ ở mức thấp (0,68%–1,43%, năm 2025 là 1,12%).\n"
            "  • Hạn chế tồn tại: (1) Chất lượng tài sản biến động mạnh theo chu kỳ vĩ mô và phụ thuộc vào hiệu ứng mẫu số: năm 2023, nợ xấu hợp nhất tăng 94,9% và nợ nhóm 2 tăng 78,2% (đẩy Tỷ lệ nợ có vấn đề lên 3,88%); năm 2025, dù NPL giảm về 1,29% nhờ dư nợ tăng 39,6%, nợ xấu tuyệt đối vẫn tăng 11,5% lên 14.027 tỷ đồng; (2) Sự suy giảm mạnh của bộ đệm bao phủ nợ xấu (LLCR): LLCR hợp nhất của MB giảm từ mức đỉnh 268,0% (2021) và 238,0% (2022) xuống dưới 100% trong hai năm 2024–2025 (92,3% và 93,8%), khiến MB đối mặt với khoảng cách thiếu hụt dự phòng lớn (+14.006 tỷ đồng, tương đương +106,5%) khi mô phỏng theo chuẩn IFRS 9; (3) Rủi ro cao tại phân khúc tài chính tiêu dùng công ty con (MCredit): khối công ty con có tỷ lệ NPL lên tới 6,2%–8,5% (2.509 tỷ đồng nợ xấu cuối năm 2025) và phải xóa nợ tới 4.362 tỷ đồng trong năm 2025.\n"
            "  • Nguyên nhân (Khách quan & Chủ quan): Về khách quan, cú sốc đóng băng thị trường TPDN và bất động sản giai đoạn 2022–2023 cùng quy định phân loại nợ liên đới qua CIC (Thông tư 11/2021) và sự suy giảm thu nhập của nhóm khách hàng vay tiêu dùng sau dịch Covid-19 đã tác động trực diện vào các phân khúc trọng tâm của MB. Về chủ quan, khẩu vị rủi ro theo đuổi mục tiêu tăng trưởng tín dụng cao (CAGR 29,4%/năm) và tối đa hóa ROE đã thúc đẩy MB mở rộng tỷ trọng cho vay BĐS & Xây dựng (tăng từ 10,6% năm 2020 lên 15,4% năm 2025), đầu tư TPDN giai đoạn 2020–2022 và đẩy mạnh cho vay tín chấp tại MCredit, đồng thời lựa chọn chính sách trích lập dự phòng vừa đủ theo quy định VAS trong giai đoạn 2023–2025 để bảo toàn đà tăng trưởng lợi nhuận.",
            italic=False,
            size_pt=12
        )

doc.save(doc_path)
print("Successfully upgraded Word document:", doc_path)
