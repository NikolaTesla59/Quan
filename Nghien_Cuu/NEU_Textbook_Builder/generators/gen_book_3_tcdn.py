# -*- coding: utf-8 -*-
"""
Generator for Textbook 3:
[NEU] Tài chính doanh nghiệp - PGS.TS Vũ Duy Hào (NXB ĐHKTQD)
"""
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_tcdn():
    title = "Tài chính doanh nghiệp"
    subject_code = "TCDN1101"
    faculty = "Viện Ngân hàng - Tài chính"
    authors = "PGS.TS. Vũ Duy Hào & PGS.TS. Trần Ngọc Thơ (Đồng Chủ biên)"
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\01_Tài chính Doanh nghiệp & Đầu tư\[NEU] Tài chính doanh nghiệp - PGS.TS Vũ Duy Hào (NXB ĐHKTQD)"
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Tài chính doanh nghiệp - PGS.TS Vũ Duy Hào (NXB ĐHKTQD).pdf")
    
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
            "chapter_title": "Tổng quan Tài chính Doanh nghiệp và Mục tiêu Tối đa hóa Giá trị Cổ đông",
            "topics": [
                "Bản chất của tài chính doanh nghiệp: Ba quyết định tài chính cốt lõi (Đầu tư, Tài trợ, Cổ tức)",
                "Hình thức tổ chức doanh nghiệp và vấn đề người đại diện (Agency Problem)",
                "Môi trường tài chính và các chuẩn mực đạo đức kinh doanh",
                "Chuyên đề Tiến sĩ: Lý thuyết Hợp đồng (Contract Theory), Chi phí Đại diện Jensen & Meckling (1976)"
            ]
        },
        {
            "chapter_num": "2",
            "chapter_title": "Phân tích Báo cáo Tài chính và Quản trị Dòng tiền Doanh nghiệp",
            "topics": [
                "Đọc hiểu hệ thống BCTC theo VAS và IFRS: Bảng CĐKT, Báo cáo KQKD, Báo cáo LCTT",
                "Phân tích tỷ số tài chính (Thanh khoản, Hoạt động, Đòn bẩy, Khả năng sinh lời) và Hệ thống DuPont 5 nhân tố",
                "Dự báo tài chính và xác định nhu cầu vốn lưu động ròng (NWC)",
                "Chuyên đề Tiến sĩ: Quản trị lợi nhuận (Earnings Management) và Mô hình dồn tích Jones (1991)"
            ]
        },
        {
            "chapter_num": "3",
            "chapter_title": "Hoạch định Ngân sách Vốn Đầu tư (Capital Budgeting under Uncertainty)",
            "topics": [
                "Ước tính dòng tiền dự án: FCFF, FCFE, Chi phí cơ hội, Chi phí chìm và Xói mòn doanh thu",
                "Các tiêu chí thẩm định: NPV, IRR, Chỉ số sinh lời PI, Thời gian hoàn vốn hòa vốn",
                "Phân tích kịch bản (Scenario Analysis), Phân tích độ nhạy (Sensitivity Analysis) và Mô phỏng Monte Carlo",
                "Chuyên đề Tiến sĩ: Quyền chọn thực trong đầu tư doanh nghiệp và Quản trị chi tiêu vốn R&D"
            ]
        },
        {
            "chapter_num": "4",
            "chapter_title": "Cấu trúc Vốn và Chính sách Đòn bẩy Tài chính",
            "topics": [
                "Định đề Modigliani-Miller (MM) trong thị trường hoàn hảo và khi có thuế thu nhập doanh nghiệp",
                "Lý thuyết Đánh đổi Cấu trúc Vốn (Trade-off Theory) và Chi phí kiệt quệ tài chính (Financial Distress)",
                "Lý thuyết Trật tự Phân hạng (Pecking Order Theory) của Myers & Majluf (1984)",
                "Chuyên đề Tiến sĩ: Mô hình Cấu trúc Vốn Động (Dynamic Capital Structure) và Tốc độ điều chỉnh nợ (SOA)"
            ]
        },
        {
            "chapter_num": "5",
            "chapter_title": "Chính sách Cổ tức, Mua lại Cổ phiếu và Quản trị Vốn Lưu động",
            "topics": [
                "Tranh luận về sự phi thích đáng của cổ tức (Dividend Irrelevance - MM) và Hiệu ứng khách hàng (Clientele Effect)",
                "Cổ tức bằng tiền mặt, Cổ tức bằng cổ phiếu và Mua lại cổ phiếu quỹ (Share Repurchases)",
                "Chiến lược quản trị vốn lưu động: Chu kỳ tiền mặt (Cash Conversion Cycle - CCC), Tín dụng thương mại và Tồn kho EOQ",
                "Chuyên đề Tiến sĩ: Lý thuyết Tín hiệu Cổ tức Bhattacharya (1979) và Dự trữ Tiền mặt Phòng ngừa (Precautionary Cash)"
            ]
        },
        {
            "chapter_num": "6",
            "chapter_title": "Tái cấu trúc Tài chính, Định giá Mua bán & Sáp nhập (M&A) và Phá sản Doanh nghiệp",
            "topics": [
                "Động cơ kinh tế của M&A: Hiệu ứng cộng hưởng (Synergy), Quy mô và Đa dạng hóa",
                "Các phương pháp định giá doanh nghiệp M&A: DCF, SOTP (Sum of the Parts), Bội số giao dịch thị trường",
                "Dự báo phá sản: Mô hình Z-score của Altman, Mô hình O-score của Ohlson và Tái cấu trúc nợ",
                "Chuyên đề Tiến sĩ: Cân bằng M&A trong thị trường cạnh tranh không hoàn hảo và Khủng hoảng thanh khoản doanh nghiệp"
            ]
        }
    ]
    b.add_table_of_contents(toc_data)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Tổng quan Tài chính Doanh nghiệp và Mục tiêu Tối đa hóa Giá trị Cổ đông",
        introduction="Chương 1 thiết lập các nguyên lý nền tảng của tài chính doanh nghiệp hiện đại, phân định rõ ba trụ cột quyết định chiến lược của Giám đốc Tài chính (CFO) và xử lý mâu thuẫn lợi ích giữa các bên liên quan trong công ty cổ phần.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bản chất của quản trị tài chính doanh nghiệp",
                "content": (
                    "Tài chính doanh nghiệp nghiên cứu cách thức doanh nghiệp huy động nguồn vốn hiệu quả nhất, phân bổ vốn vào các tài sản sinh lời "
                    "và phân phối dòng tiền tạo ra từ hoạt động kinh doanh. Ba quyết định chiến lược cốt lõi chi phối toàn bộ vận mệnh của công ty là: "
                    "Quyết định đầu tư dài hạn (Capital Budgeting), Quyết định tài trợ và cấu trúc vốn (Capital Structure), và Quyết định phân phối lợi nhuận (Dividend Policy).\n\n"
                    "Mục tiêu tối thượng của quản trị tài chính không phải là tối đa hóa lợi nhuận kế toán ngắn hạn, mà là tối đa hóa giá trị thị trường của vốn chủ sở hữu "
                    "(Maximize Shareholder Wealth) trong khuôn khổ tuân thủ pháp luật và đạo đức kinh doanh."
                ),
                "formulas": [
                    "Giá trị doanh nghiệp: Enterprise Value (EV) = Market Cap + Total Debt - Cash & Equivalents",
                    "Giá trị kinh tế gia tăng: EVA = NOPAT - (Capital * WACC)"
                ],
                "case_studies": [
                    {
                        "title": "Chuyển đổi mục tiêu chiến lược tại Tập đoàn Vinamilk (VNM)",
                        "detail": "Vinamilk áp dụng chỉ số EVA và ROIC để đánh giá hiệu quả đầu tư trang trại bò sữa hữu cơ, bảo đảm tăng trưởng giá trị dài hạn cho cổ đông thay vì chạy theo doanh thu thuần túy."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Xung đột lợi ích và vấn đề người đại diện (Agency Problem)",
                "content": (
                    "Sự tách rời giữa quyền sở hữu (Cổ đông) và quyền quản lý (Ban điều hành) nảy sinh mâu thuẫn lợi ích người đại diện. "
                    "Các nhà quản trị có xu hướng theo đuổi lợi ích cá nhân, bành trướng quy mô công ty quá mức (Empire Building) "
                    "hoặc lựa chọn các dự án an toàn dưới chuẩn để bảo vệ vị trí công tác.\n\n"
                    "Cơ chế giải quyết chi phí đại diện bao gồm: Thiết kế gói thù lao gắn với cổ phiếu thưởng (ESOP), "
                    "tăng cường vai trò độc lập của Hội đồng quản trị (HĐQT) và áp lực đe dọa thâu tóm thù địch từ thị trường kiểm soát doanh nghiệp."
                ),
                "formulas": [
                    "Chi phí đại diện: Agency Costs = Chi phí giám sát + Chi phí cam kết + Tổn thất thặng dư (Residual Loss)",
                    "Tỷ lệ nắm giữ cổ phần của ban điều hành: Insider Ownership = Shares_insiders / Total_shares"
                ],
                "case_studies": [
                    {
                        "title": "Vấn đề thù lao ESOP tại Thế Giới Di Động (MWG)",
                        "detail": "MWG sử dụng chính sách phát hành ESOP tỷ lệ 3% hàng năm gắn với tiêu chí tăng trưởng lợi nhuận ròng, tạo động lực gắn kết đội ngũ quản lý cấp cao nhưng cũng gặp phản ứng từ cổ đông tổ chức khi thị trường gặp khó khăn."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Chi phí Đại diện của Jensen & Meckling (1976): Mô hình hóa sự đánh đổi giữa tiêu dùng bổng lộc ngoài lương (Perquisite Consumption) và hiệu quả giám sát.",
                "Lý thuyết Hợp đồng Tối ưu (Optimal Contracting) của Holmström (1979) về đãi ngộ điều hành trong điều kiện rủi ro đạo đức (Moral Hazard).",
                "Khung quản trị công ty thực nghiệm: Đo lường chỉ số G-Index (Gompers et al. 2003) và E-Index (Bebchuk et al. 2009) tại các thị trường châu Á."
            ]
        },
        review_questions=[
            "Tại sao mục tiêu tối đa hóa giá trị cổ đông lại vượt trội hơn mục tiêu tối đa hóa lợi nhuận kế toán ròng trong quản trị tài chính?",
            "Phân tích các cơ chế quản trị công ty nội bộ và bên ngoài nhằm giảm thiểu xung đột đại diện giữa cổ đông và ban giám đốc?",
            "Xây dựng mô hình đại diện của Jensen-Meckling và chứng minh toán học sự sụt giảm giá trị doanh nghiệp khi tỷ lệ sở hữu của nhà quản trị giảm?"
        ]
    )
    
    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Phân tích Báo cáo Tài chính và Quản trị Dòng tiền Doanh nghiệp",
        introduction="Chương 2 hướng dẫn phương pháp giải mã hệ thống báo cáo tài chính, đo lường sức khỏe dòng tiền vận hành và phân rã các động lực sinh lời cốt lõi thông qua mô hình DuPont mở rộng.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phân tích cấu trúc báo cáo tài chính và dòng tiền",
                "content": (
                    "Báo cáo tài chính là ngôn ngữ của kinh doanh. Bảng cân đối kế toán cung cấp bức tranh tĩnh về tài sản và nguồn vốn tại một thời điểm; "
                    "Báo cáo kết quả kinh doanh phản ánh hiệu quả vận hành trong một kỳ; trong khi Báo cáo lưu chuyển tiền tệ "
                    "phơi bày sự thật về năng lực tạo tiền mặt thực tế từ hoạt động kinh doanh (CFO), hoạt động đầu tư (CFI) và hoạt động tài chính (CFF).\n\n"
                    "Lợi nhuận kế toán dương nhưng dòng tiền kinh doanh (CFO) âm kéo dài là tín hiệu cảnh báo hàng đầu về nguy cơ vỡ nợ kỹ thuật."
                ),
                "formulas": [
                    "Dòng tiền tự do cho doanh nghiệp: FCFF = EBIT * (1 - t) + D&A - Capex - Delta NWC",
                    "Dòng tiền tự do cho chủ sở hữu: FCFE = FCFF - Lãi vay * (1 - t) + Vay ròng mới"
                ],
                "case_studies": [
                    {
                        "title": "Chênh lệch dòng tiền và lợi nhuận tại các doanh nghiệp bất động sản",
                        "detail": "Nhiều doanh nghiệp BĐS ghi nhận doanh thu và lợi nhuận cao nhờ bàn giao dự án trên giấy, nhưng dòng tiền CFO âm nặng nề do tồn kho dự án dở dang tăng vọt và công nợ khách hàng kéo dài."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Hệ thống chỉ số tài chính và mô hình DuPont 5 nhân tố",
                "content": (
                    "Phân tích tỷ số tài chính bao quát 4 nhóm chỉ tiêu: Thanh khoản (Current ratio, Quick ratio), "
                    "Hiệu quả hoạt động (Vòng quay tồn kho, Kỳ thu tiền bình quân), Đòn bẩy nợ (D/E, Interest Coverage) và Sinh lời (ROA, ROE, ROS).\n\n"
                    "Mô hình DuPont phân rã tỷ suất sinh lời trên vốn chủ sở hữu (ROE) thành 5 cấu phần độc lập, giúp lãnh đạo doanh nghiệp "
                    "nhận diện chính xác động lực tăng trưởng bắt nguồn từ biên lợi nhuận, hiệu suất sử dụng tài sản, đòn bẩy tài chính, gánh nặng lãi vay hay chính sách thuế."
                ),
                "formulas": [
                    "DuPont 5 bước: ROE = (NI/EBT) * (EBT/EBIT) * (EBIT/Sales) * (Sales/Assets) * (Assets/Equity)",
                    "Ý nghĩa: ROE = Tax Burden * Interest Burden * Operating Margin * Asset Turnover * Financial Leverage",
                    "Hệ số bao phủ lãi vay: ICR = EBIT / Interest Expense"
                ],
                "case_studies": [
                    {
                        "title": "Phân tích DuPont tại Công ty Cổ phần Thép Hòa Phát (HPG)",
                        "detail": "ROE của HPG tăng vọt trong chu kỳ bùng nổ ngành thép nhờ sự cộng hưởng của việc tăng biên EBIT (lợi thế lò cao BOF khép kín) và vòng quay tài sản tăng mạnh từ giai đoạn 1 dự án Dung Quất."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Dồn tích Điều chỉnh của Dechow, Sloan & Sweeney (1995) (Modified Jones Model): Phát hiện hành vi điều chỉnh thu nhập (Discretionary Accruals) trước kỳ báo cáo.",
                "Chỉ số M-score của Beneish (1999) đánh giá xác suất gian lận báo cáo tài chính (Financial Statement Manipulation).",
                "Chất lượng Dòng tiền (Cash Flow Quality) và Dự báo Khả năng Sinh lời trong Tương lai (Sloan 1996 Accrual Anomaly)."
            ]
        },
        review_questions=[
            "Tại sao phân tích dòng tiền kinh doanh (CFO) lại có ý nghĩa quyết định hơn việc chỉ quan sát lợi nhuận sau thuế của doanh nghiệp?",
            "Trình bày chi tiết từng nhân tố trong phương trình DuPont 5 bước và chỉ ra chiến lược cải thiện ROE cho doanh nghiệp bán lẻ?",
            "Thiết lập mô hình kinh tế lượng ước lượng Discretionary Accruals theo phương pháp Modified Jones Model trên dữ liệu mảng các công ty niêm yết?"
        ]
    )
    
    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Hoạch định Ngân sách Vốn Đầu tư (Capital Budgeting under Uncertainty)",
        introduction="Chương 3 trang bị khung phương pháp luận ra quyết định đầu tư vốn dài hạn, xử lý các dự án loại trừ nhau, dự án có tuổi thọ khác nhau và kỹ thuật phân tích rủi ro dòng tiền.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Kỹ thuật thẩm định dự án đầu tư và các tiêu chí quyết định",
                "content": (
                    "Hoạch định ngân sách vốn là quá trình thẩm định và lựa chọn các dự án đầu tư dài hạn nhằm tạo ra giá trị gia tăng kinh tế lớn nhất. "
                    "Nguyên tắc vàng của việc ước tính ngân lưu là chỉ tính toán dòng tiền gia tăng (Incremental Cash Flows) sau thuế, "
                    "loại trừ chi phí chìm (Sunk Cost), tính đủ chi phí cơ hội (Opportunity Cost) và hiệu ứng xói mòn sản phẩm hiện có (Cannibalization).\n\n"
                    "Khi xảy ra mâu thuẫn giữa xếp hạng NPV và IRR (do khác biệt quy mô vốn hoặc hình thái dòng tiền phi quy ước), "
                    "NPV luôn là tiêu chí quyết định tối hậu vì giả định tái đầu tư dòng tiền tại chi phí vốn (WACC) thực tế hơn."
                ),
                "formulas": [
                    "Chỉ số sinh lời: PI = PV(Cash Inflows) / Initial Investment = 1 + NPV / I_0",
                    "Chuỗi chi phí hàng năm tương đương: EAC = NPV / PVIFA(r, n) (dành cho dự án có vòng đời khác nhau)",
                    "Thời gian hoàn vốn có chiết khấu: DPB = Thời gian để Cumulative Discounted CF = 0"
                ],
                "case_studies": [
                    {
                        "title": "Quyết định mở rộng nhà máy lọc dầu Dung Quất của BSR",
                        "detail": "BSR thực hiện thẩm định dự án nâng cấp mở rộng trị giá 1.25 tỷ USD, áp dụng phương pháp EAC để so sánh các phương án công nghệ phối trộn dầu thô nhập khẩu từ Mỹ và Trung Đông."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Đánh giá rủi ro dự án trong điều kiện bất định",
                "content": (
                    "Trong thực tế, các biến số doanh thu, chi phí vận hành, giá nguyên liệu đầu vào và tỷ suất chiết khấu đều có tính ngẫu nhiên. "
                    "Phân tích độ nhạy (Sensitivity Analysis) khảo sát mức độ biến thiên của NPV khi một biến số thay đổi độc lập. "
                    "Phân tích kịch bản (Scenario Analysis) xem xét sự kết hợp đồng thời của các biến số trong điều kiện kịch bản xấu nhất, cơ sở và tốt nhất.\n\n"
                    "Mô phỏng Monte Carlo sử dụng máy tính chạy hàng chục nghìn lần thử ngẫu nhiên theo các phân phối xác suất xác định, "
                    "tạo ra biểu đồ phân phối xác suất liên tục của NPV dự án."
                ),
                "formulas": [
                    "Độ nhạy của NPV: S_NPV = (dNPV / dX) * (X / NPV)",
                    "Kỳ vọng NPV ngẫu nhiên: E(NPV) = sum P_i * NPV_i, với Var(NPV) = sum P_i * [NPV_i - E(NPV)]^2"
                ],
                "case_studies": [
                    {
                        "title": "Ứng dụng mô phỏng Monte Carlo trong dự án Điện khí LNG Sơn Mỹ",
                        "detail": "Tập đoàn Dầu khí Việt Nam (PVN) mô phỏng rủi ro biến động giá khí LNG thế giới và rủi ro tỷ giá USD/VND tác động đến tỷ suất hoàn vốn IRR của tổ hợp dự án."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Quyền chọn Thực (Real Options) của Myers (1977): Dự án đầu tư như một danh mục quyền chọn tăng trưởng (Growth Options).",
                "Chiến lược Đầu tư Dưới Tác động của Đòn bẩy Tài chính và Xung đột Nợ - Vốn chủ sở hữu: Hiện tượng Dưới Đầu tư (Underinvestment) theo Myers (1977) và Đầu tư Liều mạng (Asset Substitution) theo Jensen & Meckling (1976).",
                "Hàm Chi phí Đầu tư Bất đối xứng và Phản ứng Trễ của Doanh nghiệp trước Cú sốc Lãi suất."
            ]
        },
        review_questions=[
            "Tại sao việc loại trừ chi phí chìm (Sunk Cost) lại là nguyên tắc bắt buộc khi tính toán dòng tiền gia tăng của dự án?",
            "Phân tích trường hợp xuất hiện đa nghiệm IRR khi dòng tiền dự án đổi dấu nhiều lần và giải pháp khắc phục bằng MIRR?",
            "Xây dựng mô hình toán học giải thích hiện tượng Underinvestment xảy ra khi doanh nghiệp có tỷ lệ đòn bẩy nợ quá cao?"
        ]
    )
    
    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Cấu trúc Vốn và Chính sách Đòn bẩy Tài chính",
        introduction="Chương 4 phân tích các lý thuyết cấu trúc vốn kinh điển từ định đề Modigliani-Miller đến lý thuyết đánh đổi, trật tự phân hạng và các bằng chứng thực nghiệm về cấu trúc vốn tối ưu của doanh nghiệp.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Định đề Modigliani-Miller (MM) và vai trò lá chắn thuế",
                "content": (
                    "Năm 1958, Franco Modigliani và Merton Miller công bố định đề MM1 trong thị trường vốn hoàn hảo (không thuế, không chi phí giao dịch, không chi phí phá sản), "
                    "chứng minh rằng giá trị doanh nghiệp độc lập với cấu trúc vốn (V_L = V_U). Quyết định tạo ra giá trị nằm ở tài sản chứ không phải ở cách chia tài sản.\n\n"
                    "Năm 1963, khi bổ sung thuế thu nhập doanh nghiệp, MM2 chứng minh rằng nợ vay tạo ra giá trị gia tăng nhờ lá chắn thuế từ lãi vay (Interest Tax Shield), "
                    "doanh nghiệp vay nợ càng nhiều thì giá trị doanh nghiệp càng tăng (V_L = V_U + t_c * D)."
                ),
                "formulas": [
                    "MM1 có thuế: V_L = V_U + t_c * D",
                    "MM2 có thuế: r_e = r_0 + (D/E) * (r_0 - r_d) * (1 - t_c)",
                    "Giá trị hiện tại của lá chắn thuế vĩnh viễn: PV(Tax Shield) = t_c * D"
                ],
                "case_studies": [
                    {
                        "title": "Tối ưu hóa lá chắn thuế tại các tập đoàn sản xuất công nghiệp nặng",
                        "detail": "Các tập đoàn xi măng, lọc hóa dầu duy trì tỷ lệ nợ vay cao trong giai đoạn đầu xây dựng để tận dụng tối đa khấu trừ chi phí lãi vay vào lợi nhuận chịu thuế."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Lý thuyết đánh đổi tĩnh và trật tự phân hạng",
                "content": (
                    "Trong thế giới thực, việc gia tăng nợ vay làm tăng xác suất xảy ra kiệt quệ tài chính (Financial Distress) và chi phí phá sản (trực tiếp và gián tiếp). "
                    "Lý thuyết Đánh đổi Cấu trúc Vốn (Static Trade-off Theory) khẳng định tồn tại một cấu trúc vốn tối ưu tại điểm mà lợi ích biên từ lá chắn thuế "
                    "cân bằng chính xác với chi phí biên của kiệt quệ tài chính.\n\n"
                    "Ngược lại, Lý thuyết Trật tự Phân hạng (Pecking Order Theory) của Myers & Majluf (1984) dựa trên bất cân xứng thông tin, "
                    "chỉ ra rằng doanh nghiệp ưu tiên sử dụng vốn nội bộ (lợi nhuận giữ lại), tiếp đến là nợ vay, và chỉ phát hành cổ phiếu mới như phương án cuối cùng."
                ),
                "formulas": [
                    "Cấu trúc vốn tối ưu Trade-off: V_L = V_U + PV(Tax Shield) - PV(Cost of Financial Distress)",
                    "Chi phí kiệt quệ tài chính: PV(FD) = Xác suất vỡ nợ (Prob_default) * Chi phí thiệt hại khi vỡ nợ (Loss Given Default)"
                ],
                "case_studies": [
                    {
                        "title": "Cấu trúc vốn thận trọng của FPT và Vinamilk",
                        "detail": "Cả FPT và Vinamilk đều ưu tiên dòng tiền kinh doanh dồi dào và lợi nhuận giữ lại để tài trợ đầu tư công nghệ và mở rộng thị trường, tuân thủ chặt chẽ mô hình Pecking Order."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Cấu trúc Vốn Động (Dynamic Capital Structure Model) theo Strebulaev (2007): Doanh nghiệp điều chỉnh nợ định kỳ khi chi phí điều chỉnh vượt ngưỡng cận biên.",
                "Tốc độ Điều chỉnh Nợ về Mục tiêu (Speed of Adjustment - SOA): Ước lượng mô hình Partial Adjustment bằng Blundell-Bond System GMM kiểm soát nội sinh.",
                "Tác động của Định chế Pháp lý, Quyền của Chủ nợ (Creditor Rights) và Rủi ro Hệ thống đến Cấu trúc Vốn theo Djankov et al. (2007)."
            ]
        },
        review_questions=[
            "Trình bày lập luận kinh tế của định đề Modigliani-Miller không thuế và cơ chế kinh doanh chênh lệch giá của nhà đầu tư cá nhân (Homemade Leverage)?",
            "Phân tích sự khác biệt cốt lõi trong dự báo hành vi tài trợ vốn giữa Lý thuyết Đánh đổi và Lý thuyết Trật tự Phân hạng?",
            "Thiết lập mô hình hồi quy kinh tế lượng đo lường tốc độ điều chỉnh cấu trúc vốn mục tiêu (SOA) cho các doanh nghiệp niêm yết tại Việt Nam?"
        ]
    )
    
    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Chính sách Cổ tức, Mua lại Cổ phiếu và Quản trị Vốn Lưu động",
        introduction="Chương 5 đi sâu vào tranh luận về chính sách phân phối thu nhập cho cổ đông, cơ chế phát tín hiệu tài chính và chiến lược tối ưu hóa chu kỳ luân chuyển vốn lưu động.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Chính sách phân phối cổ tức và mua lại cổ phiếu",
                "content": (
                    "Chính sách cổ tức giải quyết bài toán: Doanh nghiệp nên giữ lại bao nhiêu phần trăm lợi nhuận để tái đầu tư và chi trả bao nhiêu cho cổ đông. "
                    "Định đề MM về cổ tức chứng minh trong thị trường hoàn hảo, chính sách cổ tức là phi thích đáng (Dividend Irrelevance). "
                    "Tuy nhiên, khi có thuế sai biệt (thuế cổ tức cao hơn thuế thặng dư vốn), nhà đầu tư sẽ ưa thích lợi nhuận giữ lại hơn chi trả tiền mặt.\n\n"
                    "Mua lại cổ phiếu quỹ (Share Repurchases) là phương thức phân phối tiền mặt linh hoạt, giúp tăng chỉ số EPS "
                    "và phát tín hiệu đến thị trường rằng ban giám đốc tin tưởng cổ phiếu công ty đang bị định giá thấp."
                ),
                "formulas": [
                    "Tỷ lệ chi trả cổ tức: Dividend Payout Ratio = DPS / EPS = Total Dividends / Net Income",
                    "Tỷ lệ tái đầu tư: Retention Rate (b) = 1 - Payout Ratio",
                    "Tốc độ tăng trưởng bền vững: g_sustainable = ROE * b"
                ],
                "case_studies": [
                    {
                        "title": "Chính sách cổ tức tiền mặt đều đặn của Dược Hậu Giang (DHG)",
                        "detail": "DHG duy trì chính sách trả cổ tức tiền mặt từ 30% đến 40% mệnh giá suốt hơn một thập kỷ, thu hút các quỹ hưu trí và nhà đầu tư dài hạn yêu thích dòng thu nhập ổn định."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Quản trị vốn lưu động và chu kỳ luân chuyển tiền mặt",
                "content": (
                    "Quản trị vốn lưu động (Working Capital Management) tập trung vào việc quản trị tài sản ngắn hạn và nợ ngắn hạn nhằm bảo đảm khả năng thanh toán "
                    "và tối ưu hóa chi phí nắm giữ vốn. Chu kỳ tiền mặt (Cash Conversion Cycle - CCC) đo lường khoảng thời gian từ lúc doanh nghiệp "
                    "bỏ tiền mua nguyên vật liệu thô đến lúc thu được tiền bán hàng từ khách hàng.\n\n"
                    "Rút ngắn CCC bằng cách đẩy nhanh tốc độ quay vòng tồn kho, tối ưu hóa thu hồi công nợ và thương lượng kéo dài thời gian trả nợ nhà cung cấp "
                    "sẽ giải phóng một lượng tiền mặt khổng lồ cho doanh nghiệp."
                ),
                "formulas": [
                    "Chu kỳ tiền mặt: CCC = ICP + RCP - PDP",
                    "Thời gian luân chuyển tồn kho: ICP = (Tồn kho bình quân / Giá vốn hàng bán) * 365",
                    "Thời gian thu hồi nợ bình quân: RCP = (Phải thu bình quân / Doanh thu thuần) * 365",
                    "Thời gian thanh toán nợ bình quân: PDP = (Phải trả bình quân / Giá vốn hàng bán) * 365"
                ],
                "case_studies": [
                    {
                        "title": "Mô hình quản trị chuỗi cung ứng 'âm vốn lưu động' của Thế Giới Di Động",
                        "detail": "MWG tận dụng sức mạnh đàm phán với các nhà cung cấp điện thoại để đạt PDP lên tới 60-75 ngày trong khi thời gian tồn kho và thu tiền khách hàng rất ngắn, tạo ra CCC âm và thặng dư tiền mặt lớn."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Tín hiệu Cổ tức của Bhattacharya (1979) và John & Williams (1985): Cổ tức tiền mặt đóng vai trò tín hiệu đắt giá (Costly Signaling) chứng minh dòng tiền thực.",
                "Tài chính Hành vi và Cổ tức: Lý thuyết Khung Khách hàng (Catering Theory of Dividends) của Baker & Wurgler (2004).",
                "Động cơ Nắm giữ Tiền mặt Doanh nghiệp (Corporate Cash Holdings): Đánh đổi giữa Chi phí Cơ hội và Giá trị Dự phòng theo Bates, Kahle & Stulz (2009)."
            ]
        },
        review_questions=[
            "Phân tích ưu điểm và nhược điểm của hình thức mua lại cổ phiếu quỹ so với chi trả cổ tức bằng tiền mặt?",
            "Tại sao một chu kỳ luân chuyển tiền mặt (CCC) quá ngắn hoặc âm có thể đem lại lợi ích thanh khoản nhưng cũng tiềm ẩn rủi ro quan hệ chuỗi cung ứng?",
            "Trình bày mô hình Catering Theory của Baker-Wurgler giải thích tại sao ban điều hành quyết định trả cổ tức phụ thuộc vào tâm lý thị trường?"
        ]
    )
    
    # Chapter 6
    b.add_chapter(
        chap_num="6",
        chap_title="Tái cấu trúc Tài chính, Định giá Mua bán & Sáp nhập (M&A) và Phá sản Doanh nghiệp",
        introduction="Chương 6 hoàn thiện hệ thống tài chính doanh nghiệp với các thương vụ mua bán sáp nhập (M&A), kỹ thuật định giá cộng hưởng và các mô hình cảnh báo sớm nguy cơ phá sản.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Động cơ và phương pháp định giá thương vụ M&A",
                "content": (
                    "M&A là công cụ tăng trưởng phi hữu cơ giúp doanh nghiệp mở rộng thị phần nhanh chóng, thâu tóm công nghệ hoặc hoàn thiện chuỗi giá trị tích hợp dọc. "
                    "Cộng hưởng (Synergy) là nguồn cội tạo ra giá trị gia tăng trong M&A, bao gồm: Cộng hưởng hoạt động (Operating Synergy từ tính kinh tế theo quy mô) "
                    "và Cộng hưởng tài chính (Financial Synergy từ giảm chi phí sử dụng vốn và lợi thế thuế).\n\n"
                    "Định giá M&A đòi hỏi kết hợp mô hình dòng tiền chiết khấu độc lập của bên bị thâu tóm cộng với hiện giá ròng của giá trị cộng hưởng sau sáp nhập."
                ),
                "formulas": [
                    "Giá trị cộng hưởng: Synergy = V_{AB} - (V_A + V_B)",
                    "Mức giá chào mua tối đa: Maximum Price = V_B + Synergy",
                    "Thặng dư cho cổ đông bên mua: Gain_A = Synergy - Premium (với Premium = Offer_Price - V_B)"
                ],
                "case_studies": [
                    {
                        "title": "Thương vụ Masan Group thâu tóm hệ thống VinCommerce (WinCommerce)",
                        "detail": "Masan sáp nhập mảng bán lẻ của Vingroup để xây dựng nền tảng 'Point of Life' tích hợp từ sản xuất hàng tiêu dùng (Masan Consumer) đến mạng lưới phân phối hơn 3,000 siêu thị WinMart."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Dự báo phá sản và tái cơ cấu nợ doanh nghiệp",
                "content": (
                    "Khủng hoảng tài chính diễn ra khi dòng tiền hoạt động không đủ trang trải các nghĩa vụ nợ đến hạn. "
                    "Tái cấu trúc nợ tài chính có thể thực hiện thông qua hoán đổi nợ thành cổ phần (Debt-to-Equity Swap), "
                    "giãn hoãn kỳ hạn thanh toán, hoặc tái tài trợ bằng nguồn vốn mới.\n\n"
                    "Các mô hình dự báo phá sản định lượng hỗ trợ các ngân hàng và nhà đầu tư phát hiện sớm các dấu hiệu suy giảm sức khỏe tài chính "
                    "từ 1 đến 2 năm trước khi doanh nghiệp lâm vào tình trạng mất khả năng thanh toán."
                ),
                "formulas": [
                    "Mô hình Altman Z-score (doanh nghiệp sản xuất): Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 0.999*X5",
                    "Trong đó: X1 = NWC/Total Assets, X2 = Retained Earnings/Total Assets, X3 = EBIT/Total Assets, X4 = Market Value Equity/Total Debt, X5 = Sales/Total Assets",
                    "Ngưỡng: Z < 1.81 (Vùng nguy hiểm - Distress Zone), Z > 2.99 (Vùng an toàn - Safe Zone)"
                ],
                "case_studies": [
                    {
                        "title": "Tái cấu trúc tài chính của Tổng công ty Hàng không Việt Nam (Vietnam Airlines)",
                        "detail": "HVN áp dụng gói hỗ trợ tái cấp vốn 4,000 tỷ đồng, phát hành cổ phiếu tăng vốn 8,000 tỷ đồng cho cổ đông hiện hữu và tái đàm phán giãn nợ thuê máy bay quốc tế để vượt qua khủng hoảng thanh khoản hậu dịch."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Cạnh tranh Mua lại Doanh nghiệp (Merger Waves) và Sốc Công nghệ theo Harford (2005).",
                "Mô hình Phá sản Cấu trúc Merton (1974): Vốn chủ sở hữu như một quyền chọn mua (Call Option) trên tổng tài sản doanh nghiệp, đo lường Khoảng cách đến Phá sản (Distance to Default - DtD).",
                "Hiệu quả Tái cấu trúc Doanh nghiệp Nhà nước (SOE Privatization) bằng phương pháp Ghép điểm Xu hướng (Propensity Score Matching - PSM) kết hợp DiD."
            ]
        },
        review_questions=[
            "Phân tích ba nguồn gốc cốt lõi tạo ra giá trị cộng hưởng (Synergy) trong một thương vụ sáp nhập theo chiều dọc?",
            "Tại sao mô hình Z-score của Edward Altman lại gán trọng số cao nhất cho biến số X3 (EBIT / Tổng tài sản)?",
            "Trình bày mô hình cấu trúc vỡ nợ của Robert Merton và giải thích mối quan hệ giữa biến động tài sản (Asset Volatility) và xác suất vỡ nợ của công ty?"
        ]
    )
    
    pages, sz = b.save(out_pdf)
    print(f"[SUCCESS] Book 3 saved: {out_pdf} ({pages} pages, {sz:.2f} MB)")
    return {
        "title": title,
        "code": subject_code,
        "author": authors,
        "path": out_pdf,
        "pages": pages,
        "size_mb": round(sz, 2)
    }

if __name__ == "__main__":
    build_tcdn()
