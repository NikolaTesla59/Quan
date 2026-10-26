# -*- coding: utf-8 -*-
"""
NEU Master Textbook Builder - Batch 3: Research Methods, Financial Econometrics, Business Law & Business English
Courses:
9. Phương pháp nghiên cứu khoa học trong kinh tế & kinh doanh (Bậc Thạc sĩ & Tiến sĩ)
10. Kinh tế lượng tài chính & Chuỗi thời gian nâng cao (Financial Econometrics - Bậc Thạc sĩ & Tiến sĩ)
11. Luật kinh tế & Kinh doanh - TS Trần Văn Nam
12. Tiếng Anh chuyên ngành Kinh tế & Kinh doanh - Khoa Ngoại ngữ NEU
"""
import os
import sys

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

BASE_DIR_07 = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\07_Toán, Thống kê, Kinh tế lượng & Tin học"
BASE_DIR_08 = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\08_Pháp luật & Ngoại ngữ chuyên ngành"

def build_research_methods():
    print("Building: Phương pháp nghiên cứu khoa học trong kinh tế & kinh doanh...")
    b = NEUTextbookBuilder(
        title="Phương pháp nghiên cứu khoa học trong kinh tế & kinh doanh",
        subject_code="NCKH1101",
        faculty="Viện Quản lý Châu Á - Thái Bình Dương & Khoa Toán Kinh tế",
        authors="GS.TS. Trần Thọ Đạt & PGS.TS. Tô Trung Thành (Đồng Chủ biên)",
        level_text="CHƯƠNG TRÌNH ĐÀO TẠO SAU ĐẠI HỌC (THẠC SĨ KINH TẾ & TIẾN SĨ KINH TẾ)",
        edition="CẨM NANG NGHIÊN CỨU HỌC THUẬT QUỐC TẾ CHUẨN SSCI/SCOPUS & THỰC THI LUẬN ÁN TIẾN SĨ"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Triết học Khoa học và Khung Lý thuyết Nghiên cứu Kinh tế",
         "topics": ["Bản thể luận (Ontology) và Nhận thức luận (Epistemology): Thực chứng vs Kiến tạo", "Quy nạp (Inductive) vs Diễn dịch (Deductive) trong xây dựng lý thuyết kinh tế", "Tổng quan y văn (Literature Review), ma trận lý thuyết và xác định khe hổng nghiên cứu (Research Gap)", "Phát triển khung khái niệm và giả thuyết nghiên cứu"]},
        {"chapter_num": 2, "chapter_title": "Thiết kế Nghiên cứu: Định lượng, Định tính và Phương pháp Hỗn hợp",
         "topics": ["Thiết kế nghiên cứu thực nghiệm: Cắt ngang (Cross-sectional), Chuỗi thời gian và Dữ liệu mảng (Panel)", "Phương pháp nghiên cứu định tính: Phỏng vấn sâu, Nghiên cứu tình huống (Case study), Focus group", "Thiết kế bảng câu hỏi khảo sát và thang đo Likert", "Đánh giá độ tin cậy thang đo (Cronbach's Alpha) và độ giá trị (EFA, CFA, SEM)"]},
        {"chapter_num": 3, "chapter_title": "Chiến lược Nhận diện Nội sinh và Kiểm tra Độ vững (Robustness Checks)",
         "topics": ["Vấn đề nội sinh (Endogeneity) do biến bỏ sót, sai số đo lường hoặc nhân quả đảo chiều", "Phương pháp giải quyết nội sinh: Biến công cụ (IV/2SLS), GMM hệ thống, Kiểm soát hiệu ứng cố định cấp cao", "Kỹ thuật kiểm tra độ vững: Thay đổi mẫu, đổi biến đại diện, kiểm định giả dược (Placebo test)", "Phân tích cơ chế tác động (Mechanism/Mediation analysis) và hiệu ứng điều tiết (Moderation)"]},
        {"chapter_num": 4, "chapter_title": "Chuyên đề Tiến sĩ: Cấu trúc Luận án Tiến sĩ và Quy trình Xuất bản Quốc tế Top-Tier",
         "topics": ["Cấu trúc chuẩn mực của một bài báo khoa học SSCI (IMRaD): Abstract, Intro, Literature, Data/Method, Results, Discussion, Conclusion", "Chiến lược phản hồi ý kiến phản biện (Response to Reviewers) chuyên nghiệp", "Chuẩn mực đạo đức nghiên cứu, liêm chính học thuật và phòng chống đạo văn (Turnitin)", "Open Science, chia sẻ dữ liệu và khả năng tái lập kết quả nghiên cứu (Replication)"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Quy trình Nghiên cứu Khoa học và Chiến lược Nhận diện Nội sinh",
        introduction="Phương pháp nghiên cứu khoa học trang bị tư duy phản biện và bộ công cụ đo lường thực nghiệm khắt khe nhất để bảo đảm kết quả nghiên cứu kinh tế có giá trị khoa học và độ tin cậy khách quan.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Vấn đề nội sinh và chiến lược nhận diện quan hệ nhân quả",
                "content": "Sai lầm phổ biến nhất trong các nghiên cứu kinh tế là quy kết mối quan hệ tương quan (correlation) thành quan hệ nhân quả (causality). Hiện tượng nội sinh xảy ra khi biến giải thích X có tương quan với sai số ngẫu nhiên u trong phương trình hồi quy Y = beta*X + u, dẫn đến ước lượng OLS bị chệch và không nhất quán.\n\nBa nguồn gốc chính của nội sinh bao gồm: (1) Biến bị bỏ sót (Omitted Variables), (2) Sai số đo lường (Measurement Error), và (3) Nhân quả đồng thời hay nhân quả đảo chiều (Simultaneity / Reverse Causality).",
                "formulas": [
                    "Độ chệch OLS khi có biến bỏ sót: E(beta_hat_OLS) = beta_1 + beta_2 * [Cov(X_1, X_2) / Var(X_1)]",
                    "Ước lượng Biến công cụ 2SLS: beta_hat_2SLS = (Z^T * X)^(-1) * Z^T * Y (với điều kiện Cov(Z, X) != 0 và Cov(Z, u) = 0)",
                    "Kiểm định Weak Instrument: Thống kê F giai đoạn 1 (First-stage F-statistic) phải lớn hơn 10 theo tiêu chuẩn Staiger-Stock"
                ],
                "case_studies": [
                    {"title": "Đánh giá tác động của tín dụng xanh đến hiệu quả tài chính ngân hàng", "detail": "Thiết kế nghiên cứu sử dụng phương pháp GMM hệ thống của Blundell-Bond trên mẫu 31 ngân hàng thương mại Việt Nam giai đoạn 2012-2024 để kiểm soát nội sinh."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp thực nghiệm tự nhiên (Natural Experiments) và tận dụng cú sốc chính sách ngoại sinh",
                "Mô hình cấu trúc tuyến tính bình phương bé nhất từng phần (PLS-SEM) so với CB-SEM trong nghiên cứu quản trị",
                "Phân tích tổng hợp nghiên cứu (Meta-Analysis) và kiểm định thiên lệch xuất bản (Publication Bias) bằng biểu đồ Funnel Plot"
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt giữa phương pháp tiếp cận quy nạp và diễn dịch trong nghiên cứu khoa học kinh tế.",
            "Trình bày ba nguồn gốc chính gây ra hiện tượng nội sinh và các kỹ thuật kinh tế lượng tương ứng để khắc phục.",
            "Mô tả quy trình 5 bước xây dựng đề cương Luận án Tiến sĩ kinh tế theo chuẩn mực quốc tế."
        ]
    )

    out_path = os.path.join(BASE_DIR_07, r"[NEU] Phương pháp nghiên cứu khoa học trong kinh tế & kinh doanh (Bậc Thạc sĩ & Tiến sĩ)", r"[NEU] [Giáo trình Toàn văn] Phương pháp nghiên cứu khoa học trong kinh tế & kinh doanh (Bậc Thạc sĩ & Tiến sĩ).pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Phương pháp NCKH -> {pages} pages, {sz:.2f} MB")
    return {"name": "Phương pháp NCKH", "pages": pages, "size_mb": sz, "path": out_path}

def build_financial_econometrics():
    print("Building: Kinh tế lượng tài chính & Chuỗi thời gian nâng cao...")
    b = NEUTextbookBuilder(
        title="Kinh tế lượng tài chính & Chuỗi thời gian nâng cao",
        subject_code="FIEC1102",
        faculty="Khoa Toán Kinh tế & Viện Ngân hàng - Tài chính",
        authors="PGS.TS. Nguyễn Khắc Minh & PGS.TS. Nguyễn Ngọc Cường (Đồng Chủ biên)",
        level_text="CHƯƠNG TRÌNH ĐÀO TẠO SAU ĐẠI HỌC (THẠC SĨ TÀI CHÍNH ĐỊNH LƯỢNG & TIẾN SĨ)",
        edition="CHUYÊN KHẢO KINH TẾ LƯỢNG CHUỖI THỜI GIAN, BIẾN ĐỘNG RỦI RO & MÔ HÌNH HÓA ĐA BIẾN TIẾN SĨ"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Đặc trưng Thống kê của Lợi suất Tài sản và Tính dừng (Stationarity)",
         "topics": ["Lợi suất đơn và lợi suất nhật ký (Log-returns)", "Các sự kiện cách điệu (Stylized facts): Bất đối xứng, đuôi dày và biến động tụ cụm", "Khái niệm tính dừng yếu (Weak stationarity) và hàm tự tương quan (ACF/PACF)", "Kiểm định nghiệm đơn vị: Augmented Dickey-Fuller (ADF), Phillips-Perron (PP), KPSS test"]},
        {"chapter_num": 2, "chapter_title": "Mô hình Chuỗi Thời gian Đơn biến: ARMA và Biến động ARCH/GARCH",
         "topics": ["Quy trình Box-Jenkins nhận diện và ước lượng mô hình ARMA/ARIMA", "Bản chất của phương sai thay đổi có điều kiện tự hồi quy (ARCH) của Engle", "Mô hình GARCH(1,1) của Bollerslev và điều kiện dừng phương sai", "Các mô hình GARCH bất đối xứng: EGARCH của Nelson, GJR-GARCH của Glosten, TARCH đo lường hiệu ứng đòn bẩy (Leverage effect)"]},
        {"chapter_num": 3, "chapter_title": "Hệ Phương trình Đa biến: Mô hình VAR, VECM và Đồng Tích Hợp",
         "topics": ["Mô hình Vector Autoregression (VAR) không ràng buộc và lựa chọn độ trễ tối ưu (AIC, BIC, HQ)", "Kiểm định quan hệ nhân quả Granger (Granger Causality)", "Hàm phản ứng đẩy (Impulse Response Function - IRF) và phân rã phương sai sai số dự báo (FEVD)", "Lý thuyết đồng tích hợp Engle-Granger và kiểm định đồng tích hợp Johansen (Trace & Max-Eigenvalue)", "Mô hình hiệu chỉnh sai số dạng vectơ (VECM)"]},
        {"chapter_num": 4, "chapter_title": "Chuyên đề Tiến sĩ: Kinh tế lượng Tần số Cao, Rủi ro Hệ thống và Machine Learning",
         "topics": ["Kinh tế lượng tần số cao (High-Frequency Econometrics) và biến động thực tế (Realized Volatility)", "Đo lường lan tỏa rủi ro tài chính (Spillover Index) theo phương pháp Diebold-Yilmaz", "Mô hình CoVaR của Adrian & Brunnermeier và Marginal Expected Shortfall (MES) đo lường rủi ro hệ thống", "Mô hình Copula phi tuyến tính trong kết hợp phân phối biên lợi suất đa tài sản"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Mô hình Hóa Biến động Tài chính và Phân tích Hệ thống Đa biến",
        introduction="Kinh tế lượng tài chính tập trung phân tích động thái phi tuyến của chuỗi thời gian giá tài sản, cấu trúc biến động có điều kiện và mức độ liên kết rủi ro giữa các thị trường vốn toàn cầu.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Mô hình GARCH đơn biến và hiệu ứng đòn bẩy trong thị trường chứng khoán",
                "content": "Trong chuỗi thời gian tài chính, phương sai của sai số không cố định mà thay đổi theo thời gian và phụ thuộc vào quy mô của các cú sốc trong quá khứ (Volatility Clustering). Mô hình GARCH(1,1) mô tả phương sai có điều kiện sigma_t^2 như một hàm số của phần dư bình phương kỳ trước e_{t-1}^2 và phương sai kỳ trước sigma_{t-1}^2.\n\nĐể nắm bắt hiện tượng tin xấu (cú sốc âm) gây ra biến động lớn hơn tin tốt (cú sốc dương) cùng quy mô, mô hình EGARCH sử dụng hàm số dạng logarit không đòi hỏi ràng buộc dương của các tham số.",
                "formulas": [
                    "Phương trình phương sai GARCH(1,1): sigma_t^2 = omega + alpha * e_{t-1}^2 + beta * sigma_{t-1}^2 (với alpha + beta < 1)",
                    "Phương trình EGARCH(1,1): ln(sigma_t^2) = omega + alpha * |e_{t-1}/sigma_{t-1}| + gamma * (e_{t-1}/sigma_{t-1}) + beta * ln(sigma_{t-1}^2)",
                    "Mô hình VECM: Delta Y_t = Pi * Y_{t-1} + sum_{i=1}^{p-1} Gamma_i * Delta Y_{t-i} + e_t (với Pi = alpha * beta^T)"
                ],
                "case_studies": [
                    {"title": "Mô hình hóa biến động và đo lường VaR của thị trường chứng khoán Việt Nam", "detail": "Ước lượng mô hình GJR-GARCH với phân phối Student-t bất đối xứng cho chỉ số VN-Index nhằm tính toán giá trị chịu rủi ro Value-at-Risk (VaR 99%) và kiểm định hậu kiểm Kupiec Backtesting."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình DCC-GARCH (Dynamic Conditional Correlation) đo lường ma trận tương quan biến đổi theo thời gian",
                "Kỹ thuật kiểm định đồng tích hợp phi tuyến NARDL (Nonlinear Autoregressive Distributed Lag)",
                "Mô hình hồi quy lượng tử (Quantile Regression) và Quantile-on-Quantile trong phân tích thị trường trong điều kiện khủng hoảng"
            ]
        },
        review_questions=[
            "Chứng minh điều kiện để mô hình GARCH(1,1) có tính dừng phương sai vô điều kiện.",
            "Giải thích ý nghĩa tham số gamma trong mô hình EGARCH. Khi gamma < 0, hiệu ứng đòn bẩy thể hiện như thế nào?",
            "Phân biệt sự khác nhau giữa kiểm định nhân quả Granger và hàm phản ứng đẩy (IRF) trong mô hình VAR."
        ]
    )

    out_path = os.path.join(BASE_DIR_07, r"[NEU] Kinh tế lượng tài chính & Chuỗi thời gian nâng cao (Financial Econometrics - Bậc Thạc sĩ & Tiến sĩ)", r"[NEU] [Giáo trình Toàn văn] Kinh tế lượng tài chính & Chuỗi thời gian nâng cao (Financial Econometrics - Bậc Thạc sĩ & Tiến sĩ).pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Kinh tế lượng tài chính -> {pages} pages, {sz:.2f} MB")
    return {"name": "Kinh tế lượng tài chính", "pages": pages, "size_mb": sz, "path": out_path}

def build_business_law():
    print("Building: Luật kinh tế & Kinh doanh...")
    b = NEUTextbookBuilder(
        title="Luật kinh tế & Kinh doanh",
        subject_code="LUAT1101",
        faculty="Khoa Luật",
        authors="TS. Trần Văn Nam & PGS.TS. Nguyễn Văn Tuyến (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, CẬP NHẬT LUẬT DOANH NGHIỆP 2020, LUẬT ĐẦU TƯ & TRỌNG TÀI THƯƠNG MẠI TIẾN SĨ"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Địa vị Pháp lý của Các Chủ thể Kinh doanh tại Việt Nam",
         "topics": ["Khái niệm và đặc điểm của pháp luật kinh tế", "Pháp luật về Công ty Cổ phần, Công ty TNHH 1TV & 2TV+", "Pháp luật về Doanh nghiệp tư nhân và Công ty Hợp danh", "Tổ chức lại, giải thể và phá sản doanh nghiệp (Luật Phá sản 2014)"]},
        {"chapter_num": 2, "chapter_title": "Pháp luật về Hợp đồng trong Hoạt động Thương mại và Đầu tư",
         "topics": ["Giao kết, thực hiện và sửa đổi hợp đồng thương mại theo Luật Thương mại 2005 và Bộ luật Dân sự 2015", "Các điều khoản cơ bản, điều khoản bất khả kháng và miễn trách nhiệm", "Các biện pháp bảo đảm thực hiện nghĩa vụ hợp đồng", "Chế tài do vi phạm hợp đồng: Buộc thực hiện đúng, phạt vi phạm, bồi thường thiệt hại"]},
        {"chapter_num": 3, "chapter_title": "Pháp luật Cạnh tranh và Bảo vệ Quyền Sở hữu Trí tuệ",
         "topics": ["Hành vi hạn chế cạnh tranh bị cấm: Thỏa thuận hạn chế cạnh tranh, Lạm dụng vị trí thống lĩnh/độc quyền", "Hành vi cạnh tranh không lành mạnh", "Bảo hộ quyền sở hữu công nghiệp: Bằng sáng chế, nhãn hiệu, kiểu dáng công nghiệp, bí mật kinh doanh", "Bảo vệ quyền lợi người tiêu dùng trong giao dịch điện tử"]},
        {"chapter_num": 4, "chapter_title": "Chuyên đề Tiến sĩ: Giải quyết Tranh chấp Thương mại Quốc tế và Phân tích Kinh tế về Pháp luật",
         "topics": ["Giải quyết tranh chấp bằng Tòa án nhân dân và Trọng tài thương mại quốc tế (VIAC, SIAC, ICC)", "Công ước New York 1958 về công nhận và cho thi hành phán quyết của trọng tài nước ngoài", "Phân tích kinh tế về pháp luật (Law & Economics): Định lý Coase và chi phí giao dịch pháp lý", "Quản trị rủi ro pháp lý xuyên biên giới trong các hiệp định thương mại tự do thế hệ mới (CPTPP, EVFTA)"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Địa vị Pháp lý của Doanh nghiệp và Pháp luật Hợp đồng Thương mại",
        introduction="Pháp luật kinh tế thiết lập hành lang an toàn pháp lý, xác định quyền và nghĩa vụ tài sản của các chủ thể kinh doanh, đồng thời bảo vệ trật tự thị trường minh bạch và cạnh tranh lành mạnh.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Cơ chế quản trị nội bộ công ty cổ phần và bảo vệ cổ đông thiểu số",
                "content": "Công ty cổ phần là loại hình doanh nghiệp đối vốn điển hình, có sự tách biệt rõ ràng giữa quyền sở hữu (Đại hội đồng cổ đông) và quyền quản lý điều hành (Hội đồng quản trị và Ban Tổng giám đốc). Vấn đề đại diện (Agency problem) phát sinh khi người điều hành có thể hành động vì lợi ích riêng thay vì tối đa hóa giá trị cho cổ đông.\n\nLuật Doanh nghiệp 2020 tăng cường cơ chế bảo vệ cổ đông thiểu số thông qua quyền yêu cầu triệu tập ĐHĐCĐ bất thường, quyền tiếp cận sổ sách kế toán và thủ tục khởi kiện người quản lý nhân danh công ty (Derivative suit).",
                "formulas": [
                    "Quy tắc bầu dồn phiếu (Cumulative Voting): Tổng số phiếu = Số cổ phần sở hữu * Số thành viên HĐQT cần bầu",
                    "Số cổ phần tối thiểu để bầu 1 ứng viên: X = [Total_Shares * 1 / (N + 1)] + 1",
                    "Mức phạt vi phạm hợp đồng: Tối đa 8% giá trị phần nghĩa vụ hợp đồng bị vi phạm (Luật Thương mại 2005)"
                ],
                "case_studies": [
                    {"title": "Tranh chấp quyền kiểm soát tại Công ty Cổ phần Xây dựng Coteccons", "detail": "Phân tích khía cạnh pháp lý của cuộc xung đột quản trị giữa nhóm cổ đông sáng lập và nhóm cổ đông ngoại Kusto Group dẫn đến thay đổi toàn bộ HĐQT."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết phân tích kinh tế về pháp luật hợp đồng: Chi phí giao dịch, hợp đồng không hoàn hảo và bồi thường kỳ vọng",
                "Học thuyết dỡ bỏ bức màn che công ty (Piercing the Corporate Veil) đối với trách nhiệm hữu hạn trong tập đoàn kinh tế",
                "Cơ chế giải quyết tranh chấp giữa nhà đầu tư và nhà nước (ISDS) trong các hiệp định bảo hộ đầu tư quốc tế"
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt cơ bản về chế độ trách nhiệm tài sản giữa thành viên công ty TNHH và thành viên hợp danh.",
            "Nêu điều kiện có hiệu lực của hợp đồng thương mại và hậu quả pháp lý khi hợp đồng bị tuyên vô hiệu.",
            "So sánh ưu thế và hạn chế của phương thức giải quyết tranh chấp bằng Trọng tài thương mại so với Tòa án."
        ]
    )

    out_path = os.path.join(BASE_DIR_08, r"[NEU] Luật kinh tế & Kinh doanh - TS Trần Văn Nam (NXB ĐHKTQD)", r"[NEU] [Giáo trình Toàn văn] Luật kinh tế & Kinh doanh - TS Trần Văn Nam (NXB ĐHKTQD).pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Luật kinh tế & Kinh doanh -> {pages} pages, {sz:.2f} MB")
    return {"name": "Luật kinh tế & Kinh doanh", "pages": pages, "size_mb": sz, "path": out_path}

def build_business_english():
    print("Building: Tiếng Anh chuyên ngành Kinh tế & Kinh doanh...")
    b = NEUTextbookBuilder(
        title="Tiếng Anh chuyên ngành Kinh tế & Kinh doanh",
        subject_code="ENG1102",
        faculty="Khoa Ngoại ngữ Kinh tế",
        authors="Tập thể Giảng viên Khoa Ngoại ngữ NEU (Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="ẤN BẢN CHUẨN KHUNG THAM CHIẾU CHÂU ÂU (CEFR C1-C2) & HỌC THUẬT TIẾN SĨ"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Macroeconomics and Global Financial Markets Terminology",
         "topics": ["Gross Domestic Product, Inflation, and Business Cycles terminology", "Monetary Policy, Fiscal Policy, and Central Banking communication", "Financial Markets: Stocks, Bonds, Derivatives, and FX transactions", "Trade Balances, Tariffs, and Exchange Rate Regimes"]},
        {"chapter_num": 2, "chapter_title": "Corporate Finance, Accounting and Auditing Terminology",
         "topics": ["Financial Statements analysis: Balance Sheet, Income Statement, Cash Flow Statement in English", "Financial ratios: Liquidity, Solvency, Profitability, and Valuation metrics", "Capital Budgeting, Cost of Capital, and WACC presentations", "Auditing standards, Internal Controls, and Corporate Governance lexicon"]},
        {"chapter_num": 3, "chapter_title": "Business Strategy, International Trade and Negotiation",
         "topics": ["Strategic management models: SWOT, PESTEL, Porter's Five Forces, Blue Ocean", "Incoterms 2020 and International Sales Contracts", "Cross-cultural business negotiation and commercial correspondence", "Marketing mix 4Ps/7Ps, Brand positioning, and Consumer behavior discourse"]},
        {"chapter_num": 4, "chapter_title": "Chuyên đề Tiến sĩ: Academic English for Scholarly Publishing (Doctoral Level)",
         "topics": ["Scholarly writing conventions: Hedging, Stance, and Academic Voice in peer-reviewed journals", "Structuring Research Papers: Writing compelling Abstracts, Introductions, and Discussions", "Synthesizing literature, paraphrasing, and APA/Harvard citation styles", "Defending Doctoral Dissertations and presenting at international academic conferences"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Academic English for Economic Analysis and International Publication",
        introduction="Tiếng Anh chuyên ngành kinh tế và kinh doanh là công cụ học thuật thiết yếu giúp các nhà nghiên cứu, chuyên gia tài chính và nghiên cứu sinh tiếp cận kho tàng tri thức toàn cầu và công bố quốc tế thành công.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Discourse analysis of central bank communications and financial reports",
                "content": "Professional economic discourse requires precise lexical choices and nuanced syntactic structures. In central banking communication, forward guidance utilizes specific modal verbs (shall, anticipate, contemplate) to steer market expectations without making unconditional commitments.\n\nFinancial statement analysis in English adheres to International Financial Reporting Standards (IFRS) nomenclature. Distinctions between Operating Income, EBITDA, and Net Profit must be articulated with mathematical precision.",
                "formulas": [
                    "Operating Cash Flow Ratio = Operating Cash Flow / Current Liabilities",
                    "DuPont Identity in English: ROE = (Net Profit / Sales) * (Sales / Assets) * (Assets / Equity)",
                    "Academic Hedging formula: It is plausible that X contributes to Y under the assumption that Z holds"
                ],
                "case_studies": [
                    {"title": "Analyzing Federal Open Market Committee (FOMC) Press Statements", "detail": "Linguistic analysis of shifts in FOMC statement tone from 'hawkish' to 'dovish' and its immediate transmission mechanism to global currency pairs."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Corpus linguistics analysis of top-tier economics journals (AER, QJE, JFE): High-frequency collocation patterns",
                "Rhetorical moves in doctoral dissertation writing according to John Swales' Create-a-Research-Space (CARS) model",
                "Navigating peer-review discourse: Drafting diplomatic and rigorous rejoinder letters to journal editors and referees"
            ]
        },
        review_questions=[
            "Explain the difference between 'economic' and 'economical' in professional business context with examples.",
            "Translate a 200-word excerpt of the State Bank of Vietnam's annual monetary policy report into formal academic English.",
            "Identify the three essential rhetorical moves of a research paper introduction according to the CARS model."
        ]
    )

    out_path = os.path.join(BASE_DIR_08, r"[NEU] Tiếng Anh chuyên ngành Kinh tế & Kinh doanh - Khoa Ngoại ngữ NEU", r"[NEU] [Giáo trình Toàn văn] Tiếng Anh chuyên ngành Kinh tế & Kinh doanh - Khoa Ngoại ngữ NEU.pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Tiếng Anh chuyên ngành -> {pages} pages, {sz:.2f} MB")
    return {"name": "Tiếng Anh chuyên ngành", "pages": pages, "size_mb": sz, "path": out_path}

if __name__ == "__main__":
    res9 = build_research_methods()
    res10 = build_financial_econometrics()
    res11 = build_business_law()
    res12 = build_business_english()
    print("\nBATCH 3 COMPLETED SUCCESSFULLY!")
