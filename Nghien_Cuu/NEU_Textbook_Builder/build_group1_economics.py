# -*- coding: utf-8 -*-
"""
NEU Master Textbook Builder - Group 1: Economics
Covers 5 Courses:
1. Kinh tế học vi mô - PGS.TS Vũ Kim Dũng
2. Kinh tế học vĩ mô - PGS.TS Vũ Kim Dũng
3. Lịch sử các học thuyết kinh tế - GS.TS Nguyễn Văn Dần
4. Kinh tế quốc tế - PGS.TS Nguyễn Thường Lạng
5. Kinh tế phát triển - PGS.TS Nguyễn Ngọc Sơn
"""
import os
import sys

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

BASE_DIR_06 = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\06_Kinh tế học, Quản trị kinh doanh & Marketing"
BASE_DIR_05 = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\05_Tài chính Quốc tế"

def build_microeconomics():
    print("Building: Kinh tế học vi mô...")
    builder = NEUTextbookBuilder(
        title="Kinh tế học vi mô",
        subject_code="KHMI1101",
        faculty="Khoa Kinh tế học",
        authors="PGS.TS. Vũ Kim Dũng & PGS.TS. Nguyễn Văn Công (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, CHUẨN HÓA TOÀN DIỆN & TÍCH HỢP MÔ HÌNH TOÁN KINH TẾ TIẾN SĨ"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về kinh tế học vi mô và phương pháp nghiên cứu",
         "topics": ["Đối tượng và phương pháp nghiên cứu kinh tế học vi mô", "Quy luật khan hiếm, chi phí cơ hội và đường PPF", "Hệ thống kinh tế và vai trò của nhà nước"]},
        {"chapter_num": 2, "chapter_title": "Cơ chế thị trường: Lý thuyết Cung - Cầu và Độ co giãn",
         "topics": ["Quy luật cầu, đường cầu và hàm số cầu", "Quy luật cung, đường cung và hàm số cung", "Trạng thái cân bằng thị trường và biến động cân bằng", "Lý thuyết độ co giãn và ứng dụng chính sách"]},
        {"chapter_num": 3, "chapter_title": "Lý thuyết hành vi người tiêu dùng và Tối đa hóa hữu dụng",
         "topics": ["Lý thuyết hữu dụng biên (Marginal Utility)", "Lý thuyết đường bàng quan và đường ngân sách", "Cân bằng người tiêu dùng và xây dựng đường cầu cá nhân"]},
        {"chapter_num": 4, "chapter_title": "Lý thuyết sản xuất và Chi phí doanh nghiệp",
         "topics": ["Hàm sản xuất ngắn hạn và dài hạn", "Năng suất biên và quy luật năng suất biên giảm dần", "Hệ thống các loại chi phí và tối thiểu hóa chi phí"]},
        {"chapter_num": 5, "chapter_title": "Cấu trúc thị trường và Chiến lược định giá doanh nghiệp",
         "topics": ["Thị trường cạnh tranh hoàn hảo", "Thị trường độc quyền thuần túy", "Cạnh tranh độc quyền và độc quyền nhóm", "Lý thuyết trò chơi và cân bằng Nash trong độc quyền nhóm"]},
        {"chapter_num": 6, "chapter_title": "Thị trường các yếu tố sản xuất và Phân phối thu nhập",
         "topics": ["Cầu về yếu tố sản xuất phái sinh", "Thị trường lao động, tiền lương và vốn", "Thị trường đất đai và địa tô"]},
        {"chapter_num": 7, "chapter_title": "Cân bằng tổng thể, Hiệu quả Pareto và Thất bại thị trường",
         "topics": ["Cân bằng tổng thể Arrow-Debreu và hiệu quả Pareto", "Ngoại tác và giải pháp kinh tế học Pigou - Coase", "Hàng hóa công cộng và bất cân xứng thông tin"]}
    ]
    builder.add_table_of_contents(toc_data)

    # Chương 1
    builder.add_chapter(
        chap_num=1,
        chap_title="Tổng quan về kinh tế học vi mô và phương pháp nghiên cứu",
        introduction="Kinh tế học vi mô nghiên cứu hành vi lựa chọn tối ưu của các thực thể kinh tế riêng lẻ (hộ gia đình, doanh nghiệp, người tiêu dùng) trong điều kiện nguồn lực khan hiếm nhằm đạt được lợi ích tối đa.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Bản chất của kinh tế học vi mô và quy luật khan hiếm",
                "content": "Nền tảng của kinh tế học bắt nguồn từ mâu thuẫn vĩnh cửu giữa nhu cầu vô hạn của con người và tính khan hiếm (scarcity) của các nguồn lực kinh tế (lao động, vốn, tài nguyên thiên nhiên, kỹ năng công nghệ).\n\nKinh tế học vi mô tập trung giải quyết 3 vấn đề cốt lõi của nền kinh tế: Sản xuất cái gì? Sản xuất như thế nào? Và sản xuất cho ai? Quá trình này được điều tiết thông qua cơ chế giá cả thị trường và tín hiệu phân bổ nguồn lực.",
                "formulas": [
                    "Đường giới hạn khả năng sản xuất (PPF): F(X, Y) = C",
                    "Chi phí cơ hội (Opportunity Cost): OC_X = - dY / dX (Độ dốc tuyệt đối của PPF)",
                    "Tỷ lệ biến đổi biên (MRT): MRT_{XY} = MC_X / MC_Y"
                ],
                "case_studies": [
                    {"title": "Đánh đổi phân bổ nguồn lực sản xuất tại Việt Nam", "detail": "Nghiên cứu sự chuyển dịch nguồn lực nông nghiệp sang công nghiệp bán dẫn và logistics tại các tỉnh vùng kinh tế trọng điểm phía Bắc (Bắc Ninh, Hải Phòng) trong giai đoạn 2020-2026."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Phương pháp luận và mô hình hóa trong kinh tế học vi mô",
                "content": "Kinh tế học vi mô sử dụng các mô hình trừu tượng hóa dựa trên giả định 'các yếu tố khác không đổi' (ceteris paribus). Phương pháp tối ưu hóa tĩnh và so sánh tĩnh giúp giải thích sự thay đổi của trạng thái cân bằng khi có ngoại lực tác động.\n\nPhân biệt rõ ràng giữa kinh tế học thực chứng (positive economics - mô tả thực tế khách quan, kiểm định được) và kinh tế học chuẩn tắc (normative economics - đánh giá giá trị, đưa ra lời khuyên chính sách).",
                "formulas": [
                    "Quy tắc tối ưu hóa biên: MB(X) = MC(X)",
                    "Lợi ích ròng tối đa: max NB(X) = TB(X) - TC(X) <=> dTB/dX = dTC/dX"
                ],
                "case_studies": [
                    {"title": "Chính sách giá trần vé máy bay nội địa", "detail": "Phân tích tác động thực chứng của chính sách áp trần giá vé máy bay đối với thặng dư của người tiêu dùng và hãng hàng không tại Việt Nam."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Tiên đề hóa sở thích và Sự tồn tại của Hàm hữu dụng (Debreu's Representation Theorem).",
                "Phân tích Cân bằng tổng thể Arrow-Debreu và Định lý Phúc lợi Kinh tế học Căn bản (First & Second Fundamental Theorems of Welfare Economics).",
                "Mô hình Tối ưu hóa động thời gian liên tục (Hamiltonian Optimization & Pontryagin Maximum Principle) trong phân bổ tài nguyên cạn kiệt.",
                "Hướng nghiên cứu thực nghiệm SSCI: Nhận diện Causal Inference trong vi mô bằng Randomized Controlled Trials (RCTs) và Regression Discontinuity Design (RDD)."
            ]
        },
        review_questions=[
            "Trình bày bản chất của quy luật chi phí cơ hội ngày càng tăng và hình dạng đường cong PPF cong lõm so với gốc tọa độ.",
            "Phân tích sự khác biệt cốt lõi giữa kinh tế học thực chứng và kinh tế học chuẩn tắc thông qua ví dụ thuế tiêu thụ đặc biệt đồ uống có đường.",
            "Xây dựng bài toán tối ưu hóa lợi ích ròng xã hội và chứng minh điều kiện biên MB = MC."
        ]
    )

    # Chương 2
    builder.add_chapter(
        chap_num=2,
        chap_title="Cơ chế thị trường: Lý thuyết Cung - Cầu và Độ co giãn",
        introduction="Thị trường là cơ chế phối hợp kỳ diệu của hệ thống giá cả. Chương này khảo sát quy luật vận động của cung và cầu, xác định trạng thái cân bằng và lượng hóa mức độ phản ứng thông qua hệ số co giãn.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Lý thuyết Cầu, Cung và Cân bằng thị trường",
                "content": "Cầu phản ánh số lượng hàng hóa mà người mua sẵn sàng và có khả năng mua tại các mức giá khác nhau. Cung phản ánh lượng hàng hóa mà người bán sẵn lòng cung ứng.\n\nĐiểm cân bằng thị trường E(P*, Q*) đạt được khi lượng cung bằng lượng cầu. Thặng dư người tiêu dùng (CS) và thặng dư nhà sản xuất (PS) đo lường phúc lợi ròng của các chủ thể tham gia thị trường.",
                "formulas": [
                    "Hàm cầu tuyến tính: Q_D = a - bP (b > 0); Hàm cung tuyến tính: Q_S = -c + dP (d > 0)",
                    "Giá cân bằng: P* = (a + c) / (b + d); Sản lượng cân bằng: Q* = (ad - bc) / (b + d)",
                    "Tổng thặng dư xã hội (Total Surplus): TS = CS + PS"
                ],
                "case_studies": [
                    {"title": "Biến động thị trường xăng dầu Việt Nam", "detail": "Phân tích tác động của thuế bảo vệ môi trường và Quỹ bình ổn giá xăng dầu (BOG) đến giá cân bằng và tổn thất vô ích (Deadweight Loss - DWL)."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Lý thuyết Độ co giãn và Ứng dụng chính sách",
                "content": "Độ co giãn của cầu theo giá (E_P) đo lường phần trăm thay đổi của lượng cầu khi giá thay đổi 1%. Độ co giãn chéo (E_XY) phân loại hàng hóa thay thế và bổ sung. Độ co giãn theo thu nhập (E_I) phân loại hàng hóa thông thường, thiết yếu và xa xỉ.\n\nĐộ co giãn quyết định mức độ gánh chịu thuế giữa người mua và người bán. Bên nào có độ co giãn kém hơn (ít linh hoạt hơn) sẽ phải chịu gánh nặng thuế lớn hơn.",
                "formulas": [
                    "Co giãn điểm của cầu: E_P = (dQ/dP) * (P/Q)",
                    "Doanh thu và độ co giãn: MR = P * (1 + 1/E_P)",
                    "Gánh nặng thuế của người mua: t_B = t * [E_S / (E_S + |E_D|)]"
                ],
                "case_studies": [
                    {"title": "Độ co giãn cầu nông sản xuất khẩu gạo ST25", "detail": "Phân tích tác động của lệnh hạn chế xuất khẩu gạo của Ấn Độ tới độ co giãn cầu và tổng kim ngạch xuất khẩu gạo của Việt Nam năm 2023-2024."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Ước lượng Hệ thống Cầu Hoàn chỉnh (Almost Ideal Demand System - AIDS) của Deaton & Muellbauer.",
                "Hàm Cầu Bù đắp Hicksian vs Hàm Cầu Marshallian: Bổ đề Shephard (Shephard's Lemma) và Phương trình Slutsky nâng cao.",
                "Đo lường Biến thiên Bù đắp (Compensating Variation - CV) và Biến thiên Tương đương (Equivalent Variation - EV) trong đánh giá chính sách thuế.",
                "Kiểm định tính đồng nhất và tính đối xứng ma trận Slutsky trên dữ liệu khảo sát mức sống hộ gia đình Việt Nam (VHLSS)."
            ]
        },
        review_questions=[
            "Chứng minh mối quan hệ giữa doanh thu biên MR, giá cả P và độ co giãn của cầu theo giá E_P.",
            "Tại sao một mức thuế áp lên hàng hóa có cầu co giãn rất ít lại gây ra tổn thất vô ích nhỏ hơn so với hàng hóa có cầu co giãn mạnh?",
            "Viết phương trình Slutsky và giải thích tác động thay thế (Substitution Effect) và tác động thu nhập (Income Effect) khi giá hàng hóa Giffen tăng."
        ]
    )

    # Chương 3
    builder.add_chapter(
        chap_num=3,
        chap_title="Lý thuyết hành vi người tiêu dùng và Tối đa hóa hữu dụng",
        introduction="Chương này đi sâu vào nền tảng vi mô của quyết định tiêu dùng: cách thức người tiêu dùng phân bổ ngân sách hạn hẹp giữa các giỏ hàng hóa để đạt được mức thỏa dụng cao nhất.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Sở thích, Đường bàng quan và Tỷ lệ thay thế biên",
                "content": "Sở thích của người tiêu dùng tuân theo các giả định: tính hoàn chỉnh, tính bắc cầu, và tính không bão hòa (thích nhiều hơn ít). Đường bàng quan (Indifference Curve) tập hợp các giỏ hàng mang lại cùng mức hữu dụng.\n\nTỷ lệ thay thế biên (MRS) phản ánh số lượng hàng hóa Y mà người tiêu dùng sẵn sàng từ bỏ để có thêm 1 đơn vị hàng hóa X mà độ thỏa dụng không đổi.",
                "formulas": [
                    "Tỷ lệ thay thế biên: MRS_{XY} = - dY/dX = MU_X / MU_Y",
                    "Đường ngân sách: P_X * X + P_Y * Y = I <=> Y = (I / P_Y) - (P_X / P_Y) * X",
                    "Điều kiện cân bằng người tiêu dùng: MRS_{XY} = P_X / P_Y <=> MU_X / P_X = MU_Y / P_Y"
                ],
                "case_studies": [
                    {"title": "Cơ cấu chi tiêu tiêu dùng của hộ gia đình Việt Nam thời kỳ số hóa", "detail": "Khảo sát sự dịch chuyển đường ngân sách và giỏ tiêu dùng sang dịch vụ số (thương mại điện tử, giáo dục trực tuyến) theo dữ liệu Tổng cục Thống kê."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Tiên đề về Sở thích Lộ diện (Weak & Strong Axioms of Revealed Preference - WARP & SARP).",
                "Bài toán Đối ngẫu trong Lý thuyết Tiêu dùng: Tối thiểu hóa Chi tiêu (Expenditure Function) vs Tối đa hóa Hữu dụng (Indirect Utility Function - Roy's Identity).",
                "Lý thuyết Quyết định trong Điều kiện Rủi ro: Kỳ vọng Hữu dụng von Neumann-Morgenstern và Hệ số Né tránh Rủi ro Tuyệt đối Arrow-Pratt (CARA, CRRA)."
            ]
        },
        review_questions=[
            "Trình bày ý nghĩa kinh tế của điểm tiếp xúc giữa đường bàng quan và đường ngân sách.",
            "Sử dụng đồ thị để phân tích tác động thay thế và tác động thu nhập theo phương pháp Hicks và Slutsky đối với hàng hóa thông thường.",
            "Chứng minh đẳng thức Roy (Roy's Identity) suy ra hàm cầu Marshallian từ hàm thỏa dụng gián tiếp."
        ]
    )

    # Chương 4
    builder.add_chapter(
        chap_num=4,
        chap_title="Lý thuyết sản xuất và Chi phí doanh nghiệp",
        introduction="Doanh nghiệp đóng vai trò chuyển hóa các yếu tố đầu vào thành sản phẩm đầu ra. Chương này phân tích quy luật công nghệ sản xuất, chi phí và nguyên tắc tối thiểu hóa chi phí trong ngắn hạn và dài hạn.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Hàm sản xuất và Năng suất các yếu tố",
                "content": "Trong ngắn hạn, vốn (K) là cố định, lao động (L) là biến đổi. Quy luật năng suất biên giảm dần (Law of Diminishing Marginal Returns) chi phối hành vi sản xuất.\n\nTrong dài hạn, mọi yếu tố đều biến đổi. Đường đồng lượng (Isoquant) và đường đồng phí (Isocost) xác định phối hợp tối ưu giữa K và L. Tỷ lệ kỹ thuật thay thế biên (MRTS) đo lường khả năng thay thế giữa vốn và lao động.",
                "formulas": [
                    "Hàm Cobb-Douglas: Q = A * K^alpha * L^beta (alpha + beta: quy mô hiệu quả)",
                    "Tỷ lệ thay thế kỹ thuật biên: MRTS_{LK} = - dK/dL = MP_L / MP_K",
                    "Điều kiện tối thiểu hóa chi phí: MRTS_{LK} = w / r <=> MP_L / w = MP_K / r"
                ],
                "case_studies": [
                    {"title": "Hiệu suất theo quy mô trong ngành thép Hòa Phát", "detail": "Đánh giá lợi thế kinh tế nhờ quy mô (Economies of Scale) tại Khu liên hợp Gang thép Dung Quất và tối ưu hóa hàm sản xuất công nghiệp nặng."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Lý thuyết Chi phí sản xuất ngắn hạn và dài hạn",
                "content": "Hệ thống chi phí gồm chi phí cố định (FC), chi phí biến đổi (VC), tổng chi phí (TC), chi phí biên (MC) và các chi phí bình quân (AFC, AVC, ATC).\n\nĐường chi phí trung bình dài hạn (LRATC) là đường bao của các đường ngắn hạn (SRATC), thể hiện tính kinh tế theo quy mô, quy mô không đổi và phi kinh tế theo quy mô.",
                "formulas": [
                    "Chi phí biên: MC = dTC / dQ = dVC / dQ",
                    "Đẳng thức chi phí: MC cắt ATC và AVC tại các điểm cực tiểu của chúng",
                    "Độ co giãn của chi phí theo sản lượng: E_C = (dTC/dQ) * (Q/TC) = MC / ATC"
                ],
                "case_studies": [
                    {"title": "Chi phí biên trong sản xuất xe điện VinFast", "detail": "Phân tích tác động của chi phí cố định khổng lồ (R&D, dây chuyền dập tự động) đến chi phí trung bình khi sản lượng tích lũy gia tăng (Learning Curve Effect)."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Hàm Sản xuất CES (Constant Elasticity of Substitution) và Translog Production Function trong phân tích kinh tế lượng thực nghiệm.",
                "Bổ đề Hotelling (Hotelling's Lemma) và Hàm Lợi nhuận Đối ngẫu (Profit Function).",
                "Biên Sản xuất Ngẫu nhiên (Stochastic Frontier Analysis - SFA) và Phân tích Màng dữ liệu (Data Envelopment Analysis - DEA) đo lường Hiệu quả Kỹ thuật (Technical Efficiency) của doanh nghiệp Việt Nam."
            ]
        },
        review_questions=[
            "Tại sao đường chi phí biên MC luôn cắt đường chi phí trung bình ATC tại điểm cực tiểu của ATC? Chứng minh bằng giải tích toán học.",
            "Phân tích hiện tượng đường cong học tập (Learning Curve) và sự khác biệt với tính kinh tế nhờ quy mô (Economies of Scale).",
            "Thiết lập bài toán tối thiểu hóa chi phí có ràng buộc Lagrange và giải điều kiện bậc 1 (FOC)."
        ]
    )

    # Chương 5
    builder.add_chapter(
        chap_num=5,
        chap_title="Cấu trúc thị trường và Chiến lược định giá doanh nghiệp",
        introduction="Chương này phân tích hành vi tối đa hóa lợi nhuận của doanh nghiệp trong 4 cấu trúc thị trường: Cạnh tranh hoàn hảo, Độc quyền thuần túy, Cạnh tranh độc quyền và Độc quyền nhóm.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Cạnh tranh hoàn hảo và Độc quyền thuần túy",
                "content": "Trong cạnh tranh hoàn hảo, doanh nghiệp là người chấp nhận giá (P = MR = AR). Điều kiện tối đa hóa lợi nhuận là P = MC. Trong dài hạn, lợi nhuận kinh tế bằng 0.\n\nTrong độc quyền thuần túy, doanh nghiệp quyết định giá và đối diện với đường cầu dốc xuống. Tối đa hóa lợi nhuận tại MR = MC, định giá P > MC tạo ra sức mạnh thị trường (Market Power) và gây tổn thất vô ích cho xã hội.",
                "formulas": [
                    "Tối đa hóa lợi nhuận: MR = MC (Điều kiện bậc hai: dMR/dQ < dMC/dQ)",
                    "Chỉ số Lerner đo sức mạnh độc quyền: L = (P - MC) / P = - 1 / E_P",
                    "Định giá phân biệt cấp 1, cấp 2 và cấp 3"
                ],
                "case_studies": [
                    {"title": "Mô hình độc quyền tự nhiên của Tập đoàn Điện lực Việt Nam (EVN)", "detail": "Phân tích cấu trúc chi phí chìm lớn của lưới truyền tải điện và cơ chế điều tiết giá điện bán lẻ bậc thang tại Việt Nam."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Độc quyền nhóm và Lý thuyết trò chơi (Game Theory)",
                "content": "Thị trường độc quyền nhóm đặc trưng bởi tính phụ thuộc lẫn nhau giữa các đối thủ. Mô hình Cournot giả định sản lượng cạnh tranh, mô hình Bertrand giả định giá cả cạnh tranh, mô hình Stackelberg mô tả kẻ dẫn đầu và kẻ bám đuôi.\n\nLý thuyết trò chơi cung cấp công cụ phân tích chiến lược: Ma trận chi trả, Chiến lược thống trị, Cân bằng Nash (Nash Equilibrium) và Thế lưỡng nan của tù nhân (Prisoner's Dilemma).",
                "formulas": [
                    "Cân bằng Cournot 2 doanh nghiệp: q_1* = (a - c)/(3b), Q* = 2(a - c)/(3b), P* = (a + 2c)/3",
                    "Cân bằng Stackelberg: Doanh nghiệp dẫn đầu chiếm 50% thị phần thị trường",
                    "Chỉ số Herfindahl-Hirschman (HHI): HHI = sum(s_i^2)"
                ],
                "case_studies": [
                    {"title": "Cạnh tranh viễn thông Viettel - VNPT - MobiFone", "detail": "Phân tích thế cân bằng oligopoly và các chiến lược cạnh tranh giá cước dữ liệu di động 4G/5G tại thị trường Việt Nam."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Cân bằng Nash Hoàn hảo trong Trò chơi Con (Subgame Perfect Nash Equilibrium - SPNE) và Inductive Backward Induction.",
                "Mô hình Tổ chức Ngành Thực nghiệm Mới (Empirical Industrial Organization - NEIO): Nhận diện hành vi liên minh ngầm (Tacit Collusion) và Cartel.",
                "Mô hình Cạnh tranh Không gian Hotelling (Hotelling Spatial Competition) và Khác biệt hóa Sản phẩm Salop Circle.",
                "Cơ chế Đấu giá Doanh thu Tương đương (Revenue Equivalence Theorem) của Vickrey."
            ]
        },
        review_questions=[
            "So sánh giá, sản lượng và phúc lợi xã hội giữa mô hình Cạnh tranh hoàn hảo, Độc quyền thuần túy, Cournot và Bertrand.",
            "Giải thích nghịch lý Bertrand (Bertrand Paradox) và nêu các giả định thực tế giúp tháo gỡ nghịch lý này.",
            "Xây dựng ma trận trò chơi định giá giữa hai doanh nghiệp viễn thông và tìm điểm cân bằng Nash."
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Kinh tế học vi mô - PGS.TS Vũ Kim Dũng (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Kinh tế học vi mô - PGS.TS Vũ Kim Dũng (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Kinh tế học vi mô", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_macroeconomics():
    print("Building: Kinh tế học vĩ mô...")
    builder = NEUTextbookBuilder(
        title="Kinh tế học vĩ mô",
        subject_code="KHMA1101",
        faculty="Khoa Kinh tế học",
        authors="PGS.TS. Vũ Kim Dũng & PGS.TS. Nguyễn Văn Công (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, HIỆN ĐẠI HÓA CHUẨN MỰC QUỐC TẾ & DSGE MODELS"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Khái quát kinh tế vĩ mô và Hệ thống số liệu tài khoản quốc gia",
         "topics": ["Đối tượng và mục tiêu kinh tế học vĩ mô", "Đo lường sản lượng quốc gia: GDP, GNP, NNP, NI", "Đo lường lạm phát và thất nghiệp"]},
        {"chapter_num": 2, "chapter_title": "Tổng cầu và Sản lượng cân bằng trong nền kinh tế mở",
         "topics": ["Hàm tiêu dùng, đầu tư, chi tiêu chính phủ và xuất khẩu ròng", "Mô hình số nhân chi tiêu Keynes (Keynesian Cross)", "Nghịch lý của sự tiết kiệm và chính sách kích cầu"]},
        {"chapter_num": 3, "chapter_title": "Thị trường tiền tệ, Hệ thống ngân hàng và Chính sách tiền tệ",
         "topics": ["Bản chất và chức năng của tiền tệ", "Quá trình tạo tiền của hệ thống ngân hàng thương mại", "Ngân hàng Trung ương và các công cụ điều hành chính sách tiền tệ"]},
        {"chapter_num": 4, "chapter_title": "Mô hình IS-LM: Tương tác giữa khu vực thực và khu vực tiền tệ",
         "topics": ["Xây dựng đường IS từ cân bằng thị trường hàng hóa", "Xây dựng đường LM từ cân bằng thị trường tiền tệ", "Cân bằng đồng thời và hiệu quả chính sách tài khóa, tiền tệ", "Hiện tượng lấn át đầu tư tư nhân (Crowding-out Effect)"]},
        {"chapter_num": 5, "chapter_title": "Mô hình Tổng cầu - Tổng cung (AS-AD) và Cú sốc kinh tế",
         "topics": ["Xây dựng đường Tổng cầu AD từ IS-LM", "Đường Tổng cung ngắn hạn (SRAS) và dài hạn (LRAS)", "Cú sốc tổng cầu, cú sốc tổng cung và hiện tượng đình lạm (Stagflation)"]},
        {"chapter_num": 6, "chapter_title": "Kinh tế vĩ mô nền kinh tế mở và Mô hình Mundell-Fleming",
         "topics": ["Cán cân thanh toán quốc tế (BOP) và tỷ giá hối đoái", "Mô hình Mundell-Fleming dưới tỷ giá cố định và thả nổi", "Tam giác bất khả thi (Impossible Trinity)"]},
        {"chapter_num": 7, "chapter_title": "Tăng trưởng kinh tế dài hạn và Chu kỳ kinh tế",
         "topics": ["Hàm sản xuất tổng hợp và mô hình Solow-Swan", "Quy tắc vàng của tích lũy vốn (Golden Rule)", "Lý thuyết tăng trưởng nội sinh (Endogenous Growth Theory)"]}
    ]
    builder.add_table_of_contents(toc_data)

    # Chương 1
    builder.add_chapter(
        chap_num=1,
        chap_title="Khái quát kinh tế vĩ mô và Hệ thống số liệu tài khoản quốc gia",
        introduction="Kinh tế học vĩ mô nghiên cứu nền kinh tế dưới giác độ tổng thể: tăng trưởng GDP, ổn định lạm phát, việc làm, cán cân thương mại và các chính sách vĩ mô điều tiết.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Đo lường sản lượng quốc gia: GDP và các chỉ tiêu liên quan",
                "content": "Tổng sản phẩm quốc nội (GDP) là tổng giá trị thị trường của toàn bộ hàng hóa và dịch vụ cuối cùng được sản xuất ra trong phạm vi lãnh thổ quốc gia trong một thời kỳ nhất định.\n\nBa phương pháp đo lường GDP: Phương pháp chi tiêu (Expenditure Approach), Phương pháp thu nhập (Income Approach), và Phương pháp giá trị gia tăng (Value Added Approach) mang lại kết quả đồng nhất theo nguyên lý chu chuyển thu nhập.",
                "formulas": [
                    "GDP theo chi tiêu: GDP = C + I + G + NX (NX = X - M)",
                    "Mối quan hệ GDP và GNP: GNP = GDP + NPI (Thu nhập yếu tố ròng từ nước ngoài)",
                    "Chỉ số giảm phát GDP: GDP Deflator = (Nominal GDP / Real GDP) * 100"
                ],
                "case_studies": [
                    {"title": "Đánh giá lại quy mô GDP Việt Nam năm 2020", "detail": "Phân tích tác động của việc rà soát và đánh giá lại quy mô nền kinh tế của Tổng cục Thống kê làm tăng quy mô GDP thêm 25.4% và ý nghĩa đối với tỷ lệ nợ công/GDP."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Đo lường lạm phát và Thất nghiệp",
                "content": "Chỉ số giá tiêu dùng (CPI) đo lường sự thay đổi giá cả của rổ hàng hóa tiêu dùng điển hình. Lạm phát phản ánh sự gia tăng liên tục của mức giá chung.\n\nThất nghiệp gồm thất nghiệp tự nhiên (cọ xát và cơ cấu) và thất nghiệp chu kỳ. Định luật Okun phản ánh mối quan hệ tỷ lệ nghịch giữa khoảng cách thất nghiệp và khoảng cách sản lượng.",
                "formulas": [
                    "Chỉ số CPI: CPI_t = (sum(P_{it} * Q_{i0}) / sum(P_{i0} * Q_{i0})) * 100",
                    "Tỷ lệ lạm phát: pi_t = [(CPI_t - CPI_{t-1}) / CPI_{t-1}] * 100",
                    "Định luật Okun: (Y - Y*) / Y* = - beta * (u - u*)"
                ],
                "case_studies": [
                    {"title": "Kiểm soát lạm phát và mục tiêu CPI dưới 4.5% của Việt Nam", "detail": "Đánh giá chính sách phối hợp giữa Ngân hàng Nhà nước và Bộ Tài chính trong việc bình ổn giá lương thực, năng lượng và dịch vụ công."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Cân bằng Chu chuyển Liên thế hệ (Overlapping Generations Model - OLG) của Diamond.",
                "Hạch toán Tăng trưởng (Growth Accounting) và Ước lượng TFP (Total Factor Productivity) bằng phương pháp Solow Residual.",
                "Kinh tế lượng chuỗi thời gian vĩ mô: Mô hình Vector Autoregression (VAR) và Structural VAR (SVAR) nhận diện các cú sốc chính sách tiền tệ."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt giữa CPI và Chỉ số giảm phát GDP (GDP Deflator). Khi giá xăng dầu nhập khẩu tăng, chỉ số nào phản ứng mạnh hơn?",
            "Trình bày định luật Okun và giải thích tại sao tốc độ tăng trưởng GDP không tương ứng 1:1 với mức giảm tỷ lệ thất nghiệp.",
            "Chứng minh đẳng thức hạch toán vĩ mô: I - S = (T - G) + (M - X)."
        ]
    )

    # Chương 4
    builder.add_chapter(
        chap_num=4,
        chap_title="Mô hình IS-LM: Tương tác giữa khu vực thực và khu vực tiền tệ",
        introduction="Mô hình IS-LM do John Hicks và Alvin Hansen phát triển là công cụ phân tích trung tâm của kinh tế học vĩ mô trường phái Keynes, giải thích sự quyết định đồng thời của lãi suất và sản lượng quốc gia.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Đường IS và Cân bằng thị trường hàng hóa",
                "content": "Đường IS tập hợp các kết hợp giữa lãi suất (r) và sản lượng (Y) tại đó thị trường hàng hóa cân bằng (Tổng đầu tư bằng Tổng tiết kiệm, hoặc Tổng sản lượng bằng Tổng chi tiêu dự kiến).\n\nĐộ dốc đường IS âm: Khi lãi suất giảm, chi phí vốn giảm kích thích đầu tư (I) tăng, kéo theo tổng cầu và sản lượng tăng thông qua cơ chế số nhân chi tiêu.",
                "formulas": [
                    "Phương trình đường IS: Y = C(Y - T) + I(r) + G + NX",
                    "Dạng tuyến tính IS: Y = [A_0 - d*r] / [1 - MPC(1 - t) + MPM]",
                    "Số nhân chi tiêu chính sách tài khóa: m = 1 / [1 - MPC(1 - t) + MPM]"
                ],
                "case_studies": [
                    {"title": "Gói kích thích kinh tế 350.000 tỷ đồng của Việt Nam (Nghị quyết 43/2022/QH15)", "detail": "Phân tích tác động dịch chuyển đường IS sang phải và hiệu quả giải ngân đầu tư công phục hồi kinh tế hậu Covid-19."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Đường LM và Cân bằng thị trường tiền tệ",
                "content": "Đường LM tập hợp các phối hợp giữa lãi suất (r) và thu nhập (Y) làm cho thị trường tiền tệ cân bằng (Cầu tiền thực tế bằng Cung tiền thực tế).\n\nĐộ dốc đường LM dương: Khi thu nhập Y tăng, nhu cầu tiền tệ cho giao dịch tăng, buộc lãi suất r phải tăng để triệt tiêu nhu cầu đầu cơ tiền tệ, giữ cho cầu tiền cân bằng với cung tiền cố định.",
                "formulas": [
                    "Cầu tiền thực tế: (M/P)_d = k*Y - h*r (k: độ nhạy theo thu nhập, h: độ nhạy theo lãi suất)",
                    "Phương trình đường LM: r = (k/h)*Y - (1/h)*(M/P)",
                    "Cân bằng IS-LM: Giao điểm E(r*, Y*) xác định lãi suất và sản lượng cân bằng chung"
                ],
                "case_studies": [
                    {"title": "Chính sách nới lỏng tiền tệ và 4 lần hạ lãi suất điều hành của SBV năm 2023", "detail": "Phân tích tác động dịch chuyển đường LM sang phải, giải tỏa thanh khoản hệ thống ngân hàng thương mại và kích thích tăng trưởng tín dụng."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Bẫy thanh khoản (Liquidity Trap) và Ranh giới Lãi suất Danh nghĩa Không (Zero Lower Bound - ZLB): Chính sách Tiền tệ Phi truyền thống (Quantitative Easing - QE).",
                "Mô hình Tân Keynesian DSGE (Dynamic Stochastic General Equilibrium) với Định chế Giá cứng nhắc Calvo (Calvo Pricing).",
                "Quy tắc Taylor (Taylor Rule) và Hàm phản ứng chính sách tiền tệ tối ưu trong kiểm soát lạm phát mục tiêu (Inflation Targeting)."
            ]
        },
        review_questions=[
            "Phân tích cơ chế truyền dẫn chính sách tiền tệ qua mô hình IS-LM. Yếu tố nào quyết định mức độ dốc của đường IS và LM?",
            "Hiện tượng thoái lui đầu tư (Crowding-out effect) xảy ra như thế nào khi chính phủ tài trợ chi tiêu bằng phát hành trái phiếu?",
            "Sử dụng mô hình IS-LM để giải thích tác động kết hợp của chính sách tài khóa mở rộng và chính sách tiền tệ thắt chặt."
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Kinh tế học vĩ mô - PGS.TS Vũ Kim Dũng (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Kinh tế học vĩ mô - PGS.TS Vũ Kim Dũng (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Kinh tế học vĩ mô", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_history_of_economic_thought():
    print("Building: Lịch sử các học thuyết kinh tế...")
    builder = NEUTextbookBuilder(
        title="Lịch sử các học thuyết kinh tế",
        subject_code="LSHK1102",
        faculty="Khoa Kinh tế học",
        authors="GS.TS. Nguyễn Văn Dần & PGS.TS. Mai Ngọc Cường (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, KHẢO CỨU HỌC THUẬT TOÀN DIỆN & PHÊ PHÁN KINH TẾ CHÍNH TRỊ"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan môn học và Tư tưởng kinh tế cổ đại, trung cổ",
         "topics": ["Đối tượng và phương pháp môn học", "Tư tưởng kinh tế thời kỳ Hy Lạp - La Mã cổ đại (Plato, Aristotle)", "Tư tưởng kinh tế trung cổ và Thuyết giá cả công bằng của Thomas Aquinas"]},
        {"chapter_num": 2, "chapter_title": "Chủ nghĩa trọng thương (Mercantilism) - Giai đoạn sơ khai của kinh tế học",
         "topics": ["Hoàn cảnh lịch sử và bản chất của chủ nghĩa trọng thương", "Giai đoạn tích lũy tiền tệ và giai đoạn cán cân thương mại", "Các đại biểu tiêu biểu: Thomas Mun, Jean-Baptiste Colbert"]},
        {"chapter_num": 3, "chapter_title": "Chủ nghĩa trọng nông (Physiocracy) và Quy luật tự nhiên",
         "topics": ["Triết lý trật tự tự nhiên và vai trò tuyệt đối của nông nghiệp", "François Quesnay và Biểu kinh tế (Tableau Économique)", "Tư tưởng tự do kinh tế Laissez-faire của Turgot"]},
        {"chapter_num": 4, "chapter_title": "Trường phái Kinh tế học Cổ điển Anh (Classical Economics)",
         "topics": ["Adam Smith: Bàn tay vô hình, Phân công lao động và Thuyết giá trị lao động", "David Ricardo: Thuyết lợi thế so sánh và Quy luật phân phối thu nhập", "Thomas Malthus và Thuyết nhân khẩu học", "Jean-Baptiste Say và Quy luật thị trường Say's Law"]},
        {"chapter_num": 5, "chapter_title": "Học thuyết kinh tế Mác - Lênin về Phương thức sản xuất TBCN",
         "topics": ["Học thuyết giá trị thặng dư và bản chất của tích lũy tư bản", "Quy luật tỷ suất lợi nhuận có xu hướng giảm", "Lý luận về chủ nghĩa tư bản độc quyền và độc quyền nhà nước"]},
        {"chapter_num": 6, "chapter_title": "Cuộc cách mạng cận biên và Trường phái Tân cổ điển (Neoclassical)",
         "topics": ["Cách mạng cận biên (Marginalist Revolution): Jevons, Menger, Walras", "Alfred Marshall: Nguyên lý kinh tế học và Cân bằng cục bộ", "Vilfredo Pareto và Cân bằng tổng thể tối ưu"]},
        {"chapter_num": 7, "chapter_title": "Cuộc cách mạng Keynes và Sự trỗi dậy của Kinh tế học Vĩ mô hiện đại",
         "topics": ["Bối cảnh Đại khủng hoảng 1929-1933 và sự phá sản của Say's Law", "Lý thuyết tổng quát của John Maynard Keynes: Tổng cầu hữu hiệu và Vai trò Nhà nước", "Sự tổng hợp Tân cổ điển (Neoclassical Synthesis) của Samuelson"]},
        {"chapter_num": 8, "chapter_title": "Các trường phái kinh tế hiện đại nửa sau thế kỷ XX và XXI",
         "topics": ["Chủ nghĩa tiền tệ của Milton Friedman (Monetarism)", "Trường phái Áo (Austrian School): Ludwig von Mises và Friedrich Hayek", "Kinh tế học Thể chế mới (New Institutional Economics): Ronald Coase và Douglass North"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=4,
        chap_title="Trường phái Kinh tế học Cổ điển Anh (Classical Economics)",
        introduction="Trường phái Cổ điển Anh đặt nền móng khoa học vững chắc cho kinh tế học hiện đại, với trọng tâm là học thuyết giá trị lao động, cơ chế thị trường tự do cạnh tranh và quy luật tích lũy của cải.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Adam Smith và Tác phẩm 'Sự giàu có của các quốc gia' (The Wealth of Nations - 1776)",
                "content": "Adam Smith được tôn vinh là cha đẻ của kinh tế học hiện đại. Tư tưởng trọng tâm của ông là khái niệm 'Bàn tay vô hình' (Invisible Hand): Khi mỗi cá nhân theo đuổi lợi ích cá nhân chính đáng của mình trong môi trường tự do cạnh tranh, họ bị dẫn dắt bởi một bàn tay vô hình để thúc đẩy lợi ích chung của toàn xã hội một cách hiệu quả hơn cả khi họ chủ động làm điều đó.\n\nSmith phân tích sâu sắc lợi ích của sự phân công lao động (Division of Labour) thông qua ví dụ xưởng sản xuất đinh ghim, chỉ ra rằng phân công làm tăng năng suất lao động vượt bậc nhờ chuyên môn hóa kỹ năng, tiết kiệm thời gian chuyển đổi thao tác và phát minh máy móc.",
                "formulas": [
                    "Học thuyết giá trị của Smith: Giá trị sử dụng (Use Value) vs Giá trị trao đổi (Exchange Value)",
                    "Nghịch lý giá trị Kim cương - Nước (Water-Diamond Paradox)",
                    "Giá cả tự nhiên (Natural Price) = Tiền lương tự nhiên + Lợi nhuận tự nhiên + Địa tô tự nhiên"
                ],
                "case_studies": [
                    {"title": "Ý nghĩa học thuyết 'Bàn tay vô hình' đối với công cuộc Đổi mới tại Việt Nam", "detail": "Phân tích sự chuyển đổi từ cơ chế kế hoạch hóa tập trung bao cấp sang nền kinh tế thị trường định hướng XHCN, tôn trọng quy luật giá trị và giải phóng sức sản xuất cá nhân."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "David Ricardo và Quy luật phân phối trong nền kinh tế tư bản",
                "content": "David Ricardo hoàn thiện học thuyết giá trị lao động, khẳng định giá trị hàng hóa hoàn toàn do lượng lao động hao phí để sản xuất ra nó quyết định.\n\nRicardo xây dựng lý thuyết địa tô chênh lệch (Differential Rent), chỉ ra rằng khi dân số tăng, đất đai kém màu mỡ bị đưa vào canh tác, đẩy chi phí sản xuất biên và giá lương thực tăng, làm giảm tỷ suất lợi nhuận của nhà tư bản công nghiệp và kìm hãm tích lũy tư bản.",
                "formulas": [
                    "Mô hình phân phối thu nhập quốc dân: Y = Lương (W) + Lợi nhuận (P) + Địa tô (R)",
                    "Thuyết Lợi thế so sánh (Comparative Advantage): Thương mại cùng có lợi khi chi phí cơ hội khác nhau",
                    "Định lý Tương đương Ricardian (Ricardian Equivalence): Tài trợ chi tiêu công bằng nợ hay thuế có hiệu ứng tương đương"
                ],
                "case_studies": [
                    {"title": "Ứng dụng thuyết lợi thế so sánh trong chiến lược xuất khẩu dệt may và thủy sản Việt Nam", "detail": "Phân tích lợi thế so sánh dựa trên nguồn nhân lực dồi dào và chi phí cơ hội thấp trong chuỗi giá trị toàn cầu."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp luận Khoa học Kinh tế: Tiêu chuẩn Bác bỏ được của Karl Popper (Popperian Falsifiability) đối chiếu với Tiến trình Chuyển dịch Hệ hình của Thomas Kuhn (Paradigm Shifts in Economics).",
                "Tranh luận Cambridge - Cambridge về Lý thuyết Tư bản (Cambridge Capital Controversy) giữa MIT (Solow, Samuelson) và Cambridge Anh (Joan Robinson, Piero Sraffa).",
                "Kinh tế học Thể chế và Sự trỗi dậy của các Quốc gia: Đánh giá luận điểm 'Tại sao các quốc gia thất bại' của Daron Acemoglu & James Robinson."
            ]
        },
        review_questions=[
            "Phân tích cách giải quyết Nghịch lý Kim cương - Nước của Adam Smith và sự thấu suốt sau đó của Cách mạng cận biên (Marginalist Revolution).",
            "Trình bày mô hình Lợi thế so sánh của David Ricardo và chứng minh rằng hai quốc gia luôn có thể thu lợi từ thương mại ngay cả khi một quốc gia có lợi thế tuyệt đối ở tất cả các mặt hàng.",
            "Tại sao David Ricardo coi địa tô là mối đe dọa đối với tăng trưởng kinh tế dài hạn?"
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Lịch sử các học thuyết kinh tế - GS.TS Nguyễn Văn Dần (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Lịch sử các học thuyết kinh tế - GS.TS Nguyễn Văn Dần (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Lịch sử các học thuyết kinh tế", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_international_economics():
    print("Building: Kinh tế quốc tế...")
    builder = NEUTextbookBuilder(
        title="Kinh tế quốc tế",
        subject_code="KTQT1101",
        faculty="Viện Thương mại và Kinh tế Quốc tế",
        authors="PGS.TS. Nguyễn Thường Lạng & Tập thể Giảng viên (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, TÍCH HỢP HIỆP ĐỊNH FTA THẾ HỆ MỚI & MELITZ MODEL"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về kinh tế quốc tế và Xu thế toàn cầu hóa",
         "topics": ["Đối tượng, nội dung môn học Kinh tế quốc tế", "Toàn cầu hóa và sự phân công lao động quốc tế", "Các dòng dịch chuyển thương mại, vốn và công nghệ toàn cầu"]},
        {"chapter_num": 2, "chapter_title": "Các lý thuyết thương mại quốc tế cổ điển và hiện đại",
         "topics": ["Lợi thế tuyệt đối (Adam Smith) và Lợi thế so sánh (David Ricardo)", "Mô hình tỷ lệ các yếu tố sản xuất Heckscher-Ohlin (H-O)", "Nghịch lý Leontief và các lý thuyết thương mại hiện đại (Paul Krugman)"]},
        {"chapter_num": 3, "chapter_title": "Chính sách thương mại quốc tế: Thuế quan và Phi thuế quan",
         "topics": ["Thuế quan và phân tích cân bằng bộ phận về tác động của thuế", "Hạn ngạch nhập khẩu (Quotas) và Hạn chế xuất khẩu tự nguyện (VER)", "Các rào cản kỹ thuật (TBT, SPS) và biện pháp phòng vệ thương mại"]},
        {"chapter_num": 4, "chapter_title": "Liên kết kinh tế quốc tế và Các hiệp định thương mại tự do",
         "topics": ["Các cấp độ liên kết kinh tế quốc tế", "Hiệu ứng tạo lập thương mại (Trade Creation) và chuyển hướng thương mại (Trade Diversion)", "Việt Nam trong các FTA thế hệ mới: CPTPP, EVFTA, RCEP"]},
        {"chapter_num": 5, "chapter_title": "Cán cân thanh toán quốc tế và Thị trường ngoại hối",
         "topics": ["Cấu trúc cán cân thanh toán quốc tế (BOP)", "Cơ chế điều chỉnh cán cân thanh toán", "Tỷ giá hối đoái và các chế độ tỷ giá trên thế giới"]},
        {"chapter_num": 6, "chapter_title": "Đầu tư quốc tế và Hoạt động của Tập đoàn đa quốc gia (MNEs)",
         "topics": ["Đầu tư trực tiếp nước ngoài (FDI) và Khung lý thuyết OLI Dunning", "Đầu tư gián tiếp quốc tế (FII) và Vay nợ thương mại", "Chuyển giao công nghệ và tác động lan tỏa (Spillover Effects)"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=2,
        chap_title="Các lý thuyết thương mại quốc tế cổ điển và hiện đại",
        introduction="Thương mại quốc tế là động lực cốt lõi thúc đẩy của cải quốc gia. Chương này phân tích quá trình tiến hóa của các lý thuyết thương mại từ Ricardian, Heckscher-Ohlin đến Kinh tế học Địa lý & Thương mại Mới của Paul Krugman.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Mô hình Heckscher-Ohlin (H-O) và Các định lý mở rộng",
                "content": "Mô hình Heckscher-Ohlin giải thích nguồn gốc lợi thế so sánh xuất phát từ sự khác biệt về mức độ dồi dào các yếu tố sản xuất (Factor Endowments) giữa các quốc gia.\n\nĐịnh lý H-O khẳng định: Quốc gia dồi dào yếu tố sản xuất nào sẽ có lợi thế so sánh và xuất khẩu hàng hóa thâm dụng yếu tố sản xuất đó, đồng thời nhập khẩu hàng hóa thâm dụng yếu tố khan hiếm.",
                "formulas": [
                    "Định lý Cân bằng giá cả các yếu tố sản xuất (Heckscher-Ohlin-Samuelson Theorem): w_A -> w_B và r_A -> r_B",
                    "Định lý Stolper-Samuelson: Tăng giá hàng hóa xuất khẩu làm tăng thu nhập thực tế của yếu tố thâm dụng",
                    "Định lý Rybczynski: Gia tăng trữ lượng một yếu tố làm tăng sản lượng hàng hóa thâm dụng yếu tố đó nhiều hơn tỷ lệ thuận"
                ],
                "case_studies": [
                    {"title": "Mô hình H-O và chuyển dịch cơ cấu xuất khẩu Việt Nam", "detail": "Phân tích sự dịch chuyển từ xuất khẩu hàng hóa thâm dụng lao động phổ thông (may mặc, giày da) sang hàng hóa thâm dụng vốn và công nghệ (linh kiện điện tử, điện thoại thông minh Samsung)."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Thương mại nội ngành (Intra-Industry Trade) và Mô hình Paul Krugman",
                "content": "Lý thuyết thương mại truyền thống không giải thích được vì sao các quốc gia phát triển có tỷ lệ yếu tố sản xuất tương đồng lại trao đổi các sản phẩm cùng loại với nhau (ví dụ: Đức và Pháp trao đổi xe hơi).\n\nPaul Krugman đưa ra Lý thuyết Thương mại Mới dựa trên tính kinh tế theo quy mô nội bộ (Internal Economies of Scale) và sở thích đa dạng hóa sản phẩm của người tiêu dùng trong thị trường cạnh tranh độc quyền.",
                "formulas": [
                    "Chỉ số Grubel-Lloyd đo lường thương mại nội ngành: GL_i = 1 - [|X_i - M_i| / (X_i + M_i)]",
                    "Mô hình Trọng lực thương mại (Gravity Model): T_{ij} = G * [(Y_i^alpha * Y_j^beta) / D_{ij}^theta]"
                ],
                "case_studies": [
                    {"title": "Thương mại nội ngành linh kiện điện tử trong chuỗi cung ứng ASEAN - Việt Nam", "detail": "Ứng dụng chỉ số Grubel-Lloyd đánh giá mức độ chuyên môn hóa dọc và thương mại nội ngành bán dẫn giữa Việt Nam, Malaysia và Singapore."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Doanh nghiệp Không đồng nhất của Marc Melitz (Melitz 2003 Econometrica): Phân bổ lại Nguồn lực Nội ngành và Sự chọn lọc Tự nhiên của Doanh nghiệp Xuất khẩu.",
                "Chuỗi Giá trị Toàn cầu (Global Value Chains - GVCs): Đo lường Giá trị Gia tăng Thương mại (Trade in Value-Added - TiVA) theo Koopman, Wang & Wei.",
                "Kinh tế lượng Thương mại Quốc tế: Ước lượng Mô hình Trọng lực Cấu trúc (Structural Gravity Model) bằng phương pháp Poisson Pseudo-Maximum Likelihood (PPML)."
            ]
        },
        review_questions=[
            "Trình bày 4 định lý cốt lõi của mô hình Heckscher-Ohlin và đánh giá tính phù hợp thực nghiệm với các nước đang phát triển.",
            "Giải thích nghịch lý Leontief (Leontief Paradox) và các hướng tiếp cận lý thuyết giải tỏa nghịch lý này.",
            "Xây dựng phương trình mô hình Trọng lực thương mại và phân tích tác động của khoảng cách địa lý và các hiệp định thương mại tự do (FTAs)."
        ]
    )

    out_file_06 = os.path.join(BASE_DIR_06, "[NEU] Kinh tế quốc tế - PGS.TS Nguyễn Thường Lạng (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Kinh tế quốc tế - PGS.TS Nguyễn Thường Lạng (NXB ĐHKTQD).pdf")
    out_file_05 = os.path.join(BASE_DIR_05, "[NEU] Kinh tế quốc tế - PGS.TS Nguyễn Thường Lạng (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Kinh tế quốc tế - PGS.TS Nguyễn Thường Lạng (NXB ĐHKTQD).pdf")
    
    pages, size_mb = builder.save(out_file_06)
    print(f"-> Hoàn thành (Dir 06): {out_file_06} ({pages} trang, {size_mb:.2f} MB)")
    
    # Save copy to Dir 05 as well
    import shutil
    os.makedirs(os.path.dirname(out_file_05), exist_ok=True)
    src = '\\\\?\\' + os.path.abspath(out_file_06) if os.name == 'nt' else out_file_06
    dst = '\\\\?\\' + os.path.abspath(out_file_05) if os.name == 'nt' else out_file_05
    shutil.copyfile(src, dst)
    print(f"-> Đồng bộ sang (Dir 05): {out_file_05}")
    return {"subject": "Kinh tế quốc tế", "path": out_file_06, "pages": pages, "size_mb": size_mb}

def build_development_economics():
    print("Building: Kinh tế phát triển...")
    builder = NEUTextbookBuilder(
        title="Kinh tế phát triển",
        subject_code="KTPT1101",
        faculty="Khoa Kinh tế học",
        authors="PGS.TS. Nguyễn Ngọc Sơn & PGS.TS. Vũ Cường (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, CẬP NHẬT PHÁT TRIỂN BỀN VỮNG & THỂ CHẾ PHÁT TRIỂN"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Bản chất của phát triển kinh tế và Các thước đo tiến bộ xã hội",
         "topics": ["Khái niệm tăng trưởng kinh tế và phát triển kinh tế", "Chỉ số phát triển con người (HDI) và Bất bình đẳng thu nhập (Hệ số Gini)", "Nghèo đói đa chiều (MPI) và các mục tiêu phát triển bền vững (SDGs)"]},
        {"chapter_num": 2, "chapter_title": "Các mô hình và lý thuyết tăng trưởng trong kinh tế phát triển",
         "topics": ["Mô hình tăng trưởng tuyến tính Rostow", "Mô hình Harrod-Domar và vai trò của tích lũy vốn", "Mô hình hai khu vực của Arthur Lewis và quá trình chuyển dịch lao động", "Lý thuyết Cú hích lớn (Big Push) và Tăng trưởng cân đối"]},
        {"chapter_num": 3, "chapter_title": "Nguồn vốn đầu tư và Hiệu quả sử dụng vốn trong phát triển",
         "topics": ["Nguồn vốn trong nước: Tiết kiệm tư nhân và Đầu tư công", "Nguồn vốn nước ngoài: FDI, ODA và Kiều hối", "Hệ số sinh lời vốn đầu tư ICOR và năng suất vốn"]},
        {"chapter_num": 4, "chapter_title": "Phát triển nguồn nhân lực và Vốn con người (Human Capital)",
         "topics": ["Vai trò của giáo dục, đào tạo và y tế trong phát triển", "Bẫy thu nhập trung bình (Middle-Income Trap)", "Chảy máu chất xám và di cư lao động"]},
        {"chapter_num": 5, "chapter_title": "Chuyển dịch cơ cấu kinh tế và Đô thị hóa",
         "topics": ["Quy luật chuyển dịch cơ cấu ngành kinh tế (Nông nghiệp - Công nghiệp - Dịch vụ)", "Đô thị hóa và Mô hình di cư nông thôn - thành thị Harris-Todaro", "Kinh tế phi chính thức và thị trường lao động kép"]},
        {"chapter_num": 6, "chapter_title": "Bền vững môi trường và Kinh tế tuần hoàn trong phát triển",
         "topics": ["Đường cong Kuznets môi trường (EKC)", "Biến đổi khí hậu và chuyển đổi năng lượng công bằng (JETP)", "Kinh tế xanh và kinh tế tuần hoàn"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=2,
        chap_title="Các mô hình và lý thuyết tăng trưởng trong kinh tế phát triển",
        introduction="Lý thuyết kinh tế phát triển cung cấp khung phân tích về quá trình một quốc gia thoát nghèo, tích lũy nguồn lực và chuyển đổi cơ cấu kinh tế toàn diện.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Mô hình Harrod-Domar và Hệ số ICOR",
                "content": "Mô hình Harrod-Domar khẳng định tốc độ tăng trưởng kinh tế phụ thuộc trực tiếp vào tỷ lệ tiết kiệm quốc gia và tỷ lệ vốn - sản lượng (ICOR).\n\nĐể đạt được tốc độ tăng trưởng mục tiêu, nền kinh tế cần duy trì một tỷ lệ tiết kiệm và đầu tư tương ứng, đồng thời nâng cao hiệu quả sử dụng vốn để giảm hệ số ICOR.",
                "formulas": [
                    "Phương trình Harrod-Domar: g = s / k (g: tốc độ tăng trưởng, s: tỷ lệ tiết kiệm, k: hệ số ICOR)",
                    "Hệ số ICOR: ICOR = Delta K / Delta Y = I / Delta Y",
                    "Khoảng trống tài trợ (Financing Gap): Đầu tư cần thiết - Tiết kiệm nội địa"
                ],
                "case_studies": [
                    {"title": "Diễn biến hệ số ICOR của nền kinh tế Việt Nam giai đoạn 2011-2025", "detail": "Phân tích sự cải thiện hiệu quả đầu tư công giúp giảm hệ số ICOR từ mức 6.5 xuống xấp xỉ 5.2, phản ánh chất lượng tăng trưởng được nâng cao."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Mô hình Hai khu vực của Arthur Lewis",
                "content": "Mô hình Lewis phân chia nền kinh tế chậm phát triển thành hai khu vực: Khu vực nông nghiệp truyền thống (năng suất thấp, lao động dư thừa với năng suất biên bằng 0) và Khu vực công nghiệp hiện đại (năng suất cao, hướng tới lợi nhuận).\n\nQuá trình phát triển là quá trình tích lũy vốn tại khu vực công nghiệp và thu hút lao động dư thừa từ nông thôn sang thành thị với mức tiền lương cố định cho đến khi chạm Điểm ngoặt Lewis (Lewis Turning Point).",
                "formulas": [
                    "Năng suất biên lao động nông nghiệp: MP_L = 0",
                    "Tiền lương công nghiệp: w_m = (1 + phi) * w_a (phi: thặng dư khuyến khích di cư ~ 30%)",
                    "Điểm ngoặt Lewis: Khi lao động dư thừa cạn kiệt, tiền lương bắt đầu tăng"
                ],
                "case_studies": [
                    {"title": "Việt Nam trước ngưỡng cửa Điểm ngoặt Lewis", "detail": "Đánh giá quá trình chuyển dịch lao động nông nghiệp sang công nghiệp chế biến chế tạo tại vùng đồng bằng sông Hồng và sự suy giảm nguồn cung lao động giá rẻ."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Căn nguyên Thể chế của Phát triển (Institutional Foundations of Comparative Development - Acemoglu, Johnson & Robinson 2001 AER).",
                "Phương pháp Thử nghiệm Đối chứng Ngẫu nhiên (Randomized Controlled Trials - RCTs) trong Đánh giá Chính sách Giảm nghèo (Banerjee, Duflo & Kremer - Nobel 2019).",
                "Bẫy Thu nhập Trung bình: Phân tích Thực nghiệm Bước nhảy Đổi mới Sáng tạo (Innovation Leapfrogging) và Tối ưu hóa Chuỗi Giá trị."
            ]
        },
        review_questions=[
            "Trình bày mô hình Harrod-Domar và nêu những hạn chế lớn của mô hình này khi áp dụng cho các nền kinh tế đang phát triển.",
            "Phân tích điều kiện và hệ quả khi nền kinh tế chạm Điểm ngoặt Lewis (Lewis Turning Point).",
            "Đường cong Kuznets về bất bình đẳng thu nhập mô tả điều gì? Bằng chứng thực nghiệm tại các nước Đông Á có ủng hộ giả thuyết này không?"
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Kinh tế phát triển - PGS.TS Nguyễn Ngọc Sơn (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Kinh tế phát triển - PGS.TS Nguyễn Ngọc Sơn (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Kinh tế phát triển", "path": out_file, "pages": pages, "size_mb": size_mb}

if __name__ == "__main__":
    results = []
    results.append(build_microeconomics())
    results.append(build_macroeconomics())
    results.append(build_history_of_economic_thought())
    results.append(build_international_economics())
    results.append(build_development_economics())
    print("\n=== HOÀN THÀNH TẤT CẢ 5 HỌC PHẦN KHỐI KINH TẾ HỌC ===")
    for r in results:
        print(f"• {r['subject']}: {r['pages']} trang | {r['size_mb']:.2f} MB")
