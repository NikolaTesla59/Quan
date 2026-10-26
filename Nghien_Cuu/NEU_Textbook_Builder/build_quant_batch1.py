# -*- coding: utf-8 -*-
"""
NEU Master Textbook Builder - Batch 1: Mathematics & Statistics
Courses:
1. Toán cho các nhà kinh tế - PGS.TS Nguyễn Cao Văn
2. Xác suất và Thống kê toán - PGS.TS Nguyễn Cao Văn
3. Nguyên lý Thống kê kinh tế - PGS.TS Trần Ngọc Phác
4. Thống kê doanh nghiệp - PGS.TS Phan Công Nghĩa
"""
import os
import sys

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

BASE_DIR_07 = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\07_Toán, Thống kê, Kinh tế lượng & Tin học"

def build_math_for_economists():
    print("Building: Toán cho các nhà kinh tế...")
    b = NEUTextbookBuilder(
        title="Toán cho các nhà kinh tế",
        subject_code="TOA1101",
        faculty="Khoa Toán Kinh tế",
        authors="PGS.TS. Nguyễn Cao Văn & PGS.TS. Trần Văn Ba (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, CHUẨN HÓA TOÀN DIỆN & TÍCH HỢP MÔ HÌNH TỐI ƯU HÓA ĐỘNG TIẾN SĨ"
    )
    b.build_cover()
    
    toc_data = [
        {"chapter_num": 1, "chapter_title": "Đại số tuyến tính và Không gian vectơ trong Phân tích Kinh tế",
         "topics": ["Ma trận, định thức và các phép toán ma trận", "Hệ phương trình tuyến tính và quy tắc Cramer", "Mô hình cân bằng thị trường đa hàng hóa và mô hình Input-Output Leontief", "Không gian vectơ R^n và dạng toàn phương"]},
        {"chapter_num": 2, "chapter_title": "Giải tích hàm một biến và Ứng dụng trong Tối ưu hóa Kinh tế",
         "topics": ["Giới hạn, tính liên tục và tốc độ tăng trưởng", "Đạo hàm và giá trị cận biên (Marginal Concept)", "Độ co giãn của hàm số kinh tế (Elasticity)", "Bài toán tối ưu hóa một biến trong doanh nghiệp"]},
        {"chapter_num": 3, "chapter_title": "Giải tích hàm nhiều biến và Tối ưu hóa Tĩnh có Ràng buộc",
         "topics": ["Đạo hàm riêng và vi phân toàn phần", "Tối ưu hóa không điều kiện của hàm nhiều biến", "Tối ưu hóa có ràng buộc đẳng thức: Phương pháp nhân tử Lagrange", "Tối ưu hóa phi tuyến có ràng buộc bất đẳng thức: Điều kiện Kuhn-Tucker"]},
        {"chapter_num": 4, "chapter_title": "Phương trình Vi phân, Sai phân và Động học Kinh tế",
         "topics": ["Phương trình vi phân cấp 1 và cấp 2 trong mô hình giá cả liên tục", "Phương trình sai phân tuyến tính và mô hình mạng nhện Cobweb", "Tính ổn định của điểm cân bằng động", "Chuyên đề Tiến sĩ: Tối ưu hóa động liên tục và Quy hoạch động Bellman"]}
    ]
    b.add_table_of_contents(toc_data)
    
    b.add_chapter(
        chap_num=1,
        chap_title="Đại số tuyến tính và Không gian vectơ trong Phân tích Kinh tế",
        introduction="Đại số tuyến tính cung cấp công cụ toán học nền tảng để mô hình hóa và giải quyết các hệ thống kinh tế vĩ mô và vi mô phức tạp gồm nhiều biến số tương tác đồng thời.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Lý thuyết ma trận, định thức và định lý Rouché-Capelli",
                "content": "Một hệ thống kinh tế gồm n thị trường liên kết được biểu diễn dưới dạng ma trận A.X = B. Khả năng tồn tại nghiệm duy nhất phụ thuộc vào hạng của ma trận hệ số rank(A) và định thức det(A) khác 0.\n\nTrong phân tích kinh tế lượng và chuỗi thời gian, ma trận nghịch đảo và ma trận giả nghịch đảo Moore-Penrose đóng vai trò then chốt trong ước lượng OLS đa biến.",
                "formulas": [
                    "Hệ cân bằng tổng quát: A * X = D (A là ma trận công nghệ/hệ số)",
                    "Quy tắc Cramer nghiệm duy nhất: x_i = det(A_i) / det(A) (khi det(A) != 0)",
                    "Dạng toàn phương xác định dấu: Q(x) = x^T * H * x (với H là ma trận Hessian)"
                ],
                "case_studies": [
                    {"title": "Mô hình cân bằng 3 thị trường hàng hóa tại Việt Nam", "detail": "Thiết lập hệ phương trình cung cầu cho thị trường gạo, xăng dầu và vận tải để tính toán giá và lượng cân bằng đồng thời."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Mô hình cân đối liên ngành Input-Output (I-O) Leontief",
                "content": "Mô hình I-O của Wassily Leontief mô tả sự phụ thuộc tương hỗ giữa các ngành trong nền kinh tế quốc dân. Ma trận hệ số chi phí trực tiếp A = [a_ij] đo lường lượng giá trị ngành i cần cung cấp để ngành j tạo ra 1 đơn vị sản lượng cuối cùng.\n\nMa trận nghịch đảo Leontief (I - A)^(-1) cho phép xác định tổng sản lượng cần thiết của từng ngành để đáp ứng cầu cuối cùng thay đổi.",
                "formulas": [
                    "Phương trình cân đối tổng quát: X = A * X + Y  <=>  (I - A) * X = Y",
                    "Nghiệm sản lượng Leontief: X = (I - A)^(-1) * Y (với (I - A)^(-1) >= 0)",
                    "Điều kiện Hawkins-Simon: Tất cả các định thức con chính của ma trận (I - A) phải mang dấu dương"
                ],
                "case_studies": [
                    {"title": "Phân tích lan tỏa của ngành năng lượng tái tạo", "detail": "Sử dụng bảng I-O của Tổng cục Thống kê để đánh giá mức độ lan tỏa của đầu tư điện gió đến sản lượng các ngành công nghiệp phụ trợ."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Không gian Hilbert và không gian Banach trong kinh tế học toán học vô hạn chiều",
                "Định lý tách tập lồi Hahn-Banach và sự tồn tại hệ thống giá cân bằng hỗ trợ",
                "Mô hình cân bằng tổng thể Arrow-Debreu: Chứng minh sự tồn tại nghiệm cân bằng qua Định lý điểm bất động Kakutani",
                "Phương pháp ma trận ngẫu nhiên (Random Matrix Theory) trong xử lý nhiễu dữ liệu tài chính đa chiều"
            ]
        },
        review_questions=[
            "Nêu điều kiện để ma trận (I - A) khả nghịch theo tiêu chuẩn Frobenius-Perron.",
            "Phân tích ý nghĩa kinh tế của các phần tử trong ma trận nghịch đảo Leontief.",
            "Vận dụng quy tắc Cramer để tìm nghiệm của hệ cân bằng cung - cầu 2 thị trường bổ sung."
        ]
    )

    b.add_chapter(
        chap_num=2,
        chap_title="Giải tích hàm một biến và Ứng dụng trong Tối ưu hóa Kinh tế",
        introduction="Chương 2 trình bày các nguyên lý giải tích vi phân và tích phân, làm rõ nguyên lý tối ưu hóa cận biên - hòn đá tảng của lý thuyết kinh tế học tân cổ điển.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Nguyên lý cận biên (Marginalism) và đạo hàm trong kinh tế",
                "content": "Mọi quyết định duy lý trong kinh tế học đều dựa trên so sánh giữa lợi ích cận biên (MB) và chi phí cận biên (MC). Đạo hàm bậc nhất f'(x) đo lường tốc độ biến thiên tức thời của biến phụ thuộc khi biến độc lập thay đổi vô cùng nhỏ.\n\nĐộ co giãn điểm (point elasticity) epsilon = (dy/dx) * (x/y) là đại lượng không thứ nguyên, giúp so sánh độ nhạy giữa các thị trường độc lập với đơn vị đo lường.",
                "formulas": [
                    "Hàm doanh thu cận biên: MR(Q) = dTR / dQ = P * (1 + 1 / E_P^D)",
                    "Quy tắc tối đa hóa lợi nhuận: MR(Q) = MC(Q) và d^2 pi / dQ^2 < 0",
                    "Độ co giãn của hàm số: epsilon_{y,x} = lim_{Delta x -> 0} (Delta y / y) / (Delta x / x) = f'(x) * (x / f(x))"
                ],
                "case_studies": [
                    {"title": "Chiến lược định giá vé viễn thông theo độ co giãn", "detail": "Ước lượng độ co giãn của cầu dịch vụ truyền số liệu 5G để xác định biểu cước tối đa hóa doanh thu của Viettel Telecom."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết đối ngẫu trong tối ưu hóa vi mô: Hàm chi phí gián tiếp và hàm chi tiêu",
                "Bổ đề Shephard và Bổ đề Roy trong phục hồi hàm cầu Marshallian và Hicksian",
                "Định lý bao bì Envelope Theorem đối với bài toán tối ưu hóa có tham số"
            ]
        },
        review_questions=[
            "Chứng minh mối quan hệ giữa doanh thu cận biên, giá bán và hệ số co giãn của cầu theo giá.",
            "Tìm điều kiện bậc hai để hàm lợi nhuận đạt cực đại toàn cục."
        ]
    )

    out_path = os.path.join(BASE_DIR_07, r"[NEU] Toán cho các nhà kinh tế - PGS.TS Nguyễn Cao Văn (NXB ĐHKTQD)", r"[NEU] [Giáo trình Toàn văn] Toán cho các nhà kinh tế - PGS.TS Nguyễn Cao Văn (NXB ĐHKTQD).pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Toán cho các nhà kinh tế -> {pages} pages, {sz:.2f} MB")
    return {"name": "Toán cho các nhà kinh tế", "pages": pages, "size_mb": sz, "path": out_path}

def build_probability_statistics():
    print("Building: Xác suất và Thống kê toán...")
    b = NEUTextbookBuilder(
        title="Xác suất và Thống kê toán",
        subject_code="XSTK1101",
        faculty="Khoa Toán Kinh tế",
        authors="PGS.TS. Nguyễn Cao Văn & PGS.TS. Trần Ngọc Phác (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, CHUẨN HÓA LÝ THUYẾT ĐO ĐỘ ĐO & SUY DIỄN THỐNG KÊ TIẾN SĨ"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Không gian Xác suất và Biến ngẫu nhiên",
         "topics": ["Định nghĩa xác suất Kolmogorov và đại số sigma", "Biến ngẫu nhiên rời rạc và liên tục", "Hàm phân phối tích lũy (CDF) và hàm mật độ xác suất (PDF)", "Các đặc trưng số: Kỳ vọng, phương sai, moment, độ lệch, độ nhọn"]},
        {"chapter_num": 2, "chapter_title": "Các Phân phối Xác suất Thông dụng trong Kinh tế - Tài chính",
         "topics": ["Phân phối nhị thức, Poisson, Geometric", "Phân phối chuẩn (Normal Distribution) và Log-normal", "Phân phối Student t, Chi-square, Fisher Snedecor", "Phân phối đuôi dày (Fat-tailed) và giá trị cực trị (EVT)"]},
        {"chapter_num": 3, "chapter_title": "Lý thuyết Suy diễn Thống kê: Ước lượng và Kiểm định Giả thuyết",
         "topics": ["Mẫu ngẫu nhiên và phân phối mẫu", "Phương pháp ước lượng điểm: OLS, MLE (Maximum Likelihood), GMM", "Khoảng tin cậy cho kỳ vọng và phương sai", "Kiểm định giả thuyết thống kê tham số và phi tham số"]},
        {"chapter_num": 4, "chapter_title": "Chuyên đề Tiến sĩ: Giải tích Ngẫu nhiên và Quá trình Ngẫu nhiên trong Tài chính",
         "topics": ["Quá trình ngẫu nhiên, chuỗi Markov và Martingale", "Chuyển động Brown và Bổ đề Ito", "Mô hình hóa định giá quyền chọn Black-Scholes-Merton", "Bootstrap và mô phỏng Monte Carlo đa chiều"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Không gian Xác suất và Biến ngẫu nhiên trong Phân tích Kinh tế",
        introduction="Xác suất và Thống kê toán là cơ sở lý thuyết nghiêm ngặt để đo lường sự không chắc chắn, quản trị rủi ro danh mục và xây dựng các mô hình kinh tế lượng thực nghiệm.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Cấu trúc không gian xác suất Kolmogorov và hàm đặc trưng",
                "content": "Một không gian xác suất chuẩn tắc gồm bộ ba (Omega, F, P), trong đó Omega là không gian biến cố sơ cấp, F là sigma-đại số các biến cố và P là độ đo xác suất thỏa mãn các tiên đề Kolmogorov.\n\nHàm đặc trưng (Characteristic function) phi_X(t) = E[e^{i t X}] hoàn toàn xác định phân phối xác suất và là công cụ không thể thay thế để chứng minh Định lý giới hạn trung tâm (CLT).",
                "formulas": [
                    "Bất đẳng thức Chebyshev: P(|X - mu| >= k * sigma) <= 1 / k^2",
                    "Định lý Giới hạn Trung tâm Lindeberg-Lévy: sqrt(n) * (bar{X}_n - mu) / sigma -> N(0, 1) khi n -> vô cùng",
                    "Hàm sinh moment: M_X(t) = E[e^{t X}] = sum_{k=0}^{oo} (t^k / k!) * E[X^k]"
                ],
                "case_studies": [
                    {"title": "Đo lường rủi ro đuôi lợi suất chỉ số VN-Index", "detail": "Kiểm định tính chuẩn của chuỗi lợi suất nhật ký VN-Index giai đoạn 2010-2025, phát hiện hiện tượng thừa độ nhọn (leptokurtosis) và bất đối xứng."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết độ đo tích phân Lebesgue-Stieltjes và tích phân ngẫu nhiên Ito",
                "Định lý Girsanov về chuyển đổi độ đo xác suất tương đương và định giá trung hòa rủi ro",
                "Quá trình Levy, mô hình nhảy phân tán (Jump-Diffusion) và mô hình biến động ngẫu nhiên Heston",
                "Phương pháp suy diễn Bayesian MCMC (Markov Chain Monte Carlo) trong ước lượng tham số phức"
            ]
        },
        review_questions=[
            "Trình bày định nghĩa hàm mật độ xác suất và tính chất của hàm phân phối tích lũy.",
            "Chứng minh bất đẳng thức Cauchy-Schwarz đối với kỳ vọng của hai biến ngẫu nhiên.",
            "Giải thích ý nghĩa của Bổ đề Ito trong định giá tài sản tài chính phái sinh."
        ]
    )

    out_path = os.path.join(BASE_DIR_07, r"[NEU] Xác suất và Thống kê toán - PGS.TS Nguyễn Cao Văn (NXB ĐHKTQD)", r"[NEU] [Giáo trình Toàn văn] Xác suất và Thống kê toán - PGS.TS Nguyễn Cao Văn (NXB ĐHKTQD).pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Xác suất và Thống kê toán -> {pages} pages, {sz:.2f} MB")
    return {"name": "Xác suất và Thống kê toán", "pages": pages, "size_mb": sz, "path": out_path}

def build_principles_of_statistics():
    print("Building: Nguyên lý Thống kê kinh tế...")
    b = NEUTextbookBuilder(
        title="Nguyên lý Thống kê kinh tế",
        subject_code="TKKT1101",
        faculty="Khoa Thống kê",
        authors="PGS.TS. Trần Ngọc Phác & PGS.TS. Trần Thị Kim Thu (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, HIỆN ĐẠI HÓA CHUẨN QUỐC TẾ & PHÂN TÍCH CHỈ SỐ KINH TẾ TIẾN SĨ"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Đối tượng, Phương pháp và Quá trình Nghiên cứu Thống kê",
         "topics": ["Bản chất và chức năng của thống kê kinh tế", "Tổng thể thống kê, đơn vị điều tra và tiêu thức thống kê", "Thang đo thống kê: Định danh, thứ bậc, khoảng và tỷ lệ", "Tổ chức điều tra chọn mẫu và thu thập dữ liệu lớn"]},
        {"chapter_num": 2, "chapter_title": "Phân tổ Thống kê và Hệ thống Các Mức độ của Hiện tượng Kinh tế",
         "topics": ["Kỹ thuật phân tổ thống kê và bảng phân phối tần số", "Mức độ tuyệt đối và mức độ tương đối", "Mức độ bình quân: Số bình quân số học, điều hòa, hình học, mốt, trung vị", "Độ biến thiên: Khoảng biến thiên, phương sai, độ lệch chuẩn, hệ số biến thiên"]},
        {"chapter_num": 3, "chapter_title": "Lý thuyết Chỉ số Kinh tế và Hệ thống Chỉ số Tổng hợp",
         "topics": ["Khái niệm và tác dụng của phương pháp chỉ số", "Chỉ số đơn và chỉ số phát triển", "Chỉ số tổng hợp giá cả và khối lượng: Laspeyres, Paasche, Fisher", "Hệ thống chỉ số nhân tố phân tích biến động tổng thể"]},
        {"chapter_num": 4, "chapter_title": "Dãy số Thời gian và Dự báo Thống kê Kinh tế",
         "topics": ["Khái niệm và phân loại dãy số thời gian", "Các chỉ tiêu phân tích tốc độ phát triển và biến động mùa vụ", "Các phương pháp làm trơn và ngoại suy xu thế (ARIMA, Holt-Winters)", "Chuyên đề Tiến sĩ: Xử lý gãy cấu trúc (Structural Breaks) trong chuỗi vĩ mô"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Lý thuyết Chỉ số Kinh tế và Phân tích Biến động Vĩ mô",
        introduction="Phương pháp chỉ số là công cụ đặc thù của thống kê học dùng để nghiên cứu sự biến động của các hiện tượng kinh tế phức tạp gồm nhiều phần tử không thể cộng trực tiếp với nhau.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Lý thuyết chỉ số tổng hợp Laspeyres, Paasche và Fisher lý tưởng",
                "content": "Chỉ số giá phản ánh sự biến động thuần túy của mức giá thị trường sau khi cố định quyền số lượng hàng hóa tiêu thụ. Chỉ số Laspeyres (L_p) sử dụng quyền số kỳ gốc q_0, có xu hướng phóng đại mức tăng giá sinh hoạt do bỏ qua hiệu ứng thay thế của người tiêu dùng.\n\nChỉ số Paasche (P_p) sử dụng quyền số kỳ báo cáo q_1, thường đánh giá thấp mức tăng giá. Chỉ số lý tưởng Fisher (F_p) là trung bình nhân của L_p và P_p, thỏa mãn đồng thời phép thử hoán vị thời gian và phép thử nghịch đảo nhân tố theo tiêu chuẩn Irving Fisher.",
                "formulas": [
                    "Chỉ số giá Laspeyres: I_p^L = sum(p_1 * q_0) / sum(p_0 * q_0)",
                    "Chỉ số giá Paasche: I_p^P = sum(p_1 * q_1) / sum(p_0 * q_1)",
                    "Chỉ số Fisher lý tưởng: I_p^F = sqrt(I_p^L * I_p^P)"
                ],
                "case_studies": [
                    {"title": "Tính toán chỉ số giá tiêu dùng (CPI) tại Việt Nam", "detail": "Nghiên cứu phương pháp luận của Tổng cục Thống kê (GSO) trong việc cập nhật rổ hàng hóa đại diện gồm 752 mặt hàng và trọng số chi tiêu gia đình."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết số mũ Divisia và Törnqvist trong đo lường năng suất tổng nhân tố (TFP)",
                "Chỉ số giá Hedonic trong điều chỉnh chất lượng sản phẩm công nghệ cao và bất động sản",
                "Mô hình chuỗi thời gian trạng thái không gian (State-Space Models) và bộ lọc Kalman trong ước lượng xu thế tiềm năng"
            ]
        },
        review_questions=[
            "So sánh ưu nhược điểm của công thức chỉ số giá Laspeyres và Paasche trong thực tiễn thống kê.",
            "Trình bày hệ thống chỉ số phân tích sự biến động của chỉ tiêu tổng doanh thu theo giá bán và khối lượng sản phẩm."
        ]
    )

    out_path = os.path.join(BASE_DIR_07, r"[NEU] Nguyên lý Thống kê kinh tế - PGS.TS Trần Ngọc Phác (NXB ĐHKTQD)", r"[NEU] [Giáo trình Toàn văn] Nguyên lý Thống kê kinh tế - PGS.TS Trần Ngọc Phác (NXB ĐHKTQD).pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Nguyên lý Thống kê kinh tế -> {pages} pages, {sz:.2f} MB")
    return {"name": "Nguyên lý Thống kê kinh tế", "pages": pages, "size_mb": sz, "path": out_path}

def build_business_statistics():
    print("Building: Thống kê doanh nghiệp...")
    b = NEUTextbookBuilder(
        title="Thống kê doanh nghiệp",
        subject_code="TKDN1102",
        faculty="Khoa Thống kê",
        authors="PGS.TS. Phan Công Nghĩa & PGS.TS. Trần Thị Kim Thu (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, TÍCH HỢP QUẢN TRỊ DỮ LIỆU HIỆN ĐẠI & PHÂN TÍCH HIỆU QUẢ TIẾN SĨ"
    )
    b.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Hệ thống Thông tin và Chỉ tiêu Thống kê Doanh nghiệp",
         "topics": ["Bản chất, đối tượng và nhiệm vụ thống kê doanh nghiệp", "Hệ thống báo cáo thống kê định kỳ và cơ sở dữ liệu doanh nghiệp", "Hệ thống chỉ tiêu kết quả hoạt động sản xuất kinh doanh: GO, VA, NVA"]},
        {"chapter_num": 2, "chapter_title": "Thống kê Lao động, Tiền lương và Năng suất Lao động",
         "topics": ["Thống kê số lượng, cơ cấu và thời gian sử dụng lao động", "Thống kê quỹ tiền lương và thu nhập của người lao động", "Hệ thống chỉ tiêu năng suất lao động (thuần túy và tổng hợp)", "Mô hình phân tích nhân tố biến động tổng quỹ lương"]},
        {"chapter_num": 3, "chapter_title": "Thống kê Tài sản Cố định, Thiết bị và Vốn Doanh nghiệp",
         "topics": ["Đánh giá tài sản cố định: Nguyên giá, giá trị còn lại, giá trị khôi phục", "Thống kê tình hình trang bị và hiệu quả sử dụng TSCĐ", "Thống kê luân chuyển vốn lưu động và hiệu quả sử dụng vốn"]},
        {"chapter_num": 4, "chapter_title": "Thống kê Chi phí Sản xuất, Giá thành và Hiệu quả Tài chính Doanh nghiệp",
         "topics": ["Thống kê chi phí theo yếu tố và theo khoản mục", "Phân tích biến động giá thành sản phẩm và tỷ suất chi phí", "Thống kê lợi nhuận, tỷ suất sinh lời (ROA, ROE, ROCE)", "Chuyên đề Tiến sĩ: Phân tích bao hàm dữ liệu (DEA) và Hàm biên ngẫu nhiên (SFA) trong đo lường hiệu quả kỹ thuật"]}
    ]
    b.add_table_of_contents(toc_data)

    b.add_chapter(
        chap_num=1,
        chap_title="Thống kê Năng suất Lao động và Phân tích Hiệu quả Doanh nghiệp",
        introduction="Đo lường và phân tích năng suất lao động cùng hiệu quả sử dụng các nguồn lực đầu vào là nội dung trọng tâm của thống kê doanh nghiệp phục vụ quyết định điều hành vi mô.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Hệ thống chỉ tiêu năng suất lao động và phương pháp phân tích nhân tố",
                "content": "Năng suất lao động phản ánh hiệu quả có ích của lao động cụ thể trong quá trình sản xuất. Mức năng suất lao động cá biệt W = Q / T (sản lượng trên thời gian hao phí). Đối với tổng thể doanh nghiệp, năng suất lao động bình quân chịu ảnh hưởng bởi 2 nhân tố: Mức năng suất lao động từng bộ phận và cơ cấu phân bổ lao động giữa các phân xưởng.\n\nPhương pháp chỉ số cấu thành khả biến giúp phân tách rõ nét tốc độ tăng trưởng năng suất nội tại và hiệu ứng dịch chuyển cơ cấu lao động.",
                "formulas": [
                    "Chỉ số năng suất lao động cấu thành khả biến: I_{bar{W}} = bar{W}_1 / bar{W}_0 = [sum(W_1 * T_1) / sum(T_1)] / [sum(W_0 * T_0) / sum(T_0)]",
                    "Chỉ số năng suất cố định: I_{W}^{co_dinh} = sum(W_1 * T_1) / sum(W_0 * T_1)",
                    "Chỉ số ảnh hưởng cơ cấu kết cấu lao động: I_{T}^{co_cau} = [sum(W_0 * T_1) / sum(T_1)] / [sum(W_0 * T_0) / sum(T_0)]"
                ],
                "case_studies": [
                    {"title": "Phân tích năng suất lao động tại Tập đoàn Dệt may Việt Nam (Vinatex)", "detail": "Áp dụng hệ thống chỉ số để bóc tách nguyên nhân tăng năng suất lao động bình quân nhờ đổi mới thiết bị tự động hóa và cơ cấu lại lực lượng công nhân may."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp phân tích bao hàm dữ liệu phi tham số (Data Envelopment Analysis - DEA) CRS và VRS",
                "Mô hình phân tích biên ngẫu nhiên tham số (Stochastic Frontier Analysis - SFA) phân tách phi hiệu quả kỹ thuật và nhiễu ngẫu nhiên",
                "Chỉ số năng suất Malmquist đo lường biến động năng suất tổng nhân tố (TFP growth) theo thời gian trong dữ liệu mảng doanh nghiệp"
            ]
        },
        review_questions=[
            "Trình bày phương pháp tính giá trị sản xuất (GO) và giá trị gia tăng (VA) trong doanh nghiệp.",
            "Xây dựng phương trình liên hệ giữa chỉ số năng suất cấu thành khả biến, chỉ số năng suất cố định và chỉ số cơ cấu."
        ]
    )

    out_path = os.path.join(BASE_DIR_07, r"[NEU] Thống kê doanh nghiệp - PGS.TS Phan Công Nghĩa (NXB ĐHKTQD)", r"[NEU] [Giáo trình Toàn văn] Thống kê doanh nghiệp - PGS.TS Phan Công Nghĩa (NXB ĐHKTQD).pdf")
    pages, sz = b.save(out_path)
    print(f"DONE: Thống kê doanh nghiệp -> {pages} pages, {sz:.2f} MB")
    return {"name": "Thống kê doanh nghiệp", "pages": pages, "size_mb": sz, "path": out_path}

if __name__ == "__main__":
    res1 = build_math_for_economists()
    res2 = build_probability_statistics()
    res3 = build_principles_of_statistics()
    res4 = build_business_statistics()
    print("\nBATCH 1 COMPLETED SUCCESSFULLY!")
