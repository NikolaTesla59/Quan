# -*- coding: utf-8 -*-
"""
NEU Textbook Generator - Batch 2 (Books 4, 5, 6)
4. Kế toán quản trị - PGS.TS Trương Bá Thanh
5. Kiểm toán căn bản - GS.TS Nguyễn Quang Quynh
6. Phân tích báo cáo tài chính - PGS.TS Nguyễn Năng Phúc
"""
import os
import sys
import json
import pymupdf

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

BASE_DIR = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế"

def build_book_4():
    print("--- Đang biên soạn Sách 4: Kế toán quản trị ---")
    title = "Kế toán Quản trị"
    code = "KTKT1105"
    faculty = "Viện Kế toán - Kiểm toán"
    authors = "PGS.TS. Trương Bá Thanh (Chủ biên), PGS.TS. Đoàn Ngọc Quế, TS. Nguyễn Hữu Phú"
    
    b = NEUTextbookBuilder(title, code, faculty, authors)
    b.build_cover()
    
    toc = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về Kế toán Quản trị trong Doanh nghiệp",
         "topics": ["Bản chất và chức năng của kế toán quản trị trong hệ thống quản trị", "So sánh kế toán quản trị và kế toán tài chính", "Tổ chức công tác kế toán quản trị và đạo đức nghề nghiệp IMA", "Xu hướng phát triển hiện đại của kế toán quản trị chiến lược"]},
        {"chapter_num": 2, "chapter_title": "Phân loại Chi phí và Mô hình Ứng xử của Chi phí",
         "topics": ["Phân loại chi phí theo chức năng hoạt động và mức độ kiểm soát", "Mô hình ứng xử của chi phí: Chi phí biến đổi, chi phí cố định, chi phí hỗn hợp", "Các phương pháp phân tách chi phí hỗn hợp (Cực trị, Đồ thị phân tán, OLS)", "Khái niệm chi phí chìm, chi phí cơ hội và chi phí thích hợp"]},
        {"chapter_num": 3, "chapter_title": "Phân tích Mối quan hệ Chi phí - Khối lượng - Lợi nhuận (CVP)",
         "topics": ["Ý nghĩa kinh tế và các giả định của mô hình CVP", "Xác định điểm hòa vốn bằng sản lượng và bằng doanh thu", "Số dư đảm nhiệm (Contribution Margin) và tỷ suất số dư đảm nhiệm", "Đòn bẩy hoạt động (Degree of Operating Leverage - DOL) và phân tích CVP đa sản phẩm"]},
        {"chapter_num": 4, "chapter_title": "Dự toán Toàn diện Hoạt động Doanh nghiệp (Master Budget)",
         "topics": ["Bản chất, vai trò và quy trình lập dự toán tổng thể", "Hệ thống dự toán hoạt động: Tiêu thụ, sản xuất, NVL, nhân công, SX chung", "Dự toán chi phí bán hàng, chi phí quản lý doanh nghiệp", "Dự toán tài chính: Dự toán tiền mặt, BCTC dự toán và dự toán linh hoạt (Flexible Budget)"]},
        {"chapter_num": 5, "chapter_title": "Thông tin Thích hợp cho Ra Quyết định Quản trị Ngắn hạn",
         "topics": ["Khái niệm và tiêu chuẩn nhận diện thông tin thích hợp", "Quyết định chấp nhận hay từ chối đơn đặt hàng đặc biệt", "Quyết định tự sản xuất hay mua ngoài linh kiện (Make or Buy)", "Quyết định loại bỏ hay tiếp tục kinh doanh dòng sản phẩm/bộ phận thua lỗ", "Quyết định bán ngay tại điểm phân chia hay tiếp tục chế biến sâu"]},
        {"chapter_num": 6, "chapter_title": "Kế toán Quản trị Trách nhiệm và Đánh giá Thành quả",
         "topics": ["Mô hình phân cấp quản lý và các trung tâm trách nhiệm (Chi phí, Doanh thu, Lợi nhuận, Đầu tư)", "Đánh giá thành quả bằng ROI (Return on Investment) và RI (Residual Income)", "Giá trị gia tăng kinh tế (EVA - Economic Value Added)", "Thẻ điểm cân bằng (Balanced Scorecard - BSC) và định giá chuyển nhượng nội bộ (Transfer Pricing)"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chương 1
    intro1 = ("Chương 1 cung cấp cái nhìn toàn diện về kế toán quản trị như một hệ thống đo lường và cung cấp thông tin "
              "định hướng tương lai phục vụ trực tiếp cho việc hoạch định chiến lược, kiểm soát hoạt động và ra quyết định của ban lãnh đạo.")
    sec1 = [
        {"sec_num": 1, "sec_title": "Bản Chất và Vai Trò của Kế Toán Quản Trị",
         "content": ("Kế toán quản trị (Management Accounting) là một phân hệ thông tin kế toán cung cấp các thông tin định lượng "
                     "(cả tài chính và phi tài chính) cho các nhà quản trị nội bộ doanh nghiệp nhằm thực hiện 4 chức năng cốt lõi: "
                     "Lập kế hoạch, Tổ chức điều hành, Kiểm soát đánh giá và Ra quyết định chiến lược.\n\n"
                     "Khác với Kế toán tài chính mang tính pháp quy, tuân thủ nghiêm ngặt các chuẩn mực kế toán (VAS/IFRS) "
                     "và hướng về quá khứ để phục vụ cổ đông, ngân hàng và cơ quan thuế; "
                     "Kế toán quản trị hoàn toàn linh hoạt, không bị ràng buộc bởi các quy định pháp lý, tập trung vào từng bộ phận, phân xưởng "
                     "và định hướng về các kịch bản tương lai."),
         "formulas": ["Giá trị thông tin quản trị = Lợi ích kinh tế gia tăng từ quyết định đúng - Chi phí thu thập và xử lý thông tin",
                      "Hệ thống thông tin quản lý tích hợp: Dữ liệu giao dịch ERP -> Phân tích quản trị (BI) -> Quyết định điều hành"],
         "case_studies": [{"title": "Tập đoàn TH True Milk", "detail": "Thiết lập hệ thống kế toán quản trị trang trại và nhà máy sữa tươi, theo dõi chi phí dinh dưỡng từng cá thể đàn bò và năng suất vắt sữa tự động theo thời gian thực."}]},
        {"sec_num": 2, "sec_title": "Đạo Đức Nghề Nghiệp và Xu Hướng Phát Triển Hiện Đại",
         "content": ("Các chuẩn mực đạo đức nghề nghiệp theo Viện Kế toán Quản trị Hoa Kỳ (IMA Code of Professional Ethics) gồm 4 trụ cột: "
                     "(1) Năng lực chuyên môn (Competence); (2) Tính bảo mật (Confidentiality); (3) Tính chính trực (Integrity); "
                     "và (4) Tính khách quan (Credibility).\n\n"
                     "Trong kỷ nguyên số, kế toán quản trị phát triển mạnh mẽ theo hướng Kế toán quản trị chiến lược (Strategic Management Accounting - SMA), "
                     "kết hợp dữ liệu chi phí vòng đời sản phẩm (Life-cycle costing), chi phí chất lượng (Cost of Quality), "
                     "và kế toán quản trị môi trường (Environmental Management Accounting - EMA)."),
         "formulas": ["Chi phí chất lượng (COQ) = Chi phí ngăn ngừa + Chi phí kiểm định + Chi phí sai hỏng nội bộ + Chi phí sai hỏng ngoại vi"],
         "case_studies": [{"title": "Công ty Cổ phần Sợi Thế Kỷ (STK)", "detail": "Ứng dụng kế toán quản trị xanh theo dõi chi phí sản xuất sợi tái chế từ vỏ chai nhựa (Recycled Yarn) phục vụ các thương hiệu thời trang thể thao toàn cầu."}]}
    ]
    phd1 = {
        "topics": [
            "Hệ thống Kiểm soát Quản trị (Management Control Systems - Simons' 1995 Levers of Control): Sự cân bằng động giữa Hệ thống Niềm tin (Belief Systems), Hệ thống Giới hạn (Boundary Systems), Hệ thống Kiểm soát Chẩn đoán (Diagnostic) và Hệ thống Kiểm soát Tương tác (Interactive).",
            "Lý thuyết Dự phòng trong Kế toán Quản trị (Contingency Theory of Management Accounting - Otley 1980, Chenhall 2003): Sự tương thích giữa thiết kế hệ thống kế toán quản trị với chiến lược cạnh tranh, công nghệ sản xuất và mức độ bất định của môi trường vĩ mô.",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về mối liên hệ giữa Kế toán Quản trị Chiến lược (SMA) và Lợi thế Cạnh tranh Bền vững của các doanh nghiệp sản xuất tại Việt Nam."
        ]
    }
    q1 = [
        "Lập bảng so sánh chi tiết sự khác nhau căn bản giữa Kế toán quản trị và Kế toán tài chính về các khía cạnh: Mục đích, đối tượng phục vụ, tính pháp lý, thước đo sử dụng và phạm vi báo cáo.",
        "Trình bày 4 chuẩn mực đạo đức nghề nghiệp của kế toán quản trị theo quy định của Hiệp hội Kế toán Quản trị Quốc tế (IMA).",
        "Phân tích vai trò của thông tin kế toán quản trị trong việc thúc đẩy chiến lược dẫn đầu về chi phí thấp (Cost Leadership) và chiến lược khác biệt hóa (Differentiation)."
    ]
    b.add_chapter(1, "Tổng quan về Kế toán Quản trị trong Doanh nghiệp", intro1, sec1, phd1, q1)
    
    # Chương 2
    intro2 = ("Chương 2 phân tích chuyên sâu về hành vi ứng xử của chi phí theo sự thay đổi của mức độ hoạt động. "
              "Đây là chìa khóa then chốt để xây dựng các mô hình dự báo và tối ưu hóa lợi nhuận.")
    sec2 = [
        {"sec_num": 1, "sec_title": "Mô Hình Ứng Xử của Chi Phí: Biến Phí, Định Phí và Chi Phí Hỗn Hợp",
         "content": ("Căn cứ vào mối quan hệ giữa biến động chi phí và mức độ hoạt động (sản lượng, số giờ máy, doanh thu), chi phí được phân thành:\n"
                     "(1) Chi phí biến đổi (Biến phí - Variable Costs): Là những chi phí có tổng số thay đổi tỷ lệ thuận với mức độ hoạt động "
                     "(ví dụ: Chi phí nguyên vật liệu trực tiếp, hoa hồng bán hàng). Tuy nhiên, biến phí tính trên một đơn vị sản phẩm là một hằng số cố định.\n\n"
                     "(2) Chi phí cố định (Định phí - Fixed Costs): Là những chi phí mà tổng số không thay đổi khi mức độ hoạt động thay đổi trong phạm vi phù hợp "
                     "(ví dụ: Chi phí khấu hao TSCĐ theo đường thẳng, lương ban quản lý, tiền thuê nhà xưởng). "
                     "Định phí trên một đơn vị sản phẩm sẽ giảm dần khi sản lượng sản xuất tăng lên (hiệu quả kinh tế nhờ quy mô).\n\n"
                     "(3) Chi phí hỗn hợp (Mixed Costs): Chứa đựng cả yếu tố biến phí và định phí (ví dụ: Chi phí điện thoại, bảo dưỡng máy móc)."),
         "formulas": ["Phương trình đường chi phí tổng quát: Y = a + b * X",
                      "Trong đó: Y là Tổng chi phí; a là Tổng định phí; b là Biến phí đơn vị; X là Mức độ hoạt động"],
         "case_studies": [{"title": "Công ty Cổ phần Xi măng Hà Tiên 1 (HT1)", "detail": "Phân tích cấu trúc chi phí điện năng và nhiệt năng trong các lò nung clinker theo sản lượng sản xuất xi măng hàng tháng."}]},
        {"sec_num": 2, "sec_title": "Các Phương Pháp Phân Tách Chi Phí Hỗn Hợp",
         "content": ("Để lập kế hoạch chi phí, người quản lý phải phân tách chi phí hỗn hợp thành định phí (a) và biến phí đơn vị (b):\n"
                     "(1) Phương pháp Cực trị (High-Low Method): Dựa vào kỳ có mức độ hoạt động cao nhất và thấp nhất:\n"
                     "b = (Chi phí tại điểm cao nhất - Chi phí tại điểm thấp nhất) / (Mức hoạt động cao nhất - Mức hoạt động thấp nhất)\n"
                     "a = Chi phí tại điểm cực trị - (b x Mức hoạt động tại điểm cực trị)\n\n"
                     "(2) Phương pháp Hồi quy Tuyến tính Bình phương bé nhất (OLS Method): "
                     "Sử dụng toàn bộ các quan sát trong quá khứ để tìm đường hồi quy tối thiểu hóa tổng bình phương sai số. "
                     "Đây là phương pháp có độ tin cậy và chuẩn mực học thuật thống kê cao nhất."),
         "formulas": ["Biến phí đơn vị (OLS): b = [N * ∑(XY) - ∑X * ∑Y] / [N * ∑(X^2) - (∑X)^2]",
                      "Định phí (OLS): a = (∑Y - b * ∑X) / N",
                      "Hệ số xác định R^2 = Tỷ lệ phần trăm biến thiên của chi phí được giải thích bởi mức độ hoạt động"],
         "case_studies": [{"title": "Tổng Công ty Khí Việt Nam (PV GAS)", "detail": "Ứng dụng mô hình hồi quy phân tách chi phí vận hành và bảo dưỡng hệ thống đường ống dẫn khí Nam Côn Sơn theo lưu lượng khí truyền dẫn."}]}
    ]
    phd2 = {
        "topics": [
            "Hiện tượng Chi phí 'Dính' (Cost Stickiness - Anderson, Banker & Janakiraman 2003): Lý thuyết giải thích tại sao chi phí tăng nhiều hơn khi hoạt động tăng, nhưng lại giảm ít hơn khi mức độ hoạt động giảm tương ứng (Asymmetric Cost Behavior).",
            "Động cơ của các Nhà Quản trị đằng sau Hành vi Chi phí Dính: Quyết định giữ lại các nguồn lực dư thừa do kỳ vọng nhu cầu hồi phục hoặc do tư lợi cá nhân (Empire Building) và rủi ro chi phí đại diện.",
            "Chuyên đề Tiến sĩ: Mô hình hóa hiện tượng Cost Stickiness tại các doanh nghiệp niêm yết trên thị trường chứng khoán Việt Nam trong các giai đoạn khủng hoảng chu kỳ kinh tế."
        ]
    }
    q2 = [
        "Phân biệt đặc điểm biến thiên của Tổng biến phí và Biến phí đơn vị; Tổng định phí và Định phí đơn vị khi mức độ hoạt động gia tăng.",
        "Trình bày các bước thực hiện phân tách chi phí hỗn hợp bằng phương pháp Cực trị (High-Low Method) và nêu rõ nhược điểm của phương pháp này.",
        "Phân tích hiện tượng Chi phí Dính (Cost Stickiness) và giải thích nguyên nhân tại sao ban điều hành không thể cắt giảm chi phí ngay lập tức khi doanh thu sụt giảm."
    ]
    b.add_chapter(2, "Phân loại Chi phí và Mô hình Ứng xử của Chi phí", intro2, sec2, phd2, q2)
    
    # Chương 3
    intro3 = ("Chương 3 đi sâu vào phân tích mối quan hệ tương hỗ giữa Chi phí - Khối lượng - Lợi nhuận (CVP Analysis). "
              "Đây là một trong những công cụ toán kinh tế quyền lực nhất giúp nhà quản trị tối ưu hóa quy mô và điểm hòa vốn.")
    sec3 = [
        {"sec_num": 1, "sec_title": "Xác Định Điểm Hòa Vốn và Số Dư Đảm Nhiệm",
         "content": ("Số dư đảm nhiệm (Contribution Margin - CM) là phần chênh lệch giữa Doanh thu và Chi phí biến đổi. "
                     "Số dư đảm nhiệm trước hết bù đắp toàn bộ Chi phí cố định (Định phí), phần dôi ra sau khi đã bù đắp định phí chính là Lợi nhuận thuần của doanh nghiệp.\n\n"
                     "Điểm hòa vốn (Break-Even Point - BEP) là điểm mà tại đó Tổng doanh thu bằng Tổng chi phí, "
                     "nghĩa là Lợi nhuận kinh doanh bằng 0, hoặc Tổng số dư đảm nhiệm vừa vặn bù đắp Tổng định phí.\n"
                     "Doanh nghiệp có thể xác định sản lượng hòa vốn hoặc doanh thu hòa vốn. "
                     "Ngoài ra, doanh nghiệp xác định sản lượng cần thiết để đạt mức lợi nhuận mục tiêu mong muốn."),
         "formulas": ["Số dư đảm nhiệm đơn vị (cm) = Giá bán đơn vị (p) - Biến phí đơn vị (b)",
                      "Tỷ lệ số dư đảm nhiệm (CM Ratio) = cm / p = Tổng số dư đảm nhiệm / Tổng doanh thu",
                      "Sản lượng hòa vốn (Q_BEP) = Tổng định phí (FC) / cm",
                      "Doanh thu hòa vốn (TR_BEP) = Tổng định phí (FC) / CM Ratio",
                      "Sản lượng đạt lợi nhuận mục tiêu = (FC + Lợi nhuận mục tiêu trước thuế) / cm"],
         "case_studies": [{"title": "Hãng hàng không Bamboo Airways", "detail": "Tính toán hệ số lấp đầy ghế bình quân (Seat Load Factor) để đạt điểm hòa vốn cho từng chặng bay nội địa và quốc tế."}]},
        {"sec_num": 2, "sec_title": "Độ An Toàn và Đòn Bẩy Hoạt Động (DOL)",
         "content": ("- Mức doanh thu an toàn (Margin of Safety - MoS) phản ánh khoảng cách an toàn giữa Doanh thu thực tế (hoặc dự kiến) với Doanh thu hòa vốn. "
                     "Tỷ lệ doanh thu an toàn càng cao thì mức độ rủi ro kinh doanh thua lỗ càng thấp.\n\n"
                     "- Đòn bẩy hoạt động (Degree of Operating Leverage - DOL) đo lường mức độ nhạy cảm của Lợi nhuận hoạt động (EBIT) "
                     "trước sự biến thiên của Doanh thu. Doanh nghiệp có tỷ trọng định phí cao (sử dụng nhiều máy móc tự động hóa) "
                     "sẽ có DOL rất lớn: Chỉ cần doanh thu tăng nhẹ thì lợi nhuận sẽ tăng vọt, "
                     "nhưng ngược lại nếu doanh thu giảm sút thì nguy cơ rơi vào thua lỗ nặng nề là rất cao."),
         "formulas": ["Doanh thu an toàn = Doanh thu thực hiện - Doanh thu hòa vốn",
                      "Tỷ lệ doanh thu an toàn = Doanh thu an toàn / Doanh thu thực hiện",
                      "Độ lớn đòn bẩy hoạt động: DOL = Tổng số dư đảm nhiệm (CM) / Lợi nhuận thuần trước thuế (EBIT)",
                      "% Thay đổi của Lợi nhuận EBIT = DOL x % Thay đổi của Doanh thu"],
         "case_studies": [{"title": "Tập đoàn Thép Hòa Phát (HPG)", "detail": "Phân tích đòn bẩy hoạt động cực cao tại Khu liên hợp Dung Quất với chi phí khấu hao hàng nghìn tỷ đồng mỗi năm và ảnh hưởng khuếch đại lợi nhuận theo chu kỳ giá thép."}]}
    ]
    phd3 = {
        "topics": [
            "Mô hình CVP trong Điều kiện Bất định (CVP Analysis under Uncertainty - Jaedicke & Robichek 1964): Ứng dụng phân phối xác suất ngẫu nhiên và mô phỏng Monte Carlo để xác định xác suất hòa vốn khi cả giá bán và biến phí đều biến động.",
            "Phân tích Đánh đổi giữa Rủi ro Hoạt động (Operating Leverage) và Rủi ro Tài chính (Financial Leverage): Mô hình tổng hợp DTL (Degree of Total Leverage = DOL x DFL) và cấu trúc tối ưu của doanh nghiệp.",
            "Chuyên đề Tiến sĩ: Đánh giá độ co giãn của lợi nhuận hoạt động và rủi ro sụt giảm dòng tiền của các doanh nghiệp niêm yết có đòn bẩy hoạt động cao trong bối cảnh cú sốc lãi suất toàn cầu."
        ]
    }
    q3 = [
        "Trình bày các giả định cơ bản của mô hình phân tích Chi phí - Khối lượng - Lợi nhuận (CVP). Nêu rõ những hạn chế của các giả định này trong thực tiễn kinh doanh.",
        "Công thức tính Điểm hòa vốn trong trường hợp doanh nghiệp sản xuất và kinh doanh nhiều dòng sản phẩm khác nhau (phương pháp cơ cấu sản phẩm kết hợp).",
        "Định nghĩa và ý nghĩa kinh tế của Độ lớn đòn bẩy hoạt động (DOL). Tại sao doanh nghiệp có tỷ trọng định phí cao lại phải đối mặt với rủi ro hoạt động lớn?"
    ]
    b.add_chapter(3, "Phân tích Mối quan hệ Chi phí - Khối lượng - Lợi nhuận (CVP)", intro3, sec3, phd3, q3)
    
    # Chương 4
    intro4 = ("Chương 4 nghiên cứu hệ thống dự toán ngân sách toàn diện doanh nghiệp (Master Budget). "
              "Đây là kế hoạch hành động bằng tiền bao quát toàn bộ các hoạt động sản xuất, tiêu thụ và tài chính trong niên độ kế toán.")
    sec4 = [
        {"sec_num": 1, "sec_title": "Quy Trình Xây Dựng Dự Toán Hoạt Động Doanh Nghiệp",
         "content": ("Dự toán toàn diện (Master Budget) là mạng lưới các dự toán bộ phận có mối quan hệ phụ thuộc lẫn nhau một cách chặt chẽ. "
                     "Điểm khởi đầu bắt buộc của toàn bộ chu trình dự toán là Dự toán Tiêu thụ (Sales Budget) - căn cứ vào dự báo thị trường và đơn đặt hàng.\n\n"
                     "Quy trình luân chuyển dự toán sản xuất kinh doanh:\n"
                     "(1) Dự toán Tiêu thụ -> (2) Dự toán Sản xuất (căn cứ nhu cầu bán và tồn kho dự kiến) -> "
                     "(3) Dự toán Chi phí Nguyên vật liệu trực tiếp, Dự toán Chi phí Nhân công trực tiếp, Dự toán Chi phí Sản xuất chung -> "
                     "(4) Dự toán Giá thành sản phẩm và Tồn kho thành phẩm cuối kỳ -> "
                     "(5) Dự toán Chi phí Bán hàng và Quản lý doanh nghiệp."),
         "formulas": ["Sản lượng sản xuất cần thiết = Sản lượng tiêu thụ dự kiến + Tồn kho thành phẩm cuối kỳ mong muốn - Tồn kho thành phẩm đầu kỳ",
                      "Số lượng NVL cần mua = Nhu cầu NVL cho sản xuất + Dự trữ NVL cuối kỳ mong muốn - Dự trữ NVL đầu kỳ"],
         "case_studies": [{"title": "Công ty Cổ phần Sữa Việt Nam (Vinamilk - VNM)", "detail": "Quy trình lập dự toán sản xuất chuỗi cung ứng sữa bột và sữa chua dựa trên dự báo tiêu thụ theo mùa vụ và ngày khai giảng trường học."}]},
        {"sec_num": 2, "sec_title": "Dự Toán Tài Chính và Dự Toán Linh Hoạt (Flexible Budget)",
         "content": ("Dự toán tài chính tổng hợp toàn bộ các dòng tiền và cấu trúc tài sản: Dự toán Tiền mặt (Cash Budget), "
                     "Báo cáo Kết quả kinh doanh dự toán và Bảng Cân đối kế toán dự toán.\n\n"
                     "Dự toán tiền mặt gồm 4 phần chính: (1) Số dư tiền đầu kỳ; (2) Dòng tiền thu dự kiến (thu tiền bán hàng, thu nợ); "
                     "(3) Dòng tiền chi dự kiến (mua NVL, trả lương, chi phí quản lý, nộp thuế, mua sắm TSCĐ); "
                     "(4) Cân đối thừa/thiếu tiền và phương án tài trợ vốn vay ngắn hạn ngân hàng.\n\n"
                     "Dự toán linh hoạt (Flexible Budget) là dự toán được điều chỉnh tự động tương ứng với các mức sản lượng hoạt động thực tế đạt được, "
                     "giúp ban giám đốc so sánh chính xác chênh lệch giá và chênh lệch lượng mà không bị sai lệch bởi chênh lệch quy mô sản xuất."),
         "formulas": ["Số dư tiền cuối kỳ = Tiền đầu kỳ + Dòng tiền thu trong kỳ - Dòng tiền chi trong kỳ +/- Dòng tiền vay/trả nợ tài chính",
                      "Biến động dự toán linh hoạt (Flexible Budget Variance) = Kết quả thực tế - Dự toán linh hoạt tính theo sản lượng thực tế"],
         "case_studies": [{"title": "Tập đoàn Dệt may Việt Nam (Vinatex)", "detail": "Áp dụng dự toán linh hoạt kiểm soát chi phí nhân công may công nghiệp khi các đơn hàng gia công FOB/CMT biến động thất thường."}]}
    ]
    phd4 = {
        "topics": [
            "Hành vi Độn Ngân sách và Rủi ro Bất cân xứng Thông tin (Budgetary Slack & Information Asymmetry - Dunk 1993): Động cơ của các nhà quản lý cấp cơ sở cố tình khai tăng chi phí dự toán và hạ thấp chỉ tiêu doanh thu để dễ dàng đạt thưởng vượt mức kế hoạch.",
            "Mô hình Ngân sách Vượt trội (Beyond Budgeting Model - Hope & Fraser 2003): Phê phán những cứng nhắc của hệ thống dự toán truyền thống hàng năm và sự chuyển dịch sang các mục tiêu co giãn tương đối (Relative Performance Targets) và dự báo cuộn (Rolling Forecasts).",
            "Chuyên đề Tiến sĩ: Nghiên cứu tác động của mức độ tham gia lập dự toán (Budgetary Participation) đến sự gắn kết tổ chức và hiệu quả công việc tại các doanh nghiệp có vốn đầu tư nước ngoài (FDI)."
        ]
    }
    q4 = [
        "Mô tả trình tự logic các bước lập hệ thống dự toán toàn diện (Master Budget) từ Dự toán tiêu thụ đến Báo cáo tài chính dự toán.",
        "Trình bày cấu trúc chi tiết của một Dự toán Tiền mặt (Cash Budget) và ý nghĩa của việc duy trì mức dự trữ tiền mặt an toàn tối thiểu.",
        "Tại sao việc so sánh Chi phí thực tế với Dự toán tĩnh (Static Budget) có thể dẫn đến những đánh giá sai lệch về hiệu quả quản lý chi phí? Phân tích ưu thế của Dự toán linh hoạt."
    ]
    b.add_chapter(4, "Dự toán Toàn diện Hoạt động Doanh nghiệp (Master Budget)", intro4, sec4, phd4, q4)
    
    # Chương 5
    intro5 = ("Chương 5 trang bị phương pháp luận nhận diện và sử dụng thông tin thích hợp trong việc ra quyết định kinh doanh ngắn hạn. "
              "Kỹ năng này giúp nhà quản trị ra các quyết định sáng suốt về đơn đặt hàng, gia công ngoài hay tái cấu trúc sản phẩm.")
    sec5 = [
        {"sec_num": 1, "sec_title": "Bản Chất của Thông Tin Thích Hợp và Chi Phí Cơ Hội",
         "content": ("Thông tin thích hợp (Relevant Information) là những dòng tiền doanh thu và chi phí thỏa mãn đồng thời hai điều kiện: "
                     "(1) Là thông tin phát sinh trong tương lai; (2) Có sự khác biệt giữa các phương án kinh doanh đang được cân nhắc lựa chọn.\n\n"
                     "Hai khái niệm loại trừ quan trọng:\n"
                     "- Chi phí chìm (Sunk Cost): Là những chi phí đã phát sinh trong quá khứ và không thể thay đổi được dù lựa chọn bất kỳ phương án nào "
                     "(ví dụ: Giá trị còn lại của máy móc cũ đã mua, chi phí R&D đã bỏ ra). Chi phí chìm hoàn toàn KHÔNG THÍCH HỢP cho việc ra quyết định.\n"
                     "- Chi phí cơ hội (Opportunity Cost): Là lợi ích kinh tế tiềm năng bị mất đi khi lựa chọn phương án này thay vì phương án tốt nhất khác. "
                     "Chi phí cơ hội luôn luôn là thông tin thích hợp và phải được tính vào chi phí của phương án lựa chọn."),
         "formulas": ["Lợi ích thuần của phương án = Tổng doanh thu thích hợp - Tổng chi phí thích hợp - Chi phí cơ hội",
                      "Tiêu chí quyết định: Chọn phương án có Chênh lệch Số dư đảm nhiệm tăng thêm > 0"],
         "case_studies": [{"title": "Công ty Cổ phần Pin Hà Nội (Habaco - PHN)", "detail": "Đánh giá chi phí cơ hội của việc sử dụng mặt bằng kho bãi nhàn rỗi để tự sản xuất vỏ pin hay cho thuê văn phòng bên ngoài."}]},
        {"sec_num": 2, "sec_title": "Các Quyết Định Quản Trị Ngắn Hạn Điển Hình",
         "content": ("(1) Quyết định Đơn đặt hàng đặc biệt (Special Order): Chấp nhận đơn hàng với giá bán thấp hơn giá thông thường khi công ty còn công suất nhàn rỗi "
                     "nếu: Giá bán đơn hàng > Biến phí đơn vị + Chi phí phát sinh riêng của đơn hàng.\n\n"
                     "(2) Quyết định Tự sản xuất hay Mua ngoài (Make-or-Buy Decision): So sánh Chi phí biến đổi tự sản xuất + Định phí riêng biệt có thể tránh được "
                     "với Giá mua chào hàng từ nhà cung cấp bên ngoài (kèm xem xét yếu tố chất lượng và rủi ro gián đoạn chuỗi cung ứng).\n\n"
                     "(3) Quyết định Loại bỏ hay Giữ lại phân xưởng/dòng sản phẩm thua lỗ: Phân xưởng có lãi ròng âm chỉ nên bị đóng cửa "
                     "nếu Số dư đảm nhiệm (CM) của nó nhỏ hơn Định phí có thể tránh được khi đóng cửa. "
                     "Nếu định phí là chi phí chung phân bổ không thể tránh được thì việc đóng cửa sẽ làm lợi nhuận chung của toàn công ty sụt giảm thêm.\n\n"
                     "(4) Quyết định Bán ngay hay Tiếp tục chế biến (Sell or Process Further): So sánh Doanh thu tăng thêm sau khi chế biến với Chi phí chế biến thêm riêng biệt."),
         "formulas": ["Chênh lệch đơn hàng đặc biệt = Sản lượng đặt hàng x (Giá chào mua đặc biệt - Biến phí đơn vị) - Chi phí khuôn mẫu riêng",
                      "Chi phí tránh được khi đóng cửa = Định phí trực tiếp riêng biệt bị triệt tiêu khi ngừng kinh doanh"],
         "case_studies": [{"title": "Công ty Cổ phần Thủy sản Vĩnh Hoàn (VHC)", "detail": "Quyết định chế biến sâu phụ phẩm da cá và mỡ cá tra thành Collagen và Gelatin xuất khẩu giá trị cao thay vì bán ngay cá phế liệu thô."}]}
    ]
    phd5 = {
        "topics": [
            "Định giá Mục tiêu (Target Costing) và Kỹ thuật Giá trị (Value Engineering - Cooper & Slagmulder 1997): Phương pháp quản trị chi phí ngược từ giá thị trường chấp nhận được trong chu kỳ phát triển sản phẩm mới.",
            "Lý thuyết Điểm nghẽn Ràng buộc (Theory of Constraints - TOC & Throughput Accounting - Goldratt 1984): Tối đa hóa tỷ suất Số dư thông lượng trên mỗi đơn vị nguồn lực khan hiếm (Throughput per Constraint Unit).",
            "Chuyên đề Tiến sĩ: Nghiên cứu các bẫy tâm lý hành vi (Cognitive Biases - Escalation of Commitment) khi nhà điều hành tiếp tục rót vốn vào các dự án thua lỗ do ảnh hưởng của chi phí chìm."
        ]
    }
    q5 = [
        "Định nghĩa Thông tin thích hợp (Relevant Information). Tại sao Chi phí chìm không bao giờ được coi là thông tin thích hợp trong việc ra quyết định kinh doanh?",
        "Phân tích điều kiện để một doanh nghiệp chấp nhận một Đơn đặt hàng đặc biệt có mức giá bán thấp hơn giá bán niêm yết hiện hành.",
        "Trình bày phương pháp phân tích quyết định 'Tự sản xuất hay Mua ngoài' (Make or Buy) và các yếu tố phi tài chính cần cân nhắc trước khi ra quyết định."
    ]
    b.add_chapter(5, "Thông tin Thích hợp cho Ra Quyết định Quản trị Ngắn hạn", intro5, sec5, phd5, q5)
    
    # Chương 6
    intro6 = ("Chương 6 nghiên cứu tổ chức kế toán quản trị trách nhiệm và đo lường thành quả hoạt động. "
              "Hệ thống giúp căn chỉnh mục tiêu cá nhân của các nhà quản lý bộ phận với mục tiêu chiến lược của tổ chức.")
    sec6 = [
        {"sec_num": 1, "sec_title": "Các Trung Tâm Trách Nhiệm và Thước Đo Đánh Giá",
         "content": ("Doanh nghiệp phân quyền quản lý theo 4 loại Trung tâm Trách nhiệm (Responsibility Centers):\n"
                     "(1) Trung tâm Chi phí (Cost Center): Nhà quản lý chỉ chịu trách nhiệm kiểm soát chi phí (phân xưởng sản xuất, phòng kế toán).\n"
                     "(2) Trung tâm Doanh thu (Revenue Center): Nhà quản lý chịu trách nhiệm về doanh thu bán hàng (phòng kinh doanh, chi nhánh).\n"
                     "(3) Trung tâm Lợi nhuận (Profit Center): Nhà quản lý chịu trách nhiệm cả về doanh thu và chi phí phát sinh (nhà máy tự hạch toán).\n"
                     "(4) Trung tâm Đầu tư (Investment Center): Nhà quản lý chịu trách nhiệm về doanh thu, chi phí và hiệu quả sử dụng vốn đầu tư (công ty con, khối kinh doanh chiến lược SBU).\n\n"
                     "Hai thước đo tài chính kinh điển cho trung tâm đầu tư:\n"
                     "- Tỷ suất sinh lời trên vốn đầu tư (ROI - Return on Investment) = Lợi nhuận hoạt động thuần / Tài sản hoạt động bình quân.\n"
                     "- Lợi nhuận thặng dư (RI - Residual Income) = Lợi nhuận hoạt động thuần - (Tài sản hoạt động x Tỷ suất sinh lời tối thiểu)."),
         "formulas": ["ROI = (Lợi nhuận / Doanh thu) x (Doanh thu / Tài sản) = Tỷ suất lợi nhuận trên doanh thu (Margin) x Vòng quay tài sản (Turnover)",
                      "RI = EBIT - (Tài sản hoạt động x WACC)",
                      "Giá trị gia tăng kinh tế: EVA = NOPAT - (Vốn đầu tư x WACC)"],
         "case_studies": [{"title": "Tập đoàn FPT", "detail": "Phân chia các khối kinh doanh Viễn thông, Công nghệ phần mềm và Giáo dục thành các trung tâm đầu tư độc lập và đánh giá thành quả dựa trên EVA và OKR."}]},
        {"sec_num": 2, "sec_title": "Thẻ Điểm Cân Bằng (Balanced Scorecard) và Giá Chuyển Nhượng Nội Bộ",
         "content": ("Thẻ điểm cân bằng (BSC - Kaplan & Norton) chuyển đổi tầm nhìn chiến lược thành hệ thống mục tiêu đo lường trên 4 viễn cảnh:\n"
                     "(1) Viễn cảnh Tài chính (ROI, EVA, tăng trưởng doanh thu);\n"
                     "(2) Viễn cảnh Khách hàng (Sự hài lòng, mức độ trung thành, thị phần);\n"
                     "(3) Viễn cảnh Quy trình nội bộ (Thời gian chu kỳ sản xuất, chất lượng sản phẩm, đổi mới sáng tạo);\n"
                     "(4) Viễn cảnh Học hỏi và Phát triển (Năng lực nhân viên, hệ thống thông tin, văn hóa tổ chức).\n\n"
                     "Định giá chuyển nhượng nội bộ (Transfer Pricing) giữa các bộ phận trong tập đoàn có thể căn cứ theo:\n"
                     "- Giá thị trường (Market-based Price): Tối ưu nhất khi tồn tại thị trường cạnh tranh hoàn hảo bên ngoài.\n"
                     "- Giá dựa trên chi phí (Cost-based Price): Biến phí, Giá thành sản xuất toàn bộ, hoặc Chi phí cộng lãi.\n"
                     "- Giá thương lượng (Negotiated Price): Thỏa thuận tự nguyện giữa người bán và người mua nội bộ."),
         "formulas": ["Quy tắc giá chuyển nhượng tối thiểu (Bên bán) = Biến phí đơn vị + Chi phí cơ hội trên mỗi đơn vị chuyển nhượng",
                      "Giá chuyển nhượng tối đa (Bên mua) = Min(Giá mua thị trường bên ngoài, Doanh thu cận biên của bên mua)"],
         "case_studies": [{"title": "Công ty Cổ phần Ô tô Trường Hải (THACO)", "detail": "Thiết lập cơ chế giá chuyển nhượng nội bộ giữa Nhà máy Cơ khí chế tạo và Nhà máy Lắp ráp ô tô Bus, Tải tại Chu Lai Open Economic Zone."}]}
    ]
    phd6 = {
        "topics": [
            "Lý thuyết Căn chỉnh Mục tiêu và Thước đo Đánh giá (Goal Congruence & Performance Evaluation - Hopwood 1972): Phân tích xung đột giữa việc sử dụng chỉ số ROI (có thể khiến nhà quản lý từ chối các dự án sinh lời cho tập đoàn nhưng thấp hơn ROI hiện tại của bộ phận) và chỉ số RI.",
            "Lý thuyết Đại diện và Động cơ Định giá Chuyển nhượng (Transfer Pricing & Tax Arbitrage): Sử dụng định giá chuyển nhượng xuyên biên giới để chuyển dịch lợi nhuận về các thiên đường thuế và chiến lược chống xói mòn cơ sở thuế (BEPS).",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về vai trò điều tiết của Thẻ điểm cân bằng (BSC) đối với mối quan hệ giữa Chiến lược định hướng thị trường và Hiệu quả tài chính tại các doanh nghiệp Việt Nam."
        ]
    }
    q6 = [
        "Phân biệt 4 loại trung tâm trách nhiệm trong doanh nghiệp: Trung tâm chi phí, doanh thu, lợi nhuận và đầu tư.",
        "So sánh ưu điểm và nhược điểm của hai thước đo thành quả tài chính: Tỷ suất sinh lời trên vốn đầu tư (ROI) và Lợi nhuận thặng dư (RI). Cho ví dụ minh họa.",
        "Trình bày 4 viễn cảnh của Thẻ điểm cân bằng (Balanced Scorecard) và giải thích mối quan hệ nhân quả (Cause-and-effect relationship) giữa các viễn cảnh."
    ]
    b.add_chapter(6, "Kế toán Quản trị Trách nhiệm và Đánh giá Thành quả", intro6, sec6, phd6, q6)
    
    out_dir = os.path.join(BASE_DIR, r"02_Kế toán & Kiểm toán\[NEU] Kế toán quản trị - PGS.TS Trương Bá Thanh (NXB ĐHKTQD)")
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Kế toán quản trị - PGS.TS Trương Bá Thanh (NXB ĐHKTQD).pdf")
    pages, size_mb = b.save(out_pdf)
    print(f"-> Hoàn thành Sách 4: {pages} trang, {size_mb:.2f} MB. Lưu tại: {out_pdf}")
    return {"book": "Kế toán quản trị", "pages": pages, "size_mb": size_mb, "path": out_pdf}


def build_book_5():
    print("--- Đang biên soạn Sách 5: Kiểm toán căn bản ---")
    title = "Kiểm toán Căn bản"
    code = "KTKT1108"
    faculty = "Viện Kế toán - Kiểm toán"
    authors = "GS.TS. Nguyễn Quang Quynh (Chủ biên), PGS.TS. Ngô Trí Tuệ, TS. Bùi Thị Minh Hải"
    
    b = NEUTextbookBuilder(title, code, faculty, authors)
    b.build_cover()
    
    toc = [
        {"chapter_num": 1, "chapter_title": "Bản chất, Chức năng và Đối tượng của Kiểm toán",
         "topics": ["Nguồn gốc lịch sử hình thành và sự cần thiết khách quan của kiểm toán", "Bản chất, chức năng và vai trò của kiểm toán trong nền kinh tế thị trường", "Phân loại kiểm toán theo chủ thể (Độc lập, Nhà nước, Nội bộ) và theo mục đích", "Khuôn khổ pháp lý và hệ thống chuẩn mực kiểm toán (VSA & ISA)"]},
        {"chapter_num": 2, "chapter_title": "Bằng chứng Kiểm toán và Phương pháp Thu thập",
         "topics": ["Khái niệm, đặc trưng bằng chứng kiểm toán: Đầy đủ và thích hợp (VSA 500)", "Cơ sở dẫn liệu của BCTC (Existence, Rights, Completeness, Valuation...)", "Các kỹ thuật thu thập bằng chứng kiểm toán (Kiểm tra, Quan sát, Xác nhận, Tính toán, Phân tích)", "Hồ sơ kiểm toán: Hồ sơ chung và hồ sơ năm hiện hành (VSA 230)"]},
        {"chapter_num": 3, "chapter_title": "Trọng yếu và Rủi ro trong Kiểm toán",
         "topics": ["Khái niệm mức trọng yếu (Materiality) và các cấp độ xác định (VSA 320)", "Trọng yếu tổng thể và trọng yếu thực hiện (Performance Materiality)", "Mô hình rủi ro kiểm toán: AR = IR x CR x DR", "Đánh giá rủi ro tiềm tàng (IR) và rủi ro kiểm soát (CR)"]},
        {"chapter_num": 4, "chapter_title": "Hệ thống Kiểm soát Nội bộ và Đánh giá Rủi ro",
         "topics": ["Khái niệm và mục tiêu của Hệ thống kiểm soát nội bộ (Khuôn khổ COSO)", "5 bộ phận cấu thành KSNB: Môi trường, Đánh giá rủi ro, Hoạt động KS, Thông tin & Giám sát", "Quy trình tìm hiểu và đánh giá sơ bộ hệ thống KSNB của khách hàng", "Thử nghiệm kiểm soát (Tests of Controls) và thử nghiệm cơ bản (Substantive Tests)"]},
        {"chapter_num": 5, "chapter_title": "Phương pháp Kiểm toán và Lấy mẫu Kiểm toán",
         "topics": ["Phương pháp kiểm toán chứng từ và phương pháp kiểm toán ngoài chứng từ", "Thủ tục phân tích (Analytical Procedures - VSA 520) trong các giai đoạn kiểm toán", "Lấy mẫu kiểm toán thống kê và phi thống kê (VSA 530)", "Lấy mẫu theo đơn vị tiền tệ (MUS) và đánh giá kết quả kiểm toán mẫu"]},
        {"chapter_num": 6, "chapter_title": "Báo cáo Kiểm toán và Đạo đức Nghề nghiệp",
         "topics": ["Bản chất, ý nghĩa và cấu trúc Báo cáo kiểm toán chuẩn mực (VSA 700)", "Các loại ý kiến kiểm toán (Chấp nhận toàn phần, Ngoại trừ, Trái ngược, Từ chối - VSA 705)", "Vấn đề kiểm toán trọng yếu (KAM - Key Audit Matters theo ISA 701)", "Quy tắc đạo đức nghề nghiệp kiểm toán viên theo IFAC Code of Ethics"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chương 1
    intro1 = ("Chương 1 giới thiệu nguồn gốc phát sinh và bản chất của hoạt động kiểm toán trong nền kinh tế. "
              "Chương này giúp người học hiểu rõ sự phân kỳ của kiểm toán độc lập, kiểm toán nhà nước và kiểm toán nội bộ.")
    sec1 = [
        {"sec_num": 1, "sec_title": "Nguồn Gốc và Bản Chất của Hoạt Động Kiểm Toán",
         "content": ("Kiểm toán ra đời từ sự phân tách giữa quyền sở hữu và quyền quản lý điều hành kinh doanh (Lý thuyết Đại diện - Agency Theory). "
                     "Khi các chủ sở hữu (cổ đông) ủy thác tài sản cho các nhà quản lý điều hành, nhu cầu về một bên thứ ba độc lập, "
                     "có năng lực chuyên môn để xác minh tính trung thực và hợp lý của các báo cáo tài chính trở thành một đòi hỏi khách quan tất yếu.\n\n"
                     "Kiểm toán là quá trình các kiểm toán viên độc lập thu thập và đánh giá các bằng chứng về các thông tin có thể định lượng "
                     "của một thực thể kinh tế cụ thể nhằm xác nhận và báo cáo về mức độ phù hợp giữa các thông tin đó với các chuẩn mực đã được thiết lập (VAS/IFRS).\n\n"
                     "Ba loại hình kiểm toán chủ yếu theo mục đích:\n"
                     "(1) Kiểm toán Báo cáo tài chính: Đánh giá tính trung thực và hợp lý của BCTC.\n"
                     "(2) Kiểm toán Tuân thủ: Đánh giá mức độ chấp hành luật pháp, quy chế, chính sách nội bộ.\n"
                     "(3) Kiểm toán Hoạt động: Đánh giá tính kinh tế (Economy), hiệu quả (Efficiency) và hiệu lực (Effectiveness) của hoạt động quản lý."),
         "formulas": ["Tam giác kiểm toán (The Audit Triangle): Đơn vị được kiểm toán <-> Kiểm toán viên <-> Người sử dụng thông tin BCTC",
                      "Mô hình chất lượng 3E: Kinh tế (Chi phí thấp nhất) + Hiệu quả (Đầu ra tối đa trên đầu vào) + Hiệu lực (Đạt mục tiêu)"],
         "case_studies": [{"title": "Vụ sụp đổ của Tập đoàn Enron và Arthur Andersen (2001)", "detail": "Bài học lịch sử dẫn đến sự ra đời của Đạo luật Sarbanes-Oxley (SOX 2002) tái định hình toàn bộ ngành kiểm toán độc lập toàn cầu."}]},
        {"sec_num": 2, "sec_title": "Phân Loại Kiểm Toán Theo Chủ Thể Thực Hiện",
         "content": ("Căn cứ vào chủ thể tiến hành, kiểm toán được phân định thành ba nhánh độc lập:\n"
                     "(1) Kiểm toán Độc lập (Independent Audit): Do các kiểm toán viên chuyên nghiệp thuộc các công ty kiểm toán độc lập thực hiện "
                     "(Big 4: PwC, EY, Deloitte, KPMG và các công ty kiểm toán phi Big 4). Mục tiêu chủ yếu là cung cấp dịch vụ kiểm toán BCTC và dịch vụ đảm bảo có thu phí.\n\n"
                     "(2) Kiểm toán Nhà nước (State Audit): Do cơ quan Kiểm toán Nhà nước (SAV) thực hiện theo Luật Kiểm toán Nhà nước, "
                     "hoạt động nhân danh Quốc hội để kiểm toán việc quản lý, sử dụng tài chính công và tài sản công của các cơ quan nhà nước, doanh nghiệp nhà nước.\n\n"
                     "(3) Kiểm toán Nội bộ (Internal Audit): Do các kiểm toán viên thuộc biên chế của chính đơn vị thực hiện, "
                     "báo cáo trực tiếp lên Ủy ban Kiểm toán trực thuộc Hội đồng Quản trị nhằm đánh giá hệ thống quản trị rủi ro và kiểm soát nội bộ."),
         "formulas": ["Tính độc lập của KTV: Độc lập về tư tưởng (Independence of Mind) + Độc lập về hình thức (Independence in Appearance)"],
         "case_studies": [{"title": "Kiểm toán Nhà nước Việt Nam kiểm toán Ngân sách Thành phố Hà Nội", "detail": "Đánh giá việc phân bổ vốn đầu tư công các dự án đường vành đai và các khoản thu tiền sử dụng đất phát sinh trên địa bàn."}]}
    ]
    phd1 = {
        "topics": [
            "Lý thuyết Đại diện và Vai trò Xác nhận Thông tin của Kiểm toán (Agency Theory & Information Assurance - Jensen & Meckling 1976): Kiểm toán như một cơ chế giám sát ngoại sinh làm giảm thiểu chi phí đại diện và rủi ro đạo đức (Moral Hazard) của ban điều hành.",
            "Lý thuyết Cung cầu Dịch vụ Kiểm toán (Signaling & Insurance Hypothesis - Wallace 1980): Doanh nghiệp lựa chọn kiểm toán chất lượng cao (Big 4) để phát tín hiệu về chất lượng quản trị và bảo hiểm rủi ro pháp lý cho nhà đầu tư.",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về Phí kiểm toán phụ trội (Big 4 Audit Fee Premium) và mối quan hệ với chi phí vốn vay của các doanh nghiệp niêm yết tại các thị trường cận biên (Frontier Markets)."
        ]
    }
    q1 = [
        "Phân tích sự cần thiết khách quan của hoạt động kiểm toán trong nền kinh tế thị trường dựa trên Lý thuyết Đại diện (Agency Theory).",
        "Phân biệt mục tiêu, chủ thể thực hiện, tính pháp lý và người sử dụng kết quả giữa: Kiểm toán Độc lập, Kiểm toán Nhà nước và Kiểm toán Nội bộ.",
        "Trình bày 3 yêu cầu trong đánh giá hoạt động (Kinh tế - Hiệu quả - Hiệu lực) của kiểm toán hoạt động."
    ]
    b.add_chapter(1, "Bản chất, Chức năng và Đối tượng của Kiểm toán", intro1, sec1, phd1, q1)
    
    # Chương 2
    intro2 = ("Chương 2 nghiên cứu bản chất của bằng chứng kiểm toán và các cơ sở dẫn liệu của báo cáo tài chính. "
              "Đây là nền tảng cốt lõi định hướng mọi thủ tục thu thập thông tin và chứng minh ý kiến kiểm toán.")
    sec2 = [
        {"sec_num": 1, "sec_title": "Cơ Sở Dẫn Liệu và Yêu Cầu Bằng Chứng Kiểm Toán (VSA 500)",
         "content": ("Cơ sở dẫn liệu (Management Assertions) là các giải trình của Ban Giám đốc được thể hiện một cách trực tiếp "
                     "hoặc gián tiếp trong các Báo cáo tài chính. KTV sử dụng cơ sở dẫn liệu để xác định các rủi ro có sai sót trọng yếu:\n"
                     "(1) Cơ sở dẫn liệu đối với các nhóm giao dịch trong kỳ (KQKD): Tính hiện hữu/phát sinh (Occurrence); "
                     "Tính đầy đủ (Completeness); Tính chính xác (Accuracy); Đúng kỳ (Cut-off); Phân loại đúng (Classification).\n"
                     "(2) Cơ sở dẫn liệu đối với số dư tài khoản cuối kỳ (Bảng CĐKT): Tính hiện hữu (Existence); "
                     "Quyền và nghĩa vụ (Rights and Obligations); Tính đầy đủ (Completeness); Đánh giá và phân bổ (Valuation and Allocation).\n\n"
                     "Bằng chứng kiểm toán phải thỏa mãn hai tiêu chuẩn định lượng và định tính:\n"
                     "- Tính Đầy đủ (Sufficiency): Thước đo về số lượng bằng chứng (bị ảnh hưởng bởi mức độ rủi ro và chất lượng bằng chứng).\n"
                     "- Tính Thích hợp (Appropriateness): Thước đo về chất lượng bằng chứng, bao gồm Tính phù hợp (Relevance) và Độ tin cậy (Reliability)."),
         "formulas": ["Độ tin cậy của bằng chứng: Bằng chứng độc lập từ bên ngoài > Bằng chứng KTV tự thu thập trực tiếp > Bằng chứng do khách hàng cung cấp (hệ thống KSNB hữu hiệu > KSNB yếu kém) > Bằng chứng văn bản gốc > Bằng chứng photo/lời nói"],
         "case_studies": [{"title": "Kiểm toán Khoản mục Hàng tồn kho của Tập đoàn Thép Nam Kim", "detail": "Kiểm toán viên trực tiếp tham gia chứng kiến kiểm kê kho thực tế vào ngày 31/12 để thu thập bằng chứng về Tính hiện hữu (Existence) và Tình trạng phẩm chất của cuộn thép cán nguội."}]},
        {"sec_num": 2, "sec_title": "Các Kỹ Thuật Thu Thập Bằng Chứng và Hồ Sơ Kiểm Toán",
         "content": ("Theo Chuẩn mực kiểm toán Việt Nam VSA 500, KTV áp dụng 7 kỹ thuật thu thập bằng chứng cơ bản:\n"
                     "(1) Kiểm tra vật chất (Physical Inspection): Trực tiếp kiểm kê tài sản hữu hình (tiền mặt, TSCĐ, hàng tồn kho).\n"
                     "(2) Kiểm tra tài liệu chứng từ (Documentation Inspection): Đối chiếu chứng từ gốc với sổ sách (Vouching) "
                     "hoặc từ chứng từ gốc đi lên báo cáo (Tracing để kiểm tra tính đầy đủ).\n"
                     "(3) Quan sát (Observation): Theo dõi một quy trình hoạt động do nhân viên khách hàng thực hiện.\n"
                     "(4) Xác nhận từ bên ngoài (External Confirmation - VSA 505): Gửi thư xác nhận số dư tiền gửi ngân hàng, nợ phải thu, nợ phải trả đến bên thứ ba.\n"
                     "(5) Tính toán lại (Recalculation): Kiểm tra tính chính xác toán học của các bảng biểu, chi phí khấu hao.\n"
                     "(6) Thực hiện lại (Reperformance): KTV độc lập thực hiện lại các thủ tục kiểm soát.\n"
                     "(7) Thủ tục phân tích (Analytical Procedures): Đánh giá các tỷ số, so sánh xu hướng biến động dữ liệu.\n\n"
                     "Hồ sơ kiểm toán (VSA 230) gồm: Hồ sơ kiểm toán chung (lưu trữ thông tin pháp lý, điều lệ, mô hình kinh doanh dùng cho nhiều năm) "
                     "và Hồ sơ kiểm toán năm hiện hành (chương trình kiểm toán, giấy tờ làm việc Working Papers của niên độ kiểm toán hiện tại)."),
         "formulas": ["Thủ tục Vouching (Kiểm tra ngược từ Sổ -> Chứng từ): Kiểm định Tính hiện hữu (Phát hiện ghi khống)",
                      "Thủ tục Tracing (Kiểm tra xuôi từ Chứng từ -> Sổ): Kiểm định Tính đầy đủ (Phát hiện bỏ sót)"],
         "case_studies": [{"title": "Gửi Thư Xác Nhận Ngân Hàng (Bank Confirmation)", "detail": "Thủ tục bắt buộc gửi xác nhận độc lập tới tất cả các ngân hàng mở tài khoản để phát hiện tiền gửi bị phong tỏa, nợ thấu chi hoặc nghĩa vụ bảo lãnh chưa công bố."}]}
    ]
    phd2 = {
        "topics": [
            "Mô hình Đánh giá Độ tin cậy Bằng chứng Kiểm toán bằng Mạng Bayes (Bayesian Belief Networks in Audit Evidence Evaluation): Cập nhật xác suất tiên nghiệm (Prior Probability) về rủi ro sai sót sau khi thu thập các bằng chứng kiểm toán độc lập.",
            "Tác động của Công nghệ Kiểm toán Tự động (Continuous Auditing) và Phân tích Dữ liệu Lớn (Big Data Analytics): Dịch chuyển từ kiểm toán chọn mẫu truyền thống sang kiểm tra 100% tổng thể giao dịch bằng thuật toán phát hiện gian lận tự động.",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về Phán đoán Chuyên môn (Professional Judgment) và Sự hoài nghi nghề nghiệp (Professional Skepticism) của kiểm toán viên trong môi trường làm việc chịu áp lực về thời gian và ngân sách giờ kiểm toán."
        ]
    }
    q1 = [
        "Phân tích mối quan hệ giữa Cơ sở dẫn liệu của Ban Giám đốc và Mục tiêu kiểm toán của Kiểm toán viên. Cho ví dụ minh họa.",
        "Trình bày 7 kỹ thuật thu thập bằng chứng kiểm toán theo chuẩn mực VSA 500. Kỹ thuật nào cung cấp bằng chứng có độ tin cậy cao nhất?",
        "Phân biệt thủ tục Kiểm tra ngược (Vouching) và Kiểm tra xuôi (Tracing). Mục tiêu phát hiện sai phạm của mỗi thủ tục là gì?"
    ]
    b.add_chapter(2, "Bằng chứng Kiểm toán và Phương pháp Thu thập", intro2, sec2, phd2, q1)
    
    # Chương 3
    intro3 = ("Chương 3 đi sâu vào hai khái niệm nền tảng chi phối toàn bộ chiến lược và chi phí của cuộc kiểm toán: "
              "Mức trọng yếu (Materiality) và Mô hình rủi ro kiểm toán (Audit Risk Model).")
    sec3 = [
        {"sec_num": 1, "sec_title": "Mức Trọng Yếu và Các Cấp Độ Xác Định (VSA 320)",
         "content": ("Theo VSA 320, thông tin được coi là trọng yếu nếu việc thiếu sót hoặc sai sót của thông tin đó có thể làm ảnh hưởng "
                     "đến các quyết định kinh tế của người sử dụng Báo cáo tài chính. Trọng yếu mang cả tính chất định lượng (quy mô số tiền) "
                     "và định tính (bản chất sai phạm, ví dụ: Gian lận của ban giám đốc, vi phạm cam kết khế ước vay, giao dịch với bên liên quan).\n\n"
                     "KTV xác định 3 cấp độ mức trọng yếu:\n"
                     "(1) Mức trọng yếu tổng thể (Overall Materiality): Áp dụng cho toàn bộ BCTC, thường tính bằng 0.5% - 1% Tổng doanh thu, "
                     "hoặc 1% - 2% Tổng tài sản, hoặc 5% - 10% Lợi nhuận trước thuế.\n"
                     "(2) Mức trọng yếu thực hiện (Performance Materiality): Được thiết lập ở mức thấp hơn mức trọng yếu tổng thể (thường từ 50% đến 75%) "
                     "nhằm giảm thiểu rủi ro tích tụ các sai sót nhỏ chưa phát hiện vượt quá mức trọng yếu tổng thể.\n"
                     "(3) Ngưỡng sai sót không đáng kể (Clearly Trivial Threshold - CTT): Mức sai sót nhỏ (khoảng 3% - 5% mức trọng yếu tổng thể) "
                     "được bỏ qua không cần tổng hợp vào bảng chênh lệch kiểm toán."),
         "formulas": ["Mức trọng yếu thực hiện = Mức trọng yếu tổng thể x (50% đến 75%)",
                      "Ngưỡng CTT = Mức trọng yếu tổng thể x (3% đến 5%)"],
         "case_studies": [{"title": "Xác định Mức Trọng Yếu cho Tập đoàn Bán lẻ", "detail": "Lựa chọn tiêu chí chuẩn là 1% Doanh thu thuần (thay vì Lợi nhuận trước thuế) đối với doanh nghiệp ngành bán lẻ có biên lợi nhuận ròng rất mỏng và biến động thất thường."}]},
        {"sec_num": 2, "sec_title": "Mô Hình Rủi Ro Kiểm Toán và Chiến Lược Kiểm Toán",
         "content": ("Rủi ro kiểm toán (Audit Risk - AR) là rủi ro KTV đưa ra ý kiến chấp nhận toàn phần không thích hợp khi BCTC vẫn còn chứa đựng sai sót trọng yếu.\n"
                     "Mô hình rủi ro kiểm toán kinh điển: AR = IR x CR x DR = RMM x DR.\n"
                     "- Rủi ro tiềm tàng (Inherent Risk - IR): Rủi ro tiềm ẩn một số dư tài khoản hoặc giao dịch dễ mắc phải sai sót trọng yếu do tính chất phức tạp, "
                     "ước tính chủ quan hoặc do đặc thù ngành (độc lập với hệ thống KSNB).\n"
                     "- Rủi ro kiểm soát (Control Risk - CR): Rủi ro hệ thống kiểm soát nội bộ của khách hàng không thể ngăn chặn, phát hiện và sửa chữa kịp thời sai sót.\n"
                     "- Rủi ro có sai sót trọng yếu (Risk of Material Misstatement - RMM): Là tích số IR x CR, là rủi ro nội tại của khách hàng mà KTV không thể thay đổi được.\n"
                     "- Rủi ro phát hiện (Detection Risk - DR): Rủi ro các thủ tục kiểm toán do KTV thực hiện không phát hiện được các sai sót trọng yếu. "
                     "KTV chỉ có thể kiểm soát và điều chỉnh DR bằng cách tăng giảm quy mô mẫu và phạm vi các thử nghiệm cơ bản."),
         "formulas": ["Mô hình rủi ro kiểm toán: AR = IR x CR x DR",
                      "Rủi ro phát hiện có thể chấp nhận được: DR = AR / (IR x CR) = AR / RMM",
                      "Mối quan hệ nghịch đảo: Nếu RMM được đánh giá cao -> KTV bắt buộc phải hạ thấp DR -> Mở rộng quy mô mẫu và tăng cường thủ tục cơ bản"],
         "case_studies": [{"title": "Kiểm toán Doanh nghiệp Kinh doanh Bất động sản", "detail": "Đánh giá Rủi ro tiềm tàng (IR) ở mức Tối đa (High) đối với ước tính giá trị thu hồi của các dự án dở dang vướng mắc pháp lý giải phóng mặt bằng."}]}
    ]
    phd3 = {
        "topics": [
            "Mô hình Phí Kiểm toán Simunic (Simunic 1980 Audit Fee Model): Phân tích hàm phí kiểm toán phụ thuộc vào Quy mô khách hàng, Độ phức tạp hoạt động, Đòn bẩy nợ và Mức độ rủi ro kiểm toán đánh giá.",
            "Lý thuyết Quản trị Rủi ro Kiểm toán theo Hướng Tiếp cận Kinh doanh (Business Risk Audit Approach): Sự chuyển dịch từ kiểm toán giao dịch thuần túy sang kiểm toán chiến lược và rủi ro kinh doanh toàn diện (Bell et al. 1997, 2002).",
            "Chuyên đề Tiến sĩ: Nghiên cứu định lượng mối quan hệ phi tuyến tính giữa Mức độ Trọng yếu, Rủi ro Kiện tụng (Litigation Risk) và Chất lượng Kiểm toán tại các nền kinh tế có hệ thống pháp lý yếu."
        ]
    }
    q3 = [
        "Phân tích bản chất kinh tế của 3 thành phần trong Mô hình rủi ro kiểm toán: AR = IR x CR x DR.",
        "Tại sao Kiểm toán viên không thể thay đổi Rủi ro có sai sót trọng yếu (RMM) của khách hàng mà chỉ có thể điều chỉnh Rủi ro phát hiện (DR)?",
        "Trình bày các bước xác định Mức trọng yếu tổng thể, Mức trọng yếu thực hiện và Ngưỡng sai sót không đáng kể theo VSA 320."
    ]
    b.add_chapter(3, "Trọng yếu và Rủi ro trong Kiểm toán", intro3, sec3, phd3, q3)
    
    # Chương 4
    intro4 = ("Chương 4 trang bị phương pháp đánh giá hệ thống kiểm soát nội bộ của khách hàng theo khuôn khổ COSO. "
              "Kết quả đánh giá này quyết định trực tiếp việc lựa chọn chiến lược kiểm toán dựa trên kiểm soát hay kiểm toán cơ bản.")
    sec4 = [
        {"sec_num": 1, "sec_title": "Khuôn Khổ Kiểm Soát Nội Bộ COSO Hiện Đại",
         "content": ("Theo Báo cáo COSO (Ủy ban Treadway), Kiểm soát nội bộ là một quy trình do Hội đồng quản trị, Ban giám đốc "
                     "và các nhân viên khác của đơn vị thiết kế và vận hành nhằm cung cấp sự đảm bảo hợp lý về việc đạt được 3 mục tiêu:\n"
                     "(1) Hiệu quả và hiệu lực hoạt động; (2) Độ tin cậy của báo cáo tài chính; (3) Sự tuân thủ luật pháp và quy định.\n\n"
                     "5 bộ phận cấu thành hữu cơ của hệ thống KSNB (COSO Framework):\n"
                     "- Môi trường kiểm soát (Control Environment): Tinh thần kỷ luật, giá trị đạo đức, phong cách điều hành của lãnh đạo (Tone at the top).\n"
                     "- Đánh giá rủi ro (Risk Assessment): Nhận diện và phân tích các rủi ro cản trở việc đạt mục tiêu của đơn vị.\n"
                     "- Hoạt động kiểm soát (Control Activities): Các chính sách và thủ tục đảm bảo chỉ thị của lãnh đạo được thực thi (phân công phân nhiệm, phê duyệt, bảo vệ tài sản, đối chiếu).\n"
                     "- Thông tin và truyền thông (Information and Communication): Hệ thống truyền tải thông tin thích hợp và kịp thời.\n"
                     "- Giám sát (Monitoring Activities): Đánh giá liên tục và định kỳ về chất lượng vận hành của hệ thống."),
         "formulas": ["Nguyên tắc bất kiêm nhiệm (Segregation of Duties): Tách biệt 4 chức năng: Phê duyệt giao dịch - Thực hiện nghiệp vụ - Bảo quản tài sản - Ghi sổ kế toán"],
         "case_studies": [{"title": "Vụ Gian Lận Tiền Gửi Huyền Như tại VietinBank", "detail": "Bài học kinh điển về sự suy sụp của Môi trường kiểm soát và vi phạm nghiêm trọng nguyên tắc phân công phân nhiệm và kiểm tra chéo."}]},
        {"sec_num": 2, "sec_title": "Thử Nghiệm Kiểm Soát và Thử Nghiệm Cơ Bản",
         "content": ("Quy trình đánh giá KSNB của KTV gồm 4 bước:\n"
                     "(1) Tìm hiểu hệ thống KSNB qua phỏng vấn, kiểm tra sơ đồ quy trình và thử nghiệm Walk-through.\n"
                     "(2) Đánh giá sơ bộ rủi ro kiểm soát (CR).\n"
                     "(3) Thực hiện Thử nghiệm kiểm soát (Tests of Controls): Kiểm tra tính hữu hiệu của việc thiết kế và sự vận hành liên tục "
                     "của các thủ tục kiểm soát trong suốt kỳ kế toán (ví dụ: Kiểm tra chữ ký phê duyệt chi tiền trên các chứng từ mẫu).\n"
                     "(4) Đánh giá lại rủi ro kiểm soát và thiết kế Thử nghiệm cơ bản (Substantive Procedures):\n"
                     "- Nếu KSNB tốt (CR thấp): KTV giảm bớt các thử nghiệm cơ bản, giảm cỡ mẫu.\n"
                     "- Nếu KSNB yếu kém (CR cao): KTV không thực hiện thử nghiệm kiểm soát mà chuyển thẳng sang thực hiện thử nghiệm cơ bản mở rộng tối đa."),
         "formulas": ["Thủ tục Walk-through: Lựa chọn 1 giao dịch duy nhất từ khi bắt đầu phát sinh đến khi lên BCTC để kiểm tra luồng kiểm soát thực tế",
                      "Thử nghiệm cơ bản = Thủ tục phân tích cơ bản + Kiểm tra chi tiết nghiệp vụ và số dư (Tests of Details)"],
         "case_studies": [{"title": "Kiểm toán Chu trình Mua hàng và Trả tiền", "detail": "Thử nghiệm kiểm soát đối chiếu 3 chiều (3-Way Matching): Đơn đặt hàng (PO) - Biên bản giao nhận hàng (GRN) - Hóa đơn tài chính của nhà cung cấp trước khi giải ngân thanh toán."}]}
    ]
    phd4 = {
        "topics": [
            "Đánh giá Điểm yếu Trọng yếu của KSNB (Internal Control Material Weaknesses - SOX Section 404): Phân tích tác động của việc công bố điểm yếu kiểm soát nội bộ đến chi phí vốn vay và sự từ chức của các Giám đốc Tài chính (CFO).",
            "Mô hình Đánh giá Rủi ro Gian lận Tam giác Gian lận (Fraud Triangle - Cressey 1953): Áp lực (Pressure), Cơ hội (Opportunity) và Hợp lý hóa hành vi (Rationalization) trong môi trường hệ thống kiểm soát nội bộ bị vô hiệu hóa bởi Ban điều hành (Management Override of Controls).",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về vai trò độc lập của Ủy ban Kiểm toán (Audit Committee) trong việc hạn chế hành vi thao túng báo cáo tài chính tại các ngân hàng thương mại cổ phần Việt Nam."
        ]
    }
    q4 = [
        "Trình bày 5 bộ phận cấu thành hệ thống Kiểm soát nội bộ theo khuôn khổ COSO. Bộ phận nào giữ vai trò nền tảng?",
        "Phân tích nguyên tắc 'Bất kiêm nhiệm' (Segregation of Duties) trong kiểm soát nội bộ và nêu hậu quả nếu nguyên tắc này bị vi phạm.",
        "Phân biệt mục đích và phương pháp thực hiện giữa Thử nghiệm kiểm soát (Tests of Controls) và Thử nghiệm cơ bản (Substantive Tests)."
    ]
    b.add_chapter(4, "Hệ thống Kiểm soát Nội bộ và Đánh giá Rủi ro", intro4, sec4, phd4, q4)
    
    # Chương 5
    intro5 = ("Chương 5 cung cấp lý thuyết phương pháp kiểm toán và kỹ thuật chọn mẫu kiểm toán theo chuẩn mực VSA 530. "
              "KTV nắm vững phương pháp lấy mẫu thống kê toán học để kết luận về tổng thể với độ tin cậy xác định.")
    sec5 = [
        {"sec_num": 1, "sec_title": "Thủ Tục Phân Tích (Analytical Procedures - VSA 520)",
         "content": ("Thủ tục phân tích là việc đánh giá các thông tin tài chính thông qua việc phân tích các mối quan hệ hợp lý "
                     "giữa các dữ liệu tài chính và phi tài chính (ví dụ: So sánh tỷ số nợ, tỷ suất lợi nhuận gộp, so sánh doanh thu khách sạn với số lượng phòng và công suất lấp đầy).\n\n"
                     "Thủ tục phân tích được thực hiện bắt buộc trong 3 giai đoạn:\n"
                     "- Giai đoạn Lập kế hoạch kiểm toán: Nhận diện các vùng có rủi ro bất thường và thiết kế chương trình kiểm toán.\n"
                     "- Giai đoạn Thực hiện kiểm toán: Đóng vai trò là thử nghiệm cơ bản để thu thập bằng chứng xác nhận số dư.\n"
                     "- Giai đoạn Soát xét tổng thể cuối kỳ: Đánh giá lần cuối xem BCTC có phù hợp với hiểu biết của KTV về toàn bộ doanh nghiệp hay không."),
         "formulas": ["Ước tính doanh thu vận tải độc lập = Số đầu xe x Số chuyến bình quân/ngày x Cự ly bình quân x Giá vé niêm yết x Số ngày hoạt động",
                      "Chênh lệch bất thường = |Giá trị sổ sách - Giá trị KTV ước tính| > Ngưỡng chênh lệch có thể chấp nhận được"],
         "case_studies": [{"title": "Thủ Tục Phân Tích Doanh Thu Khách Sạn Mường Thanh", "detail": "Đối chiếu doanh thu phòng trên sổ kế toán với dữ liệu đăng ký tạm trú tại công an phường và hóa đơn tiền giặt là khăn ga giường thực tế."}]},
        {"sec_num": 2, "sec_title": "Lấy Mẫu Kiểm Toán Theo Chuẩn Mực VSA 530",
         "content": ("Lấy mẫu kiểm toán là việc áp dụng các thủ tục kiểm toán trên số lượng phần tử ít hơn 100% tổng số phần tử của tổng thể "
                     "sao cho tất cả các phần tử đều có cơ hội được lựa chọn nhằm đưa ra kết luận về toàn bộ tổng thể.\n\n"
                     "Hai phương pháp lấy mẫu:\n"
                     "(1) Lấy mẫu thống kê (Statistical Sampling): Dựa trên lý thuyết xác suất toán học để xác định cỡ mẫu và đánh giá rủi ro lấy mẫu một cách khách quan.\n"
                     "(2) Lấy mẫu phi thống kê (Non-statistical Sampling): Dựa hoàn toàn vào xét đoán chuyên môn của KTV.\n\n"
                     "Kỹ thuật Lấy mẫu theo đơn vị tiền tệ (Monetary Unit Sampling - MUS): "
                     "Từng đồng tiền trong số dư tài khoản được coi là một phần tử chọn mẫu. "
                     "Phương pháp này tự động ưu tiên lựa chọn các hóa đơn có giá trị tiền tệ lớn, cực kỳ hiệu quả trong việc phát hiện rủi ro ghi khống tài sản."),
         "formulas": ["Bước nhảy chọn mẫu (Sampling Interval): k = Tổng giá trị tổng thể / Cỡ mẫu (n)",
                      "Phần tử chọn mẫu thứ i = Điểm xuất phát ngẫu nhiên + (i - 1) * k"],
         "case_studies": [{"title": "Lấy Mẫu Kiểm Toán Khoản Mục Nợ Phải Thu Khách Hàng", "detail": "Áp dụng kỹ thuật MUS lựa chọn 60 khách hàng nợ lớn nhất từ tổng thể 1.200 khách hàng để gửi thư xác nhận đạt độ bao phủ 85% giá trị toàn bộ khoản phải thu."}]}
    ]
    phd5 = {
        "topics": [
            "Lý thuyết Chọn mẫu Kiểm toán Bayes (Bayesian Audit Sampling - Cox & Snell 1979): Kết hợp phán đoán chuyên môn ban đầu với bằng chứng mẫu toán học để tối ưu hóa kích thước mẫu kiểm toán.",
            "Rủi ro Lấy mẫu (Sampling Risk) so với Rủi ro Ngoài Lấy mẫu (Non-sampling Risk): Phân tích sai lầm loại I (Alpha Risk - Rủi ro từ chối sai) và sai lầm loại II (Beta Risk - Rủi ro chấp nhận sai) và chi phí tổn thất pháp lý của công ty kiểm toán.",
            "Chuyên đề Tiến sĩ: Ứng dụng Thuật toán Học máy không giám sát (Unsupervised Anomaly Detection & Isolation Forests) trong việc quét toàn bộ nhật ký giao dịch tài chính thay thế kỹ thuật lấy mẫu truyền thống."
        ]
    }
    q5 = [
        "Trình bày vai trò và yêu cầu bắt buộc của Thủ tục phân tích (Analytical Procedures) trong 3 giai đoạn của cuộc kiểm toán.",
        "Phân biệt bản chất và điều kiện áp dụng giữa Lấy mẫu thống kê và Lấy mẫu phi thống kê theo VSA 530.",
        "Giải thích cơ chế vận hành của Kỹ thuật Lấy mẫu theo đơn vị tiền tệ (Monetary Unit Sampling - MUS). Tại sao phương pháp này tự động ưu tiên các khoản mục có giá trị lớn?"
    ]
    b.add_chapter(5, "Phương pháp Kiểm toán và Lấy mẫu Kiểm toán", intro5, sec5, phd5, q5)
    
    # Chương 6
    intro6 = ("Chương 6 tổng kết toàn bộ quy trình kiểm toán qua sản phẩm đầu ra pháp lý cao nhất: Báo cáo Kiểm toán. "
              "Chương này phân tích các dạng ý kiến kiểm toán, Vấn đề kiểm toán trọng yếu (KAM) và đạo đức nghề nghiệp.")
    sec6 = [
        {"sec_num": 1, "sec_title": "Cấu Trúc Báo Cáo Kiểm Toán và Các Dạng Ý Kiến (VSA 700 / 705 / 706)",
         "content": ("Báo cáo kiểm toán là tài liệu pháp lý do KTV lập để bày tỏ ý kiến nhận xét của mình về tính trung thực và hợp lý "
                     "của BCTC được kiểm toán trên các khía cạnh trọng yếu.\n\n"
                     "4 dạng ý kiến kiểm toán theo Chuẩn mực VSA 700 và VSA 705:\n"
                     "(1) Ý kiến Chấp nhận toàn phần (Unmodified Opinion): BCTC phản ánh trung thực, hợp lý trên các khía cạnh trọng yếu.\n"
                     "(2) Ý kiến Chấp nhận từng phần / Ngoại trừ (Qualified Opinion): Có sai sót trọng yếu nhưng không lan tỏa (Not Pervasive), "
                     "hoặc KTV không thể thu thập đầy đủ bằng chứng thích hợp nhưng ảnh hưởng có thể trọng yếu mà không lan tỏa.\n"
                     "(3) Ý kiến Trái ngược (Adverse Opinion): Sai sót vừa mang tính trọng yếu vừa có tính chất lan tỏa (Pervasive) "
                     "làm cho BCTC không phản ánh trung thực tình hình tài chính.\n"
                     "(4) Từ chối đưa ra ý kiến (Disclaimer of Opinion): KTV bị giới hạn nghiêm trọng phạm vi kiểm toán hoặc gặp các yếu tố không chắc chắn trọng yếu "
                     "mang tính lan tỏa tới mức không thể hình thành ý kiến kiểm toán."),
         "formulas": ["Ma trận quyết định ý kiến kiểm toán:\n- Sai sót Trọng yếu nhưng KHÔNG Lan tỏa -> Ý kiến Ngoại trừ (Except for)\n- Sai sót Trọng yếu VÀ Lan tỏa -> Ý kiến Trái ngược (Adverse)\n- Bị giới hạn Trọng yếu nhưng KHÔNG Lan tỏa -> Ý kiến Ngoại trừ\n- Bị giới hạn Trọng yếu VÀ Lan tỏa -> Từ chối đưa ra ý kiến (Disclaimer)"],
         "case_studies": [{"title": "Báo Cáo Kiểm Toán Ngoại Trừ của Công ty Cổ phần Hoàng Anh Gia Lai (HAG)", "detail": "Kiểm toán viên Ernst & Young đưa ra ý kiến ngoại trừ và nhấn mạnh vấn đề nghi ngờ khả năng hoạt động liên tục do nợ ngắn hạn vượt quá tài sản ngắn hạn."}]},
        {"sec_num": 2, "sec_title": "Vấn Đề Kiểm Toán Trọng Yếu (KAM) và Chuẩn Mực Đạo Đức IFAC",
         "content": ("Theo Chuẩn mực ISA 701, Báo cáo kiểm toán của các công ty niêm yết bắt buộc phải có mục Vấn đề Kiểm toán Trọng yếu (KAM - Key Audit Matters). "
                     "KAM là những vấn đề được KTV đánh giá là có ý nghĩa quan trọng nhất trong cuộc kiểm toán, "
                     "thường liên quan đến các ước tính kế toán phức tạp có tính chủ quan cao của ban điều hành "
                     "(ví dụ: Tổn thất lợi thế thương mại, ghi nhận doanh thu dự án dài hạn, dự phòng rủi ro tín dụng).\n\n"
                     "Bộ quy tắc Đạo đức Nghề nghiệp của IFAC (Quy định 100) đưa ra 5 nguyên tắc đạo đức cơ bản:\n"
                     "(1) Tính Chính trực (Integrity); (2) Tính Khách quan (Objectivity); (3) Năng lực chuyên môn và tính thận trọng (Professional Competence & Due Care); "
                     "(4) Tính Bảo mật (Confidentiality); (5) Tư cách nghề nghiệp (Professional Behavior).\n"
                     "Đồng thời kiểm soát 5 nguy cơ đe dọa tính độc lập: Nguy cơ do tư lợi, Nguy cơ tự kiểm tra, Nguy cơ bào chữa, Nguy cơ thân quen và Nguy cơ bị đe dọa."),
         "formulas": ["Bảo vệ tính độc lập = Nhận diện nguy cơ -> Đánh giá mức độ nghiêm trọng -> Áp dụng biện pháp bảo vệ (Safeguards) hoặc từ chối hợp đồng"],
         "case_studies": [{"title": "Xoay Vòng Kiểm Toán Viên Định Kỳ (Partner Rotation)", "detail": "Quy định bắt buộc KTV ký báo cáo phải luân chuyển sau tối đa 5 năm liên tục để triệt tiêu nguy cơ thân quen (Familiarity Threat) theo Luật Kiểm toán Độc lập."}]}
    ]
    phd6 = {
        "topics": [
            "Chất lượng Kiểm toán và Danh tiếng KTV (Audit Quality Metrics - DeAngelo 1981, Francis 2011): Khái niệm chất lượng kiểm toán như xác suất phát hiện sai phạm và xác suất báo cáo sai phạm đó của kiểm toán viên.",
            "Tác động của Việc Công bố Key Audit Matters (KAM Under ISA 701) đến Phản ứng của Nhà Đầu tư: Sự cải thiện tính minh bạch thông tin thị trường vốn so với nguy cơ công bố theo khuôn mẫu sáo rỗng (Boilerplate Language).",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về Tác động của việc Ký tên Kiểm toán viên cá nhân (Audit Partner Signature) đến Mức độ Thận trọng và Phí kiểm toán tại các thị trường tài chính Châu Á."
        ]
    }
    q6 = [
        "Phân tích điều kiện để đưa ra từng dạng trong 4 loại ý kiến kiểm toán theo chuẩn mực VSA 705. Khái niệm 'Lan tỏa' (Pervasive) được hiểu như thế nào?",
        "Ý nghĩa và mục đích của phần 'Vấn đề kiểm toán trọng yếu' (Key Audit Matters - KAM) trên Báo cáo kiểm toán của các công ty niêm yết theo ISA 701.",
        "Trình bày 5 nguyên tắc đạo đức cơ bản của nghề kiểm toán viên và phân tích 5 nguy cơ đe dọa tính độc lập theo Bộ quy tắc đạo đức của IFAC."
    ]
    b.add_chapter(6, "Báo cáo Kiểm toán và Đạo đức Nghề nghiệp", intro6, sec6, phd6, q6)
    
    out_dir = os.path.join(BASE_DIR, r"02_Kế toán & Kiểm toán\[NEU] Kiểm toán căn bản - GS.TS Nguyễn Quang Quynh (NXB ĐHKTQD)")
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Kiểm toán căn bản - GS.TS Nguyễn Quang Quynh (NXB ĐHKTQD).pdf")
    pages, size_mb = b.save(out_pdf)
    print(f"-> Hoàn thành Sách 5: {pages} trang, {size_mb:.2f} MB. Lưu tại: {out_pdf}")
    return {"book": "Kiểm toán căn bản", "pages": pages, "size_mb": size_mb, "path": out_pdf}


def build_book_6():
    print("--- Đang biên soạn Sách 6: Phân tích báo cáo tài chính ---")
    title = "Phân tích Báo cáo Tài chính"
    code = "KTKT1110"
    faculty = "Viện Kế toán - Kiểm toán"
    authors = "PGS.TS. Nguyễn Năng Phúc (Chủ biên), PGS.TS. Phạm Đức Hiếu, TS. Nguyễn Thị Mỹ Dung"
    
    b = NEUTextbookBuilder(title, code, faculty, authors)
    b.build_cover()
    
    toc = [
        {"chapter_num": 1, "chapter_title": "Cơ sở Lý luận và Phương pháp Phân tích BCTC",
         "topics": ["Mục tiêu và vai trò của phân tích BCTC đối với các bên liên quan", "Hệ thống tài liệu và thông tin sử dụng trong phân tích tài chính", "Các phương pháp phân tích kỹ thuật: So sánh, tỷ số, xu hướng, tỷ trọng", "Những giới hạn nội tại của dữ liệu BCTC và các thủ thuật kế toán"]},
        {"chapter_num": 2, "chapter_title": "Phân tích Cấu trúc Tài chính và Khả năng Thanh toán",
         "topics": ["Phân tích cơ cấu tài sản và cơ cấu nguồn vốn doanh nghiệp", "Đánh giá mức độ độc lập tài chính và đòn bẩy nợ (D/E, Debt/Assets)", "Phân tích khả năng thanh toán ngắn hạn (Current, Quick, Cash Ratio)", "Đo lường vốn lưu động ròng (NWC) và khả năng thanh toán lãi vay (ICR)"]},
        {"chapter_num": 3, "chapter_title": "Phân tích Hiệu quả Hoạt động và Chu kỳ Kinh doanh",
         "topics": ["Đo lường hiệu quả quản trị khoản phải thu (Receivables Turnover, DSO)", "Đo lường hiệu quả quản trị hàng tồn kho (Inventory Turnover, DIO)", "Vòng quay khoản phải trả (Payables Turnover, DPO)", "Chu kỳ chuyển hóa tiền mặt (Cash Conversion Cycle - CCC) và vòng quay tài sản"]},
        {"chapter_num": 4, "chapter_title": "Phân tích Khả năng Sinh lời và Mô hình DuPont",
         "topics": ["Các chỉ tiêu sinh lời hoạt động: Biên lợi nhuận gộp, biên EBIT, ROS", "Tỷ suất sinh lời trên tài sản (ROA) và trên vốn đầu tư (ROIC)", "Mô hình phân tích DuPont 3 nhân tố và 5 nhân tố của ROE", "Chất lượng lợi nhuận kế toán và mô hình Sloan Accrual"]},
        {"chapter_num": 5, "chapter_title": "Phân tích Báo cáo Lưu chuyển Tiền tệ và Khả năng Tạo tiền",
         "topics": ["Đánh giá chất lượng dòng tiền từ hoạt động kinh doanh (CFO)", "Phân tích mối quan hệ giữa Lợi nhuận kế toán và Dòng tiền CFO", "Dòng tiền tự do của doanh nghiệp (FCFF) và dòng tiền tự do vốn chủ sở hữu (FCFE)", "Dấu hiệu cảnh báo suy kiệt thanh khoản và mô hình gian lận Beneish M-Score"]},
        {"chapter_num": 6, "chapter_title": "Dự báo Tài chính và Mô hình Cảnh báo Sớm Phá sản",
         "topics": ["Phương pháp tỷ lệ phần trăm trên doanh thu để lập BCTC dự kiến", "Xác định nhu cầu vốn lưu động bổ sung bên ngoài (AFN)", "Mô hình chấm điểm rủi ro phá sản Altman Z-Score (Sản xuất và Phi sản xuất)", "Mô hình Ohlson O-Score và ứng dụng Machine Learning trong xếp hạng tín dụng"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chương 1
    intro1 = ("Chương 1 cung cấp khung lý thuyết và phương pháp luận của phân tích báo cáo tài chính. "
              "Người phân tích học cách 'đọc vị' những câu chuyện kinh doanh và chiến lược doanh nghiệp ẩn sau các con số dồn tích.")
    sec1 = [
        {"sec_num": 1, "sec_title": "Mục Tiêu và Phương Pháp Luận Phân Tích Tài Chính",
         "content": ("Phân tích Báo cáo tài chính là nghệ thuật biến đổi các dữ liệu thô trên BCTC thành các thông tin hữu ích "
                     "phục vụ việc ra quyết định kinh tế của các nhóm đối tượng khác nhau:\n"
                     "- Nhà đầu tư cổ phiếu: Quan tâm đến tiềm năng tăng trưởng doanh thu, tỷ suất sinh lời ROE, rủi ro pha loãng và khả năng chia cổ tức.\n"
                     "- Ngân hàng và chủ nợ: Quan tâm hàng đầu đến khả năng thanh toán đúng hạn, cơ cấu tài sản bảo đảm và đòn bẩy nợ vay.\n"
                     "- Ban Giám đốc: Sử dụng phân tích để tìm kiếm các điểm nghẽn chi phí, tối ưu hóa vòng quay vốn và cải thiện năng lực cạnh tranh.\n"
                     "- Cơ quan thuế và quản lý thị trường: Giám sát việc tuân thủ pháp luật và phát hiện các dấu hiệu trốn thuế, gian lận.\n\n"
                     "4 phương pháp phân tích kỹ thuật cơ bản:\n"
                     "(1) Phân tích ngang (Horizontal Analysis): So sánh biến động tuyệt đối và tỷ lệ % của từng chỉ tiêu qua các niên độ liên tiếp.\n"
                     "(2) Phân tích dọc (Vertical Analysis / Common-Size Statements): Quy đổi BCTC thành tỷ lệ phần trăm trên Tổng tài sản hoặc Doanh thu thuần.\n"
                     "(3) Phân tích xu hướng (Trend Analysis): Sử dụng một năm gốc làm mốc 100% để đánh giá xu hướng phát triển dài hạn.\n"
                     "(4) Phân tích tỷ số (Ratio Analysis): Đo lường các mối quan hệ logic giữa các nhóm chỉ tiêu tài chính."),
         "formulas": ["Biến động tương đối (%) = [(Chỉ tiêu năm nay - Chỉ tiêu năm trước) / |Chỉ tiêu năm trước|] x 100%",
                      "Tỷ trọng chỉ tiêu (Common-size BS) = (Giá trị khoản mục / Tổng tài sản) x 100%"],
         "case_studies": [{"title": "Phân Tích Quy Mô Tập Đoàn Vingroup (VIC)", "detail": "Ứng dụng phân tích dọc Common-Size đánh giá sự chuyển dịch cấu trúc tài sản từ Bất động sản dân cư sang Công nghiệp sản xuất công nghệ cao xe điện."}]},
        {"sec_num": 2, "sec_title": "Các Hạn Chế của BCTC và Thủ Thuật Làm Đẹp Báo Cáo (Window Dressing)",
         "content": ("Người phân tích tài chính phải luôn giữ sự hoài nghi chuyên môn trước những hạn chế nội tại của dữ liệu kế toán:\n"
                     "- Nguyên tắc giá gốc (Historical Cost) làm sai lệch giá trị thực tế của tài sản trong thời kỳ lạm phát hoặc sốt đất đai.\n"
                     "- Các chính sách kế toán khác nhau (ví dụ: Khấu hao nhanh vs Khấu hao đường thẳng) làm triệt tiêu tính có thể so sánh giữa các doanh nghiệp cùng ngành.\n"
                     "- Ước tính kế toán mang tính chủ quan của ban giám đốc (ước tính nợ khó đòi, dự phòng hàng tồn kho).\n\n"
                     "Các thủ thuật làm đẹp BCTC phổ biến (Window Dressing & Creative Accounting):\n"
                     "- Trì hoãn ghi nhận chi phí sửa chữa lớn sang các năm sau.\n"
                     "- Bán tài sản cố định hoặc bất động sản vào cuối quý để ghi nhận lợi nhuận đột biến một lần nhằm đạt mục tiêu kế hoạch.\n"
                     "- Đẩy mạnh bán hàng vào tuần cuối năm cho các đại lý với chính sách cho trả lại hàng đầu năm sau để thổi phồng doanh thu dồn tích."),
         "formulas": ["Chỉ số chất lượng BCTC: Tỷ lệ Dòng tiền CFO / Lợi nhuận sau thuế < 1 liên tục nhiều năm là tín hiệu cảnh báo rủi ro cao"],
         "case_studies": [{"title": "Vụ Gian Lận BCTC Tập Đoàn Gỗ Trường Thành (TTF)", "detail": "Phát hiện hàng nghìn tỷ đồng hàng tồn kho bị ghi khống và các khoản phải thu khống khi đối tác kiểm toán mới tiến hành kiểm kê thực tế."}]}
    ]
    phd1 = {
        "topics": [
            "Hàm lượng Thông tin Kế toán và Thị trường Vốn Hiệu quả (Value Relevance & Market Efficiency - Beaver 1968, Lev & Thiagarajan 1993): Đánh giá 12 tín hiệu tài chính cơ bản (Fundamental Financial Signals) trong việc dự báo giá cổ phiếu vượt trội.",
            "Lý thuyết Quản trị Lợi nhuận và Tính Bền vững của Thu nhập (Earnings Quality & Earnings Persistence - Dechow, Ge & Schrand 2010): Phân tách thành phần tiền tệ và thành phần dồn tích trong thu nhập.",
            "Chuyên đề Tiến sĩ: Ứng dụng Xử lý Ngôn ngữ Tự nhiên (NLP) phân tích mức độ trung thực của Thuyết minh BCTC và Báo cáo thường niên để dự báo nguy cơ vi phạm gian lận chứng khoán tại Việt Nam."
        ]
    }
    q1 = [
        "Trình bày các phương pháp phân tích BCTC cơ bản: Phân tích so sánh ngang, phân tích tỷ trọng dọc và phân tích tỷ số tài chính.",
        "Tại sao việc chỉ dựa vào các con số kế toán trên Báo cáo kết quả hoạt động kinh doanh có thể đưa ra những đánh giá sai lầm về sức khỏe tài chính của doanh nghiệp?",
        "Phân tích các thủ thuật 'Làm đẹp Báo cáo tài chính' (Window Dressing) phổ biến mà các doanh nghiệp thường sử dụng vào thời điểm cuối niên độ tài chính."
    ]
    b.add_chapter(1, "Cơ sở Lý luận và Phương pháp Phân tích BCTC", intro1, sec1, phd1, q1)
    
    # Chương 2
    intro2 = ("Chương 2 phân tích cấu trúc tài sản, nguồn vốn và khả năng thanh toán của doanh nghiệp. "
              "Đây là phần cốt lõi để xác định mức độ an toàn tài chính, rủi ro đòn bẩy nợ và nguy cơ vỡ nợ ngắn hạn.")
    sec2 = [
        {"sec_num": 1, "sec_title": "Phân Tích Cơ Cấu Nguồn Vốn và Đòn Bẩy Nợ",
         "content": ("Cơ cấu nguồn vốn phản ánh chính sách tài trợ và mức độ rủi ro tài chính của doanh nghiệp. "
                     "Nợ vay mang lại 'Lá chắn thuế' từ lãi vay (Tax Shield), giúp khuếch đại lợi nhuận trên vốn chủ sở hữu (ROE), "
                     "nhưng đồng thời đẩy doanh nghiệp đối mặt với rủi ro kiệt quệ tài chính (Financial Distress) nếu thị trường đảo chiều.\n\n"
                     "Các chỉ số cơ cấu tài chính cốt lõi:\n"
                     "- Tỷ số Nợ trên Tổng tài sản (Debt Ratio) = Tổng nợ phải trả / Tổng tài sản.\n"
                     "- Tỷ số Nợ trên Vốn chủ sở hữu (Debt to Equity - D/E) = Tổng nợ phải trả / Vốn chủ sở hữu.\n"
                     "- Hệ số nợ vay tài chính thuần = (Vay ngắn hạn + Vay dài hạn - Tiền & tương đương tiền) / Vốn chủ sở hữu.\n"
                     "- Khả năng thanh toán lãi vay (Interest Coverage Ratio - ICR) = EBIT / Chi phí lãi vay. "
                     "ICR < 1.5 là ngưỡng báo động đỏ cho thấy lợi nhuận kinh doanh không đủ bù đắp nghĩa vụ trả lãi ngân hàng."),
         "formulas": ["Hệ số đòn bẩy tài chính (FL) = Tổng tài sản bình quân / Vốn chủ sở hữu bình quân",
                      "Lá chắn thuế từ lãi vay = Chi phí lãi vay x Thuế suất thuế TNDN",
                      "ICR = EBIT / Chi phí lãi vay (Threshold an toàn: ICR > 3.0)"],
         "case_studies": [{"title": "Tập đoàn Đầu tư Địa ốc No Va (Novaland - NVL)", "detail": "Phân tích cấu trúc nợ vay trái phiếu ngắn hạn đến hạn trả và cuộc khủng hoảng thanh khoản diện rộng khi thị trường bất động sản đóng băng năm 2022-2023."}]},
        {"sec_num": 2, "sec_title": "Phân Tích Khả Năng Thanh Toán Ngắn Hạn và Vốn Lưu Động",
         "content": ("Khả năng thanh toán ngắn hạn phản ánh năng lực đáp ứng các nghĩa vụ nợ đến hạn trong vòng 1 năm của doanh nghiệp:\n"
                     "(1) Tỷ số Thanh toán Hiện hành (Current Ratio) = Tài sản ngắn hạn / Nợ ngắn hạn. "
                     "Current Ratio > 2.0 thường được coi là an toàn trong sản xuất, nhưng nếu quá cao có thể chỉ ra việc ứ đọng vốn trong tồn kho hoặc nợ khó đòi.\n\n"
                     "(2) Tỷ số Thanh toán Nhanh (Quick Ratio / Acid-test Ratio) = (Tiền + Đầu tư ngắn hạn + Phải thu) / Nợ ngắn hạn "
                     "= (Tài sản ngắn hạn - Hàng tồn kho) / Nợ ngắn hạn. Loại trừ hàng tồn kho vì tồn kho có tính thanh khoản kém nhất.\n\n"
                     "(3) Tỷ số Thanh toán Tức thời (Cash Ratio) = (Tiền & tương đương tiền) / Nợ ngắn hạn.\n\n"
                     "- Vốn lưu động ròng (Net Working Capital - NWC) = Tài sản ngắn hạn - Nợ ngắn hạn. "
                     "NWC dương cho thấy một phần tài sản ngắn hạn được tài trợ bằng nguồn vốn dài hạn ổn định, tạo lớp đệm an toàn vững chắc."),
         "formulas": ["Current Ratio = Current Assets / Current Liabilities",
                      "Quick Ratio = (Cash + Marketable Securities + Receivables) / Current Liabilities",
                      "NWC = Current Assets - Current Liabilities = (Vốn chủ sở hữu + Nợ dài hạn) - Tài sản dài hạn"],
         "case_studies": [{"title": "Công ty Cổ phần Sữa Việt Nam (Vinamilk - VNM)", "detail": "Duy trì tỷ số thanh toán hiện hành trên 2.2 và tỷ số thanh toán tức thời trên 0.8 nhờ dòng tiền bán hàng tiền mặt dồi dào từ mạng lưới phân phối."}]}
    ]
    phd2 = {
        "topics": [
            "Lý thuyết Cấu trúc Vốn Đánh đổi Động (Dynamic Trade-off Theory of Capital Structure - Fischer, Heinkel & Zechner 1989): Tốc độ điều chỉnh của cấu trúc nợ về đòn bẩy mục tiêu tối ưu trong môi trường chi phí giao dịch thị trường.",
            "Lý thuyết Khả năng Tiếp cận Thanh khoản Ngân hàng (Credit Line Availability & Corporate Liquidity - Sufi 2009): Sự thay thế giữa tích trữ tiền mặt tại quỹ (Cash Holdings) và hạn mức tín dụng dự phòng (Bank Lines of Credit).",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về Tác động của rủi ro thanh khoản đến Quyết định đầu tư tài sản cố định của các doanh nghiệp niêm yết trong giai đoạn thắt chặt chính sách tiền tệ."
        ]
    }
    q2 = [
        "Phân tích ý nghĩa kinh tế và ngưỡng giá trị an toàn của 3 chỉ số thanh toán: Hệ số thanh toán hiện hành, Hệ số thanh toán nhanh và Hệ số thanh toán tức thời.",
        "Định nghĩa Vốn lưu động ròng (NWC). Giải thích tại sao một doanh nghiệp có NWC âm lại đối mặt với rủi ro thanh khoản tiềm tàng rất lớn?",
        "Phân tích công thức và ý nghĩa của Hệ số khả năng thanh toán lãi vay (ICR). Khi nào thì ICR trở thành dấu hiệu cảnh báo nguy cơ phá sản?"
    ]
    b.add_chapter(2, "Phân tích Cấu trúc Tài chính và Khả năng Thanh toán", intro2, sec2, phd2, q2)
    
    # Chương 3
    intro3 = ("Chương 3 đi sâu vào phân tích hiệu quả hoạt động và tốc độ chu chuyển vốn. "
              "Trọng tâm nghiên cứu là Chu kỳ chuyển hóa tiền mặt (Cash Conversion Cycle) - thước đo tốc độ vận hành của toàn bộ doanh nghiệp.")
    sec3 = [
        {"sec_num": 1, "sec_title": "Hiệu Quả Quản Trị Phải Thu, Tồn Kho và Phải Trả",
         "content": ("Hiệu quả hoạt động phản ánh tốc độ chuyển hóa tài sản thành doanh thu và tiền mặt thông qua 3 vòng quay trọng yếu:\n"
                     "(1) Vòng quay các khoản phải thu (Receivables Turnover) = Doanh thu thuần / Số dư phải thu khách hàng bình quân.\n"
                     "Số ngày thu tiền bình quân (Days Sales Outstanding - DSO) = 365 / Vòng quay phải thu. "
                     "DSO cho biết thời gian trung bình từ khi xuất bán hàng đến khi thu được tiền mặt về tài khoản.\n\n"
                     "(2) Vòng quay hàng tồn kho (Inventory Turnover) = Giá vốn hàng bán / Giá trị tồn kho bình quân.\n"
                     "Số ngày lưu kho bình quân (Days Inventory Outstanding - DIO) = 365 / Vòng quay hàng tồn kho. "
                     "DIO phản ánh thời gian bình quân một lô hàng nằm trong kho trước khi xuất bán.\n\n"
                     "(3) Vòng quay nợ phải trả người bán (Payables Turnover) = Doanh số mua hàng (hoặc Giá vốn) / Phải trả người bán bình quân.\n"
                     "Số ngày trả tiền bình quân (Days Payables Outstanding - DPO) = 365 / Vòng quay nợ phải trả. "
                     "DPO phản ánh mức độ doanh nghiệp chiếm dụng vốn tín dụng thương mại từ các nhà cung cấp."),
         "formulas": ["DSO = (Khoản phải thu bình quân / Doanh thu thuần) x 365 ngày",
                      "DIO = (Hàng tồn kho bình quân / Giá vốn hàng bán) x 365 ngày",
                      "DPO = (Nợ phải trả người bán bình quân / Giá vốn hàng bán) x 365 ngày"],
         "case_studies": [{"title": "Thế Giới Di Động (Mobile World - MWG)", "detail": "Quản trị chuỗi cung ứng tối ưu hạ số ngày lưu kho DIO từ 90 ngày xuống 65 ngày đối với ngành hàng thiết bị điện thoại, máy tính bảng."}]},
        {"sec_num": 2, "sec_title": "Chu Kỳ Chuyển Hóa Tiền Mặt (CCC) và Vòng Quay Tổng Tài Sản",
         "content": ("Chu kỳ chuyển hóa tiền mặt (Cash Conversion Cycle - CCC) đo lường khoảng thời gian bằng ngày "
                     "từ khi doanh nghiệp chi tiền mặt mua nguyên vật liệu, hàng hóa đầu vào cho đến khi thực tế thu được tiền mặt "
                     "từ việc bán sản phẩm đó cho khách hàng:\n"
                     "CCC = DIO (Số ngày lưu kho) + DSO (Số ngày thu tiền) - DPO (Số ngày trả nợ người bán).\n\n"
                     "Mô hình chu kỳ tiền mặt âm (Negative Cash Conversion Cycle): "
                     "Xảy ra khi doanh nghiệp có quyền lực thương lượng rất lớn đối với nhà cung cấp (kéo dài DPO cực lớn) "
                     "trong khi bán hàng thu tiền mặt ngay (DIO và DSO cực ngắn). Doanh nghiệp hoạt động hoàn toàn bằng vốn chiếm dụng miễn phí của nhà cung cấp "
                     "(ví dụ điển hình: Amazon, Walmart, Thế Giới Di Động).\n\n"
                     "Vòng quay Tổng tài sản (Total Asset Turnover - ATO) = Doanh thu thuần / Tổng tài sản bình quân. "
                     "Đo lường mỗi 1 đồng tài sản đầu tư tạo ra được bao nhiêu đồng doanh thu."),
         "formulas": ["Chu kỳ chuyển hóa tiền mặt: CCC = DIO + DSO - DPO",
                      "Vòng quay tổng tài sản: ATO = Doanh thu thuần / Tổng tài sản bình quân",
                      "Vòng quay TSCĐ (FAT) = Doanh thu thuần / Nguyên giá ròng TSCĐ bình quân"],
         "case_studies": [{"title": "Mô Hình Bán Lẻ Siêu Thị WinMart (Masan)", "detail": "Chiến lược tối ưu hóa vốn lưu động với CCC đạt mức âm 15 ngày, tạo ra dòng tiền mặt hoạt động thặng dư tài trợ cho việc mở rộng điểm bán mới."}]}
    ]
    phd3 = {
        "topics": [
            "Lý thuyết Quản trị Vốn Lưu động và Giá trị Doanh nghiệp (Working Capital Management & Firm Value - Deloof 2003): Mối quan hệ hình chữ U ngược giữa Chu kỳ chuyển hóa tiền mặt (CCC) và Khả năng sinh lời của doanh nghiệp.",
            "Tín dụng Thương mại như một Kênh Thay thế Tín dụng Ngân hàng (Trade Credit vs Bank Credit - Petersen & Rajan 1997): Động cơ các nhà cung cấp cấp tín dụng cho khách hàng trong điều kiện thắt chặt tiền tệ.",
            "Chuyên đề Tiến sĩ: Nghiên cứu thực nghiệm về Tác động của Chu kỳ tiền mặt CCC đến Rủi ro thanh khoản và Giá trị thị trường cổ phiếu tại các nước mới nổi ASEAN."
        ]
    }
    q3 = [
        "Trình bày công thức và ý nghĩa kinh tế của Chu kỳ chuyển hóa tiền mặt (Cash Conversion Cycle - CCC).",
        "Thế nào là 'Chu kỳ chuyển hóa tiền mặt âm' (Negative CCC)? Doanh nghiệp cần những điều kiện gì để vận hành mô hình tiền mặt âm này?",
        "Phân tích mối quan hệ giữa Vòng quay các khoản phải thu (DSO), Vòng quay hàng tồn kho (DIO) và Vòng quay nợ phải trả (DPO)."
    ]
    b.add_chapter(3, "Phân tích Hiệu quả Hoạt động và Chu kỳ Kinh doanh", intro3, sec3, phd3, q3)
    
    # Chương 4
    intro4 = ("Chương 4 nghiên cứu khả năng sinh lời và kỹ thuật phân tích DuPont - "
              "mô hình phân rã toán học giúp khám phá các động lực cốt lõi tạo ra lợi nhuận cho cổ đông.")
    sec4 = [
        {"sec_num": 1, "sec_title": "Các Chỉ Tiêu Sinh Lời Hoạt Động (ROS, ROA, ROIC)",
         "content": ("Khả năng sinh lời là thước đo tổng hợp tối cao phản ánh năng lực cạnh tranh và hiệu quả sử dụng nguồn lực của doanh nghiệp:\n"
                     "(1) Tỷ suất Sinh lời trên Doanh thu (ROS - Return on Sales) = Lợi nhuận sau thuế / Doanh thu thuần. "
                     "Đo lường hiệu quả quản trị chi phí và năng lực định giá của sản phẩm.\n\n"
                     "(2) Tỷ suất Sinh lời trên Tài sản (ROA - Return on Assets) = Lợi nhuận sau thuế (hoặc EBIT) / Tổng tài sản bình quân. "
                     "Đo lường năng lực của ban giám đốc trong việc chuyển hóa tài sản đầu tư thành lợi nhuận, không phân biệt nguồn tài trợ bằng nợ hay vốn chủ.\n\n"
                     "(3) Tỷ suất Sinh lời trên Vốn Đầu tư (ROIC - Return on Invested Capital) = NOPAT / Vốn đầu tư hoạt động (Invested Capital). "
                     "Trong đó NOPAT = EBIT x (1 - Thuế suất). Doanh nghiệp chỉ tạo ra giá trị gia tăng kinh tế thực sự cho cổ đông khi ROIC > WACC (Chi phí sử dụng vốn bình quân)."),
         "formulas": ["Biên lợi nhuận gộp (Gross Margin) = Lợi nhuận gộp / Doanh thu thuần",
                      "ROA = Lợi nhuận sau thuế / Tổng tài sản bình quân",
                      "ROIC = [EBIT x (1 - t)] / [Vốn chủ sở hữu + Nợ vay tài chính - Tiền mặt dư thừa]",
                      "Chênh lệch tạo giá trị kinh tế = ROIC - WACC"],
         "case_studies": [{"title": "Công ty Cổ phần Sữa Việt Nam (Vinamilk - VNM)", "detail": "Duy trì biên lợi nhuận gộp trên 40% và ROIC vượt trội trên 30% liên tục trong hơn một thập kỷ nhờ thương hiệu quốc gia và vùng nguyên liệu tự chủ."}]},
        {"sec_num": 2, "sec_title": "Mô Hình Phân Tích DuPont Đa Nhân Tố",
         "content": ("Mô hình DuPont do Tập đoàn Hóa chất DuPont phát triển, phân rã chỉ tiêu Lợi nhuận trên vốn chủ sở hữu (ROE):\n\n"
                     "- Mô hình DuPont 3 nhân tố:\n"
                     "ROE = (Lợi nhuận sau thuế / Doanh thu) x (Doanh thu / Tổng tài sản) x (Tổng tài sản / Vốn chủ sở hữu)\n"
                     "ROE = Biên lợi nhuận ròng (ROS) x Vòng quay tài sản (ATO) x Đòn bẩy tài chính (FL).\n"
                     "Cho thấy 3 con đường tạo ra lợi nhuận cao: Bán hàng biên lãi cao, quay vòng vốn nhanh, hoặc sử dụng đòn bẩy tài chính lớn.\n\n"
                     "- Mô hình DuPont 5 nhân tố chi tiết:\n"
                     "ROE = Gánh nặng thuế x Gánh nặng lãi vay x Biên lợi nhuận hoạt động (EBIT Margin) x Vòng quay tài sản (ATO) x Đòn bẩy tài chính (FL).\n"
                     "Trong đó: Gánh nặng thuế = NI / EBT; Gánh nặng lãi vay = EBT / EBIT; EBIT Margin = EBIT / Doanh thu."),
         "formulas": ["Mô hình DuPont 3 nhân tố: ROE = Net Margin x Asset Turnover x Leverage Multiplier",
                      "Mô hình DuPont 5 nhân tố: ROE = (NI/EBT) x (EBT/EBIT) x (EBIT/Sales) x (Sales/Assets) x (Assets/Equity)"],
         "case_studies": [{"title": "So Sánh Mô Hình Hoạt Động Giữa Thế Giới Di Động (MWG) và Vinamilk (VNM)", "detail": "Vinamilk đạt ROE cao nhờ Biên lợi nhuận ròng vượt trội (High Margin), trong khi Thế Giới Di Động đạt ROE cao nhờ Vòng quay tài sản thần tốc (High Turnover)."}]}
    ]
    phd4 = {
        "topics": [
            "Lý thuyết Bền vững của Thu nhập DuPont (DuPont Component Persistence - Nissim & Penman 2001): Phân tích tính bền vững của Tỷ suất Lợi nhuận Hoạt động (Operating Profitability) so với tác động tạm thời của Đòn bẩy Tài chính.",
            "Bất thường Dồn tích Sloan (The Sloan Accrual Anomaly - Sloan 1996): Nhà đầu tư định giá sai thành phần dồn tích (Accruals) so với thành phần tiền mặt (Cash Flows) trong mô hình DuPont dẫn đến khả năng kiếm lợi nhuận bất thường.",
            "Chuyên đề Tiến sĩ: Ứng dụng mô hình phân tách DuPont kết hợp hồi quy dữ liệu bảng (Panel Data Fixed Effects) đánh giá tác động của Quản trị công ty đến tỷ suất ROE tại Việt Nam."
        ]
    }
    q4 = [
        "Trình bày công thức và phân tích ý nghĩa kinh tế của từng thành phần trong Mô hình DuPont 3 nhân tố và Mô hình DuPont 5 nhân tố.",
        "Phân biệt sự khác nhau căn bản giữa ROA (Return on Assets), ROE (Return on Equity) và ROIC (Return on Invested Capital).",
        "Một doanh nghiệp có thể làm tăng chỉ số ROE bằng cách tăng đòn bẩy nợ vay (Assets/Equity). Chiến lược này hàm chứa những rủi ro gì đối với cổ đông?"
    ]
    b.add_chapter(4, "Phân tích Khả năng Sinh lời và Mô hình DuPont", intro4, sec4, phd4, q4)
    
    # Chương 5
    intro5 = ("Chương 5 nghiên cứu phân tích báo cáo lưu chuyển tiền tệ và phát hiện các dấu hiệu bóp méo, gian lận BCTC. "
              "Trọng tâm là mô hình định lượng Beneish M-Score và phân tích dòng tiền tự do (FCFF / FCFE).")
    sec5 = [
        {"sec_num": 1, "sec_title": "Chất Lượng Dòng Tiền và Mối Quan Hệ Với Lợi Nhuận",
         "content": ("Lợi nhuận là một con số kế toán dồn tích (có thể bị thao túng bởi các ước tính chủ quan), "
                     "trong khi Dòng tiền từ hoạt động kinh doanh (CFO) là tiền mặt thực tế chảy vào tài khoản. "
                     "Đánh giá chất lượng lợi nhuận qua ma trận quan hệ Lợi nhuận và Dòng tiền:\n"
                     "- Mẫu hình Tốt nhất: Lợi nhuận thuần dương và CFO dương, trong đó CFO > Lợi nhuận thuần. "
                     "Cho thấy lợi nhuận có chất lượng cao, được bảo đảm bằng tiền mặt thực tế thu hồi.\n"
                     "- Mẫu hình Đáng ngờ: Lợi nhuận tăng trưởng đều đặn qua các năm nhưng CFO âm liên tục hoặc suy giảm nghiêm trọng. "
                     "Đây là dấu hiệu kinh điển của việc ghi nhận doanh thu non, nợ đọng khó đòi hoặc hàng hóa tồn kho ứ đọng không bán được.\n\n"
                     "Dòng tiền tự do (Free Cash Flow):\n"
                     "- Dòng tiền tự do của doanh nghiệp: FCFF = CFO + Chi phí lãi vay x (1 - t) - Chi tiêu mua sắm TSCĐ (CAPEX).\n"
                     "- Dòng tiền tự do của vốn chủ sở hữu: FCFE = CFO - CAPEX + Vay nợ ròng mới."),
         "formulas": ["Hệ số chuyển hóa tiền mặt = CFO / Lợi nhuận sau thuế (Ngưỡng an toàn: > 1.0)",
                      "Dòng tiền tự do FCF = CFO - CAPEX",
                      "Độ bao phủ nợ bằng dòng tiền = CFO / Tổng nợ vay"],
         "case_studies": [{"title": "Tập đoàn Xây dựng FLC", "detail": "Phân tích chuỗi các niên độ tài chính có lợi nhuận kế toán dương hàng trăm tỷ đồng nhưng dòng tiền kinh doanh CFO âm hàng nghìn tỷ đồng trước thời điểm khởi tố lãnh đạo tập đoàn."}]},
        {"sec_num": 2, "sec_title": "Nhận Diện Gian Lận BCTC và Mô Hình Beneish M-Score",
         "content": ("Mô hình Beneish M-Score (Messod Beneish 1999) là mô hình kinh tế lượng xác suất "
                     "sử dụng 8 biến số tài chính để tính toán xác suất doanh nghiệp thao túng báo cáo tài chính (Earnings Manipulation):\n"
                     "(1) DSRI (Days Sales in Receivables Index): Chỉ số số ngày thu tiền phải thu (phát hiện ghi nhận doanh thu ảo).\n"
                     "(2) GMI (Gross Margin Index): Chỉ số biên lợi nhuận gộp (biên lãi suy giảm thúc đẩy động cơ gian lận).\n"
                     "(3) AQI (Asset Quality Index): Chỉ số chất lượng tài sản (tỷ lệ tài sản vô hình và chi phí hoãn lại).\n"
                     "(4) SGI (Sales Growth Index): Chỉ số tăng trưởng doanh thu.\n"
                     "(5) DEPI (Depreciation Index): Chỉ số tốc độ khấu hao (giảm tỷ lệ khấu hao để tăng lợi nhuận).\n"
                     "(6) SGAI (Sales, General and Administrative expenses Index): Chỉ số chi phí bán hàng và QLDN.\n"
                     "(7) LVGI (Leverage Index): Chỉ số đòn bẩy nợ vay.\n"
                     "(8) TATA (Total Accruals to Total Assets): Tỷ lệ các khoản dồn tích trên tổng tài sản.\n\n"
                     "Quy tắc đánh giá: Nếu M-Score > -1.78, doanh nghiệp có xác suất rất cao đang thao túng lợi nhuận (Enron có M-Score = -0.05)."),
         "formulas": ["M-Score = -4.84 + 0.920*DSRI + 0.528*GMI + 0.404*AQI + 0.892*SGI + 0.115*DEPI - 0.172*SGAI + 4.037*TATA + 0.0327*LVGI",
                      "Ngưỡng cảnh báo: M-Score > -1.78 -> Nguy cơ thao túng báo cáo tài chính cao"],
         "case_studies": [{"title": "Vụ Gian Lận BCTC Enron Phát Hiện Bởi Beneish M-Score", "detail": "Ứng dụng mô hình Beneish đã cảnh báo chính xác rủi ro gian lận của Enron trước khi tập đoàn này tuyên bố phá sản 1 năm."}]}
    ]
    phd5 = {
        "topics": [
            "Mô hình Nhận diện Thao túng Lợi nhuận Thực tính so với Thao túng Hoạt động Thực tế (Accrual-based vs Real Earnings Management - Roychowdhury 2006, Cohen & Zarowin 2010): Phân tích chi phí cơ hội dài hạn khi doanh nghiệp cắt giảm chi phí R&D, quảng cáo để làm đẹp lợi nhuận ngắn hạn.",
            "Lý thuyết Trò chơi trong Kiểm toán và Báo cáo Tài chính (Strategic Audit Interaction & Fraud Detection): Động cơ của ban quản lý trong việc che giấu thông tin xấu và năng lực phát hiện của kiểm toán viên độc lập.",
            "Chuyên đề Tiến sĩ: Ứng dụng Mô hình Beneish M-Score hiệu chỉnh trên tập dữ liệu bảng các doanh nghiệp niêm yết tại Sở Giao dịch Chứng khoán TP.HCM (HOSE)."
        ]
    }
    q5 = [
        "Tại sao doanh nghiệp có lợi nhuận kế toán sau thuế dương nhưng dòng tiền thuần từ hoạt động kinh doanh (CFO) âm liên tục lại là một dấu hiệu cảnh báo rủi ro phá sản nghiêm trọng?",
        "Trình bày ý nghĩa và công thức tính Dòng tiền tự do của doanh nghiệp (FCFF) và Dòng tiền tự do vốn chủ sở hữu (FCFE).",
        "Nêu các biến số chính trong Mô hình Beneish M-Score và giải thích ngưỡng giá trị cảnh báo nguy cơ thao túng báo cáo tài chính."
    ]
    b.add_chapter(5, "Phân tích Báo cáo Lưu chuyển Tiền tệ và Khả năng Tạo tiền", intro5, sec5, phd5, q5)
    
    # Chương 6
    intro6 = ("Chương 6 tổng kết toàn bộ quy trình phân tích BCTC qua kỹ thuật lập dự báo tài chính tương lai "
              "và các mô hình định lượng cảnh báo sớm nguy cơ kiệt quệ tài chính (Financial Distress) và phá sản.")
    sec6 = [
        {"sec_num": 1, "sec_title": "Phương Pháp Dự Báo Tài Chính và Nhu Cầu Vốn Bên Ngoài (AFN)",
         "content": ("Dự báo tài chính là việc lập các Báo cáo tài chính dự kiến (Pro-forma Financial Statements) cho các năm tới "
                     "căn cứ vào kế hoạch tăng trưởng doanh thu và các mối quan hệ tỷ lệ tài chính lịch sử.\n\n"
                     "Phương pháp Tỷ lệ phần trăm trên Doanh thu (Percentage of Sales Method):\n"
                     "- Giả định các khoản mục tài sản (tiền mặt, phải thu, hàng tồn kho) và các khoản mục nợ tự phát sinh (phải trả người bán, chi phí trích trước) "
                     "tăng trưởng cùng tỷ lệ với tốc độ tăng trưởng doanh thu.\n"
                     "- Xác định Nhu cầu Vốn Bổ sung Bên ngoài (Additional Funds Needed - AFN):\n"
                     "AFN = Gia tăng Tài sản cần thiết - Gia tăng Nợ tự phát sinh - Lợi nhuận giữ lại bổ sung trong kỳ.\n\n"
                     "Nếu AFN > 0: Doanh nghiệp thiếu vốn và bắt buộc phải huy động thêm từ vay nợ ngân hàng hoặc phát hành cổ phiếu mới.\n"
                     "Nếu AFN < 0: Doanh nghiệp có thặng dư vốn và có thể dùng để trả bớt nợ hoặc chia cổ tức tiền mặt."),
         "formulas": ["AFN = (A*/S0) * ΔS - (L*/S0) * ΔS - M * S1 * (1 - d)",
                      "Trong đó: A*/S0 là Tỷ lệ tài sản tự phát sinh; L*/S0 là Tỷ lệ nợ tự phát sinh; M là Biên lợi nhuận ròng; S1 là Doanh thu năm tới; d là Tỷ lệ chi trả cổ tức",
                      "Tốc độ tăng trưởng nội tại (Internal Growth Rate - IGR) = (ROA x b) / [1 - (ROA x b)]",
                      "Tốc độ tăng trưởng bền vững (Sustainable Growth Rate - SGR) = (ROE x b) / [1 - (ROE x b)] (với b là Tỷ lệ lợi nhuận giữ lại)"],
         "case_studies": [{"title": "Kế Hoạch Mở Rộng Hệ Thống Trang Trại Sữa Mộc Châu (MCM)", "detail": "Tính toán chỉ số AFN và tốc độ tăng trưởng bền vững SGR khi lập kế hoạch đầu tư tổ hợp chăn nuôi bò sữa công nghệ cao trị giá 1.000 tỷ đồng."}]},
        {"sec_num": 2, "sec_title": "Các Mô Hình Cảnh Báo Sớm Phá Sản (Altman Z-Score & Ohlson O-Score)",
         "content": ("(1) Mô hình Altman Z-Score (Edward Altman 1968) cho doanh nghiệp sản xuất niêm yết:\n"
                     "Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 0.999*X5\n"
                     "Trong đó:\n"
                     "- X1 = Vốn lưu động ròng / Tổng tài sản (Khả năng thanh khoản).\n"
                     "- X2 = Lợi nhuận giữ lại lũy kế / Tổng tài sản (Tuổi thọ và tích lũy vốn).\n"
                     "- X3 = EBIT / Tổng tài sản (Hiệu quả sinh lời của tài sản).\n"
                     "- X4 = Giá trị thị trường vốn chủ sở hữu / Giá trị sổ sách tổng nợ (Mức độ an toàn đòn bẩy).\n"
                     "- X5 = Doanh thu thuần / Tổng tài sản (Vòng quay tổng tài sản).\n\n"
                     "Phân vùng đánh giá rủi ro Z-Score:\n"
                     "- Z > 2.99: Vùng An toàn (Safe Zone) - Nguy cơ phá sản rất thấp.\n"
                     "- 1.81 <= Z <= 2.99: Vùng Xám (Grey Zone) - Cần theo dõi chặt chẽ.\n"
                     "- Z < 1.81: Vùng Nguy hiểm (Distress Zone) - Xác suất phá sản trong vòng 2 năm tới là rất cao.\n\n"
                     "(2) Mô hình Ohlson O-Score (1980): Sử dụng mô hình hồi quy Logistic đa biến kết hợp 9 biến số tài chính, "
                     "khắc phục các hạn chế của phân tích biệt số MDA trong mô hình Altman."),
         "formulas": ["Mô hình Altman Z'-Score (Cho doanh nghiệp chưa niêm yết): Z' = 0.717*X1 + 0.847*X2 + 3.107*X3 + 0.420*X4 + 0.998*X5",
                      "Ngưỡng Z': Z' > 2.9 (An toàn); 1.23 <= Z' <= 2.9 (Cảnh báo); Z' < 1.23 (Nguy cơ phá sản cao)"],
         "case_studies": [{"title": "Chấm Điểm Rủi Ro Tín Dụng Doanh Nghiệp Ngành Thép (POM)", "detail": "Áp dụng mô hình Altman Z-Score nhận diện chỉ số Z rơi xuống vùng nguy hiểm 0.8 do đòn bẩy nợ vay quá lớn và thua lỗ triền miên."}]}
    ]
    phd6 = {
        "topics": [
            "Lý thuyết Cấu trúc Dự báo Phá sản Merton (Merton Structural Credit Risk Model 1974): Mô hình quyền chọn Black-Scholes đo lường Khoảng cách đến Vỡ nợ (Distance to Default - DD) của doanh nghiệp.",
            "So sánh Mô hình Thống kê Truyền thống (Logit, Probit) với Thuật toán Trí tuệ Nhân tạo (XGBoost, Random Forest, Neural Networks) trong Dự báo Kiệt quệ Tài chính Doanh nghiệp (Financial Distress Prediction).",
            "Chuyên đề Tiến sĩ: Xây dựng Mô hình Định giá Rủi ro Vỡ nợ Doanh nghiệp tích hợp dữ liệu vĩ mô và vi mô cho các doanh nghiệp phát hành trái phiếu doanh nghiệp tại Việt Nam."
        ]
    }
    q6 = [
        "Trình bày phương pháp tính Nhu cầu Vốn Bổ sung Bên ngoài (AFN) theo Phương pháp tỷ lệ phần trăm trên doanh thu.",
        "Phân biệt Tốc độ tăng trưởng nội tại (Internal Growth Rate - IGR) và Tốc độ tăng trưởng bền vững (Sustainable Growth Rate - SGR).",
        "Trình bày 5 biến số trong Mô hình Altman Z-Score và phân tích các vùng rủi ro (Vùng an toàn, Vùng xám, Vùng nguy hiểm)."
    ]
    b.add_chapter(6, "Dự báo Tài chính và Mô hình Cảnh báo Sớm Phá sản", intro6, sec6, phd6, q6)
    
    out_dir = os.path.join(BASE_DIR, r"02_Kế toán & Kiểm toán\[NEU] Phân tích báo cáo tài chính - PGS.TS Nguyễn Năng Phúc (NXB ĐHKTQD)")
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Phân tích báo cáo tài chính - PGS.TS Nguyễn Năng Phúc (NXB ĐHKTQD).pdf")
    pages, size_mb = b.save(out_pdf)
    print(f"-> Hoàn thành Sách 6: {pages} trang, {size_mb:.2f} MB. Lưu tại: {out_pdf}")
    return {"book": "Phân tích báo cáo tài chính", "pages": pages, "size_mb": size_mb, "path": out_pdf}


if __name__ == "__main__":
    r4 = build_book_4()
    r5 = build_book_5()
    r6 = build_book_6()
    results = [r4, r5, r6]
    with open(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_agent_2_batch2_res.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("XONG BATCH 2 TOÀN VĂN!")
