# -*- coding: utf-8 -*-
"""
Generator for Textbook 8:
[NEU] Tài chính quốc tế - PGS.TS Nguyễn Thị Quy (NXB ĐHKTQD)
"""
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_tcqt():
    title = "Tài chính quốc tế"
    subject_code = "TCQT1101"
    faculty = "Viện Ngân hàng - Tài chính / Khoa Kinh tế quốc tế"
    authors = "PGS.TS. Nguyễn Thị Quy & PGS.TS. Đinh Xuân Trình (Đồng Chủ biên)"
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\05_Tài chính Quốc tế\[NEU] Tài chính quốc tế - PGS.TS Nguyễn Thị Quy (NXB ĐHKTQD)"
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Tài chính quốc tế - PGS.TS Nguyễn Thị Quy (NXB ĐHKTQD).pdf")
    
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
            "chapter_title": "Tổng quan Môi trường Tài chính Quốc tế và Hệ thống Tiền tệ Toàn cầu",
            "topics": [
                "Bản chất và phạm vi nghiên cứu của tài chính quốc tế trong bối cảnh toàn cầu hóa",
                "Lịch sử tiến hóa của hệ thống tiền tệ quốc tế: Bản vị vàng (Gold Standard), Hệ thống Bretton Woods và Hệ thống tỷ giá thả nổi hậu 1973",
                "Các tổ chức tài chính quốc tế trụ cột: Quỹ Tiền tệ Quốc tế (IMF), Ngân hàng Thế giới (World Bank) và Ngân hàng Thanh toán Quốc tế (BIS)",
                "Chuyên đề Tiến sĩ: Tam nan Bất khả thi (Mundell-Fleming Impossible Trinity) và Lý thuyết Khu vực Đồng tiền Tối ưu (Optimum Currency Areas) của Mundell"
            ]
        },
        {
            "chapter_num": "2",
            "chapter_title": "Cán cân Thanh toán Quốc tế (BOP) và Cân bằng Kinh tế Vĩ mô",
            "topics": [
                "Nguyên tắc hạch toán ghi sổ kép và cấu trúc tài khoản BOP: Cán cân vãng lai (CA), Cán cân tài chính (FA), Cán cân vốn (KA) và Sai số ròng",
                "Mối liên hệ giữa cán cân vãng lai và các đại lượng tiết kiệm - đầu tư vĩ mô quốc gia",
                "Cơ chế tự điều chỉnh và các chính sách can thiệp của chính phủ nhằm tái lập cân bằng cán cân thanh toán",
                "Chuyên đề Tiến sĩ: Lý thuyết Cán cân Vãng lai Liên thời gian (Intertemporal Approach to the Current Account) của Obstfeld & Rogoff"
            ]
        },
        {
            "chapter_num": "3",
            "chapter_title": "Thị trường Ngoại hối và Các Điều kiện Ngang giá Quốc tế",
            "topics": [
                "Cấu trúc thị trường ngoại hối (Forex): Giao dịch giao ngay (Spot), Kỳ hạn (Forward), Hoán đổi (Swap), Tương lai (Futures) và Quyền chọn (Options)",
                "Ngang giá Sức mua (Purchasing Power Parity - PPP): Dạng tuyệt đối và Dạng tương đối",
                "Ngang giá Lãi suất có bảo hiểm (Covered Interest Parity - CIP) và Ngang giá Lãi suất không bảo hiểm (Uncovered Interest Parity - UIP)",
                "Chuyên đề Tiến sĩ: Hiện tượng Tỷ giá Hối đoái Biến động Quá đà (Exchange Rate Overshooting Model) của Dornbusch (1976)"
            ]
        },
        {
            "chapter_num": "4",
            "chapter_title": "Quản trị Rủi ro Tỷ giá trong Doanh nghiệp Đa quốc gia (MNCs)",
            "topics": [
                "Phân loại rủi ro tỷ giá: Rủi ro giao dịch (Transaction Exposure), Rủi ro chuyển đổi kế toán (Translation Exposure) và Rủi ro kinh tế (Economic/Operating Exposure)",
                "Các kỹ thuật phòng ngừa rủi ro nội bộ: Kết hợp tiền tệ, Bù trừ đa phương (Multilateral Netting), Điều khoản điều chỉnh giá",
                "Các công cụ tài chính phái sinh phòng ngừa rủi ro ngoại hối: Hợp đồng kỳ hạn, Hoán đổi tiền tệ chéo (Cross-Currency Swap) và Hợp đồng quyền chọn",
                "Chuyên đề Tiến sĩ: Định giá Hợp đồng Quyền chọn Ngoại hối Garman-Kohlhagen (1983) và Độ lệch Ngang giá Lãi suất CIP trong Khủng hoảng"
            ]
        },
        {
            "chapter_num": "5",
            "chapter_title": "Thị trường Vốn Quốc tế, Đầu tư Trực tiếp Nước ngoài và Khủng hoảng Nợ",
            "topics": [
                "Thị trường Eurocurrency, Thị trường Eurobond và Trái phiếu quốc tế (Yankee, Samurai, Trái phiếu Chính phủ Việt Nam)",
                "Chiến lược đầu tư quốc tế và đa dạng hóa danh mục tài sản toàn cầu",
                "Khủng hoảng nợ công và tái cơ cấu nợ quốc gia tại các thị trường mới nổi",
                "Chuyên đề Tiến sĩ: Mô hình Khủng hoảng Tiền tệ Thế hệ 1 (Krugman 1979), Thế hệ 2 (Obstfeld 1994) và Chu kỳ Tài chính Toàn cầu (Global Financial Cycle) theo Hélène Rey"
            ]
        }
    ]
    b.add_table_of_contents(toc_data)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Tổng quan Môi trường Tài chính Quốc tế và Hệ thống Tiền tệ Toàn cầu",
        introduction="Chương 1 giới thiệu bức tranh tổng thể về tài chính quốc tế, phân tích các nấc thang lịch sử của hệ thống tiền tệ thế giới và các thách thức về phối hợp chính sách kinh tế vĩ mô toàn cầu.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bản chất của tài chính quốc tế và dòng vốn xuyên biên giới",
                "content": (
                    "Tài chính quốc tế là môn khoa học nghiên cứu các luồng vận động của vốn, tiền tệ và tài sản tài chính xuyên qua biên giới các quốc gia. "
                    "So với tài chính doanh nghiệp nội địa, tài chính quốc tế có thêm hai biến số rủi ro then chốt: Rủi ro tỷ giá hối đoái (Exchange Rate Risk) "
                    "và Rủi ro chính trị / rủi ro quốc gia (Sovereign / Country Risk).\n\n"
                    "Dòng chu chuyển vốn toàn cầu bao gồm: Dòng vốn thương mại hàng hóa và dịch vụ; Dòng vốn đầu tư trực tiếp (FDI) xây dựng nhà máy; "
                    "và Dòng vốn đầu tư gián tiếp (FII) mua bán cổ phiếu, trái phiếu và phái sinh trên các trung tâm tài chính quốc tế."
                ),
                "formulas": [
                    "Cân bằng dòng tiền quốc tế: Net Capital Inflows = Investment - National Savings",
                    "Độ mở tài chính quốc tế: Financial Openness = (Foreign Assets + Foreign Liabilities) / GDP * 100%"
                ],
                "case_studies": [
                    {
                        "title": "Hội nhập tài chính quốc tế của Việt Nam",
                        "detail": "Việt Nam gia nhập WTO (2007) và tham gia các hiệp định thương mại tự do thế hệ mới (CPTPP, EVFTA, RCEP), mở cửa thị trường dịch vụ tài chính, ngân hàng và thu hút hàng trăm tỷ USD vốn đầu tư quốc tế."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Sự tiến hóa của hệ thống tiền tệ quốc tế",
                "content": (
                    "Lịch sử hệ thống tiền tệ quốc tế trải qua bốn giai đoạn: "
                    "1. Chế độ Bản vị vàng cổ điển (1875-1914): Các đồng tiền neo cố định vào vàng theo hàm lượng vàng chính thức, tỷ giá tự động cân bằng qua cơ chế Price-Specie-Flow của David Hume; "
                    "2. Giai đoạn hỗn loạn giữa hai cuộc đại chiến thế giới (1914-1944) với chính sách phá giá tiền tệ để ăn cướp việc làm láng giềng (Beggar-thy-neighbor);\n\n"
                    "3. Hệ thống Bretton Woods (1944-1971): Đồng USD neo vào vàng tại mức 35 USD/ounce, các đồng tiền khác neo vào USD trong biên độ hẹp +/-1%; "
                    "4. Hệ thống Tỷ giá Thả nổi hậu Bretton Woods (Hiệp định Jamaica 1976 đến nay) với sự trỗi dậy của đồng Euro và xu thế phi đô la hóa (De-dollarization)."
                ),
                "formulas": [
                    "Cơ chế Hume: Thặng dư thương mại -> Vàng chảy vào -> Cung tiền tăng -> Giá cả P tăng -> Xuất khẩu giảm, Nhập khẩu tăng -> Cán cân BOP tự cân bằng",
                    "Nghịch lý Triffin (Triffin Dilemma): Mỹ phải chịu thâm hụt BOP liên tục để cung cấp thanh khoản USD cho thế giới, nhưng điều này lại làm suy giảm niềm tin vào khả năng đổi USD ra vàng."
                ],
                "case_studies": [
                    {
                        "title": "Cú sốc Nixon năm 1971 và sự sụp đổ của Hệ thống Bretton Woods",
                        "detail": "Ngày 15/08/1971, Tổng thống Mỹ Richard Nixon đơn phương tuyên bố đình chỉ việc chuyển đổi đồng USD ra vàng, chính thức chấm dứt kỷ nguyên Bretton Woods và mở ra thời kỳ tỷ giá thả nổi tự do trên toàn thế giới."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Tam nan Bất khả thi (Mundell-Fleming Trilemma): Một quốc gia không thể duy trì đồng thời ba mục tiêu: (1) Ổn định Tỷ giá hối đoái, (2) Tự do Luân chuyển Vốn, và (3) Độc lập Chính sách Tiền tệ.",
                "Lý thuyết Khu vực Đồng tiền Tối ưu (Optimum Currency Areas - OCA) của Robert Mundell (1961): Bốn điều kiện để liên minh tiền tệ (như Eurozone) vận hành bền vững.",
                "Thách thức Thuyết Tam nan Mới: Hélène Rey (2013) chứng minh rằng trong điều kiện Chu kỳ Tài chính Toàn cầu (Global Financial Cycle), thế giới thực tế chỉ là Dilemma (Chỉ có thể chọn giữa Tự do Vốn hoặc Độc lập CSTT, bất kể chế độ tỷ giá)."
            ]
        },
        review_questions=[
            "Phân tích Nghịch lý Triffin và giải thích nguyên nhân kinh tế học sâu xa dẫn tới sự sụp đổ của Hệ thống tiền tệ Bretton Woods năm 1971?",
            "Trình bày nội dung của Tam nan Bất khả thi (Trilemma) và chỉ ra lựa chọn chính sách tiền tệ - tỷ giá của Ngân hàng Nhà nước Việt Nam hiện nay?",
            "Thiết lập mô hình Mundell-Fleming và phân tích tác động của chính sách tài khóa mở rộng trong điều kiện tỷ giá thả nổi và vốn luân chuyển hoàn hảo?"
        ]
    )
    
    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Cán cân Thanh toán Quốc tế (BOP) và Cân bằng Kinh tế Vĩ mô",
        introduction="Chương 2 hướng dẫn phương pháp hạch toán cán cân thanh toán quốc tế theo cẩm nang BPM6 của IMF, giải thích mối quan hệ biện chứng giữa cán cân vãng lai, thâm hụt kép và các chính sách điều chỉnh vĩ mô.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Cấu trúc và nguyên tắc hạch toán cán cân thanh toán (BOP)",
                "content": (
                    "Cán cân thanh toán quốc tế (Balance of Payments - BOP) là bản báo cáo thống kê tổng hợp toàn bộ các giao dịch kinh tế "
                    "giữa người cư trú (Residents) và người không cư trú (Non-residents) của một quốc gia trong một thời kỳ xác định. "
                    "BOP được ghi chép theo nguyên tắc bút toán kép (Double-entry Bookkeeping): Mọi giao dịch phát sinh luồng tiền vào được ghi Có (+), "
                    "mọi luồng tiền ra được ghi Nợ (-).\n\n"
                    "Cấu trúc BOP gồm ba tài khoản chính: 1. Cán cân Vãng lai (Current Account - CA: Thương mại hàng hóa, Dịch vụ, Thu nhập sơ cấp, Thu nhập thứ cấp/Kiều hối); "
                    "2. Cán cân Vốn (Capital Account - KA: Chuyển giao vốn đơn phương); "
                    "3. Cán cân Tài chính (Financial Account - FA: Dòng vốn FDI, FII, Vay trả nợ nước ngoài ròng, Phái sinh tài chính)."
                ),
                "formulas": [
                    "Nguyên lý cân bằng tổng thể: Current Account (CA) + Capital Account (KA) + Financial Account (FA) + Net Errors & Omissions = Delta FX_Reserves",
                    "Đồng nhất thức thu nhập quốc dân mở: CA = (S_private - I) + (T - G) = Tiết kiệm quốc gia ròng - Đầu tư tư nhân"
                ],
                "case_studies": [
                    {
                        "title": "Thặng dư cán cân vãng lai và nguồn kiều hối kỷ lục tại Việt Nam",
                        "detail": "Việt Nam liên tục duy trì thặng dư cán cân vãng lai ấn tượng (trên 15-20 tỷ USD/năm) nhờ xuất siêu thương mại lớn và lượng kiều hối hàng năm đạt từ 16-19 tỷ USD, củng cố nguồn dự trữ ngoại hối quốc gia."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Thâm hụt cán cân thanh toán và cơ chế điều chỉnh vĩ mô",
                "content": (
                    "Thâm hụt cán cân vãng lai kéo dài báo hiệu một quốc gia đang tiêu dùng và đầu tư vượt quá khả năng tiết kiệm nội tại, "
                    "bắt buộc phải tài trợ bằng cách vay nợ nước ngoài hoặc bán tài sản quốc gia. Hiện tượng Thâm hụt Kép (Twin Deficits) "
                    "xảy ra khi thâm hụt ngân sách chính phủ (G - T > 0) dẫn thẳng tới thâm hụt cán cân vãng lai (CA < 0).\n\n"
                    "Chính phủ có thể áp dụng các chính sách điều chỉnh: Chính sách giảm chi tiêu (Expenditure-reducing policies bằng thắt chặt tài khóa/tiền tệ); "
                    "hoặc Chính sách chuyển hướng chi tiêu (Expenditure-switching policies bằng phá giá đồng nội tệ)."
                ),
                "formulas": [
                    "Điều kiện Marshall-Lerner: Phá giá nội tệ chỉ cải thiện cán cân thương mại khi tổng độ co giãn của cầu xuất khẩu và nhập khẩu lớn hơn 1: |eta_x| + |eta_m| > 1",
                    "Hiệu ứng đường cong chữ J (J-Curve Effect): Sau khi phá giá, cán cân thương mại xấu đi trong ngắn hạn do hợp đồng cũ cố định giá, trước khi cải thiện trong dài hạn."
                ],
                "case_studies": [
                    {
                        "title": "Hiệu ứng J-Curve sau các đợt điều chỉnh tỷ giá trung tâm của NHNN",
                        "detail": "Dữ liệu xuất nhập khẩu của Việt Nam xác nhận sự tồn tại của hiệu ứng J-curve: Trong 1-2 quý đầu sau khi điều chỉnh tỷ giá VND/USD, nhập khẩu tính bằng VND tăng làm thâm hụt tạm thời trước khi năng lực cạnh tranh xuất khẩu tăng vọt."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Cán cân Vãng lai Liên thời gian (Intertemporal Current Account Model) của Sachs (1981) và Obstfeld & Rogoff (1995): CA như quyết định làm mịn tiêu dùng (Consumption Smoothing).",
                "Kiểm định Điều kiện Marshall-Lerner và Hiệu ứng J-Curve bằng Mô hình Phân phối Trễ Tự hồi quy Phi tuyến (Non-linear ARDL - NARDL).",
                "Hiện tượng Tắc nghẽn Dòng vốn Quốc tế Đột ngột (Sudden Stops of Capital Inflows) theo Calvo (1998) tại các nền kinh tế mới nổi."
            ]
        },
        review_questions=[
            "Trình bày cấu trúc chi tiết của Cán cân thanh toán quốc tế (BOP) và giải thích tại sao tổng đại số của BOP luôn bằng 0 theo nguyên tắc kế toán?",
            "Phân tích Điều kiện Marshall-Lerner và cơ chế hình thành Hiệu ứng đường cong chữ J (J-Curve) sau khi một quốc gia phá giá đồng tiền?",
            "Xây dựng mô hình tối ưu hóa tiêu dùng liên thời gian hai kỳ của hộ gia đình đại diện và chứng minh phương trình cán cân vãng lai theo Obstfeld-Rogoff?"
        ]
    )
    
    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Thị trường Ngoại hối và Các Điều kiện Ngang giá Quốc tế",
        introduction="Chương 3 khảo sát cấu trúc vận hành của thị trường ngoại hối quốc tế 24/7, phân tích các điều kiện cân bằng lý thuyết then chốt kết nối tỷ giá, lạm phát và lãi suất giữa các quốc gia.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Cấu trúc và nghiệp vụ trên thị trường ngoại hối",
                "content": (
                    "Thị trường ngoại hối (Forex) là thị trường tài chính phi tập trung (OTC) lớn nhất hành tinh với doanh số giao dịch vượt 7.5 nghìn tỷ USD/ngày. "
                    "Các chủ thể tham gia chủ yếu gồm: Các ngân hàng đại lý tạo lập thị trường (Tier 1 Market Makers), các NHTW, các quỹ đầu cơ tiền tệ và các tập đoàn đa quốc gia.\n\n"
                    "Phương thức yết giá tỷ giá gồm Yết giá trực tiếp (Direct Quotation: 1 đơn vị ngoại tệ = x đơn vị nội tệ) "
                    "và Yết giá gián tiếp (Indirect Quotation). Các giao dịch phái sinh kỳ hạn (Forward) và hoán đổi (Swap) "
                    "chiếm tỷ trọng chi phối trong việc phòng ngừa rủi ro tỷ giá của các định chế tài chính."
                ),
                "formulas": [
                    "Quy tắc chéo tính tỷ giá: E(VND/EUR) = E(VND/USD) * E(USD/EUR)",
                    "Điểm kỳ hạn (Forward Points): Forward_Points = Forward_Rate - Spot_Rate"
                ],
                "case_studies": [
                    {
                        "title": "Cơ chế điều hành tỷ giá trung tâm USD/VND hàng ngày của NHNN",
                        "detail": "NHNN công bố Tỷ giá trung tâm mỗi sáng dựa trên 3 trụ cột: Diễn biến tỷ giá liên ngân hàng, Chỉ số USD Index đo sức mạnh đồng USD trên thị trường thế giới và Cân đối vĩ mô tiền tệ trong nước, với biên độ dao động +/- 5%."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Hệ thống các điều kiện ngang giá quốc tế",
                "content": (
                    "Bốn điều kiện ngang giá quốc tế thiết lập mối liên kết lý thuyết hoàn hảo giữa thị trường hàng hóa và thị trường tiền tệ: "
                    "1. Ngang giá Sức mua (PPP): Tỷ giá hối đoái điều chỉnh phản ánh chênh lệch lạm phát giữa hai nước (E_t / E_0 = (1 + pi) / (1 + pi*)); "
                    "2. Ngang giá Lãi suất có bảo hiểm (CIP): Chênh lệch tỷ giá kỳ hạn phản ánh chính xác chênh lệch lãi suất thị trường tiền tệ;\n\n"
                    "3. Ngang giá Lãi suất không bảo hiểm (UIP): Tỷ lệ thay đổi tỷ giá giao ngay kỳ vọng bằng chênh lệch lãi suất; "
                    "4. Hiệu ứng Fisher Quốc tế (IFE): Lãi suất danh nghĩa chênh lệch phản ánh tỷ lệ lạm phát kỳ vọng."
                ),
                "formulas": [
                    "Ngang giá Lãi suất có bảo hiểm (CIP): F / S = (1 + i_domestic) / (1 + i_foreign)",
                    "Ngang giá Lãi suất không bảo hiểm (UIP): E(S_{t+1}) / S_t = (1 + i_domestic) / (1 + i_foreign)",
                    "Chiến lược kinh doanh chênh lệch lãi suất (Carry Trade): Vay đồng tiền lãi suất thấp (JPY) đầu tư vào đồng tiền lãi suất cao khi UIP bị vi phạm"
                ],
                "case_studies": [
                    {
                        "title": "Sự đứt gãy của Ngang giá Lãi suất có bảo hiểm (CIP Deviation) sau khủng hoảng 2008",
                        "detail": "Do các quy định ngặt nghèo của Basel III về an toàn bảng cân đối và chi phí tiếp cận thanh khoản USD liên ngân hàng, chỉ số Cross-Currency Basis Spread âm kéo dài, tạo ra cơ hội kinh doanh chênh lệch giá nhưng không thể lấp đầy."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Tỷ giá Biến động Quá đà (Overshooting Model) của Rudiger Dornbusch (1976): Giá cả hàng hóa kết dính trong ngắn hạn khiến tỷ giá hối đoái phải phản ứng quá mức trước cú sốc cung tiền để dọn sạch thị trường tiền tệ.",
                "Bí ẩn Phá vỡ UIP (Forward Premium Puzzle) của Fama (1984): Kiểm định thực nghiệm hệ số beta âm trong hồi quy Fama và Giải thích bằng Phần bù Rủi ro Ngoại hối (Time-varying Risk Premium).",
                "Mô hình Vi mô Thị trường Ngoại hối và Dòng lệnh Đặt cọc (Order Flow) theo Evans & Lyons (2002)."
            ]
        },
        review_questions=[
            "Phân tích cơ chế kinh doanh chênh lệch lãi suất có phòng ngừa (Covered Interest Arbitrage - CIA) khi điều kiện CIP bị vi phạm?",
            "Trình bày chi tiết Mô hình Dornbusch Overshooting (1976) và giải thích tại sao tỷ giá hối đoái lại biến động dữ dội hơn các biến số kinh tế vĩ mô cơ bản?",
            "Thiết lập mô hình hồi quy Fama kiểm định Forward Premium Puzzle và thảo luận về các lý giải dựa trên tài chính hành vi?"
        ]
    )
    
    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Quản trị Rủi ro Tỷ giá trong Doanh nghiệp Đa quốc gia (MNCs)",
        introduction="Chương 4 cung cấp khung chiến lược nhận diện, đo lường và phòng ngừa ba loại rủi ro hối đoái của các tập đoàn đa quốc gia và các doanh nghiệp xuất nhập khẩu.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Nhận diện và phân loại rủi ro tỷ giá",
                "content": (
                    "Biến động tỷ giá hối đoái tác động trực tiếp đến dòng tiền, lợi nhuận và giá trị thị trường của doanh nghiệp quốc tế. "
                    "Ba loại rủi ro tỷ giá gồm: "
                    "1. Rủi ro Giao dịch (Transaction Exposure): Rủi ro phát sinh từ các hợp đồng đã ký kết bằng ngoại tệ có thời gian thanh toán trong tương lai (hợp đồng xuất khẩu, nhập khẩu, vay nợ ngoại tệ);\n\n"
                    "2. Rủi ro Chuyển đổi Kế toán (Translation Exposure): Rủi ro phát sinh khi hợp nhất báo cáo tài chính của các công ty con ở nước ngoài về đồng tiền của công ty mẹ (theo chuẩn IAS 21); "
                    "3. Rủi ro Kinh tế / Rủi ro Hoạt động (Operating Exposure): Rủi ro biến động tỷ giá làm suy giảm năng lực cạnh tranh dài hạn và hiện giá dòng tiền hoạt động tương lai của doanh nghiệp."
                ),
                "formulas": [
                    "Rủi ro giao dịch dòng tiền ròng: Net Exposure = (Dòng thu ngoại tệ dự kiến) - (Dòng chi ngoại tệ dự kiến)",
                    "Độ nhạy rủi ro hoạt động: Beta_exposure = Cov(CF_t, Delta S_t) / Var(Delta S_t)"
                ],
                "case_studies": [
                    {
                        "title": "Tổn thất tỷ giá tại Tổng công ty Điện lực Dầu khí Việt Nam (POW)",
                        "detail": "POW gánh chịu các khoản lỗ chênh lệch tỷ giá hàng trăm tỷ đồng trong các năm đồng USD và EUR tăng giá mạnh do các khoản vay nợ quốc tế bằng ngoại tệ lớn để đầu tư các nhà máy nhiệt điện Vũng Áng và Nhơn Trạch."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Chiến lược và kỹ thuật phòng ngừa rủi ro hối đoái",
                "content": (
                    "Doanh nghiệp áp dụng kết hợp các biện pháp phòng ngừa nội bộ và công cụ tài chính phái sinh: "
                    "Kỹ thuật nội bộ bao gồm: Bù trừ đa phương (Multilateral Netting giữa các công ty con trong tập đoàn); "
                    "Đẩy nhanh hoặc trì hoãn thanh toán (Leading and Lagging); và Điều khoản chia sẻ rủi ro tỷ giá (Currency Risk Sharing Clause).\n\n"
                    "Kỹ thuật phòng ngừa bằng thị trường tài chính gồm: Hợp đồng kỳ hạn Forward (khóa chặt tỷ giá thanh toán); "
                    "Hợp đồng quyền chọn Currency Options (bảo hiểm rủi ro bất lợi nhưng vẫn giữ lại cơ hội hưởng lợi nếu tỷ giá biến động thuận lợi); "
                    "và Nghiệp vụ phòng hộ bằng thị trường tiền tệ (Money Market Hedge)."
                ),
                "formulas": [
                    "Chi phí phòng ngừa bằng hợp đồng Forward: Cost = (Forward_Rate - Current_Spot) / Current_Spot * 100%",
                    "Money Market Hedge cho khoản phải thu ngoại tệ: Vay ngoại tệ ngay hôm nay -> Đổi ra nội tệ gửi ngân hàng -> Dùng tiền thu từ khách hàng trả nợ gốc ngoại tệ"
                ],
                "case_studies": [
                    {
                        "title": "Chiến lược phòng hộ tỷ giá của Tập đoàn Dệt may Việt Nam (Vinatex)",
                        "detail": "Vinatex thực hiện chính sách 'tự nhiên phòng hộ' (Natural Hedging) bằng cách cân đối dòng tiền thu bằng USD từ xuất khẩu hàng may mặc để chi trả trực tiếp cho việc nhập khẩu bông, xơ sợi và máy móc thiết bị dệt."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Phòng hộ Rủi ro Doanh nghiệp Tối ưu (Corporate Hedging Theory) của Froot, Scharfstein & Stein (1993): Phòng ngừa rủi ro hối đoái giảm chi phí tài trợ bên ngoài và bảo đảm khả năng đầu tư nội bộ.",
                "Định giá Quyền chọn Ngoại hối theo Mô hình Garman-Kohlhagen (1983): C = S*e^{-r_f*T}*N(d1) - K*e^{-r_d*T}*N(d2).",
                "Đo lường Rủi ro Hoạt động Đa quốc gia (Operating Exposure) bằng Mô hình Hồi quy Đa nhân tố Có kiểm soát Biến số Ngành (Jorion 1990)."
            ]
        },
        review_questions=[
            "Phân tích sự khác nhau căn bản giữa Rủi ro giao dịch (Transaction Exposure) và Rủi ro hoạt động (Operating Exposure)?",
            "Trình bày chi tiết bốn bước thực hiện Nghiệp vụ phòng hộ bằng thị trường tiền tệ (Money Market Hedge) đối với một khoản phải trả nhập khẩu bằng ngoại tệ?",
            "Chứng minh công thức định giá quyền chọn ngoại hối Garman-Kohlhagen (1983) và giải thích tại sao tỷ suất sinh lời của đồng ngoại tệ r_f đóng vai trò tương tự như tỷ suất cổ tức liên tục?"
        ]
    )
    
    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Thị trường Vốn Quốc tế, Đầu tư Trực tiếp Nước ngoài và Khủng hoảng Nợ",
        introduction="Chương 5 hoàn thiện giáo trình với việc nghiên cứu thị trường trái phiếu quốc tế, chiến lược đa dạng hóa danh mục toàn cầu, giải phẫu các mô hình khủng hoảng tiền tệ và quản lý nợ công quốc gia.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Thị trường vốn quốc tế và phát hành trái phiếu xuyên biên giới",
                "content": (
                    "Thị trường vốn quốc tế cung cấp cơ hội tiếp cận nguồn vốn khổng lồ với chi phí rẻ hơn thị trường nội địa. "
                    "Thị trường Eurocurrency (tiền gửi bằng đồng tiền nằm ngoài quốc gia phát hành, ví dụ Eurodollar) "
                    "và Thị trường Eurobond (trái phiếu phát hành tại thị trường quốc tế không chịu sự quản lý của một chính phủ đơn lẻ) "
                    "là hai động lực cốt lõi dẫn truyền vốn toàn cầu.\n\n"
                    "Phát hành Trái phiếu Quốc tế Chính phủ và Trái phiếu Xanh xuyên biên giới (Green Bonds) "
                    "giúp thiết lập đường cong lãi suất tham chiếu quốc gia và đa dạng hóa cơ cấu nhà đầu tư tổ chức."
                ),
                "formulas": [
                    "Phần bù rủi ro quốc gia: Emerging Market Bond Index Spread (EMBI Spread) = Yield_VN_Bond - Yield_US_Treasury",
                    "Chi phí vốn chủ sở hữu quốc tế: r_e = R_f,world + beta_world * ERP_world + Country_Risk_Premium"
                ],
                "case_studies": [
                    {
                        "title": "Các đợt phát hành thành công Trái phiếu Quốc tế của Chính phủ Việt Nam",
                        "detail": "Việt Nam phát hành thành công các lô Trái phiếu Chính phủ kỳ hạn 10 năm tại Sở Giao dịch Chứng khoán New York (NYSE), thu hút sự tham gia của các quỹ quản lý tài sản hàng đầu thế giới với mức chênh lệch lãi suất (Spread) rất cạnh tranh."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Các thế hệ mô hình khủng hoảng tiền tệ và nợ công",
                "content": (
                    "Lịch sử tài chính quốc tế ghi nhận ba thế hệ mô hình giải thích khủng hoảng tiền tệ: "
                    "Thế hệ 1 (Krugman 1979): Khủng hoảng bắt nguồn từ sự bất nhất giữa chính sách tài khóa thâm hụt kéo dài và cam kết duy trì tỷ giá cố định, dẫn tới dự trữ ngoại hối cạn kiệt; "
                    "Thế hệ 2 (Obstfeld 1994): Khủng hoảng tự ứng nghiệm (Self-fulfilling Crises) nảy sinh từ kỳ vọng đầu cơ khi chính phủ cân nhắc giữa chi phí bảo vệ tỷ giá và chi phí thất nghiệp tăng cao;\n\n"
                    "Thế hệ 3 (Krugman 1999, Aghion et al.): Khủng hoảng bảng cân đối tài chính (Balance Sheet Effects) do đòn bẩy nợ ngoại tệ quá lớn kết hợp với sự đổ vỡ của hệ thống ngân hàng nội địa (Twin Crises: Khủng hoảng ngân hàng và khủng hoảng tiền tệ)."
                ),
                "formulas": [
                    "Mô hình Krugman: Thời điểm tấn công đầu cơ t* xuất hiện khi Shadow Exchange Rate S_shadow(t*) = Fixed Rate S_bar",
                    "Chỉ số dễ tổn thương nợ công: Debt_Sustainability = (r - g) * Debt_{t-1} - Primary_Balance_t"
                ],
                "case_studies": [
                    {
                        "title": "Bài học từ Khủng hoảng Tài chính Tiền tệ Đông Á năm 1997",
                        "detail": "Bắt đầu từ sự sụp đổ của đồng Baht Thái Lan ngày 02/07/1997, cuộc khủng hoảng lan truyền chóng mặt sang Indonesia, Malaysia, Hàn Quốc do cấu trúc nợ ngắn hạn bằng USD quá lớn trong khi dự trữ ngoại hối quốc gia mỏng manh."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Chu kỳ Tài chính Toàn cầu (Global Financial Cycle - GFC) của Miranda-Agrippino & Rey (2020): Biến số VIX và Chính sách Tiền tệ của Cục Dự trữ Liên bang Mỹ (Fed) chi phối dòng vốn toàn cầu.",
                "Mô hình Vỡ nợ Quốc gia Chiến lược (Sovereign Default) theo Eaton & Gersovitz (1981) và Arellano (2008): Tối ưu hóa quyết định vỡ nợ khi chi phí bị loại khỏi thị trường vốn quốc tế nhỏ hơn chi phí trả nợ.",
                "Mô hình Phân tích Khả năng Bền vững Nợ (Debt Sustainability Analysis - DSA) của IMF/WB kết hợp Mô phỏng Ngẫu nhiên Fan Chart."
            ]
        },
        review_questions=[
            "Phân tích cơ chế tấn công đầu cơ vào đồng tiền định giá cao trong Mô hình Khủng hoảng Tiền tệ Thế hệ 1 của Paul Krugman?",
            "Tại sao hiệu ứng bảng cân đối tài chính (Balance Sheet Effects) lại biến việc phá giá đồng tiền từ công cụ kích thích xuất khẩu thành cú sốc phá sản hàng loạt của doanh nghiệp trong Khủng hoảng Đông Á 1997?",
            "Trình bày luận điểm của Hélène Rey về Chu kỳ Tài chính Toàn cầu (GFC) và thảo luận về các biện pháp kiểm soát dòng vốn (Capital Flow Management - CFM) của các nước đang phát triển?"
        ]
    )
    
    pages, sz = b.save(out_pdf)
    print(f"[SUCCESS] Book 8 saved: {out_pdf} ({pages} pages, {sz:.2f} MB)")
    return {
        "title": title,
        "code": subject_code,
        "author": authors,
        "path": out_pdf,
        "pages": pages,
        "size_mb": round(sz, 2)
    }

if __name__ == "__main__":
    build_tcqt()
