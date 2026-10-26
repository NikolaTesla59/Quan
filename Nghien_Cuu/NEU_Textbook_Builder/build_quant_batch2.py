# -*- coding: utf-8 -*-
"""
NEU Master Textbook Builder - Batch 2: Econometrics, Data Science & Management Information Systems
Courses:
5. Kinh tế lượng cơ bản & nâng cao - GS.TS Nguyễn Quang Dong
6. Phân tích dữ liệu kinh tế với Python & R - Khoa Toán Kinh tế NEU
7. Hệ thống thông tin quản lý (MIS) - PGS.TS Trần Thị Song Minh
8. Mô hình toán kinh tế & Tối ưu hóa - GS.TS Trần Túc & Khoa Toán Kinh tế NEU
"""
import os
import sys

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

BASE_DIR_07 = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\07_Toán, Thống kê, Kinh tế lượng & Tin học"

def build_econometrics():
    print("Building: Kinh tế lượng cơ bản & nâng cao...")
    b = NEUTextbookBuilder(
        title="Kinh tế lượng cơ bản & nâng cao",
        subject_code="KTLN1101",
        faculty="Khoa Toán Kinh tế",
        authors="GS.TS. Nguyễn Quang Dong & PGS.TS. Nguyễn Ngọc Cường (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, HIỆN ĐẠI HÓA TOÀN DIỆN & TÍCH HỢP PHƯƠNG PHÁP SUY LUẬN NHÂN QUẢ TIẾN SĨ"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Mô hình Hồi quy Tuyến tính Cổ điển (Classical Linear Regression)",
         "topics": ["Bản chất của kinh tế lượng và phương pháp tiếp cận thực nghiệm", "Phương pháp bình phương bé nhất (OLS) và các giả thiết Gauss-Markov", "Định lý Gauss-Markov và tính chất BLUE (Best Linear Unbiased Estimator)", "Đánh giá độ phù hợp của mô hình: Hệ số R^2, Adjusted R^2 và kiểm định ANOVA F"]},
        {"chapter_num": 2, "chapter_title": "Kiểm định Giả thuyết và Các Khuyết tật của Mô hình Hồi quy",
         "topics": ["Hiện tượng đa cộng tuyến (Multicollinearity) và hệ số VIF", "Hiện tượng phương sai sai số thay đổi (Heteroskedasticity): Breusch-Pagan, White test và ước lượng sai số chuẩn vững Robust SE (HC1-HC3)", "Hiện tượng tự tương quan (Autocorrelation): Durbin-Watson, Breusch-Godfrey LM test và ước lượng Newey-West HAC", "Sai định dạng mô hình: Ramsey RESET test"]},
        {"chapter_num": 3, "chapter_title": "Hồi quy với Biến Định tính và Mô hình Lựa chọn Nhị phân",
         "topics": ["Biến giả (Dummy variables) và phân tích tương tác", "Mô hình xác suất tuyến tính (LPM) và những hạn chế", "Mô hình Logit và Probit: Hàm hợp lý cực đại (MLE) và hiệu ứng biên (Marginal Effects)", "Mô hình Tobit và hồi quy cắt cụt"]},
        {"chapter_num": 4, "chapter_title": "Chuyên đề Tiến sĩ: Suy luận Nhân quả và Kinh tế lượng Thực nghiệm Nâng cao",
         "topics": ["Chiến lược nhận diện nhân quả (Identification Strategy)", "Mô hình dữ liệu mảng (Panel Data): Pooled OLS, Fixed Effects (FE), Random Effects (RE) và Hausman test", "Phương pháp Sai phân trong Sai phân (Difference-in-Differences - DiD) và Event Study", "Biến công cụ (Instrumental Variables - IV), 2SLS và kiểm định ngoại sinh Hansen-Sargan", "Hồi quy gián đoạn (Regression Discontinuity Design - RDD) và Synthetic Control"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Chiến lược Nhận diện Nhân quả và Mô hình Dữ liệu Mảng trong Nghiên cứu Kinh tế",
        introduction="Kinh tế lượng hiện đại chuyển dịch trọng tâm từ tương quan thống kê đơn thuần sang suy luận nhân quả nghiêm ngặt nhằm đánh giá chính xác tác động của các chính sách công và quyết định quản trị.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Nguyên lý ước lượng OLS và điều kiện thỏa mãn tính chất BLUE",
                "content": "Ước lượng OLS tối thiểu hóa tổng bình phương phần dư. Theo Định lý Gauss-Markov, khi các giả thiết cổ điển được thỏa mãn (kỳ vọng sai số bằng 0, không có nội sinh Cov(X, u) = 0, phương sai thuần nhất và không tự tương quan), ước lượng OLS là ước lượng tuyến tính không chệch tốt nhất (BLUE).\n\nKhi giả định phương sai sai số không đổi bị vi phạm, ma trận hiệp phương sai của OLS không còn vững. Cần áp dụng ma trận hiệp phương sai Huber-White (HC1-HC3) hoặc phân cụm sai số chuẩn (Clustered Standard Errors) theo doanh nghiệp/tỉnh thành.",
                "formulas": [
                    "Vector ước lượng OLS: beta_hat = (X^T * X)^(-1) * X^T * Y",
                    "Ma trận hiệp phương sai vững Huber-White: Var(beta_hat) = (X^T * X)^(-1) * (sum e_i^2 * x_i * x_i^T) * (X^T * X)^(-1)",
                    "Kiểm định Breusch-Pagan: LM = n * R^2_{aux} ~ Chi^2(p)"
                ],
                "case_studies": [
                    {"title": "Đánh giá tác động của cải cách thủ tục hành chính đến FDI", "detail": "Ước lượng tác động của chỉ số PCI (Chỉ số Năng lực cạnh tranh cấp tỉnh) đến dòng vốn đầu tư trực tiếp nước ngoài tại 63 tỉnh thành Việt Nam giai đoạn 2015-2025."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Sai phân trong Sai phân so le thời gian (Staggered DiD) và các ước lượng vững Goodman-Bacon / Callaway-Sant'Anna",
                "Mô hình GMM sai phân (Arellano-Bond) và GMM hệ thống (Blundell-Bond) đối với dữ liệu mảng động",
                "Thiết kế hồi quy gián đoạn mờ (Fuzzy RDD) và kiểm định thao túng điểm ngưỡng McCrary Density Test",
                "Machine Learning trong kinh tế lượng nhân quả: Double/Debiased Machine Learning (DML) của Chernozhukov"
            ]
        },
        review_questions=[
            "Trình bày chiến lược nhận diện nhân quả trong mô hình Difference-in-Differences và giả định xu hướng song song (Parallel Trends).",
            "Giải thích cơ chế vận hành của kiểm định Hausman để lựa chọn giữa mô hình Fixed Effects và Random Effects.",
            "Tại sao biến công cụ (IV) phải thỏa mãn đồng thời hai điều kiện: Tính liên quan (Relevance) và Tính ngoại sinh (Exogeneity)?"
        ]
    )

    out_path = os.path.join(BASE_DIR_07, r"[NEU] Kinh tế lượng cơ bản & nâng cao - GS.TS Nguyễn Quang Dong (NXB ĐHKTQD)", r"[NEU] [Giáo trình Toàn văn] Kinh tế lượng cơ bản & nâng cao - GS.TS Nguyễn Quang Dong (NXB ĐHKTQD).pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Kinh tế lượng cơ bản & nâng cao -> {pages} pages, {sz:.2f} MB")
    return {"name": "Kinh tế lượng cơ bản & nâng cao", "pages": pages, "size_mb": sz, "path": out_path}

def build_data_science_python_r():
    print("Building: Phân tích dữ liệu kinh tế với Python & R...")
    b = NEUTextbookBuilder(
        title="Phân tích dữ liệu kinh tế với Python & R",
        subject_code="DASC1103",
        faculty="Khoa Toán Kinh tế",
        authors="Tập thể Giảng viên Khoa Toán Kinh tế NEU (Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="ẤN BẢN ĐỔI MỚI SÁNG TẠO, TÍCH HỢP POLARS, TIDYVERSE & HỌC MÁY NÂNG CAO"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Kiến trúc Khoa học Dữ liệu Kinh tế và Môi trường Lập trình",
         "topics": ["Hệ sinh thái phân tích dữ liệu: Python (Pandas, Polars, Statsmodels, Scikit-learn) và R (Tidyverse, fixest, plm)", "Thu thập dữ liệu kinh tế vĩ mô và tài chính qua API (vnstock, yfinance, FRED)", "Kỹ thuật làm sạch và biến đổi dữ liệu (Data Wrangling, Reshaping, Imputation)", "Trực quan hóa dữ liệu học thuật với Seaborn, Matplotlib và ggplot2"]},
        {"chapter_num": 2, "chapter_title": "Phân tích Thống kê và Kinh tế lượng Thực hành",
         "topics": ["Thống kê mô tả và kiểm định tham số trong Python & R", "Ước lượng mô hình hồi quy đa biến với statsmodels và lm()", "Kiểm định khuyết tật mô hình tự động và xuất bảng báo cáo chuẩn Top-5 Journals", "Mô hình dữ liệu mảng với thư viện Linearmodels (Python) và fixest (R)"]},
        {"chapter_num": 3, "chapter_title": "Phân tích Chuỗi thời gian Tài chính và Biến động",
         "topics": ["Xử lý dữ liệu DateTime và tính dừng (ADF test, KPSS test)", "Mô hình ARIMA/SARIMAX dự báo chuỗi thời gian", "Mô hình biến động ARCH/GARCH với thư viện arch trong Python và rugarch trong R", "Phân tích đa biến Vector Autoregression (VAR) và đồng tích hợp Johansen"]},
        {"chapter_num": 4, "chapter_title": "Chuyên đề Tiến sĩ: Học máy (Machine Learning) và Xử lý Ngôn ngữ Tự nhiên trong Tài chính",
         "topics": ["Mô hình hồi quy co rút Lasso, Ridge, ElasticNet trong lựa chọn biến", "Mô hình cây quyết định, Random Forest và XGBoost/LightGBM trong dự báo vỡ nợ", "Xử lý ngôn ngữ tự nhiên (NLP) phân tích tâm lý thị trường từ báo cáo tài chính và tin tức báo chí", "Causal Forest và học máy tăng cường trong tối ưu hóa danh mục đầu tư"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Hệ sinh thái Dữ liệu Lớn và Mô hình Hóa Kinh tế Thực nghiệm",
        introduction="Khoa học dữ liệu kinh tế kết hợp sức mạnh tính toán hiện đại với lý thuyết kinh tế lượng chặt chẽ để bóc tách thông tin giá trị từ các bộ dữ liệu vi mô và vĩ mô quy mô lớn.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Pipeline xử lý dữ liệu bảng (Panel Data) hiệu năng cao",
                "content": "Trong kỷ nguyên dữ liệu lớn, việc xử lý dữ liệu tài chính hàng triệu quan sát đòi hỏi kiến trúc tối ưu. Polars tận dụng kiến trúc bộ nhớ Apache Arrow và cơ chế tính toán đa luồng Lazy Evaluation để tăng tốc độ xử lý gấp hàng chục lần so với Pandas truyền thống.\n\nTrong môi trường R, gói fixest cung cấp thuật toán tối ưu hóa khử hiệu ứng cố định đa chiều (High-Dimensional Fixed Effects) với tốc độ vượt trội.",
                "formulas": [
                    "Độ phức tạp tính toán OLS ma trận: O(n * k^2 + k^3)",
                    "Thuật toán Frisch-Waugh-Lovell (FWL) phân rã biến: y* = M_X2 * y,  X1* = M_X2 * X1",
                    "Hàm mất mát hồi quy ElasticNet: L(beta) = ||y - X*beta||^2 + lambda1 * ||beta||_1 + lambda2 * ||beta||_2^2"
                ],
                "case_studies": [
                    {"title": "Xây dựng pipeline cảnh báo sớm rủi ro tín dụng ngân hàng", "detail": "Thiết kế luồng xử lý tự động từ thu thập dữ liệu giao dịch tài khoản đến huấn luyện mô hình XGBoost phân loại nợ xấu tại ngân hàng thương mại Việt Nam."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Causal Machine Learning (Athey & Imbens) trong đánh giá chính sách không đồng nhất (HTE)",
                "Mô hình Transformer và FinBERT trong phân tích nội dung cuộc họp ĐHĐCĐ và báo cáo thường niên",
                "Kỹ thuật giải thích mô hình học máy (Explainable AI - XAI): SHAP (Shapley Additive exPlanations) và LIME trong thẩm định tín dụng"
            ]
        },
        review_questions=[
            "So sánh hiệu năng và cơ chế quản lý bộ nhớ giữa Pandas và Polars trong xử lý dữ liệu lớn.",
            "Trình bày cấu trúc kịch bản mã nguồn R sử dụng gói `fixest` để hồi quy Fixed Effects có kiểm soát hiệu ứng ngành và năm.",
            "Nêu vai trò của phương pháp cross-validation (K-fold) trong đánh giá khả năng tổng quát hóa của mô hình Machine Learning."
        ]
    )

    out_path = os.path.join(BASE_DIR_07, r"[NEU] Phân tích dữ liệu kinh tế với Python & R - Khoa Toán Kinh tế NEU", r"[NEU] [Giáo trình Toàn văn] Phân tích dữ liệu kinh tế với Python & R - Khoa Toán Kinh tế NEU.pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Phân tích dữ liệu kinh tế với Python & R -> {pages} pages, {sz:.2f} MB")
    return {"name": "Phân tích dữ liệu kinh tế với Python & R", "pages": pages, "size_mb": sz, "path": out_path}

def build_mis():
    print("Building: Hệ thống thông tin quản lý (MIS)...")
    b = NEUTextbookBuilder(
        title="Hệ thống thông tin quản lý (MIS)",
        subject_code="HTTT1101",
        faculty="Khoa Tin học Kinh tế",
        authors="PGS.TS. Trần Thị Song Minh & TS. Đặng Vũ Tùng (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, CẬP NHẬT CHUYỂN ĐỔI SỐ, ERP, CLOUD & TRÍ TUỆ NHÂN TẠO TIẾN SĨ"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về Hệ thống Thông tin Quản lý trong Doanh nghiệp Số",
         "topics": ["Khái niệm dữ liệu, thông tin, tri thức và hệ thống thông tin", "Vai trò chiến lược của HTTT trong nâng cao năng lực cạnh tranh", "Mô hình 5 lực lượng cạnh tranh của Michael Porter và HTTT chiến lược", "Các cấp bậc HTTT: TPS, MIS, DSS, ESS"]},
        {"chapter_num": 2, "chapter_title": "Cơ sở Hạ tầng Công nghệ Thông tin và Quản trị Dữ liệu Doanh nghiệp",
         "topics": ["Phần cứng, phần mềm mạng và điện toán đám mây (Cloud Computing: IaaS, PaaS, SaaS)", "Cơ sở dữ liệu quan hệ (RDBMS), SQL và hệ quản trị DBMS", "Kho dữ liệu (Data Warehouse), Hồ dữ liệu (Data Lake) và kiến trúc Big Data", "Bảo mật HTTT, an toàn dữ liệu và tuân thủ Luật An ninh mạng"]},
        {"chapter_num": 3, "chapter_title": "Các Hệ thống Ứng dụng Doanh nghiệp Tích hợp (Enterprise Applications)",
         "topics": ["Hệ thống hoạch định nguồn lực doanh nghiệp (ERP: SAP, Oracle, Odoo)", "Hệ thống quản lý chuỗi cung ứng số (SCM)", "Hệ thống quản trị quan hệ khách hàng (CRM)", "Hệ thống thương mại điện tử (E-Commerce) và nền tảng kinh tế số"]},
        {"chapter_num": 4, "chapter_title": "Chuyên đề Tiến sĩ: Chuyển đổi Số, Quản trị Kiến trúc Doanh nghiệp và AI",
         "topics": ["Khung kiến trúc doanh nghiệp TOGAF và Zachman", "Mô hình chấp nhận công nghệ (TAM, UTAUT) trong nghiên cứu hành vi người dùng", "Chiến lược chuyển đổi số và quản trị sự thay đổi tổ chức (Kotter 8 bước)", "Ứng dụng Trí tuệ Nhân tạo thế hệ mới (Generative AI) và tự động hóa quy trình nghiệp vụ (RPA)"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Hệ thống Ứng dụng Tích hợp Doanh nghiệp và Chiến lược Chuyển đổi Số",
        introduction="Hệ thống thông tin quản lý là xương sống kết nối toàn bộ dòng thông tin, dòng vật chất và dòng tiền tệ trong tổ chức kinh tế hiện đại phục vụ hoạch định chiến lược và điều hành tác nghiệp.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Kiến trúc hệ thống ERP và dòng quy trình nghiệp vụ tích hợp",
                "content": "Hệ thống hoạch định nguồn lực doanh nghiệp (ERP) xóa bỏ các silo thông tin phân tán, tích hợp mọi chức năng cốt lõi (sản xuất, bán hàng, mua hàng, kho vận, kế toán, nhân sự) vào một cơ sở dữ liệu dùng chung duy nhất.\n\nViệc triển khai ERP không chỉ là dự án công nghệ thuần túy mà là quá trình tái cấu trúc quy trình nghiệp vụ (Business Process Reengineering - BPR) toàn diện nhằm loại bỏ các bước lãng phí và chuẩn hóa theo thông lệ quốc tế tốt nhất.",
                "formulas": [
                    "Hệ số ROI dự án HTTT: ROI = (Tổng Lợi ích thuần tích lũy - Tổng Chi phí đầu tư TCO) / TCO",
                    "Tổng chi phí sở hữu (TCO): TCO = Chi phí bản quyền phần mềm + Phần cứng + Dịch vụ triển khai + Chi phí đào tạo + Chi phí bảo trì hàng năm",
                    "Chỉ số hiệu quả quy trình nghiệp vụ: Chu kỳ quy trình (Lead Time) = Thời gian xử lý + Thời gian chờ + Thời gian vận chuyển"
                ],
                "case_studies": [
                    {"title": "Triển khai SAP S/4HANA tại Tập đoàn Sữa Vinamilk", "detail": "Phân tích kinh nghiệm triển khai thành công hệ thống ERP tích hợp quản lý toàn bộ chuỗi cung ứng từ trang trại bò sữa đến hệ thống phân phối toàn quốc."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết tài nguyên dựa trên tri thức (Knowledge-Based View - KBV) trong đánh giá năng lực số động",
                "Mô hình chấp nhận và sử dụng công nghệ hợp nhất (UTAUT2) và phương pháp mô hình hóa cấu trúc tuyến tính PLS-SEM",
                "Khai phá quy trình nghiệp vụ (Process Mining) bằng dữ liệu Event Log để phát hiện nút thắt cổ chai và sai lệch quy trình"
            ]
        },
        review_questions=[
            "Phân tích vai trò của cơ sở dữ liệu tích hợp trong việc giải quyết vấn đề phân tán dữ liệu của doanh nghiệp.",
            "Trình bày 4 cấp bậc của hệ thống thông tin quản lý và mối liên hệ với các cấp quản trị trong tổ chức.",
            "Tại sao yếu tố văn hóa doanh nghiệp và quản trị sự thay đổi là nguyên nhân quyết định đến sự thành bại của dự án ERP?"
        ]
    )

    out_path = os.path.join(BASE_DIR_07, r"[NEU] Hệ thống thông tin quản lý (MIS) - PGS.TS Trần Thị Song Minh (NXB ĐHKTQD)", r"[NEU] [Giáo trình Toàn văn] Hệ thống thông tin quản lý (MIS) - PGS.TS Trần Thị Song Minh (NXB ĐHKTQD).pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Hệ thống thông tin quản lý (MIS) -> {pages} pages, {sz:.2f} MB")
    return {"name": "Hệ thống thông tin quản lý (MIS)", "pages": pages, "size_mb": sz, "path": out_path}

def build_math_econ_optimization():
    print("Building: Mô hình toán kinh tế & Tối ưu hóa...")
    b = NEUTextbookBuilder(
        title="Mô hình toán kinh tế & Tối ưu hóa",
        subject_code="MHTK1102",
        faculty="Khoa Toán Kinh tế",
        authors="GS.TS. Trần Túc & Tập thể Giảng viên Khoa Toán Kinh tế NEU",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="ẤN BẢN KHOA HỌC CHUYÊN SÂU, TÍCH HỢP QUY HOẠCH PHI TUYẾN & TỐI ƯU ĐỘNG TIẾN SĨ"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Phương pháp Luận Mô hình Hóa Toán Kinh tế",
         "topics": ["Bản chất và các bước xây dựng mô hình toán kinh tế", "Phân loại mô hình: Tĩnh vs Động, Tuyến tính vs Phi tuyến, Xác định vs Ngẫu nhiên", "Nguyên lý cân bằng thị trường và phân tích cân bằng tĩnh"]},
        {"chapter_num": 2, "chapter_title": "Quy hoạch Tuyến tính và Bài toán Đối ngẫu",
         "topics": ["Dạng chính tắc và dạng chuẩn của bài toán quy hoạch tuyến tính", "Phương pháp đơn nguyên (Simplex Algorithm) và bảng đơn nguyên cải biên", "Lý thuyết đối ngẫu (Duality Theory) và ý nghĩa kinh tế của giá bóng (Shadow Price)", "Phân tích độ nhạy (Sensitivity Analysis) của phương án tối ưu"]},
        {"chapter_num": 3, "chapter_title": "Quy hoạch Phi tuyến và Điều kiện Tối ưu Karush-Kuhn-Tucker (KKT)",
         "topics": ["Hàm lồi, tập lồi và bài toán quy hoạch lồi", "Điều kiện tối ưu KKT đối với bài toán có ràng buộc bất đẳng thức", "Phương pháp hàm phạt và thuật toán Gradient", "Ứng dụng trong bài toán lựa chọn danh mục Markowitz và cân bằng độc quyền"]},
        {"chapter_num": 4, "chapter_title": "Chuyên đề Tiến sĩ: Tối ưu hóa Động và Lý thuyết Điều khiển Tối ưu",
         "topics": ["Giải tích biến phân (Calculus of Variations) và phương trình Euler-Lagrange", "Nguyên lý Cực đại Pontryagin trong điều khiển tối ưu liên tục", "Quy hoạch động rời rạc và phương trình Bellman", "Mô hình tăng trưởng kinh tế tối ưu Ramsey-Cass-Koopmans"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Lý thuyết Đối ngẫu và Tối ưu hóa Ràng buộc trong Quản trị Kinh tế",
        introduction="Mô hình toán kinh tế cho phép chuyển hóa các vấn đề kinh tế thực tế thành các bài toán tối ưu hóa hình thức để tìm ra phương án phân bổ nguồn lực đạt hiệu quả cao nhất.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Lý thuyết đối ngẫu và giá bóng của các nguồn lực sản xuất",
                "content": "Mỗi bài toán quy hoạch tuyến tính gốc (Primal) đều tồn tại một bài toán đối ngẫu (Dual) tương ứng. Nghiệm tối ưu của bài toán đối ngẫu y* chính là vectơ 'giá bóng' (shadow prices) đo lường mức gia tăng giá trị hàm mục tiêu khi nguồn lực khan hiếm b_i được nới lỏng thêm 1 đơn vị.\n\nTheo Định lý đối ngẫu mạnh, giá trị tối ưu của hàm mục tiêu gốc và đối ngẫu luôn bằng nhau: c^T * x* = b^T * y*. Định lý bù chéo cung cấp tiêu chuẩn kiểm tra xem một nguồn lực có đang bị dư thừa hay sử dụng triệt để.",
                "formulas": [
                    "Bài toán gốc: max Z = c^T * x  với A * x <= b,  x >= 0",
                    "Bài toán đối ngẫu: min W = b^T * y  với A^T * y >= c,  y >= 0",
                    "Điều kiện bù chéo (Complementary Slackness): y_i * (sum a_ij * x_j - b_i) = 0 và x_j * (sum a_ij * y_i - c_j) = 0"
                ],
                "case_studies": [
                    {"title": "Tối ưu hóa kế hoạch vận tải và phân phối xi măng Vicem", "detail": "Thiết lập mô hình vận tải cỡ lớn nhằm giảm thiểu chi phí logistics từ 10 nhà máy đến 63 trung tâm phân phối trên toàn quốc."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết điểm bất động Kakutani và định lý Brouwer trong chứng minh cân bằng thị trường",
                "Mô hình cân bằng động ngẫu nhiên tổng thể (DSGE) giải bằng phương pháp xấp xỉ tuyến tính hóa xung quanh điểm dừng",
                "Lý thuyết trò chơi tiến hóa (Evolutionary Game Theory) và trạng thái ổn định tiến hóa (ESS) trong hành vi doanh nghiệp"
            ]
        },
        review_questions=[
            "Phát biểu và chứng minh định lý đối ngẫu yếu và định lý đối ngẫu mạnh trong quy hoạch tuyến tính.",
            "Ý nghĩa kinh tế của giá bóng là gì? Doanh nghiệp nên sẵn sàng trả tối đa bao nhiêu tiền để mua thêm một đơn vị nguyên liệu?",
            "Viết điều kiện Karush-Kuhn-Tucker cho bài toán tối đa hóa lợi nhuận của nhà độc quyền sản xuất hai sản phẩm có tính thay thế."
        ]
    )

    out_path = os.path.join(BASE_DIR_07, r"[NEU] Mô hình toán kinh tế & Tối ưu hóa - GS.TS Trần Túc & Khoa Toán Kinh tế NEU", r"[NEU] [Giáo trình Toàn văn] Mô hình toán kinh tế & Tối ưu hóa - GS.TS Trần Túc & Khoa Toán Kinh tế NEU.pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Mô hình toán kinh tế & Tối ưu hóa -> {pages} pages, {sz:.2f} MB")
    return {"name": "Mô hình toán kinh tế & Tối ưu hóa", "pages": pages, "size_mb": sz, "path": out_path}

if __name__ == "__main__":
    res5 = build_econometrics()
    res6 = build_data_science_python_r()
    res7 = build_mis()
    res8 = build_math_econ_optimization()
    print("\nBATCH 2 COMPLETED SUCCESSFULLY!")
