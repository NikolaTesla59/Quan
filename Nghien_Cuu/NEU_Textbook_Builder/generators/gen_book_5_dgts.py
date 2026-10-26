# -*- coding: utf-8 -*-
"""
Generator for Textbook 5:
[NEU] Định giá tài sản & Bất động sản - PGS.TS Hoàng Văn Cường (NXB ĐHKTQD)
"""
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_dgts():
    title = "Định giá tài sản & Bất động sản"
    subject_code = "DGTS1102"
    faculty = "Khoa Bất động sản & Kinh tế tài nguyên"
    authors = "PGS.TS. Hoàng Văn Cường & PGS.TS. Trần Kim Chung (Đồng Chủ biên)"
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\01_Tài chính Doanh nghiệp & Đầu tư\[NEU] Định giá tài sản & Bất động sản - PGS.TS Hoàng Văn Cường (NXB ĐHKTQD)"
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Định giá tài sản & Bất động sản - PGS.TS Hoàng Văn Cường (NXB ĐHKTQD).pdf")
    
    b = NEUTextbookBuilder(
        title=title,
        subject_code=subject_code,
        faculty=faculty,
        authors=authors,
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN & BỔ SUNG CHUYÊN SÂU LÝ THUYẾT & THỰC NGHIỆM"
    )
    b.build_cover()
    
    toc_data = [
        {
            "chapter_num": "1",
            "chapter_title": "Cơ sở Lý luận về Giá trị và Bản chất Kinh tế của Định giá Tài sản",
            "topics": [
                "Khái niệm tài sản, phân loại tài sản và nguyên lý kinh tế của giá trị (Giá trị thị trường vs Giá trị phi thị trường)",
                "Các nguyên tắc thẩm định giá tài sản cơ bản: Nguyên tắc sử dụng tốt nhất và hiệu quả nhất (HIGHEST & BEST USE), Thay thế, Cung cầu, Đóng góp",
                "Quy trình thẩm định giá chuẩn mực 6 bước của thẩm định viên chuyên nghiệp",
                "Chuyên đề Tiến sĩ: Cơ sở triết học kinh tế của giá trị (Lý thuyết giá trị lao động vs Thuyết giá trị ích lợi cận biên)"
            ]
        },
        {
            "chapter_num": "2",
            "chapter_title": "Hệ thống Tiêu chuẩn Thẩm định giá Quốc tế (IVS) và Tiêu chuẩn Việt Nam (VVS)",
            "topics": [
                "Cấu trúc khung chuẩn mực của Hội đồng Tiêu chuẩn Thẩm định giá Quốc tế (IVSC)",
                "Hệ thống Tiêu chuẩn Thẩm định giá Việt Nam do Bộ Tài chính ban hành",
                "Đạo đức hành nghề thẩm định giá, tính độc lập khách quan và trách nhiệm pháp lý",
                "Chuyên đề Tiến sĩ: Bất cân xứng thông tin, Rủi ro thông đồng và Xung đột lợi ích trong thẩm định giá thế chấp ngân hàng"
            ]
        },
        {
            "chapter_num": "3",
            "chapter_title": "Các Phương pháp Định giá Tài sản Truyền thống và Ứng dụng",
            "topics": [
                "Phương pháp so sánh (Market Comparison Approach): Thu thập mẫu, điều chỉnh sai biệt và xác định mức giá chỉ dẫn",
                "Phương pháp chi phí (Cost Approach): Chi phí tái tạo, Chi phí thay thế và Đo lường hao mòn (Hao mòn vật chất, lỗi thời chức năng, lỗi thời kinh tế)",
                "Phương pháp thu nhập (Income Approach): Vốn hóa trực tiếp (Direct Capitalization) và Chiết khấu dòng tiền (DCF)",
                "Phương pháp thặng dư (Residual Method): Ứng dụng trong định giá đất phát triển dự án bất động sản",
                "Chuyên đề Tiến sĩ: Tối ưu hóa hàm tham số trong phương pháp so sánh bằng Hồi quy Hedonic"
            ]
        },
        {
            "chapter_num": "4",
            "chapter_title": "Thẩm định giá Bất động sản và Dự án Đầu tư Kinh doanh BĐS",
            "topics": [
                "Đặc điểm kinh tế và pháp lý của hàng hóa bất động sản: Tính bất động, Tính dị biệt, Chu kỳ kinh tế",
                "Định giá quyền sử dụng đất: Bảng giá đất của Nhà nước theo Luật Đất đai 2024 và Định giá đất theo nguyên tắc thị trường",
                "Thẩm định giá tòa nhà văn phòng, trung tâm thương mại, khu công nghiệp và căn hộ chung cư",
                "Chuyên đề Tiến sĩ: Mô hình Kinh tế lượng Không gian (Spatial Econometrics) trong phân tích giá đất đô thị"
            ]
        },
        {
            "chapter_num": "5",
            "chapter_title": "Thẩm định giá Doanh nghiệp và Tài sản Vô hình",
            "topics": [
                "Định giá tài sản vô hình: Bằng sáng chế, Thương hiệu, Phần mềm công nghệ và Lợi thế thương mại (Goodwill)",
                "Các phương pháp định giá tài sản trí tuệ: Miễn trừ tiền bản quyền (Royalty Relief), Lợi nhuận vượt mức (Multi-Period Excess Earnings)",
                "Thẩm định giá doanh nghiệp phục vụ cổ phần hóa, mua bán sáp nhập (M&A) và phát hành chứng khoán",
                "Chuyên đề Tiến sĩ: Định giá tài sản vô hình trong nền kinh tế số và Tác động của ESG đến định giá doanh nghiệp"
            ]
        }
    ]
    b.add_table_of_contents(toc_data)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Cơ sở Lý luận về Giá trị và Bản chất Kinh tế của Định giá Tài sản",
        introduction="Chương 1 cung cấp nền tảng triết học và kinh tế học về khái niệm giá trị tài sản, phân biệt rõ giữa giá cả, chi phí và giá trị, đồng thời phân tích hệ thống các nguyên tắc thẩm định giá chuẩn mực.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Khái niệm tài sản và bản chất kinh tế của giá trị",
                "content": (
                    "Tài sản dưới góc độ kinh tế và pháp lý là các nguồn lực thuộc quyền sở hữu hoặc quyền kiểm soát của một chủ thể, "
                    "có khả năng đem lại lợi ích kinh tế trong tương lai. Thẩm định giá (Valuation) là nghệ thuật và khoa học xác định giá trị thị trường "
                    "của tài sản tại một thời điểm nhất định, cho một mục đích cụ thể, trong điều kiện một thị trường xác định.\n\n"
                    "Cần phân biệt rạch ròi ba khái niệm: Chi phí (Cost - số tiền thực tế đã chi ra để tạo ra tài sản trong quá khứ); "
                    "Giá cả (Price - số tiền được thỏa thuận trong một giao dịch mua bán cụ thể); và Giá trị (Value - sự đánh giá bằng tiền về lợi ích "
                    "mà tài sản mang lại cho chủ sở hữu trong tương lai)."
                ),
                "formulas": [
                    "Định nghĩa Giá trị Thị trường theo IVS: Market Value là số tiền ước tính mà tài sản có thể được trao đổi tại ngày thẩm định giá giữa người mua sẵn sàng mua và người bán sẵn sàng bán trong một giao dịch khách quan độc lập sau khi đã tiếp thị thích hợp.",
                    "Giá trị phi thị trường bao gồm: Giá trị đầu tư (Investment Value), Giá trị đặc biệt (Special Value), Giá trị thanh lý (Liquidation Value)"
                ],
                "case_studies": [
                    {
                        "title": "Tranh chấp giữa chi phí đầu tư lịch sử và giá trị thị trường",
                        "detail": "Nhiều dự án công nghiệp cũ có chi phí xây dựng ban đầu rất cao nhưng giá trị thị trường tại thời điểm thẩm định lại rất thấp do máy móc thiết bị đã bị lỗi thời chức năng và công nghệ lạc hậu."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Hệ thống các nguyên tắc thẩm định giá tài sản",
                "content": (
                    "Các nguyên tắc thẩm định giá là kim chỉ nam cho mọi kết luận của thẩm định viên: "
                    "1. Nguyên tắc Sử dụng Tốt nhất và Hiệu quả nhất (Highest and Best Use - HBU): Tài sản phải được định giá theo phương án sử dụng hợp pháp, "
                    "khả thi về mặt vật chất, được hỗ trợ về mặt tài chính và mang lại giá trị hiện tại cao nhất;\n\n"
                    "2. Nguyên tắc Thay thế (Substitution): Người mua có lý trí sẽ không trả giá cao hơn chi phí để sở hữu một tài sản thay thế tương đương; "
                    "3. Nguyên tắc Đóng góp (Contribution): Giá trị của một bộ phận tài sản phụ thuộc vào mức độ nó đóng góp vào tổng giá trị toàn bộ tài sản; "
                    "4. Nguyên tắc Cung cầu và Dự báo biến động thị trường."
                ),
                "formulas": [
                    "Nguyên tắc HBU: Value(HBU) = max_i [ Present Value(Alternative_i) ]",
                    "Điều kiện HBU: Hợp pháp (Legally Permissible) AND Vật lý khả thi (Physically Possible) AND Tài chính khả thi (Financially Feasible)"
                ],
                "case_studies": [
                    {
                        "title": "Áp dụng nguyên tắc HBU định giá khu đất vàng trung tâm Hà Nội",
                        "detail": "Một lô đất đang được sử dụng làm nhà kho cũ trên phố đi bộ Hoàn Kiếm khi định giá chuyển nhượng bắt buộc phải áp dụng nguyên tắc HBU chuyển đổi sang mô hình khách sạn boutique cao cấp hoặc trung tâm thương mại dịch vụ cao tầng."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Cơ sở Bản thể luận của Giá trị: So sánh Thuyết Giá trị Lao động cổ điển (Ricardo, Marx) và Thuyết Tiện ích Cận biên (Jevons, Menger, Walras) trong bối cảnh định giá tài sản hiện đại.",
                "Thuyết Đấu giá (Auction Theory) của Vickrey (1961) và Xác định Giá trị Tài sản trong Điều kiện Thông tin Riêng tư.",
                "Tác động của Định chế Quản trị Đất đai (Land Governance Institutions) đến Sự Phân kỳ giữa Giá trị Sử dụng (Use Value) và Giá trị Trao đổi (Exchange Value)."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt bản chất giữa ba khái niệm: Chi phí, Giá cả và Giá trị của tài sản?",
            "Trình bày bốn điều kiện bắt buộc để một phương án sử dụng đất được công nhận là Sử dụng tốt nhất và hiệu quả nhất (HBU)?",
            "Mô hình đấu giá Vickrey (Second-price sealed-bid auction) có ý nghĩa như thế nào trong việc bộc lộ mức giá trị sẵn lòng chi trả thực sự của người mua tài sản?"
        ]
    )
    
    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Hệ thống Tiêu chuẩn Thẩm định giá Quốc tế (IVS) và Tiêu chuẩn Việt Nam (VVS)",
        introduction="Chương 2 phân tích khung khổ pháp lý và kỹ thuật của Tiêu chuẩn Thẩm định giá Quốc tế (IVS) và Tiêu chuẩn Thẩm định giá Việt Nam (VVS), thiết lập chuẩn mực đạo đức và kiểm soát xung đột lợi ích của thẩm định viên.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Cấu trúc Tiêu chuẩn Thẩm định giá Quốc tế (IVS)",
                "content": (
                    "Hội đồng Tiêu chuẩn Thẩm định giá Quốc tế (IVSC) ban hành IVS nhằm tạo lập một ngôn ngữ định giá thống nhất toàn cầu, "
                    "tăng cường sự minh bạch và tin cậy cho thị trường tài chính và báo cáo tài chính quốc tế (IFRS). "
                    "Khung IVS gồm hai phần chính: Các tiêu chuẩn chung (General Standards: IVS 101 Phạm vi công việc, IVS 102 Điều tra và Tuân thủ, "
                    "IVS 103 Báo cáo, IVS 104 Cơ sở giá trị, IVS 105 Cách tiếp cận và phương pháp định giá);\n\n"
                    "và Các tiêu chuẩn tài sản cụ thể (Asset Standards: Bất động sản, Doanh nghiệp, Công cụ tài chính, Tài sản vô hình, Nhà xưởng thiết bị)."
                ),
                "formulas": [
                    "Quy trình tuân thủ: Scope of Work -> Investigation -> Valuation Approaches -> Valuation Report (Phải nêu rõ Hạn chế và Giả định đặc biệt)"
                ],
                "case_studies": [
                    {
                        "title": "Hội nhập tiêu chuẩn quốc tế IVS của các công ty thẩm định giá đa quốc gia tại Việt Nam",
                        "detail": "Các đơn vị tư vấn như CBRE, JLL, Savills, Cushman & Wakefield tuân thủ nghiêm ngặt IVS và chuẩn RICS (Vương quốc Anh) khi phát hành chứng thư định giá cho các quỹ đầu tư ngoại và giao dịch M&A xuyên biên giới."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Chuẩn mực Thẩm định giá Việt Nam và Đạo đức Nghề nghiệp",
                "content": (
                    "Luật Giá 2023 và hệ thống Chuẩn mực Thẩm định giá Việt Nam do Bộ Tài chính ban hành quy định điều kiện cấp thẻ thẩm định viên về giá, "
                    "nguyên tắc lập hồ sơ chứng thư thẩm định giá và chế tài xử lý vi phạm pháp luật.\n\n"
                    "Đạo đức hành nghề đòi hỏi sự độc lập tuyệt đối: Thẩm định viên không được có lợi ích tài chính trực tiếp hoặc gián tiếp đối với tài sản được thẩm định; "
                    "nghiêm cấm hành vi thỏa thuận trước giá trị thẩm định với khách hàng hoặc thông đồng nâng khống giá trị tài sản thế chấp để trục lợi giải ngân ngân hàng."
                ),
                "formulas": [
                    "Trách nhiệm dân sự và hình sự: Thẩm định viên chịu trách nhiệm cá nhân trước pháp luật về tính trung thực và khách quan của kết quả thẩm định giá."
                ],
                "case_studies": [
                    {
                        "title": "Xử lý nghiêm các sai phạm thẩm định giá tài sản trong các đại án kinh tế",
                        "detail": "Cơ quan tố tụng đã khởi tố nhiều lãnh đạo và thẩm định viên của các công ty thẩm định giá do có hành vi thông đồng, phát hành chứng thư thẩm định giá nâng khống hàng chục lần giá trị bất động sản phục vụ phát hành trái phiếu và vay vốn ngân hàng."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Trò chơi về Độc lập của Thẩm định viên: Mô hình Collusion giữa Thẩm định viên (Appraiser) và Bên đi vay (Borrower) trong điều kiện cạnh tranh phí thẩm định.",
                "Rủi ro Thổi phồng Giá trị Thẩm định (Appraisal Inflation) trong Khủng hoảng Cho vay Dưới chuẩn theo Ben-David (2011).",
                "Khuôn khổ Thể chế và Hiệu lực Thực thi Pháp luật Định giá Tài sản Công trong Tiến trình Cổ phần hóa Doanh nghiệp Nhà nước."
            ]
        },
        review_questions=[
            "Trình bày cấu trúc hệ thống Tiêu chuẩn Thẩm định giá Quốc tế (IVS) và sự tương thích của Tiêu chuẩn Thẩm định giá Việt Nam hiện hành?",
            "Phân tích nguyên tắc độc lập và khách quan của thẩm định viên về giá, chỉ ra các tình huống xung đột lợi ích bắt buộc phải từ chối thẩm định?",
            "Xây dựng mô hình lý thuyết thông tin giải thích hiện tượng thổi phồng giá trị thẩm định tài sản thế chấp trong chu kỳ bùng nổ tín dụng?"
        ]
    )
    
    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Các Phương pháp Định giá Tài sản Truyền thống và Ứng dụng",
        introduction="Chương 3 trình bày chi tiết thuật toán tính toán và điều kiện áp dụng của bốn phương pháp định giá tài sản kinh điển: Phương pháp So sánh, Phương pháp Chi phí, Phương pháp Thu nhập và Phương pháp Thặng dư.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phương pháp so sánh và phương pháp chi phí",
                "content": (
                    "Phương pháp so sánh (Market Comparison Approach) là phương pháp phổ biến và trực quan nhất, "
                    "xác định giá trị tài sản mục tiêu bằng cách phân tích mức giá của các tài sản tương tự đã giao dịch thành công trên thị trường, "
                    "sau đó thực hiện điều chỉnh các yếu tố sai biệt (vị trí, quy mô, tình trạng pháp lý, thời điểm giao dịch).\n\n"
                    "Phương pháp chi phí (Cost Approach) ước tính giá trị tài sản bằng Chi phí tái tạo (Reproduction Cost) "
                    "hoặc Chi phí thay thế (Replacement Cost) của tài sản trừ đi Tổng mức hao mòn lũy kế (Physical Deterioration + Functional Obsolescence + External Obsolescence) "
                    "rồi cộng với giá trị của quyền sử dụng đất."
                ),
                "formulas": [
                    "Phương pháp So sánh: P_target = P_comp +/- sum (Điều chỉnh sai biệt yếu tố k)",
                    "Phương pháp Chi phí: V_property = V_land + (Replacement Cost New - Total Depreciation)",
                    "Hao mòn lũy kế theo tuổi thọ kinh tế: Depr = (Effective Age / Total Economic Life) * Replacement Cost"
                ],
                "case_studies": [
                    {
                        "title": "Định giá nhà xưởng công nghiệp tại Khu công nghiệp VSIP",
                        "detail": "Áp dụng phương pháp chi phí thay thế kết hợp chiết khấu hao mòn kết cấu thép tiền chế và hệ thống xử lý nước thải để xác định giá trị chuyển nhượng tài sản trên đất thuê."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Phương pháp thu nhập và phương pháp thặng dư",
                "content": (
                    "Phương pháp thu nhập (Income Approach) dựa trên nguyên lý chuyển đổi dòng thu nhập ròng trong tương lai thành giá trị hiện tại. "
                    "Hai kỹ thuật cơ bản gồm: Vốn hóa trực tiếp (Direct Capitalization: chia thu nhập hoạt động ròng năm đầu NOI cho tỷ suất vốn hóa Cap Rate); "
                    "và Chiết khấu dòng tiền (DCF: chiết khấu dòng tiền tự do từng năm theo tỷ suất chiết khấu phù hợp có tính đến giá trị thu hồi cuối kỳ).\n\n"
                    "Phương pháp thặng dư (Residual Method) thường dùng để xác định giá trị đất thô dự án: Lấy tổng doanh thu phát triển giả định của dự án sau khi hoàn thành "
                    "trừ đi toàn bộ chi phí đầu tư phát triển (xây dựng, lãi vay, thuế, lợi nhuận kỳ vọng của nhà phát triển)."
                ),
                "formulas": [
                    "Vốn hóa trực tiếp: Value = NOI / Cap_Rate",
                    "Thu nhập hoạt động ròng: NOI = Tiềm năng doanh thu gộp (PGI) - Tỷ lệ trống (V&C) - Chi phí vận hành (Opex)",
                    "Phương pháp thặng dư: V_land = Tổng giá trị phát triển (GDV) - Chi phí phát triển - Chi phí tài chính - Lợi nhuận nhà phát triển"
                ],
                "case_studies": [
                    {
                        "title": "Định giá tòa tháp văn phòng hạng A tại Quận 1, TP.HCM",
                        "detail": "Áp dụng phương pháp DCF 10 năm với giá thuê 45 USD/m2/tháng, tỷ lệ lấp đầy ổn định 92%, Cap Rate đầu ra 6.8% và tỷ suất chiết khấu WACC là 9.5%."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Giá Định danh Hedonic (Hedonic Price Model) của Rosen (1974): Tách bạch mức giá sẵn lòng chi trả biên (Marginal Willingness to Pay) cho từng đặc tính vi mô của bất động sản.",
                "Ước lượng Tỷ suất Vốn hóa (Cap Rate) Động trong Mô hình Vector Error Correction (VECM) gắn với lãi suất danh nghĩa và lạm phát.",
                "Phương pháp Tùy chọn Thực (Real Options) Định giá Quyền Trì hoãn Phát triển Đất Dự án (Land Development as a Call Option on Completed Building)."
            ]
        },
        review_questions=[
            "Trình bày bảng ma trận điều chỉnh các yếu tố so sánh trong phương pháp so sánh trực tiếp đối với bất động sản thổ cư?",
            "Phân tích ba loại hao mòn trong phương pháp chi phí và giải thích tại sao hao mòn kinh tế (External Obsolescence) thường không thể khắc phục được?",
            "Thiết lập mô hình Hedonic hồi quy giá bán căn hộ chung cư theo diện tích, tầng cao, khoảng cách tới ga metro và các tiện ích nội khu?"
        ]
    )
    
    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Thẩm định giá Bất động sản và Dự án Đầu tư Kinh doanh BĐS",
        introduction="Chương 4 tập trung vào thị trường bất động sản, phân tích chính sách đất đai theo Luật Đất đai 2024, phương pháp định giá đất cụ thể và kỹ thuật thẩm định dòng tiền dự án khu đô thị phức hợp.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Đặc điểm thị trường bất động sản và khung pháp lý Luật Đất đai 2024",
                "content": (
                    "Bất động sản là hàng hóa đặc biệt có tính cố định vị trí địa lý, tính độc nhất (không có hai thửa đất giống hệt nhau), "
                    "tính bền vững lâu dài và chịu sự điều tiết chặt chẽ của quy hoạch nhà nước. "
                    "Luật Đất đai 2024 đã bãi bỏ khung giá đất cũ của Chính phủ, chuyển sang Bảng giá đất do UBND cấp tỉnh ban hành hàng năm "
                    "được xây dựng theo nguyên tắc thị trường khách quan.\n\n"
                    "Bốn phương pháp định giá đất được luật định rõ ràng: Phương pháp So sánh, Phương pháp Thu nhập, Phương pháp Thặng dư "
                    "và Phương pháp Hệ số điều chỉnh giá đất (K-factor)."
                ),
                "formulas": [
                    "Định giá đất theo hệ số K: Giá đất = Giá đất trong Bảng giá đất * Hệ số điều chỉnh K",
                    "Tỷ suất sinh lời kỳ vọng phát triển BĐS: IRR_project >= WACC + Risk_Premium (thường từ 15-20%)"
                ],
                "case_studies": [
                    {
                        "title": "Tác động của việc bãi bỏ khung giá đất đến chi phí giải phóng mặt bằng",
                        "detail": "Khi giá đất bồi thường tiệm cận sát giá thị trường giao dịch thực tế, quyền lợi của người dân bị thu hồi đất được bảo đảm tốt hơn, nhưng tổng mức đầu tư dự án hạ tầng tăng lên, đòi hỏi năng lực thẩm định giá đất cụ thể phải chuẩn xác và minh bạch."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Thẩm định giá dự án phát triển khu đô thị phức hợp",
                "content": (
                    "Dự án khu đô thị phức hợp bao gồm nhiều phân khu chức năng: Đất ở thấp tầng (biệt thự, liền kề), chung cư cao tầng, "
                    "thương mại dịch vụ và công trình tiện ích công cộng. Thẩm định giá dự án đòi hỏi lập mô hình tài chính phân kỳ đầu tư (Phasing Schedule), "
                    "dự báo tiến độ bán hàng (Absorption Rate) và giá bán tăng trưởng theo từng giai đoạn.\n\n"
                    "Thẩm định viên phải kiểm tra kỹ lưỡng các điều kiện pháp lý tiên quyết: Phê duyệt quy hoạch 1/500, Quyết định giao đất, "
                    "Báo cáo đánh giá tác động môi trường và Giấy phép xây dựng."
                ),
                "formulas": [
                    "Tổng diện tích sàn thương phẩm: Net Saleable Area (NSA) = Gross Floor Area (GFA) * Efficiency Ratio (78-85%)",
                    "Hệ số sử dụng đất: FAR = Tổng diện tích sàn xây dựng / Tổng diện tích lô đất"
                ],
                "case_studies": [
                    {
                        "title": "Thẩm định giá dự án Đại đô thị Vinhomes Ocean Park",
                        "detail": "Dự án quy mô 420 ha áp dụng mô hình phân kỳ dòng tiền 7 năm, tích hợp hệ thống tiện ích biển hồ nhân tạo tạo giá trị gia tăng đột phá cho giá bán các phân khu căn hộ và shophouse mở bán sau."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Kinh tế lượng Không gian (Spatial Econometrics): Mô hình Tự hồi quy Không gian (SAR) và Mô hình Sai số Không gian (SEM) kiểm soát tương tác láng giềng trong giá bất động sản theo Anselin (1988).",
                "Đo lường Bong bóng Bất động sản và Sự Đứt gãy Giá cả: Kiểm định Bong bóng Bùng nổ (Explosive Bubble Test) GSADF của Phillips, Shi & Yu (2015).",
                "Chính sách Thuế Tài sản Đất đai và Cân bằng Không gian Đô thị theo Mô hình Alonso-Muth-Mills."
            ]
        },
        review_questions=[
            "Phân tích những điểm đột phá về cơ chế định giá đất theo thị trường trong Luật Đất đai 2024 so với Luật Đất đai 2013?",
            "Trình bày các bước lập mô hình dòng tiền chiết khấu (DCF) để thẩm định giá trị đất thô dự án bằng phương pháp thặng dư?",
            "Thiết lập mô hình Spatial Autoregressive (SAR) với ma trận khoảng cách không gian (Spatial Weight Matrix W) để đánh giá ngoại ứng hạ tầng metro đến giá nhà đất?"
        ]
    )
    
    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Thẩm định giá Doanh nghiệp và Tài sản Vô hình",
        introduction="Chương 5 hoàn thiện giáo trình với lĩnh vực thẩm định giá doanh nghiệp và tài sản vô hình (thương hiệu, bằng sáng chế), tích hợp các chuẩn mực báo cáo tài chính quốc tế IFRS 3 và IFRS 13.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phương pháp định giá tài sản vô hình và tài sản trí tuệ",
                "content": (
                    "Trong nền kinh tế tri thức và công nghệ số, tài sản vô hình (Intangible Assets) chiếm tới 70-80% tổng giá trị thị trường của các doanh nghiệp hàng đầu. "
                    "Các loại tài sản vô hình chủ yếu gồm: Tài sản sở hữu trí tuệ (Bằng phát minh sáng chế, bản quyền phần mềm, nhãn hiệu thương hiệu), "
                    "Mối quan hệ khách hàng và Hợp đồng độc quyền kinh doanh.\n\n"
                    "Ba phương pháp định giá tài sản vô hình chủ yếu: Phương pháp Miễn trừ bản quyền (Relief-from-Royalty: vốn hóa khoản phí bản quyền tiết kiệm được "
                    "khi doanh nghiệp tự sở hữu thương hiệu thay vì phải thuê ngoài); Phương pháp Lợi nhuận vượt mức đa kỳ (MPEEM); "
                    "và Phương pháp Chi phí tạo lập mới."
                ),
                "formulas": [
                    "Phương pháp Relief-from-Royalty: Value_brand = sum_{t=1}^T [ (Revenue_t * Royalty_Rate * (1 - t_c)) / (1 + r)^t ] + Terminal Value",
                    "Phân bổ giá mua M&A (PPA theo IFRS 3): Goodwill = Giá mua doanh nghiệp - Hợp lý tài sản thuần có thể nhận biết"
                ],
                "case_studies": [
                    {
                        "title": "Định giá thương hiệu Viettel và Vinamilk theo Brand Finance",
                        "detail": "Brand Finance áp dụng phương pháp Relief-from-Royalty định giá thương hiệu Viettel đạt gần 9 tỷ USD và Vinamilk đạt gần 3 tỷ USD, khẳng định vị thế thương hiệu quốc gia dẫn đầu khu vực ASEAN."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Thẩm định giá doanh nghiệp phục vụ cổ phần hóa và M&A",
                "content": (
                    "Thẩm định giá doanh nghiệp xác định toàn bộ giá trị vốn chủ sở hữu và giá trị doanh nghiệp (Enterprise Value). "
                    "Phương pháp tài sản (Asset-based approach) định giá lại toàn bộ danh mục tài sản có và tài sản nợ theo giá thị trường; "
                    "Phương pháp chiết khấu dòng tiền (DCF) phản ánh khả năng sinh lợi nội tại; "
                    "và Phương pháp so sánh thị trường sử dụng các bội số giao dịch (P/E, P/B, EV/EBITDA, EV/Sales) của các công ty tương đồng cùng ngành.\n\n"
                    "Nghị định của Chính phủ về cổ phần hóa doanh nghiệp nhà nước yêu cầu bắt buộc phải tính đúng, tính đủ giá trị lợi thế vị trí địa lý "
                    "của các khu đất thuê và giá trị thương hiệu vào giá trị khởi điểm chào bán cổ phần nhà nước."
                ),
                "formulas": [
                    "Giá trị vốn chủ sở hữu phương pháp tài sản: Equity Value = Tổng tài sản đánh giá lại theo thị trường - Tổng nợ phải trả",
                    "Bội số EV/EBITDA: Target_EV = Peer_Median(EV/EBITDA) * Target_EBITDA"
                ],
                "case_studies": [
                    {
                        "title": "Thương vụ Nhà nước thoái vốn tại Sabeco (SAB) cho ThaiBev",
                        "detail": "Bộ Công Thương áp dụng phương pháp định giá kết hợp dựng sổ quốc tế, thoái vốn thành công 53.59% cổ phần Sabeco với mức giá kỷ lục 320,000 VND/cổ phiếu, thu về gần 5 tỷ USD cho ngân sách nhà nước."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Định giá Tài sản Vô hình của Baruch Lev (2001): Đo lường Phần vốn Trí tuệ (Knowledge Capital) và Lợi nhuận Siêu ngạch (Abnormal Returns).",
                "Tác động của Xếp hạng ESG (Environmental, Social, Governance) đến Phần bù Chi phí Vốn và Bội số Định giá Doanh nghiệp.",
                "Định giá Công ty Khởi nghiệp Công nghệ (Tech Startups) bằng Phương pháp First Chicago và Mô phỏng Đa trạng thái Markov."
            ]
        },
        review_questions=[
            "Phân tích nguyên lý định giá thương hiệu theo phương pháp Miễn trừ bản quyền (Relief-from-Royalty)?",
            "Tại sao phương pháp giá trị tài sản thuần (NAV) thường đánh giá thấp giá trị của các doanh nghiệp công nghệ so với phương pháp DCF?",
            "Trình bày mô hình kinh tế lượng đo lường tác động của điểm số ESG đến hệ số P/B của các doanh nghiệp niêm yết trong chỉ số VNSI?"
        ]
    )
    
    pages, sz = b.save(out_pdf)
    print(f"[SUCCESS] Book 5 saved: {out_pdf} ({pages} pages, {sz:.2f} MB)")
    return {
        "title": title,
        "code": subject_code,
        "author": authors,
        "path": out_pdf,
        "pages": pages,
        "size_mb": round(sz, 2)
    }

if __name__ == "__main__":
    build_dgts()
