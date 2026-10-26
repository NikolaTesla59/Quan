# -*- coding: utf-8 -*-
"""
Generator for Textbook 7:
[NEU] Quản trị ngân hàng thương mại - PGS.TS Phan Thị Thu Hà (NXB ĐHKTQD)
"""
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_nhtm():
    title = "Quản trị ngân hàng thương mại"
    subject_code = "NHTM1102"
    faculty = "Viện Ngân hàng - Tài chính"
    authors = "PGS.TS. Phan Thị Thu Hà & PGS.TS. Nguyễn Thị Mùi (Đồng Chủ biên)"
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\03_Ngân hàng & Bảo hiểm\[NEU] Quản trị ngân hàng thương mại - PGS.TS Phan Thị Thu Hà (NXB ĐHKTQD)"
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Quản trị ngân hàng thương mại - PGS.TS Phan Thị Thu Hà (NXB ĐHKTQD).pdf")
    
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
            "chapter_title": "Tổng quan Hoạt động Kinh doanh và Báo cáo Tài chính Ngân hàng",
            "topics": [
                "Bản chất của NHTM: Định chế trung gian tài chính kinh doanh chữ tín và tiền tệ",
                "Cấu trúc bảng cân đối kế toán NHTM: Tài sản Có (Tín dụng, Chứng khoán đầu tư, Dự trữ) và Tài sản Nợ (Tiền gửi, Vốn vay liên ngân hàng, Vốn tự có)",
                "Báo cáo kết quả kinh doanh: Thu nhập lãi thuần (NII), Thu nhập ngoài lãi (Non-Interest Income) và Chi phí trích lập dự phòng",
                "Chuyên đề Tiến sĩ: Cạnh tranh Ngân hàng và Ổn định Tài chính (Competition-Stability vs Competition-Fragility Nexus)"
            ]
        },
        {
            "chapter_num": "2",
            "chapter_title": "Quản trị Tài sản Có - Tài sản Nợ (ALM) và Quản trị Thanh khoản",
            "topics": [
                "Chiến lược quản trị ALM: Cân đối kỳ hạn, cơ cấu lãi suất và bảo toàn tỷ lệ thu nhập lãi thuần (NIM)",
                "Quản trị rủi ro thanh khoản: Chiến lược quản trị thanh khoản từ tài sản nợ vs tài sản có",
                "Các chỉ số an toàn thanh khoản theo Thông tư 22/2019/TT-NHNN và Chuẩn mực Basel III (LCR, NSFR, LDR)",
                "Chuyên đề Tiến sĩ: Mô hình Quản trị Thanh khoản Động và Tối ưu hóa Danh mục Trái phiếu Dự trữ HQLA"
            ]
        },
        {
            "chapter_num": "3",
            "chapter_title": "Quản trị Hoạt động Tín dụng và Quản lý Rủi ro Tín dụng",
            "topics": [
                "Quy trình tín dụng chuẩn mực: Tiếp nhận hồ sơ, Thẩm định tín dụng 5C/6C, Giải ngân và Giám sát sau vay",
                "Phân loại nợ theo Thông tư 11/2021/TT-NHNN: 5 nhóm nợ và tỷ lệ trích lập dự phòng rủi ro cụ thể, dự phòng chung",
                "Xếp hạng tín dụng nội bộ và các mô hình chấm điểm tín dụng cá nhân (Credit Scoring)",
                "Chuyên đề Tiến sĩ: Mô hình Rủi ro Tín dụng Cấu trúc Merton (1974) và Mô hình Xếp hạng Nội bộ Nâng cao (A-IRB) theo Basel II/III"
            ]
        },
        {
            "chapter_num": "4",
            "chapter_title": "Quản trị Rủi ro Lãi suất trên Sổ Ngân hàng (IRRBB) và Rủi ro Thị trường",
            "topics": [
                "Đo lường khe hở nhạy cảm lãi suất: Mô hình định giá lại (Repricing Model) và Khe hở kỳ hạn (Duration Gap)",
                "Tác động của cú sốc lãi suất đến Thu nhập lãi thuần (NII) và Giá trị kinh tế của vốn chủ sở hữu (EVE)",
                "Quản trị rủi ro hối đoái và trạng thái ngoại tệ ròng của NHTM",
                "Chuyên đề Tiến sĩ: Mô hình Mô phỏng Lợi tức Động (Dynamic Dynamic Duration Analysis) và Công cụ Phái sinh Lãi suất (IRS/CCS)"
            ]
        },
        {
            "chapter_num": "5",
            "chapter_title": "Quản trị Rủi ro Hoạt động, Ngân hàng Số và Khung Khổ An toàn Vốn",
            "topics": [
                "Rủi ro hoạt động (Operational Risk) theo Basel: Con người, Hệ thống công nghệ, Quy trình nội bộ và Sự kiện bên ngoài",
                "Chuyển đổi số ngành ngân hàng: Core Banking thế hệ mới, Open API, Ngân hàng mở (Open Banking) và Trí tuệ nhân tạo (AI/ML) trong phòng chống gian lận",
                "Khung khổ an toàn vốn Basel II & Basel III: Đo lường tài sản có rủi ro (RWA) và Trụ cột 2 Đánh giá nội bộ an toàn vốn (ICAAP)",
                "Chuyên đề Tiến sĩ: Kịch bản Kiểm tra Sức chịu đựng Ngân hàng (Macro Stress Testing) và Mô hình Rủi ro Ngân hàng Bóng đêm (Shadow Banking)"
            ]
        }
    ]
    b.add_table_of_contents(toc_data)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Tổng quan Hoạt động Kinh doanh và Báo cáo Tài chính Ngân hàng",
        introduction="Chương 1 phân tích mô hình tổ chức của ngân hàng thương mại hiện đại, giải phẫu bảng cân đối tài chính và báo cáo kết quả hoạt động kinh doanh, làm rõ các động lực tạo lập lợi nhuận và an toàn hệ thống.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bản chất và vị thế đặc thù của ngân hàng thương mại",
                "content": (
                    "Ngân hàng thương mại là doanh nghiệp đặc biệt kinh doanh 'tiền tệ và rủi ro'. Đặc điểm cốt lõi phân biệt ngân hàng với các doanh nghiệp thông thường "
                    "là tỷ lệ đòn bẩy tài chính cực cao: Vốn chủ sở hữu chỉ chiếm từ 8% đến 12% tổng nguồn vốn, trong khi gần 90% còn lại là các khoản nợ phải trả "
                    "(chủ yếu là tiền gửi của khách hàng và vay mượn thị trường liên ngân hàng).\n\n"
                    "Cấu trúc bảng cân đối kế toán ngân hàng thể hiện: Bên Nợ là các nguồn vốn huy động (tiền gửi thanh toán CASA, tiền gửi tiết kiệm, giấy tờ có giá); "
                    "Bên Có là các tài sản sinh lời (cho vay khách hàng, chứng khoán đầu tư) và tài sản thanh khoản (dự trữ tại NHTW, tiền gửi tại TCTD khác)."
                ),
                "formulas": [
                    "Đòn bẩy tài chính ngân hàng: Leverage = Total Assets / Equity (thường từ 8x đến 12x)",
                    "Tỷ lệ tiền gửi không kỳ hạn CASA: CASA Ratio = (Demand Deposits) / Total Customer Deposits * 100%"
                ],
                "case_studies": [
                    {
                        "title": "Chiến lược tối ưu hóa chi phí vốn bằng tỷ lệ CASA tại Techcombank và MB",
                        "detail": "Techcombank và MB tiên phong áp dụng chính sách Zero Fee (miễn 100% phí chuyển khoản) và ứng dụng số vượt trội, duy trì tỷ lệ CASA cao ngất ngưởng từ 40% đến 50%, giúp hạ thấp chi phí vốn đầu vào (COF) và mở rộng biên lãi ròng (NIM)."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Báo cáo thu nhập và các chỉ số đo lường hiệu quả sinh lời",
                "content": (
                    "Lợi nhuận trước thuế của ngân hàng được tạo thành từ hai cấu phần chính: Thu nhập lãi thuần (Net Interest Income - NII = Thu nhập lãi - Chi phí trả lãi) "
                    "và Thu nhập ngoài lãi (Non-Interest Income: phí dịch vụ thanh toán, tài trợ thương mại, kinh doanh ngoại hối, bảo hiểm Bancassurance) "
                    "trừ đi Chi phí hoạt động (Opex) và Chi phí trích lập dự phòng rủi ro tín dụng.\n\n"
                    "Các chỉ số đánh giá hiệu quả vận hành gồm: Biên lãi ròng (NIM), Tỷ lệ chi phí trên thu nhập (Cost-to-Income Ratio - CIR), "
                    "Tỷ suất sinh lời trên tổng tài sản (ROA) và Tỷ suất sinh lời trên vốn chủ sở hữu (ROE)."
                ),
                "formulas": [
                    "Biên lãi ròng: NIM = (Interest Income - Interest Expense) / Average Earning Assets",
                    "Chênh lệch lãi suất thuần: Spread = Lợi suất tài sản sinh lời - Chi phí nguồn vốn phải trả lãi",
                    "Tỷ lệ chi phí trên thu nhập: CIR = Operating Expenses / Total Operating Income (TOI) * 100%"
                ],
                "case_studies": [
                    {
                        "title": "Hiệu quả sinh lời vượt trội của Ngân hàng TMCP Ngoại thương Việt Nam (Vietcombank)",
                        "detail": "Năm 2023-2024, Vietcombank đạt lợi nhuận trước thuế trên 40,000 tỷ đồng (gần 1.7 tỷ USD), dẫn đầu toàn ngành nhờ NIM duy trì trên 3.2%, CIR ở mức thấp dưới 32% và tỷ lệ nợ xấu được kiểm soát dưới 1%."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Tranh luận Cạnh tranh - Ổn định (Competition-Stability Nexus): Mô hình Boyd & De Nicolo (2005) chứng minh cạnh tranh làm giảm lãi suất cho vay, giảm xác suất vỡ nợ của người vay.",
                "Đo lường Quyền lực Thị trường Ngân hàng: Hệ số Lerner điều chỉnh và Mô hình Panzar-Rosse (H-statistic).",
                "Hàm Chi phí Siêu việt Translog và Tính Kinh tế theo Quy mô (Economies of Scale and Scope) trong ngành ngân hàng bằng Stochastic Frontier Analysis (SFA)."
            ]
        },
        review_questions=[
            "Phân tích cấu trúc bảng cân đối kế toán của ngân hàng thương mại và chỉ ra tại sao rủi ro thanh khoản luôn là rủi ro sống còn của định chế ngân hàng?",
            "Trình bày phương pháp tính toán chỉ số Biên lãi thuần (NIM) và phân tích các nhân tố làm xói mòn NIM trong giai đoạn cạnh tranh lãi suất gay gắt?",
            "Thiết lập mô hình kinh tế lượng đo lường hiệu quả chi phí (Cost Efficiency) của hệ thống NHTM bằng phương pháp SFA?"
        ]
    )
    
    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Quản trị Tài sản Có - Tài sản Nợ (ALM) và Quản trị Thanh khoản",
        introduction="Chương 2 trang bị kỹ năng quản trị tích hợp Tài sản Có và Tài sản Nợ (Asset-Liability Management - ALM), tối ưu hóa nguồn vốn huy động và bảo đảm khả năng thanh toán liên tục của ngân hàng.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Chiến lược quản trị ALM trong ngân hàng",
                "content": (
                    "Hội đồng Quản lý Tài sản Nợ - Tài sản Có (ALCO) là cơ quan chiến lược cao nhất tại ngân hàng chịu trách nhiệm điều phối "
                    "quy mô, cơ cấu kỳ hạn, loại tiền tệ và lãi suất của toàn bộ tài sản có và tài sản nợ. "
                    "Mục tiêu của ALM là tối đa hóa giá trị cổ đông dài hạn trong khi kiểm soát rủi ro lãi suất và rủi ro thanh khoản trong giới hạn khẩu vị rủi ro (Risk Appetite) cho phép.\n\n"
                    "Cơ chế chuyển giá vốn nội bộ (Funds Transfer Pricing - FTP) là công cụ điều tiết quan trọng của ALM, "
                    "giúp đo lường chính xác đóng góp lợi nhuận của từng chi nhánh huy động vốn và chi nhánh cho vay."
                ),
                "formulas": [
                    "Lợi nhuận biên đơn vị kinh doanh: Unit_Margin = Lending_Rate - FTP_rate (đối với cho vay) hoặc FTP_rate - Deposit_Rate (đối với huy động)",
                    "Mục tiêu ALM: Maximize NIM song song với Giảm thiểu Độ biến động của EVE"
                ],
                "case_studies": [
                    {
                        "title": "Ứng dụng hệ thống FTP đa đường cong tại VPBank",
                        "detail": "VPBank triển khai hệ thống FTP hiện đại dựa trên đường cong lãi suất chuẩn thị trường, bóc tách rủi ro thanh khoản và rủi ro lãi suất khỏi các chi nhánh bán lẻ về đơn vị Treasury trung tâm quản lý tập trung."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Quản trị rủi ro thanh khoản và các chỉ số an toàn",
                "content": (
                    "Rủi ro thanh khoản phát sinh khi ngân hàng không thể đáp ứng các nghĩa vụ chi trả tiền gửi đến hạn hoặc không tài trợ được cho các cam kết giải ngân mới "
                    "mà không phải chịu tổn thất tài chính nghiêm trọng. Quản trị thanh khoản đòi hỏi duy trì một đệm tài sản thanh khoản chất lượng cao (HQLA) "
                    "gồm tiền mặt, tiền gửi tại NHTW và Trái phiếu Chính phủ sẵn sàng bán hoặc chiết khấu trên thị trường mở (OMO).\n\n"
                    "Tại Việt Nam, các quy định an toàn thanh khoản then chốt gồm: Tỷ lệ dự trữ bắt buộc, Tỷ lệ dư nợ cho vay trên tổng tiền gửi (LDR tối đa 85%), "
                    "và Tỷ lệ tối đa nguồn vốn ngắn hạn được sử dụng để cho vay trung và dài hạn (hạ xuống mức 30%)."
                ),
                "formulas": [
                    "Tỷ lệ LDR: Loan-to-Deposit Ratio = Total Loans / Total Customer Deposits <= 85%",
                    "Tỷ lệ vốn ngắn hạn cho vay trung dài hạn: Short_for_MLT = (MLT_Loans - MLT_Capital) / Short_Term_Funding <= 30%",
                    "Hệ số LCR theo Basel III: LCR = HQLA / Net Cash Outflows (30 days) >= 100%"
                ],
                "case_studies": [
                    {
                        "title": "Áp lực tuân thủ tỷ lệ vốn ngắn hạn cho vay trung dài hạn 30%",
                        "detail": "Để đáp ứng lộ trình siết vốn ngắn hạn cho vay trung dài hạn của NHNN về 30%, các NHTM đẩy mạnh phát hành trái phiếu kỳ hạn 3-5 năm nhằm bổ sung nguồn vốn cấp 2 và ổn định cấu trúc kỳ hạn nguồn vốn."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Quản trị Thanh khoản Tối ưu (Optimal Liquidity Management) theo Rochet & Vives (2004): Giải quyết xung đột giữa Cơ chế Thị trường và Sự can thiệp của Người cho vay Cứu cánh Cuối cùng (LOLR).",
                "Tác động của Thanh khoản Nội sinh (Endogenous Liquidity) và Rủi ro Bán tháo Hoảng loạn (Fire-sale Externality) đến Hệ thống Ngân hàng.",
                "Mô hình Cân bằng Dòng tiền Ngân hàng Đa kỳ với Quy hoạch Ngẫu nhiên Tuyến tính (Stochastic Linear Programming)."
            ]
        },
        review_questions=[
            "Trình bày vai trò và cơ chế vận hành của hệ thống Chuyển giá vốn nội bộ (FTP) trong quản trị ALM của một ngân hàng thương mại?",
            "Phân tích ý nghĩa của quy định giới hạn tỷ lệ nguồn vốn ngắn hạn cho vay trung và dài hạn đối với việc kiểm soát rủi ro kỳ hạn của hệ thống ngân hàng Việt Nam?",
            "Thiết lập mô hình tối ưu hóa danh mục dự trữ tài sản thanh khoản (HQLA) nhằm cân bằng giữa chi phí cơ hội lợi nhuận và an toàn chi trả?"
        ]
    )
    
    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Quản trị Hoạt động Tín dụng và Quản lý Rủi ro Tín dụng",
        introduction="Chương 3 đi sâu vào nghiệp vụ cấp tín dụng, quy trình thẩm định khách hàng, hệ thống xếp hạng tín dụng nội bộ và các chuẩn mực quản lý nợ xấu, trích lập dự phòng rủi ro theo Basel II/III.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Quy trình cấp tín dụng và thẩm định khách hàng",
                "content": (
                    "Tín dụng là hoạt động sinh lời lớn nhất nhưng cũng mang lại rủi ro lớn nhất cho ngân hàng. "
                    "Quy trình cấp tín dụng khép kín bao gồm: Tìm kiếm khách hàng -> Thu thập hồ sơ -> Thẩm định tín dụng toàn diện -> Phê duyệt độc lập -> "
                    "Giải ngân kiểm soát chứng từ -> Giám sát thu hồi nợ và xử lý nợ có vấn đề.\n\n"
                    "Thẩm định tín dụng doanh nghiệp dựa trên nguyên tắc 5C/6C: Tư cách người vay (Character), Năng lực tài chính (Capacity), "
                    "Vốn tự có tham gia (Capital), Tài sản bảo đảm (Collateral), Điều kiện kinh tế ngành (Conditions) và Pháp lý tuân thủ (Compliance)."
                ),
                "formulas": [
                    "Hệ số bao phủ nợ: DSCR = (EBITDA - Thuế) / (Gốc đến hạn + Lãi vay) >= 1.25x",
                    "Tỷ lệ cho vay trên giá trị tài sản bảo đảm: LTV = Loan Amount / Appraised Value of Collateral <= 70%"
                ],
                "case_studies": [
                    {
                        "title": "Chuyển đổi phê duyệt tín dụng tập trung tại Trung tâm Phê duyệt Vùng",
                        "detail": "Các ngân hàng như BIDV, VietinBank, ACB chuyển đổi triệt để từ mô hình chi nhánh tự thẩm định tự duyệt sang mô hình tách bạch: Chi nhánh chuyên trách bán hàng (Front Office), thẩm định và định giá độc lập tập trung tại Back Office."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Phân loại nợ, trích lập dự phòng và quản lý nợ xấu",
                "content": (
                    "Theo Thông tư 11/2021/TT-NHNN, nợ ngân hàng được phân loại thành 5 nhóm: Nhóm 1 (Nợ đủ tiêu chuẩn, trích dự phòng cụ thể 0%); "
                    "Nhóm 2 (Nợ cần chú ý quá hạn từ 10-90 ngày, trích 5%); Nhóm 3 (Nợ dưới tiêu chuẩn quá hạn 91-180 ngày, trích 20%); "
                    "Nhóm 4 (Nợ nghi ngờ quá hạn 181-360 ngày, trích 50%); và Nhóm 5 (Nợ có khả năng mất vốn quá hạn trên 360 ngày, trích 100%).\n\n"
                    "Ngoài ra ngân hàng phải trích lập dự phòng chung 0.75% trên tổng dư nợ từ nhóm 1 đến nhóm 4. "
                    "Tỷ lệ bao phủ nợ xấu (LLR = Dự phòng cụ thể + chung / Nợ nhóm 3-5) phản ánh bộ đệm an toàn tài chính vững chắc của ngân hàng."
                ),
                "formulas": [
                    "Tỷ lệ nợ xấu: NPL Ratio = (Nợ nhóm 3 + 4 + 5) / Tổng dư nợ cho vay * 100% <= 3%",
                    "Tỷ lệ bao phủ nợ xấu: LLR = (Tổng số dư dự phòng rủi ro) / (Nợ nhóm 3 + 4 + 5) * 100%",
                    "Dự phòng cụ thể = max(0, Dư nợ - Giá trị tài sản bảo đảm đã chiết khấu) * Tỷ lệ trích lập nhóm nợ"
                ],
                "case_studies": [
                    {
                        "title": "Tỷ lệ bao phủ nợ xấu kỷ lục tại Vietcombank",
                        "detail": "Vietcombank duy trì tỷ lệ LLR lên tới trên 250-300%, nghĩa là với mỗi 1 đồng nợ xấu, ngân hàng đã trích lập sẵn sàng gần 3 đồng dự phòng trong bảng cân đối, triệt tiêu mọi nguy cơ bào mòn lợi nhuận tương lai."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Xếp hạng Nội bộ Nâng cao (A-IRB) theo Basel II/III: Ước lượng ba tham số cốt lõi: Xác suất Vỡ nợ (PD), Tỷ lệ Tổn thất khi Vỡ nợ (LGD), và Dư nợ tại thời điểm Vỡ nợ (EAD).",
                "Tổn thất Dự tính (Expected Loss): EL = PD * LGD * EAD và Tổn thất Bất thường (Unexpected Loss - UL) theo Mô hình Một Nhân tố Tiềm ẩn Vasicek (2002).",
                "Mô hình Chấm điểm Tín dụng Bằng Machine Learning (XGBoost, Random Forest, Neural Networks) kết hợp Giải thích Mô hình SHAP Values."
            ]
        },
        review_questions=[
            "Trình bày chi tiết 5 nhóm nợ theo quy định của Ngân hàng Nhà nước và nêu công thức tính dự phòng rủi ro cụ thể có xét đến giá trị tài sản bảo đảm?",
            "Tại sao tỷ lệ bao phủ nợ xấu (LLR) lại là chỉ báo quan trọng hàng đầu để đánh giá chất lượng tài sản và tính bền vững lợi nhuận của ngân hàng?",
            "Chứng minh công thức phân phối vốn rủi ro của Vasicek (2002) áp dụng trong Trụ cột 1 của Hiệp ước Basel II?"
        ]
    )
    
    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Quản trị Rủi ro Lãi suất trên Sổ Ngân hàng (IRRBB) và Rủi ro Thị trường",
        introduction="Chương 4 phân tích các kỹ thuật lượng hóa rủi ro lãi suất phát sinh từ sự mất cân xứng về kỳ hạn định giá lại của tài sản và nợ, cùng các phương pháp quản trị rủi ro hối đoái và rủi ro thị trường.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Đo lường rủi ro lãi suất: Mô hình Repricing Gap và Duration Gap",
                "content": (
                    "Rủi ro lãi suất trên sổ ngân hàng (IRRBB) là rủi ro suy giảm thu nhập lãi hoặc vốn chủ sở hữu khi lãi suất thị trường biến động. "
                    "Hai phương pháp đo lường kinh điển gồm: "
                    "1. Mô hình Khe hở Định giá lại (Repricing Model): Phân nhóm tài sản và nợ nhạy cảm lãi suất (RSA và RSL) theo từng khung thời gian. "
                    "Nếu RSA > RSL (Khe hở dương), lãi suất tăng làm tăng thu nhập lãi thuần NII;\n\n"
                    "2. Mô hình Khe hở Kỳ hạn (Duration Gap): Đánh giá tác động của biến động lãi suất đến Giá trị Kinh tế của Vốn chủ sở hữu (Economic Value of Equity - EVE). "
                    "Bằng cách cân bằng Duration của tài sản và nợ, ngân hàng có thể miễn nhiễm EVE trước các cú sốc lãi suất song song."
                ),
                "formulas": [
                    "Khe hở định giá lại: Gap = RSA - RSL",
                    "Biến động thu nhập lãi thuần: Delta NII = Gap * Delta i",
                    "Khe hở thời lượng: Duration Gap (DG) = D_A - (Total Liabilities / Total Assets) * D_L",
                    "Biến động vốn chủ sở hữu: Delta E = - [ D_A - (L/A) * D_L ] * Total Assets * [ Delta i / (1 + i) ]"
                ],
                "case_studies": [
                    {
                        "title": "Quản trị khe hở kỳ hạn tại các NHTM khi lãi suất huy động đảo chiều",
                        "detail": "Khi lãi suất liên ngân hàng tăng vọt vào cuối năm 2022, các ngân hàng có Duration Gap dương lớn chịu áp lực sụt giảm EVE mạnh, thúc đẩy các bộ phận Treasury tái cơ cấu danh mục tài sản nhạy cảm lãi suất."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Quản trị rủi ro hối đoái và rủi ro thị trường",
                "content": (
                    "Rủi ro hối đoái phát sinh từ sự mất cân đối giữa tài sản có bằng ngoại tệ và tài sản nợ bằng ngoại tệ. "
                    "Trạng thái ngoại tệ ròng (Net Open Position - NOP) đo lường mức độ rủi ro hối đoái của ngân hàng. "
                    "Quy định của NHNN giới hạn trạng thái ngoại tệ ròng cuối ngày không được vượt quá +/- 20% vốn tự có của ngân hàng.\n\n"
                    "Rủi ro thị trường trên sổ kinh doanh (Trading Book) được lượng hóa bằng mô hình Giá trị Chịu rủi ro (Value at Risk - VaR), "
                    "xác định mức tổn thất tối đa có thể xảy ra trong một khoảng thời gian xác định (ví dụ 10 ngày) tại mức độ tin cậy nhất định (ví dụ 99%)."
                ),
                "formulas": [
                    "Trạng thái ngoại tệ ròng: NOP = Ngoại tệ Tài sản Có - Ngoại tệ Tài sản Nợ (tính bằng % Vốn tự có)",
                    "Mô hình VaR tham số: VaR_{alpha, T} = Position * Z_{alpha} * sigma * sqrt(T)",
                    "Tỷ lệ giới hạn trạng thái ngoại tệ: |NOP| <= 20% Vốn tự có theo quy định NHNN"
                ],
                "case_studies": [
                    {
                        "title": "Nghiệp vụ phòng ngừa rủi ro tỷ giá cho doanh nghiệp XNK bằng Hợp đồng Kỳ hạn (Forward)",
                        "detail": "Các ngân hàng bán hợp đồng Forward USD/VND kỳ hạn 3-6 tháng cho doanh nghiệp xuất nhập khẩu, đồng thời thực hiện cân bằng trạng thái ngoại tệ ròng trên thị trường liên ngân hàng."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Khung Chuẩn mực Mới về Rủi ro Lãi suất trên Sổ Ngân hàng (BCBS 2016 IRRBB Standards): 6 kịch bản Sốc Lãi suất Giả định (Parallel up/down, Flattener, Steepener, Short rate up/down).",
                "Đo lường Rủi ro Thị trường theo Khung Đánh giá Toàn diện Sổ Giao dịch (FRTB - Fundamental Review of the Trading Book): Chuyển đổi từ VaR sang Expected Shortfall (ES).",
                "Mô hình Hành vi Tiền gửi Không Kỳ hạn NMDs (Non-Maturing Deposits) và Tùy chọn Trả nợ Trước Hạn (Prepayment Options) trong Định lượng EVE."
            ]
        },
        review_questions=[
            "Phân tích cơ chế tác động của biến động lãi suất đến Giá trị Kinh tế của Vốn chủ sở hữu (EVE) thông qua chỉ số Duration Gap?",
            "Trình bày phương pháp tính toán trạng thái ngoại tệ ròng (NOP) và giải thích tại sao NHNN lại khống chế giới hạn NOP không vượt quá 20% vốn tự có?",
            "So sánh sự khác biệt bản chất giữa hai thước đo rủi ro thị trường: Value at Risk (VaR) và Expected Shortfall (ES) theo chuẩn mực Basel III FRTB?"
        ]
    )
    
    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Quản trị Rủi ro Hoạt động, Ngân hàng Số và Khung Khổ An toàn Vốn",
        introduction="Chương 5 hoàn thiện giáo trình với việc nghiên cứu rủi ro hoạt động, xu thế cách mạng ngân hàng số (Fintech/Neobanks) và quy trình đánh giá mức độ đủ vốn nội bộ (ICAAP) theo Basel II/III.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Rủi ro hoạt động và an ninh mạng trong ngân hàng số",
                "content": (
                    "Rủi ro hoạt động (Operational Risk) là rủi ro tổn thất phát sinh từ sự không đầy đủ hoặc sai hỏng của các quy trình nội bộ, "
                    "hành vi con người, lỗi hệ thống công nghệ thông tin hoặc từ các sự kiện bên ngoài (gian lận gian lận mạng, thiên tai, dịch bệnh). "
                    "Sự bùng nổ của ngân hàng số (Digital Banking), thanh toán không tiếp xúc và ngân hàng mở (Open API) "
                    "làm dịch chuyển trọng tâm rủi ro hoạt động sang rủi ro an ninh mạng và rò rỉ dữ liệu khách hàng.\n\n"
                    "Các ngân hàng triển khai kiến trúc bảo mật Zero Trust, ứng dụng công nghệ sinh trắc học (eKYC, nhận diện khuôn mặt) "
                    "theo Quyết định 2345/QĐ-NHNN để xác thực các giao dịch chuyển tiền giá trị cao."
                ),
                "formulas": [
                    "Phương pháp Chỉ số Cơ bản (BIA Basel II): K_BIA = [ sum_{t=1}^3 max(GI_t * alpha, 0) ] / n (với alpha = 15%, GI là tổng thu nhập hoạt động)",
                    "Tiêu chuẩn bảo mật sinh trắc học Quyết định 2345: Giao dịch chuyển tiền trên 10 triệu VND/lần hoặc trên 20 triệu VND/ngày bắt buộc phải xác thực khuôn mặt khớp với dữ liệu CCCD gắn chip"
                ],
                "case_studies": [
                    {
                        "title": "Áp dụng bắt buộc sinh trắc học eKYC từ ngày 01/07/2024",
                        "detail": "Toàn bộ hệ thống ngân hàng thương mại Việt Nam triển khai thành công việc thu thập dữ liệu sinh trắc học khuôn mặt từ CCCD gắn chip cho hơn 30 triệu tài khoản khách hàng, giảm thiểu tới 80% số vụ gian lận lừa đảo chiếm đoạt tiền qua tài khoản 'rác'."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Khung khổ an toàn vốn Basel II/III và quy trình ICAAP",
                "content": (
                    "Hiệp ước Basel thiết lập chuẩn mực toàn cầu về an toàn vốn ngân hàng dựa trên ba trụ cột: "
                    "Trụ cột 1 (Yêu cầu vốn tối thiểu cho Rủi ro tín dụng, Rủi ro thị trường và Rủi ro hoạt động: CAR >= 8%); "
                    "Trụ cột 2 (Quy trình đánh giá nội bộ mức độ đủ vốn - ICAAP và sự can thiệp của cơ quan thanh tra giám sát ngân hàng); "
                    "Trụ cột 3 (Kỷ luật thị trường và minh bạch thông tin công khai).\n\n"
                    "Quy trình ICAAP yêu cầu ngân hàng phải đánh giá đầy đủ toàn bộ các loại rủi ro trọng yếu (bao gồm cả rủi ro tập trung, rủi ro danh tiếng) "
                    "và thực hiện kiểm tra sức chịu đựng (Stress Testing) định kỳ để bảo đảm duy trì đủ vốn trong các kịch bản kinh tế khủng hoảng."
                ),
                "formulas": [
                    "Tỷ lệ an toàn vốn hợp nhất: CAR = Total Regulatory Capital / (RWA_credit + RWA_market + RWA_operational) >= 8%",
                    "Vốn cấp 1 cốt lõi: Tier 1 Capital Ratio = Tier 1 / Total RWA >= 6%"
                ],
                "case_studies": [
                    {
                        "title": "Thí điểm áp dụng khung Basel III tại các ngân hàng tư nhân hàng đầu",
                        "detail": "VPBank, Techcombank, OCB, HDBank hoàn thành triển khai toàn diện Trụ cột 2 ICAAP và công bố các chỉ số an toàn vốn CAR đạt từ 12% đến 15%, cao vượt trội so với yêu cầu tối thiểu 8% của Thông tư 41/2016/TT-NHNN."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp Kiểm tra Sức chịu đựng Kinh tế Vĩ mô (Macroprudential Stress Testing): Xây dựng Kịch bản Cú sốc Suy thoái Vĩ mô (Adverse Scenario) và Phỏng chiếu Bảng Cân đối Động.",
                "Rủi ro Ngân hàng Bóng đêm (Shadow Banking System) và Tác động Lan truyền Sang Hệ thống Ngân hàng Truyền thống theo Acharya et al. (2013).",
                "Cấu trúc Vốn Tối ưu của Ngân hàng và Chi phí Xã hội của Quy định Tăng Vốn Tối thiểu (The Bankers' New Clothes Debate: Admati & Hellwig 2013)."
            ]
        },
        review_questions=[
            "Phân tích ba trụ cột cốt lõi của Hiệp ước Basel II và chỉ ra những điểm cải tiến đột phá của Hiệp ước Basel III về chất lượng vốn tự có?",
            "Trình bày các bước thực hiện Quy trình Đánh giá Nội bộ Mức độ Đủ vốn (ICAAP) và vai trò của Stress Testing trong việc xác định vốn mục tiêu?",
            "Thiết lập mô hình kinh tế lượng Vector Autoregression (VAR) liên kết các biến số vĩ mô (GDP, Lãi suất, Lạm phát) với Tỷ lệ Nợ xấu (NPL) phục vụ Macro Stress Testing?"
        ]
    )
    
    pages, sz = b.save(out_pdf)
    print(f"[SUCCESS] Book 7 saved: {out_pdf} ({pages} pages, {sz:.2f} MB)")
    return {
        "title": title,
        "code": subject_code,
        "author": authors,
        "path": out_pdf,
        "pages": pages,
        "size_mb": round(sz, 2)
    }

if __name__ == "__main__":
    build_nhtm()
