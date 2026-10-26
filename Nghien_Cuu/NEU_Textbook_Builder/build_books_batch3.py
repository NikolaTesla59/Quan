# -*- coding: utf-8 -*-
"""
NEU Textbook Generator - Batch 3 (Books 7, 8, 9)
7. Kinh tế công cộng - PGS.TS Vũ Cường
8. Quản trị thuế trong kinh doanh - PGS.TS Nguyễn Thị Thùy Dương
9. Kinh tế phát triển - PGS.TS Nguyễn Ngọc Sơn
"""
import os
import sys
import json
import pymupdf

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

BASE_DIR = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế"

def build_book_7():
    print("--- Đang biên soạn Sách 7: Kinh tế công cộng ---")
    title = "Kinh tế Công cộng"
    code = "KTCC1101"
    faculty = "Khoa Kinh tế học"
    authors = "PGS.TS. Vũ Cường (Chủ biên), PGS.TS. Hoàng Văn Cường, TS. Phạm Thế Anh"
    
    b = NEUTextbookBuilder(title, code, faculty, authors)
    b.build_cover()
    
    toc = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về Kinh tế Công cộng và Vai trò của Chính phủ",
         "topics": ["Đối tượng, phương pháp và mục tiêu nghiên cứu của kinh tế công cộng", "Hiệu quả Pareto và hai định lý cơ bản của kinh tế học phúc lợi", "Các thất bại của thị trường (Market Failures) và lý do can thiệp của chính phủ", "Ba chức năng kinh tế cốt lõi của chính phủ: Phân bổ, Phân phối, Ổn định"]},
        {"chapter_num": 2, "chapter_title": "Hàng hóa Công cộng và Cung ứng Công cộng",
         "topics": ["Đặc tính phi cạnh tranh (Non-rivalry) và phi loại trừ (Non-excludability)", "Phân loại hàng hóa thuần túy, không thuần túy, hàng hóa khuyến dụng", "Điều kiện cân bằng cung ứng tối ưu Samuelson (Tổng MRS = MRT)", "Vấn đề kẻ ăn không (Free-Rider Problem) và cơ chế giá định ngạch Lindahl"]},
        {"chapter_num": 3, "chapter_title": "Ngoại ứng và các Biện pháp Can thiệp của Chính phủ",
         "topics": ["Bản chất ngoại ứng tiêu cực và ngoại ứng tích cực trong sản xuất/tiêu dùng", "Chi phí xã hội cận biên (MSC) và lợi ích xã hội cận biên (MSB)", "Các giải pháp can thiệp dựa vào thị trường: Thuế Pigou và Trợ cấp Pigou", "Định lý Coase về quyền tài sản và thị trường hạn ngạch phát thải (Cap-and-Trade)"]},
        {"chapter_num": 4, "chapter_title": "Lý thuyết Lựa chọn Công cộng (Public Choice)",
         "topics": ["Cơ chế ra quyết định tập thể và quy tắc biểu quyết đa số (Majority Rule)", "Nghịch lý Condorcet và Định lý Bất khả của Kenneth Arrow", "Mô hình Cử tri Trung vị (Median Voter Theorem) và ứng dụng", "Hành vi tìm kiếm đặc lợi (Rent-Seeking) và các thất bại của chính phủ"]},
        {"chapter_num": 5, "chapter_title": "Lý thuyết Chi tiêu Công và Đánh giá Dự án Công",
         "topics": ["Quy mô, cơ cấu và xu hướng tăng trưởng chi tiêu công (Quy luật Wagner)", "Chi tiêu cho an sinh xã hội, giáo dục, y tế và đầu tư kết cấu hạ tầng", "Phương pháp Phân tích Chi phí - Lợi ích (Cost-Benefit Analysis - CBA)", "Xác định Tỷ suất chiết khấu xã hội (Social Discount Rate) và giá bóng"]},
        {"chapter_num": 6, "chapter_title": "Lý thuyết Thuế và Phân bổ Gánh nặng Thuế",
         "topics": ["Nguyên tắc đánh thuế tối ưu: Công bằng (Ngang/Dọc) và Hiệu quả kinh tế", "Phân tích gánh nặng thuế (Tax Incidence) và độ co giãn cung cầu", "Tổn thất vô ích của thuế (Deadweight Loss / Excess Burden)", "Nguyên tắc thuế tối ưu Ramsey và mô hình thuế thu nhập tối ưu Mirrlees"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chương 1
    intro1 = ("Chương 1 thiết lập nền tảng lý luận của kinh tế học khu vực công. "
              "Người học nắm vững các tiêu chuẩn hiệu quả kinh tế Pareto, các dạng thất bại thị trường và vai trò của nhà nước.")
    sec1 = [
        {"sec_num": 1, "sec_title": "Hiệu Quả Pareto và Hai Định Lý Phúc Lợi Kinh Tế",
         "content": ("Hiệu quả Pareto (Pareto Efficiency) là trạng thái phân bổ nguồn lực kinh tế mà tại đó không thể làm cho bất kỳ cá nhân nào "
                     "có lợi hơn mà không làm cho ít nhất một cá nhân khác bị thiệt hại.\n\n"
                     "Hai định lý cơ bản của Kinh tế học Phúc lợi (Fundamental Theorems of Welfare Economics):\n"
                     "- Định lý 1: Nếu thị trường là cạnh tranh hoàn hảo và tồn tại thị trường cho mọi hàng hóa (không có ngoại ứng, không có thông tin bất đối xứng), "
                     "thì trạng thái cân bằng thị trường tự do sẽ tự động đạt được hiệu quả phân bổ Pareto (Bàn tay vô hình của Adam Smith).\n"
                     "- Định lý 2: Bằng cách tái phân bổ các nguồn lực ban đầu thông qua các khoản thuế hoặc trợ cấp trọn gói (Lump-sum transfers), "
                     "xã hội có thể đạt được bất kỳ điểm cân bằng Pareto mong muốn nào phù hợp với mục tiêu công bằng xã hội."),
         "formulas": ["Điều kiện hiệu quả tiêu dùng: MRS_xy^A = MRS_xy^B",
                      "Điều kiện hiệu quả sản xuất: MRTS_LK^X = MRTS_LK^Y",
                      "Điều kiện hiệu quả tổng thể: MRT_xy = MRS_xy^A = MRS_xy^B"],
         "case_studies": [{"title": "Cơ Chế Thị Trường Bán Buôn Điện Cạnh Tranh Việt Nam (VWEM)", "detail": "Quá trình chuyển đổi từ cơ chế độc quyền mua bán điện duy nhất sang thị trường phát điện cạnh tranh nhằm tiệm cận hiệu quả Pareto."}]},
        {"sec_num": 2, "sec_title": "Các Thất Bại của Thị Trường và Chức Năng của Chính Phủ",
         "content": ("Thị trường thực tế luôn thất bại trong việc đạt tới hiệu quả Pareto do 4 nguyên nhân nội tại:\n"
                     "(1) Độc quyền tự nhiên và sức mạnh thị trường (Market Power): Dẫn đến việc định giá cao hơn chi phí cận biên (P > MC) và gây ra tổn thất xã hội.\n"
                     "(2) Hàng hóa công cộng (Public Goods): Thị trường tư nhân không có động cơ cung ứng do không loại trừ được người không trả tiền.\n"
                     "(3) Ngoại ứng (Externalities): Hoạt động của một chủ thể tác động đến lợi ích của chủ thể khác nhưng không được phản ánh qua giá cả thị trường.\n"
                     "(4) Thông tin bất đối xứng (Asymmetric Information): Dẫn đến lựa chọn đối nghịch (Adverse Selection) và rủi ro đạo đức (Moral Hazard).\n\n"
                     "Trước những thất bại đó, Nhà nước thực hiện 3 chức năng kinh tế của Musgrave: "
                     "Chức năng Phân bổ nguồn lực (Allocation), Chức năng Phân phối lại thu nhập (Distribution), và Chức năng Ổn định kinh tế vĩ mô (Stabilization)."),
         "formulas": ["Thước đo tổn thất xã hội do độc quyền: Deadweight Loss (DWL) = 0.5 x (P - MC) x (Q_c - Q_m)",
                      "Hệ số Lerner đo sức mạnh thị trường: L = (P - MC) / P = 1 / |Ed|"],
         "case_studies": [{"title": "Quy Hoạch Mạng Lưới Y Tế Dự Phòng và Kiểm Soát Dịch Bệnh", "detail": "Chính phủ đầu tư ngân sách công lập cung cấp vắc-xin tiêm chủng mở rộng miễn phí nhằm khắc phục thất bại thị trường y tế tư nhân."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Trạng thái Tốt thứ Nhì (The Theory of the Second Best - Lipsey & Lancaster 1956): Khi một trong các điều kiện tối ưu Pareto không thể thỏa mãn, việc cố gắng áp dụng các điều kiện tối ưu còn lại không chắc chắn nâng cao phúc lợi xã hội.",
            "Kinh tế học Thể chế Mới về Thất bại Thị trường và Thất bại Nhà nước (Market Failure vs Government Failure - Stiglitz 1998, Acemoglu 2005): Đánh đổi giữa chi phí giao dịch thị trường và chi phí quản liêu, tham nhũng của bộ máy công quyền.",
            "Chuyên đề Tiến sĩ: Mô hình hóa phúc lợi xã hội phi tuyến tính (Social Welfare Function) kiểm định đánh đổi giữa Hiệu quả kinh tế (Efficiency) và Công bằng phân phối (Equity - Okun's Leaky Bucket) trong chính sách thuế thu nhập tại Việt Nam."
        ]
    }
    q1 = [
        "Phát biểu và phân tích ý nghĩa kinh tế sâu sắc của Hai định lý cơ bản của Kinh tế học phúc lợi.",
        "Phân tích 4 nguyên nhân cốt lõi dẫn đến Thất bại của thị trường (Market Failures). Cho ví dụ thực tiễn tại Việt Nam cho từng dạng thất bại.",
        "Trình bày 3 chức năng kinh tế vĩ mô của Chính phủ theo mô hình Richard Musgrave: Phân bổ, Tái phân phối và Ổn định hóa."
    ]
    b.add_chapter(1, "Tổng quan về Kinh tế Công cộng và Vai trò của Chính phủ", intro1, sec1, phd1, q1)
    
    # Chương 2
    intro2 = ("Chương 2 đi sâu vào lý thuyết hàng hóa công cộng và cơ chế cung ứng công. "
              "Chương này giải thích hiện tượng kẻ ăn không (Free-Rider) và điều kiện cung ứng tối ưu Samuelson.")
    sec2 = [
        {"sec_num": 1, "sec_title": "Đặc Tính và Phân Loại Hàng Hóa Công Cộng",
         "content": ("Hàng hóa được phân loại dựa trên hai thuộc tính kinh tế cơ bản:\n"
                     "- Tính Cạnh tranh trong tiêu dùng (Rivalry): Việc một người tiêu dùng hàng hóa làm giảm lượng hàng hóa còn lại cho người khác.\n"
                     "- Tính Loại trừ trong tiêu dùng (Excludability): Có thể ngăn chặn những người không trả tiền sử dụng hàng hóa một cách dễ dàng và chi phí thấp.\n\n"
                     "Ma trận 4 loại hàng hóa kinh tế:\n"
                     "(1) Hàng hóa Tư nhân thuần túy (Private Goods): Có tính cạnh tranh VÀ Có tính loại trừ (quần áo, bánh mì, ô tô).\n"
                     "(2) Hàng hóa Công cộng thuần túy (Pure Public Goods): Phi cạnh tranh VÀ Phi loại trừ (Quốc phòng, Hải đăng, Dự báo thời tiết, Hệ thống pháp luật).\n"
                     "(3) Hàng hóa Công cộng không thuần túy / Hàng hóa Câu lạc bộ (Club Goods): Phi cạnh tranh NHƯNG Có tính loại trừ (Đường cao tốc thu phí, Truyền hình cáp).\n"
                     "(4) Nguồn tài nguyên chung (Common Pool Resources): Có tính cạnh tranh NHƯNG Phi loại trừ (Nguồn lợi thủy sản biển khơi, Nguồn nước ngầm)."),
         "formulas": ["Bi kịch nguồn tài nguyên chung (Tragedy of the Commons - Hardin 1968): Khai thác quá mức tài nguyên tự do tiếp cận dẫn đến cạn kiệt xã hội",
                      "Cầu thị trường hàng hóa tư nhân (Cộng ngang): Q_D = ∑ q_i(P)",
                      "Cầu thị trường hàng hóa công cộng (Cộng dọc): P = ∑ P_i(Q) = ∑ MRS_i"],
         "case_studies": [{"title": "Hệ Thống Đê Điều Sông Hồng và Trạm Radar Cảnh Báo Khí Tượng", "detail": "Ví dụ điển hình về hàng hóa công thuần túy bảo vệ toàn bộ cư dân đồng bằng Bắc Bộ mà không thể tư nhân hóa thu phí riêng lẻ."}]},
        {"sec_num": 2, "sec_title": "Điều Kiện Cung Ứng Samuelson và Cơ Chế Giá Lindahl",
         "content": ("Điều kiện Samuelson (Samuelson Condition - 1954) xác định mức cung ứng hàng hóa công cộng tối ưu Pareto:\n"
                     "Tổng tỷ lệ thay thế cận biên của tất cả các cá nhân trong xã hội phải bằng Tỷ lệ chuyển đổi cận biên trong sản xuất: ∑ MRS_i = MRT.\n"
                     "Nghĩa là: Tổng số tiền mà tất cả các cá nhân sẵn lòng chi trả cho một đơn vị hàng hóa công cộng bổ sung "
                     "phải đúng bằng Chi phí cận biên để sản xuất đơn vị hàng hóa công cộng đó (∑ MB_i = MC).\n\n"
                     "Vấn đề kẻ ăn không (Free-Rider Problem): "
                     "Do đặc tính phi loại trừ, mỗi cá nhân đều có động cơ che giấu mức độ sẵn lòng chi trả thực tế của mình để người khác gánh chịu chi phí, "
                     "dẫn đến việc thị trường tư nhân luôn cung ứng hàng hóa công dưới mức tối ưu xã hội (Underprovision).\n\n"
                     "Cơ chế giá định ngạch Lindahl (Lindahl Pricing): Mỗi cá nhân đóng góp một mức thuế suất đúng bằng lợi ích cận biên cá nhân mình nhận được. "
                     "Tuy nhiên cơ chế này khó áp dụng trong thực tế do chi phí thu thập thông tin sở thích quá lớn."),
         "formulas": ["Điều kiện Samuelson: ∑(MRS_xy^i) = MRT_xy  (với mọi cá nhân i = 1..N)",
                      "Cơ chế Lindahl: t_i = MRS_i(G*) sao cho ∑ t_i = MC(G*)"],
         "case_studies": [{"title": "Đầu Tư Tuyến Đường Sắt Đô Thị Cát Linh - Hà Đông", "detail": "Đánh giá lợi ích kinh tế xã hội vượt trội (giảm ùn tắc, giảm phát thải ô nhiễm) chứng minh sự cần thiết phải tài trợ ngân sách công cho giao thông công cộng."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Thiết kế Cơ chế Tiết lộ Sở thích (Mechanism Design & Preference Revelation - Groves-Ledyard & Clarke-Tiedeman Mechanism): Các thuật toán đánh thuế phạt (Vickrey-Clarke-Groves - VCG Mechanism) buộc các cá nhân tiết lộ trung thực mức sẵn lòng chi trả cho hàng hóa công.",
            "Cung cấp Hàng hóa Công cộng Cục bộ và Giả thuyết Di chuyển Tiebout (Tiebout Hypothesis 1956 'Voting with one's feet'): Sự cạnh tranh giữa các chính quyền địa phương tạo ra sự phân bổ tối ưu hàng hóa công theo sở thích cư dân.",
            "Chuyên đề Tiến sĩ: Mô hình hóa thực nghiệm sự hợp tác tự nguyện (Voluntary Provision of Public Goods) và lý thuyết Lòng vị tha ấm áp (Warm-glow Giving - Andreoni 1990) tại các cộng đồng làng xã nông thôn Việt Nam."
        ]
    }
    q2 = [
        "Phân biệt 4 nhóm hàng hóa trong nền kinh tế dựa trên hai tiêu chuẩn: Tính Cạnh tranh và Tính Loại trừ trong tiêu dùng.",
        "Phát biểu và chứng minh công thức Điều kiện Samuelson (∑ MRS = MRT) đối với cung ứng hàng hóa công cộng tối ưu.",
        "Giải thích bản chất kinh tế của 'Vấn đề kẻ ăn không' (Free-Rider Problem) và tại sao thị trường tự do luôn thất bại trong việc cung ứng hàng hóa công thuần túy."
    ]
    b.add_chapter(2, "Hàng hóa Công cộng và Cung ứng Công cộng", intro2, sec2, phd1, q2)
    
    # Chương 3
    intro3 = ("Chương 3 phân tích ngoại ứng - nguyên nhân gây ra sự sai lệch giữa chi phí cá nhân và chi phí xã hội. "
              "Nội dung đi sâu vào Thuế Pigou, Trợ cấp Pigou, Định lý Coase và Thị trường mua bán hạn ngạch khí thải.")
    sec3 = [
        {"sec_num": 1, "sec_title": "Bản Chất Ngoại Ứng và Tổn Thất Phúc Lợi Xã Hội",
         "content": ("Ngoại ứng (Externalities) phát sinh khi hành vi sản xuất hoặc tiêu dùng của một thực thể ảnh hưởng trực tiếp "
                     "đến phúc lợi của thực thể khác mà không thông qua bất kỳ khoản thanh toán hay bồi thường giá cả thị trường nào.\n\n"
                     "- Ngoại ứng tiêu cực (Negative Externalities): Ví dụ xả chất thải gây ô nhiễm môi trường. "
                     "Chi phí xã hội cận biên lớn hơn Chi phí tư nhân cận biên: MSC = MPC + MEC (Chi phí ngoại ứng cận biên). "
                     "Thị trường tư nhân sẽ sản xuất sản lượng lớn hơn mức tối ưu xã hội (Q_market > Q_social), gây ra tổn thất vô ích phúc lợi.\n\n"
                     "- Ngoại ứng tích cực (Positive Externalities): Ví dụ nghiên cứu khoa học R&D, giáo dục, tiêm chủng vắc-xin. "
                     "Lợi ích xã hội cận biên lớn hơn Lợi ích tư nhân cận biên: MSB = MPB + MEB (Lợi ích ngoại ứng cận biên). "
                     "Thị trường tư nhân sẽ cung ứng sản lượng thấp hơn mức tối ưu xã hội (Q_market < Q_social)."),
         "formulas": ["Ngoại ứng tiêu cực: Chi phí xã hội cận biên: MSC = MPC + MEC",
                      "Ngoại ứng tích cực: Lợi ích xã hội cận biên: MSB = MPB + MEB",
                      "Điều kiện tối ưu xã hội: MSC = MSB"],
         "case_studies": [{"title": "Vụ Xả Thải Ô Nhiễm Môi Trường Biển Formosa Hà Tĩnh (2016)", "detail": "Phân tích ngoại ứng tiêu cực khổng lồ làm sụp đổ ngành thủy sản, du lịch 4 tỉnh miền Trung và bài học về đánh giá chi phí môi trường trong dự án FDI."}]},
        {"sec_num": 2, "sec_title": "Các Giải Pháp Xử Lý Ngoại Ứng: Thuế Pigou và Định Lý Coase",
         "content": ("(1) Thuế Pigou (Pigouvian Tax): Chính phủ đánh thuế trên mỗi đơn vị sản phẩm gây ô nhiễm đúng bằng Chi phí ngoại ứng cận biên "
                     "tại mức sản lượng tối ưu xã hội: t* = MEC(Q*). "
                     "Thuế Pigou nội hóa hoàn toàn ngoại ứng (Internalizing the externality), buộc doanh nghiệp phải gánh chịu toàn bộ chi phí xã hội do mình gây ra.\n\n"
                     "(2) Trợ cấp Pigou (Pigouvian Subsidy): Đối với ngoại ứng tích cực, chính phủ trợ cấp đúng bằng Lợi ích ngoại ứng cận biên: s* = MEB(Q*).\n\n"
                     "(3) Định lý Coase (Ronald Coase 1960): Nếu quyền tài sản (Property Rights) được xác định rõ ràng, chi phí giao dịch bằng 0 (hoặc rất nhỏ), "
                     "và số lượng các bên tham gia ít, thì các bên tư nhân có thể tự thương lượng đàm phán để đạt được mức sản lượng tối ưu xã hội "
                     "mà không cần sự can thiệp của chính phủ, bất kể quyền tài sản ban đầu được trao cho ai.\n\n"
                     "(4) Thị trường Hạn ngạch Phát thải có thể chuyển nhượng (Cap-and-Trade): "
                     "Chính phủ ấn định trần phát thải tối đa và cấp phát hạn ngạch, cho phép các doanh nghiệp tự do mua bán giấy phép phát thải carbon."),
         "formulas": ["Mức thuế Pigou tối ưu: t* = MEC(Q*)",
                      "Định lý Coase: Đạt hiệu quả phân bổ Pareto khi Chi phí giao dịch (Transaction Costs) = 0"],
         "case_studies": [{"title": "Thiết Lập Thị Trường Tín Chỉ Carbon Việt Nam", "detail": "Xây dựng sàn giao dịch hạn ngạch phát thải khí nhà kính thí điểm theo Nghị định 06/2022/NĐ-CP hướng tới mục tiêu Net Zero 2050."}]}
    ]
    phd1 = {
        "topics": [
            "Định lý Weitzman về Lựa chọn Công cụ Chính sách Môi trường (Prices vs Quantities - Weitzman 1974): Phân tích điều kiện bất định về chi phí để quyết định nên kiểm soát bằng Giá (Thuế phát thải) hay kiểm soát bằng Lượng (Hạn ngạch phát thải).",
            "Mô hình Tăng trưởng Xanh và Lý thuyết Bội tức Kép của Thuế Carbon (Double Dividend Hypothesis of Environmental Taxes): Thuế môi trường vừa cắt giảm ô nhiễm, vừa tạo nguồn thu để giảm thuế đánh vào lao động và vốn, kích thích tăng trưởng kinh tế.",
            "Chuyên đề Tiến sĩ: Đánh giá tác động của Cơ chế điều chỉnh biên giới carbon của EU (CBAM) đối với xuất khẩu thép và nhôm của Việt Nam bằng mô hình CGE (Computable General Equilibrium)."
        ]
    }
    q3 = [
        "Phân biệt bản chất và sự sai lệch về sản lượng thị trường giữa Ngoại ứng tiêu cực và Ngoại ứng tích cực. Vẽ đồ thị minh họa.",
        "Trình bày nguyên tắc xác định mức Thuế Pigou tối ưu để nội hóa ngoại ứng ô nhiễm môi trường.",
        "Phát biểu Định lý Coase. Nêu rõ các điều kiện tiên quyết để Định lý Coase phát huy hiệu lực và những rào cản khi áp dụng vào thực tế."
    ]
    b.add_chapter(3, "Ngoại ứng và các Biện pháp Can thiệp của Chính phủ", intro3, sec3, phd1, q3)
    
    # Chương 4
    intro4 = ("Chương 4 tiếp cận khu vực công từ góc độ kinh tế học chính trị: Lý thuyết Lựa chọn Công cộng (Public Choice Theory). "
              "Chương này nghiên cứu hành vi thực tế của cử tri, chính trị gia và các nhóm lợi ích trong việc ra quyết định chính sách.")
    sec4 = [
        {"sec_num": 1, "sec_title": "Cơ Chế Biểu Quyết và Nghịch Lý Lựa Chọn Tập Thể",
         "content": ("Lý thuyết Lựa chọn Công cộng áp dụng các công cụ kinh tế học tân cổ điển để phân tích hành vi của các tác nhân chính trị "
                     "(giả định các chính trị gia và quan chức bộ máy công quyền cũng theo đuổi tư lợi cá nhân chứ không thuần túy là những 'thiên thần vị tha').\n\n"
                     "Các cơ chế biểu quyết tập thể:\n"
                     "- Biểu quyết nhất trí (Unanimity Rule - Wicksell): Đảm bảo cải thiện Pareto tuyệt đối nhưng chi phí thương lượng là vô tận.\n"
                     "- Biểu quyết đa số (Majority Rule): Phổ biến nhất nhưng chứa đựng nhiều khiếm khuyết toán học:\n"
                     "(1) Nghịch lý Condorcet (Condorcet Paradox): Hiện tượng biểu quyết luân vòng (Voting Cycles), trong đó sở thích tập thể mang tính bắc cầu bị phá vỡ "
                     "(Phương án A thắng B, B thắng C, nhưng C lại thắng A) tùy thuộc vào thứ tự đưa ra biểu quyết (Agenda Control).\n\n"
                     "(2) Định lý Bất khả của Kenneth Arrow (Arrow's Impossibility Theorem 1951): "
                     "Không tồn tại bất kỳ quy tắc biểu quyết tập thể nào có thể đồng thời thỏa mãn 5 điều kiện dân chủ và logic hợp lý tối thiểu "
                     "(Phạm vi không hạn chế, Tính Pareto, Tính độc lập đối với các phương án không liên quan, Phi độc tài, Tính bắc cầu)."),
         "formulas": ["Quy tắc tối ưuBuchanan-Tullock: Tối thiểu hóa Tổng chi phí = Chi phí đối kháng bên ngoài (External Costs) + Chi phí thương lượng ra quyết định (Decision-making Costs)"],
         "case_studies": [{"title": "Biểu Quyết Dự Án Đầu Tư Sân Bay Long Thành", "detail": "Quá trình tranh biện và biểu quyết thông qua chủ trương đầu tư đại dự án cảng hàng không quốc tế tại Quốc hội khóa XIII."}]},
        {"sec_num": 2, "sec_title": "Mô Hình Cử Tri Trung Vị và Hành Vi Tìm Kiếm Đặc Lợi (Rent-Seeking)",
         "content": ("- Mô hình Cử tri Trung vị (Median Voter Theorem - Downs 1957, Black 1948): "
                     "Nếu sở thích của các cử tri là đơn đỉnh (Single-peaked preferences) trên một không gian chính sách một chiều, "
                     "thì phương án được cử tri trung vị ưa thích nhất sẽ luôn đánh bại mọi phương án khác trong biểu quyết theo đa số. "
                     "Mô hình giải thích tại sao hai đảng phái chính trị lớn đều có xu hướng dịch chuyển cương lĩnh tranh cử về trung dung.\n\n"
                     "- Hành vi tìm kiếm đặc lợi (Rent-Seeking - Tullock 1967, Krueger 1974): "
                     "Là việc các doanh nghiệp hoặc nhóm lợi ích bỏ ra các nguồn lực kinh tế (vận động hành lang, hối lộ, tài trợ bầu cử) "
                     "không phải để tạo ra của cải mới cho xã hội, mà nhằm mục đích vận động chính phủ ban hành các cơ chế độc quyền, hạn ngạch nhập khẩu, "
                     "giấy phép con hoặc ưu đãi thuế riêng biệt. "
                     "Tổn thất xã hội do Rent-Seeking lớn hơn rất nhiều so với tổn thất vô ích thuần túy của độc quyền (Tullock Rectangle)."),
         "formulas": ["Tổn thất Rent-seeking của Gordon Tullock: Toàn bộ diện tích hình chữ nhật thặng dư độc quyền (Monopoly Rents) bị lãng phí vào các nỗ lực vận động chính sách",
                      "Điều kiện cử tri trung vị: Vị trí chính sách x* sao cho có đúng 50% cử tri muốn x <= x* và 50% cử tri muốn x >= x*"],
         "case_studies": [{"title": "Vấn Nạn Giấy Phép Con và Quản Lý Nhập Khẩu Ô Tô (Nghị định 116)", "detail": "Phân tích hành vi vận động chính sách của các liên doanh sản xuất ô tô trong nước nhằm dựng lên các rào cản kỹ thuật bảo hộ thị trường."}]}
    ]
    phd1 = {
        "topics": [
            "Mô hình Kinh tế Chính trị Nội sinh về Thuế và Chi tiêu (Probabilistic Voting Model & Citizen-Candidate Model - Besley & Coate 1997, Persson & Tabellini 2000): Cân bằng chính trị giữa phân bổ ngân sách cho hàng hóa công và trợ cấp mục tiêu cho các nhóm cử tri dao động (Swing Voters).",
            "Lý thuyết Bắt tù binh Quản lý (Regulatory Capture Theory - Stigler 1971): Cơ chế các cơ quan quản lý nhà nước bị thao túng và phục vụ lợi ích của chính các tập đoàn kinh doanh mà cơ quan đó có trách nhiệm thanh tra giám sát.",
            "Chuyên đề Tiến sĩ: Nghiên cứu định lượng mối quan hệ giữa Mức độ Phân cấp Tài khóa (Fiscal Decentralization), Chất lượng Thể chế Địa phương (PCI) và Hiệu quả Đầu tư Công tại 63 tỉnh thành Việt Nam."
        ]
    }
    q4 = [
        "Phát biểu và phân tích ý nghĩa của Định lý Bất khả của Kenneth Arrow đối với các quy tắc biểu quyết dân chủ.",
        "Trình bày Mô hình Cử tri Trung vị (Median Voter Theorem). Điều kiện nào về sở thích của cử tri để định lý này luôn luôn đúng?",
        "Phân biệt Khái niệm 'Tìm kiếm lợi nhuận thông thường' (Profit-Seeking) và 'Tìm kiếm đặc lợi' (Rent-Seeking). Tại sao Rent-Seeking lại làm lãng phí nguồn lực xã hội nghiêm trọng?"
    ]
    b.add_chapter(4, "Lý thuyết Lựa chọn Công cộng (Public Choice)", intro4, sec4, phd1, q4)
    
    # Chương 5
    intro5 = ("Chương 5 nghiên cứu lý thuyết chi tiêu công và phương pháp đánh giá dự án công bằng Phân tích Chi phí - Lợi ích (CBA). "
              "Chương này giúp người học lượng hóa các giá trị vô hình, giá bóng và tỷ suất chiết khấu xã hội.")
    sec5 = [
        {"sec_num": 1, "sec_title": "Quy Mô, Cơ Cấu và Động Lực Gia Tăng Chi Tiêu Công",
         "content": ("Chi tiêu công (Public Expenditure) là việc sử dụng các nguồn lực tài chính nhà nước để cung ứng hàng hóa, dịch vụ công "
                     "và thực hiện các chính sách an sinh xã hội. Chi tiêu công phân thành: Chi thường xuyên (lương công chức, y tế, giáo dục, quốc phòng) "
                     "và Chi đầu tư phát triển (xây dựng cầu đường, cảng biển, mạng lưới điện quốc gia).\n\n"
                     "Các lý thuyết giải thích sự gia tăng chi tiêu công trong lịch sử:\n"
                     "- Quy luật Wagner (Wagner's Law of Increasing State Activity): Khi thu nhập bình quân đầu người tăng lên, "
                     "nhu cầu của người dân về các dịch vụ công (giáo dục, y tế, an ninh, môi trường) tăng với tốc độ nhanh hơn thu nhập (độ co giãn co giãn theo thu nhập > 1).\n"
                     "- Bệnh chi phí của Baumol (Baumol's Cost Disease): Năng suất lao động trong khu vực công (giáo dục, hành chính) tăng rất chậm so với khu vực tư nhân công nghệ, "
                     "nhưng tiền lương khu vực công vẫn phải tăng tương ứng để giữ chân lao động, làm chi phí dịch vụ công tăng vọt theo thời gian.\n"
                     "- Hiệu ứng Dịch chuyển của Peacock và Wiseman (Displacement Effect): Trong các cuộc khủng hoảng, chiến tranh, dịch bệnh, "
                     "chi tiêu công tăng đột biến lên một mặt bằng mới và không bao giờ quay lại mức thấp trước khủng hoảng."),
         "formulas": ["Tỷ lệ chi tiêu công / GDP = (Tổng chi ngân sách nhà nước / GDP) x 100%",
                      "Độ co giãn của chi tiêu công theo thu nhập: E_G = (% Δ Chi tiêu công) / (% Δ GDP)"],
         "case_studies": [{"title": "Gói Kích Thích Kinh Tế và An Sinh Xã Hội Phòng Chống Covid-19 (Nghị quyết 43/2022/QH15)", "detail": "Gói hỗ trợ tài khóa quy mô 350.000 tỷ đồng tập trung vào đầu tư hạ tầng cao tốc Bắc - Nam và hỗ trợ lãi suất doanh nghiệp."}]},
        {"sec_num": 2, "sec_title": "Phân Tích Chi Phí - Lợi Ích (Cost-Benefit Analysis - CBA)",
         "content": ("Phân tích Chi phí - Lợi ích (CBA) là công cụ kinh tế lượng định giá toàn diện nhằm so sánh tổng chi phí xã hội "
                     "với tổng lợi ích xã hội của một dự án đầu tư công qua suốt vòng đời hoạt động:\n"
                     "(1) Nhận diện tất cả các dòng chi phí và lợi ích trực tiếp, gián tiếp và vô hình.\n"
                     "(2) Đo lường và quy đổi về giá trị tiền tệ sử dụng Giá bóng (Shadow Prices - điều chỉnh các méo mó do thuế, độc quyền hoặc trợ cấp).\n"
                     "(3) Chiết khấu dòng tiền tệ về hiện tại sử dụng Tỷ suất Chiết khấu Xã hội (Social Discount Rate - SDR).\n"
                     "(4) Đánh giá các tiêu chí lựa chọn dự án: Giá trị hiện tại ròng xã hội (Social Net Present Value - ENPV > 0), "
                     "Tỷ số Lợi ích - Chi phí (BCR > 1), Tỷ suất hoàn vốn nội bộ kinh tế (EIRR > SDR).\n\n"
                     "Định giá các giá trị phi thị trường: Phương pháp Chi phí Di chuyển (Travel Cost Method), "
                     "Phương pháp Định giá Nhà ở Hưởng thụ (Hedonic Pricing Method), và Phương pháp Đánh giá Ngẫu nhiên (Contingent Valuation Method - CVM)."),
         "formulas": ["Giá trị hiện tại ròng xã hội: ENPV = ∑ [(Lợi ích xã hội_t - Chi phí xã hội_t) / (1 + SDR)^t] - Chi phí đầu tư ban đầu",
                      "Tỷ số Lợi ích - Chi phí xã hội: BCR = PV(Social Benefits) / PV(Social Costs)"],
         "case_studies": [{"title": "Phân Tích CBA Dự Án Đường Sắt Tốc Độ Cao Bắc - Nam", "detail": "Lượng hóa giá trị tiết kiệm thời gian đi lại của hành khách, giảm tai nạn giao thông và giảm phát thải khí nhà kính trong bài toán kinh tế dự án 70 tỷ USD."}]}
    ]
    phd1 = {
        "topics": [
            "Tỷ suất Chiết khấu Xã hội Liên thế hệ (Intergenerational Discounting & Ramsey Rule - Stern Review on the Economics of Climate Change): Tranh luận giữa trường phái đạo đức (Stern SDR = 1.4%) và trường phái thị trường (Nordhaus SDR = 4.3%) trong định giá chi phí biến đổi khí hậu dài hạn.",
            "Lượng hóa Giá trị Thống kê của Một Đời Người (Value of a Statistical Life - VSL): Ứng dụng hồi quy tiền lương bù trừ rủi ro (Compensating Wage Differentials) để xác định giá trị kinh tế của việc cứu sống mạng người trong các dự án an toàn giao thông và y tế công cộng.",
            "Chuyên đề Tiến sĩ: Đánh giá Hiệu quả Chi tiêu Công cho Giáo dục Đại học và Nghiên cứu Khoa học đối với Tăng trưởng Năng suất Nhân tố Tổng hợp (TFP) của Việt Nam bằng mô hình Biến công cụ (Instrumental Variables)."
        ]
    }
    q5 = [
        "Phân tích 3 lý thuyết giải thích sự gia tăng chi tiêu công trong lịch sử: Quy luật Wagner, Bệnh chi phí Baumol và Hiệu ứng dịch chuyển Peacock-Wiseman.",
        "Trình bày các bước tiến hành Phân tích Chi phí - Lợi ích (CBA) đối với một dự án kết cấu hạ tầng công cộng.",
        "Khái niệm 'Giá bóng' (Shadow Price) và 'Tỷ suất chiết khấu xã hội' (Social Discount Rate). Tại sao không nên sử dụng lãi suất thị trường thương mại để chiết khấu các dự án công?"
    ]
    b.add_chapter(5, "Lý thuyết Chi tiêu Công và Đánh giá Dự án Công", intro5, sec5, phd1, q5)
    
    # Chương 6
    intro6 = ("Chương 6 nghiên cứu lý thuyết thuế và phân bổ gánh nặng thuế. "
              "Chương này trang bị phương pháp toán kinh tế phân tích tổn thất vô ích của thuế và các mô hình thuế tối ưu Ramsey, Mirrlees.")
    sec6 = [
        {"sec_num": 1, "sec_title": "Các Nguyên Tắc Đánh Thuế và Phân Bổ Gánh Nặng Thuế",
         "content": ("Thuế là khoản đóng góp bắt buộc, không hoàn trả trực tiếp của các pháp nhân và thể nhân cho Nhà nước "
                     "nhằm tài trợ cho việc cung cấp hàng hóa công và thực hiện tái phân phối thu nhập.\n\n"
                     "Hai nguyên tắc công bằng đánh thuế của Adam Smith:\n"
                     "- Nguyên tắc Công bằng theo Chiều ngang (Horizontal Equity): Những người có năng lực nộp thuế ngang nhau phải nộp số thuế như nhau.\n"
                     "- Nguyên tắc Công bằng theo Chiều dọc (Vertical Equity): Những người có năng lực nộp thuế cao hơn phải nộp thuế nhiều hơn "
                     "(thông qua biểu thuế lũy tiến từng phần Progressive Tax).\n\n"
                     "Phân bổ gánh nặng thuế (Tax Incidence): "
                     "Chủ thể thực tế phải gánh chịu số tiền thuế (Kinh tế) hoàn toàn khác biệt với chủ thể nộp thuế trên danh nghĩa luật định (Pháp lý). "
                     "Gánh nặng thuế được phân chia giữa người mua và người bán phụ thuộc vào Độ co giãn tương đối của Cung và Cầu theo giá:\n"
                     "- Bên nào có độ co giãn kém hơn (ít linh hoạt hơn, khó thay đổi hành vi hơn) sẽ phải gánh chịu phần lớn gánh nặng thuế.\n"
                     "- Nếu Cầu hoàn toàn không co giãn (Ed = 0): Người mua gánh chịu 100% số thuế.\n"
                     "- Nếu Cung hoàn toàn không co giãn (Es = 0): Người bán gánh chịu 100% số thuế."),
         "formulas": ["Tỷ lệ gánh nặng thuế người mua chịu: ΔP_d / t = Es / (Es + |Ed|)",
                      "Tỷ lệ gánh nặng thuế người bán chịu: |ΔP_s| / t = |Ed| / (Es + |Ed|)"],
         "case_studies": [{"title": "Tác Động của Thuế Bảo Vệ Môi Trường Đối Với Xăng Dầu", "detail": "Do cầu về xăng dầu của người dân ít co giãn trong ngắn hạn, phần lớn mức thuế môi trường 4.000 đ/lít được chuyển dịch hoàn toàn vào giá bán cho người tiêu dùng gánh chịu."}]},
        {"sec_num": 2, "sec_title": "Tổn Thất Vô Ích và Lý Thuyết Thuế Tối Ưu Ramsey",
         "content": ("Tổn thất vô ích của thuế (Deadweight Loss - DWL / Excess Burden): "
                     "Thuế làm thay đổi giá tương đối, bóp méo hành vi kinh tế (khiến người tiêu dùng mua ít đi, doanh nghiệp giảm sản xuất). "
                     "Tổn thất vô ích chính là phần phúc lợi thặng dư tiêu dùng và thặng dư sản xuất bị mất đi mà Nhà nước không thu được vào ngân sách.\n"
                     "Định luật Harberger: Tổn thất vô ích tỷ lệ thuận với độ co giãn cung cầu và tỷ lệ thuận với BÌNH PHƯƠNG của mức thuế suất (DWL ~ t^2). "
                     "Do đó, đánh thuế suất thấp trên một cơ sở thuế rộng (Broad base) sẽ gây ra tổn thất xã hội nhỏ hơn rất nhiều "
                     "so với việc đánh thuế suất rất cao trên một cơ sở thuế hẹp.\n\n"
                     "Nguyên tắc thuế tối ưu Ramsey (Ramsey Rule - 1927): "
                     "Để giảm thiểu tổng tổn thất vô ích khi thu một lượng ngân sách nhất định từ thuế gián thu hàng hóa, "
                     "Nhà nước nên đánh thuế suất cao hơn vào những hàng hóa có độ co giãn của cầu theo giá thấp (Hàng hóa thiết yếu ít co giãn) "
                     "và đánh thuế suất thấp vào hàng hóa có cầu co giãn mạnh (Nguyên tắc nghịch đảo độ co giãn - Inverse Elasticity Rule)."),
         "formulas": ["Tổn thất vô ích Harberger: DWL = 0.5 x [Ed x Es / (Es + |Ed|)] x P x Q x t^2",
                      "Quy tắc Ramsey nghịch đảo: t_i / t_j = |Ed_j| / |Ed_i| (Thuế suất tỷ lệ nghịch với độ co giãn của cầu)"],
         "case_studies": [{"title": "Cải Cách Thuế Tiêu Thụ Đặc Biệt Đối Với Rượu Bia và Nước Ngọt Có Đường", "detail": "Đánh giá tổn thất vô ích và hiệu quả điều tiết hành vi tiêu dùng khi tăng thuế suất thuế TTĐB rượu bia lên 75% tại Việt Nam."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Thuế Thu nhập Tối ưu Mirrlees (Mirrlees 1971 Optimal Income Taxation): Mô hình giải bài toán cân bằng giữa Tái phân phối thu nhập bình đẳng và Động lực làm việc của người lao động trong điều kiện năng lực lao động là thông tin tư nhân bất đối xứng.",
            "Độ co giãn của Thu nhập Chịu thuế (Elasticity of Taxable Income - ETI - Feldstein 1995, Saez, Slemrod & Giertz 2012): Đo lường toàn diện các phản ứng hành vi của người nộp thuế (trốn thuế, chuyển dịch thu nhập, giảm giờ làm) đối với thuế suất cận biên cao nhất.",
            "Chuyên đề Tiến sĩ: Ước lượng Độ co giãn của thu nhập chịu thuế (ETI) đối với tầng lớp người có thu nhập cao nhất tại Việt Nam bằng phương pháp Hồi quy Gián đoạn (Regression Discontinuity Design - RDD)."
        ]
    }
    q6 = [
        "Phân tích nguyên tắc phân bổ gánh nặng thuế (Tax Incidence). Tại sao chủ thể nộp thuế theo luật định không đồng nghĩa với chủ thể thực tế gánh chịu gánh nặng kinh tế của thuế?",
        "Chứng minh tại sao Tổn thất vô ích của thuế (Deadweight Loss) lại tăng theo hàm số bậc hai (bình phương) của mức thuế suất.",
        "Trình bày Quy tắc đánh thuế tối ưu Ramsey (Ramsey Rule). Phân tích xung đột giữa Mục tiêu hiệu quả kinh tế của quy tắc Ramsey với Mục tiêu công bằng xã hội."
    ]
    b.add_chapter(6, "Lý thuyết Thuế và Phân bổ Gánh nặng Thuế", intro1, sec1, phd1, q6)
    
    out_dir = os.path.join(BASE_DIR, r"04_Tài chính Công, Thuế & Hải quan\[NEU] Kinh tế công cộng - PGS.TS Vũ Cường (NXB ĐHKTQD)")
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Kinh tế công cộng - PGS.TS Vũ Cường (NXB ĐHKTQD).pdf")
    pages, size_mb = b.save(out_pdf)
    print(f"-> Hoàn thành Sách 7: {pages} trang, {size_mb:.2f} MB. Lưu tại: {out_pdf}")
    return {"book": "Kinh tế công cộng", "pages": pages, "size_mb": size_mb, "path": out_pdf}


def build_book_8():
    print("--- Đang biên soạn Sách 8: Quản trị thuế trong kinh doanh ---")
    title = "Quản trị Thuế trong Kinh doanh"
    code = "QTT1102"
    faculty = "Khoa Tài chính Công & Thuế"
    authors = "PGS.TS. Nguyễn Thị Thùy Dương (Chủ biên), PGS.TS. Lê Xuân Trường, TS. Nguyễn Đình Chiến"
    
    b = NEUTextbookBuilder(title, code, faculty, authors)
    b.build_cover()
    
    toc = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về Quản trị Thuế trong Doanh nghiệp",
         "topics": ["Bản chất và vai trò của quản trị thuế trong chiến lược tài chính", "Phân định ranh giới: Tối ưu hóa thuế (Tax Planning), Tránh thuế (Tax Avoidance) và Trốn thuế (Tax Evasion)", "Nhận diện và phân loại các rủi ro thuế trong chu trình kinh doanh", "Thiết lập hệ thống kiểm soát nội bộ và quản trị tuân thủ thuế"]},
        {"chapter_num": 2, "chapter_title": "Quản trị Thuế Giá trị Gia tăng (VAT Management)",
         "topics": ["Quản trị thuế GTGT đầu vào: Điều kiện khấu trừ và hóa đơn điện tử hợp pháp (NĐ 123/2020)", "Quản trị thuế GTGT đầu ra và thuế suất 0% cho hàng hóa xuất khẩu", "Thủ tục và kiểm soát rủi ro trong hoàn thuế GTGT dự án đầu tư và xuất khẩu", "Xử lý kế toán và điều chỉnh sai sót kê khai thuế GTGT"]},
        {"chapter_num": 3, "chapter_title": "Quản trị Thuế Thu nhập Doanh nghiệp (CIT Management)",
         "topics": ["Quản trị doanh thu tính thuế và thời điểm xác định doanh thu", "Quản trị chi phí được trừ và không được trừ theo Luật Thuế TNDN", "Chiến lược tận dụng ưu đãi thuế: Thuế suất ưu đãi, miễn giảm thuế theo địa bàn và ngành nghề", "Quản trị chính sách chuyển lỗ kinh doanh và trích lập quỹ phát triển KH&CN"]},
        {"chapter_num": 4, "chapter_title": "Quản trị Giao dịch Liên kết và Chống Chuyển giá",
         "topics": ["Bản chất của chuyển giá (Transfer Pricing) và nguyên tắc giao dịch độc lập (Arm's Length Principle)", "Quy định về giao dịch liên kết theo Nghị định 132/2020/NĐ-CP của Việt Nam", "Khống chế trần chi phí lãi vay được trừ (30% EBITDA)", "Phương pháp xác định giá giao dịch liên kết và lập hồ sơ 3 cấp (Local File, Master File, CbCR)"]},
        {"chapter_num": 5, "chapter_title": "Quản trị Thuế Nhà thầu Nước ngoài và Thương mại Điện tử",
         "topics": ["Đối tượng áp dụng và đối tượng được miễn thuế nhà thầu (FCT)", "Các phương pháp tính thuế FCT: Phương pháp trực tiếp, phương pháp khấu trừ và phương pháp hỗn hợp", "Quản trị thuế đối với các nhà cung cấp nước ngoài (Google, Meta, Netflix) và kinh tế số", "Áp dụng Hiệp định tránh đánh thuế hai lần (DTA) để miễn giảm thuế nhà thầu"]},
        {"chapter_num": 6, "chapter_title": "Chiến lược Thuế Toàn cầu và Thanh tra, Kiểm tra Thuế",
         "topics": ["Thuế tối thiểu toàn cầu (Global Minimum Tax - Pillar Two của OECD) và cơ chế QDMTT tại Việt Nam", "Hoạch định thuế trong hoạt động mua bán sáp nhập doanh nghiệp (Tax Due Diligence in M&A)", "Quy trình chuẩn bị hồ sơ quyết toán thuế và giải trình khi thanh tra thuế", "Quản trị rủi ro truy thu thuế và xử phạt vi phạm hành chính về thuế"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chương 1
    intro1 = ("Chương 1 cung cấp khung tư duy chiến lược về quản trị thuế doanh nghiệp. "
              "Người quản lý nắm vững ranh giới pháp lý giữa hoạch định thuế hợp pháp và hành vi trốn thuế bất hợp pháp.")
    sec1 = [
        {"sec_num": 1, "sec_title": "Khái Niệm và Ranh Giới Giữa Lập Kế Hoạch Thuế và Trốn Thuế",
         "content": ("Quản trị thuế (Tax Management) là quá trình chủ động lập kế hoạch, tổ chức thực hiện và kiểm soát "
                     "các nghĩa vụ thuế của doanh nghiệp nhằm tối ưu hóa số thuế phải nộp trong khuôn khổ pháp luật cho phép, "
                     "đồng thời hạn chế tối đa các rủi ro phạt vi phạm hành chính và tổn hại danh tiếng.\n\n"
                     "Phân định 3 cấp độ hành vi thuế:\n"
                     "(1) Hoạch định thuế hợp pháp (Tax Planning): Vận dụng các chính sách ưu đãi, miễn giảm thuế, "
                     "lựa chọn hình thức đầu tư và phương pháp kế toán tối ưu mà luật thuế khuyến khích.\n"
                     "(2) Tránh thuế (Tax Avoidance): Tận dụng các 'kẽ hở', khoảng trống pháp lý hoặc sự thiếu đồng bộ của hệ thống luật "
                     "để giảm thiểu nghĩa vụ thuế. Hành vi này không vi phạm câu chữ của luật nhưng đi ngược lại tinh thần lập pháp (Spirit of the Law).\n"
                     "(3) Trốn thuế (Tax Evasion): Hành vi cố ý vi phạm pháp luật bằng các thủ đoạn gian dối "
                     "(bỏ ngoài sổ sách kế toán, sử dụng hóa đơn khống, khai man doanh thu, hợp thức hóa chi phí giả tạo). "
                     "Trốn thuế là hành vi vi phạm pháp luật hình sự (Điều 200 Bộ luật Hình sự Việt Nam)."),
         "formulas": ["Lợi ích ròng của kế hoạch thuế = Tiết kiệm thuế ròng - Chi phí thực hiện kế hoạch thuế - Rủi ro bị truy thu & phạt",
                      "Tỷ lệ thuế hiệu dụng (Effective Tax Rate - ETR) = Tổng số thuế TNDN thực nộp / Lợi nhuận kế toán trước thuế"],
         "case_studies": [{"title": "Vụ Truy Thu Thuế Big C và Metro Cash & Carry Việt Nam", "detail": "Bài học kinh điển về chuyển nhượng vốn gián tiếp thông qua các pháp nhân trung gian tại nước ngoài và cuộc đấu tranh bảo vệ quyền đánh thuế của Tổng cục Thuế Việt Nam."}]},
        {"sec_num": 2, "sec_title": "Nhận Diện Rủi Ro Thuế và Hệ Thống Kiểm Soát Nội Bộ Về Thuế",
         "content": ("Rủi ro thuế trong doanh nghiệp phát sinh từ 4 nguồn chính:\n"
                     "- Rủi ro chính sách: Luật thuế thay đổi liên tục, thiếu hướng dẫn rõ ràng hoặc cách hiểu khác nhau giữa các đoàn kiểm tra thuế.\n"
                     "- Rủi ro giao dịch: Các giao dịch mua bán tài sản lớn, tái cấu trúc, giao dịch liên kết có tính chất phức tạp.\n"
                     "- Rủi ro tuân thủ: Sai sót kế toán, chậm nộp hồ sơ khai thuế, sử dụng phải hóa đơn của các doanh nghiệp 'ma' bỏ trốn.\n"
                     "- Rủi ro danh tiếng: Bị công khai danh sách nợ thuế, bị thanh tra chuyển giá gây ảnh hưởng đến giá cổ phiếu trên thị trường.\n\n"
                     "Xây dựng hệ thống kiểm soát nội bộ về thuế bao gồm: Quy chế kiểm soát hóa đơn đầu vào, "
                     "quy trình rà soát tính hợp lý - hợp lệ - hợp pháp của chứng từ chi phí, và định kỳ thực hiện Soát xét thuế độc lập (Tax Health-check)."),
         "formulas": ["Tiền chậm nộp thuế = Số tiền thuế chậm nộp x 0.03% x Số ngày chậm nộp",
                      "Phạt khai sai dẫn đến thiếu thuế = 20% số tiền thuế khai thiếu"],
         "case_studies": [{"title": "Quy Trình Kiểm Tra Rủi Ro Hóa Đơn Điện Tử Bằng Trí Tuệ Nhân Tạo", "detail": "Tổng cục Thuế áp dụng thuật toán phân tích chuỗi hóa đơn mua bán lòng vòng để tự động chặn các doanh nghiệp mua bán hóa đơn GTGT khống."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Tránh thuế Doanh nghiệp và Chi phí Đại diện (Corporate Tax Avoidance & Agency Theory - Desai & Dharmapala 2006, Hanlon & Heitzman 2010): Sự phức tạp của các cấu trúc né thuế tạo ra cơ hội cho các nhà quản lý che giấu thông tin và biển thủ tài sản của cổ đông.",
            "Thước đo Tránh thuế Thực nghiệm: Đo lường Cash ETR (Dyreng et al. 2008) dài hạn và Chênh lệch Sổ sách - Thuế Bất thường (Abnormal Book-Tax Differences) trong các nghiên cứu kinh tế lượng tài chính.",
            "Chuyên đề Tiến sĩ: Đánh giá mối quan hệ giữa Quản trị công ty (Quy mô HĐQT, Thành viên độc lập, Sở hữu tổ chức) và Mức độ Rủi ro Thuế (Tax Risk) tại các doanh nghiệp niêm yết trên thị trường chứng khoán Việt Nam."
        ]
    }
    q1 = [
        "Phân biệt rõ ràng ranh giới pháp lý và bản chất kinh tế giữa: Hoạch định thuế (Tax Planning), Tránh thuế (Tax Avoidance) và Trốn thuế (Tax Evasion).",
        "Trình bày các nhóm rủi ro thuế chủ yếu mà doanh nghiệp thường gặp phải và các biện pháp xây dựng hệ thống kiểm soát nội bộ về thuế hữu hiệu.",
        "Phân tích cơ chế phạt vi phạm hành chính về thuế và cách tính tiền chậm nộp thuế theo Luật Quản lý Thuế số 38/2019/QH14."
    ]
    b.add_chapter(1, "Tổng quan về Quản trị Thuế trong Doanh nghiệp", intro1, sec1, phd1, q1)
    
    # Chương 2
    intro2 = ("Chương 2 đi sâu vào quản trị thuế Giá trị gia tăng (VAT) - sắc thuế gián thu chiếm quy mô lớn nhất "
              "và có tần suất kiểm tra cao nhất trong mọi cuộc thanh tra thuế.")
    sec2 = [
        {"sec_num": 1, "sec_title": "Quản Trị Thuế GTGT Đầu Vào và Hóa Đơn Điện Tử (NĐ 123/2020)",
         "content": ("Theo Luật Thuế GTGT và Thông tư 219/2013/TT-BTC, thuế GTGT đầu vào được khấu trừ phải thỏa mãn 3 điều kiện đồng thời:\n"
                     "(1) Có hóa đơn GTGT hợp pháp của hàng hóa, dịch vụ mua vào (theo chuẩn hóa đơn điện tử Nghị định 123/2020/NĐ-CP).\n"
                     "(2) Có chứng từ thanh toán không dùng tiền mặt đối với hàng hóa, dịch vụ mua vào có giá trị từ 20 triệu đồng trở lên (bao gồm cả thuế GTGT).\n"
                     "(3) Hàng hóa, dịch vụ mua vào phải phục vụ cho hoạt động sản xuất kinh doanh hàng hóa, dịch vụ chịu thuế GTGT.\n\n"
                     "Quản trị rủi ro hóa đơn đầu vào:\n"
                     "- Tuyệt đối không chấp nhận các chứng từ thanh toán ủy nhiệm chi tiền mặt hoặc nộp tiền mặt vào tài khoản bên bán.\n"
                     "- Thường xuyên tra cứu tình trạng hoạt động của người bán trên Cổng thông tin của Tổng cục Thuế để loại trừ các đối tượng doanh nghiệp ngừng hoạt động, bỏ trốn mang theo hóa đơn.\n"
                     "- Phân bổ thuế GTGT đầu vào dùng chung cho hoạt động chịu thuế và không chịu thuế theo tỷ lệ doanh thu."),
         "formulas": ["Thuế GTGT phải nộp = Thuế GTGT đầu ra - Thuế GTGT đầu vào được khấu trừ",
                      "Thuế GTGT đầu vào được khấu trừ dùng chung = Thuế GTGT đầu vào dùng chung x (Doanh thu chịu thuế GTGT / Tổng doanh thu)"],
         "case_studies": [{"title": "Rủi Ro Mua Hàng của Doanh Nghiệp 'Bỏ Địa Bàn Kinh Doanh'", "detail": "Doanh nghiệp bị loại bỏ toàn bộ số thuế GTGT đầu vào khấu trừ và truy thu phạt 20% do nhà cung cấp bị cơ quan thuế thông báo bỏ trốn trước ngày lập hóa đơn."}]},
        {"sec_num": 2, "sec_title": "Quản Trị Hoàn Thuế GTGT và Thuế Suất 0% Cho Hàng Xuất Khẩu",
         "content": ("Thuế suất thuế GTGT 0% áp dụng cho hàng hóa, dịch vụ xuất khẩu ra nước ngoài hoặc bán vào khu phi thuế quan. "
                     "Hồ sơ chứng minh áp dụng thuế suất 0% bao gồm: Hợp đồng xuất khẩu, Tờ khai hải quan thông quan và Chứng từ thanh toán qua ngân hàng từ nước ngoài.\n\n"
                     "Quản trị quy trình hoàn thuế GTGT:\n"
                     "- Hoàn thuế cho dự án đầu tư mới: Áp dụng khi số thuế GTGT lũy kế của dự án đầu tư chưa đi vào hoạt động đạt từ 300 triệu đồng trở lên.\n"
                     "- Hoàn thuế cho hàng hóa xuất khẩu: Áp dụng khi số thuế GTGT đầu vào chưa được khấu trừ của hàng xuất khẩu từ 300 triệu đồng trở lên.\n"
                     "- Phân loại hồ sơ hoàn thuế: Hồ sơ 'Hoàn thuế trước, kiểm tra sau' (dành cho doanh nghiệp tuân thủ pháp luật thuế tốt) "
                     "và hồ sơ 'Kiểm tra trước, hoàn thuế sau' (dành cho doanh nghiệp có rủi ro cao, hoàn thuế lần đầu hoặc có dấu hiệu gian lận)."),
         "formulas": ["Số thuế GTGT hoàn cho hàng xuất khẩu = Min(Thuế GTGT đầu vào chưa khấu trừ của hàng xuất khẩu, 10% Doanh thu hàng hóa xuất khẩu)"],
         "case_studies": [{"title": "Vụ Án Gian Lận Hoàn Thuế GTGT Tại Công Ty Cổ Phần Thuduc House (TDH)", "detail": "Thủ đoạn lập hợp đồng xuất khẩu linh kiện điện tử giả mạo để chiếm đoạt hàng trăm tỷ đồng tiền hoàn thuế GTGT từ ngân sách nhà nước."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Chuỗi Giá trị Thuế GTGT và Cơ chế Tự Thực thi (Self-Enforcing Mechanism of VAT): Phân tích động cơ đối kháng quyền lợi giữa người mua (muốn hóa đơn để khấu trừ) và người bán (muốn giấu doanh thu) và các điểm đứt gãy chuỗi giá trị tại khâu bán lẻ tiêu dùng.",
            "Tác động của Hóa đơn Điện tử Tập trung (E-Invoicing Big Data): Khả năng giám sát theo thời gian thực của cơ quan thuế và sự sụt giảm của các hành vi gian lận hoàn thuế GTGT tại các nền kinh tế đang phát triển.",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về Tác động của chính sách giảm thuế suất thuế GTGT từ 10% xuống 8% đến hành vi tiêu dùng và khả năng phục hồi của các doanh nghiệp bán lẻ sau khủng hoảng."
        ]
    }
    q2 = [
        "Trình bày chi tiết 3 điều kiện bắt buộc để doanh nghiệp được khấu trừ thuế GTGT đầu vào theo quy định hiện hành.",
        "Phân biệt điều kiện áp dụng và hồ sơ chứng minh giữa Hàng hóa áp dụng Thuế suất GTGT 0% và Hàng hóa thuộc đối tượng Không chịu thuế GTGT.",
        "Quy trình quản trị rủi ro trong hồ sơ hoàn thuế GTGT đối với Dự án đầu tư và Hàng hóa xuất khẩu theo Luật Quản lý Thuế 2019."
    ]
    b.add_chapter(2, "Quản trị Thuế Giá trị Gia tăng (VAT Management)", intro2, sec2, phd1, q2)
    
    # Chương 3
    intro3 = ("Chương 3 phân tích trọng tâm quản trị thuế Thu nhập doanh nghiệp (CIT) - sắc thuế trực thu "
              "có mối liên hệ mật thiết nhất với lợi nhuận ròng sau thuế và cấu trúc chi phí doanh nghiệp.")
    sec3 = [
        {"sec_num": 1, "sec_title": "Quản Trị Chi Phí Được Trừ và Không Được Trừ Khi Tính Thuế TNDN",
         "content": ("Theo Luật Thuế TNDN, chi phí được trừ khi xác định thu nhập chịu thuế phải đáp ứng 3 điều kiện cốt lõi: "
                     "(1) Thực tế phát sinh liên quan đến hoạt động sản xuất, kinh doanh của doanh nghiệp; "
                     "(2) Có đủ hóa đơn, chứng từ hợp pháp theo quy định; "
                     "(3) Có chứng từ thanh toán không dùng tiền mặt đối với hóa đơn từ 20 triệu đồng trở lên.\n\n"
                     "Quản trị các khoản chi phí không được trừ trọng yếu (Điều 6 Thông tư 78/2014/TT-BTC):\n"
                     "- Chi phí khấu hao TSCĐ vượt mức quy định của Bộ Tài chính, hoặc khấu hao xe ô tô chở người từ 9 chỗ ngồi trở xuống có nguyên giá vượt trên 1.6 tỷ đồng (phần vượt 1.6 tỷ bị loại trừ).\n"
                     "- Chi phí tiền lương không có chứng từ thanh toán thực tế, lương của chủ doanh nghiệp tư nhân, công ty TNHH một thành viên do cá nhân làm chủ.\n"
                     "- Chi phí trang phục bằng tiền vượt quá 5 triệu đồng/người/năm.\n"
                     "- Chi phí lãi vay tương ứng với phần vốn điều lệ còn thiếu theo tiến độ góp vốn.\n"
                     "- Chi phí lãi vay vượt mức khống chế trần 30% EBITDA đối với doanh nghiệp có giao dịch liên kết theo Nghị định 132/2020/NĐ-CP.\n"
                     "- Các khoản tiền phạt vi phạm hành chính, phạt chậm nộp thuế."),
         "formulas": ["Thu nhập chịu thuế = Doanh thu tính thuế - Chi phí được trừ + Thu nhập chịu thuế khác",
                      "Thu nhập tính thuế = Thu nhập chịu thuế - Thu nhập được miễn thuế - Các khoản lỗ kết chuyển theo quy định (tối đa 5 năm)",
                      "Thuế TNDN phải nộp = Thu nhập tính thuế x Thuế suất (20%) - Quỹ KH&CN (tối đa 10%)"],
         "case_studies": [{"title": "Quản Trị Chi Phí Lãi Vay Vốn Góp Điều Lệ Thiếu", "detail": "Doanh nghiệp bị cơ quan thuế bóc tách loại trừ hàng chục tỷ đồng chi phí lãi vay do các cổ đông sáng lập chưa góp đủ vốn điều lệ theo Giấy phép đăng ký kinh doanh."}]},
        {"sec_num": 2, "sec_title": "Chiến Lược Tận Dụng Ưu Đãi Thuế và Chuyển Lỗ Kinh Doanh",
         "content": ("Chính phủ Việt Nam áp dụng nhiều gói ưu đãi thuế TNDN hấp dẫn nhằm thu hút đầu tư:\n"
                     "- Ưu đãi theo Địa bàn: Thuế suất ưu đãi 10% trong 15 năm, miễn thuế 4 năm và giảm 50% số thuế phải nộp trong 9 năm tiếp theo đối với dự án đầu tư tại địa bàn có điều kiện kinh tế - xã hội đặc biệt khó khăn, khu kinh tế, khu công nghệ cao.\n"
                     "- Ưu đãi theo Ngành nghề: Công nghệ cao, công nghệ thông tin phần mềm, bảo vệ môi trường, năng lượng tái tạo, nông nghiệp công nghệ cao.\n\n"
                     "Quản trị chuyển lỗ kinh doanh:\n"
                     "- Doanh nghiệp sau khi quyết toán thuế mà bị lỗ thì được chuyển toàn bộ và liên tục số lỗ vào thu nhập tính thuế của các năm tiếp theo.\n"
                     "- Thời gian chuyển lỗ tính liên tục không quá 5 năm kể từ năm tiếp sau năm phát sinh lỗ.\n"
                     "- Kế toán phải theo dõi chi tiết số lỗ của từng năm và lập Kế hoạch chuyển lỗ (Mẫu 03-2A/TNDN) để tối ưu hóa số thuế phải nộp."),
         "formulas": ["Công thức ưu đãi thuế: Thuế TNDN ưu đãi = Thu nhập từ dự án ưu đãi x Thuế suất ưu đãi x (1 - Tỷ lệ giảm thuế)",
                      "Giới hạn chuyển lỗ: Số lỗ chuyển trong kỳ <= Thu nhập tính thuế trước khi chuyển lỗ của kỳ đó"],
         "case_studies": [{"title": "Samsung Electronics Việt Nam (SEV Bắc Ninh & Thái Nguyên)", "detail": "Chiến lược tận dụng gói ưu đãi thuế cao nhất dành cho dự án công nghệ cao quy mô lớn, tiết kiệm hàng chục nghìn tỷ đồng tiền thuế TNDN trong thập kỷ qua."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Tránh thuế Doanh nghiệp và Cấu trúc Vốn (Taxes and Capital Structure - Graham 2000): Ước tính giá trị biên của lá chắn thuế từ lãi vay (Marginal Tax Rate) và điểm bão hòa của nợ vay.",
            "Tác động của Các Biện pháp Khuyến khích Thuế (Tax Incentives) đến Quyết định Đầu tư Trực tiếp Nước ngoài (FDI): Tranh luận về hiệu quả thực sự của các ưu đãi thuế so với chi phí mất nguồn thu ngân sách nhà nước.",
            "Chuyên đề Tiến sĩ: Đánh giá tác động của Quy định khống chế chi phí lãi vay (EBITDA Cap under Action 4 BEPS) đến cấu trúc tài trợ và hành vi đầu tư của các tập đoàn niêm yết tại Việt Nam."
        ]
    }
    q3 = [
        "Phân tích 3 điều kiện tiên quyết để một khoản chi phí được tính vào chi phí được trừ khi xác định thu nhập chịu thuế TNDN.",
        "Lập danh mục 6 khoản chi phí không được trừ điển hình mà doanh nghiệp thường xuyên bị cơ quan thuế bóc tách khi quyết toán thuế.",
        "Trình bày các hình thức ưu đãi thuế TNDN (về thuế suất, về thời gian miễn giảm) và quy định pháp luật về việc chuyển lỗ kinh doanh."
    ]
    b.add_chapter(3, "Quản trị Thuế Thu nhập Doanh nghiệp (CIT Management)", intro3, sec3, phd1, q3)
    
    # Chương 4
    intro4 = ("Chương 4 nghiên cứu vấn đề nóng bỏng nhất của quản trị thuế hiện đại: Quản trị giao dịch liên kết và chống chuyển giá. "
              "Chương này phân tích các quy định khắt khe của Nghị định 132/2020/NĐ-CP và nguyên tắc giao dịch độc lập.")
    sec4 = [
        {"sec_num": 1, "sec_title": "Bản Chất Chuyển Giá và Nguyên Tắc Giao Dịch Độc Lập",
         "content": ("Chuyển giá (Transfer Pricing) là việc các bên có quan hệ liên kết thiết lập giá giao dịch nội bộ "
                     "(mua bán hàng hóa, cung cấp dịch vụ, chuyển giao tài sản vô hình, cho vay vốn) khác biệt so với giá thị trường "
                     "nhằm mục đích chuyển dịch lợi nhuận từ nơi có thuế suất cao sang nơi có thuế suất thấp hoặc nơi đang được miễn thuế.\n\n"
                     "Nguyên tắc Giao dịch Độc lập (Arm's Length Principle): "
                     "Đòi hỏi các điều kiện thương mại và tài chính trong giao dịch giữa các bên liên kết phải tương đương "
                     "với các điều kiện trong các giao dịch độc lập giữa các bên không có quan hệ liên kết trong hoàn cảnh tương tự.\n\n"
                     "Các trường hợp xác định Bên liên kết theo Nghị định 132/2020/NĐ-CP:\n"
                     "- Một bên nắm giữ trực tiếp hoặc gián tiếp ít nhất 25% vốn góp của bên kia.\n"
                     "- Một bên bảo lãnh hoặc cho một bên khác vay vốn dưới bất kỳ hình thức nào với điều kiện khoản vốn vay ít nhất bằng 25% vốn góp và chiếm trên 50% tổng giá trị các khoản nợ trung và dài hạn.\n"
                     "- Hai bên đều có cùng một bên thứ ba nắm giữ từ 25% vốn góp trở lên."),
         "formulas": ["Nguyên tắc Arm's Length: Giá giao dịch liên kết = Giá giao dịch độc lập tương đương (P_related = P_independent)"],
         "case_studies": [{"title": "Vụ Thanh Tra Chuyển Giá Keangnam Vina (Hà Nội)", "detail": "Cơ quan thuế Việt Nam buộc Keangnam Vina giảm trừ hàng nghìn tỷ đồng chi phí xây dựng dàn xếp nội bộ và truy thu thuế TNDN phát sinh."}]},
        {"sec_num": 2, "sec_title": "Quy Định Nghị Định 132/2020/NĐ-CP và Khống Chế Lãi Vay 30% EBITDA",
         "content": ("Nghị định 132/2020/NĐ-CP đưa ra các quy định kiểm soát giao dịch liên kết chặt chẽ nhất từ trước đến nay:\n"
                     "(1) Quy định khống chế trần chi phí lãi vay (Khoản 3 Điều 16):\n"
                     "Tổng chi phí lãi vay (sau khi trừ lãi tiền gửi và lãi cho vay) phát sinh trong kỳ được trừ khi xác định thu nhập chịu thuế TNDN "
                     "không vượt quá 30% của tổng lợi nhuận thuần từ hoạt động kinh doanh cộng chi phí lãi vay thuần cộng chi phí khấu hao (EBITDA).\n"
                     "Phần chi phí lãi vay vượt mức 30% không được trừ sẽ được chuyển sang kỳ tính thuế tiếp theo khi xác định tổng chi phí lãi vay được trừ "
                     "trong thời hạn không quá 5 năm liên tục.\n\n"
                     "(2) Hệ thống Hồ sơ xác định giá giao dịch liên kết 3 cấp:\n"
                     "- Hồ sơ quốc gia (Local File): Phân tích chi tiết giao dịch liên kết của pháp nhân tại Việt Nam.\n"
                     "- Hồ sơ toàn cầu (Master File): Mô tả chuỗi giá trị và cơ cấu tổ chức của toàn bộ tập đoàn đa quốc gia.\n"
                     "- Báo cáo lợi nhuận liên quốc gia (Country-by-Country Report - CbCR): Báo cáo phân bổ doanh thu, lợi nhuận và thuế nộp trên toàn cầu."),
         "formulas": ["Trần chi phí lãi vay được trừ = 30% x EBITDA",
                      "EBITDA = Lợi nhuận thuần từ HĐKD + Chi phí lãi vay thuần (Chi phí lãi vay - Lãi tiền gửi/cho vay) + Chi phí khấu hao trong kỳ",
                      "Chi phí lãi vay không được trừ = Max(0, Chi phí lãi vay thuần - 30% x EBITDA)"],
         "case_studies": [{"title": "Tác Động của Trần Lãi Vay 30% EBITDA Đối Với Các Tập Đoàn Năng Lượng Tái Tạo", "detail": "Các dự án điện gió, điện mặt trời có tỷ lệ đòn bẩy vay nợ dự án (Project Finance) lên tới 80% đối mặt với rủi ro bị loại trừ hàng trăm tỷ đồng chi phí lãi vay trong những năm đầu vận hành."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Tránh thuế Xuyên Biên giới của Tập đoàn Đa quốc gia (MNE International Tax Avoidance - Hines & Rice 1994, Dharmapala 2014): Phân tích độ nhạy của việc chuyển dịch lợi nhuận (Profit Shifting) đối với chênh lệch thuế suất quốc tế.",
            "Khuôn khổ BEPS Action 8-10 và Đánh giá Bản chất Giao dịch Kinh tế (Substance over Form): Phân bổ lợi nhuận căn cứ vào Chức năng, Tài sản và Rủi ro thực tế (FAR Analysis - Functions, Assets, Risks) thay vì các hợp đồng danh nghĩa.",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về Tác động của việc ban hành Nghị định 132/2020/NĐ-CP đối với Quyết định cấu trúc vốn và Giá chuyển nhượng nội bộ của các doanh nghiệp FDI tại Việt Nam."
        ]
    }
    q4 = [
        "Định nghĩa Chuyển giá (Transfer Pricing) và phân tích Bản chất của Nguyên tắc Giao dịch Độc lập (Arm's Length Principle).",
        "Trình bày chi tiết tiêu chuẩn xác định các bên có quan hệ liên kết và quy định khống chế trần chi phí lãi vay 30% EBITDA theo Nghị định 132/2020/NĐ-CP.",
        "Mô tả cấu trúc của Bộ Hồ sơ xác định giá giao dịch liên kết 3 cấp (Local File, Master File, CbCR) mà doanh nghiệp liên kết bắt buộc phải chuẩn bị."
    ]
    b.add_chapter(4, "Quản trị Giao dịch Liên kết và Chống Chuyển giá", intro4, sec4, phd1, q4)
    
    # Chương 5
    intro5 = ("Chương 5 nghiên cứu quản trị thuế nhà thầu nước ngoài (Foreign Contractor Tax - FCT) "
              "và các mô hình thuế đối với thương mại điện tử, nền tảng số xuyên biên giới.")
    sec5 = [
        {"sec_num": 1, "sec_title": "Cơ Chế Thuế Nhà Thầu Nước Ngoài (FCT) Tại Việt Nam",
         "content": ("Thuế nhà thầu nước ngoài (FCT) áp dụng đối với các tổ chức, cá nhân nước ngoài kinh doanh tại Việt Nam "
                     "hoặc có thu nhập phát sinh tại Việt Nam trên cơ sở hợp đồng, thỏa thuận với tổ chức, cá nhân Việt Nam (Thông tư 103/2014/TT-BTC). "
                     "Thuế nhà thầu bao gồm nghĩa vụ thuế GTGT và nghĩa vụ thuế TNDN (hoặc thuế TNCN đối với cá nhân).\n\n"
                     "3 phương pháp nộp thuế nhà thầu:\n"
                     "(1) Phương pháp Khấu trừ: Nhà thầu nước ngoài thành lập văn phòng tại Việt Nam, nộp thuế GTGT và TNDN như doanh nghiệp Việt Nam.\n"
                     "(2) Phương pháp Trực tiếp (Phương pháp Tỷ lệ % trên doanh thu): Phổ biến nhất. "
                     "Bên Việt Nam có trách nhiệm khấu trừ và nộp thuế thay cho nhà thầu nước ngoài trước khi chuyển tiền ra nước ngoài:\n"
                     "- Tỷ lệ thuế GTGT tính trên doanh thu: Dịch vụ (5%), Xây dựng/sản xuất (3%).\n"
                     "- Tỷ lệ thuế TNDN tính trên doanh thu: Bản quyền (10%), Dịch vụ (5%), Cho vay vốn (5%), Thương mại phân phối (1%).\n"
                     "(3) Phương pháp Hỗn hợp: Nộp thuế GTGT theo phương pháp khấu trừ và nộp thuế TNDN theo tỷ lệ % doanh thu."),
         "formulas": ["Doanh thu tính thuế TNDN (Giá Net chưa bao gồm thuế): Doanh thu tính thuế = Số tiền thanh toán Net / (1 - Tỷ lệ % thuế TNDN)",
                      "Số thuế TNDN khấu trừ = Doanh thu tính thuế TNDN x Tỷ lệ % thuế TNDN",
                      "Số thuế GTGT khấu trừ = Doanh thu tính thuế GTGT x Tỷ lệ % thuế GTGT"],
         "case_studies": [{"title": "Hợp Đồng Thuê Bản Quyền Phần Mềm Oracle (Gross vs Net Contract)", "detail": "Đàm phán điều khoản hợp đồng Gross (nhà thầu chịu thuế FCT) so với hợp đồng Net (doanh nghiệp Việt Nam gánh chịu và đội chi phí lên)."}]},
        {"sec_num": 2, "sec_title": "Quản Trị Thuế Thương Mại Điện Tử Xuyên Biên Giới và DTA",
         "content": ("Sự bùng nổ của nền kinh tế số đặt ra bài toán thu thuế đối với các đại gia công nghệ không có hiện diện thể chất tại Việt Nam "
                     "(Google, Meta, Apple, Netflix, Amazon).\n\n"
                     "- Cổng thông tin điện tử dành cho Nhà cung cấp nước ngoài (NCCNN) của Tổng cục Thuế: "
                     "Cho phép các tập đoàn công nghệ trực tiếp đăng ký, kê khai và nộp thuế trực tuyến bằng ngoại tệ từ nước ngoài mà không cần ủy quyền bên Việt Nam.\n"
                     "- Trách nhiệm khấu trừ thuế của các sàn TMĐT và ngân hàng thương mại: Khấu trừ thuế trực tiếp trên dòng tiền thanh toán dịch vụ xuyên biên giới.\n\n"
                     "Áp dụng Hiệp định Tránh đánh thuế hai lần (Double Taxation Avoidance Agreement - DTA):\n"
                     "- Nếu nhà thầu nước ngoài thuộc quốc gia đã ký DTA với Việt Nam và KHÔNG tạo thành Cơ sở thường trú (Permanent Establishment - PE) tại Việt Nam, "
                     "thì lợi nhuận kinh doanh của nhà thầu đó sẽ được miễn thuế TNDN tại Việt Nam theo Điều 7 của Hiệp định DTA.\n"
                     "- Thủ tục áp dụng DTA đòi hỏi doanh nghiệp phải nộp Hồ sơ thông báo miễn giảm thuế kèm Giấy chứng nhận cư trú thuế hợp pháp."),
         "formulas": ["Tiêu chuẩn Cơ sở Thường trú (PE under OECD Model): Cơ sở cố định (chi nhánh, văn phòng) HOẶC Hiện diện dịch vụ trên 183 ngày HOẶC Đại lý phụ thuộc có thẩm quyền ký hợp đồng"],
         "case_studies": [{"title": "Thu Thuế Nền Tảng Quảng Cáo Trực Tuyến Facebook và Google", "detail": "Các tập đoàn công nghệ lớn đã chủ động đăng ký nộp thuế hàng nghìn tỷ đồng mỗi năm qua Cổng thông tin NCCNN của Tổng cục Thuế Việt Nam."}]}
    ]
    phd1 = {
        "topics": [
            "Khái niệm Cơ sở Thường trú Kỹ thuật số (Significant Economic Presence - SEP & Digital PE): Thách thức đối với quy tắc đánh thuế quốc tế truyền thống khi doanh nghiệp tạo ra giá trị khổng lồ từ dữ liệu người dùng nhưng không cần tài sản vật chất tại nước sở tại.",
            "Lý thuyết Trọng tài Thuế Quốc tế (International Tax Arbitrage & Treaty Shopping): Động cơ các tập đoàn lập công ty vỏ bọc (Conduit Companies) tại các quốc gia có mạng lưới hiệp định thuế ưu đãi để tránh thuế khấu trừ tại nguồn.",
            "Chuyên đề Tiến sĩ: Đánh giá hiệu quả của chính sách thuế đối với các giao dịch thương mại điện tử và dòng tiền thanh toán số tại Việt Nam bằng phương pháp kinh tế lượng chuỗi thời gian."
        ]
    }
    q5 = [
        "Trình bày các phương pháp kê khai và nộp Thuế Nhà thầu Nước ngoài (FCT) theo Thông tư 103/2014/TT-BTC. So sánh hợp đồng ký theo giá Net và giá Gross.",
        "Cơ chế quản lý và thu thuế đối với các Nhà cung cấp nước ngoài (Google, Meta, Netflix) không có hiện diện thể chất tại Việt Nam theo Thông tư 80/2021/TT-BTC.",
        "Phân tích điều kiện để một nhà thầu nước ngoài được miễn thuế TNDN tại Việt Nam theo Hiệp định Tránh đánh thuế hai lần (DTA)."
    ]
    b.add_chapter(5, "Quản trị Thuế Nhà thầu Nước ngoài và Thương mại Điện tử", intro5, sec5, phd1, q5)
    
    # Chương 6
    intro6 = ("Chương 6 tổng kết chiến lược quản trị thuế doanh nghiệp qua các xu hướng toàn cầu: Thuế tối thiểu toàn cầu (Pillar Two), "
              "hoạch định thuế trong M&A và quy trình chuyên nghiệp bảo vệ số liệu khi thanh tra kiểm tra thuế.")
    sec6 = [
        {"sec_num": 1, "sec_title": "Thuế Tối Thiểu Toàn Cầu (Pillar Two) và Tác Động Tại Việt Nam",
         "content": ("Trụ cột 2 (Pillar Two) trong Khuôn khổ Hợp tác Toàn cầu của OECD/G20 thiết lập mức Thuế tối thiểu toàn cầu là 15% "
                     "đối với các tập đoàn đa quốc gia có doanh thu hợp nhất từ 750 triệu Euro trở lên (khoảng 20.000 tỷ đồng) trong ít nhất 2 năm của 4 năm liền kề.\n\n"
                     "Cơ chế thực thi của Việt Nam theo Nghị quyết số 107/2023/QH15 của Quốc hội:\n"
                     "- Áp dụng Quy định thuế bổ sung tối thiểu nội địa đạt chuẩn (Qualified Domestic Minimum Top-up Tax - QDMTT):\n"
                     "Nếu một công ty con của tập đoàn đa quốc gia đầu tư tại Việt Nam có thuế suất hiệu dụng thực tế (Effective Tax Rate - ETR) dưới 15% "
                     "(do đang hưởng các gói ưu đãi thuế 0%, 5%, 10%), thì Việt Nam sẽ thực hiện quyền ưu tiên thu khoản thuế bổ sung chênh lệch để nâng ETR lên đúng 15%.\n"
                     "- Việc này đảm bảo nguồn thu thuế bổ sung nằm lại ngân sách nhà nước Việt Nam, "
                     "thay vì để nước nơi đặt trụ sở công ty mẹ thu theo Quy tắc tổng hợp thu nhập chịu thuế (IIR - Income Inclusion Rule)."),
         "formulas": ["Thuế suất bổ sung (Top-up Tax Rate) = 15% - Thuế suất hiệu dụng thực tế (ETR)",
                      "Thuế bổ sung phải nộp = (Thuế suất bổ sung x Thu nhập ròng theo Pillar Two) - Giảm trừ theo tài sản hữu hình và tiền lương (SBIE)"],
         "case_studies": [{"title": "Tác Động của Trụ Cột 2 Đến Chiến Lược Giữ Chân Đại Bàng FDI Của Việt Nam", "detail": "Chính phủ xây dựng Quỹ Hỗ trợ Đầu tư để chuyển đổi từ ưu đãi bằng thuế suất sang hỗ trợ chi phí nghiên cứu phát triển và hạ tầng công nghệ."}]},
        {"sec_num": 2, "sec_title": "Kỹ Năng Giải Trình và Quản Trị Rủi Ro Khi Thanh Tra, Kiểm Tra Thuế",
         "content": ("Thanh tra, kiểm tra thuế là quy trình cơ quan thuế đánh giá lại tính chính xác, trung thực của hồ sơ khai thuế doanh nghiệp.\n"
                     "Quy trình chuẩn bị hồ sơ quyết toán và ứng phó thanh tra thuế chuyên nghiệp:\n"
                     "(1) Giai đoạn trước thanh tra: Rà soát lại toàn bộ hệ thống hóa đơn, hợp đồng kinh tế, biên bản nghiệm thu, "
                     "chứng từ thanh toán ngân hàng; đối chiếu số liệu giữa BCTC và Tờ khai quyết toán thuế TNDN, TNCN, GTGT; "
                     "chủ động nộp tờ khai bổ sung điều chỉnh sai sót trước khi có Quyết định thanh tra để tránh bị phạt 20%.\n"
                     "(2) Giai đoạn trong thanh tra: Cử nhân sự kế toán trưởng am hiểu luật trực tiếp làm việc; "
                     "chỉ cung cấp các tài liệu thuộc phạm vi quyết định thanh tra; ghi chép chi tiết các biên bản làm việc hàng ngày.\n"
                     "(3) Giai đoạn dự thảo kết luận thanh tra: Nghiên cứu kỹ các căn cứ pháp lý của các khoản chi phí bị loại trừ; "
                     "chuẩn bị công văn giải trình kèm bằng chứng thực tế thuyết phục; đàm phán giải trình trước khi ký Biên bản thanh tra chính thức.\n"
                     "(4) Quyền khiếu nại và khởi kiện: Doanh nghiệp có quyền khiếu nại lên Cục Thuế/Tổng cục Thuế hoặc khởi kiện ra Tòa án Hành chính "
                     "nếu quyết định xử lý vi phạm thuế không đúng quy định pháp luật."),
         "formulas": ["Chiến lược giải trình: Chứng từ gốc đầy đủ + Bản chất giao dịch thực tế + Căn cứ văn bản quy phạm pháp luật có hiệu lực tại thời điểm phát sinh giao dịch"],
         "case_studies": [{"title": "Kinh Nghiệm Bảo Vệ Thành Công Chi Phí Nghiên Cứu và Phát Triển (R&D)", "detail": "Doanh nghiệp cung cấp nhật ký thử nghiệm lâm sàng, bằng sáng chế và hợp đồng chuyên gia bảo vệ thành công 50 tỷ đồng chi phí R&D không bị bóc tách."}]}
    ]
    phd1 = {
        "topics": [
            "Tác động của Thuế Tối thiểu Toàn cầu (OECD Pillar Two) đến Cạnh tranh Thuế Quốc tế (Tax Competition & Race to the Bottom): Sự tái cấu trúc dòng vốn đầu tư toàn cầu và các hình thức hỗ trợ đầu tư phi thuế (Subsidies & Grants).",
            "Mô hình Trò chơi Giữa Doanh nghiệp Nộp thuế và Cơ quan Thuế (Tax Audit Game - Reinganum & Wilde 1985): Xác suất thanh tra tối ưu của cơ quan thuế và mức độ tuân thủ của doanh nghiệp trong điều kiện nguồn lực thanh tra hữu hạn.",
            "Chuyên đề Tiến sĩ: Phân tích thực nghiệm các yếu tố quyết định mức độ bị truy thu và xử phạt thuế của các doanh nghiệp tư nhân trong các đợt thanh tra thuế định kỳ tại Việt Nam."
        ]
    }
    q6 = [
        "Bản chất và cơ chế vận hành của Thuế Tối thiểu Toàn cầu (Trụ cột 2 - Pillar Two). Phân tích giải pháp QDMTT của Việt Nam theo Nghị quyết số 107/2023/QH15.",
        "Quy trình kỹ thuật các bước chuẩn bị hồ sơ và chiến lược giải trình bảo vệ số liệu kế toán khi có Quyết định thanh tra, kiểm tra thuế tại doanh nghiệp.",
        "Phân tích vai trò của thẩm định rủi ro thuế (Tax Due Diligence) trong các thương vụ mua bán sáp nhập doanh nghiệp (M&A)."
    ]
    b.add_chapter(6, "Chiến lược Thuế Toàn cầu và Thanh tra, Kiểm tra Thuế", intro1, sec1, phd1, q6)
    
    out_dir = os.path.join(BASE_DIR, r"04_Tài chính Công, Thuế & Hải quan\[NEU] Quản trị thuế trong kinh doanh - PGS.TS Nguyễn Thị Thùy Dương (NXB ĐHKTQD)")
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Quản trị thuế trong kinh doanh - PGS.TS Nguyễn Thị Thùy Dương (NXB ĐHKTQD).pdf")
    pages, size_mb = b.save(out_pdf)
    print(f"-> Hoàn thành Sách 8: {pages} trang, {size_mb:.2f} MB. Lưu tại: {out_pdf}")
    return {"book": "Quản trị thuế trong kinh doanh", "pages": pages, "size_mb": size_mb, "path": out_pdf}


def build_book_9():
    print("--- Đang biên soạn Sách 9: Kinh tế phát triển ---")
    title = "Kinh tế Phát triển"
    code = "KTPT1101"
    faculty = "Khoa Kinh tế học"
    authors = "PGS.TS. Nguyễn Ngọc Sơn (Chủ biên), GS.TS. Ngô Thắng Lợi, TS. Đỗ Thị Hải Hà"
    
    b = NEUTextbookBuilder(title, code, faculty, authors)
    b.build_cover()
    
    toc = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về Kinh tế Phát triển và Đo lường Phát triển",
         "topics": ["Khái niệm tăng trưởng kinh tế và phát triển kinh tế bền vững", "Hệ thống chỉ tiêu đo lường: GDP, GNI, Thu nhập bình quân đầu người", "Chỉ số phát triển con người (HDI) và Chỉ số nghèo đa chiều (MPI)", "Mục tiêu phát triển thiên niên kỷ (MDGs) và Mục tiêu phát triển bền vững (SDGs 2030)"]},
        {"chapter_num": 2, "chapter_title": "Các Mô hình Tăng trưởng Kinh tế Cổ điển và Hiện đại",
         "topics": ["Mô hình Harrod-Domar và tỷ số hiệu quả sử dụng vốn (ICOR)", "Mô hình Nhị nguyên của W. Arthur Lewis về chuyển dịch lao động", "Mô hình Các giai đoạn phát triển kinh tế của W.W. Rostow", "Mô hình Tân cổ điển Solow-Swan, phân rã nguồn gốc tăng trưởng TFP và Mô hình tăng trưởng nội sinh Romer - Lucas"]},
        {"chapter_num": 3, "chapter_title": "Tích lũy Vốn, Dân số và Chuyển dịch Cơ cấu Kinh tế",
         "topics": ["Vai trò của vốn vật chất và vốn con người (Human Capital) trong tăng trưởng", "Biến động dân số, cổ tức dân số (Demographic Dividend) và già hóa dân số", "Mô hình di cư nông thôn - thành thị Todaro và thất nghiệp đô thị", "Quy luật chuyển dịch cơ cấu ngành: Nông nghiệp - Công nghiệp - Dịch vụ (Clark-Fisher)"]},
        {"chapter_num": 4, "chapter_title": "Bất bình đẳng Thu nhập và Xóa đói Giảm nghèo",
         "topics": ["Khái niệm nghèo tuyệt đối, nghèo tương đối và chuẩn nghèo đa chiều", "Đường cong Lorenz và Hệ số Gini đo lường bất bình đẳng", "Chỉ số nghèo Foster-Greer-Thorbecke (FGT) và khoảng cách nghèo", "Giả thuyết Chữ U ngược của Simon Kuznets và chính sách tăng trưởng bao trùm (Inclusive Growth)"]},
        {"chapter_num": 5, "chapter_title": "Thương mại Quốc tế, Dòng vốn Đầu tư và Phát triển",
         "topics": ["Chiến lược công nghiệp hóa thay thế nhập khẩu (ISI) và chiến lược hướng về xuất khẩu (EOI)", "Vai trò của đầu tư trực tiếp nước ngoài (FDI) và chuyển giao công nghệ", "Viện trợ phát triển chính thức (ODA) và quản lý nợ nước ngoài", "Bẫy nợ quốc gia và nguy cơ Bẫy thu nhập trung bình (Middle-Income Trap)"]},
        {"chapter_num": 6, "chapter_title": "Thể chế, Môi trường và Phát triển Bền vững",
         "topics": ["Kinh tế học thể chế mới (New Institutional Economics - Acemoglu, Robinson)", "Thể chế dung hợp (Inclusive Institutions) và thể chế chiếm đoạt (Extractive Institutions)", "Đường cong Môi trường Kuznets (EKC) và đánh đổi tăng trưởng - môi trường", "Kinh tế xanh, kinh tế tuần hoàn và chiến lược phát thải ròng bằng không (Net Zero)"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chương 1
    intro1 = ("Chương 1 mở đầu môn học Kinh tế phát triển bằng việc làm sáng tỏ sự khác biệt giữa Tăng trưởng kinh tế thuần túy "
              "và Phát triển kinh tế toàn diện theo quan điểm nhân văn của Amartya Sen (Phát triển là tự do).")
    sec1 = [
        {"sec_num": 1, "sec_title": "Khái Niệm Tăng Trưởng Kinh Tế và Phát Triển Kinh Tế",
         "content": ("Tăng trưởng kinh tế (Economic Growth) là sự gia tăng về quy mô sản lượng hàng hóa và dịch vụ "
                     "được sản xuất ra trong một nền kinh tế trong một khoảng thời gian nhất định (thường đo bằng tốc độ tăng GDP hoặc GNI thực tế).\n\n"
                     "Phát triển kinh tế (Economic Development) là một quá trình biến đổi tiến bộ toàn diện về mọi mặt của nền kinh tế, "
                     "bao gồm 3 nội dung cốt lõi:\n"
                     "(1) Sự gia tăng vững chắc của thu nhập bình quân đầu người gắn liền với nâng cao năng suất lao động;\n"
                     "(2) Sự chuyển dịch tiến bộ của cơ cấu kinh tế (cơ cấu ngành, cơ cấu vùng, cơ cấu thành phần kinh tế);\n"
                     "(3) Sự cải thiện sâu sắc về mặt xã hội: Xóa đói giảm nghèo, thu hẹp bất bình đẳng, nâng cao chất lượng giáo dục, y tế "
                     "và mở rộng các quyền tự do lựa chọn của con người (Amartya Sen - Development as Freedom)."),
         "formulas": ["Tốc độ tăng trưởng GDP thực tế: g_t = [(GDP_t - GDP_{t-1}) / GDP_{t-1}] x 100%",
                      "GNI = GDP + Thu nhập thuần từ yếu tố nước ngoài (NPI)"],
         "case_studies": [{"title": "Thành Tựu Đổi Mới Của Việt Nam Từ Năm 1986 Đến Nay", "detail": "Đưa Việt Nam từ một trong những quốc gia nghèo nhất thế giới trở thành nền kinh tế có thu nhập trung bình thấp với quy mô GDP vượt mốc 430 tỷ USD."}]},
        {"sec_num": 2, "sec_title": "Đo Lường Phát Triển Con Người (HDI) và Nghèo Đa Chiều (MPI)",
         "content": ("Nhằm khắc phục những hạn chế của chỉ tiêu GDP thuần túy, Chương trình Phát triển Liên Hợp Quốc (UNDP) "
                     "đã phát triển các thước đo tổng hợp chất lượng cuộc sống:\n\n"
                     "(1) Chỉ số Phát triển Con người (HDI - Human Development Index): Tính bằng trung bình nhân của 3 chỉ số thành phần:\n"
                     "- Sức khỏe: Đo bằng Tuổi thọ kỳ vọng khi sinh (từ 20 đến 85 tuổi).\n"
                     "- Giáo dục: Đo bằng Số năm đi học bình quân của người lớn và Số năm đi học kỳ vọng của trẻ em.\n"
                     "- Mức sống: Đo bằng GNI bình quân đầu người theo sức mua tương đương (PPP USD) lấy logarit tự nhiên.\n\n"
                     "(2) Chỉ số Nghèo Đa chiều (MPI - Multidimensional Poverty Index): Đo lường sự thiếu hụt trầm trọng của các hộ gia đình "
                     "trên 3 chiều kích tương tự (Y tế, Giáo dục, Điều kiện sống) thông qua 10 chỉ báo cụ thể "
                     "(dinh dưỡng, tử vong trẻ em, năm đi học, chuyên cần, nhiên liệu đun nấu, vệ sinh, nước sạch, điện, nhà ở, tài sản)."),
         "formulas": ["Chỉ số HDI = (I_SucKhoe x I_GiaoDuc x I_ThuNhap)^(1/3)",
                      "Chỉ số thành phần I = (Giá trị thực tế - Giá trị tối thiểu) / (Giá trị tối đa - Giá trị tối thiểu)",
                      "I_ThuNhap = [ln(GNIpc) - ln(100)] / [ln(75000) - ln(100)]",
                      "Chỉ số MPI = Tỷ lệ người nghèo đa chiều (H) x Mức độ thiếu hụt bình quân (A)"],
         "case_studies": [{"title": "Chỉ Số HDI và Giảm Nghèo Đa Chiều Tại Vùng Tây Bắc Việt Nam", "detail": "Phân tích khoảng cách phát triển giữa các vùng miền và nỗ lực nâng chỉ số HDI của Việt Nam lên nhóm Phát triển Con người Cao (High Human Development)."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Năng lực và Tự do của Amartya Sen (Capability Approach - Sen 1999): Đo lường sự phát triển không phải qua của cải vật chất mà qua việc mở rộng các năng lực thực chất (Substantive Freedoms) và cơ hội phát triển tiềm năng con người.",
            "Phê phán Thước đo GDP và Phong trào Vượt qua GDP (Beyond GDP Movement & Stiglitz-Sen-Fitoussi Commission Report 2009): Đo lường hạnh phúc xã hội, vốn tự nhiên và sự suy giảm tài nguyên môi trường.",
            "Chuyên đề Tiến sĩ: Ứng dụng mô hình phân tách Shapley phân tích các nhân tố đóng góp vào sự biến động của Chỉ số Nghèo đa chiều (MPI) tại các vùng đồng bào dân tộc thiểu số Việt Nam."
        ]
    }
    q1 = [
        "Phân biệt sự khác nhau căn bản giữa Tăng trưởng kinh tế (Economic Growth) và Phát triển kinh tế (Economic Development).",
        "Trình bày phương pháp tính toán và ý nghĩa kinh tế của 3 chỉ số thành phần cấu thành Chỉ số Phát triển Con người (HDI) theo chuẩn mực UNDP mới nhất.",
        "Phân tích cách tiếp cận Nghèo đa chiều (Multidimensional Poverty). Tại sao một gia đình có thu nhập trên chuẩn nghèo tiền tệ vẫn có thể bị coi là nghèo đa chiều?"
    ]
    b.add_chapter(1, "Tổng quan về Kinh tế Phát triển và Đo lường Phát triển", intro1, sec1, phd1, q1)
    
    # Chương 2
    intro2 = ("Chương 2 trình bày các mô hình tăng trưởng kinh tế cổ điển và hiện đại. "
              "Người học nắm vững mô hình Harrod-Domar, mô hình nhị nguyên Lewis, mô hình Solow-Swan và lý thuyết tăng trưởng nội sinh.")
    sec2 = [
        {"sec_num": 1, "sec_title": "Mô Hình Harrod-Domar và Tỷ Số ICOR",
         "content": ("Mô hình Harrod-Domar (1939, 1946) thiết lập mối quan hệ trực tiếp giữa Tỷ lệ tiết kiệm, Tích lũy vốn và Tốc độ tăng trưởng kinh tế:\n"
                     "Tốc độ tăng trưởng kinh tế (g) tỷ lệ thuận với Tỷ lệ tiết kiệm và đầu tư (s), và tỷ lệ nghịch với Hệ số gia tăng vốn - sản lượng (ICOR - Incremental Capital-Output Ratio):\n"
                     "g = s / ICOR.\n\n"
                     "Hệ số ICOR phản ánh để tạo ra thêm 1 đồng sản lượng GDP tăng thêm thì cần phải đầu tư thêm bao nhiêu đồng vốn:\n"
                     "ICOR = Vốn đầu tư tăng thêm (ΔK) / Sản lượng tăng thêm (ΔY) = Tổng vốn đầu tư / Mức gia tăng GDP.\n"
                     "ICOR càng thấp cho thấy hiệu quả sử dụng vốn của nền kinh tế càng cao. "
                     "Tại các nền kinh tế phát triển Đông Á (Hàn Quốc, Đài Loan trong thời kỳ cất cánh), ICOR thường duy trì ở mức 3 - 4; "
                     "trong khi tại Việt Nam giai đoạn trước đây, ICOR từng ở mức cao 6 - 7 do đầu tư công phân tán và kém hiệu quả."),
         "formulas": ["Tốc độ tăng trưởng Harrod-Domar: g = s / k (với s = I/Y; k = ICOR = ΔK/ΔY)",
                      "Hệ số ICOR = Tổng vốn đầu tư thực hiện (% GDP) / Tốc độ tăng trưởng GDP (%)"],
         "case_studies": [{"title": "Tái Cơ Cấu Đầu Tư Công và Cải Thiện Chỉ Số ICOR Việt Nam", "detail": "Nỗ lực siết chặt kỷ luật đầu tư công theo Luật Đầu tư công 2019 giúp giảm chỉ số ICOR từ 6.5 xuống mức khoảng 5.0."}]},
        {"sec_num": 2, "sec_title": "Mô Hình Tân Cổ Điển Solow-Swan và Tăng Trưởng Nội Sinh",
         "content": ("(1) Mô hình Tân Cổ Điển Solow-Swan (Robert Solow 1956 - Giải Nobel Kinh tế 1987):\n"
                     "Hàm sản xuất Cobb-Douglas dạng thâm dụng vốn: Y = A * K^α * L^(1-α)  (với 0 < α < 1).\n"
                     "Đặc tính quy luật lợi suất cận biên giảm dần của vốn (Diminishing Returns to Capital): "
                     "Khi tích lũy vốn trên một lao động (k = K/L) tăng lên, sản lượng cận biên của vốn sẽ giảm dần, "
                     "dẫn đến nền kinh tế sẽ tiệm cận Trạng thái Dừng (Steady State) mà tại đó đầu tư mới vừa đủ bù đắp khấu hao và tăng dân số.\n"
                     "Kết luận cách mạng của Solow: Tích lũy vốn vật chất không thể duy trì tăng trưởng kinh tế dài hạn. "
                     "Động lực duy nhất quyết định tăng trưởng thu nhập bình quân đầu người bền vững trong dài hạn là Tiến bộ Công nghệ ngoại sinh (A).\n\n"
                     "(2) Hạch toán Tăng trưởng và Năng suất Nhân tố Tổng hợp (TFP - Total Factor Productivity):\n"
                     "Phân rã tốc độ tăng trưởng GDP: g_Y = g_TFP + α * g_K + (1 - α) * g_L.\n\n"
                     "(3) Mô hình Tăng trưởng Nội sinh (Endogenous Growth Theory - Romer 1986, Lucas 1988):\n"
                     "Nội sinh hóa tiến bộ công nghệ thông qua Đầu tư cho Nghiên cứu & Phát triển (R&D), Đổi mới sáng tạo và Tích lũy Vốn con người (Human Capital) "
                     "với đặc tính Lợi suất tăng dần theo quy mô nhờ tính lan tỏa tri thức (Knowledge Spillovers)."),
         "formulas": ["Phương trình tích lũy vốn cơ bản của Solow: Δk = s*f(k) - (n + g + δ)*k",
                      "Trạng thái dừng (Steady State): s*f(k*) = (n + g + δ)*k*",
                      "Hạch toán tăng trưởng TFP: g_TFP = g_Y - [α * g_K + (1 - α) * g_L]"],
         "case_studies": [{"title": "Chuyển Đổi Mô Hình Tăng Trưởng Của Việt Nam Sang Đổi Mới Sáng Tạo", "detail": "Chỉ tiêu đóng góp của Năng suất các nhân tố tổng hợp (TFP) vào tăng trưởng GDP giai đoạn 2021-2025 đạt trên 45% thay thế dần mô hình thâm dụng vốn và lao động giá rẻ."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Hội tụ Kinh tế (Economic Convergence Hypothesis - Barro & Sala-i-Martin 1992): Kiểm định Hội tụ Tuyệt đối (Absolute Convergence) và Hội tụ Có điều kiện (Conditional Convergence) giữa các quốc gia đang phát triển và các quốc gia công nghiệp phát triển.",
            "Mô hình Tăng trưởng Phá hủy Sáng tạo Schumpeterian (Schumpeterian Growth Theory - Aghion & Howitt 1992): Quá trình cạnh tranh đổi mới công nghệ đào thải các doanh nghiệp lạc hậu và thúc đẩy biên giới công nghệ toàn cầu.",
            "Chuyên đề Tiến sĩ: Ước lượng đóng góp của TFP và Vốn nhân lực vào tăng trưởng kinh tế cấp tỉnh tại Việt Nam bằng phương pháp Hồi quy GMM hệ thống (System GMM Panel Data)."
        ]
    }
    q2 = [
        "Trình bày phương trình mô hình tăng trưởng Harrod-Domar. Phân tích ý nghĩa kinh tế và những hạn chế của hệ số ICOR.",
        "Phân tích cơ chế tiệm cận Trạng thái Dừng (Steady State) trong mô hình Tân cổ điển Solow-Swan. Tại sao Solow kết luận tiến bộ công nghệ là nhân tố duy nhất duy trì tăng trưởng dài hạn?",
        "Phương pháp Hạch toán Tăng trưởng (Growth Accounting) phân tách nguồn gốc tăng trưởng GDP thành đóng góp của Vốn (K), Lao động (L) và Năng suất Nhân tố Tổng hợp (TFP)."
    ]
    b.add_chapter(2, "Các Mô hình Tăng trưởng Kinh tế Cổ điển và Hiện đại", intro2, sec2, phd1, q2)
    
    # Chương 3
    intro3 = ("Chương 3 đi sâu vào các động lực cấu trúc: Tích lũy vốn, vốn con người, chuyển dịch lao động "
              "và mô hình di cư nông thôn - thành thị Todaro trong quá trình công nghiệp hóa, đô thị hóa.")
    sec3 = [
        {"sec_num": 1, "sec_title": "Vốn Con Người và Biến Động Cơ Cấu Dân Số",
         "content": ("Vốn con người (Human Capital - Gary Becker, Theodore Schultz) là toàn bộ kiến thức, kỹ năng, "
                     "sức khỏe và năng lực sáng tạo được tích lũy trong mỗi cá nhân thông qua giáo dục, đào tạo nghề và chăm sóc y tế.\n\n"
                     "Cơ cấu dân số và Cơ hội Cổ tức Dân số (Demographic Dividend):\n"
                     "- Thời kỳ Cơ cấu Dân số Vàng: Xảy ra khi tỷ lệ người trong độ tuổi lao động (15 - 64 tuổi) lớn gấp đôi tỷ lệ người phụ thuộc (dưới 15 và từ 65 tuổi trở lên). "
                     "Đây là cơ hội lịch sử chỉ xuất hiện một lần trong chu kỳ nhân khẩu học để tạo ra sự bứt phá kinh tế thần kỳ (như Nhật Bản thập niên 1960, Hàn Quốc thập niên 1980).\n"
                     "- Thách thức Già hóa Dân số: Việt Nam đang là một trong những quốc gia có tốc độ già hóa dân số nhanh nhất thế giới, "
                     "đối mặt với nguy cơ 'Chưa giàu đã già' nếu không kịp thời nâng cao năng suất lao động và hoàn thiện hệ thống an sinh xã hội."),
         "formulas": ["Tỷ số phụ thuộc dân số (Dependency Ratio) = [(Dân số dưới 15 + Dân số trên 65) / Dân số từ 15 đến 64] x 100%",
                      "Phương trình tiền lương Mincer (Human Capital Earnings Function): ln(w) = β0 + β1*Edu + β2*Exp + β3*Exp^2 + ε"],
         "case_studies": [{"title": "Chiến Lược Tận Dụng Giai Đoạn Cuối Cơ Cấu Dân Số Vàng Của Việt Nam", "detail": "Đẩy mạnh đào tạo nguồn nhân lực chất lượng cao ngành bán dẫn, trí tuệ nhân tạo và tự động hóa để vượt qua bẫy lao động giá rẻ."}]},
        {"sec_num": 2, "sec_title": "Mô Hình Chuyển Dịch Lao Động Lewis và Mô Hình Di Cư Todaro",
         "content": ("(1) Mô hình Nhị nguyên của W. Arthur Lewis (1954 - Giải Nobel Kinh tế 1979):\n"
                     "Nền kinh tế chia làm hai khu vực: Khu vực nông nghiệp truyền thống (thừa mứa lao động, năng suất cận biên bằng 0) "
                     "và Khu vực công nghiệp hiện đại (năng suất cao, tích lũy tư bản). "
                     "Khu vực hiện đại thu hút lao động nông thôn với mức lương cao hơn mức sống tự cấp tự túc. "
                     "Quá trình này tiếp diễn cho đến Điểm ngoặt Lewis (Lewis Turning Point) khi lao động nông nghiệp không còn dư thừa, "
                     "tiền lương nông nghiệp bắt đầu tăng lên và nền kinh tế chuyển sang giai đoạn thương mại hóa hoàn toàn.\n\n"
                     "(2) Mô hình Di cư Nông thôn - Thành thị Harris-Todaro (1970):\n"
                     "Giải thích nghịch lý tại sao người nông dân vẫn ồ ạt di cư ra thành phố bất chấp tỷ lệ thất nghiệp đô thị rất cao. "
                     "Quyết định di cư không dựa trên mức lương thực tế mà dựa trên Chênh lệch Thu nhập Kỳ vọng:\n"
                     "Thu nhập kỳ vọng tại đô thị = Tiền lương tối thiểu khu vực chính thức x Xác suất tìm được việc làm (tỷ lệ có việc làm).\n"
                     "Kết luận chính sách: Biện pháp tạo thêm việc làm ở thành phố sẽ chỉ kích thích làn sóng di cư mới lớn hơn, "
                     "làm trầm trọng thêm nạn thất nghiệp đô thị. Giải pháp căn cơ là phát triển nông thôn toàn diện và thu hẹp khoảng cách nông thôn - thành thị."),
         "formulas": ["Điều kiện cân bằng di cư Harris-Todaro: w_A = [E / (E + U)] x w_M",
                      "Trong đó: w_A là lương nông nghiệp; w_M là lương tối thiểu đô thị; E là số việc làm đô thị; U là số người thất nghiệp đô thị"],
         "case_studies": [{"title": "Làn Sóng Di Cư Lao Động Từ Miền Tây Lên Vùng Công Nghiệp Bình Dương - TP.HCM", "detail": "Phân tích thực trạng di cư theo mùa vụ và nhu cầu nhà ở xã hội, trường học cho con em công nhân tại các khu công nghiệp phía Nam."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Biến đổi Cấu trúc (Structural Transformation - Herrendorf, Rogerson & Valentinyi 2014): Phân tích động cơ dịch chuyển cơ cấu kinh tế giữa hiệu ứng thu nhập (Income Effect - Engel's Law) và hiệu ứng thay thế giá tương đối (Baumol Effect).",
            "Điểm ngoặt Lewis (Lewis Turning Point) và Bẫy Thiếu hụt Lao động tại các Nước Mới nổi Đông Á: Bài học từ Trung Quốc khi tiền lương nhân công tăng vọt buộc các ngành thâm dụng lao động phải dịch chuyển sang Việt Nam, Ấn Độ.",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về Tỷ suất sinh lời của Giáo dục Đại học (Returns to Higher Education) tại Việt Nam sử dụng phương pháp Biến công cụ (IV 2SLS) kiểm soát biến nội sinh năng lực bẩm sinh."
        ]
    }
    q3 = [
        "Trình bày khái niệm 'Cơ cấu dân số vàng' và phân tích những cơ hội, thách thức đối với phát triển kinh tế Việt Nam khi bước vào giai đoạn già hóa dân số.",
        "Phân tích cơ chế chuyển dịch lao động từ khu vực truyền thống sang khu vực hiện đại trong Mô hình Nhị nguyên của Arthur Lewis. 'Điểm ngoặt Lewis' là gì?",
        "Giải thích hiện tượng thất nghiệp đô thị ngày càng gia tăng bằng Mô hình di cư Harris-Todaro. Nêu các hàm ý chính sách giải quyết việc làm."
    ]
    b.add_chapter(3, "Tích lũy Vốn, Dân số và Chuyển dịch Cơ cấu Kinh tế", intro3, sec3, phd1, q3)
    
    # Chương 4
    intro4 = ("Chương 4 nghiên cứu mối quan hệ giữa tăng trưởng kinh tế, bất bình đẳng thu nhập và xóa đói giảm nghèo. "
              "Chương này trang bị các công cụ toán thống kê: Đường cong Lorenz, Hệ số Gini và chính sách phát triển bao trùm.")
    sec4 = [
        {"sec_num": 1, "sec_title": "Đo Lường Bất Bình Đẳng Thu Nhập và Hệ Số Gini",
         "content": ("Bất bình đẳng thu nhập phản ánh sự chênh lệch trong phân phối của cải và thu nhập giữa các tầng lớp dân cư trong xã hội.\n\n"
                     "- Đường cong Lorenz (Lorenz Curve): Đồ thị biểu diễn mối quan hệ giữa Tỷ lệ phần trăm cộng dồn của dân số (trục hoành) "
                     "và Tỷ lệ phần trăm cộng dồn của tổng thu nhập mà họ nhận được (trục tung). "
                     "Đường chéo 45 độ là đường phân phối hoàn toàn bình đẳng. Đường cong Lorenz càng võng xa đường 45 độ thì bất bình đẳng càng trầm trọng.\n\n"
                     "- Hệ số Gini (Gini Coefficient): Là tỷ số giữa diện tích nằm giữa đường 45 độ và đường cong Lorenz (A) "
                     "trên tổng diện tích tam giác nằm dưới đường 45 độ (A + B):\n"
                     "Gini = A / (A + B), có giá trị từ 0 đến 1.\n"
                     "- Gini = 0: Bình đẳng tuyệt đối (mọi người thu nhập bằng nhau).\n"
                     "- Gini = 1: Bất bình đẳng tuyệt đối (1 người nắm giữ toàn bộ thu nhập xã hội).\n"
                     "- Gini < 0.3: Bất bình đẳng thấp; 0.3 <= Gini <= 0.4: Bất bình đẳng trung bình; Gini > 0.4: Bất bình đẳng cao (nguy cơ bất ổn định xã hội)."),
         "formulas": ["Hệ số Gini = A / (A + B) = 1 - 2*B",
                      "Công thức tính Gini rời rạc: G = [1 / (2 * N^2 * μ)] * ∑∑ |y_i - y_j|",
                      "Tỷ số 20:20 (Palma Ratio) = Thu nhập của 20% người giàu nhất / Thu nhập của 20% (hoặc 40%) người nghèo nhất"],
         "case_studies": [{"title": "Diễn Biến Hệ Số Gini Của Việt Nam Qua Các Kỳ Khảo Sát Mức Sống (VHLSS)", "detail": "Hệ số Gini của Việt Nam duy trì ổn định ở mức 0.37 - 0.39, phản ánh thành công trong việc kết hợp tăng trưởng kinh tế nhanh với kiểm soát bất bình đẳng xã hội."}]},
        {"sec_num": 2, "sec_title": "Giả Thuyết Chữ U Ngược Kuznets và Tăng Trưởng Bao Trùm",
         "content": ("- Giả thuyết Chữ U ngược của Simon Kuznets (1955 - Giải Nobel Kinh tế 1971):\n"
                     "Mối quan hệ giữa Bất bình đẳng thu nhập (trục tung) và Thu nhập bình quân đầu người (trục hoành) có dạng hình chữ U ngược:\n"
                     "Trong giai đoạn đầu của quá trình phát triển (khi chuyển từ nông nghiệp sang công nghiệp), bất bình đẳng thu nhập có xu hướng gia tăng "
                     "do một bộ phận nhỏ nắm bắt cơ hội kinh doanh mới trở nên giàu có vượt bậc.\n"
                     "Tuy nhiên, khi nền kinh tế đạt tới mức phát triển công nghiệp hóa cao, bất bình đẳng sẽ đạt đỉnh và bắt đầu giảm xuống "
                     "nhờ sự phổ cập giáo dục, tiền lương lao động phổ thông tăng lên và nhà nước mở rộng chính sách phúc lợi an sinh xã hội.\n\n"
                     "- Chiến lược Tăng trưởng Bao trùm (Inclusive Growth): "
                     "Bác bỏ tư duy chờ đợi lợi ích kinh tế tự động 'thấm xuống' người nghèo (Trickle-down Economics). "
                     "Tăng trưởng bao trùm đòi hỏi tạo lập cơ hội tiếp cận bình đẳng cho mọi tầng lớp (đặc biệt là người yếu thế) "
                     "về giáo dục chất lượng cao, tín dụng vi mô, thị trường lao động và hạ tầng kết nối số."),
         "formulas": ["Chỉ số nghèo FGT tổng quát: P_α = (1 / N) * ∑ [ (z - y_i) / z ]^α  (cho y_i < z)",
                      "Với α = 0: Tỷ lệ đếm đầu người nghèo (Headcount Ratio - H); α = 1: Khoảng cách nghèo (Poverty Gap Ratio); α = 2: Mức độ nghiêm trọng của nghèo đói"],
         "case_studies": [{"title": "Chương Trình Mục Tiêu Quốc Gia Giảm Nghèo Bền Vững (Giai Đoạn 2021-2025)", "detail": "Chuyển đổi từ hỗ trợ cho không sang hỗ trợ sinh kế có điều kiện, tạo chuỗi giá trị nông nghiệp hàng hóa bản địa tại các huyện nghèo."}]}
    ]
    phd1 = {
        "topics": [
            "Bất bình đẳng Thu nhập và Bất bình đẳng Cơ hội (Inequality of Outcome vs Inequality of Opportunity - Roemer 1998, Chetty et al. 2014): Đo lường sự chuyển dịch kinh tế - xã hội giữa các thế hệ (Intergenerational Mobility).",
            "Tranh biện Thomas Piketty về Tư bản Thế kỷ 21 (Capital in the Twenty-First Century - Piketty 2014): Định luật r > g (Tỷ suất sinh lời của tư bản cao hơn tốc độ tăng trưởng kinh tế) như động lực cốt lõi dẫn đến sự tích tụ tài sản cực đoan của nhóm 1% giàu nhất.",
            "Chuyên đề Tiến sĩ: Đánh giá tác động của Tín dụng chính sách xã hội (NHCSXH) đối với việc thu hẹp khoảng cách giàu nghèo vùng dân tộc thiểu số Việt Nam bằng phương pháp Ghép điểm xu hướng (Propensity Score Matching - PSM)."
        ]
    }
    q4 = [
        "Vẽ và phân tích ý nghĩa kinh tế của Đường cong Lorenz. Trình bày công thức hình học và công thức thống kê tính Hệ số Gini.",
        "Phát biểu Giả thuyết Chữ U ngược của Simon Kuznets. Phân tích các yếu tố thúc đẩy bất bình đẳng gia tăng ở giai đoạn đầu và giảm đi ở giai đoạn sau của phát triển.",
        "Trình bày 3 chỉ số trong hệ thống đo lường nghèo đói Foster-Greer-Thorbecke (FGT): Tỷ lệ đếm đầu nghèo đói, Khoảng cách nghèo và Mức độ trầm trọng của nghèo."
    ]
    b.add_chapter(4, "Bất bình đẳng Thu nhập và Xóa đói Giảm nghèo", intro4, sec4, phd1, q4)
    
    # Chương 5
    intro5 = ("Chương 5 phân tích vai trò của hội nhập kinh tế quốc tế, thương mại và các dòng vốn đầu tư nước ngoài (FDI, ODA). "
              "Chương này làm sáng tỏ nguy cơ Bẫy thu nhập trung bình (Middle-Income Trap) và chiến lược nâng cấp chuỗi giá trị toàn cầu.")
    sec5 = [
        {"sec_num": 1, "sec_title": "Chiến Lược Thương Mại: Thay Thế Nhập Khẩu (ISI) vs Hướng Về Xuất Khẩu (EOI)",
         "content": ("Hai chiến lược công nghiệp hóa kinh điển của các quốc gia đang phát triển:\n"
                     "(1) Chiến lược Công nghiệp hóa Thay thế Nhập khẩu (Import Substitution Industrialization - ISI):\n"
                     "- Phổ biến tại Mỹ Latinh thập niên 1950 - 1970. Sử dụng hàng rào thuế quan và phi thuế quan bảo hộ nghiêm ngặt các ngành sản xuất non trẻ trong nước (Infant Industries).\n"
                     "- Hậu quả: Dẫn đến sự hình thành của các doanh nghiệp độc quyền hoạt động kém hiệu quả, hàng hóa chất lượng thấp, "
                     "thâm hụt ngân sách nặng nề và cuộc khủng hoảng nợ công tàn khốc.\n\n"
                     "(2) Chiến lược Công nghiệp hóa Hướng về Xuất khẩu (Export-Oriented Industrialization - EOI):\n"
                     "- Áp dụng thành công rực rỡ tại các nền kinh tế 'Bốn con Rồng Châu Á' (Hàn Quốc, Đài Loan, Singapore, Hồng Kông) và Việt Nam.\n"
                     "- Mở cửa thị trường, khai thác triệt để lợi thế so sánh (lao động dồi dào, vị trí địa kinh tế), tham gia sâu rộng vào chuỗi giá trị toàn cầu (GVC), "
                     "buộc các doanh nghiệp trong nước phải không ngừng cải tiến năng suất để cạnh tranh trên thị trường quốc tế."),
         "formulas": ["Độ mở kinh tế (Trade Openness) = [(Tổng kim ngạch xuất khẩu + Tổng kim ngạch nhập khẩu) / GDP] x 100%",
                      "Chỉ số Lợi thế So sánh Biểu hiện (RCA - Balassa Index): RCA_ij = (x_ij / X_i) / (x_wj / X_w)  (RCA > 1 thể hiện có lợi thế so sánh)"],
         "case_studies": [{"title": "Độ Mở Thương Mại Vượt Trội Của Nền Kinh Tế Việt Nam", "detail": "Tổng kim ngạch xuất nhập khẩu đạt trên 700 tỷ USD, đưa độ mở kinh tế của Việt Nam lên xấp xỉ 190% GDP - nằm trong nhóm cao nhất thế giới."}]},
        {"sec_num": 2, "sec_title": "Dòng Vốn FDI, ODA và Bẫy Thu Nhập Trung Bình (Middle-Income Trap)",
         "content": ("- Đầu tư trực tiếp nước ngoài (FDI): Mang lại vốn, công nghệ tiên tiến, kỹ năng quản trị và thị trường xuất khẩu. "
                     "Tuy nhiên, nếu thiếu vắng sự lan tỏa công nghệ (Spillover effects) và công nghiệp hỗ trợ trong nước yếu kém, "
                     "nền kinh tế sẽ rơi vào bẫy 'Gia công lắp ráp' giá trị gia tăng thấp (chỉ ăn phần nhân công mỏng).\n\n"
                     "- Viện trợ phát triển chính thức (ODA) và Quản lý Nợ nước ngoài: ODA cung cấp nguồn vốn ưu đãi xây dựng hạ tầng chiến lược, "
                     "nhưng phải kiểm soát chặt chẽ để tránh rủi ro gánh nặng nợ vay và biến động tỷ giá hối đoái.\n\n"
                     "- Bẫy Thu nhập Trung bình (Middle-Income Trap): Hiện tượng một nền kinh tế sau khi thoát khỏi ngưỡng nghèo đói "
                     "và đạt mức thu nhập trung bình (khoảng 4.000 - 12.000 USD/người) thì bị đình trệ tăng trưởng kéo dài hàng thập kỷ mà không thể bứt phá thành nước phát triển cao. "
                     "Nguyên nhân: Lợi thế nhân công giá rẻ mất dần trong khi chưa tạo dựng được năng lực công nghệ và đổi mới sáng tạo."),
         "formulas": ["Tỷ lệ liên kết chuỗi giá trị nội địa = (Giá trị nguyên phụ liệu trong nước / Tổng giá trị xuất khẩu) x 100%",
                      "Ngưỡng an toàn nợ công theo luật định: Nợ công <= 60% GDP; Nợ nước ngoài của quốc gia <= 45% GDP"],
         "case_studies": [{"title": "Kinh Nghiệm Vượt Bẫy Thu Nhập Trung Bình Của Hàn Quốc", "detail": "Đầu tư mạnh mẽ cho các tập đoàn Chaebol công nghệ (Samsung, Hyundai, LG) và nâng chi tiêu R&D lên trên 4.5% GDP để trở thành cường quốc công nghiệp phát triển."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Chuỗi Giá trị Toàn cầu và Nâng cấp Năng lực Công nghiệp (Global Value Chains & Industrial Upgrading - Gereffi 1999, Baldwin 2016): Bốn cấp độ nâng cấp: Nâng cấp quy trình (Process), Nâng cấp sản phẩm (Product), Nâng cấp chức năng (Functional: OBM/ODM) và Nâng cấp liên ngành (Inter-sectoral).",
            "Mô hình Vết dầu loang Công nghệ FDI (FDI Technology Spillovers - Javorcik 2004): Kiểm định sự lan tỏa công nghệ theo chiều dọc (Vertical Backward/Forward Linkages) so với sự chèn ép cạnh tranh theo chiều ngang (Horizontal Crowding-out Effect).",
            "Chuyên đề Tiến sĩ: Phân tích các yếu tố thể chế và vốn con người quyết định khả năng vượt Bẫy thu nhập trung bình của Việt Nam bằng mô hình Hồi quy Bảng Động (Dynamic Panel Data)."
        ]
    }
    q5 = [
        "So sánh bản chất, ưu điểm và nhược điểm giữa Chiến lược công nghiệp hóa thay thế nhập khẩu (ISI) và Chiến lược công nghiệp hóa hướng về xuất khẩu (EOI).",
        "Phân tích tác động tích cực và các tác động tiêu cực tiềm tàng của dòng vốn Đầu tư trực tiếp nước ngoài (FDI) đối với phát triển kinh tế các nước đang phát triển.",
        "Khái niệm 'Bẫy thu nhập trung bình' (Middle-Income Trap). Phân tích các nguyên nhân chính khiến các nền kinh tế bị mắc kẹt và giải pháp vượt bẫy cho Việt Nam."
    ]
    b.add_chapter(5, "Thương mại Quốc tế, Dòng vốn Đầu tư và Phát triển", intro5, sec5, phd1, q5)
    
    # Chương 6
    intro6 = ("Chương 6 đúc kết tầm nhìn phát triển hiện đại: Vai trò nền tảng của thể chế chính trị - kinh tế "
              "và chiến lược phát triển bền vững, kinh tế tuần hoàn, chuyển đổi xanh Net Zero 2050.")
    sec6 = [
        {"sec_num": 1, "sec_title": "Kinh Tế Học Thể Chế Mới và Nguồn Gốc Sâu Xa Của Thịnh Vượng",
         "content": ("Kinh tế học Thể chế Mới (New Institutional Economics - Douglass North 1990, Daron Acemoglu & James Robinson 2012):\n"
                     "Thể chế là 'luật chơi của một xã hội' (Rules of the game), bao gồm các ràng buộc chính thức (luật pháp, hiến pháp, quyền tài sản) "
                     "và các chuẩn mực phi chính thức (tập quán, văn hóa, niềm tin xã hội).\n\n"
                     "Hai loại hình thể chế kinh tế theo Acemoglu & Robinson (Why Nations Fail):\n"
                     "(1) Thể chế Dung hợp (Inclusive Economic Institutions): Bảo vệ an toàn quyền sở hữu tư nhân; "
                     "thực thi hợp đồng kinh tế công minh; tạo sân chơi cạnh tranh bình đẳng; khuyến khích tự do gia nhập thị trường và đổi mới sáng tạo. "
                     "Thể chế dung hợp là điều kiện tiên quyết bắt buộc để duy trì tăng trưởng kinh tế thịnh vượng dài hạn.\n\n"
                     "(2) Thể chế Chiếm đoạt (Extractive Economic Institutions): Được thiết kế bởi một nhóm thiểu số tinh hoa cầm quyền "
                     "nhằm bòn rút của cải, duy trì đặc quyền độc quyền và ngăn cản sự thâm nhập của công nghệ mới vì sợ đe dọa vị thế chính trị. "
                     "Thể chế chiếm đoạt có thể tạo ra tăng trưởng ngắn hạn nhưng chắc chắn sẽ sụp đổ khi cạn kiệt tài nguyên."),
         "formulas": ["Mối quan hệ nhân quả thể chế: Thể chế chính trị dung hợp -> Thể chế kinh tế dung hợp -> Bảo vệ quyền sở hữu & Khuyến khích đầu tư -> Tăng trưởng thịnh vượng dài hạn"],
         "case_studies": [{"title": "Nghiên Cứu Lịch Sử Đối Lập Giữa Bắc Triều Tiên và Hàn Quốc", "detail": "Cùng chung một dân tộc, địa lý và văn hóa ban đầu, nhưng sự phân nhánh giữa hai thể chế (chiếm đoạt vs dung hợp) sau năm 1953 đã tạo ra khoảng cách GDP đầu người chênh lệch hơn 30 lần ngày nay."}]},
        {"sec_num": 2, "sec_title": "Phát Triển Bền Vững, Đường Cong EKC và Cam Kết Net Zero 2050",
         "content": ("- Đường cong Môi trường Kuznets (Environmental Kuznets Curve - EKC - Grossman & Krueger 1991):\n"
                     "Mối quan hệ giữa Suy thoái ô nhiễm môi trường (trục tung) và Thu nhập bình quân đầu người (trục hoành) có dạng hình chữ U ngược:\n"
                     "Ở giai đoạn đầu công nghiệp hóa, ô nhiễm tăng nhanh do khai thác tài nguyên và khí thải công nghiệp nặng. "
                     "Khi thu nhập đạt mức cao, nền kinh tế chuyển sang dịch vụ công nghệ cao, người dân đòi hỏi chất lượng sống sạch hơn, "
                     "và công nghệ xử lý môi trường tiến bộ giúp ô nhiễm giảm dần.\n\n"
                     "- Kinh tế Tuần hoàn (Circular Economy): Mô hình kinh tế dựa trên nguyên lý thiết kế loại bỏ chất thải và ô nhiễm, "
                     "kéo dài vòng đời của sản phẩm và vật liệu, và tái tạo hệ thống tự nhiên (khác với mô hình kinh tế tuyến tính 'Khai thác - Sản xuất - Vứt bỏ').\n\n"
                     "- Cam kết Net Zero 2050 của Việt Nam tại COP26: Chuyển dịch năng lượng công bằng (JETP), "
                     "thay thế dần các nhà máy nhiệt điện than bằng điện gió ngoài khơi, điện mặt trời và phát triển thị trường tín chỉ carbon."),
         "formulas": ["Phương trình IPAT đo tác động môi trường: I = P x A x T\n(Trong đó: I là Tác động môi trường; P là Quy mô dân số; A là Mức độ giàu có thu nhập; T là Trình độ công nghệ)"],
         "case_studies": [{"title": "Chuyển Dịch Năng Lượng Công Bằng JETP Tại Việt Nam", "detail": "Huy động gói tài chính quốc tế 15.5 tỷ USD hỗ trợ Việt Nam đóng cửa sớm các nhà máy nhiệt điện than và phát triển lưới điện thông minh truyền tải năng lượng tái tạo."}]}
    ]
    phd1 = {
        "topics": [
            "Nguồn gốc Thuộc địa của Phát triển So sánh (The Colonial Origins of Comparative Development - Acemoglu, Johnson & Robinson 2001): Sử dụng Tỷ lệ Tử vong của Người định cư Châu Âu thế kỷ 18-19 làm Biến công cụ (Instrumental Variable) chứng minh thể chế là nguyên nhân căn bản của sự thịnh vượng kinh tế dài hạn.",
            "Địa lý vs Thể chế trong Tăng trưởng Dài hạn (Geography vs Institutions Debate - Sachs 2003 vs Rodrik et al. 2004): Tranh luận về vai trò chi phối của bệnh tật nhiệt đới, khí hậu so với chất lượng thượng tôn pháp luật (Rule of Law).",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về Tác động của Thể chế Quản trị Môi trường Địa phương đến Quyết định Thu hút Vốn FDI Xanh tại các tỉnh thành ven biển Việt Nam."
        ]
    }
    q6 = [
        "Phân biệt bản chất và sự tác động đến tăng trưởng dài hạn giữa Thể chế kinh tế dung hợp (Inclusive) và Thể chế kinh tế chiếm đoạt (Extractive) theo Acemoglu & Robinson.",
        "Trình bày nội dung và vẽ đồ thị minh họa Đường cong Môi trường Kuznets (EKC). Phân tích các yếu tố giúp chuyển hướng suy thoái môi trường sang xu hướng phục hồi.",
        "Phân biệt Mô hình kinh tế tuyến tính (Linear Economy) và Mô hình kinh tế tuần hoàn (Circular Economy). Nêu các giải pháp để Việt Nam thực hiện cam kết Net Zero 2050."
    ]
    b.add_chapter(6, "Thể chế, Môi trường và Phát triển Bền vững", intro1, sec1, phd1, q6)
    
    out_dir = os.path.join(BASE_DIR, r"06_Kinh tế học, Quản trị kinh doanh & Marketing\[NEU] Kinh tế phát triển - PGS.TS Nguyễn Ngọc Sơn (NXB ĐHKTQD)")
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Kinh tế phát triển - PGS.TS Nguyễn Ngọc Sơn (NXB ĐHKTQD).pdf")
    pages, size_mb = b.save(out_pdf)
    print(f"-> Hoàn thành Sách 9: {pages} trang, {size_mb:.2f} MB. Lưu tại: {out_pdf}")
    return {"book": "Kinh tế phát triển", "pages": pages, "size_mb": size_mb, "path": out_pdf}


if __name__ == "__main__":
    r7 = build_book_7()
    r8 = build_book_8()
    r9 = build_book_9()
    results = [r7, r8, r9]
    with open(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_agent_2_batch3_res.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("XONG BATCH 3 TOÀN VĂN!")
