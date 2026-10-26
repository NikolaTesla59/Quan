# -*- coding: utf-8 -*-
"""
Generator for Textbook 6:
[NEU] Kinh doanh bảo hiểm - PGS.TS Nguyễn Văn Định (NXB ĐHKTQD)
"""
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_kdbh():
    title = "Kinh doanh bảo hiểm"
    subject_code = "BH1101"
    faculty = "Khoa Bảo hiểm"
    authors = "PGS.TS. Nguyễn Văn Định & PGS.TS. Hoàng Mạnh Cừ (Đồng Chủ biên)"
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\03_Ngân hàng & Bảo hiểm\[NEU] Kinh doanh bảo hiểm - PGS.TS Nguyễn Văn Định (NXB ĐHKTQD)"
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Kinh doanh bảo hiểm - PGS.TS Nguyễn Văn Định (NXB ĐHKTQD).pdf")
    
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
            "chapter_title": "Bản chất Kinh tế, Lịch sử và Vai trò Xã hội của Bảo hiểm",
            "topics": [
                "Khái niệm rủi ro, quản trị rủi ro và các phương thức xử lý rủi ro trong đời sống kinh tế",
                "Bản chất kinh tế của bảo hiểm: Cơ chế phân tán rủi ro và quy luật số lớn (Law of Large Numbers)",
                "Phân loại bảo hiểm theo đối tượng: Bảo hiểm tài sản, Bảo hiểm con người, Bảo hiểm trách nhiệm dân sự",
                "Chuyên đề Tiến sĩ: Lý thuyết Tiện ích Kỳ vọng von Neumann-Morgenstern và Hệ số ngại rủi ro Arrow-Pratt"
            ]
        },
        {
            "chapter_num": "2",
            "chapter_title": "Cơ sở Pháp lý và Hợp đồng Bảo hiểm theo Luật KDBH 2022",
            "topics": [
                "Các nguyên tắc pháp lý nền tảng: Nguyên tắc Trung thực tuyệt đối (Utmost Good Faith), Quyền lợi có thể được bảo hiểm (Insurable Interest), Bồi thường (Indemnity), Thế quyền (Subrogation)",
                "Cấu trúc hợp đồng bảo hiểm, điều khoản loại trừ trách nhiệm bảo hiểm và cơ chế giải quyết tranh chấp",
                "Quyền và nghĩa vụ của doanh nghiệp bảo hiểm, bên mua bảo hiểm, người được bảo hiểm và người thụ hưởng",
                "Chuyên đề Tiến sĩ: Bất cân xứng thông tin trong bảo hiểm: Mô hình Rothschild & Stiglitz (1976) về Cân bằng Tách biệt (Separating Equilibrium)"
            ]
        },
        {
            "chapter_num": "3",
            "chapter_title": "Nghiệp vụ Bảo hiểm Phi Nhân thọ và Giám định Tổn thất",
            "topics": [
                "Bảo hiểm tài sản và thiệt hại: Bảo hiểm hỏa hoạn, nổ, rủi ro xây dựng lắp đặt (CAR/EAR)",
                "Bảo hiểm hàng hóa vận chuyển đường biển và thân tàu biển (Quy tắc Institute Cargo Clauses - ICC A, B, C)",
                "Bảo hiểm trách nhiệm dân sự của chủ xe cơ giới và trách nhiệm sản phẩm",
                "Quy trình giám định tổn thất, bồi thường và phòng ngừa gian lận bảo hiểm",
                "Chuyên đề Tiến sĩ: Mô hình Tổn thất Tổng hợp (Aggregate Loss Models) và Phân phối Đuôi Dày Pareto/Lognormal"
            ]
        },
        {
            "chapter_num": "4",
            "chapter_title": "Nghiệp vụ Bảo hiểm Nhân thọ và Quản lý Rủi ro Tuổi thọ",
            "topics": [
                "Đặc điểm bảo hiểm nhân thọ: Tính bảo vệ kết hợp tính tích lũy đầu tư và rủi ro dài hạn",
                "Các sản phẩm nhân thọ truyền thống: Tử kỳ, Sinh kỳ, Hỗn hợp và Sản phẩm liên kết đầu tư (Unit-Linked, Universal Life)",
                "Bảng tỷ lệ tử vong (Life Table) và kỹ thuật tính phí bảo hiểm thuần nhân thọ",
                "Chuyên đề Tiến sĩ: Mô hình Động học Tỷ lệ Tử vong Lee-Carter (1992) và Quản trị Rủi ro Sống thọ (Longevity Risk)"
            ]
        },
        {
            "chapter_num": "5",
            "chapter_title": "Định phí Bảo hiểm, Trích lập Dự phòng và Tái Bảo hiểm (Reinsurance)",
            "topics": [
                "Nguyên tắc định phí bảo hiểm: Đầy đủ, công bằng, khuyến khích phòng ngừa tổn thất",
                "Trích lập dự phòng nghiệp vụ phi nhân thọ (Dự phòng phí chưa được hưởng UPR, Dự phòng bồi thường IBNR theo phương pháp Chain Ladder)",
                "Nghiệp vụ Tái bảo hiểm: Tái bảo hiểm tỷ lệ (Quota Share, Surplus) và phi tỷ lệ (Excess of Loss)",
                "Chuyên đề Tiến sĩ: Lý thuyết Phá sản Actuary (Cramér-Lundberg Ruin Theory) và Chuẩn mực IFRS 17 / Khung Solvency II"
            ]
        }
    ]
    b.add_table_of_contents(toc_data)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Bản chất Kinh tế, Lịch sử và Vai trò Xã hội của Bảo hiểm",
        introduction="Chương 1 làm rõ cơ sở khách quan của sự tồn tại và phát triển của bảo hiểm, phân tích cơ chế tập hợp số đông bù số ít theo Quy luật số lớn và đánh giá vai trò của bảo hiểm đối với ổn định xã hội và tăng trưởng kinh tế.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Khái niệm rủi ro và bản chất kinh tế của bảo hiểm",
                "content": (
                    "Rủi ro là sự bất trắc có thể đo lường được về mặt xác suất, có khả năng dẫn đến tổn thất vật chất hoặc tinh thần ngoài ý muốn. "
                    "Bảo hiểm là phương thức chuyển giao rủi ro từ một cá nhân hoặc tổ chức sang cho doanh nghiệp bảo hiểm. "
                    "Bản chất kinh tế của bảo hiểm là sự phân phối lại thu nhập giữa những người tham gia: Tập hợp nguồn tài chính từ số đông người có nguy cơ gặp rủi ro "
                    "thành một quỹ dự trữ tập trung để bồi thường thiệt hại cho số ít người không may gặp tai nạn, tổn thất thực tế.\n\n"
                    "Cơ sở toán học của bảo hiểm dựa trên Quy luật số lớn (Law of Large Numbers) của Chebyshev và Bernoulli: "
                    "Khi số lượng đối tượng tham gia bảo hiểm đủ lớn, tần suất xảy ra tổn thất thực tế sẽ tiệm cận sát xác suất tổn thất lý thuyết."
                ),
                "formulas": [
                    "Quy luật số lớn: lim_{N -> inf} P( | (1/N)*sum X_i - mu | < epsilon ) = 1",
                    "Độ lệch chuẩn tổn thất bình quân trên một đơn vị bảo hiểm: sigma_mean = sigma / sqrt(N)"
                ],
                "case_studies": [
                    {
                        "title": "Bảo hiểm nông nghiệp thí điểm tại các tỉnh Đồng bằng Sông Cửu Long",
                        "detail": "Các chương trình bảo hiểm cây lúa và thủy sản bảo vệ nông dân trước thiên tai bão lũ, hạn mặn, giúp người dân nhanh chóng tái thiết sản xuất sau các thảm họa khí hậu."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Vai trò kinh tế - xã hội của ngành bảo hiểm",
                "content": (
                    "Bảo hiểm thực hiện ba chức năng kinh tế vĩ mô then chốt: "
                    "Thứ nhất, bồi thường tổn thất kịp thời, ổn định đời sống nhân dân và khôi phục hoạt động sản xuất kinh doanh của doanh nghiệp; "
                    "Thứ hai, đóng vai trò nhà đầu tư tổ chức khổng lồ trên thị trường vốn thông qua việc giải ngân quỹ nhàn rỗi vào trái phiếu chính phủ, hạ tầng quốc gia; "
                    "Thứ ba, nâng cao ý thức phòng ngừa và kiểm soát rủi ro cho toàn xã hội.\n\n"
                    "Thị trường bảo hiểm Việt Nam đạt tốc độ tăng trưởng doanh thu phí bình quân trên 15%/năm, "
                    "đóng góp tích cực vào mạng lưới an sinh xã hội quốc gia."
                ),
                "formulas": [
                    "Mức độ thâm nhập bảo hiểm: Insurance Penetration = Total Gross Written Premium (GWP) / GDP * 100%",
                    "Mật độ bảo hiểm: Insurance Density = Total GWP / Total Population (USD/người)"
                ],
                "case_studies": [
                    {
                        "title": "Quy mô đầu tư trở lại nền kinh tế của ngành bảo hiểm Việt Nam",
                        "detail": "Tổng số tiền các doanh nghiệp bảo hiểm tại Việt Nam tái đầu tư vào nền kinh tế đạt trên 750,000 tỷ đồng (gần 30 tỷ USD), trong đó hơn 60% được phân bổ vào Trái phiếu Chính phủ kỳ hạn dài 15-30 năm."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Tiện ích Kỳ vọng von Neumann-Morgenstern (VNM Expected Utility Theory): Hàm tiện ích lồi U''(w) < 0 và Độ ngại rủi ro tuyệt đối Arrow-Pratt: ARA(w) = -U''(w)/U'(w).",
                "Nghịch lý Allais (Allais Paradox) và Bằng chứng Bác bỏ Tiên đề Độc lập (Independence Axiom) trong Lựa chọn Bảo hiểm.",
                "Mô hình Bảo hiểm Cắt giảm Rủi ro Tối ưu của Mossin (1968): Chứng minh tại sao khi có phụ phí bảo hiểm (Positive Loading), người mua hợp lý không bao giờ mua bảo hiểm toàn bộ 100%."
            ]
        },
        review_questions=[
            "Phân tích cơ sở toán học của Quy luật số lớn và giải thích tại sao quy mô danh mục hợp đồng càng lớn thì rủi ro thanh toán của công ty bảo hiểm càng giảm?",
            "Trình bày ba vai trò kinh tế - xã hội then chốt của ngành bảo hiểm đối với nền kinh tế thị trường?",
            "Thiết lập bài toán tối ưu hóa tiện ích kỳ vọng của Mossin (1968) và chứng minh điều kiện người tiêu dùng lựa chọn mức khấu trừ (Deductible) tối ưu?"
        ]
    )
    
    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Cơ sở Pháp lý và Hợp đồng Bảo hiểm theo Luật KDBH 2022",
        introduction="Chương 2 phân tích các chuẩn mực pháp lý và nguyên tắc hợp đồng theo Luật Kinh doanh bảo hiểm năm 2022, làm rõ cơ chế bảo vệ quyền lợi người tiêu dùng và phân xử tranh chấp bồi thường.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Các nguyên tắc pháp lý nền tảng của hợp đồng bảo hiểm",
                "content": (
                    "Hợp đồng bảo hiểm là sự thỏa thuận giữa bên mua bảo hiểm và doanh nghiệp bảo hiểm. "
                    "Hợp đồng được chi phối bởi bốn nguyên tắc pháp lý cốt lõi: "
                    "1. Nguyên tắc Trung thực tuyệt đối (Utmost Good Faith): Các bên phải cung cấp đầy đủ, trung thực mọi thông tin trọng yếu (Material Facts) liên quan đến rủi ro;\n\n"
                    "2. Nguyên tắc Quyền lợi có thể được bảo hiểm (Insurable Interest): Bên mua bảo hiểm phải có quan hệ nhân thân, tài sản hoặc nghĩa vụ pháp lý chịu thiệt hại tài chính khi sự kiện bảo hiểm xảy ra; "
                    "3. Nguyên tắc Bồi thường (Indemnity): Doanh nghiệp bảo hiểm bồi thường đúng thiệt hại thực tế nhằm phục hồi tình trạng tài chính ban đầu cho người được bảo hiểm, không để họ trục lợi từ bảo hiểm; "
                    "4. Nguyên tắc Thế quyền (Subrogation): Doanh nghiệp bảo hiểm sau khi bồi thường có quyền thay mặt người được bảo hiểm đòi người thứ ba có lỗi bồi hoàn."
                ),
                "formulas": [
                    "Nguyên tắc Bồi thường tài sản: Bồi thường = min(Tổn thất thực tế, Số tiền bảo hiểm, Giá trị thị trường tài sản)",
                    "Quy tắc tỷ lệ bảo hiểm dưới giá trị: Bồi thường = Tổn thất * (Số tiền bảo hiểm / Giá trị thực tế tài sản)"
                ],
                "case_studies": [
                    {
                        "title": "Tranh chấp bồi thường do vi phạm nguyên tắc trung thực tuyệt đối",
                        "detail": "Tòa án tuyên hủy hợp đồng bảo hiểm nhân thọ và bác yêu cầu chi trả bồi thường khi phát hiện khách hàng cố tình giấu bệnh án ung thư đã được chẩn đoán tại bệnh viện trước thời điểm ký hợp đồng."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Những điểm mới của Luật Kinh doanh bảo hiểm năm 2022",
                "content": (
                    "Luật KDBH 2022 đánh dấu bước tiến lớn trong hoàn thiện thể chế: "
                    "Thứ nhất, chuyển đổi phương thức quản lý vốn sang mô hình Vốn trên cơ sở rủi ro (Risk-Based Capital - RBC) đồng bộ với chuẩn mực quốc tế; "
                    "Thứ hai, siết chặt quy định về đại lý bảo hiểm, đại lý tổ chức (kênh Bancassurance) nhằm ngăn chặn tình trạng ép khách hàng vay vốn ngân hàng mua bảo hiểm;\n\n"
                    "Thứ ba, quy định thời gian cân nhắc tham gia bảo hiểm 21 ngày cho khách hàng và bắt buộc doanh nghiệp bảo hiểm phải ghi âm, lưu trữ bằng chứng tư vấn đối với các sản phẩm liên kết đầu tư."
                ),
                "formulas": [
                    "Mô hình Vốn trên cơ sở rủi ro: RBC Ratio = Tổng vốn khả dụng / Vốn yêu cầu trên cơ sở rủi ro (RBC) >= 100%"
                ],
                "case_studies": [
                    {
                        "title": "Chấn chỉnh hoạt động phân phối bảo hiểm qua ngân hàng (Bancassurance)",
                        "detail": "Bộ Tài chính tiến hành thanh tra toàn diện hoạt động Bancassurance tại các công ty bảo hiểm nhân thọ lớn (Prudential, Manulife, MB Ageas, Sun Life), xử phạt nghiêm các vi phạm tư vấn không đúng bản chất sản phẩm và ép buộc khách hàng."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Cân bằng Cạnh tranh trong Thị trường Bảo hiểm của Rothschild & Stiglitz (1976): Chứng minh sự không tồn tại của Cân bằng Gộp (Pooling Equilibrium) khi có Bất cân xứng Thông tin.",
                "Rủi ro Đạo đức Sau Khi Ký Hợp đồng (Ex-post Moral Hazard): Chi phí Kiểm định Tổn thất và Mô hình Hợp đồng Bảo hiểm Tối ưu Townsend (1979) với Quy tắc Kiểm toán Xác suất.",
                "Lý thuyết Kinh tế về Gian lận Bảo hiểm (Insurance Fraud): Mô hình Trò chơi Giám sát giữa Thẩm định viên Bồi thường và Người được Bảo hiểm theo Picard (1996)."
            ]
        },
        review_questions=[
            "Phân tích nguyên tắc Quyền lợi có thể được bảo hiểm (Insurable Interest) và chỉ ra sự khác biệt khi áp dụng trong bảo hiểm tài sản so với bảo hiểm nhân thọ?",
            "Tại sao nguyên tắc thế quyền (Subrogation) chỉ áp dụng trong bảo hiểm phi nhân thọ mà không áp dụng trong bảo hiểm con người?",
            "Trình bày mô hình Rothschild-Stiglitz (1976) và giải thích tại sao khách hàng rủi ro thấp phải chấp nhận hợp đồng có mức khấu trừ cao để phát tín hiệu tách biệt?"
        ]
    )
    
    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Nghiệp vụ Bảo hiểm Phi Nhân thọ và Giám định Tổn thất",
        introduction="Chương 3 trình bày các nghiệp vụ bảo hiểm phi nhân thọ cốt lõi, quy tắc bảo hiểm hàng hải quốc tế ICC và quy trình nghiệp vụ giám định, bồi thường giải quyết khiếu nại chuyên nghiệp.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bảo hiểm tài sản, thiệt hại và bảo hiểm hàng hải",
                "content": (
                    "Bảo hiểm tài sản bảo vệ quyền sở hữu của doanh nghiệp và cá nhân trước các thảm họa cháy nổ, thiên tai, hỏng hóc máy móc. "
                    "Hợp đồng bảo hiểm hỏa hoạn và các rủi ro đặc biệt chuẩn hóa điều khoản bồi thường theo giá trị thay thế mới hoặc giá trị thực tế sau khấu hao.\n\n"
                    "Bảo hiểm hàng hải (Marine Insurance) là nghiệp vụ bảo hiểm lâu đời nhất thế giới, tuân thủ Bộ điều khoản bảo hiểm hàng hóa của Viện những người bảo hiểm Luân Đôn (Institute Cargo Clauses - ICC 1/1/1982 và 2009). "
                    "Điều kiện ICC (A) là bảo hiểm mọi rủi ro (All Risks); Điều kiện ICC (B) bảo hiểm các rủi ro cụ thể như chìm tàu, mắc cạn, sét đánh; "
                    "Điều kiện ICC (C) là phạm vi hẹp nhất loại trừ tổn thất riêng do sóng biển cuốn trôi."
                ),
                "formulas": [
                    "Định giá bảo hiểm hàng hóa xuất nhập khẩu: CIF = (CFR + F) / (1 - R)",
                    "Số tiền bảo hiểm thông thường: V = CIF * 110% (10% dự tính lãi của nhà nhập khẩu)"
                ],
                "case_studies": [
                    {
                        "title": "Bồi thường tổn thất trong sự cố mắc cạn tàu Ever Given tại kênh đào Suez",
                        "detail": "Khi chủ tàu tuyên bố Tổn thất chung (General Average), toàn bộ các chủ hàng có hàng trên tàu (bao gồm nhiều doanh nghiệp xuất khẩu Việt Nam) phải đóng góp chi phí cứu hộ tàu tương ứng với tỷ lệ giá trị hàng hóa theo Luật Hàng hải quốc tế."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Bảo hiểm trách nhiệm dân sự và quy trình giám định bồi thường",
                "content": (
                    "Bảo hiểm trách nhiệm bảo vệ người được bảo hiểm trước trách nhiệm pháp lý bồi thường thiệt hại ngoài hợp đồng cho bên thứ ba do hành vi hoặc tài sản của mình gây ra. "
                    "Bảo hiểm trách nhiệm dân sự bắt buộc của chủ xe cơ giới là yêu cầu pháp lý tại Việt Nam, quy định mức trách nhiệm tối đa về người và tài sản.\n\n"
                    "Quy trình giải quyết quyền lợi bảo hiểm gồm: Tiếp nhận thông báo tổn thất -> Giám định hiện trường -> Thu thập hồ sơ chứng từ pháp lý -> "
                    "Xác định nguyên nhân trực tiếp (Proximate Cause) -> Tính toán số tiền bồi thường -> Chi trả và thực hiện thế quyền đòi bên thứ ba nếu có."
                ),
                "formulas": [
                    "Tỷ lệ tổn thất bồi thường (Loss Ratio): LR = (Tổng bồi thường đã chi trả + Dự phòng bồi thường ròng) / Phí bảo hiểm gốc được hưởng * 100%",
                    "Tỷ lệ kết hợp (Combined Ratio): CR = Loss Ratio + Expense Ratio (Nếu CR < 100%, doanh nghiệp có lãi thuần từ kinh doanh bảo hiểm)"
                ],
                "case_studies": [
                    {
                        "title": "Giám định và bồi thường thiệt hại sau cơn bão số 3 (Yagi) năm 2024",
                        "detail": "Các DNBH phi nhân thọ tại Việt Nam (Bảo Việt, PVI, PTI, PJICO) huy động toàn bộ giám định viên hiện trường, chi trả tạm ứng bồi thường hơn 11,000 tỷ đồng cho hàng nghìn nhà xưởng, tàu bè và phương tiện bị tàn phá bởi siêu bão Yagi."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Tổn thất Tổng hợp (Aggregate Claims Theory): Phân phối Hỗn hợp Poisson Tổng hợp (Compound Poisson Process) và xấp xỉ Panjer Recursion.",
                "Đo lường Rủi ro Đuôi Cực trị bằng Extreme Value Theory (EVT): Định lý Pickands-Balkema-de Haan và Mô hình Generalized Pareto Distribution (GPD).",
                "Kỹ thuật Phụ thuộc Phi tuyến (Non-linear Dependence) giữa các rủi ro thảm họa sử dụng Archimedean Copulas (Clayton, Gumbel)."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt về phạm vi bảo hiểm giữa ba điều kiện bảo hiểm hàng hóa quốc tế ICC (A), ICC (B) và ICC (C)?",
            "Trình bày nguyên tắc nguyên nhân trực tiếp (Proximate Cause) trong giải quyết bồi thường tổn thất bảo hiểm phi nhân thọ?",
            "Chứng minh công thức truy hồi Panjer cho phân phối tổn thất tổng hợp và giải thích ứng dụng trong mô phỏng rủi ro thảm họa thiên tai?"
        ]
    )
    
    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Nghiệp vụ Bảo hiểm Nhân thọ và Quản lý Rủi ro Tuổi thọ",
        introduction="Chương 4 đi sâu vào các sản phẩm bảo hiểm nhân thọ hiện đại, kỹ thuật xây dựng bảng tỷ lệ tử vong Actuary và chiến lược quản lý rủi ro già hóa dân số đối với các quỹ hưu trí.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Cấu trúc sản phẩm bảo hiểm nhân thọ",
                "content": (
                    "Bảo hiểm nhân thọ là hợp đồng bảo đảm quyền lợi tài chính cho người thụ hưởng khi người được bảo hiểm qua đời hoặc sống sót đến một độ tuổi nhất định. "
                    "Các sản phẩm nhân thọ truyền thống gồm: Bảo hiểm tử kỳ (Term Life - chỉ chi trả khi người được bảo hiểm tử vong trong thời hạn hợp đồng, phí rẻ không tích lũy); "
                    "Bảo hiểm sinh kỳ (Pure Endowment - chi trả khi người được bảo hiểm còn sống đến ngày đáo hạn); và Bảo hiểm hỗn hợp (Endowment - kết hợp bảo vệ và tiết kiệm).\n\n"
                    "Sản phẩm bảo hiểm liên kết đầu tư (Unit-Linked và Universal Life) tách bạch phí bảo hiểm thành hai phần: "
                    "Phần bảo vệ rủi ro tử vong và Phần mang đi đầu tư vào các quỹ cổ phiếu/trái phiếu do khách hàng tự lựa chọn và chấp nhận rủi ro đầu tư."
                ),
                "formulas": [
                    "Giá trị hoàn lại của hợp đồng nhân thọ: Cash Value = Dự phòng toán học tích lũy - Phí hủy hợp đồng trước hạn",
                    "Định phí thuần bảo hiểm tử kỳ n năm: A^1_{x:n|} = sum_{t=0}^{n-1} [ v^{t+1} * {}_t p_x * q_{x+t} ] (với v = 1/(1+i))"
                ],
                "case_studies": [
                    {
                        "title": "Chuyển dịch cơ cấu sản phẩm bảo hiểm nhân thọ tại Việt Nam",
                        "detail": "Doanh thu phí bảo hiểm liên kết chung (Universal Life) và liên kết đơn vị (Unit-Linked) đã vượt qua các sản phẩm hỗn hợp truyền thống, chiếm trên 85% tổng doanh thu khai thác mới của thị trường nhân thọ Việt Nam."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Bảng tỷ lệ tử vong và định phí toán học Actuary",
                "content": (
                    "Bảng tỷ lệ tử vong (Mortality Table) là bảng thống kê xác suất sống sót (p_x) và xác suất tử vong (q_x) của một nhóm dân cư chuẩn tại từng độ tuổi x. "
                    "Chuyên viên định phí (Actuary) sử dụng bảng tử vong kết hợp với tỷ suất lãi suất kỹ thuật (Technical Interest Rate) "
                    "để tính toán Phí bảo hiểm thuần (Net Premium) theo nguyên tắc cân bằng tương đương: Giá trị hiện tại của phí bảo hiểm thu về trong tương lai "
                    "phải bằng giá trị hiện tại của quyền lợi bảo hiểm dự kiến chi trả."
                ),
                "formulas": [
                    "Quan hệ xác suất sống và chết: p_x + q_x = 1",
                    "Xác suất một người x tuổi sống thêm t năm: {}_t p_x = l_{x+t} / l_x",
                    "Ký hiệu giao hoán Actuary: D_x = v^x * l_x, C_x = v^{x+1} * d_x, M_x = sum_{k=x}^w C_k, N_x = sum_{k=x}^w D_k"
                ],
                "case_studies": [
                    {
                        "title": "Ban hành Bảng tỷ lệ tử vong chuẩn CSO Việt Nam",
                        "detail": "Cục Quản lý, Giám sát Bảo hiểm ban hành bảng tỷ lệ tử vong chuẩn phản ánh tuổi thọ trung bình người Việt Nam đạt trên 73.6 tuổi, làm căn cứ bắt buộc để các công ty nhân thọ định phí và trích lập dự phòng nghiệp vụ."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Động học Dự báo Tỷ lệ Tử vong Lee-Carter (1992): ln(m_{x,t}) = alpha_x + beta_x * kappa_t + epsilon_{x,t} với kappa_t là chỉ số tử vong thời gian.",
                "Mô hình Cairns-Blake-Dowd (CBD 2006) hai nhân tố cho độ tuổi cao và Quản trị Rủi ro Tuổi thọ (Longevity Risk).",
                "Chứng khoán hóa Rủi ro Bảo hiểm (Insurance-Linked Securities): Trái phiếu Thảm họa (Catastrophe Bonds) và Longevity Swaps trên thị trường vốn quốc tế."
            ]
        },
        review_questions=[
            "Phân tích cơ chế hoạt động của sản phẩm bảo hiểm nhân thọ liên kết đơn vị (Unit-Linked) và chỉ ra sự phân chia rủi ro đầu tư giữa khách hàng và công ty bảo hiểm?",
            "Trình bày phương pháp tính toán phí bảo hiểm thuần niên kim nhân thọ trọn đời chi trả đầu kỳ (a_x) bằng hệ thống ký hiệu giao hoán D_x và N_x?",
            "Thiết lập mô hình Lee-Carter và ước lượng tham số kappa_t bằng phương pháp Phân rã Giá trị Suy biến (Singular Value Decomposition - SVD) trên dữ liệu tử vong?"
        ]
    )
    
    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Định phí Bảo hiểm, Trích lập Dự phòng và Tái Bảo hiểm (Reinsurance)",
        introduction="Chương 5 hoàn thiện các nghiệp vụ cốt lõi của khoa học Actuary: Phương pháp ước tính dự phòng bồi thường chưa phát sinh (IBNR), kỹ thuật chuyển dịch rủi ro qua tái bảo hiểm và chuẩn mực IFRS 17.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Trích lập dự phòng nghiệp vụ và phương pháp Chain Ladder",
                "content": (
                    "Dự phòng nghiệp vụ là khoản tiền mà doanh nghiệp bảo hiểm bắt buộc phải trích lập để bảo đảm khả năng thanh toán các trách nhiệm bảo hiểm đã cam kết. "
                    "Trong bảo hiểm phi nhân thọ, hai quỹ dự phòng quan trọng nhất là: Dự phòng phí chưa được hưởng (Unearned Premium Reserve - UPR) "
                    "và Dự phòng bồi thường (Loss Reserve) gồm Dự phòng cho các vụ tổn thất đã phát sinh nhưng chưa giải quyết (OSLR) "
                    "và Dự phòng tổn thất đã phát sinh nhưng chưa khai báo (Incurred But Not Reported - IBNR).\n\n"
                    "Phương pháp Tam giác tổn thất Chain Ladder (Mack 1993) là công cụ thống kê chuẩn mực để ngoại suy hệ số phát triển tổn thất lũy kế qua các năm."
                ),
                "formulas": [
                    "Hệ số phát triển tổn thất: f_j = sum_{i=1}^{n-j} C_{i, j+1} / sum_{i=1}^{n-j} C_{i, j}",
                    "Tổn thất cuối cùng dự phóng: C_{i, n} = C_{i, n-i+1} * prod_{j=n-i+1}^{n-1} f_j",
                    "Dự phòng bồi thường IBNR = Tổn thất cuối cùng dự kiến - Tổng bồi thường lũy kế đã ghi nhận"
                ],
                "case_studies": [
                    {
                        "title": "Chuyển đổi chuẩn mực kế toán IFRS 17 tại ngành bảo hiểm Việt Nam",
                        "detail": "Chuẩn mực IFRS 17 thay thế IFRS 4, loại bỏ việc ghi nhận toàn bộ doanh thu phí bảo hiểm tại ngày phát hành, yêu cầu tách bạch dòng tiền thực tế, điều chỉnh rủi ro phi tài chính (Risk Adjustment) và phân bổ Biên lợi nhuận dịch vụ bảo hiểm (CSM) suốt thời gian hợp đồng."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Nghiệp vụ tái bảo hiểm và phân tán rủi ro toàn cầu",
                "content": (
                    "Tái bảo hiểm (Reinsurance) là bảo hiểm cho chính các doanh nghiệp bảo hiểm (bảo hiểm lần hai). "
                    "Tái bảo hiểm cho phép công ty bảo hiểm gốc mở rộng năng lực nhận bảo hiểm vượt quá quy mô vốn chủ sở hữu, "
                    "bảo vệ doanh nghiệp trước các tổn thất thảm họa lớn và ổn định biên lợi nhuận kinh doanh.\n\n"
                    "Hai phương thức hợp đồng tái bảo hiểm: Tái bảo hiểm tỷ lệ (Proportional: Quota Share chia theo tỷ lệ cố định, Surplus chia theo mức giữ lại - Retention Line); "
                    "và Tái bảo hiểm phi tỷ lệ (Non-Proportional: Excess of Loss bồi thường phần tổn thất vượt quá mức tự giữ)."
                ),
                "formulas": [
                    "Mức giữ lại tối đa: Retention Limit = max(Capital * k, Legal Maximum 10% Vốn chủ sở hữu theo Luật KDBH)",
                    "Phân bổ Surplus Reinsurance: Tỷ lệ nhượng tái = (Số tiền bảo hiểm - Mức giữ lại) / Số tiền bảo hiểm"
                ],
                "case_studies": [
                    {
                        "title": "Vai trò điều tiết của Tổng công ty Cổ phần Tái bảo hiểm Quốc gia Việt Nam (VINARE)",
                        "detail": "VINARE giữ vai trò trung tâm trong nước nhận tái bảo hiểm từ các công ty bảo hiểm phi nhân thọ nội địa và thu xếp nhượng tái bảo hiểm ra các thị trường tài chính quốc tế hàng đầu (Munich Re, Swiss Re, Hannover Re)."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Phá sản Cổ điển Cramér-Lundberg (Ruin Theory): Quá trình thặng dư U(t) = u + c*t - sum_{i=1}^{N(t)} X_i và Bất đẳng thức Lundberg cho Xác suất Phá sản psi(u) <= e^{-R*u}.",
                "Mô hình Khung Solvency II: Định lượng Yêu cầu Vốn Khả năng Thanh toán (SCR) dựa trên Thước đo Giá trị Chịu rủi ro VaR 99.5% trong khoảng thời gian 1 năm.",
                "Biên Dịch vụ Hợp đồng (Contractual Service Margin - CSM) theo IFRS 17 và Mô hình Dòng tiền Thực hiện (Building Block Approach - BBA)."
            ]
        },
        review_questions=[
            "Trình bày thuật toán của Phương pháp Tam giác tổn thất Chain Ladder để ước tính dự phòng tổn thất đã phát sinh nhưng chưa thông báo (IBNR)?",
            "Phân biệt sự khác nhau căn bản giữa hợp đồng tái bảo hiểm Quota Share và hợp đồng tái bảo hiểm Excess of Loss?",
            "Chứng minh hệ số điều chỉnh Lundberg R thỏa mãn phương trình E[e^{R*X - R*c*T}] = 1 và phân tích ý nghĩa của nó đối với an toàn vốn của công ty bảo hiểm?"
        ]
    )
    
    pages, sz = b.save(out_pdf)
    print(f"[SUCCESS] Book 6 saved: {out_pdf} ({pages} pages, {sz:.2f} MB)")
    return {
        "title": title,
        "code": subject_code,
        "author": authors,
        "path": out_pdf,
        "pages": pages,
        "size_mb": round(sz, 2)
    }

if __name__ == "__main__":
    build_kdbh()
