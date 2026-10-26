# -*- coding: utf-8 -*-
"""
Generator for Textbook 4:
[NEU] Tài chính tiền tệ - PGS.TS Nguyễn Đăng Dốt (NXB ĐHKTQD)
"""
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_tctt():
    title = "Tài chính tiền tệ"
    subject_code = "TCTT1101"
    faculty = "Viện Ngân hàng - Tài chính"
    authors = "PGS.TS. Nguyễn Đăng Dốt & PGS.TS. Nguyễn Hữu Tài (Đồng Chủ biên)"
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\01_Tài chính Doanh nghiệp & Đầu tư\[NEU] Tài chính tiền tệ - PGS.TS Nguyễn Đăng Dốt (NXB ĐHKTQD)"
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Tài chính tiền tệ - PGS.TS Nguyễn Đăng Dốt (NXB ĐHKTQD).pdf")
    
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
            "chapter_title": "Bản chất, Chức năng của Tiền tệ và Hệ thống Tiền tệ Quốc tế",
            "topics": [
                "Nguồn gốc phát sinh, bản chất và sự tiến hóa của các hình thái tiền tệ (Từ tiền hàng hóa đến Tiền kỹ thuật số CBDC)",
                "Ba chức năng kinh tế cốt lõi của tiền tệ: Thước đo giá trị, Phương tiện lưu thông, Phương tiện tích lũy",
                "Chế độ tiền tệ (Bản vị vàng, Bản vị tiền giấy pháp định Fiat Money) và Khối tiền tệ (M0, M1, M2, M3)",
                "Chuyên đề Tiến sĩ: Lý thuyết Tiền tệ Tối ưu của Friedman và Mô hình Tiền tệ Hóa (Search-Theoretic Approach to Money)"
            ]
        },
        {
            "chapter_num": "2",
            "chapter_title": "Thị trường Tài chính và Các Định chế Tài chính Trung gian",
            "topics": [
                "Cấu trúc hệ thống tài chính: Thị trường tiền tệ, Thị trường vốn và Kênh dẫn vốn trực tiếp/gián tiếp",
                "Lý thuyết trung gian tài chính: Giảm thiểu chi phí giao dịch và khắc phục bất cân xứng thông tin (Lựa chọn đối nghịch & Rủi ro đạo đức)",
                "Hệ thống các định chế nhận tiền gửi, định chế tiết kiệm theo hợp đồng và định chế đầu tư",
                "Chuyên đề Tiến sĩ: Mô hình Diamond-Dybvig (1983) về Đột biến rút tiền gửi (Bank Runs) và Bảo hiểm tiền gửi"
            ]
        },
        {
            "chapter_num": "3",
            "chapter_title": "Ngân hàng Trung ương, Cung - Cầu Tiền tệ và Cơ chế Tạo Tiền",
            "topics": [
                "Vị trí pháp lý, chức năng của NHTW và vai trò Người cho vay cứu cánh cuối cùng (Lender of Last Resort)",
                "Bảng cân đối tiền tệ của NHTW và lượng tiền cơ sở (Monetary Base - MB / High-powered Money)",
                "Quá trình mở rộng tiền gửi của hệ thống NHTM và hệ số nhân tiền tệ (Money Multiplier)",
                "Chuyên đề Tiến sĩ: Tính nội sinh của tiền tệ (Endogenous Money) và Mô hình Cân bằng Đa thị trường Tiền tệ"
            ]
        },
        {
            "chapter_num": "4",
            "chapter_title": "Lãi suất, Lạm phát và Cấu trúc Kỳ hạn của Lãi suất",
            "topics": [
                "Bản chất của lãi suất và các lý thuyết xác định lãi suất (Lý thuyết Quỹ cho vay và Lý thuyết Ưa thích thanh khoản Keynes)",
                "Hiệu ứng Fisher về lãi suất danh nghĩa, lãi suất thực và lạm phát kỳ vọng",
                "Cấu trúc kỳ hạn của lãi suất: Lý thuyết Kỳ vọng thuần túy, Lý thuyết Thị trường phân đoạn và Lý thuyết Phần bù thanh khoản",
                "Chuyên đề Tiến sĩ: Mô hình Cấu trúc Kỳ hạn Lãi suất Không Chênh lệch (No-Arbitrage Affine Term Structure Models)"
            ]
        },
        {
            "chapter_num": "5",
            "chapter_title": "Chính sách Tiền tệ: Mục tiêu, Công cụ và Cơ chế Truyền dẫn Vĩ mô",
            "topics": [
                "Mục tiêu tối thượng (Kiểm soát lạm phát, Tăng trưởng, Việc làm) và Mục tiêu trung gian (M2, Lãi suất liên ngân hàng)",
                "Hệ thống công cụ điều hành: Nghiệp vụ thị trường mở (OMO), Tái cấp vốn / Tái chiết khấu, Tỷ lệ dự trữ bắt buộc",
                "Các kênh truyền dẫn chính sách tiền tệ: Kênh lãi suất, Kênh tín dụng ngân hàng, Kênh tỷ giá và Kênh giá tài sản",
                "Chuyên đề Tiến sĩ: Mô hình New Keynesian DSGE với Quy tắc Taylor (Taylor Rule) và Bẫy Thanh khoản (Zero Lower Bound)"
            ]
        },
        {
            "chapter_num": "6",
            "chapter_title": "Khủng hoảng Tài chính Tiền tệ và Chính sách An toàn Vĩ mô (Macroprudential)",
            "topics": [
                "Giải phẫu các cuộc khủng hoảng tài chính toàn cầu: Từ Khủng hoảng châu Á 1997 đến Đại suy thoái 2008 và Khủng hoảng Ngân hàng 2023",
                "Chính sách an toàn vĩ mô (Macroprudential Policy) và Bộ đệm vốn chống chu kỳ (CCyB)",
                "Kiểm soát rủi ro hệ thống, bong bóng tài sản và phối hợp chính sách tài khóa - tiền tệ tại Việt Nam",
                "Chuyên đề Tiến sĩ: Vòng xoáy Thanh khoản Brunnermeier & Pedersen (2009) và Mô hình Mạng lưới Rủi ro Lan truyền Hệ thống"
            ]
        }
    ]
    b.add_table_of_contents(toc_data)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Bản chất, Chức năng của Tiền tệ và Hệ thống Tiền tệ Quốc tế",
        introduction="Chương 1 làm sáng tỏ cội nguồn phát sinh của tiền tệ, phân tích quá trình chuyển hóa từ tiền hàng hóa sơ khai sang tiền pháp định và tiền kỹ thuật số của Ngân hàng Trung ương (CBDC), đồng thời xác định các khối tiền tệ phục vụ điều hành vĩ mô.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bản chất và sự tiến hóa của các hình thái tiền tệ",
                "content": (
                    "Tiền tệ là một phát minh vĩ đại của nền văn minh nhân loại, giải quyết triệt để sự trùng hợp ngẫu nhiên về nhu cầu (Double Coincidence of Wants) "
                    "trong nền kinh tế đổi chác hàng - hàng sơ khai. Sự tiến hóa của tiền tệ trải qua bốn nấc thang lịch sử: Tiền hàng hóa (vàng, bạc, kim loại quý), "
                    "Tiền danh nghĩa quy ước (tiền giấy có khả năng đổi ra vàng), Tiền pháp định (Fiat Money - tiền giấy bất khả hoán do Nhà nước bảo hộ pháp lý), "
                    "và Tiền điện tử, tiền kỹ thuật số (Digital Currency, CBDC).\n\n"
                    "Dù dưới hình thái nào, tiền tệ vẫn giữ nguyên bản chất là vật ngang giá chung, đại biểu cho một lượng giá trị xã hội nhất định "
                    "và được cộng đồng thừa nhận rộng rãi."
                ),
                "formulas": [
                    "Quy luật lưu thông tiền tệ của Karl Marx: M = (P * Q - Giao dịch bù trừ + Nợ đến hạn) / V",
                    "Phương trình trao đổi Fisher: M * V = P * Y"
                ],
                "case_studies": [
                    {
                        "title": "Nghiên cứu triển khai Tiền kỹ thuật số Ngân hàng Trung ương (CBDC) tại Việt Nam",
                        "detail": "Ngân hàng Nhà nước Việt Nam (NHNN) thành lập tổ công tác chuyên trách nghiên cứu thí điểm CBDC nhằm thúc đẩy thanh toán không dùng tiền mặt, tăng tính bao trùm tài chính và bảo vệ chủ quyền tiền tệ số quốc gia."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Hệ thống tiền tệ và các phép đo khối tiền",
                "content": (
                    "Chế độ tiền tệ quốc gia quy định đơn vị tiền tệ tiêu chuẩn, thể thức đúc tiền, phát hành tiền giấy và chế độ bảo đảm giá trị đồng tiền. "
                    "Để điều hành chính sách tiền tệ, các NHTW phân chia cung tiền thành các khối tiền tệ (Monetary Aggregates) theo mức độ thanh khoản giảm dần: "
                    "M0 (Tiền mặt lưu hành ngoài hệ thống ngân hàng); M1 (M0 + Tiền gửi thanh toán không kỳ hạn); M2 (M1 + Tiền gửi tiết kiệm, có kỳ hạn);\n\n"
                    "Tại Việt Nam, M2 là mục tiêu trung gian chủ yếu được NHNN giám sát chặt chẽ nhằm duy trì lạm phát mục tiêu dưới 4-4.5% hàng năm."
                ),
                "formulas": [
                    "Khối tiền giao dịch M1 = Currency + Demand Deposits",
                    "Khối tiền mở rộng M2 = M1 + Time Deposits + Savings Deposits",
                    "Tốc độ lưu thông tiền tệ: V = (Nominal GDP) / M2"
                ],
                "case_studies": [
                    {
                        "title": "Tăng trưởng cung tiền M2 và mục tiêu lạm phát tại Việt Nam",
                        "detail": "Giai đoạn 2016-2024, tốc độ tăng trưởng M2 bình quân của Việt Nam duy trì ổn định ở mức 12-14%/năm, giúp kiểm soát vững chắc lạm phát cơ bản dưới 3% trong khi GDP tăng trưởng ấn tượng."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Tiền tệ Tìm kiếm (Search-Theoretic Model of Money) của Kiyotaki & Wright (1989): Tiền tệ xuất hiện nội sinh như một trạng thái cân bằng Nash trong mạng lưới giao dịch phi tập trung.",
                "Lý thuyết Cung tiền Tối ưu của Milton Friedman (Friedman Rule): Tỷ suất danh nghĩa tối ưu bằng 0 nhằm loại bỏ chi phí giữ tiền mặt.",
                "Cạnh tranh Tiền tệ Tư nhân và Sự sụp đổ của các thuật toán Stablecoin (Hayek's Denationalisation of Money trong kỷ nguyên Web3)."
            ]
        },
        review_questions=[
            "Phân tích ba chức năng kinh tế cơ bản của tiền tệ và chỉ ra chức năng nào giữ vai trò quyết định để một vật phẩm trở thành tiền tệ?",
            "Tại sao trong điều hành kinh tế vĩ mô hiện đại, Ngân hàng Nhà nước lại lựa chọn khối tiền M2 làm mục tiêu trung gian thay vì M0 hay M1?",
            "Trình bày mô hình Kiyotaki-Wright (1989) chứng minh tại sao một tài sản không có giá trị nội tại vẫn có thể được chấp nhận rộng rãi làm tiền tệ?"
        ]
    )
    
    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Thị trường Tài chính và Các Định chế Tài chính Trung gian",
        introduction="Chương 2 phân tích kiến trúc hệ thống tài chính, lý giải nguyên nhân kinh tế học đằng sau sự tồn tại của các định chế tài chính trung gian thông qua lý thuyết bất cân xứng thông tin của Akerlof và Stiglitz.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Cấu trúc hệ thống tài chính và luân chuyển vốn",
                "content": (
                    "Hệ thống tài chính thực hiện chức năng phân bổ nguồn vốn dư thừa từ những chủ thể tiết kiệm (hộ gia đình) "
                    "đến những chủ thể thiếu hụt vốn có cơ hội đầu tư sinh lời (doanh nghiệp, chính phủ). Luân chuyển vốn diễn ra qua hai kênh: "
                    "Kênh tài trợ trực tiếp (Direct Finance thông qua thị trường cổ phiếu, trái phiếu) và Kênh tài trợ gián tiếp (Indirect Finance thông qua các định chế trung gian).\n\n"
                    "Thị trường tài chính được phân đoạn thành Thị trường tiền tệ (công cụ nợ ngắn hạn dưới 1 năm có thanh khoản cao) "
                    "và Thị trường vốn (công cụ nợ và vốn chủ sở hữu dài hạn trên 1 năm)."
                ),
                "formulas": [
                    "Cân bằng dòng vốn tài chính: Total Savings = S_private + S_public + (M - X)",
                    "Tỷ lệ tín dụng / GDP: Credit_to_GDP = Total Bank Credit / Nominal GDP * 100%"
                ],
                "case_studies": [
                    {
                        "title": "Cơ cấu hệ thống tài chính dựa vào ngân hàng (Bank-based System) của Việt Nam",
                        "detail": "Dư nợ tín dụng nền kinh tế tại Việt Nam đạt trên 130% GDP, phản ánh sự phụ thuộc rất lớn vào kênh ngân hàng thương mại và đặt ra yêu cầu cấp bách phát triển thị trường trái phiếu doanh nghiệp để cân bằng hệ thống."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Lý thuyết bất cân xứng thông tin trong trung gian tài chính",
                "content": (
                    "Nếu thị trường tài chính không có chi phí giao dịch và thông tin hoàn hảo, trung gian tài chính sẽ không tồn tại. "
                    "Tuy nhiên, sự bất cân xứng thông tin sinh ra hai nghịch lý: Lựa chọn đối nghịch (Adverse Selection xảy ra trước khi giao kết hợp đồng, "
                    "khi những người vay rủi ro nhất lại tích cực tìm kiếm vốn vay nhất) và Rủi ro đạo đức (Moral Hazard xảy ra sau khi giải ngân, "
                    "khi người vay sử dụng vốn vào các mục đích liều lĩnh khác thỏa thuận ban đầu).\n\n"
                    "Các định chế tài chính trung gian giải quyết bài toán này nhờ lợi thế quy mô trong thu thập, xử lý thông tin và giám sát hợp đồng (Delegated Monitoring)."
                ),
                "formulas": [
                    "Lãi suất cân bằng khi có lựa chọn đối nghịch: r* thỏa mãn dPi_bank / dr = 0 (Stiglitz-Weiss 1981)",
                    "Mức độ phân tán rủi ro: Var(Portfolio) = (1/N) * sigma_i^2 -> 0 khi N tiến tới vô cùng"
                ],
                "case_studies": [
                    {
                        "title": "Vai trò của Trung tâm Thông tin Tín dụng Quốc gia (CIC)",
                        "detail": "CIC lưu trữ và cung cấp lịch sử tín dụng của hàng chục triệu khách hàng cá nhân và doanh nghiệp, giúp hệ thống ngân hàng giảm thiểu chi phí thẩm định và triệt tiêu nguy cơ lựa chọn đối nghịch."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Cắt giảm Tín dụng (Credit Rationing) của Stiglitz & Weiss (1981): Chứng minh tại sao tăng lãi suất làm trầm trọng thêm lựa chọn đối nghịch và ngân hàng chủ động từ chối cho vay ngay cả khi có dư thừa cầu.",
                "Mô hình Giám sát Ủy thác (Delegated Monitoring) của Diamond (1984): Trung gian tài chính tối ưu hóa chi phí giám sát người vay.",
                "Mô hình Đột biến Rút tiền gửi Diamond-Dybvig (1983): Cân bằng đa nghiệm (Multiple Equilibria) và vai trò của Bảo hiểm tiền gửi (Deposit Insurance)."
            ]
        },
        review_questions=[
            "Phân tích cơ chế phân bổ nguồn lực của kênh tài trợ trực tiếp và kênh tài trợ gián tiếp trong hệ thống tài chính?",
            "Lựa chọn đối nghịch (Adverse Selection) và Rủi ro đạo đức (Moral Hazard) biểu hiện như thế nào trong hoạt động tín dụng ngân hàng?",
            "Trình bày mô hình Stiglitz-Weiss (1981) và giải thích tại sao cơ chế giá (lãi suất) không thể tự động dọn sạch thị trường tín dụng?"
        ]
    )
    
    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Ngân hàng Trung ương, Cung - Cầu Tiền tệ và Cơ chế Tạo Tiền",
        introduction="Chương 3 phân tích vị trí độc tôn của Ngân hàng Trung ương trong việc phát hành tiền tệ cơ sở, mô hình hóa quá trình nhân tiền của hệ thống ngân hàng thương mại và các trường phái lý thuyết cầu tiền tệ.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Ngân hàng Trung ương và cơ sở tiền tệ (Monetary Base)",
                "content": (
                    "Ngân hàng Trung ương là cơ quan quản lý nhà nước duy nhất nắm độc quyền phát hành giấy bạc ngân hàng và quản lý dự trữ quốc gia. "
                    "Bảng cân đối tiền tệ giản đơn của NHTW thể hiện: Bên Tài sản nợ gồm Tiền mặt lưu hành ngoài hệ thống (C) và Dự trữ của các NHTM (R = RR + ER); "
                    "Bên Tài sản có gồm Chứng khoán chính phủ nắm giữ, Cho vay tái cấp vốn các tổ chức tín dụng và Dự trữ ngoại hối ròng.\n\n"
                    "Tổng tài sản nợ tạo thành Cơ sở tiền tệ (Monetary Base - MB hay Tiền mạnh H). Mọi sự thay đổi tài sản có của NHTW "
                    "đều tác động trực tiếp làm co giãn cơ số tiền tệ trong nền kinh tế."
                ),
                "formulas": [
                    "Cơ sở tiền tệ: MB = C + R = C + RR + ER",
                    "Dự trữ bắt buộc: RR = r_d * D (với r_d là tỷ lệ dự trữ bắt buộc)",
                    "Dự trữ thanh khoản dư thừa: ER = Excess Reserves"
                ],
                "case_studies": [
                    {
                        "title": "Tác động can thiệp mua ngoại tệ của Ngân hàng Nhà nước Việt Nam",
                        "detail": "Khi NHNN mua ròng 10-15 tỷ USD để tăng dự trữ ngoại hối quốc gia, cơ sở tiền tệ MB tăng mạnh. Để triệt tiêu nguy cơ dư thừa thanh khoản gây lạm phát, NHNN thực hiện nghiệp vụ trung hòa (Sterilization) bằng cách phát hành tín phiếu NHNN (SBV Bills) hút tiền về."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Hệ số nhân tiền tệ và quá trình mở rộng tiền gửi",
                "content": (
                    "Tiền tệ không chỉ do NHTW tạo ra. Khi một khoản tiền gửi ban đầu được đưa vào hệ thống ngân hàng, "
                    "các NHTM giữ lại một phần dự trữ bắt buộc và cho vay phần còn lại. Người vay sử dụng tiền thanh toán, tiền lại chảy vào tài khoản ngân hàng khác, "
                    "khởi động quá trình tạo tiền gửi phái sinh liên ngân hàng đa kỳ.\n\n"
                    "Mức độ mở rộng cung tiền M2 từ lượng tiền cơ sở MB được quy định bởi Hệ số nhân tiền tệ (Money Multiplier - m). "
                    "Hệ số này phụ thuộc vào hành vi nắm giữ tiền mặt của người dân (c = C/D) và tỷ lệ dự trữ của các ngân hàng (e = ER/D)."
                ),
                "formulas": [
                    "Cung tiền: M = m * MB",
                    "Hệ số nhân tiền tệ toàn diện: m = (1 + c) / (r_d + e + c)",
                    "Trong đó: c = C/D (tỷ lệ tiền mặt / tiền gửi), e = ER/D (tỷ lệ dự trữ dư thừa / tiền gửi)"
                ],
                "case_studies": [
                    {
                        "title": "Sự suy giảm tỷ lệ tiền mặt/tiền gửi nhờ thanh toán số tại Việt Nam",
                        "detail": "Sự phổ biến của mã VietQR và ví điện tử khiến tỷ lệ nắm giữ tiền mặt ngoài hệ thống (c) sụt giảm mạnh, làm tăng hệ số nhân tiền m và nâng cao hiệu quả dẫn vốn của hệ thống NHTM."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Cầu tiền Tồn trữ của Baumol-Tobin (Inventory-Theoretic Model of Cash Balances): Tối ưu hóa chi phí rút tiền từ ngân hàng.",
                "Lý thuyết Ưa thích Thanh khoản của Keynes và Động cơ Đầu cơ (Speculative Motive of Money Demand) trong điều kiện kỳ vọng lãi suất.",
                "Kiểm định Đồng tích hợp (Cointegration) và Tính Ổn định của Hàm Cầu Tiền Tệ dài hạn tại các nền kinh tế đang phát triển bằng mô hình ARDL Bounds Testing."
            ]
        },
        review_questions=[
            "Phân tích cơ chế tác động của nghiệp vụ thị trường mở (mua/bán tín phiếu) của NHTW đến lượng tiền cơ sở MB?",
            "Tại sao trong giai đoạn khủng hoảng tài chính, hệ số nhân tiền m lại có xu hướng sụt giảm nghiêm trọng mặc dù NHTW bơm mạnh lượng tiền cơ sở MB?",
            "Thiết lập mô hình Baumol-Tobin và chứng minh độ co giãn của cầu tiền tệ theo thu nhập là 0.5 và theo lãi suất là -0.5?"
        ]
    )
    
    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Lãi suất, Lạm phát và Cấu trúc Kỳ hạn của Lãi suất",
        introduction="Chương 4 nghiên cứu các quy luật vận động của lãi suất trên thị trường tiền tệ, phân tích tác động của lạm phát kỳ vọng qua hiệu ứng Fisher và lý giải hình dạng của đường cong lợi suất trái phiếu.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Các lý thuyết xác định lãi suất thị trường",
                "content": (
                    "Lãi suất là giá cả của việc sử dụng vốn trong một thời kỳ nhất định. Hai trường phái lý thuyết lớn giải thích sự hình thành lãi suất: "
                    "Lý thuyết Quỹ cho vay (Loanable Funds Theory) tiếp cận từ góc độ cung - cầu vốn thực tế của nền kinh tế (tiết kiệm tạo cung, đầu tư và thâm hụt ngân sách tạo cầu); "
                    "và Lý thuyết Ưa thích thanh khoản của Keynes (Liquidity Preference Theory) tiếp cận từ sự cân bằng cung - cầu tiền tệ.\n\n"
                    "Lãi suất thị trường danh nghĩa luôn phản ánh phần bù lạm phát kỳ vọng theo Phương trình Fisher. "
                    "Khi lạm phát kỳ vọng tăng lên, lãi suất danh nghĩa sẽ điều chỉnh tăng tương ứng để bảo đảm lãi suất thực dương cho người gửi tiền."
                ),
                "formulas": [
                    "Phương trình Fisher chính xác: (1 + i) = (1 + r) * (1 + pi^e)",
                    "Phương trình Fisher xấp xỉ: i = r + pi^e (với i là lãi suất danh nghĩa, r là lãi suất thực, pi^e là lạm phát kỳ vọng)"
                ],
                "case_studies": [
                    {
                        "title": "Chính sách duy trì lãi suất thực dương của Ngân hàng Nhà nước",
                        "detail": "NHNN kiên định định hướng lãi suất huy động danh nghĩa luôn cao hơn tỷ lệ lạm phát mục tiêu từ 1.5% đến 2.5%, ngăn chặn tình trạng người dân rút tiền gửi chuyển sang đầu cơ vàng và bất động sản."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Cấu trúc kỳ hạn và đường cong lợi suất (Yield Curve)",
                "content": (
                    "Đường cong lợi suất phản ánh mối quan hệ giữa lãi suất đáo hạn (YTM) và kỳ hạn của các công cụ nợ có cùng chất lượng tín dụng (thường là Trái phiếu Chính phủ). "
                    "Đường cong có thể dốc lên bình thường (kỳ hạn dài lãi suất cao hơn ngắn hạn), nằm ngang, hoặc dốc xuống (đảo ngược - Inverted Yield Curve).\n\n"
                    "Ba lý thuyết kinh điển giải thích đường cong lợi suất: Lý thuyết Kỳ vọng thuần túy (Pure Expectations), "
                    "Lý thuyết Thị trường phân đoạn (Segmented Markets) và Lý thuyết Phần bù thanh khoản (Liquidity Premium Theory). "
                    "Hiện tượng đường cong lợi suất đảo ngược được coi là chỉ báo dự báo suy thoái kinh tế chính xác nhất trong lịch sử tài chính."
                ),
                "formulas": [
                    "Lý thuyết Kỳ vọng thuần túy: (1 + i_{nt})^n = (1 + i_{1t}) * (1 + i^e_{1,t+1}) * ... * (1 + i^e_{1,t+n-1})",
                    "Lãi suất kỳ hạn (Forward Rate): f_{1, t+1} = [ (1 + i_{2t})^2 / (1 + i_{1t}) ] - 1",
                    "Lý thuyết Phần bù thanh khoản: i_{nt} = (1/n) * sum i^e_{1,t+k} + l_{nt} (với l_{nt} > 0 là phần bù thanh khoản kỳ hạn n)"
                ],
                "case_studies": [
                    {
                        "title": "Đường cong lợi suất Trái phiếu Chính phủ Việt Nam tại HNX",
                        "detail": "Đường cong lợi suất TPCP chuẩn hóa từ kỳ hạn 1 năm đến 30 năm được HNX công bố hàng ngày, đóng vai trò đường cong lãi suất không rủi ro tham chiếu cho toàn bộ hệ thống định giá tài sản tài chính tại Việt Nam."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Cấu trúc Kỳ hạn Lãi suất Cân bằng Động (Equilibrium Term Structure): Mô hình Vasicek (1977) với quá trình hoàn lương trung bình (Mean-Reverting Ornstein-Uhlenbeck) và Mô hình Cox-Ingersoll-Ross (CIR 1985).",
                "Mô hình Cấu trúc Kỳ hạn Nelson-Siegel (1987) và Svensson (1994) mở rộng: Phân rã đường cong thành ba nhân tố Level, Slope và Curvature.",
                "Hiện tượng Lãi suất Thực Toàn cầu R-star (Natural Rate of Interest) sụt giảm theo mô hình Laubach-Williams (2003)."
            ]
        },
        review_questions=[
            "Phân tích cơ chế tác động của lạm phát kỳ vọng đến lãi suất danh nghĩa theo Hiệu ứng Fisher?",
            "Tại sao hiện tượng đường cong lợi suất đảo ngược (Inverted Yield Curve) lại được coi là phong vũ biểu cảnh báo suy thoái kinh tế?",
            "Giải phương trình vi phân ngẫu nhiên của mô hình Vasicek và giải thích tại sao mô hình này cho phép lãi suất danh nghĩa âm?"
        ]
    )
    
    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Chính sách Tiền tệ: Mục tiêu, Công cụ và Cơ chế Truyền dẫn Vĩ mô",
        introduction="Chương 5 phân tích hệ thống mục tiêu và công cụ điều hành chính sách tiền tệ hiện đại, làm rõ các kênh truyền dẫn từ công cụ của NHTW đến khu vực kinh tế thực và lạm phát.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Hệ thống mục tiêu và công cụ điều hành chính sách tiền tệ",
                "content": (
                    "Chính sách tiền tệ (CSTT) là tổng thể các biện pháp do NHTW khởi xướng nhằm kiểm soát cung tiền và lãi suất để đạt các mục tiêu kinh tế vĩ mô: "
                    "Ổn định giá trị đồng tiền (kiểm soát lạm phát), duy trì việc làm cao và hỗ trợ tăng trưởng kinh tế bền vững. "
                    "Cơ chế điều hành vận hành theo thứ bậc: Công cụ tác động -> Mục tiêu hoạt động (Dự trữ ngân hàng, Lãi suất O/N) -> Mục tiêu trung gian (M2, Tín dụng) -> Mục tiêu cuối cùng.\n\n"
                    "Tại Việt Nam, NHNN phối hợp linh hoạt ba công cụ thị trường (Nghiệp vụ OMO, Tái cấp vốn, Dự trữ bắt buộc) "
                    "kết hợp công cụ hành chính trực tiếp là Hạn mức tăng trưởng tín dụng (Room tín dụng) phân bổ cho từng ngân hàng."
                ),
                "formulas": [
                    "Quy tắc Taylor kinh điển (1993): i_t = r* + pi_t + 0.5*(pi_t - pi*) + 0.5*(y_t - y*)",
                    "Trong đó: r* là lãi suất thực cân bằng, pi* là lạm phát mục tiêu, (y_t - y*) là khoảng trống sản lượng (Output Gap)"
                ],
                "case_studies": [
                    {
                        "title": "Cơ chế phân bổ và lộ trình gỡ bỏ 'Room tín dụng' tại Việt Nam",
                        "detail": "NHNN áp dụng chỉ tiêu tăng trưởng tín dụng hàng năm (khoảng 14-15%) để kiểm soát rủi ro bong bóng tài sản, đồng thời từng bước nâng cao chuẩn mực an toàn vốn Basel II/Basel III để tiến tới điều hành hoàn toàn bằng lãi suất thị trường."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Các kênh truyền dẫn chính sách tiền tệ",
                "content": (
                    "Cơ chế truyền dẫn CSTT (Monetary Transmission Mechanism) mô tả các chuỗi mắt xích mà qua đó các quyết định của NHTW "
                    "lan tỏa tới tổng cầu và mặt bằng giá cả. Bốn kênh truyền dẫn trụ cột gồm: Kênh lãi suất (Lãi suất giảm -> Chi phí vốn giảm -> Đầu tư và tiêu dùng tăng);\n\n"
                    "Kênh tín dụng ngân hàng (Bank Lending Channel: Thanh khoản ngân hàng dồi dào -> Cung cấp thêm vốn cho doanh nghiệp phụ thuộc ngân hàng); "
                    "Kênh tỷ giá hối đoái (Lãi suất giảm -> Đồng tiền giảm giá -> Xuất khẩu ròng tăng); "
                    "và Kênh giá tài sản (Lãi suất giảm -> Giá cổ phiếu, BĐS tăng -> Hiệu ứng của cải - Wealth Effect thúc đẩy tiêu dùng cá nhân)."
                ),
                "formulas": [
                    "Kênh lãi suất: Delta i_OMO -> Delta i_market -> Delta Capex -> Delta Y",
                    "Kênh tỷ giá: Delta i -> Delta E (Tỷ giá danh nghĩa) -> Delta Net_Exports -> Delta Y"
                ],
                "case_studies": [
                    {
                        "title": "Đợt cắt giảm 4 lần lãi suất điều hành của NHNN năm 2023",
                        "detail": "NHNN hạ lãi suất tái cấp vốn từ 6% xuống 4.5%/năm nhằm hỗ trợ nền kinh tế phục hồi sau đại dịch, tạo điều kiện cho các NHTM hạ lãi suất cho vay thương mại từ 1.5% đến 2.5%."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình New Keynesian DSGE (Smets & Wouters 2007): Tác động của Cú sốc Chính sách Tiền tệ với giá cả và tiền lương kết dính (Calvo Sticky Prices).",
                "Bẫy Thanh khoản và Chính sách Tiền tệ Phi truyền thống (Unconventional Monetary Policy): Nới lỏng định lượng (QE) và Định hướng kỳ vọng (Forward Guidance) tại Ngưỡng Lãi suất Cận Không (Zero Lower Bound - ZLB).",
                "Nhận diện Causal Effects của CSTT bằng High-Frequency Identification (HFI) xung quanh thời điểm công bố chính sách của NHTW theo Gertler & Karadi (2015)."
            ]
        },
        review_questions=[
            "Phân tích cơ chế vận hành của Quy tắc Taylor và giải thích tại sao hệ số phản ứng với lạm phát bắt buộc phải lớn hơn 1 (Nguyên lý Taylor)?",
            "Trình bày chi tiết bốn kênh truyền dẫn chính sách tiền tệ và đánh giá kênh truyền dẫn nào có hiệu lực mạnh nhất tại Việt Nam hiện nay?",
            "Thiết lập mô hình VAR cấu trúc (SVAR) với ràng buộc dấu (Sign Restrictions) để đo lường phản ứng xung của sản lượng và lạm phát trước cú sốc lãi suất?"
        ]
    )
    
    # Chapter 6
    b.add_chapter(
        chap_num="6",
        chap_title="Khủng hoảng Tài chính Tiền tệ và Chính sách An toàn Vĩ mô (Macroprudential)",
        introduction="Chương 6 đúc kết các bài học xương máu từ các cuộc khủng hoảng tài chính toàn cầu, phân tích cơ chế lan truyền rủi ro hệ thống và nghiên cứu khung khổ chính sách an toàn vĩ mô Basel III bảo vệ hệ thống tài chính quốc gia.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bản chất và cơ chế lan truyền khủng hoảng tài chính",
                "content": (
                    "Khủng hoảng tài chính thường bắt nguồn từ chu kỳ bùng nổ tín dụng kết hợp với bong bóng giá tài sản (bất động sản, chứng khoán). "
                    "Thuyết Bất ổn Tài chính của Hyman Minsky (Financial Instability Hypothesis) chỉ ra rằng các thời kỳ ổn định kinh tế kéo dài "
                    "thường khuyến khích hành vi liều lĩnh, biến cấu trúc tài chính từ Vững chắc (Hedge Finance) sang Đầu cơ (Speculative Finance) "
                    "và cuối cùng là mô hình Lừa đảo (Ponzi Finance).\n\n"
                    "Khi bong bóng tài sản vỡ vụn, hiện tượng bán tháo giải chấp tài sản bảo đảm (Fire Sales) kích hoạt vòng xoáy thanh khoản tiêu cực, "
                    "dẫn tới làn sóng phá sản dây chuyền của các định chế tài chính quá lớn để sụp đổ (Too Big To Fail)."
                ),
                "formulas": [
                    "Bộ gia tốc tài chính (Financial Accelerator): Bernanke, Gertler & Gilchrist (1999) Delta Net_Worth -> Delta External_Finance_Premium",
                    "Đòn bẩy tài chính hệ thống: Leverage = Total Assets / Equity"
                ],
                "case_studies": [
                    {
                        "title": "Bài học từ sự kiện sụp đổ của Ngân hàng Silicon Valley (SVV) và Credit Suisse năm 2023",
                        "detail": "SVB sụp đổ trong 48 giờ do lỗ lớn từ danh mục trái phiếu HTM khi Fed tăng lãi suất sốc kết hợp với hiện tượng rút tiền kỹ thuật số (Digital Bank Run), cảnh tỉnh các ngân hàng về quản trị rủi ro lãi suất trên sổ ngân hàng (IRRBB)."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Chính sách an toàn vĩ mô và hiệp ước Basel III",
                "content": (
                    "Chính sách an toàn vi mô (Microprudential) tập trung vào sự an toàn của từng ngân hàng riêng lẻ, "
                    "nhưng không ngăn chặn được rủi ro hệ thống (Fallacy of Composition). Chính sách an toàn vĩ mô (Macroprudential Policy) "
                    "được thiết kế để bảo vệ toàn bộ mạng lưới tài chính trước các cú sốc hệ thống.\n\n"
                    "Chuẩn mực Basel III thiết lập các yêu cầu ngặt nghèo về chất lượng vốn (Vốn tự có cấp 1 - CET1 tối thiểu 4.5%), "
                    "bổ sung Đệm vốn bảo toàn (Capital Conservation Buffer 2.5%), Đệm vốn chống chu kỳ (Countercyclical Capital Buffer - CCyB từ 0-2.5%), "
                    "và hai chỉ số thanh khoản định lượng: LCR (Liquidity Coverage Ratio cho 30 ngày) và NSFR (Net Stable Funding Ratio cho 1 năm)."
                ),
                "formulas": [
                    "Tỷ lệ an toàn vốn: CAR = Total Regulatory Capital / Risk-Weighted Assets (RWA) >= 8%",
                    "Hệ số LCR: Liquidity Coverage Ratio = High-Quality Liquid Assets (HQLA) / Total Net Cash Outflows (30 days) >= 100%",
                    "Hệ số NSFR: Available Stable Funding (ASF) / Required Stable Funding (RSF) >= 100%"
                ],
                "case_studies": [
                    {
                        "title": "Lộ trình triển khai Basel II và tiến tới Basel III của các NHTM Việt Nam",
                        "detail": "Sau khi phần lớn các ngân hàng thương mại hoàn thành Thông tư 41/2016/TT-NHNN (Basel II), các ngân hàng tiên phong như Vietcombank, Techcombank, VPBank, MB đã chủ động triển khai thí điểm khung thanh khoản Basel III."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Vòng xoáy Thanh khoản (Liquidity Spirals) của Brunnermeier & Pedersen (2009): Tương tác khuyếch đại giữa Thanh khoản Thị trường (Market Liquidity) và Thanh khoản Cấp vốn (Funding Liquidity).",
                "Đo lường Rủi ro Đóng góp Hệ thống: Chỉ số CoVaR của Adrian & Brunnermeier (2016) và Marginal Expected Shortfall (MES) của Acharya et al. (2017).",
                "Lý thuyết Trò chơi trong Giải cứu Ngân hàng và Rủi ro Đạo đức Của Cơ chế Bảo lãnh Quá Lớn Để Sụp Đổ (Too-Big-To-Fail Bailout Guarantees)."
            ]
        },
        review_questions=[
            "Phân tích ba trạng thái tài chính trong Thuyết Bất ổn Tài chính của Hyman Minsky và chỉ ra thời điểm Minsky Moment xuất hiện?",
            "Tại sao chính sách an toàn vi mô thuần túy không thể ngăn chặn được rủi ro mang tính hệ thống trong mạng lưới ngân hàng?",
            "Trình bày phương pháp tính toán chỉ số Delta CoVaR bằng mô hình hồi quy phân vị (Quantile Regression) để đo lường mức độ đóng góp rủi ro của từng ngân hàng vào rủi ro toàn hệ thống?"
        ]
    )
    
    pages, sz = b.save(out_pdf)
    print(f"[SUCCESS] Book 4 saved: {out_pdf} ({pages} pages, {sz:.2f} MB)")
    return {
        "title": title,
        "code": subject_code,
        "author": authors,
        "path": out_pdf,
        "pages": pages,
        "size_mb": round(sz, 2)
    }

if __name__ == "__main__":
    build_tctt()
