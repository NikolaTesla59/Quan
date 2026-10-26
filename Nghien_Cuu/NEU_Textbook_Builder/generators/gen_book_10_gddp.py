# -*- coding: utf-8 -*-
"""
Generator for Textbook 10:
[NEU] Giao dịch & Đàm phán quốc tế - PGS.TS Lê Thị Thu Hà (NXB ĐHKTQD)
"""
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_gddp():
    title = "Giao dịch & Đàm phán quốc tế"
    subject_code = "GDDP1103"
    faculty = "Khoa Kinh doanh quốc tế / Khoa Thương mại & Kinh tế quốc tế"
    authors = "PGS.TS. Lê Thị Thu Hà & PGS.TS. Nguyễn Thị Hường (Đồng Chủ biên)"
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\05_Tài chính Quốc tế\[NEU] Giao dịch & Đàm phán quốc tế - PGS.TS Lê Thị Thu Hà (NXB ĐHKTQD)"
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Giao dịch & Đàm phán quốc tế - PGS.TS Lê Thị Thu Hà (NXB ĐHKTQD).pdf")
    
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
            "chapter_title": "Tổng quan Giao dịch Thương mại Quốc tế và Môi trường Kinh doanh Toàn cầu",
            "topics": [
                "Bản chất, đặc trưng và các xu thế phát triển của thương mại quốc tế trong kỷ nguyên số",
                "Môi trường kinh doanh quốc tế đa chiều: Môi trường kinh tế, pháp lý, chính trị và rủi ro chuỗi cung ứng",
                "Hàng rào thuế quan và phi thuế quan: Quy tắc xuất xứ, Tiêu chuẩn kỹ thuật (TBT), Kiểm dịch động thực vật (SPS)",
                "Chuyên đề Tiến sĩ: Lý thuyết Chi phí Giao dịch (Transaction Cost Economics) của Williamson và Ranh giới của Doanh nghiệp Quốc tế"
            ]
        },
        {
            "chapter_num": "2",
            "chapter_title": "Các Phương thức Giao dịch Thương mại Quốc tế Thông dụng",
            "topics": [
                "Xuất nhập khẩu trực tiếp và gián tiếp (Ủy thác xuất nhập khẩu, Môi giới ngoại thương)",
                "Buôn bán đối lưu (Counter-trade): Hàng đổi hàng (Barter), Mua bù (Counterpurchase), Mua lại sản phẩm (Buyback)",
                "Đấu thầu quốc tế (International Bidding): Đấu thầu rộng rãi, Đấu thầu hạn chế, Mua sắm công theo chuẩn WTO/GPA",
                "Giao dịch gia công quốc tế (Outward/Inward Processing) và Tái xuất khẩu (Re-export / Transit Trade)",
                "Chuyên đề Tiến sĩ: Mô hình Chuỗi Giá trị Toàn cầu (Global Value Chains) và Nâng cấp Năng lực Doanh nghiệp Nội địa"
            ]
        },
        {
            "chapter_num": "3",
            "chapter_title": "Lý thuyết Nền tảng và Chu trình Đàm phán Kinh doanh Quốc tế",
            "topics": [
                "Bản chất của đàm phán: Quá trình tương tác giải quyết mâu thuẫn nhằm đạt được thỏa thuận cùng có lợi (Win-Win)",
                "Các khái niệm đàm phán cốt lõi: BATNA (Phương án thay thế tốt nhất), Giá bảo lưu (Reservation Price), Vùng thỏa thuận khả thi (ZOPA)",
                "Chu trình đàm phán 4 giai đoạn chuẩn mực: Chuẩn bị thông tin -> Mở đầu tiếp xúc -> Thảo luận thương lượng -> Ký kết và Theo dõi thực hiện",
                "Chuyên đề Tiến sĩ: Giải pháp Thương lượng Nash (Nash Bargaining Solution) và Mô hình Đàm phán Trả giá Luân phiên Rubinstein (1982)"
            ]
        },
        {
            "chapter_num": "4",
            "chapter_title": "Chiến lược, Nghệ thuật Thương lượng và Giao tiếp Xuyên Văn hóa",
            "topics": [
                "Đàm phán phân bổ (Distributive Negotiation) vs Đàm phán tích hợp (Integrative Negotiation)",
                "Nghệ thuật nhượng bộ, chiến thuật xử lý bế tắc (Deadlock) và các bẫy tâm lý trong đàm phán",
                "Giao tiếp xuyên văn hóa trong đàm phán kinh doanh quốc tế: Phong cách đàm phán Mỹ, Châu Âu, Nhật Bản, Trung Quốc và Trung Đông",
                "Chuyên đề Tiến sĩ: Khung Lý thuyết Thứ nguyên Văn hóa Hofstede và Mô hình Định hướng Giá trị Trompenaars"
            ]
        },
        {
            "chapter_num": "5",
            "chapter_title": "Soạn thảo, Ký kết Hợp đồng Ngoại thương và Giải quyết Tranh chấp",
            "topics": [
                "Công ước Viên 1980 về Hợp đồng Mua bán Hàng hóa Quốc tế (CISG): Quy định về chào hàng (Offer), chấp nhận chào hàng (Acceptance) và vi phạm cơ bản (Fundamental Breach)",
                "Cấu trúc các điều khoản chủ yếu của hợp đồng ngoại thương: Tên hàng, Số lượng, Chất lượng, Giá cả, Thanh toán, Giao hàng, Bất khả kháng (Force Majeure)",
                "Các phương thức giải quyết tranh chấp quốc tế: Thương lượng, Hòa giải (Mediation), Tòa án quốc gia và Trọng tài Thương mại Quốc tế (VIAC, SIAC, ICC)",
                "Hiệu lực công nhận và cho thi hành phán quyết trọng tài nước ngoài theo Công ước New York 1958",
                "Chuyên đề Tiến sĩ: Lý thuyết Trò chơi Hành vi (Behavioral Game Theory) và Cơ chế Trọng tài Tối ưu"
            ]
        }
    ]
    b.add_table_of_contents(toc_data)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Tổng quan Giao dịch Thương mại Quốc tế và Môi trường Kinh doanh Toàn cầu",
        introduction="Chương 1 giới thiệu bức tranh toàn cảnh về giao dịch thương mại quốc tế trong kỷ nguyên chuyển đổi số và chuỗi cung ứng mở rộng, phân tích các rào cản thương mại kỹ thuật và môi trường kinh doanh toàn cầu.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bản chất và động lực của giao dịch thương mại quốc tế",
                "content": (
                    "Giao dịch thương mại quốc tế là hoạt động mua bán hàng hóa, cung cấp dịch vụ và chuyển giao công nghệ "
                    "vượt qua ranh giới lãnh thổ quốc gia giữa các chủ thể kinh doanh có trụ sở thương mại ở các quốc gia khác nhau. "
                    "Động lực thúc đẩy giao dịch quốc tế bắt nguồn từ Lợi thế so sánh (David Ricardo), Lợi thế tuyệt đối (Adam Smith) "
                    "và Lý thuyết Tỷ lệ các yếu tố sản xuất Heckscher-Ohlin-Samuelson (H-O-S).\n\n"
                    "Thương mại điện tử xuyên biên giới (Cross-border E-commerce) qua các nền tảng B2B (như Alibaba, Amazon Global Selling) "
                    "đang tái định hình phương thức giao dịch truyền thống, rút ngắn khoảng cách giữa nhà sản xuất nội địa và người tiêu dùng quốc tế."
                ),
                "formulas": [
                    "Quy luật Lợi thế So sánh: Quốc gia A chuyên môn hóa xuất khẩu mặt hàng có chi phí cơ hội thấp hơn: (C_x / C_y)_A < (C_x / C_y)_B",
                    "Độ mở thương mại quốc gia: Trade Openness = (Export + Import) / GDP * 100% (Việt Nam đạt gần 180-200% GDP)"
                ],
                "case_studies": [
                    {
                        "title": "Bùng nổ xuất khẩu thương mại điện tử xuyên biên giới của doanh nghiệp Việt Nam",
                        "detail": "Hàng nghìn doanh nghiệp nhỏ và vừa (SMEs) Việt Nam trong các ngành thủ công mỹ nghệ, may mặc, nông sản đã xuất khẩu trực tiếp hàng hóa trị giá hàng tỷ USD đến khách hàng Bắc Mỹ và châu Âu thông qua nền tảng Amazon."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Môi trường chính sách và các rào cản thương mại",
                "content": (
                    "Khi các hiệp định thương mại tự do (FTA) xóa bỏ thuế quan nhập khẩu về 0%, các quốc gia nhập khẩu chuyển mạnh sang dựng lên "
                    "các rào cản phi thuế quan (Non-Tariff Barriers - NTBs) tinh vi để bảo hộ sản xuất trong nước. "
                    "Các rào cản chủ yếu gồm: Tiêu chuẩn Hàng rào Kỹ thuật trong Thương mại (TBT), Biện pháp Vệ sinh Dịch tễ và Kiểm dịch Động thực vật (SPS), "
                    "và các biện pháp Phòng vệ thương mại (Chống bán phá giá - Anti-dumping, Chống trợ cấp - Countervailing, Tự vệ thương mại - Safeguards).\n\n"
                    "Đặc biệt, Cơ chế Điều chỉnh Biên giới Carbon của EU (CBAM) và Quy định Chống phá rừng (EUDR) "
                    "đang đặt ra thách thức sinh tử đối với hàng xuất khẩu của các nước đang phát triển."
                ),
                "formulas": [
                    "Biên độ bán phá giá: Dumping Margin = (Giá trị thông thường tại nước xuất khẩu - Giá xuất khẩu) / Giá xuất khẩu * 100%",
                    "Thuế chống bán phá giá: Anti-dumping Duty = Dumping Margin được áp dụng để bù đắp thiệt hại vật chất cho ngành sản xuất nội địa"
                ],
                "case_studies": [
                    {
                        "title": "Các vụ điều tra chống bán phá giá đối với ngành thép và thủy sản Việt Nam",
                        "detail": "Doanh nghiệp xuất khẩu cá tra, tôm và tôn mạ của Việt Nam thường xuyên phải đối mặt với các đợt rà soát hành chính thuế chống bán phá giá (POR) khắt khe của Bộ Thương mại Hoa Kỳ (DOC), đòi hỏi hệ thống kế toán chi phí phải minh bạch chuẩn mực quốc tế."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Chi phí Giao dịch (Transaction Cost Economics - TCE) của Oliver Williamson (1985): Tính đặc thù của tài sản (Asset Specificity), Bất định (Uncertainty) và Tần suất giao dịch (Frequency) quyết định lựa chọn giữa Thị trường (Market), Hợp đồng lai (Hybrid) hay Tích hợp nội bộ (Hierarchy).",
                "Mô hình Lực hấp dẫn Thương mại Mở rộng (Structural Gravity Model of Trade) theo Anderson & van Wincoop (2003) kiểm soát Trở kháng Thương mại Đa phương (Multilateral Resistance).",
                "Tác động của Các Biện pháp Phi Thuế quan (NTMs) đến Tỷ lệ Sống sót của Hợp đồng Xuất khẩu (Export Duration Analysis) bằng Mô hình Đạo lượng Sinh tồn Cox Proportional Hazards."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt giữa hàng rào thuế quan và hàng rào phi thuế quan (TBT, SPS) trong thương mại quốc tế hiện đại?",
            "Quy định Chống phá rừng (EUDR) và Cơ chế Điều chỉnh Biên giới Carbon (CBAM) của EU tác động như thế nào đến các ngành xuất khẩu chủ lực của Việt Nam?",
            "Thiết lập mô hình Trọng lực Thương mại (Gravity Model) kiểm định tác động của Hiệp định EVFTA đến kim ngạch thương mại hai chiều giữa Việt Nam và các nước EU?"
        ]
    )
    
    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Các Phương thức Giao dịch Thương mại Quốc tế Thông dụng",
        introduction="Chương 2 phân tích cơ chế vận hành, quy trình ký kết và phòng ngừa rủi ro trong các phương thức giao dịch ngoại thương: Xuất nhập khẩu trực tiếp, Buôn bán đối lưu, Đấu thầu quốc tế và Gia công quốc tế.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Xuất nhập khẩu trực tiếp và buôn bán đối lưu (Counter-trade)",
                "content": (
                    "Xuất nhập khẩu trực tiếp là phương thức mà người bán và người mua trực tiếp quan hệ, đàm phán và ký kết hợp đồng "
                    "mà không qua bất kỳ thương nhân trung gian độc lập nào, giúp doanh nghiệp làm chủ thị trường và tối ưu hóa tỷ suất lợi nhuận.\n\n"
                    "Buôn bán đối lưu (Counter-trade) là phương thức giao dịch mà trong đó xuất khẩu kết hợp chặt chẽ với nhập khẩu, "
                    "người bán đồng thời là người mua, giá trị hàng giao cân bằng hoặc tương đương với giá trị hàng nhận về. "
                    "Các hình thức đối lưu phổ biến: Hàng đổi hàng cổ điển (Barter - không dùng tiền tệ); Mua bù (Counterpurchase - ký hai hợp đồng độc lập nhưng ràng buộc lẫn nhau); "
                    "và Mua lại sản phẩm (Buyback - cung cấp thiết bị máy móc và thu hồi vốn bằng chính sản phẩm sản xuất từ máy móc đó)."
                ),
                "formulas": [
                    "Cân bằng giá trị buôn bán đối lưu: sum (P_x * Q_x) = sum (P_m * Q_m) +/- Số dư thanh toán chuyển khoản quy ước",
                    "Tỷ lệ cam kết mua bù: Counterpurchase Commitment Ratio = Giá trị mua bù / Giá trị hợp đồng xuất khẩu gốc (thường từ 30% đến 100%)"
                ],
                "case_studies": [
                    {
                        "title": "Giao dịch hàng đổi hàng nông sản đổi phân bón giữa Việt Nam và các đối tác",
                        "detail": "Việt Nam thực hiện các hợp đồng đối lưu xuất khẩu gạo, cà phê để nhập khẩu phân bón kali, máy móc nông nghiệp từ Nga và Belarus trong các giai đoạn thiếu hụt dự trữ ngoại tệ tự do chuyển đổi."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Đấu thầu quốc tế và gia công quốc tế",
                "content": (
                    "Đấu thầu quốc tế (International Bidding) là phương thức giao dịch đặc biệt, trong đó người mua (Bên mời thầu) công bố trước các điều kiện mua hàng "
                    "để các nhà cung cấp quốc tế (Bên dự thầu) nộp hồ sơ cạnh tranh công khai theo các tiêu chí kỹ thuật và tài chính. "
                    "Quy trình đấu thầu gồm: Lập hồ sơ mời thầu (RFP/ITB) -> Mở thầu công khai -> Đánh giá hồ sơ dự thầu -> Thương thảo hợp đồng -> Trao thầu.\n\n"
                    "Gia công quốc tế (International Processing) là phương thức mà bên đặt gia công ở nước ngoài cung cấp máy móc, nguyên phụ liệu "
                    "cho bên nhận gia công trong nước để chế biến, sản xuất thành phẩm theo mẫu mã chỉ định và nhận thù lao gia công (CMP)."
                ),
                "formulas": [
                    "Tiêu chuẩn đánh giá tài chính đấu thầu: Evaluated Bid Price = Giá dự thầu +/- Điều chỉnh sai lệch kỹ thuật +/- Chi phí vòng đời vận hành (Life-cycle cost)",
                    "Phí gia công quốc tế: CMP = Chi phí cắt may (Cut & Make) + Chi phí đóng gói (Packing) + Lợi nhuận định mức"
                ],
                "case_studies": [
                    {
                        "title": "Chuyển dịch từ gia công thuần túy (CMT) sang phương thức FOB và ODM của ngành dệt may",
                        "detail": "Các tập đoàn dệt may lớn như May 10, Việt Tiến chủ động nâng cấp từ gia công thuần túy nhận nguyên liệu (CMT) sang phương thức mua nguyên liệu tự sản xuất bán FOB và tự thiết kế mẫu mã ODM để nâng cao biên lợi nhuận từ 5% lên 15-20%."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Đấu giá và Đấu thầu Ngược Quốc tế (Reverse Auctions): Nguy cơ Lời nguyền Người thắng thầu (Winner's Curse) và Mô hình Đấu thầu Cạnh tranh Điểm số (Scoring Auctions) theo Che (1993).",
                "Động thái Nâng cấp trong Chuỗi Giá trị Toàn cầu (Upgrading in GVCs) theo Gereffi (1999): Tiến trình từ Gia công Lắp ráp (OEM) sang Sản xuất Thiết kế (ODM) và Xây dựng Thương hiệu Gốc (OBM).",
                "Mô hình Hợp đồng Khuyến khích Tối ưu (Incentive Contracts) trong Gia công Xuyên Biên giới dưới Bất cân xứng Thông tin về Chi phí Nỗ lực."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt về cơ chế tài chính giữa hai hình thức buôn bán đối lưu: Hàng đổi hàng (Barter) và Mua bù (Counterpurchase)?",
            "Trình bày các tiêu chí đánh giá hồ sơ dự thầu quốc tế theo phương pháp Chấm điểm kết hợp Kỹ thuật và Giá (Quality and Cost Based Selection - QCBS)?",
            "Làm thế nào để các doanh nghiệp gia công Việt Nam vượt qua bẫy gia công giá trị gia tăng thấp (Smile Curve) để tiến lên các nấc thang cao hơn trong chuỗi cung ứng?"
        ]
    )
    
    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Lý thuyết Nền tảng và Chu trình Đàm phán Kinh doanh Quốc tế",
        introduction="Chương 3 xây dựng khung lý thuyết chuẩn tắc của đàm phán kinh doanh quốc tế theo trường phái Harvard (Principled Negotiation), làm chủ các khái niệm chiến lược BATNA, Reservation Price, ZOPA và chu trình đàm phán 4 bước.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Các khái niệm chiến lược trong đàm phán theo Trường phái Harvard",
                "content": (
                    "Đàm phán kinh doanh quốc tế là một quá trình tương tác giao tiếp chiến lược giữa hai hay nhiều bên đại diện cho các quốc gia khác nhau, "
                    "nhằm dung hòa các lợi ích mâu thuẫn và tạo lập một thỏa thuận chung ràng buộc pháp lý. "
                    "Trường phái Đàm phán Nguyên tắc của Harvard (Fisher & Ury) thiết lập các khái niệm mang tính định lượng chuẩn mực:\n\n"
                    "1. BATNA (Best Alternative to a Negotiated Agreement): Phương án thay thế tốt nhất có thể thực hiện nếu cuộc đàm phán hiện tại đổ vỡ. "
                    "BATNA quyết định sức mạnh đàm phán thực tế của một bên; "
                    "2. Giá bảo lưu (Reservation Price / Walk-away Point): Mức giới hạn cuối cùng mà một bên có thể chấp nhận, vượt qua mức này họ sẽ rời bỏ bàn đàm phán; "
                    "3. Vùng thỏa thuận khả thi (ZOPA - Zone of Possible Agreement): Khoảng không gian giao thoa giữa Giá bảo lưu của người mua và Giá bảo lưu của người bán."
                ),
                "formulas": [
                    "Vùng ZOPA tồn tại khi và chỉ khi: Reservation Price (Buyer) >= Reservation Price (Seller)",
                    "Thặng dư hợp tác đàm phán: Total Surplus = Reservation Price (Buyer) - Reservation Price (Seller) >= 0",
                    "Nguyên tắc vàng: Tuyệt đối không bao giờ ký kết một thỏa thuận có giá trị thấp hơn BATNA của mình."
                ],
                "case_studies": [
                    {
                        "title": "Xác định BATNA trong đàm phán xuất khẩu nông sản sang thị trường mới",
                        "detail": "Một công ty xuất khẩu tiêu của Việt Nam đàm phán giá với đối tác Trung Đông, nhờ có sẵn BATNA vững chắc là hợp đồng bao tiêu tại thị trường nội địa với giá sàn 120,000 VND/kg, doanh nghiệp đã tự tin từ chối mức ép giá của đối tác và giành được hợp đồng xuất khẩu giá cao."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Chu trình đàm phán kinh doanh quốc tế 4 giai đoạn",
                "content": (
                    "Một cuộc đàm phán quốc tế thành công đòi hỏi sự chuẩn bị công phu chiếm tới 70-80% thời lượng: "
                    "1. Giai đoạn Chuẩn bị: Thu thập thông tin đối tác, phân tích bối cảnh văn hóa, xác định mục tiêu tối đa - tối thiểu, thiết lập BATNA và thành lập đoàn đàm phán đa chức năng (luật sư, chuyên gia tài chính, kỹ thuật);\n\n"
                    "2. Giai đoạn Tiếp xúc và Mở đầu: Thiết lập mối quan hệ tin cậy ban đầu (Rapport), thăm dò mục đích ngầm và xác lập chương trình nghị sự (Agenda); "
                    "3. Giai đoạn Thảo luận và Nhượng bộ: Trình bày lập luận, đặt câu hỏi khai thác thông tin, thực hiện nhượng bộ có điều kiện ('Nếu bạn... thì tôi...'); "
                    "4. Giai đoạn Đạt thỏa thuận và Ký kết: Soạn thảo biên bản ghi nhớ (MOU) và ký kết hợp đồng chính thức bằng văn bản."
                ),
                "formulas": [
                    "Nguyên tắc nhượng bộ: Concession_i chỉ được đưa ra khi nhận lại Value_i tương đương: If (You agree on X) -> Then (We agree on Y)"
                ],
                "case_studies": [
                    {
                        "title": "Quá trình đàm phán Hiệp định EVFTA của phái đoàn thương mại Việt Nam",
                        "detail": "Trải qua 14 phiên đàm phán chính thức kéo dài gần 6 năm, phái đoàn Việt Nam đã chuẩn bị kỹ lưỡng các phương án đánh đổi lợi ích: Chấp nhận mở cửa thị trường mua sắm công và xe hơi dung tích lớn để đổi lấy lộ trình cắt giảm thuế quan 99% cho dệt may, giày dép và thủy sản sang EU."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Giải pháp Thương lượng Cân bằng Nash (Nash Bargaining Solution - NBS): Maximize [ u_1(x) - d_1 ]^{alpha} * [ u_2(x) - d_2 ]^{1 - alpha} với d_i là điểm bất đồng (Disagreement Point / BATNA).",
                "Mô hình Trả giá Luân phiên Rubinstein (1982) với Hệ số Chiết khấu Thời gian (Discount Factors delta_1, delta_2): Lợi thế của Người đưa ra Lời Đề nghị Đầu tiên (First-Mover Advantage).",
                "Đàm phán Đa Vấn đề (Multi-issue Bargaining) và Mô hình Tối ưu hóa Biên Pareto (Pareto Optimal Frontier) bằng Quy hoạch Phi tuyến."
            ]
        },
        review_questions=[
            "Phân tích mối quan hệ hữu cơ giữa BATNA, Giá bảo lưu (Reservation Price) và Vùng thỏa thuận khả thi (ZOPA)?",
            "Trình bày bốn nguyên tắc cốt lõi của Phương pháp Đàm phán Nguyên tắc Harvard (Getting to Yes) của Fisher & Ury?",
            "Chứng minh toán học Giải pháp Thương lượng Nash (1950) thỏa mãn bốn tiên đề đối xứng, bất biến thang đo, độc lập với các phương án không liên quan (IIA) và hiệu quả Pareto?"
        ]
    )
    
    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Chiến lược, Nghệ thuật Thương lượng và Giao tiếp Xuyên Văn hóa",
        introduction="Chương 4 cung cấp kho vũ khí chiến thuật thương lượng thực chiến, phân biệt đàm phán phân bổ và tích hợp, giải mã các bẫy đàm phán tâm lý và phân tích sự đa dạng văn hóa kinh doanh toàn cầu.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Chiến lược đàm phán phân bổ vs Đàm phán tích hợp",
                "content": (
                    "Chiến lược đàm phán phân bổ (Distributive Bargaining / Zero-Sum Game) xem cuộc đàm phán như việc phân chia một 'chiếc bánh cố định' (Fixed Pie): Lợi ích của một bên là thiệt hại trực tiếp của bên kia (thường xoay quanh một biến số giá cả). "
                    "Chiến thuật phân bổ tập trung vào việc thả neo giá đầu tiên (Anchoring), giấu kín giá bảo lưu và đưa ra nhượng bộ nhỏ giọt.\n\n"
                    "Ngược lại, Chiến lược đàm phán tích hợp (Integrative Bargaining / Win-Win) tìm cách 'mở rộng chiếc bánh' (Expand the Pie) bằng cách đưa thêm nhiều biến số vào bàn đàm phán "
                    "(kỳ hạn thanh toán, dịch vụ hậu mãi, bảo hành, hỗ trợ kỹ thuật, hợp đồng tương lai) để thực hiện các cuộc trao đổi giá trị khác nhau giữa hai bên (Logrolling)."
                ),
                "formulas": [
                    "Hiệu ứng Thả neo (Anchoring Bias): Mức giá đề nghị ban đầu P_anchor chi phối tâm lý và kéo mức giá cân bằng cuối cùng về phía người đưa ra neo: P_final = w * P_anchor + (1 - w) * P_fair",
                    "Kỹ thuật Logrolling: Đánh đổi biến số quan trọng đối với bên A nhưng ít tốn kém đối với bên B, và ngược lại."
                ],
                "case_studies": [
                    {
                        "title": "Áp dụng đàm phán tích hợp trong hợp đồng mua máy móc thiết bị y tế",
                        "detail": "Bên mua chấp nhận mức giá máy cao hơn dự kiến ban đầu để đổi lấy việc bên bán cam kết bảo hành miễn phí 5 năm, đào tạo chuyển giao công nghệ cho đội ngũ bác sĩ và cung ứng độc quyền phụ tùng thay thế với mức chiết khấu 40%."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Giao tiếp xuyên văn hóa trong đàm phán quốc tế",
                "content": (
                    "Văn hóa là lăng kính định hình nhận thức, tư duy và hành vi của nhà đàm phán. "
                    "Mô hình Ngữ cảnh Văn hóa của Edward T. Hall phân chia thế giới thành: "
                    "Văn hóa Ngữ cảnh Cao (High-Context Culture như Việt Nam, Nhật Bản, Trung Quốc): coi trọng mối quan hệ cá nhân lâu dài, giao tiếp gián tiếp tế nhị, tin tưởng ngầm định; "
                    "và Văn hóa Ngữ cảnh Thấp (Low-Context Culture như Mỹ, Đức, Thụy Sĩ): đề cao tính trực diện, logic, rõ ràng, tin tưởng tuyệt đối vào văn bản hợp đồng pháp lý.\n\n"
                    "Thấu hiểu phong cách đàm phán của từng quốc gia giúp tránh được các cú sốc văn hóa và xung đột không đáng có trên bàn thương thảo quốc tế."
                ),
                "formulas": [
                    "Các thứ nguyên văn hóa Hofstede: Khoảng cách quyền lực (PDI), Chủ nghĩa cá nhân (IDV), Né tránh bất định (UAI), Định hướng dài hạn (LTO)"
                ],
                "case_studies": [
                    {
                        "title": "Sự khác biệt văn hóa đàm phán giữa doanh nghiệp Việt Nam và đối tác Nhật Bản",
                        "detail": "Đối tác Nhật Bản thường đàm phán theo nhóm (Ringi System), mất nhiều thời gian để xây dựng sự tin cậy cá nhân (Nemawashi) và xin ý kiến đồng thuận tập thể trước khi ra quyết định, đòi hỏi doanh nghiệp Việt Nam phải kiên nhẫn và không được thúc ép ký hợp đồng vội vã."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Trò chơi Hành vi (Behavioral Game Theory) trong Đàm phán theo Camerer (2003): Vai trò của Tính Công bằng (Fairness), Sự Trừng phạt Kẻ Tham lam (Ultimatum Game) và Niềm tin Xã hội (Trust Game).",
                "Mô hình 7 Thứ nguyên Văn hóa của Trompenaars & Hampden-Turner: Chủ nghĩa phổ quát vs Chủ nghĩa đặc thù (Universalism vs Particularism) trong việc tuân thủ cam kết hợp đồng ngoại thương.",
                "Tác động của Bất cân xứng Cảm xúc (Emotional Asymmetry) và Trí tuệ Cảm xúc (Emotional Intelligence) đến Xác suất Đổ vỡ Đàm phán (Impasse)."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt bản chất giữa Chiến lược Đàm phán Phân bổ (Distributive) và Chiến lược Đàm phán Tích hợp (Integrative)?",
            "Trình bày lý thuyết Văn hóa Ngữ cảnh Cao (High-context) và Ngữ cảnh Thấp (Low-context) của Edward T. Hall và chỉ ra các lưu ý khi đàm phán với đối tác phương Tây?",
            "Trò chơi Tối hậu thư (Ultimatum Game) trong kinh tế học thực nghiệm chứng minh điều gì về hành vi từ chối thỏa thuận phi lý trí của con người?"
        ]
    )
    
    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Soạn thảo, Ký kết Hợp đồng Ngoại thương và Giải quyết Tranh chấp",
        introduction="Chương 5 hoàn thiện toàn bộ chuỗi nghiệp vụ giao dịch ngoại thương: Soạn thảo các điều khoản hợp đồng chuẩn mực theo Công ước CISG 1980 và các cơ chế giải quyết tranh chấp trọng tài quốc tế hiệu lực toàn cầu.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Soạn thảo hợp đồng ngoại thương và Công ước Viên 1980 (CISG)",
                "content": (
                    "Hợp đồng mua bán hàng hóa quốc tế (Sales Contract) là văn bản pháp lý tối cao xác lập quyền và nghĩa vụ của người bán và người mua. "
                    "Công ước Liên Hợp Quốc về Hợp đồng Mua bán Hàng hóa Quốc tế (CISG 1980 - Việt Nam chính thức là thành viên từ ngày 01/01/2017) "
                    "là nguồn luật thống nhất chi phối việc giao kết và thực hiện hợp đồng. "
                    "CISG quy định rõ nguyên tắc Chào hàng (Offer - phải đủ rõ ràng về tên hàng, số lượng, giá cả), "
                    "Chấp nhận chào hàng (Acceptance - có hiệu lực khi tới bên chào hàng, không chấp nhận im lặng làm bằng chứng đồng ý).\n\n"
                    "Bộ điều khoản cốt lõi của hợp đồng gồm: Tên hàng (Commodity), Số lượng (Quantity có dung sai), Phẩm chất (Quality), "
                    "Giá cả (Price kèm Incoterms), Thanh toán (Payment), Giao hàng (Shipment), Bất khả kháng (Force Majeure) và Khiếu nại (Claim)."
                ),
                "formulas": [
                    "Quy tắc Chấp nhận Chào hàng: Phản hồi có chứa điều kiện sửa đổi trọng yếu (giá, thanh toán, số lượng) bị coi là Từ chối và tạo thành một Hoàn trả Chào hàng (Counter-offer Điều 19 CISG)",
                    "Vi phạm cơ bản hợp đồng (Fundamental Breach Điều 25 CISG): Vi phạm làm cho bên kia bị thiệt hại nghiêm trọng đến mức tước đoạt điều mà họ có quyền kỳ vọng từ hợp đồng, cho phép bên bị vi phạm quyền hủy bỏ hợp đồng."
                ],
                "case_studies": [
                    {
                        "title": "Áp dụng điều khoản Bất khả kháng (Force Majeure) trong đại dịch Covid-19 và khủng hoảng kênh đào Suez",
                        "detail": "Nhiều doanh nghiệp xuất khẩu đã kích hoạt thành công điều khoản Bất khả kháng để miễn trừ trách nhiệm bồi thường phạt chậm giao hàng khi các cảng biển quốc tế bị phong tỏa kiểm dịch nghiêm ngặt theo khuyến nghị của Phòng Thương mại Quốc tế (ICC Force Majeure Clause 2020)."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Các phương thức giải quyết tranh chấp thương mại quốc tế",
                "content": (
                    "Khi tranh chấp ngoại thương phát sinh, các bên có thể lựa chọn 4 phương thức xử lý: "
                    "1. Thương lượng (Negotiation: tự dàn xếp không tốn kém); 2. Hòa giải (Mediation: có bên thứ ba trung gian trợ giúp); "
                    "3. Tòa án quốc gia (Litigation: công khai, thủ tục phức tạp, rất khó thi hành án ở nước ngoài); "
                    "và 4. Trọng tài Thương mại Quốc tế (International Commercial Arbitration) - phương thức được ưa chuộng nhất trong thương mại toàn cầu.\n\n"
                    "Ưu điểm vượt trội của Trọng tài: Thủ tục linh hoạt, bảo mật tuyệt đối, phán quyết có tính chung thẩm (Final and Binding), "
                    "và đặc biệt là Phán quyết trọng tài được công nhận và cho thi hành tại hơn 170 quốc gia theo Công ước New York năm 1958."
                ),
                "formulas": [
                    "Điều khoản Trọng tài Mẫu (Model Arbitration Clause): 'Mọi tranh chấp phát sinh từ hoặc liên quan đến hợp đồng này sẽ được giải quyết bằng trọng tài tại [VIAC / SIAC / ICC] theo Quy tắc trọng tài của trung tâm này... Luật áp dụng là [Luật Việt Nam / CISG], Ngôn ngữ trọng tài là [Tiếng Anh]...'"
                ],
                "case_studies": [
                    {
                        "title": "Giải quyết tranh chấp hợp đồng mua bán gạo tại Trung tâm Trọng tài Quốc tế Việt Nam (VIAC)",
                        "detail": "VIAC đã thụ lý và ban hành phán quyết trọng tài chung thẩm buộc nhà nhập khẩu châu Phi bồi thường toàn bộ thiệt hại và tiền lưu kho bãi cho doanh nghiệp xuất khẩu gạo Việt Nam do hành vi vô cớ hủy hợp đồng khi giá gạo thế giới sụt giảm."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Kinh tế về Pháp luật (Law and Economics) trong Tranh chấp Ngoại thương: Đo lường Thiệt hại Hiệu quả (Efficient Breach) và Bồi thường Kỳ vọng (Expectation Damages) theo CISG Điều 74.",
                "Cơ chế Thi hành Phán quyết Trọng tài Quốc tế theo Công ước New York 1958 và Ranh giới Trật tự Công cộng (Public Policy Defense).",
                "Ứng dụng Nền tảng Giải quyết Tranh chấp Trực tuyến (Online Dispute Resolution - ODR) và Thuật toán Phân xử Trí tuệ Nhân tạo trong Thương mại Điện tử Xuyên Biên giới."
            ]
        },
        review_questions=[
            "Thế nào là 'Vi phạm cơ bản hợp đồng' (Fundamental Breach) theo quy định của Điều 25 Công ước Viên 1980 (CISG) và hậu quả pháp lý của nó?",
            "So sánh ưu điểm và nhược điểm của Phương thức Giải quyết Tranh chấp bằng Trọng tài Thương mại Quốc tế so với Tòa án Quốc gia?",
            "Tại sao Công ước New York năm 1958 lại được coi là nền tảng pháp lý quan trọng nhất bảo đảm hiệu lực thực thi của các hợp đồng thương mại quốc tế?"
        ]
    )
    
    pages, sz = b.save(out_pdf)
    print(f"[SUCCESS] Book 10 saved: {out_pdf} ({pages} pages, {sz:.2f} MB)")
    return {
        "title": title,
        "code": subject_code,
        "author": authors,
        "path": out_pdf,
        "pages": pages,
        "size_mb": round(sz, 2)
    }

if __name__ == "__main__":
    build_gddp()
