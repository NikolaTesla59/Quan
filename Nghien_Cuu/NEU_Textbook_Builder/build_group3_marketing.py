# -*- coding: utf-8 -*-
"""
NEU Master Textbook Builder - Group 3: Marketing & Innovation
Covers 5 Courses:
1. Marketing căn bản - PGS.TS Trần Minh Đạo
2. Quản trị Marketing - PGS.TS Trần Minh Đạo
3. Hành vi người tiêu dùng - PGS.TS Vũ Trí Dũng
4. Khởi sự kinh doanh & Đổi mới sáng tạo - PGS.TS Trương Thị Nam Thắng
5. Nghiên cứu Marketing - PGS.TS Nguyễn Viết Lâm
"""
import os
import sys

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

BASE_DIR_06 = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\06_Kinh tế học, Quản trị kinh doanh & Marketing"

def build_principles_of_marketing():
    print("Building: Marketing căn bản...")
    builder = NEUTextbookBuilder(
        title="Marketing căn bản",
        subject_code="MKTB1101",
        faculty="Khoa Marketing",
        authors="PGS.TS. Trần Minh Đạo & Tập thể Giảng viên (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, HIỆN ĐẠI HÓA THEO CHUẨN MARKETING 5.0 & DIGITAL OMNICHANNEL"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Nhập môn Marketing và Quản trị mối quan hệ khách hàng",
         "topics": ["Bản chất của Marketing: Nhu cầu, mong muốn, giá trị và sự thỏa mãn", "Sự tiến hóa của các quan điểm định hướng Marketing", "Xây dựng mối quan hệ khách hàng sinh lời (CRM) và Giá trị trọn đời khách hàng (CLV)"]},
        {"chapter_num": 2, "chapter_title": "Môi trường Marketing và Hệ thống thông tin Marketing",
         "topics": ["Phân tích môi trường vĩ mô (PESTEL) và môi trường vi mô của doanh nghiệp", "Hệ thống thông tin Marketing (MIS) và quy trình nghiên cứu thị trường", "Phân tích cạnh tranh và ma trận SWOT"]},
        {"chapter_num": 3, "chapter_title": "Chiến lược STP: Phân đoạn, Chọn thị trường mục tiêu và Định vị",
         "topics": ["Các tiêu thức phân đoạn thị trường người tiêu dùng và tổ chức", "Đánh giá và lựa chọn thị trường mục tiêu (Targeting)", "Chiến lược định vị thương hiệu (Positioning) và Bản đồ nhận thức (Perceptual Map)"]},
        {"chapter_num": 4, "chapter_title": "Chiến lược Sản phẩm (Product) và Quản trị thương hiệu",
         "topics": ["Cấu trúc 3 cấp độ sản phẩm và quyết định dòng sản phẩm", "Chu kỳ sống của sản phẩm (PLC) và chiến lược Marketing theo từng giai đoạn", "Xây dựng tài sản thương hiệu (Brand Equity) và nhãn hiệu"]},
        {"chapter_num": 5, "chapter_title": "Chiến lược Giá cả (Price) và Các mô hình định giá",
         "topics": ["Các yếu tố ảnh hưởng đến quyết định giá", "Các phương pháp định giá: Dựa trên chi phí, dựa trên giá trị cảm nhận, dựa trên đối thủ", "Chiến lược giá sản phẩm mới: Hớt váng (Skimming) vs Thâm nhập (Penetration)"]},
        {"chapter_num": 6, "chapter_title": "Chiến lược Phân phối (Place) và Quản trị kênh Marketing",
         "topics": ["Bản chất và cấu trúc kênh phân phối", "Hành vi và xung đột kênh phân phối (Xung đột dọc và ngang)", "Bán lẻ, bán buôn và xu hướng phân phối đa kênh hợp nhất (Omnichannel)"]},
        {"chapter_num": 7, "chapter_title": "Chiến lược Xúc tiến hỗn hợp (Promotion) và Truyền thông IMC",
         "topics": ["Mô hình truyền thông và quy trình lập kế hoạch IMC", "Hỗn hợp xúc tiến: Quảng cáo, Khuyến mại, PR, Bán hàng cá nhân", "Marketing số (Digital Marketing) và Marketing mạng xã hội"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=3,
        chap_title="Chiến lược STP: Phân đoạn, Chọn thị trường mục tiêu và Định vị",
        introduction="STP là trái tim của Marketing hiện đại. Chương này trang bị phương pháp phân đoạn thị trường khoa học, lựa chọn phân khúc mục tiêu tối ưu và xác lập vị trí độc tôn của thương hiệu trong tâm trí khách hàng.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Phân đoạn thị trường và Lựa chọn thị trường mục tiêu",
                "content": "Phân đoạn thị trường là quá trình phân chia thị trường không đồng nhất thành các nhóm khách hàng đồng nhất có nhu cầu, hành vi và đặc điểm tương tự nhau. Bốn tiêu thức phân đoạn phổ biến: Địa lý, Nhân khẩu học, Tâm lý học (Lối sống, giá trị) và Hành vi (Lợi ích tìm kiếm, tỷ lệ sử dụng, lòng trung thành).\n\nDoanh nghiệp đánh giá tính hấp dẫn của phân đoạn dựa trên quy mô, tốc độ tăng trưởng, cường độ cạnh tranh và mức độ phù hợp với năng lực cốt lõi để chọn chiến lược: Marketing không phân biệt, phân biệt hoặc tập trung (thị trường ngách).",
                "formulas": [
                    "Quy mô doanh thu thị trường mục tiêu: TR = N * q * P (N: số khách hàng, q: lượng mua TB, P: đơn giá)",
                    "Tiêu chuẩn phân đoạn hiệu quả: Measurable (Đo lường được), Accessible (Tiếp cận được), Substantial (Đủ lớn), Differentiable (Phân biệt rõ), Actionable (Khả thi)"
                ],
                "case_studies": [
                    {"title": "Chiến lược phân đoạn khách hàng của Viettel Telecom", "detail": "Phân tích chiến lược cá nhân hóa gói cước theo từng nhóm đối tượng học sinh - sinh viên (Mocha/GenZ), công chức và doanh nhân (Vip/SME)."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Chiến lược Định vị thương hiệu và Tuyên ngôn định vị",
                "content": "Định vị (Positioning) là việc thiết kế sản phẩm và hình ảnh của doanh nghiệp nhằm chiếm lĩnh một vị trí khác biệt, có giá trị trong tâm trí của khách hàng mục tiêu so với các đối thủ cạnh tranh.\n\nBản đồ định vị (Perceptual Mapping) trực quan hóa nhận thức của khách hàng về các thương hiệu dựa trên hai trục thuộc tính trọng yếu (ví dụ: Giá cả vs Chất lượng; Truyền thống vs Hiện đại).",
                "formulas": [
                    "Cấu trúc Tuyên ngôn định vị chuẩn: 'Dành cho [Khách hàng mục tiêu], [Thương hiệu] là [Khung quy chiếu] mang lại [Lợi ích khác biệt cốt lõi] bởi vì [Lý do tin tưởng].'",
                    "Khoảng cách nhận thức Euclid trên bản đồ định vị: d_{ij} = sqrt(sum((x_{ik} - x_{jk})^2))"
                ],
                "case_studies": [
                    {"title": "Định vị 'Thật sự thiên nhiên' của TH True Milk", "detail": "Phân tích chiến lược định vị khác biệt hóa dựa trên dòng sản phẩm sữa tươi sạch nguyên chất 100%, phá vỡ thế độc tôn của sữa hoàn nguyên tại thị trường Việt Nam."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Logic Thống trị Dịch vụ (Service-Dominant Logic - S-D Logic của Vargo & Lusch): Giá trị Được Đồng Kiến tạo (Co-creation of Value) thay thế Khái niệm Hàng hóa Truyền thống.",
                "Đo lường Tài sản Khách hàng (Customer Equity) và Tối ưu hóa Giá trị Trọn đời Khách hàng (CLV) bằng Mô hình Xác suất Beta-Geometric/Negative Binomial Distribution (BG/NBD).",
                "Marketing Tương tác Dựa trên Trí tuệ Nhân tạo (AI-Driven Real-Time Algorithmic Personalization) và Quản trị Quyền riêng tư Dữ liệu Khách hàng."
            ]
        },
        review_questions=[
            "Trình bày 3 bước của quy trình STP (Segmentation, Targeting, Positioning) và phân tích mối quan hệ hữu cơ giữa chúng.",
            "Thế nào là bản đồ nhận thức (Perceptual Map)? Hãy vẽ bản đồ định vị ngành cà phê chuỗi tại Việt Nam (Trung Nguyên, Highlands, Phúc Long, Starbucks).",
            "Phân tích 5 điều kiện cần thiết để một phân đoạn thị trường được coi là có hiệu quả kinh doanh."
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Marketing căn bản - PGS.TS Trần Minh Đạo (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Marketing căn bản - PGS.TS Trần Minh Đạo (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Marketing căn bản", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_marketing_management():
    print("Building: Quản trị Marketing...")
    builder = NEUTextbookBuilder(
        title="Quản trị Marketing",
        subject_code="QTMK1101",
        faculty="Khoa Marketing",
        authors="PGS.TS. Trần Minh Đạo & PGS.TS. Vũ Minh Đức (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, HIỆN ĐẠI HÓA CHUẨN MARKETING STRATEGY & MARKETING ANALYTICS"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về Quản trị Marketing và Kế hoạch Marketing chiến lược",
         "topics": ["Bản chất và quy trình 5 giai đoạn của quản trị Marketing", "Phân tích cơ hội thị trường và khoảng trống chiến lược", "Cấu trúc bản kế hoạch Marketing chiến lược hàng năm"]},
        {"chapter_num": 2, "chapter_title": "Marketing doanh nghiệp với doanh nghiệp (B2B Marketing)",
         "topics": ["Đặc điểm thị trường B2B và hành vi mua của khách hàng tổ chức", "Trung tâm mua hàng (Buying Center) và các vai trò", "Quản trị quan hệ đối tác B2B (Key Account Management)"]},
        {"chapter_num": 3, "chapter_title": "Chiến lược cạnh tranh theo vị thế thị trường của doanh nghiệp",
         "topics": ["Chiến lược dành cho doanh nghiệp dẫn đầu thị trường (Market Leader)", "Chiến lược dành cho doanh nghiệp thách thức thị trường (Market Challenger)", "Chiến lược dành cho doanh nghiệp theo sau (Follower) và nép góc (Nicher)"]},
        {"chapter_num": 4, "chapter_title": "Quản trị tài sản thương hiệu và Kiến trúc thương hiệu",
         "topics": ["Mô hình tài sản thương hiệu dựa trên khách hàng (CBBE Keller)", "Kiến trúc thương hiệu: Ngôi nhà thương hiệu (Branded House) vs Ngôi nhà các thương hiệu (House of Brands)", "Mở rộng thương hiệu (Brand Extension) và quản lý khủng hoảng truyền thông"]},
        {"chapter_num": 5, "chapter_title": "Quản trị trải nghiệm khách hàng (CXM) và Điểm chạm số",
         "topics": ["Hành trình khách hàng (Customer Journey Mapping) đa điểm chạm", "Cá nhân hóa trải nghiệm và phân tích cảm xúc (Sentiment Analysis)", "Mô hình đo lường chỉ số hài lòng (CSAT, CES, NPS)"]},
        {"chapter_num": 6, "chapter_title": "Kiểm toán Marketing và Đo lường hiệu quả Marketing (ROMI)",
         "topics": ["Hệ thống kiểm toán Marketing (Marketing Audit)", "Các chỉ số tài chính và phi tài chính trong đánh giá hiệu quả Marketing", "Tối ưu hóa tỷ suất sinh lời đầu tư Marketing (Return on Marketing Investment - ROMI)"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=6,
        chap_title="Kiểm toán Marketing và Đo lường hiệu quả Marketing (ROMI)",
        introduction="Quản trị Marketing hiện đại đòi hỏi khả năng định lượng chính xác hiệu quả đầu tư. Chương này cung cấp hệ thống chỉ số phân tích dữ liệu Marketing (Marketing Analytics) và khung kiểm toán toàn diện.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Tỷ suất Sinh lời Đầu tư Marketing (ROMI) và Các chỉ số Hiệu năng",
                "content": "ROMI đo lường mức độ gia tăng doanh thu và lợi nhuận thuần túy do các chương trình Marketing mang lại so với tổng chi phí Marketing đã bỏ ra.\n\nCác chỉ số hiệu năng bổ trợ bao gồm: Chi phí thu hút một khách hàng mới (Customer Acquisition Cost - CAC), Giá trị trọn đời khách hàng (Customer Lifetime Value - CLV), Tỷ lệ duy trì khách hàng (Retention Rate), và Điểm người giới thiệu thuần (Net Promoter Score - NPS).",
                "formulas": [
                    "Chỉ số ROMI: ROMI = [(Doanh thu gia tăng * Biên lợi nhuận gộp) - Chi phí Marketing] / Chi phí Marketing",
                    "Tỷ lệ hoàn vốn CLV / CAC: Chuẩn mực lành mạnh khi CLV / CAC >= 3.0",
                    "Chỉ số NPS: NPS = % Khách hàng ủng hộ (Promoters) - % Khách hàng gièm pha (Detractors)"
                ],
                "case_studies": [
                    {"title": "Đo lường ROMI chiến dịch số của sàn TMĐT Shopee Việt Nam", "detail": "Phân tích mô hình phân bổ đa điểm chạm (Multi-touch Attribution) tính toán hiệu quả quảng cáo livestream và khuyến mãi Mega Sale 11.11."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Đo lường Hỗn hợp Marketing (Marketing Mix Modeling - MMM) bằng Kỹ thuật Kinh tế lượng Dữ liệu Mảng (Panel Data Econometrics) và Bayesian Time-Varying Parameters.",
                "Mô hình Phân bổ Đa Điểm chạm Dựa trên Trò chơi Hợp tác Shapley (Shapley Value Multi-Touch Attribution) trong Môi trường Omnichannel.",
                "Tác động của Tài sản Tiếp thị Số (Digital Marketing Assets) đến Giá trị Vốn hóa Doanh nghiệp (Tobin's Q và Stock Return Volatility)."
            ]
        },
        review_questions=[
            "Công thức tính ROMI là gì? Phân tích tại sao nhiều doanh nghiệp gặp khó khăn khi bóc tách doanh thu thuần túy do Marketing tạo ra.",
            "Trình bày 4 nội dung trọng tâm của một cuộc Kiểm toán Marketing (Marketing Audit) định kỳ.",
            "Giải thích ý nghĩa của tỷ lệ CLV / CAC trong việc đánh giá tính bền vững của mô hình kinh doanh khởi nghiệp công nghệ."
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Quản trị Marketing - PGS.TS Trần Minh Đạo (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Quản trị Marketing - PGS.TS Trần Minh Đạo (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Quản trị Marketing", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_consumer_behavior():
    print("Building: Hành vi người tiêu dùng...")
    builder = NEUTextbookBuilder(
        title="Hành vi người tiêu dùng",
        subject_code="HVNT1101",
        faculty="Khoa Marketing",
        authors="PGS.TS. Vũ Trí Dũng & TS. Đào Hoài Nam (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, TÍCH HỢP KINH TẾ HỌC HÀNH VI (BEHAVIORAL ECONOMICS) & NEUROMARKETING"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về nghiên cứu hành vi người tiêu dùng",
         "topics": ["Bản chất và tầm quan trọng của việc nghiên cứu hành vi người tiêu dùng", "Mô hình hộp đen người tiêu dùng và các giai đoạn tiến hóa", "Mô hình quá trình ra quyết định mua 5 bước"]},
        {"chapter_num": 2, "chapter_title": "Các yếu tố tâm lý tác động: Động cơ, Nhận thức và Học hỏi",
         "topics": ["Hệ thống động cơ: Tháp nhu cầu Maslow và xung đột động cơ", "Quá trình nhận thức: Tiếp xúc, chú ý, giải thích và định kiến nhận thức", "Học hỏi và trí nhớ: Điều kiện hóa cổ điển và phản ứng có điều kiện"]},
        {"chapter_num": 3, "chapter_title": "Thái độ người tiêu dùng và Sự thay đổi thái độ",
         "topics": ["Cấu trúc thái độ: Mô hình 3 thành phần ABC (Affect, Behavior, Cognition)", "Mô hình thái độ đa thuộc tính Fishbein", "Lý thuyết hành động hợp lý (TRA) và Thuyết hành vi có kế hoạch (TPB)"]},
        {"chapter_num": 4, "chapter_title": "Các yếu tố cá nhân, Tính cách và Lối sống",
         "topics": ["Nhân khẩu học và chu kỳ đời sống gia đình", "Tính cách, bản ngã (Self-Concept) và thương hiệu", "Phân tích lối sống và hệ thống giá trị (VALS Framework)"]},
        {"chapter_num": 5, "chapter_title": "Ảnh hưởng của Văn hóa, Xã hội và Nhóm tham khảo",
         "topics": ["Văn hóa và các giá trị văn hóa cốt lõi của người Việt", "Giai tầng xã hội và hành vi tiêu dùng phô trương (Conspicuous Consumption)", "Nhóm tham khảo, người có ảnh hưởng (KOLs, KOCs) và truyền miệng trực tuyến (eWOM)"]},
        {"chapter_num": 6, "chapter_title": "Hành vi người tiêu dùng trên môi trường số và Kinh tế học hành vi",
         "topics": ["Hành vi mua sắm trực tuyến và bốc đồng (Impulse Buying)", "Hiệu ứng tâm lý FOMO và tâm lý bầy đàn", "Lý thuyết viễn cảnh (Prospect Theory) và Kiến trúc lựa chọn (Nudge Theory)"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=3,
        chap_title="Thái độ người tiêu dùng và Sự thay đổi thái độ",
        introduction="Thái độ là trạng thái tâm lý tương đối bền vững định hướng hành vi mua. Chương này phân tích cấu trúc thái độ và các mô hình dự báo ý định hành vi tiêu dùng chuẩn mực quốc tế.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Mô hình Ba thành phần ABC và Mô hình Fishbein",
                "content": "Thái độ bao gồm 3 thành phần mật thiết: Thành phần nhận thức (Cognition - niềm tin và sự hiểu biết về sản phẩm); Thành phần cảm xúc (Affect - tình cảm yêu ghét, cảm xúc); và Thành phần hành vi (Behavior - ý định mua hoặc sử dụng thực tế).\n\nMô hình đa thuộc tính Fishbein lượng hóa thái độ tổng thể bằng cách tổng hợp niềm tin của người tiêu dùng về mức độ sở hữu các thuộc tính nhân với tầm quan trọng của từng thuộc tính đó.",
                "formulas": [
                    "Mô hình Fishbein: A_o = sum_{i=1}^n (b_i * e_i)",
                    "Trong đó: A_o: Thái độ đối với đối tượng; b_i: Niềm tin đối tượng sở hữu thuộc tính i; e_i: Đánh giá tầm quan trọng thuộc tính i"
                ],
                "case_studies": [
                    {"title": "Đánh giá thái độ người tiêu dùng đối với xe máy điện VinFast", "detail": "Ứng dụng mô hình Fishbein khảo sát niềm tin của khách hàng trẻ đối với các thuộc tính: Tiết kiệm chi phí nhiên liệu, bảo vệ môi trường, thiết kế kiểu dáng và hạ tầng trạm đổi pin."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Thuyết Hành động Hợp lý (TRA) và Thuyết Hành vi có Kế hoạch (TPB)",
                "content": "Mô hình TRA (Fishbein & Ajzen) chỉ ra rằng hành vi thực tế được dự báo trực tiếp bởi Ý định hành vi (Behavioral Intention). Ý định hành vi lại chịu sự tác động đồng thời của Thái độ đối với hành vi và Chuẩn chủ quan (Subjective Norm - áp lực từ xã hội, gia đình, bạn bè).\n\nAjzen mở rộng thành mô hình TPB bằng cách bổ sung thêm yếu tố Nhận thức kiểm soát hành vi (Perceived Behavioral Control - PBC) phản ánh mức độ tự tin về nguồn lực, thời gian và tiền bạc để thực hiện hành vi.",
                "formulas": [
                    "Phương trình TPB: BI = w_1 * A + w_2 * SN + w_3 * PBC",
                    "Hành vi thực tế: Behavior = f(BI, PBC)"
                ],
                "case_studies": [
                    {"title": "Dự báo ý định tiêu dùng thực phẩm hữu cơ (Organic Food) tại Hà Nội và TP.HCM", "detail": "Phân tích thực nghiệm mô hình TPB chỉ ra chuẩn chủ quan và nhận thức sức khỏe cá nhân tác động tích cực nhất đến ý định chi trả giá cao cho thực phẩm hữu cơ."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Viễn cảnh của Daniel Kahneman & Amos Tversky (Prospect Theory - Nobel 2002): Hàm Giá trị Hình chữ S, Tính Nhạy cảm Biên Giảm dần và Định kiến Sợ Mất mát (Loss Aversion).",
                "Thuyết Hích (Nudge Theory - Richard Thaler - Nobel 2017): Kiến trúc Lựa chọn (Choice Architecture) và Mặc định hóa (Default Options) trong Tác động Hành vi Tiêu dùng Bền vững.",
                "Phương pháp Thần kinh học Tiếp thị (Neuromarketing): Ứng dụng Điện não đồ (EEG), Theo dõi Ánh mắt (Eye-tracking) và fMRI giải mã Phản ứng Vô thức của Não bộ đối với Thương hiệu."
            ]
        },
        review_questions=[
            "Trình bày cấu trúc 3 thành phần ABC của thái độ. Trong các chiến dịch quảng cáo cảm xúc (Emotional Advertising), thành phần nào được tác động đầu tiên?",
            "Vẽ sơ đồ mô hình Thuyết hành vi có kế hoạch (TPB) của Ajzen và giải thích ý nghĩa của biến Nhận thức kiểm soát hành vi (PBC).",
            "Phân tích hiện tượng Bất hòa nhận thức sau khi mua (Post-purchase Cognitive Dissonance) và các biện pháp Marketing giúp giảm thiểu hiện tượng này."
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Hành vi người tiêu dùng - PGS.TS Vũ Trí Dũng (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Hành vi người tiêu dùng - PGS.TS Vũ Trí Dũng (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Hành vi người tiêu dùng", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_entrepreneurship():
    print("Building: Khởi sự kinh doanh & Đổi mới sáng tạo...")
    builder = NEUTextbookBuilder(
        title="Khởi sự kinh doanh & Đổi mới sáng tạo",
        subject_code="KSKD1101",
        faculty="Trung tâm Khởi nghiệp & Đổi mới sáng tạo (CEI-NEU)",
        authors="PGS.TS. Trương Thị Nam Thắng & TS. Đỗ Hương Hiển (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, TÍCH HỢP KHỞI NGHIỆP TINH GỌN (LEAN STARTUP) & TƯ DUY THIẾT KẾ"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Bản chất của Khởi nghiệp, Tinh thần Doanh nhân và Đổi mới sáng tạo",
         "topics": ["Khái niệm Khởi nghiệp (Startup) vs Doanh nghiệp nhỏ truyền thống (SME)", "Tư duy doanh nhân (Entrepreneurial Mindset) và sự chấp nhận rủi ro", "Phân loại đổi mới sáng tạo: Duy trì (Sustaining) vs Phá vỡ (Disruptive) của Christensen"]},
        {"chapter_num": 2, "chapter_title": "Nhận diện cơ hội kinh doanh và Tư duy thiết kế (Design Thinking)",
         "topics": ["Nguồn gốc cơ hội kinh doanh: Xu hướng công nghệ, thay đổi xã hội, khoảng trống thị trường", "Quy trình 5 bước Tư duy thiết kế: Thấu cảm, Xác định, Lên ý tưởng, Mẫu thử, Kiểm thử", "Khảo sát nỗi đau khách hàng (Customer Pain Points)"]},
        {"chapter_num": 3, "chapter_title": "Thiết kế Mô hình kinh doanh: Business Model Canvas & Lean Canvas",
         "topics": ["9 khối cấu thành Mô hình kinh doanh Canvas (BMC)", "Lean Canvas dành cho doanh nghiệp khởi nghiệp giai đoạn sớm", "Xác lập Giá trị đề xuất độc nhất (Unique Value Proposition - UVP)"]},
        {"chapter_num": 4, "chapter_title": "Phương pháp Khởi nghiệp tinh gọn (The Lean Startup)",
         "topics": ["Vòng lặp phản hồi cốt lõi: Xây dựng - Đo lường - Học hỏi (Build - Measure - Learn)", "Phát triển Sản phẩm khả dụng tối thiểu (Minimum Viable Product - MVP)", "Các chỉ số phù hợp Sản phẩm - Thị trường (Product-Market Fit) và quyết định Chuyển hướng (Pivot)"]},
        {"chapter_num": 5, "chapter_title": "Hoạch định tài chính và Huy động vốn khởi nghiệp",
         "topics": ["Dự phóng dòng tiền, điểm hòa vốn và Burn Rate / Runway", "Các giai đoạn huy động vốn: Tự lực cánh sinh (Bootstrapping), Nhà đầu tư thiên thần (Angels), Vốn mạo hiểm (VC)", "Định giá doanh nghiệp khởi nghiệp và phân chia cổ phần (Cap Table)"]},
        {"chapter_num": 6, "chapter_title": "Xây dựng đội ngũ sáng lập, Sở hữu trí tuệ và Mở rộng quy mô",
         "topics": ["Thiết lập đội ngũ đồng sáng lập (Hacker, Hipster, Hustler) và thỏa thuận sáng lập", "Bảo hộ quyền sở hữu trí tuệ (Sáng chế, Nhãn hiệu, Bí mật kinh doanh)", "Chiến lược tăng trưởng thần tốc (Blitzscaling) và văn hóa đổi mới bền vững"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=4,
        chap_title="Phương pháp Khởi nghiệp tinh gọn (The Lean Startup)",
        introduction="Phương pháp Khởi nghiệp tinh gọn của Eric Ries cách mạng hóa quy trình sáng lập doanh nghiệp bằng cách thay thế kế hoạch kinh doanh tĩnh bằng các thử nghiệm khoa học, giảm thiểu lãng phí và tăng tốc đạt Product-Market Fit.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Vòng lặp Xây dựng - Đo lường - Học hỏi và Phát triển MVP",
                "content": "Trọng tâm của Lean Startup là biến các giả định kinh doanh mơ hồ thành các thử nghiệm có thể kiểm chứng được. Thay vì mất nhiều năm phát triển một sản phẩm hoàn thiện trong bí mật rồi nhận ra không ai cần, doanh nghiệp xây dựng Sản phẩm khả dụng tối thiểu (MVP).\n\nMVP chỉ chứa đựng tập tính năng vừa đủ để triển khai tới nhóm khách hàng tiên phong (Early Adopters), đo lường hành vi thực tế và thu nhận bài học đã được kiểm chứng (Validated Learning) nhanh nhất với chi phí thấp nhất.",
                "formulas": [
                    "Tốc độ vòng lặp tinh gọn: Thời gian hoàn tất chu trình (Ý tưởng -> Mã hóa -> Dữ liệu -> Bài học)",
                    "Công thức tính Runway tài chính: Runway (tháng) = Số dư tiền mặt hiện tại / Tỷ lệ đốt tiền hàng tháng (Net Burn Rate)",
                    "Định luật kiểm định Product-Market Fit của Sean Ellis: Khi >= 40% người dùng khảo sát nói rằng họ sẽ 'rất thất vọng' nếu sản phẩm biến mất"
                ],
                "case_studies": [
                    {"title": "Hành trình khởi nghiệp tinh gọn của nền tảng Batdongsan.com.vn", "detail": "Phân tích quá trình thử nghiệm MVP từ một trang tin rao vặt bất động sản đơn giản, liên tục chuyển hướng và phát triển thành cổng thông tin bất động sản lớn nhất Việt Nam."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Thực hiện hóa (Effectuation Theory - Saras Sarasvathy): Tư duy Khởi sự Kinh doanh Bất định dựa trên 5 Nguyên lý (Bird in Hand, Affordable Loss, Crazy Quilt, Lemonade, Pilot in the Plane).",
                "Lý thuyết Phá hủy Sáng tạo của Schumpeter (Schumpeterian Creative Destruction): Đổi mới Sáng tạo Căn bản (Radical Innovation) vs Đổi mới Từng bước (Incremental Innovation).",
                "Kinh tế học Thể chế về Hệ sinh thái Khởi nghiệp Đổi mới Sáng tạo Quốc gia (National Innovation Systems - NIS): Sự tương tác giữa Nhà nước, Viện trường và Doanh nghiệp (Triple Helix Model)."
            ]
        },
        review_questions=[
            "Phân tích sự khác nhau căn bản giữa Kế hoạch kinh doanh truyền thống và Phương pháp Khởi nghiệp tinh gọn (Lean Startup).",
            "Định nghĩa Sản phẩm khả dụng tối thiểu (MVP). Nêu các loại hình MVP phổ biến (Concierge MVP, Wizard of Oz MVP, Landing Page MVP).",
            "Khi nào một doanh nghiệp khởi nghiệp nên quyết định 'Chuyển hướng' (Pivot) thay vì tiếp tục kiên trì với mô hình hiện tại?"
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Khởi sự kinh doanh & Đổi mới sáng tạo - PGS.TS Trương Thị Nam Thắng (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Khởi sự kinh doanh & Đổi mới sáng tạo - PGS.TS Trương Thị Nam Thắng (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Khởi sự kinh doanh & Đổi mới sáng tạo", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_marketing_research():
    print("Building: Nghiên cứu Marketing...")
    builder = NEUTextbookBuilder(
        title="Nghiên cứu Marketing",
        subject_code="NCMK1101",
        faculty="Khoa Marketing",
        authors="PGS.TS. Nguyễn Viết Lâm & TS. Nguyễn Văn Thắng (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, CHUẨN HÓA PHƯƠNG PHÁP LUẬN QUỐC TẾ & PLS-SEM"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về Nghiên cứu Marketing và Thiết kế nghiên cứu",
         "topics": ["Bản chất, vai trò và quy trình 6 bước của nghiên cứu Marketing", "Xác định vấn đề quản trị và vấn đề nghiên cứu Marketing", "Phân loại thiết kế nghiên cứu: Khám phá, mô tả và nhân quả"]},
        {"chapter_num": 2, "chapter_title": "Phương pháp thu thập dữ liệu thứ cấp và Nghiên cứu định tính",
         "topics": ["Khai thác nguồn dữ liệu thứ cấp nội bộ và bên ngoài", "Phỏng vấn sâu cá nhân (In-depth Interviews)", "Thảo luận nhóm tập trung (Focus Group Discussions - FGD)", "Kỹ thuật chiếu xạ và phương pháp quan sát"]},
        {"chapter_num": 3, "chapter_title": "Phương pháp nghiên cứu định lượng và Thiết kế bảng câu hỏi",
         "topics": ["Các phương pháp khảo sát định lượng (Trực tiếp, điện thoại, trực tuyến)", "Kỹ thuật thiết kế bảng câu hỏi chuẩn hóa và tránh câu hỏi định kiến", "Kiểm định thử bảng câu hỏi (Pre-testing)"]},
        {"chapter_num": 4, "chapter_title": "Kỹ thuật thang đo và Phương pháp chọn mẫu nghiên cứu",
         "topics": ["4 cấp độ thang đo: Định danh (Nominal), Thứ bậc (Ordinal), Khoảng (Interval), Tỷ lệ (Ratio)", "Thang đo Likert và thang đối nghĩa ngữ nghĩa", "Phương pháp chọn mẫu xác suất và phi xác suất", "Xác định quy mô mẫu nghiên cứu tối ưu"]},
        {"chapter_num": 5, "chapter_title": "Xử lý dữ liệu, Phân tích thống kê và Kiểm định giả thuyết",
         "topics": ["Làm sạch và mã hóa dữ liệu", "Phân tích thống kê mô tả và kiểm định độ tin cậy Cronbach's Alpha", "Kiểm định so sánh trung bình: One-sample t-test, Independent t-test, ANOVA", "Phân tích tương quan Pearson và hồi quy tuyến tính bội"]},
        {"chapter_num": 6, "chapter_title": "Phân tích đa biến nâng cao và Báo cáo kết quả nghiên cứu",
         "topics": ["Phân tích nhân tố khám phá (Exploratory Factor Analysis - EFA)", "Mô hình phương trình cấu trúc (SEM)", "Phân tích cụm (Cluster Analysis) và bản đồ nhận thức", "Kỹ năng trình bày báo cáo nghiên cứu phục vụ ra quyết định kinh doanh"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=4,
        chap_title="Kỹ thuật thang đo và Phương pháp chọn mẫu nghiên cứu",
        introduction="Chất lượng của nghiên cứu Marketing phụ thuộc vào tính khoa học của thang đo lường và tính đại diện của mẫu khảo sát. Chương này trang bị lý thuyết thang đo, tiêu chuẩn đo lường và công thức xác định cỡ mẫu chuẩn mực.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Kỹ thuật Thang đo Likert và Tiêu chuẩn Độ tin cậy, Độ giá trị",
                "content": "Thang đo khoảng Likert (thường từ 5 hoặc 7 điểm) là công cụ phổ biến nhất để đo lường thái độ, nhận thức và ý định hành vi trong nghiên cứu Marketing.\n\nMột thang đo tốt phải đảm bảo hai tiêu chuẩn khoa học khắt khe: Độ tin cậy (Reliability - tính nhất quán nội tại qua hệ số Cronbach's Alpha >= 0.7) và Độ giá trị (Validity - tính chính xác đo đúng khái niệm cần đo, gồm độ giá trị hội tụ và độ giá trị phân biệt).",
                "formulas": [
                    "Hệ số tin cậy Cronbach's Alpha: alpha = [k / (k - 1)] * [1 - sum(sigma_i^2) / sigma_total^2]",
                    "Tiêu chuẩn chấp nhận Cronbach's Alpha: alpha >= 0.70; Hệ số tương quan biến - tổng (Corrected Item-Total Correlation) >= 0.30"
                ],
                "case_studies": [
                    {"title": "Chuẩn hóa thang đo chất lượng dịch vụ ngân hàng số (E-Banking)", "detail": "Ứng dụng mô hình SERVQUAL cải tiến đo lường 5 khía cạnh chất lượng dịch vụ ngân hàng số (Tin cậy, Đáp ứng, Năng lực phục vụ, Đồng cảm, Phương tiện hữu hình) tại thị trường Việt Nam."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Xác định Quy mô Mẫu Nghiên cứu Định lượng",
                "content": "Cỡ mẫu nghiên cứu phải đủ lớn để đảm bảo độ tin cậy thống kê nhưng phù hợp với giới hạn ngân sách và thời gian.\n\nĐối với ước lượng trung bình tổng thể, công thức Cochran được sử dụng với độ tin cậy 95% (Z = 1.96). Đối với phân tích nhân tố khám phá EFA, quy tắc kinh nghiệm của Hair et al. yêu cầu tỷ lệ cỡ mẫu tối thiểu là 5 quan sát cho 1 biến quan sát (tỷ lệ 5:1, lý tưởng là 10:1).",
                "formulas": [
                    "Công thức cỡ mẫu ước lượng tỷ lệ: n = [Z^2 * p * (1 - p)] / e^2 (Với Z = 1.96, p = 0.5, e = 0.05 -> n = 384)",
                    "Quy tắc cỡ mẫu phân tích EFA (Hair et al.): N >= 5 * k (k là tổng số biến quan sát)",
                    "Quy tắc cỡ mẫu hồi quy đa biến (Green 1991): N >= 50 + 8 * m (m là số biến độc lập)"
                ],
                "case_studies": [
                    {"title": "Thiết kế mẫu khảo sát người tiêu dùng chuỗi siêu thị WinMart", "detail": "Ứng dụng phương pháp chọn mẫu phân tầng kết hợp chọn mẫu cụm ngẫu nhiên tại 5 quận nội thành Hà Nội với cỡ mẫu 600 khách hàng."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Phương trình Cấu trúc Bình phương Nhỏ nhất Từng phần (PLS-SEM) theo Hair, Hult, Ringle & Sarstedt (2022): Đánh giá Mô hình Đo lường Kết quả (Reflective) và Nguyên nhân (Formative).",
                "Kiểm định Tính Bất biến của Thang đo (Measurement Invariance of Composite Models - MICOM) trong Nghiên cứu Đa Nhóm (Multi-Group Analysis - MGA).",
                "Kiểm soát Sai lệch Phương pháp Chung (Common Method Bias - CMB): Phương pháp Thử nghiệm Đơn nhân tố Harman và Kỹ thuật Biến Điểm đánh dấu (Marker Variable Technique)."
            ]
        },
        review_questions=[
            "Phân biệt 4 cấp độ thang đo: Định danh, Thứ bậc, Khoảng và Tỷ lệ. Cho ví dụ cụ thể về từng loại thang đo trong bảng câu hỏi nghiên cứu người tiêu dùng.",
            "Trình bày điều kiện để một biến quan sát được giữ lại trong thang đo khi đánh giá độ tin cậy Cronbach's Alpha và phân tích nhân tố khám phá EFA.",
            "Hãy tính cỡ mẫu tối thiểu cho một cuộc khảo sát thị trường có 35 biến quan sát phục vụ phân tích EFA và hồi quy đa biến với 5 biến độc lập."
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Nghiên cứu Marketing - PGS.TS Nguyễn Viết Lâm (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Nghiên cứu Marketing - PGS.TS Nguyễn Viết Lâm (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Nghiên cứu Marketing", "path": out_file, "pages": pages, "size_mb": size_mb}

if __name__ == "__main__":
    results = []
    results.append(build_principles_of_marketing())
    results.append(build_marketing_management())
    results.append(build_consumer_behavior())
    results.append(build_entrepreneurship())
    results.append(build_marketing_research())
    print("\n=== HOÀN THÀNH TẤT CẢ 5 HỌC PHẦN KHỐI MARKETING & ĐỔI MỚI SÁNG TẠO ===")
    for r in results:
        print(f"• {r['subject']}: {r['pages']} trang | {r['size_mb']:.2f} MB")
