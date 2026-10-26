# -*- coding: utf-8 -*-
"""
NEU Textbook Generator - Batch 1 (Books 1, 2, 3)
1. Nguyên lý kế toán - GS.TS Đặng Thị Loan
2. Kế toán tài chính 1 - GS.TS Đặng Thị Loan
3. Kế toán tài chính 2 - PGS.TS Nguyễn Phú Giang
"""
import os
import sys
import json
import pymupdf

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

BASE_DIR = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế"

def build_book_1():
    print("--- Đang biên soạn Sách 1: Nguyên lý kế toán ---")
    title = "Nguyên lý Kế toán"
    code = "KTKT1101"
    faculty = "Viện Kế toán - Kiểm toán"
    authors = "GS.TS. Đặng Thị Loan (Chủ biên), PGS.TS. Phạm Đức Hiếu, TS. Nguyễn Thị Hồng Vân"
    
    b = NEUTextbookBuilder(title, code, faculty, authors)
    b.build_cover()
    
    toc = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về Kế toán và Môi trường Kế toán",
         "topics": ["Bản chất và chức năng của kế toán trong nền kinh tế", "Đối tượng kế toán và phương trình kế toán cơ bản", "Các nguyên tắc kế toán thừa nhận chung (GAAP/VAS/IFRS)", "Đạo đức nghề nghiệp kế toán"]},
        {"chapter_num": 2, "chapter_title": "Báo cáo Tài chính của Doanh nghiệp",
         "topics": ["Bảng Cân đối kế toán (Tài sản và Nguồn vốn)", "Báo cáo Kết quả hoạt động kinh doanh", "Báo cáo Lưu chuyển tiền tệ và Thuyết minh BCTC", "Mối liên hệ hữu cơ giữa các báo cáo tài chính"]},
        {"chapter_num": 3, "chapter_title": "Tài khoản và Phương pháp Ghi kép",
         "topics": ["Khái niệm và kết cấu tài khoản kế toán", "Nguyên tắc ghi kép (Double-entry bookkeeping)", "Hệ thống tài khoản kế toán doanh nghiệp Việt Nam", "Quan hệ đối ứng và lập định khoản kế toán"]},
        {"chapter_num": 4, "chapter_title": "Tính giá các Đối tượng Kế toán",
         "topics": ["Nguyên tắc giá gốc (Historical Cost) và Giá trị hợp lý (Fair Value)", "Tính giá tài sản mua vào và tài sản cố định", "Phương pháp tính giá vốn hàng tồn kho xuất kho", "Định giá dự phòng giảm giá tài sản"]},
        {"chapter_num": 5, "chapter_title": "Kế toán các Quá trình Kinh doanh Chủ yếu",
         "topics": ["Kế toán quá trình cung cấp vật tư, nguyên liệu", "Kế toán quá trình sản xuất và tập hợp chi phí", "Kế toán quá trình tiêu thụ sản phẩm và dịch vụ", "Xác định kết quả kinh doanh và phân phối lợi nhuận"]},
        {"chapter_num": 6, "chapter_title": "Sổ Kế toán, Chứng từ và Hình thức Kế toán",
         "topics": ["Hệ thống chứng từ kế toán và quy trình luân chuyển", "Sổ kế toán tổng hợp và sổ kế toán chi tiết", "Các hình thức kế toán tại Việt Nam (Nhật ký chung, Chứng từ ghi sổ)", "Khóa sổ, kiểm tra đối chiếu và lập BCTC cuối kỳ"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chương 1
    intro1 = ("Chương 1 cung cấp nền tảng tri thức khởi đầu về bản chất kế toán như một hệ thống thông tin và ngôn ngữ kinh doanh. "
              "Người học nắm vững các giả định cơ bản (thực thể kinh doanh, hoạt động liên tục, kỳ kế toán, thước đo tiền tệ) "
              "và các nguyên tắc kế toán nền tảng định hình nên cấu trúc của BCTC hiện đại.")
    sec1 = [
        {"sec_num": 1, "sec_title": "Bản chất, Chức năng và Đối tượng Nghiên cứu của Kế toán",
         "content": ("Kế toán là nghệ thuật và khoa học thu nhận, xử lý, kiểm tra, phân tích và cung cấp thông tin kinh tế - tài chính "
                     "dưới hình thức giá trị, hiện vật và thời gian lao động. Trong nền kinh tế thị trường, kế toán giữ vai trò huyết mạch "
                     "giúp các bên liên quan (nhà đầu tư, chủ nợ, cơ quan quản lý thuế, ban điều hành) đưa ra các quyết định phân bổ nguồn lực tối ưu.\n\n"
                     "Đối tượng kế toán bao gồm Tài sản (Tài sản ngắn hạn và Tài sản dài hạn) và Nguồn vốn (Nợ phải trả và Vốn chủ sở hữu), "
                     "cùng sự vận động tuần hoàn của chúng qua các giai đoạn kinh doanh. Sự cân bằng tuyệt đối giữa Tài sản và Nguồn vốn "
                     "là định luật bảo toàn giá trị cốt lõi của kế toán học."),
         "formulas": ["Tổng Tài sản (Total Assets) = Nợ phải trả (Liabilities) + Vốn chủ sở hữu (Equity)",
                      "Δ Tài sản = Δ Nợ phải trả + Δ Vốn góp chủ sở hữu + (Doanh thu - Chi phí) - Cổ tức"],
         "case_studies": [{"title": "Tập đoàn Vingroup (VIC)", "detail": "Phân tích cấu trúc bảng cân đối kế toán khi huy động vốn trái phiếu quốc tế và phát hành cổ phiếu ưu đãi để tài trợ xây dựng tổ hợp sản xuất VinFast."}]},
        {"sec_num": 2, "sec_title": "Hệ Thống Các Giả Định và Nguyên Tắc Kế Toán Cơ Bản",
         "content": ("Khuôn khổ lý thuyết kế toán (Conceptual Framework) dựa trên 4 giả định cơ bản: (1) Thực thể kinh doanh độc lập (Business Entity); "
                     "(2) Hoạt động liên tục (Going Concern); (3) Thước đo tiền tệ ổn định (Monetary Unit); (4) Kỳ kế toán (Periodicity).\n\n"
                     "Cùng với đó là các nguyên tắc thừa nhận chung: Nguyên tắc Cơ sở dồn tích (Accrual Basis) - ghi nhận nghiệp vụ tại thời điểm phát sinh "
                     "chứ không căn cứ vào dòng tiền thực thu/thực chi; Nguyên tắc Phù hợp (Matching Concept) - chi phí phải được ghi nhận tương ứng "
                     "với doanh thu tạo ra trong kỳ; Nguyên tắc Thận trọng (Prudence/Conservatism) - ghi nhận chi phí và tổn thất ngay khi có bằng chứng, "
                     "nhưng chỉ ghi nhận doanh thu khi chắc chắn thu được lợi ích kinh tế."),
         "formulas": ["Lợi nhuận Kế toán (Accrual Profit) = Doanh thu dồn tích - Chi phí tương ứng phù hợp",
                      "Dòng tiền thuần (Operating Cash Flow) = Dòng tiền vào - Dòng tiền ra thực tế"],
         "case_studies": [{"title": "Vietnam Airlines (HVN)", "detail": "Vận dụng nguyên tắc hoạt động liên tục trong bối cảnh âm vốn chủ sở hữu do ảnh hưởng dịch bệnh và các giải pháp tái cơ cấu vốn theo phê duyệt của Quốc hội."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Kế toán Thực chứng (Positive Accounting Theory - Watts & Zimmerman 1986): Giải thích nguyên nhân ban giám đốc lựa chọn các chính sách kế toán khác nhau dựa trên Giả thuyết Kế hoạch Thưởng (Bonus Plan Hypothesis), Giả thuyết Khế ước Nợ (Debt Covenant Hypothesis) và Giả thuyết Chi phí Chính trị (Political Cost Hypothesis).",
            "Sự dịch chuyển mô hình kế toán toàn cầu: Quá trình chuyển dịch từ Kế toán Dựa trên Chi phí Lịch sử (Historical Cost Accounting) sang Kế toán Giá trị Hợp lý (Fair Value Accounting - IFRS 13) và những tranh luận về tính phù hợp (Relevance) so với độ tin cậy (Reliability).",
            "Mô hình nghiên cứu định lượng: Thiết lập mô hình hồi quy Logistic đa biến kiểm định các yếu tố thúc đẩy doanh nghiệp niêm yết tại HOSE/HNX chủ động áp dụng IFRS tự nguyện trước lộ trình bắt buộc của Bộ Tài chính."
        ]
    }
    q1 = [
        "Trình bày phương trình kế toán cơ bản và phân tích ảnh hưởng của 4 dạng biến động kinh tế chủ yếu đến phương trình kế toán.",
        "Phân biệt sự khác nhau căn bản giữa Kế toán dồn tích (Accrual Accounting) và Kế toán tiền mặt (Cash Accounting). Cho ví dụ thực tế.",
        "Tại sao nguyên tắc Thận trọng (Prudence) lại đòi hỏi kế toán phải trích lập dự phòng giảm giá hàng tồn kho và nợ khó đòi?"
    ]
    b.add_chapter(1, "Tổng quan về Kế toán và Môi trường Kế toán", intro1, sec1, phd1, q1)
    
    # Chương 2
    intro2 = ("Chương 2 phân tích chuyên sâu hệ thống báo cáo tài chính doanh nghiệp - sản phẩm đầu ra cốt lõi của chu trình kế toán. "
              "Học viên được trang bị năng lực hiểu và phân tích cấu trúc, nội dung kinh tế và mối liên hệ giữa các báo cáo.")
    sec2 = [
        {"sec_num": 1, "sec_title": "Bảng Cân Đối Kế Toán và Ý Nghĩa Kinh Tế",
         "content": ("Bảng cân đối kế toán là báo cáo tài chính thời điểm, phản ánh tổng hợp toàn bộ giá trị tài sản hiện có và nguồn hình thành tài sản "
                     "của doanh nghiệp tại một thời điểm nhất định (thường là cuối quý hoặc cuối năm tài chính).\n\n"
                     "Tài sản được sắp xếp theo tính thanh khoản giảm dần (từ tiền mặt, các khoản phải thu, hàng tồn kho đến TSCĐ). "
                     "Nguồn vốn được phân chia thành Nợ phải trả (nghĩa vụ tài chính với chủ nợ theo thời hạn thanh toán) "
                     "và Vốn chủ sở hữu (nguồn vốn vĩnh viễn thuộc sở hữu của cổ đông, bao gồm vốn đầu tư ban đầu, thặng dư vốn và lợi nhuận giữ lại)."),
         "formulas": ["Vốn lưu động ròng (Net Working Capital) = Tài sản ngắn hạn - Nợ ngắn hạn",
                      "Tỷ số Nợ trên Vốn chủ sở hữu (D/E) = Tổng nợ phải trả / Vốn chủ sở hữu"],
         "case_studies": [{"title": "Công ty Cổ phần Sữa Việt Nam (Vinamilk - VNM)", "detail": "Đánh giá cấu trúc an toàn tài chính với tỷ lệ tiền mặt cao, tỷ lệ nợ vay thấp và chính sách chi trả cổ tức tiền mặt đều đặn."}]},
        {"sec_num": 2, "sec_title": "Báo Cáo Kết Quả Kinh Doanh và Báo Cáo Lưu Chuyển Tiền Tệ",
         "content": ("Báo cáo kết quả hoạt động kinh doanh là báo cáo thời kỳ, phản ánh hiệu quả kinh doanh qua các chỉ tiêu: "
                     "Doanh thu thuần, Giá vốn hàng bán, Lợi nhuận gộp, Chi phí hoạt động (bán hàng, quản lý), Lợi nhuận từ hoạt động kinh doanh, "
                     "Chi phí tài chính và Lợi nhuận sau thuế.\n\n"
                     "Báo cáo lưu chuyển tiền tệ (theo phương pháp trực tiếp hoặc gián tiếp) phân tách dòng tiền theo 3 hoạt động căn bản: "
                     "Hoạt động kinh doanh (CFO), Hoạt động đầu tư (CFI) và Hoạt động tài chính (CFF). Dòng tiền là thước đo sinh tồn thực tế "
                     "chứng minh doanh nghiệp có tạo ra tiền mặt để trả nợ và tái đầu tư hay chỉ có lợi nhuận trên giấy tờ dồn tích."),
         "formulas": ["Lợi nhuận gộp = Doanh thu thuần - Giá vốn hàng bán (COGS)",
                      "Lưu chuyển tiền thuần trong kỳ = CFO + CFI + CFF",
                      "Dòng tiền tự do (Free Cash Flow) = CFO - Chi tiêu mua sắm TSCĐ (CAPEX)"],
         "case_studies": [{"title": "Tập đoàn Hòa Phát (HPG)", "detail": "Phân tích biến động CFO và CAPEX trong giai đoạn đầu tư mở rộng Khu liên hợp Gang thép Dung Quất 1 và 2."}]}
    ]
    phd2 = {
        "topics": [
            "Hàm lượng thông tin của BCTC (Value Relevance of Financial Statements - Ohlson 1995 Model): Mối quan hệ tương quan giữa Giá trị sổ sách của Vốn chủ sở hữu (BVPS), Thu nhập trên mỗi cổ phần (EPS) và Giá trị thị trường cổ phiếu trên TTCK Việt Nam.",
            "Lý thuyết Bất cân xứng thông tin (Information Asymmetry) và Tín hiệu kế toán (Signaling Theory): Vai trò của BCTC được kiểm toán bởi Big 4 trong việc giảm chi phí vốn chủ sở hữu (Cost of Equity Capital) và chi phí nợ vay (Cost of Debt).",
            "Chuyên đề Tiến sĩ: Ứng dụng hồi quy Fama-MacBeth đánh giá sự bất thường của các khoản dồn tích (Accrual Anomaly - Sloan 1996) tại thị trường các quốc gia Đông Nam Á."
        ]
    }
    q2 = [
        "Tại sao doanh nghiệp có lợi nhuận kế toán cao trên Báo cáo kết quả kinh doanh vẫn có thể rơi vào tình trạng mất khả năng thanh toán và phá sản?",
        "So sánh cấu trúc và cách tiếp cận lập Báo cáo lưu chuyển tiền tệ theo phương pháp trực tiếp và phương pháp gián tiếp.",
        "Phân tích mối quan hệ hữu cơ kết nối giữa Bảng Cân đối kế toán đầu kỳ, Báo cáo kết quả kinh doanh trong kỳ và Bảng Cân đối kế toán cuối kỳ."
    ]
    b.add_chapter(2, "Báo cáo Tài chính của Doanh nghiệp", intro2, sec2, phd2, q2)
    
    # Chương 3
    intro3 = ("Chương 3 đi sâu vào kỹ thuật nghiệp vụ nền tảng: Tài khoản kế toán và phương pháp ghi sổ kép. "
              "Đây là công cụ phân loại, hệ thống hóa và phản ánh liên tục mọi biến động của tài sản và nguồn vốn.")
    sec3 = [
        {"sec_num": 1, "sec_title": "Tài Khoản Kế Toán và Kết Cấu Tài Khoản",
         "content": ("Tài khoản kế toán là phương pháp phân loại và theo dõi một cách thường xuyên, liên tục, có hệ thống tình hình tăng, giảm "
                     "của từng đối tượng kế toán cụ thể. Về mặt hình thức, tài khoản có dạng chữ T chia làm hai bên: Bên Nợ (Debit) và Bên Có (Credit).\n\n"
                     "Kết cấu tài khoản phản ánh tính chất hai mặt đối lập của phương trình kế toán: "
                     "Tài khoản Tài sản và Chi phí có số dư Nợ (Tăng ghi Nợ, Giảm ghi Có); "
                     "Tài khoản Nguồn vốn, Nợ phải trả và Doanh thu có số dư Có (Tăng ghi Có, Giảm ghi Nợ). "
                     "Các tài khoản doanh thu và chi phí là tài khoản tạm thời, không có số dư cuối kỳ do được kết chuyển xác định kết quả kinh doanh."),
         "formulas": ["Số dư cuối kỳ (TK Tài sản) = Số dư đầu kỳ + Phát sinh Nợ (Tăng) - Phát sinh Có (Giảm)",
                      "Số dư cuối kỳ (TK Nguồn vốn) = Số dư đầu kỳ + Phát sinh Có (Tăng) - Phát sinh Nợ (Giảm)"],
         "case_studies": [{"title": "Ngân hàng TMCP Ngoại thương Việt Nam (Vietcombank - VCB)", "detail": "Tổ chức hệ thống tài khoản chi tiết phản ánh các khoản tiền gửi thanh toán, tiết kiệm và cho vay khách hàng theo quy định của NHNN."}]},
        {"sec_num": 2, "sec_title": "Nguyên Tắc Ghi Kép và Quan Hệ Đối Ứng Tài Khoản",
         "content": ("Ghi kép là phương pháp phản ánh mỗi nghiệp vụ kinh tế tài chính phát sinh vào ít nhất hai tài khoản kế toán có liên quan "
                     "theo quan hệ đối ứng, trong đó số tiền ghi vào bên Nợ của các tài khoản phải bằng số tiền ghi vào bên Có của các tài khoản tương ứng.\n\n"
                     "Có 4 quan hệ đối ứng cơ bản: (1) Tài sản tăng - Tài sản giảm; (2) Nguồn vốn tăng - Nguồn vốn giảm; "
                     "(3) Tài sản tăng - Nguồn vốn tăng; (4) Tài sản giảm - Nguồn vốn giảm. "
                     "Bảng cân đối tài khoản (Trial Balance) tổng hợp số phát sinh Nợ/Có và số dư Nợ/Có toàn hệ thống để kiểm tra tính cân đối toán học "
                     "trước khi lập báo cáo tài chính."),
         "formulas": ["Tổng phát sinh Nợ toàn bộ tài khoản = Tổng phát sinh Có toàn bộ tài khoản",
                      "Tổng số dư Nợ cuối kỳ = Tổng số dư Có cuối kỳ"],
         "case_studies": [{"title": "Doanh nghiệp Mua Nguyên Vật Liệu", "detail": "Nghiệp vụ mua NVL 100 triệu chưa trả tiền người bán: Nợ TK 152 (100 tr) / Có TK 331 (100 tr) - tác động làm tăng cả Tài sản và Nợ phải trả cùng một lượng 100 triệu đồng."}]}
    ]
    phd3 = {
        "topics": [
            "Lịch sử phát triển và triết lý của Hệ thống Kế toán Kép (Luca Pacioli 1494): Bản chất đại số tuyến tính của ma trận giao dịch kế toán (Ijiri Axiomatic Foundations of Accounting Measurement).",
            "Kế toán sổ cái ba bên (Triple-Entry Accounting) trên nền tảng Blockchain: Đột phá công nghệ mật mã học loại bỏ rủi ro giả mạo chứng từ kế toán và cơ chế đối chiếu tự động phân tán (Smart Contracts).",
            "Mô hình nghiên cứu: Đánh giá tác động của quá trình chuyển đổi số hệ thống ERP (SAP S/4HANA, Oracle Cloud) đến chất lượng kiểm soát nội bộ và độ trễ công bố BCTC của các doanh nghiệp nhà nước cổ phần hóa."
        ]
    }
    q3 = [
        "Phân tích bản chất kinh tế và cơ sở toán học của quy tắc: 'Tổng số tiền ghi Nợ luôn luôn bằng Tổng số tiền ghi Có'.",
        "Nếu kế toán hạch toán nhầm một nghiệp vụ mua hàng sang sai tài khoản đối ứng cùng loại thì Bảng cân đối tài khoản có phát hiện được lỗi này không? Giải thích.",
        "Trình bày quy trình từ chứng từ kế toán gốc đến lập định khoản, vào sổ cái và lập Bảng cân đối thử."
    ]
    b.add_chapter(3, "Tài khoản và Phương pháp Ghi kép", intro3, sec3, phd3, q3)
    
    # Chương 4
    intro4 = ("Chương 4 cung cấp lý thuyết định giá và đo lường tài sản trong kế toán. "
              "Học viên nắm vững nguyên tắc giá gốc, các phương pháp xuất kho hàng tồn kho và xu thế định giá theo giá trị hợp lý.")
    sec4 = [
        {"sec_num": 1, "sec_title": "Nguyên Tắc Giá Gốc và Giá Trị Hợp Lý",
         "content": ("Giá gốc (Historical Cost) là toàn bộ các chi phí thực tế mà doanh nghiệp đã bỏ ra để có được tài sản ở trạng thái sẵn sàng sử dụng. "
                     "Giá gốc đảm bảo tính khách quan và có thể kiểm chứng được qua hóa đơn, chứng từ pháp lý.\n\n"
                     "Tuy nhiên, trong môi trường lạm phát hoặc biến động thị trường nhanh, giá gốc có thể làm sai lệch giá trị tài sản trên sổ sách. "
                     "Chuẩn mực BCTC quốc tế IFRS 13 định nghĩa Giá trị hợp lý (Fair Value) là giá có thể nhận được khi bán một tài sản "
                     "hoặc chuyển giao một khoản nợ phải trả trong một giao dịch tự nguyện giữa các bên tham gia thị trường tại ngày đo lường."),
         "formulas": ["Giá gốc TSCĐ mua ngoài = Giá mua trên hóa đơn (trừ chiết khấu) + Thuế không hoàn lại + Chi phí vận chuyển, lắp đặt, chạy thử",
                      "Cấp độ định giá IFRS 13: Cấp độ 1 (Giá niêm yết) -> Cấp độ 2 (Đầu vào quan sát được) -> Cấp độ 3 (Mô hình chiết khấu DCF)"],
         "case_studies": [{"title": "Tập đoàn Điện lực Việt Nam (EVN)", "detail": "Vấn đề đánh giá lại tài sản cố định nguồn điện và lưới điện truyền tải khi thực hiện cổ phần hóa các tổng công ty phát điện (GENCO)."}]},
        {"sec_num": 2, "sec_title": "Phương Pháp Tính Giá Hàng Tồn Kho Xuất Kho",
         "content": ("Khi xuất kho hàng hóa hoặc nguyên vật liệu phục vụ sản xuất, doanh nghiệp áp dụng một trong các phương pháp tính giá vốn sau:\n"
                     "(1) Phương pháp Nhập trước - Xuất trước (FIFO - First-In, First-Out): Giả định lô hàng nào nhập trước sẽ xuất trước, "
                     "hàng tồn kho cuối kỳ phản ánh mức giá nhập gần nhất. Trong thời kỳ lạm phát, FIFO tạo ra giá vốn thấp và lợi nhuận kế toán cao hơn.\n"
                     "(2) Phương pháp Bình quân gia quyền (Weighted Average Cost): Tính đơn giá bình quân sau mỗi lần nhập hoặc bình quân cả kỳ dự trữ.\n"
                     "(3) Phương pháp Thực tế đích danh (Specific Identification): Áp dụng cho các mặt hàng có giá trị cao, tính chất đơn chiếc như bất động sản, xe hơi, máy móc đặc chủng.\n"
                     "Lưu ý: Chuẩn mực kế toán Việt Nam (VAS 02) và IFRS (IAS 2) đều đã bãi bỏ hoàn toàn phương pháp LIFO (Nhập sau - Xuất trước)."),
         "formulas": ["Đơn giá BQ gia quyền cả kỳ = (Giá trị tồn đầu kỳ + Giá trị nhập trong kỳ) / (Số lượng tồn đầu kỳ + Số lượng nhập trong kỳ)",
                      "Giá trị thuần có thể thực hiện được (NRV) = Giá bán ước tính - Chi phí ước tính để hoàn thành và bán hàng"],
         "case_studies": [{"title": "Công ty Cổ phần Tập đoàn Masan (MSN)", "detail": "Ứng dụng phương pháp bình quân gia quyền di động trong quản trị hàng tồn kho chuỗi cung ứng hàng tiêu dùng nhanh (FMCG)."}]}
    ]
    phd4 = {
        "topics": [
            "Lý thuyết Đo lường Kế toán (Measurement Theory in Accounting): Tranh biện giữa Mô hình Chi phí Lịch sử Điều chỉnh Lạm phát (General Price Level Adjusted) và Kế toán Chi phí Hiện hành (Current Cost Accounting).",
            "Mức độ tin cậy của Giá trị Hợp lý Cấp độ 3 (Fair Value Level 3 Under IFRS 13): Sự phụ thuộc vào các giả định chủ quan của ban quản trị và nguy cơ quản trị lợi nhuận (Earnings Management) trong định giá bất động sản đầu tư và công cụ tài chính phái sinh phức tạp.",
            "Nghiên cứu thực nghiệm: Kiểm định phản ứng của thị trường chứng khoán đối với việc công bố lỗ tổn thất tài sản (Impairment Loss of Assets - IAS 36) tại các thị trường tài chính mới nổi."
        ]
    }
    q4 = [
        "Phân tích ưu nhược điểm của phương pháp FIFO trong bối cảnh giá cả nguyên vật liệu trên thị trường thế giới biến động tăng liên tục.",
        "Tại sao chuẩn mực IFRS và VAS lại cấm áp dụng phương pháp LIFO (Nhập sau - Xuất trước)?",
        "Trình bày nguyên tắc ghi nhận dự phòng giảm giá hàng tồn kho theo giá trị thuần có thể thực hiện được (NRV)."
    ]
    b.add_chapter(4, "Tính giá các Đối tượng Kế toán", intro4, sec4, phd4, q4)
    
    # Chương 5
    intro5 = ("Chương 5 hệ thống hóa kế toán chu kỳ kinh doanh chủ yếu của doanh nghiệp: Quá trình mua sắm cung ứng, "
              "quá trình tổ chức sản xuất tạo ra sản phẩm và quá trình bán hàng, xác định kết quả kinh doanh.")
    sec5 = [
        {"sec_num": 1, "sec_title": "Kế Toán Quá Trình Cung Ứng và Sản Xuất",
         "content": ("Quá trình cung cấp phản ánh việc mua nguyên vật liệu, công cụ dụng cụ và dịch vụ đầu vào. Kế toán theo dõi giá mua, "
                     "chi phí thu mua và thuế GTGT đầu vào được khấu trừ.\n\n"
                     "Quá trình sản xuất tập hợp 3 yếu tố chi phí cơ bản: Chi phí nguyên vật liệu trực tiếp (TK 621), "
                     "Chi phí nhân công trực tiếp (TK 622) và Chi phí sản xuất chung (TK 627). "
                     "Cuối kỳ, kế toán kết chuyển toàn bộ chi phí sản xuất vào TK 154 (Chi phí SXKD dở dang), "
                     "đánh giá sản phẩm dở dang cuối kỳ và tính tổng giá thành cũng như giá thành đơn vị sản phẩm hoàn thành nhập kho (TK 155)."),
         "formulas": ["Tổng giá thành sản phẩm = Chi phí SX dở dang đầu kỳ + Chi phí phát sinh trong kỳ (621 + 622 + 627) - Chi phí SX dở dang cuối kỳ",
                      "Giá thành đơn vị = Tổng giá thành sản phẩm hoàn thành / Số lượng sản phẩm hoàn thành"],
         "case_studies": [{"title": "Tổng Công ty May 10 (May 10)", "detail": "Quy trình hạch toán chi phí vải, phụ liệu may và chi phí nhân công theo từng đơn hàng gia công xuất khẩu."}]},
        {"sec_num": 2, "sec_title": "Kế Toán Quá Trình Tiêu Thụ và Xác Định Kết Quả Kinh Doanh",
         "content": ("Tiêu thụ là khâu cuối cùng chuyển đổi sản phẩm, hàng hóa thành tiền tệ hoặc quyền đòi tiền. Kế toán ghi nhận hai mặt của nghiệp vụ:\n"
                     "- Phản ánh giá vốn hàng bán: Nợ TK 632 / Có TK 155, 156.\n"
                     "- Phản ánh doanh thu bán hàng và cung cấp dịch vụ: Nợ TK 111, 112, 131 / Có TK 511, Có TK 3331.\n\n"
                     "Cuối kỳ kế toán, toàn bộ doanh thu, thu nhập và chi phí được kết chuyển vào Tài khoản 911 (Xác định kết quả kinh doanh). "
                     "Kết quả lãi hoặc lỗ ròng được chuyển tiếp sang Tài khoản 421 (Lợi nhuận sau thuế chưa phân phối) sau khi trừ chi phí thuế TNDN (TK 821)."),
         "formulas": ["Doanh thu thuần = Doanh thu bán hàng - Các khoản giảm trừ doanh thu (Chiết khấu thương mại, Giảm giá hàng bán, Hàng bán bị trả lại)",
                      "Lợi nhuận trước thuế = Doanh thu thuần - Giá vốn hàng bán - Chi phí bán hàng - Chi phí QLDN + Doanh thu tài chính - Chi phí tài chính + Lợi nhuận khác",
                      "Lợi nhuận sau thuế = Lợi nhuận trước thuế - Chi phí thuế TNDN hiện hành và hoãn lại"],
         "case_studies": [{"title": "Công ty Cổ phần Bán lẻ Kỹ thuật số FPT (FPT Retail - FRT)", "detail": "Hạch toán doanh thu và chiết khấu thương mại cho chuỗi nhà thuốc Long Châu và chuỗi bán lẻ FPT Shop."}]}
    ]
    phd5 = {
        "topics": [
            "Lý thuyết Quản trị Chi phí Dựa trên Hoạt động (Activity-Based Costing - ABC Theory): Phân bổ chi phí sản xuất chung gián tiếp trong các doanh nghiệp sản xuất tích hợp công nghệ cao và tự động hóa.",
            "Nhận diện doanh thu theo IFRS 15 (Revenue from Contracts with Customers): Mô hình 5 bước ghi nhận doanh thu và những thách thức khi áp dụng cho các hợp đồng xây dựng, viễn thông và dịch vụ phần mềm đa hợp phần tại Việt Nam.",
            "Nghiên cứu hành vi: Phân tích động cơ phân bổ chi phí và làm mượt lợi nhuận (Income Smoothing) của các CEO tại các doanh nghiệp niêm yết trước thời điểm phát hành thêm cổ phiếu ra công chúng (SEO)."
        ]
    }
    q5 = [
        "Trình bày quy trình tập hợp chi phí và các bước tính giá thành sản phẩm công nghiệp trong phương pháp kê khai thường xuyên.",
        "Phân biệt chi phí sản phẩm (Product Costs) và chi phí thời kỳ (Period Costs). Tại sao chi phí bán hàng và chi phí quản lý doanh nghiệp không được tính vào giá thành sản phẩm?",
        "Viết các bút toán kết chuyển doanh thu, chi phí để xác định kết quả kinh doanh vào ngày cuối năm tài chính."
    ]
    b.add_chapter(5, "Kế toán các Quá trình Kinh doanh Chủ yếu", intro5, sec5, phd5, q5)
    
    # Chương 6
    intro6 = ("Chương 6 hoàn thiện quy trình thực hành kế toán qua hệ thống chứng từ, sổ kế toán và các hình thức tổ chức kế toán. "
              "Đây là cầu nối giữa lý luận kế toán và công việc thực hành kiểm soát nội bộ tại doanh nghiệp.")
    sec6 = [
        {"sec_num": 1, "sec_title": "Chứng Từ Kế Toán và Quy Trình Luân Chuyển",
         "content": ("Chứng từ kế toán là những giấy tờ và vật mang tin phản ánh nghiệp vụ kinh tế, tài chính phát sinh và đã hoàn thành, "
                     "làm căn cứ ghi sổ kế toán. Luật Kế toán Việt Nam quy định nghiêm ngặt về nội dung chứng từ: Tên gọi, số hiệu, ngày lập, "
                     "tên địa chỉ các bên, nội dung tóm tắt nghiệp vụ, số lượng, đơn giá, số tiền và chữ ký của những người có trách nhiệm.\n\n"
                     "Hiện nay, việc áp dụng hóa đơn điện tử và chứng từ điện tử theo Nghị định 123/2020/NĐ-CP đã chuyển đổi toàn bộ quy trình "
                     "luân chuyển từ chứng từ giấy sang dữ liệu số hóa có chữ ký số xác thực của Tổng cục Thuế."),
         "formulas": ["Trình tự luân chuyển chứng từ: Lập/Tiếp nhận chứng từ -> Kiểm tra tính hợp pháp, hợp lệ -> Ghi sổ kế toán -> Lưu trữ, bảo quản theo luật (tối thiểu 10 năm)"],
         "case_studies": [{"title": "Triển khai Hóa Đơn Điện Tử Khởi Tạo Từ Máy Tính Tiền", "detail": "Kinh nghiệm thực tiễn áp dụng tại các chuỗi bán lẻ WinCommerce và Thế Giới Di Động nhằm đảm bảo tính minh bạch dữ liệu thuế."}]},
        {"sec_num": 2, "sec_title": "Các Hình Thức Kế Toán và Quy Trình Lập Báo Cáo Tài Chính",
         "content": ("Hình thức kế toán là hệ thống các loại sổ kế toán có mối quan hệ liên kết với nhau theo một trình tự và phương pháp ghi chép nhất định.\n"
                     "Việt Nam quy định 4 hình thức kế toán chính:\n"
                     "(1) Hình thức Nhật ký chung: Tất cả các nghiệp vụ được ghi vào sổ Nhật ký chung theo trình tự thời gian, sau đó vào Sổ cái.\n"
                     "(2) Hình thức Nhật ký - Sổ cái: Kết hợp ghi chép theo thời gian và theo hệ thống trên cùng một quyển sổ.\n"
                     "(3) Hình thức Chứng từ ghi sổ: Căn cứ vào chứng từ gốc lập Chứng từ ghi sổ trước khi vào Sổ Đăng ký và Sổ cái.\n"
                     "(4) Hình thức Kế toán trên máy vi tính: Phổ biến nhất hiện nay với các phần mềm kế toán (MISA, FAST, Bravo, SAP). "
                     "Quy trình cuối kỳ gồm: Kiểm kê tài sản, đối chiếu công nợ, trích lập dự phòng, khóa sổ các tài khoản và trích xuất BCTC."),
         "formulas": ["Bảng đối chiếu số phát sinh: Tổng phát sinh Nợ = Tổng phát sinh Có; Tổng dư Nợ = Tổng dư Có",
                      "Phương trình kiểm toán: Số dư đầu kỳ + Phát sinh Tăng - Phát sinh Giảm = Số dư cuối kỳ"],
         "case_studies": [{"title": "Chuyển Đổi Hệ Thống Kế Toán Sang ERP SAP", "detail": "Bài học từ Tập đoàn Dầu khí Quốc gia Việt Nam (PVN) trong chuẩn hóa danh mục tài khoản và đồng bộ quy trình lập báo cáo hợp nhất."}]}
    ]
    phd6 = {
        "topics": [
            "Tác động của Trí tuệ Nhân tạo (AI) và Học máy (Machine Learning) đối với Tự động hóa Kế toán (Robotic Process Automation - RPA): Sự dịch chuyển vai trò của kế toán viên từ ghi chép nghiệp vụ sang phân tích dữ liệu chiến lược.",
            "Lý thuyết Thể chế (Institutional Theory) và Sự thích ứng của Hệ thống Thông tin Kế toán Doanh nghiệp Nhà nước Việt Nam trong bối cảnh toàn cầu hóa và minh bạch thông tin thị trường vốn.",
            "Chuyên đề Tiến sĩ: Phân tích tác động của gian lận chứng từ kế toán và các hành vi vi phạm chuẩn mực báo cáo tài chính đến rủi ro sụp đổ giá cổ phiếu (Stock Price Crash Risk) tại thị trường Việt Nam."
        ]
    }
    q6 = [
        "Trình bày các yếu tố bắt buộc phải có trên một chứng từ kế toán hợp pháp theo quy định của Luật Kế toán 2015.",
        "So sánh ưu nhược điểm và điều kiện áp dụng của Hình thức Nhật ký chung so với Hình thức Chứng từ ghi sổ.",
        "Mô tả quy trình các công việc kế toán cần thực hiện vào thời điểm cuối niên độ tài chính trước khi khóa sổ và phát hành BCTC."
    ]
    b.add_chapter(6, "Sổ Kế toán, Chứng từ và Hình thức Kế toán", intro6, sec6, phd6, q6)
    
    out_dir = os.path.join(BASE_DIR, r"02_Kế toán & Kiểm toán\[NEU] Nguyên lý kế toán - GS.TS Đặng Thị Loan (NXB ĐHKTQD)")
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Nguyên lý kế toán - GS.TS Đặng Thị Loan (NXB ĐHKTQD).pdf")
    pages, size_mb = b.save(out_pdf)
    print(f"-> Hoàn thành Sách 1: {pages} trang, {size_mb:.2f} MB. Lưu tại: {out_pdf}")
    return {"book": "Nguyên lý kế toán", "pages": pages, "size_mb": size_mb, "path": out_pdf}


def build_book_2():
    print("--- Đang biên soạn Sách 2: Kế toán tài chính 1 ---")
    title = "Kế toán Tài chính 1"
    code = "KTKT1102"
    faculty = "Viện Kế toán - Kiểm toán"
    authors = "GS.TS. Đặng Thị Loan (Chủ biên), PGS.TS. Trần Văn Thuận, TS. Đinh Thế Hùng"
    
    b = NEUTextbookBuilder(title, code, faculty, authors)
    b.build_cover()
    
    toc = [
        {"chapter_num": 1, "chapter_title": "Kế toán Tiền và các Khoản Phải thu",
         "topics": ["Kế toán tiền mặt, tiền gửi ngân hàng và tiền đang chuyển", "Kế toán các khoản phải thu thương mại và phải thu khác", "Trích lập dự phòng nợ phải thu khó đòi (VAS 18 vs IFRS 9 ECL)", "Kế toán các nghiệp vụ hối đoái ngoại tệ (VAS 10 / IAS 21)"]},
        {"chapter_num": 2, "chapter_title": "Kế toán Hàng tồn kho",
         "topics": ["Nguyên tắc xác định giá gốc hàng tồn kho theo VAS 02 và IAS 2", "Kế toán xuất kho theo phương pháp KKTX và KKĐK", "Kế toán giá vốn hàng bán và trích lập dự phòng giảm giá HTK (NRV)", "Kiểm kê hàng tồn kho và xử lý hao hụt thừa thiếu"]},
        {"chapter_num": 3, "chapter_title": "Kế toán Tài sản cố định và Bất động sản đầu tư",
         "topics": ["Tiêu chuẩn ghi nhận TSCĐ hữu hình, vô hình (VAS 03, 04 / IAS 16, 38)", "Phương pháp tính và trích khấu hao tài sản cố định", "Kế toán sửa chữa lớn, nâng cấp, nhượng bán và thanh lý TSCĐ", "Kế toán Bất động sản đầu tư theo VAS 05 và IAS 40"]},
        {"chapter_num": 4, "chapter_title": "Kế toán Tiền lương và các Khoản Trích theo lương",
         "topics": ["Các hình thức trả lương và quỹ tiền lương doanh nghiệp", "Kế toán trích lập và nộp BHXH, BHYT, BHTN, KPCĐ theo luật định", "Kế toán các khoản phúc lợi và chi phí người lao động theo IAS 19", "Quyết toán quỹ lương và thuế TNCN gắn với tiền lương"]},
        {"chapter_num": 5, "chapter_title": "Kế toán Nợ phải trả và Nguồn vốn Chủ sở hữu",
         "topics": ["Kế toán nợ phải trả người bán và các khoản vay tài chính (VAS 06 / IFRS 16)", "Kế toán chi phí đi vay vốn hóa và ghi nhận chi phí (VAS 16 / IAS 23)", "Kế toán phát hành cổ phiếu, thặng dư vốn và các quỹ doanh nghiệp", "Kế toán lợi nhuận sau thuế chưa phân phối và chi trả cổ tức"]},
        {"chapter_num": 6, "chapter_title": "Báo cáo Tài chính Doanh nghiệp (Phần 1)",
         "topics": ["Kỹ thuật lập và trình bày Bảng Cân đối kế toán theo TT 200/2014/TT-BTC", "Kỹ thuật lập Báo cáo Kết quả hoạt động kinh doanh chuẩn mực", "Phương pháp lập Báo cáo Lưu chuyển tiền tệ (Trực tiếp & Gián tiếp)", "Bản Thuyết minh BCTC và công bố thông tin theo chuẩn mực quốc tế"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chương 1
    intro1 = ("Chương 1 trang bị kiến thức chuyên sâu về hạch toán tiền và các khoản phải thu - nhóm tài sản có tính thanh khoản cao nhất. "
              "Trọng tâm đi sâu vào quản trị rủi ro thanh khoản, dự phòng tín dụng dự kiến theo IFRS 9 và chênh lệch tỷ giá hối đoái.")
    sec1 = [
        {"sec_num": 1, "sec_title": "Kế Toán Tiền và các Nghiệp Vụ Ngoại Tệ",
         "content": ("Tiền của doanh nghiệp bao gồm tiền mặt tại quỹ (TK 111), tiền gửi ngân hàng không kỳ hạn (TK 112) và tiền đang chuyển (TK 113), "
                     "được phân loại theo tiền Việt Nam, ngoại tệ và vàng tiền tệ.\n\n"
                     "Khi phát sinh giao dịch bằng ngoại tệ, kế toán quy đổi ra đồng Việt Nam theo tỷ giá giao dịch thực tế tại thời điểm phát sinh. "
                     "Cuối kỳ kế toán, toàn bộ số dư các khoản mục tiền tệ có gốc ngoại tệ phải được đánh giá lại theo tỷ giá chuyển khoản "
                     "của ngân hàng thương mại nơi doanh nghiệp thường xuyên có giao dịch. "
                     "Chênh lệch tỷ giá hối đoái đánh giá lại được ghi nhận vào doanh thu hoạt động tài chính (TK 515) hoặc chi phí tài chính (TK 635)."),
         "formulas": ["Chênh lệch tỷ giá cuối kỳ = Số dư ngoại tệ x (Tỷ giá đánh giá lại cuối kỳ - Tỷ giá ghi sổ thực tế)",
                      "Bút toán lãi tỷ giá: Nợ TK 1112, 1122, 131 / Có TK 515",
                      "Bút toán lỗ tỷ giá: Nợ TK 635 / Có TK 1112, 1122, 331"],
         "case_studies": [{"title": "Vietnam Airlines (HVN) và Dư nợ Ngoại tệ USD/EUR", "detail": "Ảnh hưởng của biến động tỷ giá USD/VND đến kết quả kinh doanh và chi phí tài chính khi doanh nghiệp có dư nợ vay thuê mua máy bay quy mô hàng tỷ USD."}]},
        {"sec_num": 2, "sec_title": "Kế Toán Nợ Phải Thu Khách Hàng và Dự Phòng Nợ Khó Đòi",
         "content": ("Nợ phải thu khách hàng (TK 131) phản ánh quyền đòi tiền của doanh nghiệp phát sinh từ việc bán hàng hóa, cung cấp dịch vụ đã hoàn thành. "
                     "Kế toán phải theo dõi chi tiết từng khách hàng, từng hóa đơn và thời hạn thanh toán để kiểm soát rủi ro tín dụng thương mại.\n\n"
                     "Theo Thông tư 48/2019/TT-BTC, mức trích lập dự phòng nợ phải thu quá hạn: Từ 6 tháng đến dưới 1 năm trích 30%; từ 1 đến dưới 2 năm trích 50%; "
                     "từ 2 đến dưới 3 năm trích 70%; từ 3 năm trở lên trích 100%. "
                     "Bút toán trích lập: Nợ TK 642 (Chi phí QLDN) / Có TK 2293 (Dự phòng nợ phải thu khó đòi). "
                     "Nếu số dự phòng phải trích lập cuối kỳ nhỏ hơn số dư hiện có, kế toán hoàn nhập: Nợ TK 2293 / Có TK 642."),
         "formulas": ["Mô hình tổn thất tín dụng dự kiến (ECL under IFRS 9): ECL = EAD x PD x LGD",
                      "Trong đó: EAD (Dư nợ tại thời điểm vỡ nợ), PD (Xác suất vỡ nợ), LGD (Tỷ lệ tổn thất khi vỡ nợ)"],
         "case_studies": [{"title": "Công ty Cổ phần Nông nghiệp Quốc tế Hoàng Anh Gia Lai (HNG)", "detail": "Phân tích trích lập dự phòng nợ phải thu khó đòi đối với các khoản cho vay và phải thu từ các bên liên quan."}]}
    ]
    phd1 = {
        "topics": [
            "Mô hình Tổn thất Tín dụng Dự kiến (Expected Credit Loss - IFRS 9) so với Mô hình Tổn thất Đã phát sinh (Incurred Loss Model - VAS 18): Sự dịch chuyển tư duy kế toán từ bị động sang chủ động đo lường rủi ro hệ thống.",
            "Quản trị Lợi nhuận qua Dự phòng Nợ Phải thu Khó đòi (Earnings Management via Bad Debt Allowance - Healy 1985, McNichols & Wilson 1988): Kiểm định hành vi làm mượt lợi nhuận hoặc 'tắm sạch báo cáo' (Big Bath) tại các ngân hàng thương mại Việt Nam.",
            "Tác động của biến động tỷ giá hối đoái vĩ mô đối với chất lượng công bố thông tin tài chính của các doanh nghiệp định hướng xuất nhập khẩu."
        ]
    }
    q1 = [
        "Phân tích nguyên tắc xác định và xử lý chênh lệch tỷ giá hối đoái phát sinh trong kỳ so với chênh lệch tỷ giá do đánh giá lại số dư cuối kỳ theo VAS 10.",
        "So sánh cơ chế trích lập dự phòng nợ phải thu khó đòi theo Thông tư 48/2019/TT-BTC của Việt Nam với chuẩn mực quốc tế IFRS 9.",
        "Trình bày phương pháp hạch toán nghiệp vụ xử lý xóa nợ đối với khoản nợ khó đòi không thể thu hồi được và khi bất ngờ thu hồi được khoản nợ đã xóa."
    ]
    b.add_chapter(1, "Kế toán Tiền và các Khoản Phải thu", intro1, sec1, phd1, q1)
    
    # Chương 2
    intro2 = ("Chương 2 đi sâu vào kế toán hàng tồn kho - khoản mục chiếm tỷ trọng lớn trong tổng tài sản lưu động của doanh nghiệp sản xuất và thương mại. "
              "Nội dung bao gồm hạch toán giá gốc, hạch toán nhập xuất kho và dự phòng giảm giá hàng tồn kho theo NRV.")
    sec2 = [
        {"sec_num": 1, "sec_title": "Ghi Nhận và Kế Toán Hàng Tồn Kho Theo VAS 02 và IAS 2",
         "content": ("Hàng tồn kho là những tài sản được giữ để bán trong kỳ sản xuất, kinh doanh thông thường; "
                     "đang trong quá trình sản xuất kinh doanh dở dang; hoặc nguyên liệu, vật liệu, công cụ dụng cụ để sử dụng trong quá trình sản xuất. "
                     "Hàng tồn kho được tính theo giá gốc, bao gồm: Chi phí thu mua, chi phí chế biến và các chi phí liên quan trực tiếp khác.\n\n"
                     "Hai phương pháp kế toán hàng tồn kho:\n"
                     "- Phương pháp Kê khai thường xuyên (Perpetual Inventory System): Theo dõi, phản ánh liên tục, có hệ thống tình hình nhập, xuất, tồn kho "
                     "trên các tài khoản hàng tồn kho (151 đến 158). Áp dụng cho các doanh nghiệp sản xuất, thương mại quy mô lớn.\n"
                     "- Phương pháp Kiểm kê định kỳ (Periodic Inventory System): Căn cứ kết quả kiểm kê thực tế cuối kỳ để tính giá vốn hàng xuất bán: "
                     "Giá vốn xuất trong kỳ = Trị giá tồn đầu kỳ + Tổng trị giá nhập trong kỳ - Trị giá tồn cuối kỳ."),
         "formulas": ["Giá gốc hàng nhập kho = Giá mua ghi trên hóa đơn - Chiết khấu thương mại/giảm giá + Thuế không hoàn lại + Chi phí vận chuyển, bốc xếp, bảo hiểm",
                      "Giá vốn hàng bán (KKĐK) = Tồn kho đầu kỳ (TK 611) + Mua trong kỳ (TK 611) - Tồn kho cuối kỳ kiểm kê"],
         "case_studies": [{"title": "Thế Giới Di Động (Mobile World - MWG)", "detail": "Ứng dụng hệ thống kiểm kê thường xuyên kết hợp mã vạch và RFID để quản lý hàng tồn kho thiết bị điện thoại, điện máy trên toàn bộ mạng lưới hơn 3000 cửa hàng."}]},
        {"sec_num": 2, "sec_title": "Dự Phòng Giảm Giá Hàng Tồn Kho Theo Giá Trị Thuần",
         "content": ("Cuối kỳ kế toán năm, khi giá trị thuần có thể thực hiện được (NRV) của hàng tồn kho nhỏ hơn giá gốc thì phải trích lập dự phòng giảm giá.\n"
                     "Mức lập dự phòng = Số lượng hàng tồn kho x (Giá gốc - Giá trị thuần có thể thực hiện được NRV).\n\n"
                     "Bút toán trích lập dự phòng tính vào giá vốn hàng bán: Nợ TK 632 / Có TK 2294 (Dự phòng giảm giá hàng tồn kho). "
                     "Trường hợp cuối kỳ sau giá trị hàng tồn kho phục hồi thì kế toán hoàn nhập dự phòng ghi giảm giá vốn: Nợ TK 2294 / Có TK 632. "
                     "Việc trích lập phải được thực hiện cho từng mặt hàng riêng lẻ hoặc từng nhóm mặt hàng tương tự."),
         "formulas": ["NRV = Giá bán ước tính của hàng tồn kho - Chi phí ước tính để hoàn thành sản phẩm - Chi phí ước tính cần thiết cho việc tiêu thụ",
                      "Dự phòng cần trích = Max(0, Giá gốc sổ sách - NRV)"],
         "case_studies": [{"title": "Công ty Cổ phần Thép Nam Kim (NKG)", "detail": "Trích lập và hoàn nhập dự phòng giảm giá hàng tồn kho cuộn cán nóng HRC hàng trăm tỷ đồng khi giá thép thế giới biến động mạnh theo chu kỳ hàng hóa."}]}
    ]
    phd2 = {
        "topics": [
            "Lý thuyết Quản trị Hàng tồn kho và Tối ưu hóa Dòng tiền (Inventory Management & Working Capital Theory): Mối liên hệ đánh đổi giữa chi phí lưu kho, chi phí thiếu hụt và tỷ suất lợi nhuận trên tài sản (ROA).",
            "Quản trị Lợi nhuận thông qua Chi phí Sản xuất Thực tế (Real Activities Manipulation via Overproduction - Roychowdhury 2006): Hành vi sản xuất vượt mức công suất để giảm chi phí cố định phân bổ trên mỗi sản phẩm nhằm hạ giá vốn hàng bán và thổi phồng lợi nhuận ngắn hạn.",
            "Kiểm định thực nghiệm: Đo lường mức độ bất thường của hàng tồn kho (Abnormal Inventory Growth) như một tín hiệu dự báo suy giảm hiệu quả tài chính tương lai trên sàn HOSE."
        ]
    }
    q2 = [
        "Phân tích sự khác biệt về bản chất kế toán và đối tượng áp dụng giữa phương pháp Kê khai thường xuyên và Kiểm kê định kỳ.",
        "Tại sao chuẩn mực IAS 2 và VAS 02 quy định hàng tồn kho phải được đánh giá theo giá thấp hơn giữa Giá gốc và Giá trị thuần có thể thực hiện được (Lower of Cost and Net Realizable Value)?",
        "Trình bày quy trình xử lý kế toán khi phát hiện thừa hoặc thiếu hàng tồn kho trong quá trình kiểm kê thực tế cuối niên độ."
    ]
    b.add_chapter(2, "Kế toán Hàng tồn kho", intro2, sec2, phd2, q2)
    
    # Chương 3
    intro3 = ("Chương 3 trình bày kế toán tài sản cố định hữu hình, tài sản vô hình và bất động sản đầu tư - "
              "cơ sở hạ tầng vật chất và công nghệ quyết định năng lực sản xuất dài hạn của doanh nghiệp.")
    sec3 = [
        {"sec_num": 1, "sec_title": "Tiêu Chuẩn Ghi Nhận và Khấu Hao Tài Sản Cố Định",
         "content": ("Theo Thông tư 45/2013/TT-BTC, tài sản được ghi nhận là TSCĐ khi thỏa mãn đồng thời 4 tiêu chuẩn: "
                     "(1) Chắc chắn thu được lợi ích kinh tế trong tương lai; (2) Có thời gian sử dụng trên 1 năm; "
                     "(3) Nguyên giá tài sản phải được xác định một cách tin cậy và có giá trị từ 30.000.000 đồng trở lên.\n\n"
                     "Các phương pháp trích khấu hao TSCĐ:\n"
                     "- Phương pháp khấu hao đường thẳng (Straight-line Method): Mức khấu hao hàng năm không đổi theo thời gian sử dụng ước tính.\n"
                     "- Phương pháp khấu hao theo số dư giảm dần có điều chỉnh (Declining Balance Method): Mức khấu hao cao ở những năm đầu và giảm dần.\n"
                     "- Phương pháp khấu hao theo số lượng, khối lượng sản phẩm (Units-of-production Method): Căn cứ vào công suất thực tế sản xuất.\n"
                     "Bút toán trích khấu hao: Nợ TK 627, 641, 642 / Có TK 214 (Hao mòn tài sản cố định)."),
         "formulas": ["Mức khấu hao năm (Đường thẳng) = Nguyên giá TSCĐ / Thời gian trích khấu hao (năm)",
                      "Tỷ lệ khấu hao nhanh = (1 / Số năm sử dụng) x Hệ số điều chỉnh (1.5 hoặc 2.0 hoặc 2.5)"],
         "case_studies": [{"title": "Công ty Cổ phần Nhiệt điện Phả Lại (PPC)", "detail": "Ảnh hưởng đột biến đến lợi nhuận khi các tổ máy dây chuyền 1 hết khấu hao hoàn toàn nhưng vẫn tiếp tục phát điện vận hành ổn định."}]},
        {"sec_num": 2, "sec_title": "Kế Toán Nâng Cấp, Thanh Lý và Bất Động Sản Đầu Tư",
         "content": ("Chi phí sửa chữa, bảo dưỡng thường xuyên được hạch toán trực tiếp vào chi phí SXKD trong kỳ. "
                     "Ngược lại, chi phí nâng cấp làm tăng công suất, kéo dài tuổi thọ hoặc nâng cao chất lượng sản phẩm được vốn hóa ghi tăng nguyên giá TSCĐ: "
                     "Nợ TK 211 / Nợ TK 133 / Có TK 112, 331.\n\n"
                     "Khi thanh lý, nhượng bán TSCĐ, kế toán ghi giảm nguyên giá và giá trị hao mòn lũy kế: "
                     "Nợ TK 214 (Giá trị đã hao mòn), Nợ TK 811 (Giá trị còn lại) / Có TK 211 (Nguyên giá). "
                     "Khoản thu từ thanh lý được ghi nhận vào thu nhập khác: Nợ TK 112, 131 / Có TK 711, Có TK 3331.\n\n"
                     "Bất động sản đầu tư (TK 217) là quyền sử dụng đất, nhà do doanh nghiệp nắm giữ nhằm mục đích thu lợi từ việc cho thuê "
                     "hoặc chờ tăng giá để bán, không phục vụ mục đích sản xuất thông thường theo VAS 05 / IAS 40."),
         "formulas": ["Giá trị còn lại = Nguyên giá TSCĐ - Giá trị hao mòn lũy kế",
                      "Lợi nhuận thanh lý = Thu nhập thanh lý (TK 711) - Chi phí thanh lý (TK 811) - Giá trị còn lại"],
         "case_studies": [{"title": "Tổng Công ty Phát triển Đô thị Kinh Bắc (KBC)", "detail": "Hạch toán chuyển nhượng các lô đất khu công nghiệp và phân loại giữa Hàng tồn kho (TK 156), Bất động sản đầu tư (TK 217) và TSCĐ (TK 211)."}]}
    ]
    phd3 = {
        "topics": [
            "Mô hình Định giá lại TSCĐ theo IAS 16 (Revaluation Model vs Cost Model): Lựa chọn chính sách kế toán tài sản cố định và tác động đến chi phí vốn chủ sở hữu, tính biến động của vốn tự có tại các doanh nghiệp niêm yết.",
            "Lý thuyết Tổn thất Tài sản (Asset Impairment - IAS 36): Sử dụng dòng tiền chiết khấu (DCF) và đơn vị tạo tiền (Cash-Generating Unit - CGU) để đánh giá tổn thất lợi thế thương mại và tài sản dài hạn.",
            "Chuyên đề Tiến sĩ: Đánh giá độ nhạy của quyết định đầu tư TSCĐ (CAPEX) đối với dòng tiền nội bộ trong điều kiện hạn chế tài chính (Financial Constraints - Fazzari, Hubbard & Petersen 1988 Model)."
        ]
    }
    q3 = [
        "Phân biệt điều kiện vốn hóa chi phí phát sinh sau ghi nhận ban đầu (nâng cấp TSCĐ) so với chi phí sửa chữa bảo dưỡng định kỳ.",
        "Trình bày nguyên tắc và các bút toán kế toán thanh lý, nhượng bán tài sản cố định hữu hình theo Thông tư 200/2014/TT-BTC.",
        "So sánh bản chất kinh tế và phương pháp kế toán giữa Bất động sản chủ sở hữu sử dụng (VAS 03) và Bất động sản đầu tư (VAS 05)."
    ]
    b.add_chapter(3, "Kế toán Tài sản cố định và Bất động sản đầu tư", intro3, sec3, phd3, q3)
    
    # Chương 4
    intro4 = ("Chương 4 nghiên cứu kế toán tiền lương, các khoản bảo hiểm xã hội, y tế, thất nghiệp và chế độ phúc lợi người lao động. "
              "Đây là phần hành gắn kết chặt chẽ với pháp luật lao động, an sinh xã hội và chính sách thuế TNCN.")
    sec4 = [
        {"sec_num": 1, "sec_title": "Quỹ Tiền Lương và Các Khoản Trích Theo Lương",
         "content": ("Tiền lương là phần thù lao bằng tiền mà doanh nghiệp trả cho người lao động theo hợp đồng lao động và năng suất làm việc. "
                     "Doanh nghiệp tổ chức tính lương theo thời gian, theo sản phẩm hoặc lương khoán.\n\n"
                     "Các khoản trích theo lương theo quy định hiện hành tại Việt Nam:\n"
                     "- Bảo hiểm Xã hội (BHXH): Doanh nghiệp đóng 17%, Người lao động đóng 8%.\n"
                     "- Bảo hiểm Y tế (BHYT): Doanh nghiệp đóng 3%, Người lao động đóng 1.5%.\n"
                     "- Bảo hiểm Thất nghiệp (BHTN): Doanh nghiệp đóng 1%, Người lao động đóng 1%.\n"
                     "- Kinh phí Công đoàn (KPCĐ): Doanh nghiệp đóng 2% trên tổng quỹ lương đóng BHXH.\n"
                     "Tổng tỷ lệ đóng bảo hiểm và công đoàn là 34% (Doanh nghiệp chịu 23.5% tính vào chi phí SXKD; Người lao động chịu 10.5% trừ vào lương)."),
         "formulas": ["Chi phí trích theo lương tính vào DN = Quỹ lương đóng BHXH x 23.5%",
                      "Khoản trừ vào lương người lao động = Quỹ lương đóng BHXH x 10.5% + Thuế TNCN khấu trừ"],
         "case_studies": [{"title": "Công ty Cổ phần Dệt may - Đầu tư - Thương mại Thành Công (TCM)", "detail": "Quản trị chi phí nhân công quy mô hơn 7.000 công nhân và hạch toán tối ưu hóa quỹ phúc lợi, khen thưởng người lao động."}]},
        {"sec_num": 2, "sec_title": "Hạch Toán Tiền Lương và Phúc Lợi Theo IAS 19",
         "content": ("Hạch toán chi phí tiền lương phải trả người lao động trong kỳ:\n"
                     "- Phân bổ chi phí tiền lương: Nợ TK 622 (Nhân công trực tiếp), Nợ TK 627 (Nhân viên phân xưởng), Nợ TK 641 (Bán hàng), Nợ TK 642 (Quản lý) / Có TK 334 (Phải trả người lao động).\n"
                     "- Trích các khoản theo lương tính vào chi phí: Nợ TK 622, 627, 641, 642 (23.5%) / Có TK 338 (Chi tiết 3382, 3383, 3384, 3386).\n"
                     "- Trừ các khoản bảo hiểm vào lương: Nợ TK 334 (10.5%) / Có TK 338.\n"
                     "- Khấu trừ thuế TNCN: Nợ TK 334 / Có TK 3335.\n"
                     "- Chi trả tiền lương thực lĩnh cho người lao động: Nợ TK 334 / Có TK 111, 112.\n\n"
                     "Theo chuẩn mực quốc tế IAS 19 (Employee Benefits), các khoản thù lao dài hạn, trợ cấp thôi việc và quỹ hưu trí xác định "
                     "phải được ước tính theo mô hình toán bảo hiểm định phí (Actuarial Valuation) và ghi nhận nghĩa vụ nợ phải trả hiện tại."),
         "formulas": ["Lương thực lĩnh = Tổng tiền lương, thưởng - Các khoản trích BHXH, BHYT, BHTN (10.5%) - Thuế TNCN khấu trừ - Các khoản tạm ứng/phạt",
                      "Nghĩa vụ trợ cấp hưu trí (IAS 19 Defined Benefit Obligation) = Giá trị hiện tại dòng chi trả trợ cấp hưu trí tương lai chiết khấu theo lãi suất trái phiếu chính phủ"],
         "case_studies": [{"title": "Tập đoàn Viễn thông Quân đội (Viettel)", "detail": "Hạch toán quỹ tiền lương gắn liền với chỉ số đánh giá hiệu quả công việc KPI và cơ chế phân phối thù lao theo giá trị gia tăng."}]}
    ]
    phd4 = {
        "topics": [
            "Lý thuyết Thù lao Ban Điều hành và Khế ước Đại diện (Executive Compensation & Agency Theory - Jensen & Meckling 1976): Thiết kế gói quyền chọn cổ phiếu (ESOP) gắn với mục tiêu EPS và nguy cơ thao túng lợi nhuận ngắn hạn.",
            "Chuẩn mực Kế toán Quốc tế IAS 19 về Phúc lợi Người lao động: Rủi ro tài phán định phí bảo hiểm (Actuarial Risk) và phương pháp phản ánh biến động thặng dư/thâm hụt quỹ hưu trí vào Báo cáo Thu nhập Toàn diện Khác (OCI).",
            "Nghiên cứu định lượng: Tác động của chính sách tăng lương tối thiểu vùng đến cơ cấu chi phí sản xuất và năng lực cạnh tranh xuất khẩu của các doanh nghiệp thâm dụng lao động tại Việt Nam."
        ]
    }
    q4 = [
        "Trình bày chi tiết tỷ lệ các khoản trích theo lương (BHXH, BHYT, BHTN, KPCĐ) tính vào chi phí doanh nghiệp và trừ vào lương người lao động.",
        "Viết chuỗi bút toán kế toán hạch toán đầy đủ quy trình từ tính lương, trích bảo hiểm, khấu trừ thuế TNCN đến thanh toán lương cho người lao động.",
        "Phân tích sự khác biệt giữa Phúc lợi ngắn hạn và Nghĩa vụ phúc lợi dài hạn sau khi nghỉ việc theo chuẩn mực IAS 19."
    ]
    b.add_chapter(4, "Kế toán Tiền lương và các Khoản Trích theo lương", intro4, sec4, phd4, q4)
    
    # Chương 5
    intro5 = ("Chương 5 bao quát cấu trúc tài trợ dài hạn của doanh nghiệp: Nợ phải trả tài chính và Nguồn vốn chủ sở hữu. "
              "Học viên được trang bị kiến thức hạch toán phát hành cổ phiếu, trái phiếu, vốn hóa chi phí đi vay và chính sách cổ tức.")
    sec5 = [
        {"sec_num": 1, "sec_title": "Kế Toán Nợ Vay và Chi Phí Đi Vay Vốn Hóa (VAS 16 / IAS 23)",
         "content": ("Nợ vay tài chính bao gồm vay ngắn hạn, vay dài hạn (TK 341) và phát hành trái phiếu thường (TK 3431). "
                     "Kế toán theo dõi chi tiết theo từng khế ước vay, thời hạn trả nợ, lãi suất và đồng tiền vay.\n\n"
                     "Theo VAS 16 và IAS 23, chi phí đi vay liên quan trực tiếp đến việc đầu tư xây dựng hoặc sản xuất tài sản dở dang "
                     "(tài sản đủ điều kiện vốn hóa, cần một thời gian đủ dài trên 12 tháng để hoàn thành) được vốn hóa ghi tăng giá trị tài sản đó: "
                     "Nợ TK 241 (XDCB dở dang) / Có TK 112, 335. "
                     "Chi phí đi vay của các khoản vay thông thường phục vụ hoạt động sản xuất kinh doanh được tính vào chi phí tài chính trong kỳ: Nợ TK 635 / Có TK 112, 335."),
         "formulas": ["Lãi vay vốn hóa = Chi phí đi vay thực tế phát sinh trong kỳ - Thu nhập từ việc đầu tư tạm thời của các khoản vay đó",
                      "Tỷ lệ vốn hóa = Tổng chi phí đi vay bình quân của các khoản vay chung / Dư nợ bình quân trọng số các khoản vay chung"],
         "case_studies": [{"title": "Công ty Cổ phần Vinhomes (VHM)", "detail": "Hạch toán vốn hóa chi phí lãi vay hàng nghìn tỷ đồng vào giá thành các đại đô thị quy mô hàng trăm héc-ta trong giai đoạn giải phóng mặt bằng và thi công hạ tầng."}]},
        {"sec_num": 2, "sec_title": "Kế Toán Nguồn Vốn Chủ Sở Hữu và Chính Sách Cổ Tức",
         "content": ("Vốn chủ sở hữu phản ánh nguồn tài trợ dài hạn của các cổ đông, bao gồm:\n"
                     "- Vốn góp của chủ sở hữu (TK 4111): Ghi nhận theo mệnh giá cổ phiếu phát hành (tại Việt Nam là 10.000 đồng/cổ phần).\n"
                     "- Thặng dư vốn cổ phần (TK 4112): Chênh lệch giữa giá phát hành thực tế và mệnh giá cổ phiếu.\n"
                     "- Quỹ đầu tư phát triển (TK 414): Trích lập từ lợi nhuận sau thuế để tái đầu tư mở rộng sản xuất.\n"
                     "- Lợi nhuận sau thuế chưa phân phối (TK 421): Phản ánh kết quả kinh doanh lũy kế sau khi nộp thuế TNDN và chia cổ tức.\n\n"
                     "Hạch toán chi trả cổ tức:\n"
                     "- Khi có nghị quyết ĐHĐCĐ công bố cổ tức bằng tiền: Nợ TK 421 / Có TK 3388.\n"
                     "- Khi chi trả cổ tức bằng tiền mặt: Nợ TK 3388 / Có TK 112.\n"
                     "- Khi trả cổ tức bằng cổ phiếu (thưởng cổ phiếu): Nợ TK 421 / Có TK 4111 (Mệnh giá), Có TK 4112 (Thặng dư nếu có)."),
         "formulas": ["Giá trị sổ sách trên mỗi cổ phần (BVPS) = (Tổng vốn chủ sở hữu - Vốn cổ phần ưu đãi) / Số lượng cổ phiếu phổ thông đang lưu hành",
                      "Hệ số chi trả cổ tức (Dividend Payout Ratio) = Tổng cổ tức chi trả / Lợi nhuận sau thuế"],
         "case_studies": [{"title": "Ngân hàng TMCP Quân đội (MBB)", "detail": "Quy trình tăng vốn điều lệ thông qua phát hành cổ phiếu trả cổ tức từ nguồn lợi nhuận giữ lại để cải thiện hệ số an toàn vốn CAR theo chuẩn Basel II."}]}
    ]
    phd5 = {
        "topics": [
            "Lý thuyết Cấu trúc Vốn Modigliani-Miller (M&M 1958, 1963) và Lý thuyết Trật tự Phân hạng (Pecking Order Theory - Myers & Majluf 1984): Động cơ lựa chọn giữa lợi nhuận giữ lại, vay nợ ngân hàng và phát hành cổ phiếu mới.",
            "Lý thuyết Khế ước Nợ và Quản trị Lợi nhuận (Debt Covenant Hypothesis): Động cơ làm tăng lợi nhuận kế toán để tránh vi phạm các điều khoản trần nợ vay (Debt-to-EBITDA, Interest Coverage Ratio) trong hợp đồng tín dụng hợp vốn.",
            "Chuyên đề Tiến sĩ: Ứng dụng mô hình Structural Equation Modeling (SEM) khảo sát mối quan hệ giữa cơ cấu sở hữu (sở hữu nhà nước, sở hữu nước ngoài, sở hữu gia đình) và chính sách chi trả cổ tức tại Việt Nam."
        ]
    }
    q5 = [
        "Phân biệt điều kiện vốn hóa chi phí đi vay vào giá trị tài sản dở dang (VAS 16) so với việc ghi nhận trực tiếp vào chi phí tài chính trong kỳ.",
        "Trình bày kết cấu và nội dung kinh tế của Tài khoản 411 (Vốn đầu tư của chủ sở hữu) và Tài khoản 4112 (Thặng dư vốn cổ phần).",
        "Phân tích tác động của hai hình thức chi trả cổ tức: Cổ tức bằng tiền mặt và Cổ tức bằng cổ phiếu đến Bảng cân đối kế toán của doanh nghiệp."
    ]
    b.add_chapter(5, "Kế toán Nợ phải trả và Nguồn vốn Chủ sở hữu", intro5, sec5, phd5, q5)
    
    # Chương 6
    intro6 = ("Chương 6 tổng kết toàn bộ chu trình kế toán tài chính qua kỹ thuật lập và trình bày báo cáo tài chính "
              "theo Thông tư 200/2014/TT-BTC của Bộ Tài chính và định hướng hội tụ chuẩn mực quốc tế IFRS.")
    sec6 = [
        {"sec_num": 1, "sec_title": "Quy Trình và Kỹ Thuật Lập Báo Cáo Tài Chính",
         "content": ("Báo cáo tài chính là phương tiện truyền tải thông tin kinh tế quan trọng nhất của doanh nghiệp. "
                     "Hệ thống BCTC năm bao gồm: Bảng Cân đối kế toán (Mẫu B01-DN), Báo cáo Kết quả hoạt động kinh doanh (Mẫu B02-DN), "
                     "Báo cáo Lưu chuyển tiền tệ (Mẫu B03-DN) và Bản Thuyết minh Báo cáo tài chính (Mẫu B09-DN).\n\n"
                     "Kỹ thuật lấy số liệu lập Bảng Cân đối kế toán:\n"
                     "- Các chỉ tiêu Tài sản lấy từ số dư Nợ của các tài khoản tài sản loại 1 và loại 2.\n"
                     "- Các khoản dự phòng (TK 229) và hao mòn TSCĐ (TK 214) có số dư Có nhưng được trình bày ở phần Tài sản dưới dạng số âm (ghi trong ngoặc đơn).\n"
                     "- Các tài khoản lưỡng tính (TK 131, TK 331) tuyệt đối không bù trừ số dư giữa các khách hàng khác nhau: "
                     "Số dư Nợ chi tiết ghi nhận bên Tài sản (Phải thu), Số dư Có chi tiết ghi nhận bên Nguồn vốn (Khách hàng trả tiền trước/Phải trả)."),
         "formulas": ["Tính cân đối tổng thể: Tổng cộng Tài sản = Tổng cộng Nguồn vốn",
                      "Cân đối dòng tiền: Số dư tiền cuối kỳ = Số dư tiền đầu kỳ + Lưu chuyển tiền thuần trong kỳ (CFO + CFI + CFF)"],
         "case_studies": [{"title": "Tập đoàn Xăng dầu Việt Nam (Petrolimex - PLX)", "detail": "Quy trình lập và công bố báo cáo tài chính hợp nhất kiểm toán năm theo thời hạn 90 ngày quy định của UBCKNN."}]},
        {"sec_num": 2, "sec_title": "Phương Pháp Lập Báo Cáo Lưu Chuyển Tiền Tệ Theo Phương Pháp Gián Tiếp",
         "content": ("Phương pháp gián tiếp xuất phát từ Lợi nhuận trước thuế trên Báo cáo kết quả kinh doanh, "
                     "sau đó điều chỉnh cho các khoản mục phi tiền tệ và biến động vốn lưu động để xác định Lưu chuyển tiền thuần từ HĐKD (CFO):\n"
                     "(1) Điều chỉnh chi phí khấu hao TSCĐ (Cộng lại vào lợi nhuận do không thực chi tiền).\n"
                     "(2) Điều chỉnh các khoản trích lập hoặc hoàn nhập dự phòng (Cộng dự phòng trích lập, trừ hoàn nhập).\n"
                     "(3) Điều chỉnh lãi/lỗ chênh lệch tỷ giá hối đoái chưa thực hiện.\n"
                     "(4) Điều chỉnh lãi/lỗ từ hoạt động đầu tư (Trừ lãi bán TSCĐ, thanh lý đầu tư tài chính ra khỏi HĐKD để chuyển về HĐ đầu tư).\n"
                     "(5) Điều chỉnh chi phí lãi vay (Cộng lại chi phí lãi vay để phản ánh dòng tiền trả lãi riêng biệt).\n"
                     "(6) Điều chỉnh biến động vốn lưu động: Tăng các khoản phải thu (Trừ ra), Tăng hàng tồn kho (Trừ ra), Tăng các khoản phải trả (Cộng vào)."),
         "formulas": ["CFO (Gián tiếp) = Lợi nhuận trước thuế + Khấu hao TSCĐ + Dự phòng +/- Lãi/lỗ tỷ giá chưa thực hiện - Lãi đầu tư + Chi phí lãi vay - Δ Phải thu - Δ Hàng tồn kho + Δ Phải trả - Thuế TNDN thực nộp - Tiền lãi vay đã trả"],
         "case_studies": [{"title": "Công ty Cổ phần Tập đoàn Masan (MSN)", "detail": "Phân tích điều chỉnh dòng tiền gián tiếp đối với chi phí khấu hao tài sản vô hình và lợi thế thương mại phát sinh từ các thương vụ sáp nhập M&A."}]}
    ]
    phd6 = {
        "topics": [
            "Lý thuyết Quản trị Lợi nhuận Thực tính (Accrual-based Earnings Management - Modified Jones Model 1995, Dechow et al.): Đo lường các khoản dồn tích bất thường (Discretionary Accruals) tách biệt khỏi các khoản dồn tích phi chủ quan (Nondiscretionary Accruals).",
            "Mô hình Sloan Accrual Anomaly (Sloan 1996): Kiểm định mức độ bền vững (Persistence) của dòng tiền hoạt động kinh doanh (Cash Flows) so với mức độ bền vững của các khoản dồn tích kế toán (Accruals) tại thị trường Việt Nam.",
            "Chuyên đề Tiến sĩ: Đánh giá chất lượng BCTC (Financial Reporting Quality) thông qua thước đo Kothari, Leone & Wasley (2005) điều chỉnh theo hiệu quả hoạt động kinh doanh (Performance-matched discretionary accruals)."
        ]
    }
    q6 = [
        "Tại sao khi lập Bảng cân đối kế toán, kế toán viên không được tự tiện bù trừ số dư Nợ và số dư Có của Tài khoản 131 (Phải thu khách hàng)?",
        "Trình bày chi tiết các bước điều chỉnh từ Lợi nhuận trước thuế sang Lưu chuyển tiền thuần từ hoạt động kinh doanh theo phương pháp gián tiếp.",
        "Phân tích vai trò của Bản Thuyết minh Báo cáo tài chính trong việc cung cấp thông tin về các nghĩa vụ nợ tiềm tàng và các sự kiện sau ngày kết thúc niên độ."
    ]
    b.add_chapter(6, "Báo cáo Tài chính Doanh nghiệp (Phần 1)", intro6, sec6, phd6, q6)
    
    out_dir = os.path.join(BASE_DIR, r"02_Kế toán & Kiểm toán\[NEU] Kế toán tài chính 1 - GS.TS Đặng Thị Loan (NXB ĐHKTQD)")
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Kế toán tài chính 1 - GS.TS Đặng Thị Loan (NXB ĐHKTQD).pdf")
    pages, size_mb = b.save(out_pdf)
    print(f"-> Hoàn thành Sách 2: {pages} trang, {size_mb:.2f} MB. Lưu tại: {out_pdf}")
    return {"book": "Kế toán tài chính 1", "pages": pages, "size_mb": size_mb, "path": out_pdf}


def build_book_3():
    print("--- Đang biên soạn Sách 3: Kế toán tài chính 2 ---")
    title = "Kế toán Tài chính 2"
    code = "KTKT1103"
    faculty = "Viện Kế toán - Kiểm toán"
    authors = "PGS.TS. Nguyễn Phú Giang (Chủ biên), TS. Nguyễn Thị Hồng Thúy, TS. Vũ Thùy Linh"
    
    b = NEUTextbookBuilder(title, code, faculty, authors)
    b.build_cover()
    
    toc = [
        {"chapter_num": 1, "chapter_title": "Kế toán Doanh thu, Thu nhập khác và Chi phí",
         "topics": ["Kế toán doanh thu bán hàng hóa, cung cấp dịch vụ theo VAS 14 và IFRS 15", "Kế toán các hợp đồng xây dựng theo chuẩn mực kế toán", "Kế toán doanh thu hoạt động tài chính và chi phí tài chính", "Kế toán chi phí bán hàng, chi phí quản lý doanh nghiệp và chi phí khác"]},
        {"chapter_num": 2, "chapter_title": "Kế toán Thuế Thu nhập Doanh nghiệp Hiện hành và Hoãn lại",
         "topics": ["Bản chất chênh lệch vĩnh viễn và chênh lệch tạm thời theo VAS 17 / IAS 12", "Kế toán thuế TNDN hiện hành (TK 8211 / TK 3334)", "Kế toán tài sản thuế TNDN hoãn lại (TK 243)", "Kế toán thuế TNDN hoãn lại phải trả (TK 347) và lập chỉ tiêu BCTC"]},
        {"chapter_num": 3, "chapter_title": "Kế toán Đầu tư Tài chính và Công cụ Tài chính",
         "topics": ["Kế toán chứng khoán kinh doanh và đầu tư nắm giữ đến ngày đáo hạn", "Kế toán đầu tư vào công ty con, công ty liên kết và liên doanh (VAS 07, 08)", "Phương pháp giá gốc (Cost Method) và Phương pháp vốn chủ sở hữu (Equity Method)", "Kế toán trích lập dự phòng tổn thất đầu tư tài chính và IFRS 9"]},
        {"chapter_num": 4, "chapter_title": "Kế toán Hoạt động Thuê Tài sản (VAS 06 & IFRS 16)",
         "topics": ["Phân loại thuê tài chính và thuê hoạt động theo chuẩn mực VAS 06", "Kế toán thuê tài sản tại bên đi thuê và bên cho thuê theo VAS", "Mô hình quyền sử dụng tài sản (ROU Asset) và nợ thuê tài sản theo IFRS 16", "Kế toán giao dịch bán và thuê lại (Sale and Leaseback)"]},
        {"chapter_num": 5, "chapter_title": "Hợp nhất Kinh doanh và Báo cáo Tài chính Hợp nhất",
         "topics": ["Bản chất hợp nhất kinh doanh và xác định ngày mua theo IFRS 3 / VAS 11", "Xác định giá phí hợp nhất, giá trị hợp lý tài sản thuần và Lợi thế thương mại (Goodwill)", "Lợi ích của cổ đông không kiểm soát (NCI - Non-controlling Interest)", "Kỹ thuật loại trừ các giao dịch nội bộ tập đoàn khi lập BCTC hợp nhất"]},
        {"chapter_num": 6, "chapter_title": "Kế toán Thay đổi Chính sách, Ước tính Kế toán và Sai sót",
         "topics": ["Phân biệt thay đổi chính sách kế toán và thay đổi ước tính kế toán (VAS 29 / IAS 8)", "Phương pháp áp dụng hồi tố (Retrospective) và áp dụng phi hồi tố (Prospective)", "Kỹ thuật sửa chữa sai sót trọng yếu của các niên độ kế toán trước", "Kế toán các sự kiện phát sinh sau ngày kết thúc kỳ kế toán năm (VAS 23 / IAS 10)"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chương 1
    intro1 = ("Chương 1 đi sâu vào các nghiệp vụ kế toán doanh thu và chi phí thời kỳ phức tạp. "
              "Trọng tâm nghiên cứu là mô hình ghi nhận doanh thu 5 bước hiện đại theo IFRS 15 thay thế mô hình chuyển giao rủi ro truyền thống.")
    sec1 = [
        {"sec_num": 1, "sec_title": "Kế Toán Doanh Thu Bán Hàng Theo VAS 14 và IFRS 15",
         "content": ("Theo VAS 14, doanh thu bán hàng được ghi nhận khi thỏa mãn đồng thời 5 điều kiện (Doanh nghiệp đã chuyển giao phần lớn rủi ro và lợi ích gắn liền với quyền sở hữu; "
                     "Không còn nắm giữ quyền quản lý; Doanh thu xác định tương đối chắc chắn; Đã thu được hoặc chắc chắn thu được lợi ích kinh tế; "
                     "Xác định được chi phí liên quan đến giao dịch).\n\n"
                     "Tuy nhiên, IFRS 15 thiết lập một khuôn khổ toàn cầu dựa trên mô hình 5 bước thống nhất:\n"
                     "- Bước 1: Xác định hợp đồng với khách hàng.\n"
                     "- Bước 2: Xác định các nghĩa vụ thực hiện (Performance Obligations) riêng biệt trong hợp đồng.\n"
                     "- Bước 3: Xác định giá giao dịch (Transaction Price).\n"
                     "- Bước 4: Phân bổ giá giao dịch cho từng nghĩa vụ thực hiện căn cứ theo giá bán độc lập (Standalone Selling Price).\n"
                     "- Bước 5: Ghi nhận doanh thu khi (hoặc trong khi) doanh nghiệp hoàn thành từng nghĩa vụ thực hiện (tại một thời điểm hoặc theo thời gian)."),
         "formulas": ["Doanh thu phân bổ nghĩa vụ A = Giá giao dịch x (Giá bán độc lập của A / Tổng giá bán độc lập các nghĩa vụ)",
                      "Bút toán ghi nhận: Nợ TK 112, 131 / Có TK 511, Có TK 3331"],
         "case_studies": [{"title": "Tập đoàn Công nghiệp - Viễn thông Quân đội (Viettel)", "detail": "Áp dụng IFRS 15 phân bổ doanh thu cho gói cước bán kèm thiết bị di động (Handset bundle with telecom service plan)."}]},
        {"sec_num": 2, "sec_title": "Kế Toán Hợp Đồng Xây Dựng và Doanh Thu Theo Tiến Độ",
         "content": ("Theo VAS 13 và IFRS 15, đối với các hợp đồng xây dựng kéo dài qua nhiều niên độ kế toán, doanh thu và chi phí được ghi nhận "
                     "theo phương pháp tỷ lệ phần trăm hoàn thành (Percentage of Completion Method):\n"
                     "- Xác định tỷ lệ hoàn thành = Chi phí thực tế lũy kế đã phát sinh / Tổng chi phí dự toán ước tính của hợp đồng.\n"
                     "- Doanh thu ghi nhận trong kỳ = (Tỷ lệ hoàn thành x Tổng giá trị hợp đồng) - Doanh thu lũy kế đã ghi nhận các kỳ trước.\n\n"
                     "Kế toán sử dụng Tài khoản 337 (Thanh toán theo tiến độ kế hoạch hợp đồng xây dựng) để theo dõi các khoản thanh toán dở dang "
                     "và đối chiếu với hóa đơn xuất theo tiến độ thực tế."),
         "formulas": ["Tỷ lệ hoàn thành = Chi phí phát sinh thực tế / Tổng chi phí ước tính",
                      "Doanh thu kỳ này = Tỷ lệ hoàn thành x Giá trị hợp đồng - Doanh thu kỳ trước"],
         "case_studies": [{"title": "Công ty Cổ phần Xây dựng Coteccons (CTD)", "detail": "Hạch toán doanh thu theo tiến độ thi công các dự án tổng thầu xây dựng khu đô thị và căn hộ cao cấp."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Kế toán Dựa trên Hợp đồng (Contract-based Accounting Theory): Phân tích tác động của việc áp dụng IFRS 15 đến thời điểm ghi nhận doanh thu và tính biến động lợi nhuận trong ngành bất động sản dân cư tại Việt Nam.",
            "Quản trị Doanh thu Trực tiếp (Revenue Manipulation - Stubben 2010 Model): Mô hình nhận diện hành vi ghi nhận doanh thu non (Premature Revenue Recognition) thông qua phân tích biến động bất thường của số dư khoản phải thu khách hàng.",
            "Chuyên đề Tiến sĩ: Đánh giá mối quan hệ giữa chất lượng công bố thông tin doanh thu theo IFRS 15 và chi phí nợ vay của các doanh nghiệp niêm yết trên thị trường chứng khoán Việt Nam."
        ]
    }
    q1 = [
        "Phân tích 5 bước ghi nhận doanh thu theo Chuẩn mực BCTC quốc tế IFRS 15. So sánh điểm mới vượt trội so với chuẩn mực VAS 14.",
        "Trình bày phương pháp kế toán ghi nhận doanh thu và chi phí hợp đồng xây dựng theo tỷ lệ phần trăm hoàn thành.",
        "Xử lý kế toán các khoản giảm trừ doanh thu: Chiết khấu thương mại, giảm giá hàng bán và hàng bán bị trả lại theo quy định hiện hành."
    ]
    b.add_chapter(1, "Kế toán Doanh thu, Thu nhập khác và Chi phí", intro1, sec1, phd1, q1)
    
    # Chương 2
    intro2 = ("Chương 2 giải quyết một trong những vấn đề hóc búa nhất của kế toán tài chính hiện đại: "
              "Kế toán Thuế thu nhập doanh nghiệp hoãn lại phát sinh từ sự khác biệt giữa Lợi nhuận kế toán và Thu nhập tính thuế.")
    sec2 = [
        {"sec_num": 1, "sec_title": "Bản Chất Chênh Lệch Tạm Thời và Thuế Hoãn Lại (VAS 17 / IAS 12)",
         "content": ("Lợi nhuận kế toán trước thuế được tính theo chuẩn mực kế toán (nguyên tắc dồn tích, thận trọng, phù hợp). "
                     "Trong khi đó, Thu nhập chịu thuế được xác định theo Luật Thuế TNDN (nhằm mục tiêu quản lý thu ngân sách nhà nước). "
                     "Sự khác biệt này tạo ra hai nhóm chênh lệch:\n"
                     "(1) Chênh lệch vĩnh viễn (Permanent Differences): Các khoản doanh thu hoặc chi phí được kế toán ghi nhận nhưng không bao giờ được cơ quan thuế chấp nhận "
                     "(ví dụ: Tiền phạt vi phạm giao thông, chi phí lãi vay vượt mức khống chế 30% EBITDA theo NĐ 132/2020, chi phí không có hóa đơn hợp lệ). "
                     "Chênh lệch vĩnh viễn chỉ ảnh hưởng đến chi phí thuế TNDN hiện hành trong kỳ, không phát sinh thuế hoãn lại.\n\n"
                     "(2) Chênh lệch tạm thời (Temporary Differences): Là sự chênh lệch giữa giá trị ghi sổ của tài sản/nợ phải trả trên BCTC "
                     "và cơ sở tính thuế (Tax Base) của tài sản/nợ phải trả đó. Chênh lệch này sẽ được hoàn nhập trong các kỳ tương lai."),
         "formulas": ["Thu nhập chịu thuế = Lợi nhuận kế toán trước thuế +/- Chênh lệch vĩnh viễn +/- Chênh lệch tạm thời",
                      "Thuế TNDN hiện hành phải nộp = Thu nhập chịu thuế x Thuế suất thuế TNDN (20%)"],
         "case_studies": [{"title": "Tập đoàn Vingroup (VIC)", "detail": "Hạch toán thuế TNDN hoãn lại hàng nghìn tỷ đồng phát sinh từ chênh lệch khấu hao tài sản cố định và các khoản trích trước chi phí bảo hành xe điện."}]},
        {"sec_num": 2, "sec_title": "Kế Toán Tài Sản Thuế Hoãn Lại và Thuế Hoãn Lại Phải Trả",
         "content": ("- Chênh lệch tạm thời được khấu trừ (Deductible Temporary Difference): Phát sinh khi Giá trị ghi sổ của Tài sản < Cơ sở tính thuế, "
                     "hoặc Giá trị ghi sổ của Nợ phải trả > Cơ sở tính thuế (ví dụ: Trích lập dự phòng nợ khó đòi kế toán trích nhưng thuế chưa cho trừ). "
                     "Chênh lệch này làm phát sinh Tài sản thuế TNDN hoãn lại (TK 243). "
                     "Bút toán ghi nhận: Nợ TK 243 / Có TK 8212 (Chi phí thuế TNDN hoãn lại).\n\n"
                     "- Chênh lệch tạm thời chịu thuế (Taxable Temporary Difference): Phát sinh khi Giá trị ghi sổ của Tài sản > Cơ sở tính thuế, "
                     "hoặc Giá trị ghi sổ của Nợ phải trả < Cơ sở tính thuế (ví dụ: Khấu hao nhanh theo luật thuế lớn hơn khấu hao kế toán). "
                     "Chênh lệch này làm phát sinh Thuế TNDN hoãn lại phải trả (TK 347). "
                     "Bút toán ghi nhận: Nợ TK 8212 / Có TK 347.\n\n"
                     "Tổng chi phí thuế TNDN trên Báo cáo kết quả kinh doanh = Chi phí thuế TNDN hiện hành (TK 8211) + Chi phí thuế TNDN hoãn lại (TK 8212)."),
         "formulas": ["Tài sản thuế hoãn lại (TK 243) = Chênh lệch tạm thời được khấu trừ x Thuế suất thuế TNDN",
                      "Thuế hoãn lại phải trả (TK 347) = Chênh lệch tạm thời chịu thuế x Thuế suất thuế TNDN",
                      "Thuế suất hiệu dụng (Effective Tax Rate - ETR) = Tổng chi phí thuế TNDN / Lợi nhuận kế toán trước thuế"],
         "case_studies": [{"title": "Công ty Cổ phần Sữa Việt Nam (Vinamilk - VNM)", "detail": "Phân tích biến động tài sản thuế hoãn lại liên quan đến trích trước chi phí quảng cáo, khuyến mại và dự phòng hàng tồn kho."}]}
    ]
    phd2 = {
        "topics": [
            "Chênh lệch Sổ sách - Thuế và Quản trị Lợi nhuận (Book-Tax Differences & Earnings Quality - Frank, Lynch & Rego 2009): Sử dụng chênh lệch tạm thời bất thường (Abnormal Temporary Book-Tax Differences) để phát hiện hành vi thổi phồng lợi nhuận kế toán hoặc trốn thuế doanh nghiệp.",
            "Kế toán Thuế Hoãn lại theo IAS 12 và Rủi ro Bù trừ Lỗ Tính thuế (Tax Loss Carryforwards Valuation Allowance): Quyền quyết định của ban giám đốc trong việc ghi nhận tài sản thuế hoãn lại từ các khoản lỗ tính thuế chuyển giao kỳ sau.",
            "Chuyên đề Tiến sĩ: Mô hình hóa mối quan hệ giữa Trách nhiệm Xã hội Doanh nghiệp (CSR), Quản trị Công ty và Mức độ Tránh thuế (Tax Avoidance) tại các thị trường tài chính đang phát triển."
        ]
    }
    q2 = [
        "Phân biệt bản chất kế toán và hậu quả kinh tế giữa Chênh lệch vĩnh viễn và Chênh lệch tạm thời theo VAS 17.",
        "Trình bày điều kiện và các bút toán kế toán ghi nhận Tài sản thuế TNDN hoãn lại và Thuế TNDN hoãn lại phải trả.",
        "Tại sao việc áp dụng khấu hao nhanh cho mục đích tính thuế trong khi áp dụng khấu hao đường thẳng cho mục đích kế toán lại tạo ra Thuế hoãn lại phải trả?"
    ]
    b.add_chapter(2, "Kế toán Thuế Thu nhập Doanh nghiệp Hiện hành và Hoãn lại", intro2, sec2, phd2, q2)
    
    # Chương 3
    intro3 = ("Chương 3 đi sâu vào kế toán các khoản đầu tư tài chính và công cụ tài chính phức tạp: "
              "Chứng khoán kinh doanh, các khoản đầu tư vào công ty con, công ty liên kết và phương pháp vốn chủ sở hữu.")
    sec3 = [
        {"sec_num": 1, "sec_title": "Kế Toán Chứng Khoán Kinh Doanh và Đầu Tư Nắm Giữ Đến Ngày Đáo Hạn",
         "content": ("Chứng khoán kinh doanh (TK 121) là các loại cổ phiếu, trái phiếu được doanh nghiệp mua vào với mục đích bán lại trong ngắn hạn để kiếm lời chênh lệch giá. "
                     "Kế toán phản ánh theo giá gốc bao gồm giá mua và các chi phí môi giới, giao dịch.\n\n"
                     "Cuối kỳ kế toán, doanh nghiệp trích lập dự phòng giảm giá chứng khoán kinh doanh: "
                     "Mức trích lập = Số lượng chứng khoán x (Giá gốc ghi sổ - Giá trị thị trường tại ngày khóa sổ). "
                     "Bút toán trích lập: Nợ TK 635 (Chi phí tài chính) / Có TK 2291 (Dự phòng giảm giá CKKD).\n\n"
                     "Đầu tư nắm giữ đến ngày đáo hạn (TK 128) bao gồm các khoản tiền gửi tiết kiệm có kỳ hạn, trái phiếu, thương phiếu nắm giữ để thu hồi gốc và lãi. "
                     "Doanh nghiệp theo dõi theo giá trị thu hồi và phân bổ lãi định kỳ vào doanh thu tài chính (TK 515)."),
         "formulas": ["Dự phòng giảm giá CKKD = Max(0, Giá trị sổ sách - Giá thị trường niêm yết)",
                      "Lãi/lỗ chuyển nhượng CKKD = Giá bán thực tế (trừ phí) - Giá gốc bình quân của chứng khoán xuất bán"],
         "case_studies": [{"title": "Công ty Cổ phần Chứng khoán SSI (SSI)", "detail": "Hạch toán danh mục tự doanh chứng khoán niêm yết (FVTPL) và trích lập dự phòng biến động giá thị trường."}]},
        {"sec_num": 2, "sec_title": "Kế Toán Đầu Tư Vào Công Ty Liên Kết Theo Phương Pháp Vốn Chủ Sở Hữu (VAS 08 / IAS 28)",
         "content": ("Công ty liên kết là công ty mà nhà đầu tư có ảnh hưởng đáng kể (thường nắm giữ từ 20% đến dưới 50% quyền biểu quyết), nhưng không có quyền kiểm soát. "
                     "Trên Báo cáo tài chính riêng của công ty mẹ, khoản đầu tư được hạch toán theo Phương pháp Giá gốc (Cost Method - TK 222). "
                     "Cổ tức nhận được hạch toán vào doanh thu hoạt động tài chính (TK 515).\n\n"
                     "Tuy nhiên, trên Báo cáo tài chính hợp nhất, bắt buộc phải áp dụng Phương pháp Vốn chủ sở hữu (Equity Method):\n"
                     "- Khoản đầu tư ban đầu được ghi nhận theo giá gốc.\n"
                     "- Sau ngày mua, giá trị ghi sổ của khoản đầu tư được điều chỉnh tăng tương ứng với phần sở hữu của nhà đầu tư trong lợi nhuận sau thuế của bên nhận đầu tư: "
                     "Nợ TK 222 / Có Doanh thu từ phần sở hữu trong công ty liên kết (trên BCTC hợp nhất).\n"
                     "- Khi nhận cổ tức được chia, giá trị ghi sổ của khoản đầu tư bị giảm xuống (do cổ tức làm giảm tài sản thuần của bên nhận đầu tư): "
                     "Nợ TK 112 / Có TK 222."),
         "formulas": ["Giá trị khoản đầu tư cuối kỳ (Equity Method) = Giá trị đầu kỳ + Phần sở hữu trong Lợi nhuận sau thuế của công ty liên kết - Cổ tức nhận được - Tổn thất suy giảm giá trị"],
         "case_studies": [{"title": "Tập đoàn Hòa Phát (HPG)", "detail": "Hạch toán phần sở hữu vốn tại các công ty liên kết sản xuất nguyên vật liệu và khai thác mỏ quặng theo phương pháp vốn chủ sở hữu."}]}
    ]
    phd3 = {
        "topics": [
            "Kế toán Công cụ Tài chính Phức tạp theo IFRS 9 (Financial Instruments): Phân loại và đo lường theo 3 nhóm danh mục: Giá trị phân bổ (Amortized Cost), Giá trị hợp lý qua OCI (FVOCI) và Giá trị hợp lý qua Lãi/Lỗ (FVTPL).",
            "Lý thuyết Kế toán Phòng ngừa Rủi ro (Hedge Accounting): Áp dụng phòng ngừa rủi ro dòng tiền (Cash Flow Hedge) và phòng ngừa rủi ro giá trị hợp lý (Fair Value Hedge) bằng công cụ phái sinh tiền tệ và hàng hóa.",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về tác động của việc áp dụng IFRS 9 đối với mức độ biến động lợi nhuận và hành vi cho vay của hệ thống ngân hàng thương mại Việt Nam."
        ]
    }
    q3 = [
        "So sánh sự khác nhau căn bản giữa Phương pháp Giá gốc (Cost Method) và Phương pháp Vốn chủ sở hữu (Equity Method) trong hạch toán đầu tư vào công ty liên kết.",
        "Trình bày các tiêu chuẩn phân loại tài sản tài chính theo IFRS 9 dựa trên Mô hình kinh doanh (Business Model Test) và Đặc điểm dòng tiền hợp đồng (SPPI Test).",
        "Xử lý kế toán các khoản trích lập và hoàn nhập dự phòng tổn thất đầu tư tài chính dài hạn theo Thông tư 48/2019/TT-BTC."
    ]
    b.add_chapter(3, "Kế toán Đầu tư Tài chính và Công cụ Tài chính", intro3, sec3, phd3, q3)
    
    # Chương 4
    intro4 = ("Chương 4 tập trung vào chuẩn mực kế toán thuê tài sản - lĩnh vực có sự thay đổi mang tính cách mạng "
              "từ chuẩn mực truyền thống VAS 06 sang chuẩn mực quốc tế IFRS 16 loại bỏ hoàn toàn việc 'giấu nợ ngoại bảng'.")
    sec4 = [
        {"sec_num": 1, "sec_title": "Kế Toán Thuê Tài Sản Theo Chuẩn Mực VAS 06",
         "content": ("Theo VAS 06, thuê tài sản được chia làm hai loại căn cứ vào mức độ chuyển giao rủi ro và lợi ích:\n"
                     "(1) Thuê tài chính (Finance Lease): Là hình thức thuê mà bên cho thuê chuyển giao phần lớn rủi ro và lợi ích gắn liền với quyền sở hữu tài sản cho bên đi thuê. "
                     "Bên đi thuê ghi nhận TSCĐ thuê tài chính (TK 212) và nghĩa vụ nợ thuê tài chính (TK 3412) theo giá trị hiện tại của khoản thanh toán tiền thuê tối thiểu. "
                     "Hàng kỳ, bên đi thuê trích khấu hao TSCĐ thuê và phân bổ chi phí lãi thuê vào chi phí tài chính.\n\n"
                     "(2) Thuê hoạt động (Operating Lease): Là hình thức thuê không phải thuê tài chính. Bên đi thuê không ghi nhận tài sản trên Bảng cân đối kế toán "
                     "mà chỉ ghi nhận tiền thuê phải trả vào chi phí sản xuất kinh doanh theo phương pháp đường thẳng: Nợ TK 641, 642 / Có TK 112, 331."),
         "formulas": ["Giá trị hiện tại của khoản thanh toán tiền thuê (PV) = ∑ [Thanh toán năm t / (1 + r)^t]",
                      "Chi phí lãi thuê mỗi kỳ = Dư nợ gốc đầu kỳ x Lãi suất chiết khấu của hợp đồng thuê"],
         "case_studies": [{"title": "Công ty Cổ phần Vận tải Biển Việt Nam (Vosco - VOS)", "detail": "Hạch toán các hợp đồng thuê mua tàu biển định hạn và thuê tài chính phương tiện vận tải viễn dương."}]},
        {"sec_num": 2, "sec_title": "Cuộc Cách Mạng IFRS 16 và Mô Hình Quyền Sử Dụng Tài Sản (ROU)",
         "content": ("Chuẩn mực IFRS 16 đã xóa bỏ hoàn toàn sự phân biệt giữa thuê tài chính và thuê hoạt động đối với bên đi thuê, "
                     "buộc tất cả các hợp đồng thuê (trừ hợp đồng ngắn hạn dưới 12 tháng hoặc tài sản có giá trị thấp) phải được đưa lên Bảng cân đối kế toán:\n"
                     "- Bên đi thuê ghi nhận Quyền sử dụng tài sản (Right-of-Use Asset - ROU Asset) ở phần Tài sản.\n"
                     "- Đồng thời ghi nhận Nợ thuê tài sản (Lease Liability) ở phần Nợ phải trả theo giá trị hiện tại của các dòng tiền thuê trong tương lai.\n\n"
                     "Tác động lớn đến các chỉ số tài chính:\n"
                     "- Tổng tài sản và Tổng nợ phải trả tăng vọt, làm đòn bẩy tài chính (Debt/Equity) tăng lên.\n"
                     "- Chi phí thuê hoạt động biến mất, thay bằng Chi phí khấu hao ROU và Chi phí lãi vay nợ thuê, "
                     "làm cho chỉ số EBITDA và CFO tăng mạnh nhưng lợi nhuận ròng giai đoạn đầu bị giảm do chi phí dồn về phía trước (Front-loading effect)."),
         "formulas": ["Giá trị ROU Asset ban đầu = Nợ thuê tài sản ban đầu + Các khoản thanh toán trước ngày thuê + Chi phí trực tiếp ban đầu + Chi phí tháo dỡ ước tính",
                      "Thay đổi EBITDA = EBITDA_cũ + Chi phí tiền thuê hoạt động loại trừ"],
         "case_studies": [{"title": "Hàng không Vietjet (VJC)", "detail": "Tác động khổng lồ của IFRS 16 khi đưa toàn bộ đội bay hơn 80 máy bay thuê hoạt động quốc tế lên bảng cân đối kế toán, làm thay đổi quy mô tài sản và nợ vay hàng chục nghìn tỷ đồng."}]}
    ]
    phd4 = {
        "topics": [
            "Lý thuyết Tài trợ Ngoại bảng (Off-Balance-Sheet Financing Theory): Động cơ cấu trúc hợp đồng thuê hoạt động theo chuẩn mực cũ để tránh ghi nhận nợ phải trả và duy trì các chỉ số an toàn tài chính (ROA, Đòn bẩy nợ).",
            "Tác động của IFRS 16 đến Khế ước Nợ và Xếp hạng Tín nhiệm (Credit Rating & Debt Covenants): Phản ứng của các tổ chức xếp hạng tín nhiệm quốc tế (Moody's, S&P) và ngân hàng thương mại khi tái đàm phán các chỉ tiêu tài chính sau áp dụng IFRS 16.",
            "Chuyên đề Tiến sĩ: Kiểm định thực nghiệm sự thay đổi trong hành vi thuê tài sản và chi phí vốn của các tập đoàn bán lẻ đa chi nhánh tại Việt Nam trước và sau khi chuẩn bị áp dụng IFRS 16."
        ]
    }
    q4 = [
        "So sánh tiêu chuẩn phân loại hợp đồng thuê tài chính và thuê hoạt động theo Chuẩn mực Kế toán Việt Nam VAS 06.",
        "Phân tích cơ chế ghi nhận Quyền sử dụng tài sản (ROU Asset) và Nợ thuê tài sản (Lease Liability) theo Chuẩn mực BCTC quốc tế IFRS 16.",
        "Tại sao việc áp dụng IFRS 16 lại làm tăng chỉ tiêu EBITDA và dòng tiền hoạt động kinh doanh (CFO) của doanh nghiệp đi thuê?"
    ]
    b.add_chapter(4, "Kế toán Hoạt động Thuê Tài sản (VAS 06 & IFRS 16)", intro4, sec4, phd4, q4)
    
    # Chương 5
    intro5 = ("Chương 5 là đỉnh cao kỹ thuật của kế toán tài chính: Hợp nhất kinh doanh và lập Báo cáo tài chính hợp nhất. "
              "Chương này trang bị phương pháp xác định lợi thế thương mại, lợi ích cổ đông không kiểm soát và các bút toán loại trừ giao dịch nội bộ.")
    sec5 = [
        {"sec_num": 1, "sec_title": "Hợp Nhất Kinh Doanh và Xác Định Lợi Thế Thương Mại (IFRS 3 / VAS 11)",
         "content": ("Hợp nhất kinh doanh là việc kết hợp các doanh nghiệp riêng biệt thành một đơn vị kinh tế duy nhất do bên mua nắm quyền kiểm soát.\n"
                     "Phương pháp mua (Acquisition Method) được áp dụng bắt buộc gồm các bước:\n"
                     "(1) Xác định bên mua.\n"
                     "(2) Xác định ngày mua (thời điểm bên mua thực tế nắm quyền kiểm soát).\n"
                     "(3) Xác định giá phí hợp nhất kinh doanh (bao gồm tiền, tài sản chuyển giao, cổ phiếu phát hành và các khoản thanh toán tiềm tàng theo giá trị hợp lý).\n"
                     "(4) Đánh giá và ghi nhận tài sản nhận về, nợ phải trả tiếp nhận theo giá trị hợp lý tại ngày mua.\n"
                     "(5) Xác định Lợi thế thương mại (Goodwill) hoặc Lãi từ giao dịch mua rẻ (Bargain Purchase Gain).\n\n"
                     "Lợi ích của cổ đông không kiểm soát (NCI - Non-controlling Interest) phản ánh phần vốn chủ sở hữu trong công ty con "
                     "không thuộc sở hữu trực tiếp hoặc gián tiếp của công ty mẹ."),
         "formulas": ["Lợi thế thương mại (Goodwill) = Giá phí hợp nhất + Giá trị của NCI - Giá trị hợp lý tài sản thuần có thể xác định được của công ty con tại ngày mua",
                      "Lãi từ mua rẻ (Ghi vào Lãi/Lỗ ngay) = Max(0, Giá trị hợp lý tài sản thuần - Giá phí hợp nhất - NCI)"],
         "case_studies": [{"title": "Tập đoàn Vingroup (VIC) thâu tóm VinHomes và Vinpearl", "detail": "Xác định giá phí mua và ghi nhận lợi thế thương mại hàng nghìn tỷ đồng khi sáp nhập các đại dự án bất động sản và nghỉ dưỡng."}]},
        {"sec_num": 2, "sec_title": "Kỹ Thuật Loại Trừ Giao Dịch Nội Bộ Tập Đoàn Khi Lập BCTC Hợp Nhất",
         "content": ("Báo cáo tài chính hợp nhất phản ánh tình hình tài chính của tập đoàn như thể tập đoàn đó là một thực thể kinh doanh duy nhất. "
                     "Do đó, toàn bộ các giao dịch nội bộ giữa các đơn vị trong tập đoàn phải được loại trừ hoàn toàn:\n"
                     "- Loại trừ số dư nội bộ: Nợ phải thu nội bộ (TK 131) đối trừ với Nợ phải trả nội bộ (TK 331); Cho vay nội bộ đối trừ Đi vay nội bộ.\n"
                     "- Loại trừ doanh thu và giá vốn nội bộ: Bút toán Nợ Doanh thu bán hàng / Có Giá vốn hàng bán.\n"
                     "- Loại trừ lãi chưa thực hiện trong hàng tồn kho nội bộ: Nếu hàng mua nội bộ vẫn còn tồn kho cuối kỳ, "
                     "phần lãi nội bộ phải bị loại trừ: Nợ Giá vốn hàng bán / Có Hàng tồn kho.\n"
                     "- Loại trừ lãi/lỗ nội bộ trong giao dịch chuyển nhượng tài sản cố định: Loại bỏ lãi chuyển nhượng và điều chỉnh chi phí khấu hao tương ứng.\n"
                     "- Loại trừ cổ tức nội bộ đã chi trả: Nợ Doanh thu hoạt động tài chính (công ty mẹ) / Có Lợi nhuận sau thuế chưa phân phối (công ty con)."),
         "formulas": ["Lãi nội bộ chưa thực hiện trong hàng tồn kho = Giá trị hàng tồn kho mua nội bộ còn lại cuối kỳ x Tỷ suất lợi nhuận gộp của bên bán nội bộ",
                      "Bút toán loại trừ: Nợ TK 632 / Có TK 156 (Phần lãi chưa thực hiện)"],
         "case_studies": [{"title": "Tập đoàn Masan (MSN) mua lại chuỗi WinCommerce từ Vingroup", "detail": "Quy trình lập BCTC hợp nhất phức tạp loại trừ các giao dịch cung ứng hàng tiêu dùng Masan Consumer vào hệ thống siêu thị WinMart."}]}
    ]
    phd5 = {
        "topics": [
            "Lý thuyết Thực thể Tập đoàn (Entity Concept of Consolidation) so với Lý thuyết Công ty Mẹ (Parent Company Concept): Tranh luận về phương pháp đo lường NCI theo Giá trị hợp lý đầy đủ (Full Goodwill Method) hay theo Tỷ lệ tài sản thuần (Partial Goodwill Method).",
            "Kiểm định Tổn thất Lợi thế Thương mại theo IAS 36 (Goodwill Impairment Testing vs Amortization): Phân tích hành vi trì hoãn trích lập suy giảm giá trị lợi thế thương mại của các nhà điều hành nhằm che giấu thất bại của các thương vụ sáp nhập M&A.",
            "Chuyên đề Tiến sĩ: Tác động của cấu trúc tập đoàn đa sở hữu chéo (Cross-ownership & Pyramid Structure) đến tính minh bạch thông tin tài chính và chi phí đại diện tại Việt Nam."
        ]
    }
    q5 = [
        "Trình bày phương pháp xác định và công thức tính Lợi thế thương mại (Goodwill) trong hợp nhất kinh doanh theo IFRS 3.",
        "Tại sao khi lập Báo cáo tài chính hợp nhất, kế toán bắt buộc phải loại trừ phần lãi chưa thực hiện trong hàng tồn kho mua bán nội bộ?",
        "Phân biệt phương pháp đo lường Lợi ích cổ đông không kiểm soát (NCI) theo Giá trị hợp lý và theo Giá trị tài sản thuần."
    ]
    b.add_chapter(5, "Hợp nhất Kinh doanh và Báo cáo Tài chính Hợp nhất", intro5, sec5, phd5, q5)
    
    # Chương 6
    intro6 = ("Chương 6 hoàn thiện nền tảng kế toán nâng cao với các quy định xử lý thay đổi chính sách kế toán, "
              "ước tính kế toán, sửa chữa sai sót và các sự kiện phát sinh sau ngày kết thúc niên độ kế toán.")
    sec6 = [
        {"sec_num": 1, "sec_title": "Thay Đổi Chính Sách, Ước Tính Kế Toán và Sửa Chữa Sai Sót (VAS 29 / IAS 8)",
         "content": ("- Thay đổi chính sách kế toán: Xảy ra khi có chuẩn mực mới ban hành hoặc doanh nghiệp chủ động chuyển đổi sang chính sách kế toán khác "
                     "nhằm cung cấp thông tin phù hợp và tin cậy hơn (ví dụ: Chuyển đổi phương pháp tính giá hàng tồn kho từ FIFO sang Bình quân gia quyền). "
                     "Áp dụng Hồi tố (Retrospective Application): Coi như chính sách mới đã được áp dụng từ trước, điều chỉnh số dư đầu kỳ của Vốn chủ sở hữu và số liệu so sánh.\n\n"
                     "- Thay đổi ước tính kế toán: Xảy ra khi có các thông tin mới, kinh nghiệm mới làm thay đổi ước tính về thời gian sử dụng TSCĐ, tỷ lệ nợ khó đòi. "
                     "Áp dụng Phi hồi tố (Prospective Application): Ghi nhận ảnh hưởng vào kỳ hiện tại và các kỳ tương lai, không điều chỉnh số liệu quá khứ.\n\n"
                     "- Sai sót kế toán trọng yếu: Các sai sót của các kỳ trước phải được điều chỉnh hồi tố vào BCTC của kỳ phát hiện ra sai sót."),
         "formulas": ["Điều chỉnh hồi tố sai sót = Điều chỉnh số dư đầu kỳ của Tài khoản 421 (Lợi nhuận chưa phân phối) và các tài khoản tài sản/nợ phải trả tương ứng",
                      "Trình bày lại số liệu cột 'Năm trước' trên các báo cáo tài chính để đảm bảo tính so sánh"],
         "case_studies": [{"title": "Công ty Cổ phần Nông nghiệp BAF Việt Nam", "detail": "Xử lý thay đổi ước tính thời gian sử dụng hữu ích của hệ thống trang trại chăn nuôi công nghệ cao theo phương pháp phi hồi tố."}]},
        {"sec_num": 2, "sec_title": "Các Sự Kiện Sau Ngày Kết Thúc Kỳ Kế Toán Năm (VAS 23 / IAS 10)",
         "content": ("Là những sự kiện phát sinh trong khoảng thời gian từ ngày kết thúc kỳ kế toán năm (31/12) đến ngày phát hành Báo cáo tài chính. "
                     "Phân làm hai loại sự kiện:\n"
                     "(1) Sự kiện cần điều chỉnh (Adjusting Events): Những sự kiện cung cấp bằng chứng bổ sung về các tình trạng đã tồn tại tại ngày kết thúc kỳ kế toán "
                     "(ví dụ: Phán quyết của tòa án sau ngày 31/12 xác nhận nghĩa vụ bồi thường của doanh nghiệp; Khách hàng nợ lớn bị tuyên bố phá sản sau ngày 31/12 "
                     "chứng minh khoản nợ đã bị tổn thất từ trước). Doanh nghiệp phải điều chỉnh số liệu trên BCTC trước khi công bố.\n\n"
                     "(2) Sự kiện không cần điều chỉnh (Non-adjusting Events): Những sự kiện chỉ ra các tình trạng phát sinh sau ngày kết thúc kỳ kế toán "
                     "(ví dụ: Cháy nhà xưởng vào tháng 2 năm sau; Sụt giảm mạnh giá trị thị trường của các khoản đầu tư chứng khoán). "
                     "Không điều chỉnh số liệu trên BCTC nhưng bắt buộc phải thuyết minh chi tiết về bản chất sự kiện và ước tính ảnh hưởng tài chính."),
         "formulas": ["Nguyên tắc trọng yếu: Sự kiện làm thay đổi giả định hoạt động liên tục (Going concern) -> Bắt buộc lập lại BCTC trên cơ sở thanh lý"],
         "case_studies": [{"title": "Biến động Dịch Bệnh Đầu Năm 2020", "detail": "Phân loại sự kiện bùng phát đại dịch đầu năm 2020 là sự kiện không cần điều chỉnh đối với BCTC niên độ 2019 nhưng phải thuyết minh rủi ro trọng yếu."}]}
    ]
    phd6 = {
        "topics": [
            "Kế toán Thận trọng và Tính Kịp thời Bất đối xứng của Thu nhập (Accounting Conservatism & Asymmetric Timeliness - Basu 1997 Model): Đo lường mức độ phản ánh tin xấu vào thu nhập kế toán nhanh hơn tin tốt (Bad news is recognized faster than good news).",
            "Mô hình Ball & Shivakumar (2005) về Kế toán Thận trọng của các Doanh nghiệp Tư nhân so với Doanh nghiệp Niêm yết Đại chúng.",
            "Chuyên đề Tiến sĩ: Sử dụng mô hình Machine Learning phát hiện các dấu hiệu chỉnh sửa hồi tố sai sót kế toán bất thường (Financial Restatements) liên quan đến rủi ro kiện tụng và chất lượng kiểm toán độc lập tại Đông Nam Á."
        ]
    }
    q6 = [
        "Phân biệt bản chất và phương pháp xử lý kế toán giữa Thay đổi chính sách kế toán và Thay đổi ước tính kế toán theo chuẩn mực VAS 29.",
        "Trình bày tiêu chuẩn phân loại và các ví dụ thực tiễn về 'Sự kiện cần điều chỉnh' và 'Sự kiện không cần điều chỉnh' theo VAS 23.",
        "Quy trình kỹ thuật điều chỉnh hồi tố một sai sót trọng yếu của năm trước được phát hiện trong năm tài chính hiện hành."
    ]
    b.add_chapter(6, "Kế toán Thay đổi Chính sách, Ước tính Kế toán và Sai sót", intro6, sec6, phd6, q6)
    
    out_dir = os.path.join(BASE_DIR, r"02_Kế toán & Kiểm toán\[NEU] Kế toán tài chính 2 - PGS.TS Nguyễn Phú Giang (NXB ĐHKTQD)")
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Kế toán tài chính 2 - PGS.TS Nguyễn Phú Giang (NXB ĐHKTQD).pdf")
    pages, size_mb = b.save(out_pdf)
    print(f"-> Hoàn thành Sách 3: {pages} trang, {size_mb:.2f} MB. Lưu tại: {out_pdf}")
    return {"book": "Kế toán tài chính 2", "pages": pages, "size_mb": size_mb, "path": out_pdf}


if __name__ == "__main__":
    r1 = build_book_1()
    r2 = build_book_2()
    r3 = build_book_3()
    results = [r1, r2, r3]
    with open(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_agent_2_batch1_res.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("XONG BATCH 1 TOÀN VĂN!")
