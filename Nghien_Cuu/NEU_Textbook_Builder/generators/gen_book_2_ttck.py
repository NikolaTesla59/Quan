# -*- coding: utf-8 -*-
"""
Generator for Textbook 2:
[NEU] Thị trường chứng khoán - PGS.TS Nguyễn Đăng Dốt (NXB ĐHKTQD)
"""
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_ttck():
    title = "Thị trường chứng khoán"
    subject_code = "TTCK1102"
    faculty = "Viện Ngân hàng - Tài chính"
    authors = "PGS.TS. Nguyễn Đăng Dốt & PGS.TS. Đào Lê Minh (Đồng Chủ biên)"
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\01_Tài chính Doanh nghiệp & Đầu tư\[NEU] Thị trường chứng khoán - PGS.TS Nguyễn Đăng Dốt (NXB ĐHKTQD)"
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Thị trường chứng khoán - PGS.TS Nguyễn Đăng Dốt (NXB ĐHKTQD).pdf")
    
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
            "chapter_title": "Tổng quan Thị trường Chứng khoán và Cấu trúc Hệ thống Tài chính",
            "topics": [
                "Bản chất, chức năng kinh tế và lịch sử hình thành thị trường chứng khoán",
                "Hàng hóa trên thị trường chứng khoán: Cổ phiếu, trái phiếu, chứng chỉ quỹ, công cụ phái sinh",
                "Khung pháp lý điều hành: Luật Chứng khoán và vai trò của Ủy ban Chứng khoán Nhà nước (UBCKNN)",
                "Chuyên đề Tiến sĩ: Giả thuyết Thị trường Hiệu quả (EMH) của Fama và các thách thức tài chính hành vi"
            ]
        },
        {
            "chapter_num": "2",
            "chapter_title": "Thị trường Sơ cấp: Phát hành Chứng khoán và Bảo lãnh Phát hành",
            "topics": [
                "Cơ chế phát hành chứng khoán lần đầu ra công chúng (IPO) và phát hành riêng lẻ",
                "Quy trình bảo lãnh phát hành (Underwriting) và xác định giá chào bán (Bookbuilding)",
                "Cổ phần hóa doanh nghiệp nhà nước gắn với niêm yết trên HOSE và HNX",
                "Chuyên đề Tiến sĩ: Lý thuyết Định giá thấp IPO (IPO Underpricing Puzzle) và Bất cân xứng thông tin Rock (1986)"
            ]
        },
        {
            "chapter_num": "3",
            "chapter_title": "Thị trường Thứ cấp và Cấu trúc Vi mô Thị trường (Market Microstructure)",
            "topics": [
                "Nguyên tắc tổ chức giao dịch: Khớp lệnh định kỳ, khớp lệnh liên tục và giao dịch thỏa thuận",
                "Hệ thống công nghệ KRX và bù trừ thanh toán T+2 qua Tổng công ty Lưu ký và Bù trừ Chứng khoán (VSDC)",
                "Chỉ số thị trường (VN-Index, VN30, HNX-Index) và cơ chế biên độ dao động giá",
                "Chuyên đề Tiến sĩ: Động thái Sổ lệnh giới hạn (Limit Order Book), Chênh lệch Bid-Ask và Chi phí thông tin Roll (1984)"
            ]
        },
        {
            "chapter_num": "4",
            "chapter_title": "Định giá Tài sản Tài chính và Quản trị Danh mục Đầu tư",
            "topics": [
                "Mô hình chiết khấu dòng cổ tức (DDM) và dòng tiền tự do (FCFE, FCFF)",
                "Định giá trái phiếu: Đường cong lãi suất (Yield Curve), Duration và Convexity",
                "Lý thuyết Danh mục hiện đại Markowitz (MVO) và Đường biên hiệu quả (Efficient Frontier)",
                "Chuyên đề Tiến sĩ: Mô hình CAPM, Fama-French 3 và 5 nhân tố, và Carhart 4 nhân tố kiểm định GRS"
            ]
        },
        {
            "chapter_num": "5",
            "chapter_title": "Thị trường Chứng khoán Phái sinh và Chiến lược Quản trị Rủi ro",
            "topics": [
                "Hợp đồng tương lai chỉ số VN30: Cơ chế ký quỹ bù trừ và đòn bẩy tài chính",
                "Chứng quyền có bảo đảm (Covered Warrant) và hợp đồng quyền chọn (Options)",
                "Chiến lược phòng ngừa rủi ro (Delta Hedging, Cross Hedging, Protective Put)",
                "Chuyên đề Tiến sĩ: Mô hình Black-Scholes-Merton mở rộng với biến động ngẫu nhiên Heston và Jump-Diffusion"
            ]
        }
    ]
    b.add_table_of_contents(toc_data)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Tổng quan Thị trường Chứng khoán và Cấu trúc Hệ thống Tài chính",
        introduction="Chương 1 phân tích bản chất của thị trường chứng khoán trong vai trò dẫn vốn trung và dài hạn của nền kinh tế, phân loại các công cụ tài chính và làm rõ cơ chế giám sát an toàn thị trường.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bản chất và chức năng của thị trường chứng khoán",
                "content": (
                    "Thị trường chứng khoán là đỉnh cao của nền kinh tế hàng hóa tiền tệ phát triển, nơi các công cụ tài sản tài chính dài hạn "
                    "được mua bán, chuyển nhượng tự do. Thị trường thực hiện hai chức năng kinh tế then chốt: Chức năng huy động và phân bổ nguồn lực vốn, "
                    "và chức năng định giá tài sản tài chính thông qua cơ chế cung cầu thị trường khách quan.\n\n"
                    "Tại Việt Nam, sự ra đời của Trung tâm Giao dịch Chứng khoán TP.HCM (năm 2000) và Sở Giao dịch Chứng khoán Hà Nội (năm 2005) "
                    "đã đánh dấu bước ngoặt chuyển dịch mô hình hệ thống tài chính từ đơn cực (dựa hoàn toàn vào ngân hàng thương mại) sang mô hình đa cực hiện đại."
                ),
                "formulas": [
                    "Quy mô vốn hóa thị trường: Market Cap = sum_{i=1}^N (P_i * Q_i)",
                    "Mức độ thâm nhập tài chính: Financial Deepening = Market Cap / GDP * 100%"
                ],
                "case_studies": [
                    {
                        "title": "Mục tiêu nâng hạng thị trường chứng khoán Việt Nam lên Thị trường Mới nổi (Emerging Markets)",
                        "detail": "Việt Nam tích cực tháo gỡ vướng mắc ký quỹ trước giao dịch (Non-prefunding solution cho nhà đầu tư ngoại) nhằm thỏa mãn các tiêu chuẩn khắt khe của FTSE Russell và MSCI."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Các công cụ tài chính cơ bản trên thị trường",
                "content": (
                    "Cổ phiếu thường (Common Stock) trao quyền sở hữu, quyền biểu quyết và quyền nhận cổ tức thặng dư. "
                    "Cổ phiếu ưu đãi mang đặc tính lai tạp giữa nợ và vốn chủ sở hữu. "
                    "Trái phiếu doanh nghiệp và trái phiếu chính phủ là công cụ nợ cam kết chi trả lãi định kỳ và hoàn trả mệnh giá gốc khi đáo hạn.\n\n"
                    "Chứng chỉ quỹ đầu tư (Mutual Funds, ETFs) mở ra cơ hội đa dạng hóa danh mục cho các nhà đầu tư cá nhân có quy mô vốn nhỏ."
                ),
                "formulas": [
                    "Tỷ suất cổ tức: Dividend Yield = D_1 / P_0",
                    "Hệ số P/E toàn thị trường: P/E = Market Cap / Total Net Income"
                ],
                "case_studies": [
                    {
                        "title": "Sự bùng nổ của các quỹ hoán đổi danh mục ETF nội địa",
                        "detail": "Quỹ VFMVN Diamond ETF và VN30 ETF đã thu hút hàng tỷ USD vốn ngoại gián tiếp giải ngân vào các cổ phiếu hết 'room' ngoại như FPT, MWG, PNJ, REE."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Kiểm định Giả thuyết Thị trường Hiệu quả (EMH) dạng yếu, dạng vừa và dạng mạnh theo Fama (1970) bằng phương pháp Variance Ratio Test của Lo & MacKinlay.",
                "Tài chính Hành vi (Behavioral Finance): Mô hình Prospect Theory của Kahneman & Tversky (1979) giải thích hiện tượng sợ lỗ (Loss Aversion) và tâm lý bầy đàn (Herd Behavior).",
                "Cấu trúc mạng lưới liên thông tài chính (Financial Contagion Network) giữa thị trường chứng khoán và thị trường tiền tệ."
            ]
        },
        review_questions=[
            "Phân tích cơ chế phân bổ vốn của thị trường chứng khoán so với kênh tín dụng ngân hàng thương mại?",
            "Tại sao việc tháo gỡ nút thắt 'ký quỹ trước giao dịch' (Pre-funding) lại có ý nghĩa quyết định đối với việc nâng hạng thị trường?",
            "Trình bày phương pháp kiểm định tính bước đi ngẫu nhiên (Random Walk Hypothesis) của chuỗi chỉ số VN-Index?"
        ]
    )
    
    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Thị trường Sơ cấp: Phát hành Chứng khoán và Bảo lãnh Phát hành",
        introduction="Chương 2 nghiên cứu cơ chế vận hành của thị trường sơ cấp, quy trình chuẩn bị hồ sơ IPO, các phương pháp định giá chào bán và nghiệp vụ bảo lãnh phát hành của công ty chứng khoán.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Quy trình chào bán chứng khoán ra công chúng (IPO)",
                "content": (
                    "IPO là bước chuyển mình chiến lược đưa một công ty cổ phần đóng trở thành công ty đại chúng minh bạch, "
                    "mở rộng khả năng tiếp cận nguồn vốn rẻ và thanh khoản cao của xã hội. "
                    "Quy trình IPO bao gồm: Tái cơ cấu bảng cân đối tài chính, soạn thảo bản cáo bạch (Prospectus), kiểm toán theo chuẩn IFRS/VAS, "
                    "và đăng ký cấp phép với cơ quan quản lý nhà nước.\n\n"
                    "Phương thức dựng sổ (Bookbuilding) ngày càng phổ biến, giúp tổ chức bảo lãnh phát hành thăm dò nhu cầu thực của các nhà đầu tư tổ chức trước khi chốt giá phát hành chính thức."
                ),
                "formulas": [
                    "Tỷ suất sinh lời ngày đầu tiên của IPO: Initial Return = (P_close,day1 - P_offer) / P_offer * 100%",
                    "Hệ số pha loãng cổ phiếu: Dilution Factor = N_new / (N_old + N_new)"
                ],
                "case_studies": [
                    {
                        "title": "Kỷ lục huy động vốn IPO của Vinhomes (VHM) năm 2018",
                        "detail": "Vinhomes đã thực hiện thương vụ chào bán cổ phần quốc tế và niêm yết thu về 1.35 tỷ USD, trở thành một trong những thương vụ IPO lớn nhất Đông Nam Á thời điểm bấy giờ."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Nghiệp vụ bảo lãnh phát hành chứng khoán",
                "content": (
                    "Bảo lãnh phát hành là cam kết của tổ chức tài chính trung gian (thường là ngân hàng đầu tư hoặc công ty chứng khoán) "
                    "hỗ trợ tổ chức phát hành thực hiện các thủ tục trước khi chào bán và cam kết mua lại toàn bộ hoặc một phần số chứng khoán chưa phân phối hết.\n\n"
                    "Các hình thức bảo lãnh gồm: Bảo lãnh cam kết chắc chắn (Firm Commitment), bảo lãnh cố gắng tối đa (Best Efforts) "
                    "và bảo lãnh tất cả hoặc không (All-or-None)."
                ),
                "formulas": [
                    "Phí bảo lãnh phát hành: Spread = P_offer - P_paid_to_issuer",
                    "Tỷ lệ thành công đợt phát hành: Success Rate = Q_subscribed / Q_offered >= 70% theo quy định Luật Chứng khoán 2019"
                ],
                "case_studies": [
                    {
                        "title": "Bảo lãnh phát hành trái phiếu doanh nghiệp kèm chứng quyền",
                        "detail": "Công ty Chứng khoán Bản Việt (Vietcap) và SSI đã đóng vai trò tư vấn và bảo lãnh phát hành thành công nhiều lô trái phiếu chuyển đổi quy mô nghìn tỷ đồng cho các tập đoàn hạ tầng."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Winner's Curse của Rock (1986): Sự bất cân xứng thông tin giữa nhà đầu tư có thông tin (Informed) và không có thông tin (Uninformed) dẫn tới hiện tượng IPO Underpricing.",
                "Lý thuyết Tín hiệu (Signaling Theory) của Allen & Faulhaber (1989): Doanh nghiệp chất lượng cao cố tình định giá thấp IPO để tạo hiệu ứng tích cực cho các đợt phát hành cổ phiếu sau này (SEO).",
                "Chiến lược dựng sổ động (Dynamic Bookbuilding) và trích xuất thông tin riêng tư từ các quỹ đầu tư tổ chức."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt về phân bổ rủi ro giữa phương thức bảo lãnh cam kết chắc chắn và bảo lãnh cố gắng tối đa?",
            "Tại sao hiện tượng IPO Underpricing lại xảy ra phổ biến ở hầu hết các thị trường chứng khoán trên toàn thế giới?",
            "Xây dựng mô hình kinh tế lượng hồi quy đa biến kiểm định các yếu tố tác động đến tỷ suất sinh lời ngày đầu tiên của cổ phiếu IPO tại HOSE?"
        ]
    )
    
    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Thị trường Thứ cấp và Cấu trúc Vi mô Thị trường (Market Microstructure)",
        introduction="Chương 3 đi sâu vào bản chất vi mô của thị trường thứ cấp, giải mã cấu trúc sổ lệnh giới hạn, cơ chế khớp lệnh tự động, tính thanh khoản và tương tác chiến lược giữa các nhóm nhà đầu tư.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Cơ chế khớp lệnh và các loại lệnh giao dịch",
                "content": (
                    "Thị trường thứ cấp bảo đảm tính thanh khoản cho chứng khoán, cho phép nhà đầu tư chuyển đổi tài sản thành tiền mặt bất kỳ lúc nào. "
                    "Hệ thống giao dịch vận hành theo hai cơ chế: Khớp lệnh định kỳ (Call Auction) nhằm xác định giá mở cửa (ATO) và giá đóng cửa (ATC) "
                    "dựa trên nguyên tắc tối đa hóa khối lượng giao dịch; và khớp lệnh liên tục (Continuous Auction) theo thứ tự ưu tiên về giá và thời gian.\n\n"
                    "Các loại lệnh chuẩn gồm: Lệnh giới hạn (LO), lệnh thị trường (MP, MTL, MAK, MOK), lệnh điều kiện (Stop Loss, Trailing Stop)."
                ),
                "formulas": [
                    "Nguyên tắc xác định giá ATO/ATC: P* = argmax_P min(CumBuy(P), CumSell(P))",
                    "Chênh lệch giá mua bán: Bid-Ask Spread = Ask_price - Bid_price"
                ],
                "case_studies": [
                    {
                        "title": "Hiện tượng nghẽn lệnh trên sàn HOSE giai đoạn 2020-2021",
                        "detail": "Khi số lượng tài khoản mở mới F0 tăng vọt chạm giới hạn 900,000 lệnh/ngày của hệ thống cũ, thanh khoản bị phong tỏa, thúc đẩy Bộ Tài chính và FPT phối hợp triển khai giải pháp xử lý kỹ thuật tạm thời trước khi đưa KRX vào hoạt động."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Thanh khoản thị trường và tác động của giao dịch tần suất cao",
                "content": (
                    "Thanh khoản là khả năng giao dịch một khối lượng chứng khoán lớn trong thời gian nhanh nhất với chi phí trượt giá (Slippage) thấp nhất. "
                    "Độ sâu sổ lệnh (Market Depth) và độ phục hồi sổ lệnh (Resiliency) là hai thước đo quan trọng phản ánh sức chịu đựng của thị trường trước các cú sốc bán tháo.\n\n"
                    "Giao dịch thuật toán (Algorithmic Trading) và tạo lập thị trường tự động (Automated Market Making) "
                    "đang làm thay đổi căn bản cấu trúc vi mô thị trường toàn cầu."
                ),
                "formulas": [
                    "Tỷ số thanh khoản Amihud (2002): ILLIQ_t = (1/D) * sum_{d=1}^D ( |R_{t,d}| / Volume_{t,d} )",
                    "Độ sâu thị trường: Depth = 0.5 * (Qty_bid + Qty_ask) tại mức giá tốt nhất"
                ],
                "case_studies": [
                    {
                        "title": "Hiệu ứng phiên ATC ngày đáo hạn hợp đồng tương lai VN30",
                        "detail": "Sự chênh lệch vị thế phái sinh kích hoạt các đợt tái cơ cấu giỏ cổ phiếu vốn hóa lớn vào 15 phút cuối phiên ATC, gây biến động giật cục chỉ số VN30."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Vi mô Thị trường của Kyle (1985): Cân bằng Nash giữa Informed Trader, Noise Traders và Market Maker. Đo lường tham số Lambda (Price Impact of Trade).",
                "Mô hình Glosten & Milgrom (1985): Cập nhật xác suất Bayes trong sổ lệnh giới hạn và phân rã thành phần bất cân xứng thông tin trong Bid-Ask Spread.",
                "Ước lượng xác suất giao dịch nội gián PIN (Probability of Informed Trading) theo Easley, Kiefer & O'Hara (1996)."
            ]
        },
        review_questions=[
            "Phân tích thuật toán xác định giá khớp lệnh định kỳ tại phiên ATC của Sở Giao dịch Chứng khoán TP.HCM?",
            "Tại sao thước đo Amihud Illiquidity lại được sử dụng rộng rãi trong các nghiên cứu kinh tế lượng thực nghiệm về thị trường mới nổi?",
            "Trình bày mô hình Kyle (1985) và giải thích tại sao mức độ thanh khoản của thị trường tỷ lệ nghịch với mức độ biến động thông tin riêng tư?"
        ]
    )
    
    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Định giá Tài sản Tài chính và Quản trị Danh mục Đầu tư",
        introduction="Chương 4 trang bị các phương pháp định giá cổ phiếu, trái phiếu từ nền tảng chiết khấu dòng tiền đến các mô hình định giá đa nhân tố hiện đại (Asset Pricing Models) và tối ưu hóa danh mục đầu tư Markowitz.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phương pháp định giá chứng khoán vốn và chứng khoán nợ",
                "content": (
                    "Định giá cổ phiếu dựa trên giá trị nội tại (Intrinsic Value). Mô hình chiết khấu cổ tức tăng trưởng không đổi Gordon "
                    "áp dụng cho các công ty bão hòa, trong khi mô hình dòng tiền tự do cho vốn chủ sở hữu (FCFE) và phương pháp so sánh tương quan (P/E, P/B, EV/EBITDA) "
                    "thích hợp cho các doanh nghiệp tăng trưởng cao.\n\n"
                    "Đối với trái phiếu, giá trị được xác định bằng hiện giá của chuỗi Coupon định kỳ cộng với mệnh giá chiết khấu theo lãi suất đáo hạn (YTM). "
                    "Chỉ số Macaulay Duration và Convexity đo lường độ nhạy cảm của giá trái phiếu trước biến động của lãi suất thị trường."
                ),
                "formulas": [
                    "Mô hình Gordon: P_0 = D_1 / (r - g) = [ D_0 * (1 + g) ] / (r - g)",
                    "Macaulay Duration: D_mac = sum_{t=1}^T [ t * CF_t / (1 + YTM)^t ] / P_bond",
                    "Độ lồi Convexity: C = [ 1 / (P * (1+YTM)^2) ] * sum_{t=1}^T [ (t^2 + t) * CF_t / (1 + YTM)^t ]"
                ],
                "case_studies": [
                    {
                        "title": "Định giá cổ phiếu nhóm ngành ngân hàng niêm yết tại Việt Nam",
                        "detail": "Do đặc thù đòn bẩy tài chính cao, nhóm ngân hàng (VCB, TCB, MBB, CTG) chủ yếu được các CTCK định giá bằng mô hình P/B kết hợp chỉ số chất lượng tài sản (NPL, tỷ lệ bao phủ nợ xấu)."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Lý thuyết danh mục Markowitz và mô hình CAPM",
                "content": (
                    "Lý thuyết Danh mục Hiện đại (Modern Portfolio Theory) của Harry Markowitz chứng minh rằng việc kết hợp các tài sản có hệ số tương quan thấp "
                    "sẽ giúp triệt tiêu rủi ro phi hệ thống mà không làm giảm tỷ suất sinh lời kỳ vọng.\n\n"
                    "Mô hình Định giá Tài sản Vốn (CAPM) xác lập mối quan hệ tuyến tính giữa rủi ro hệ thống (đo lường bằng hệ số Beta) "
                    "và tỷ suất sinh lời kỳ vọng của tài sản, tạo cơ sở tính toán chi phí vốn chủ sở hữu."
                ),
                "formulas": [
                    "Tỷ suất sinh lời danh mục: E(R_p) = sum w_i * E(R_i)",
                    "Phương sai danh mục 2 tài sản: sigma_p^2 = w_1^2 * sigma_1^2 + w_2^2 * sigma_2^2 + 2*w_1*w_2*Cov(R_1, R_2)",
                    "Mô hình CAPM: E(R_i) = R_f + beta_i * [ E(R_m) - R_f ]",
                    "Hệ số Beta: beta_i = Cov(R_i, R_m) / Var(R_m)"
                ],
                "case_studies": [
                    {
                        "title": "Ứng dụng CAPM tính toán chi phí vốn trong các báo cáo phân tích",
                        "detail": "Các chuyên viên phân tích tại SSI Research và Vietcap sử dụng lãi suất Trái phiếu Chính phủ kỳ hạn 10 năm của Việt Nam làm lãi suất phi rủi ro (R_f) và phần bù rủi ro thị trường (ERP) dao động từ 8% đến 9.5%."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình 3 nhân tố Fama-French (1993) và 5 nhân tố Fama-French (2015): Bổ sung nhân tố quy mô (SMB), giá trị (HML), khả năng sinh lời (RMW) và phong cách đầu tư vốn (CMA).",
                "Mô hình Động lượng Momentum của Carhart (1997) và Anomalies Asset Pricing: Low-volatility anomaly, Accruals anomaly, Betting Against Beta (BAB).",
                "Kiểm định kinh tế lượng Gibbons, Ross & Shanken (GRS test 1989) và phương pháp Fama-MacBeth 2 bước ước lượng phần bù rủi ro (Risk Premia)."
            ]
        },
        review_questions=[
            "Phân tích cơ chế giảm thiểu rủi ro của đa dạng hóa danh mục theo Markowitz khi hệ số tương quan giữa hai cổ phiếu âm?",
            "Trình bày ý nghĩa kinh tế của hệ số Duration và Convexity trong việc phòng ngừa rủi ro biến động lãi suất của danh mục trái phiếu?",
            "Thiết lập mô hình hồi quy Fama-French 3 nhân tố cho thị trường chứng khoán Việt Nam và nêu các bước kiểm định GRS?"
        ]
    )
    
    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Thị trường Chứng khoán Phái sinh và Chiến lược Quản trị Rủi ro",
        introduction="Chương 5 nghiên cứu toàn diện cấu trúc sản phẩm tài chính phái sinh, nguyên lý định giá chênh lệch không rủi ro (No-Arbitrage Pricing) và các chiến lược phòng vệ danh mục đầu tư chuyên nghiệp.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Hợp đồng tương lai và cơ chế bù trừ ký quỹ",
                "content": (
                    "Hợp đồng tương lai (Futures Contract) là thỏa thuận chuẩn hóa ràng buộc các bên mua hoặc bán một tài sản cơ sở "
                    "vào một thời điểm xác định trong tương lai tại mức giá thỏa thuận trước. "
                    "Tại Việt Nam, Hợp đồng tương lai chỉ số VN30 và Hợp đồng tương lai Trái phiếu Chính phủ 5 năm là hai sản phẩm phái sinh trụ cột.\n\n"
                    "Thị trường phái sinh vận hành theo cơ chế đối tác bù trừ trung tâm (CCP) thông qua VSDC, áp dụng ký quỹ ban đầu (Initial Margin), "
                    "ký quỹ duy trì (Maintenance Margin) và định giá hàng ngày (Mark-to-Market)."
                ),
                "formulas": [
                    "Định giá Hợp đồng tương lai: F_t = S_t * e^{(r - q) * (T - t)} (với q là tỷ suất cổ tức)",
                    "Mức ký quỹ bổ sung: Variation Margin = (P_today - P_yesterday) * Số hợp đồng * Hệ số nhân (100,000 VND)"
                ],
                "case_studies": [
                    {
                        "title": "Vai trò phòng vệ rủi ro của HĐTL VN30 trong các đợt thị trường sụt giảm mạnh",
                        "detail": "Trong các nhịp điều chỉnh sâu của VN-Index năm 2022, khối lượng giao dịch HĐTL VN30 đạt kỷ lục trên 400,000 hợp đồng/phiên, giúp các quỹ đầu tư tổ chức phòng ngừa rủi ro sụt giảm danh mục cơ sở."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Hợp đồng quyền chọn và chiến lược Delta Hedging",
                "content": (
                    "Hợp đồng quyền chọn (Options) cho phép người mua có quyền nhưng không có nghĩa vụ mua (Call) hoặc bán (Put) tài sản cơ sở. "
                    "Mô hình Black-Scholes-Merton (BSM) đặt nền móng toán học cho việc định giá quyền chọn kiểu Châu Âu trong thị trường liên tục.\n\n"
                    "Hệ số Greeks (Delta, Gamma, Vega, Theta, Rho) phản ánh độ nhạy của giá quyền chọn đối với các tham số thị trường, "
                    "cho phép các định chế tài chính thiết lập trạng thái trung lập Delta (Delta-neutral portfolio) để triệt tiêu rủi ro hướng đi của giá."
                ),
                "formulas": [
                    "Công thức Black-Scholes Call: C = S * N(d1) - K * e^{-rT} * N(d2)",
                    "d1 = [ ln(S/K) + (r + sigma^2 / 2)*T ] / [ sigma * sqrt(T) ]",
                    "d2 = d1 - sigma * sqrt(T)",
                    "Hệ số Delta quyền chọn mua: Delta = dC / dS = N(d1)"
                ],
                "case_studies": [
                    {
                        "title": "Phát hành Chứng quyền có bảo đảm (Covered Warrant - CW) tại HOSE",
                        "detail": "Các CTCK hàng đầu như SSI, HSC, VNDIRECT đóng vai trò tổ chức phát hành và tạo lập thị trường cho chứng quyền mua dựa trên các cổ phiếu cơ sở VN30, thực hiện phòng hộ Delta động hàng ngày trên sàn cơ sở."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Định giá Quyền chọn dưới Phân phối Đuôi dày (Fat-tailed) và Biến động Ngẫu nhiên: Mô hình Heston (1993) và Merton Jump-Diffusion (1976).",
                "Hiện tượng Biến động Nụ cười (Volatility Smile / Surface) và Trích xuất Xác suất Trung lập Rủi ro Thực tế (Risk-Neutral Density) từ giá quyền chọn thị trường.",
                "Quản trị Rủi ro Danh mục Phái sinh phi tuyến tính: Extreme Value Theory (EVT) và Expected Shortfall (CVaR) đa chiều."
            ]
        },
        review_questions=[
            "Phân tích cơ chế Mark-to-Market và cơ chế xử lý vi phạm ký quỹ (Margin Call) của Tổng công ty Lưu ký và Bù trừ Chứng khoán Việt Nam (VSDC)?",
            "Trình bày năm giả định cốt lõi của mô hình định giá quyền chọn Black-Scholes-Merton và nêu các hạn chế khi áp dụng vào thực tiễn?",
            "Xây dựng chiến lược Delta-Gamma Hedging cho một danh mục gồm chứng quyền mua và cổ phiếu cơ sở?"
        ]
    )
    
    pages, sz = b.save(out_pdf)
    print(f"[SUCCESS] Book 2 saved: {out_pdf} ({pages} pages, {sz:.2f} MB)")
    return {
        "title": title,
        "code": subject_code,
        "author": authors,
        "path": out_pdf,
        "pages": pages,
        "size_mb": round(sz, 2)
    }

if __name__ == "__main__":
    build_ttck()
