# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_book_1():
    print("Building Book 1: Toán cho các nhà kinh tế...")
    b = NEUTextbookBuilder(
        title="Toán cho các nhà kinh tế",
        subject_code="TOA101",
        faculty="Toán Kinh tế",
        authors="PGS.TS Nguyễn Cao Văn (Chủ biên) - PGS.TS Trần Thái Ninh - TS Nguyễn Lý Quyên",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN LẦN THỨ 8 CÓ BỔ SUNG CHUYÊN ĐỀ TIẾN SĨ"
    )
    b.build_cover()
    
    toc = [
        {"chapter_num": "1", "chapter_title": "Hàm số, Đạo hàm, Vi phân và Ứng dụng Phân tích Cận biên", "topics": ["Mô hình hàm số kinh tế", "Đạo hàm và giá trị cận biên", "Hệ số co giãn (Elasticity)", "Thặng dư tiêu dùng và sản xuất"]},
        {"chapter_num": "2", "chapter_title": "Đại số Tuyến tính, Không gian Vectơ và Cân bằng Thị trường", "topics": ["Ma trận và định thức", "Hệ phương trình tuyến tính & Định lý Cramer", "Mô hình cân bằng thị trường đa hàng hóa", "Mô hình cân bằng thu nhập quốc dân IS-LM"]},
        {"chapter_num": "3", "chapter_title": "Mô hình Cân đối Liên ngành Input - Output (I-O) của Leontief", "topics": ["Bảng cân đối liên ngành I-O", "Ma trận hệ số chi phí trực tiếp A", "Ma trận nghịch đảo Leontief (I-A)^-1", "Dự báo nhu cầu tổng sản lượng nền kinh tế"]},
        {"chapter_num": "4", "chapter_title": "Hàm Nhiều Biến, Đạo hàm Riêng và Tối ưu hóa Không Ràng buộc", "topics": ["Hàm sản xuất Cobb-Douglas và CES", "Đạo hàm riêng và vi phân toàn phần", "Ma trận Hessian và điều kiện cực trị", "Tối đa hóa lợi nhuận doanh nghiệp đa sản phẩm"]},
        {"chapter_num": "5", "chapter_title": "Tối ưu hóa Có Ràng buộc và Phương pháp Nhân tử Lagrange", "topics": ["Phương pháp nhân tử Lagrange", "Điều kiện cấp một và cấp hai (Bordered Hessian)", "Tối đa hóa thỏa dụng người tiêu dùng", "Cực tiểu hóa chi phí sản xuất", "Điều kiện bù Karush-Kuhn-Tucker (KKT)"]},
        {"chapter_num": "6", "chapter_title": "Phương trình Vi phân, Sai phân và Động thái học Kinh tế", "topics": ["Phương trình vi phân cấp một và ổn định điểm cân bằng", "Mô hình tăng trưởng Solow-Swan liên tục", "Phương trình sai phân cấp một & hai", "Mô hình mạng nhện thị trường (Cobweb Model)"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Hàm số, Đạo hàm, Vi phân và Ứng dụng Phân tích Cận biên",
        introduction="Chương 1 cung cấp nền tảng vi tích phân giải tích cổ điển và hiện đại, giúp sinh viên và nghiên cứu sinh lượng hóa các quy luật kinh tế học vi mô và vĩ mô thông qua phân tích cận biên (Marginal Analysis) và độ co giãn.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Mô hình hàm số kinh tế và Phân tích cận biên",
                "content": "Trong kinh tế học, các khái niệm tổng lượng (Total), trung bình (Average) và cận biên (Marginal) có mối quan hệ giải tích mật thiết. Hàm tổng chi phí TC(Q) thể hiện chi phí phát sinh khi sản xuất Q đơn vị sản lượng. Chi phí cận biên MC(Q) được định nghĩa là đạo hàm bậc nhất của hàm tổng chi phí theo sản lượng: MC = d(TC)/dQ.\n\nTương tự, hàm tổng doanh thu TR(Q) = P(Q)*Q cho phép xác định doanh thu cận biên MR = d(TR)/dQ. Theo nguyên lý kinh tế học vi mô, doanh nghiệp tối đa hóa lợi nhuận tại điểm nơi MR(Q) = MC(Q) với điều kiện đạo hàm cấp hai d^2(Pi)/dQ^2 < 0.",
                "formulas": [
                    "MC(Q) = d(TC)/dQ;  ATC(Q) = TC(Q)/Q",
                    "MR(Q) = d(TR)/dQ = P + Q * (dP/dQ)",
                    "Dieu kien toi uu loi nhuan cap 1: MR(Q*) = MC(Q*)",
                    "Dieu kien toi uu loi nhuan cap 2: d^2(Pi)/dQ^2 = d(MR)/dQ - d(MC)/dQ < 0"
                ],
                "case_studies": [
                    {"title": "Doanh nghiệp thép Hòa Phát tối ưu hóa quy mô sản xuất", "detail": "Hàm chi phí ngắn hạn TC = 0.05*Q^3 - 3*Q^2 + 80*Q + 500. Xác định sản lượng tối ưu khi giá thị trường P = 120 triệu VNĐ/tấn bằng giải phương trình đạo hàm MC = P."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Hệ số co giãn (Elasticity) và Ứng dụng chính sách",
                "content": "Độ co giãn của hàm số y = f(x) theo biến x đo lường phần trăm thay đổi của y khi x thay đổi 1%. Trong kinh tế, hệ số co giãn của cầu theo giá (Price Elasticity of Demand - Ep) quyết định chiến lược định giá và doanh thu của doanh nghiệp.\n\nNếu |Ep| > 1 (cầu co giãn), giảm giá sẽ làm tăng tổng doanh thu. Nếu |Ep| < 1 (cầu kém co giãn), doanh nghiệp có thể tăng giá để gia tăng doanh thu. Mối quan hệ giữa doanh thu cận biên và độ co giãn được mô tả qua hệ thức Amoroso-Robinson: MR = P * (1 + 1/Ep).",
                "formulas": [
                    "E_yx = (dy/dx) * (x/y) = d(ln y) / d(ln x)",
                    "MR = P * (1 - 1/|Ep|)",
                    "He so co gian cheo: E_xy = (dQx/dPy) * (Py/Qx)"
                ],
                "case_studies": [
                    {"title": "Đo lường độ co giãn cầu giá điện EVN", "detail": "Nghiên cứu thực nghiệm tại Việt Nam cho thấy độ co giãn ngắn hạn của cầu điện sinh hoạt là -0.35 (kém co giãn), đòi hỏi chính sách biểu giá điện bậc thang để điều tiết tiêu dùng hiệu quả."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp mở rộng vi tích phân Fréchet trong không gian Banach vô hạn chiều ứng dụng cho các bài toán kinh tế học vĩ mô hiện đại.",
                "Sự tồn tại và tính duy nhất của điểm cân bằng tĩnh trong mô hình thị trường cạnh tranh không hoàn hảo với hàm cầu phi tuyến.",
                "Đề tài Luận án Tiến sĩ: Ước lượng phi tham số (Non-parametric) hàm sản xuất và độ co giãn thay thế vi mô của doanh nghiệp sản xuất Việt Nam."
            ]
        },
        review_questions=[
            "1. Chứng minh hệ thức Amoroso-Robinson MR = P * (1 + 1/Ep) và giải thích ý nghĩa kinh tế khi |Ep| = 1.",
            "2. Cho hàm cầu Q = 1000 - 2P. Hãy tính thặng dư tiêu dùng (Consumer Surplus) tại mức giá thị trường P = 200.",
            "3. Viết code Python bằng thư viện SymPy để giải bài toán tìm cực trị hàm doanh thu và tính độ co giãn giải tích."
        ]
    )

    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Đại số Tuyến tính, Không gian Vectơ và Cân bằng Thị trường",
        introduction="Đại số tuyến tính là ngôn ngữ chuẩn mực để mô hình hóa các hệ thống kinh tế đa thị trường, cân bằng vĩ mô IS-LM và danh mục đầu tư tài chính thông qua phép nhân ma trận, định thức và phân rã phổ.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Ma trận, Định thức và Hệ phương trình tuyến tính",
                "content": "Một hệ gồm n thị trường liên quan dẫn đến hệ phương trình tuyến tính dạng A*X = B, trong đó A là ma trận hệ số n x n, X là vectơ giá cân bằng và B là vectơ nhu cầu ngoại sinh. Định lý Rouché-Capelli xác định điều kiện nghiệm duy nhất thông qua hạng của ma trận hạng rank(A) = rank(A|B) = n.\n\nQuy tắc Cramer cho phép tìm nghiệm tường minh Xi = det(Ai)/det(A), trong đó Ai nhận được từ A bằng cách thay cột thứ i bởi vectơ B. Khi số chiều lớn, các thuật toán phân rã LU, Cholesky và khử Gauss-Jordan được sử dụng để tối ưu tính toán.",
                "formulas": [
                    "He Cramer: A * X = B => X = A^(-1) * B",
                    "X_i = det(A_i) / det(A), voi det(A) != 0",
                    "Dieu kien kha nghich: det(A) != 0 <=> rank(A) = n",
                    "Ma tran nghich dao: A^(-1) = (1/det(A)) * C^T (ma tran phu hop)"
                ],
                "case_studies": [
                    {"title": "Mô hình cân bằng 3 thị trường hàng hóa thay thế", "detail": "Xét hệ thị trường nông sản: Gạo, Ngô, Sắn với hàm cầu và cung phụ thuộc chéo vào giá 3 mặt hàng. Ma trận Jacobi của hệ xác định tính ổn định của cân bằng Walras."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Mô hình Cân bằng vĩ mô IS - LM bằng Ma trận",
                "content": "Mô hình kinh tế vĩ mô đóng giản đơn gồm thị trường hàng hóa (đường IS) và thị trường tiền tệ (đường LM):\nY = C(Y) + I(r) + G_0\nM_0 / P = L(Y, r)\nKhi tuyến tính hóa quanh điểm cân bằng, ta có hệ ma trận 2x2. Nghịch đảo ma trận giải trực tiếp mức sản lượng cân bằng Y* và lãi suất cân bằng r*, đồng thời cho phép tính toán các số nhân chính sách tài khóa và tiền tệ.",
                "formulas": [
                    "[ (1 - c1)   b ] * [ Y ] = [ C0 + I0 + G ]",
                    "[   k       -h ]   [ r ]   [   M/P     ]",
                    "So nhan tai khoa: dY/dG = h / [ (1 - c1)*h + b*k ] > 0",
                    "So nhan tien te: dY/dM = b / [ (1 - c1)*h + b*k ] > 0"
                ],
                "case_studies": [
                    {"title": "Đánh giá chính sách tài khóa mở rộng của Chính phủ Việt Nam", "detail": "Sử dụng ma trận IS-LM ước lượng tác động kích cầu đầu tư công 100.000 tỷ VNĐ đến sản lượng GDP và áp lực tăng lãi suất thị trường liên ngân hàng."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết ma trận không âm Perron-Frobenius và ứng dụng trong cân bằng kinh tế tổng thể.",
                "Phân tích giá trị riêng (Eigenvalues) và vectơ riêng trong việc xác định tính ổn định tiệm cận của hệ động lực kinh tế đa biến.",
                "Đề tài Luận án Tiến sĩ: Khảo sát ma trận liên kết tài chính liên ngân hàng Việt Nam bằng mô hình mạng lưới ma trận (Network Matrix Spillover)."
            ]
        },
        review_questions=[
            "1. Giải thích điều kiện Hawking-Simon trong mô hình đại số tuyến tính kinh tế.",
            "2. Chứng minh số nhân chính sách tiền tệ dY/dM trong mô hình IS-LM luôn dương nếu h > 0 và b > 0.",
            "3. Viết script Python dùng numpy.linalg.solve để giải hệ cân bằng thị trường 4 biến."
        ]
    )

    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Mô hình Cân đối Liên ngành Input - Output (I-O) của Leontief",
        introduction="Mô hình Input - Output do Wassily Leontief (Giải Nobel Kinh tế 1973) phát triển là công cụ toán học nền tảng cho công tác quy hoạch, kế hoạch hóa và phân tích cấu trúc kinh tế quốc dân.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bảng cân đối liên ngành và Ma trận hệ số chi phí trực tiếp",
                "content": "Nền kinh tế gồm n ngành sản xuất. Gọi xij là giá trị sản phẩm của ngành i được ngành j sử dụng làm chi phí trung gian; Xj là tổng giá trị sản lượng của ngành j. Hệ số chi phí trực tiếp aij = xij / Xj phản ánh số đơn vị giá trị ngành i cần thiết để ngành j tạo ra một đơn vị giá trị sản lượng.\n\nMa trận A = [aij] là ma trận vuông cấp n. Vectơ tổng sản lượng X và vectơ cầu cuối cùng Y thỏa mãn phương trình Leontief: X = A*X + Y <=> (I - A)*X = Y.",
                "formulas": [
                    "a_ij = x_ij / X_j  (0 <= a_ij < 1)",
                    "X = A * X + Y  <=>  (I - A) * X = Y",
                    "X = (I - A)^(-1) * Y = B * Y",
                    "B = (I - A)^(-1) = I + A + A^2 + A^3 + ... (Chuoi Neumann)"
                ],
                "case_studies": [
                    {"title": "Bảng I-O nền kinh tế Việt Nam do Tổng cục Thống kê lập", "detail": "Phân tích bảng I-O gồm 164 ngành sản phẩm, tính toán ma trận hệ số chi phí trực tiếp và ma trận nghịch đảo Leontief để xác định các ngành có hệ số lan tỏa cao nhất."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Hệ số lan tỏa và Hệ số độ nhạy của các ngành kinh tế",
                "content": "Phần tử bij của ma trận nghịch đảo Leontief B = (I - A)^(-1) phản ánh nhu cầu sản lượng toàn bộ (cả trực tiếp và gián tiếp) của ngành i khi cầu cuối cùng của ngành j tăng thêm 1 đơn vị. \n\nTổng cột của ma trận B đo lường chỉ số lan tỏa (Backward Linkage) của ngành j, thể hiện khả năng kích thích các ngành cung ứng đầu vào. Tổng hàng đo lường chỉ số nhạy cảm (Forward Linkage), thể hiện mức độ bị kích thích khi toàn bộ nền kinh tế mở rộng.",
                "formulas": [
                    "He so lan toa: FL_j = (1/n * Sum_i(b_ij)) / (1/n^2 * Sum_i Sum_j(b_ij))",
                    "He so nhay: BL_i = (1/n * Sum_j(b_ij)) / (1/n^2 * Sum_i Sum_j(b_ij))",
                    "Nganh mui nhon (Key Sector): FL_j > 1 va BL_j > 1"
                ],
                "case_studies": [
                    {"title": "Đánh giá vai trò mũi nhọn của ngành Công nghiệp Chế biến - Chế tạo", "detail": "Kết quả tính toán bảng I-O cho thấy ngành Công nghiệp chế biến chế tạo có chỉ số lan tỏa đạt 1.38, đóng vai trò đầu tàu kéo theo sự phát triển của logistics, năng lượng và dịch vụ tài chính."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Cân bằng tổng thể có thể tính toán (Computable General Equilibrium - CGE) xây dựng từ Ma trận Hạch toán Xã hội (SAM).",
                "Mô hình I-O Môi trường (Environmentally Extended Input-Output - EEIO) tính toán dấu chân Carbon và phát thải CO2 phạm vi 1, 2, 3 của chuỗi giá trị.",
                "Đề tài Luận án Tiến sĩ: Định lượng tác động của thuế biên giới Carbon (CBAM) đối với xuất khẩu Việt Nam bằng mô hình liên ngành toàn cầu GTAP."
            ]
        },
        review_questions=[
            "1. Điều kiện Hawking-Simon đảm bảo ma trận (I - A) có nghịch đảo không âm là gì?",
            "2. Phân biệt chi phí trực tiếp và chi phí toàn bộ trong phân tích Leontief.",
            "3. Viết chương trình Python tính ma trận nghịch đảo Leontief B = (I - A)^-1 và vẽ biểu đồ thanh hệ số lan tỏa của các ngành."
        ]
    )

    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Hàm Nhiều Biến, Đạo hàm Riêng và Tối ưu hóa Không Ràng buộc",
        introduction="Phần lớn các mô hình kinh tế vi mô và kinh tế lượng liên quan đến nhiều biến số đồng thời. Việc mở rộng giải tích sang không gian đa chiều với đạo hàm riêng, vi phân toàn phần và ma trận Hessian là yêu cầu thiết yếu để thiết lập bài toán tối ưu hóa của các chủ thể kinh tế.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Hàm sản xuất Cobb-Douglas và Hàm CES",
                "content": "Hàm sản xuất Cobb-Douglas Q = A * K^alpha * L^beta phản ánh quan hệ giữa vốn (K) và lao động (L). Tổng alpha + beta xác định quy mô hiệu suất: không đổi (Constant Returns to Scale - CRS khi = 1), tăng theo quy mô (> 1), hoặc giảm theo quy mô (< 1).\n\nHàm CES (Constant Elasticity of Substitution) tổng quát hóa với độ co giãn thay thế không đổi sigma = 1/(1+rho). Đạo hàm riêng cấp một biểu diễn năng suất cận biên: MPK = dQ/dK và MPL = dQ/dL. Tỷ lệ thay thế kỹ thuật cận biên MRTS = MPL / MPK.",
                "formulas": [
                    "Cobb-Douglas: Q = A * K^alpha * L^beta",
                    "Nang suat can bien: MPK = alpha * (Q/K);  MPL = beta * (Q/L)",
                    "MRTS = MPL / MPK = (beta/alpha) * (K/L)",
                    "Ham CES: Q = gamma * [ delta * K^(-rho) + (1-delta) * L^(-rho) ]^(-1/rho)"
                ],
                "case_studies": [
                    {"title": "Ước lượng hàm Cobb-Douglas cho ngành Dệt may Việt Nam", "detail": "Sử dụng dữ liệu mảng 500 doanh nghiệp niêm yết, hồi quy log-log ln(Q) = beta0 + alpha*ln(K) + beta*ln(L) ước lượng được alpha = 0.42, beta = 0.59, kiểm định F-test không bác bỏ giả thuyết alpha + beta = 1."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Tối ưu hóa không điều kiện và Ma trận Hessian",
                "content": "Để tìm cực trị của hàm nhiều biến z = f(x, y), điều kiện cần cấp một (FOC) là các đạo hàm riêng triệt tiêu: fx = 0 và fy = 0. Để xác định điểm tới hạn là cực đại hay cực tiểu, ta khảo sát ma trận Hessian H gồm các đạo hàm riêng cấp hai.\n\nNếu det(H) > 0 và fxx < 0, hàm số đạt cực đại địa phương. Nếu det(H) > 0 và fxx > 0, hàm số đạt cực tiểu. Nếu det(H) < 0, điểm dừng là điểm yên ngựa (Saddle Point). Khi số biến n > 2, dấu của các định thức con chính (Leading Principal Minors) quyết định tính xác định dấu của ma trận Hessian.",
                "formulas": [
                    "Ma tran Hessian H = [ f_xx   f_xy ; f_yx   f_yy ]",
                    "det(H) = f_xx * f_yy - (f_xy)^2",
                    "Cuc dai dia phuong: det(H) > 0 va f_xx < 0",
                    "Cuc tieu dia phuong: det(H) > 0 va f_xx > 0",
                    "Diem yen ngua: det(H) < 0"
                ],
                "case_studies": [
                    {"title": "Tối ưu hóa lợi nhuận của doanh nghiệp độc quyền hai thị trường", "detail": "Doanh nghiệp có hàm chi phí kết hợp C(Q1, Q2) = 2*Q1^2 + Q1*Q2 + 2*Q2^2 và bán sản phẩm trên 2 thị trường độc lập với hàm cầu P1 = 120 - Q1, P2 = 180 - 2*Q2. Thiết lập hàm lợi nhuận và kiểm tra ma trận Hessian."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Tính lồi (Convexity) và bán lồi (Quasi-convexity) trong không gian Rn và Định lý tách tập lồi Hyperplane Separation Theorem.",
                "Định lý phong bì (Envelope Theorem) cho các bài toán tối ưu hóa không ràng buộc và ứng dụng chứng minh Bổ đề Hotelling.",
                "Đề tài Luận án Tiến sĩ: Khảo sát hàm sản xuất cận biên linh hoạt Translog cho các tập đoàn công nghiệp đa ngành tại Việt Nam."
            ]
        },
        review_questions=[
            "1. Phát biểu và chứng minh Định lý Euler về hàm thuần nhất bậc k.",
            "2. Điều kiện Sylvester xác định ma trận nửa xác định âm (Negative Semi-definite) là gì?",
            "3. Sử dụng Python thư viện Scipy.optimize.minimize để giải bài toán tối đa hóa lợi nhuận đa sản phẩm."
        ]
    )

    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Tối ưu hóa Có Ràng buộc và Phương pháp Nhân tử Lagrange",
        introduction="Các quyết định kinh tế cốt lõi luôn diễn ra dưới điều kiện khan hiếm nguồn lực: người tiêu dùng tối đa hóa thỏa dụng dưới ràng buộc ngân sách, doanh nghiệp cực tiểu hóa chi phí dưới ràng buộc mức sản lượng kế hoạch.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phương pháp Nhân tử Lagrange và Ma trận Hessian có viền",
                "content": "Xét bài toán tìm cực trị hàm mục tiêu f(x, y) với ràng buộc đẳng thức g(x, y) = c. Hàm Lagrange được lập: L(x, y, lambda) = f(x, y) - lambda * [g(x, y) - c]. Hệ điều kiện cần cấp 1 gồm 3 phương trình đạo hàm riêng triệt tiêu.\n\nĐiều kiện đủ cấp hai được kiểm tra thông qua định thức ma trận Hessian có viền (Bordered Hessian). Ý nghĩa kinh tế của nhân tử Lagrange lambda chính là giá trị bóng (Shadow Price) hoặc giá cận biên: lambda = df*/dc, phản ánh mức gia tăng của giá trị tối ưu khi nới lỏng ràng buộc ngân sách thêm một đơn vị.",
                "formulas": [
                    "Ham Lagrange: L(x, y, lambda) = f(x, y) + lambda * (c - g(x,y))",
                    "FOC: dL/dx = 0;  dL/dy = 0;  dL/d(lambda) = c - g(x,y) = 0",
                    "Bordered Hessian |H_bar| = det([ 0   g_x   g_y ; g_x   f_xx   f_xy ; g_y   f_yx   f_yy ])",
                    "Cuc dai co dieu kien khi |H_bar| > 0; Cuc tieu khi |H_bar| < 0",
                    "Gia bong: lambda* = df* / dc"
                ],
                "case_studies": [
                    {"title": "Lựa chọn tiêu dùng tối ưu giữa hàng hóa thiết yếu và xa xỉ", "detail": "Hàm thỏa dụng U = X^0.6 * Y^0.4 với ngân sách I = 10 triệu VNĐ, Px = 50.000 VNĐ, Py = 100.000 VNĐ. Giải nhân tử Lagrange tính toán thặng dư thỏa dụng khi ngân sách tăng 1 triệu VNĐ."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Điều kiện Kuhn - Tucker cho Ràng buộc Bất đẳng thức",
                "content": "Khi các ràng buộc mang dạng bất đẳng thức g(x) <= c hoặc x >= 0, phương pháp nhân tử Lagrange được mở rộng thành điều kiện Karush-Kuhn-Tucker (KKT). Điều kiện bù (Complementary Slackness): lambda * [c - g(x)] = 0 chỉ ra rằng nếu ràng buộc không chạm biên (inactive, c - g(x) > 0) thì nhân tử lambda = 0; ngược lại nếu lambda > 0 thì ràng buộc phải thỏa mãn dấu bằng (active).",
                "formulas": [
                    "Bai toan: Max f(x) subject to g_i(x) <= c_i, x >= 0",
                    "Dieu kien KKT FOC: dL/dx_j <= 0 va x_j * (dL/dx_j) = 0",
                    "Dieu kien bu (Complementary slackness): lambda_i * (c_i - g_i(x)) = 0",
                    "Dieu kien khong am: lambda_i >= 0; x_j >= 0"
                ],
                "case_studies": [
                    {"title": "Đầu tư tài chính dưới ràng buộc hạn mức tín dụng", "detail": "Tối đa hóa lợi nhuận danh mục tài sản chịu ràng buộc vốn vay không vượt quá tỷ lệ LTV (Loan-to-Value) 70% theo quy định của Ngân hàng Nhà nước."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Định lý Duality trong bài toán tối ưu hóa lồi: Khoảng cách đối ngẫu (Duality Gap) và hàm Lagrange đối ngẫu.",
                "Hàm thỏa dụng gián tiếp V(P, I), Bổ đề Roy và Phương trình Slutsky phân rã hiệu ứng thay thế và hiệu ứng thu nhập.",
                "Đề tài Luận án Tiến sĩ: Ước lượng hệ thống nhu cầu tiêu dùng gần như lý tưởng (AIDS - Almost Ideal Demand System) cho hộ gia đình Việt Nam."
            ]
        },
        review_questions=[
            "1. Chứng minh Bổ đề Shephard: Chi phí cận biên theo giá yếu tố đầu vào bằng lượng cầu yếu tố đó dC/dw = L*.",
            "2. Viết điều kiện KKT cho bài toán tối đa hóa lợi nhuận khi có trần hạn ngạch phát thải CO2.",
            "3. Viết code Python sử dụng thư viện cvxpy để giải bài toán tối ưu hóa danh mục Markowitz với ràng buộc cấm bán khống (no short-sales)."
        ]
    )

    # Chapter 6
    b.add_chapter(
        chap_num="6",
        chap_title="Phương trình Vi phân, Sai phân và Động thái học Kinh tế",
        introduction="Nền kinh tế luôn biến chuyển theo thời gian. Phương trình vi phân (cho thời gian liên tục) và phương trình sai phân (cho thời gian rời rạc) cung cấp khung phân tích toán học chính xác để kiểm tra tính ổn định của cân bằng vĩ mô và chu kỳ kinh tế.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phương trình vi phân cấp một và Mô hình tăng trưởng Solow - Swan",
                "content": "Phương trình vi phân tuyến tính cấp một dy/dt + a*y = b có nghiệm tổng quát y(t) = (y0 - b/a)*exp(-a*t) + b/a. Điểm cân bằng tĩnh y* = b/a ổn định tiệm cận khi và chỉ khi a > 0.\n\nTrong mô hình Solow-Swan, phương trình tích lũy tư bản theo thời gian liên tục dk/dt = s*f(k) - (n + delta)*k mô tả sự thay đổi của trang bị tư bản trên một lao động. Tại trạng thái dừng (steady state) dk/dt = 0, ta có s*f(k*) = (n + delta)*k*.",
                "formulas": [
                    "Nghiem tong quat: y(t) = [ y(0) - y* ] * e^(-a*t) + y*",
                    "Dieu kien on dinh: a > 0 <=> lim_{t -> infty} y(t) = y*",
                    "Phuong trinh Solow: dk/dt = s * k^alpha - (n + delta) * k",
                    "Trang thai dung: k* = [ s / (n + delta) ]^(1 / (1 - alpha))"
                ],
                "case_studies": [
                    {"title": "Mô phỏng tốc độ hội tụ kinh tế Việt Nam theo mô hình Solow", "detail": "Với tỷ lệ tiết kiệm s = 30%, tốc độ tăng dân số n = 1.1%, tốc độ khấu hao delta = 5%, mô phỏng quỹ đạo vốn k(t) và thời gian bán phân kỳ (half-life of convergence) đạt 14 năm."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Phương trình sai phân và Mô hình mạng nhện (Cobweb Model)",
                "content": "Khi các quyết định sản xuất có độ trễ thời gian (đặc biệt trong nông nghiệp), cung kỳ t phụ thuộc vào giá kỳ trước: St = S(P_{t-1}), trong khi cầu phụ thuộc giá hiện hành Dt = D(Pt). Phương trình cân bằng thị trường dẫn đến phương trình sai phân cấp một của giá Pt.\n\nQuỹ đạo giá Pt = (P0 - P*)*(-b/d)^t + P* cho thấy thị trường hội tụ về giá cân bằng P* khi và chỉ khi |-b/d| < 1, tức là độ dốc đường cung d nhỏ hơn độ dốc đường cầu b.",
                "formulas": [
                    "Ham cau: D_t = a - b * P_t;  Ham cung: S_t = -c + d * P_{t-1}",
                    "Can bang: a - b * P_t = -c + d * P_{t-1} => P_t = -(d/b) * P_{t-1} + (a+c)/b",
                    "Nghiem: P_t = [ P_0 - P* ] * (-d/b)^t + P*",
                    "Dieu kien dao dong hoi tu: |d/b| < 1 <=> d < b"
                ],
                "case_studies": [
                    {"title": "Biến động chu kỳ giá thịt lợn và cà phê tại Việt Nam", "detail": "Phân tích số liệu chuỗi giá thịt lợn 2018-2024 minh họa trực quan chu kỳ mạng nhện bùng nổ (d > b) khi người chăn nuôi phản ứng trễ với tín hiệu giá thị trường."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương trình vi phân ngẫu nhiên Itô (Stochastic Differential Equations - SDE) và Bổ đề Itô trong tài chính định lượng.",
                "Hệ phương trình vi phân phi tuyến đa chiều, Ma trận Jacobian và Phân tích sơ đồ pha (Phase Diagram) trong mô hình Ramsey-Cass-Koopmans.",
                "Đề tài Luận án Tiến sĩ: Ước lượng mô hình cân bằng tổng thể ngẫu nhiên động (DSGE) cho nền kinh tế nhỏ, mở cửa Việt Nam bằng phương pháp Bayesian."
            ]
        },
        review_questions=[
            "1. Phân tích điều kiện ổn định của phương trình sai phân cấp hai Y_{t+2} + a1*Y_{t+1} + a2*Y_t = b bằng nghiệm phương trình đặc trưng.",
            "2. Vẽ sơ đồ pha (Phase Diagram) cho bài toán tối ưu hóa tiêu dùng liên thời gian của mô hình Ramsey.",
            "3. Viết script Python mô phỏng quỹ đạo mạng nhện Cobweb và vẽ biểu đồ pha trực quan."
        ]
    )
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\07_Toán, Thống kê, Kinh tế lượng & Tin học\[NEU] Toán cho các nhà kinh tế - PGS.TS Nguyễn Cao Văn (NXB ĐHKTQD)"
    pdf_name = "[NEU] [Giáo trình Toàn văn] Toán cho các nhà kinh tế - PGS.TS Nguyễn Cao Văn (NXB ĐHKTQD).pdf"
    p_path = os.path.join(out_dir, pdf_name)
    pages, sz = b.save(p_path)
    print(f"-> Book 1 Completed: {pages} pages, {sz:.2f} MB saved at: {p_path}")
    return {"id": 1, "title": b.title, "pages": pages, "size_mb": sz, "path": p_path}

def build_book_2():
    print("Building Book 2: Xác suất và Thống kê toán...")
    b = NEUTextbookBuilder(
        title="Xác suất và Thống kê toán",
        subject_code="TOA102",
        faculty="Toán Kinh tế",
        authors="PGS.TS Nguyễn Cao Văn (Chủ biên) - PGS.TS Trần Thái Ninh - TS Ngô Văn Thứ",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN LẦN THỨ 7 CÓ BỔ SUNG CHUYÊN ĐỀ TIẾN SĨ"
    )
    b.build_cover()
    
    toc = [
        {"chapter_num": "1", "chapter_title": "Biến cố Ngẫu nhiên và Không gian Xác suất", "topics": ["Không gian mẫu & Biến cố", "Định nghĩa cổ điển, hình học, tiên đề Kolmogorov", "Xác suất có điều kiện & Công thức Bayes", "Ứng dụng thẩm định rủi ro tín dụng"]},
        {"chapter_num": "2", "chapter_title": "Đại lượng Ngẫu nhiên và Quy luật Phân phối Xác suất", "topics": ["Biến ngẫu nhiên rời rạc & liên tục", "Hàm khối xác suất PMF & Hàm mật độ PDF", "Các phân phối thông dụng: Nhị thức, Poisson, Chuẩn, Student, Chi-bình phương", "Kỳ vọng, Phương sai, Moment"]},
        {"chapter_num": "3", "chapter_title": "Đại lượng Ngẫu nhiên Nhiều Chiều và Định lý Giới hạn", "topics": ["Phân phối đồng thời & Phân phối biên duyên", "Hiệp phương sai Covariance & Tương quan Pearson", "Luật số lớn Chebyshev & Khinchin", "Định lý giới hạn trung tâm (CLT)"]},
        {"chapter_num": "4", "chapter_title": "Lý thuyết Mẫu và Ước lượng Tham số Thống kê", "topics": ["Mẫu ngẫu nhiên & Thống kê mẫu", "Phương pháp ước lượng hợp lý cực đại (MLE)", "Tính chất ước lượng: Không chệch, Hiệu quả, Nhất quán", "Ước lượng khoảng tin cậy cho kỳ vọng, tỷ lệ và phương sai"]},
        {"chapter_num": "5", "chapter_title": "Kiểm định Giả thuyết Thống kê", "topics": ["Giả thuyết H0 và đối thuyết H1", "Sai lầm loại I và loại II, Lực kiểm định", "Kiểm định giá trị trung bình 1 mẫu & 2 mẫu", "Kiểm định tỷ lệ và phương sai", "Kiểm định Chi-bình phương về tính độc lập"]},
        {"chapter_num": "6", "chapter_title": "Phân tích Phương sai (ANOVA) và Kiểm định Phi tham số", "topics": ["ANOVA một nhân tố và hai nhân tố", "Kiểm định hậu nghiệm Tukey HSD", "Kiểm định phi tham số Mann-Whitney U & Kruskal-Wallis", "Kiểm định chuẩn hóa Kolmogorov-Smirnov & Shapiro-Wilk"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Biến cố Ngẫu nhiên và Không gian Xác suất",
        introduction="Lý thuyết xác suất là nền tảng toán học của việc ra quyết định kinh tế trong điều kiện bất định và là cơ sở lý luận cho toàn bộ kinh tế lượng hiện đại.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Không gian biến cố và Các tiên đề xác suất Kolmogorov",
                "content": "Xét phép thử ngẫu nhiên với không gian mẫu Omega chứa tất cả các biến cố sơ cấp. Một đại số sigma F là tập hợp các biến cố con thỏa mãn các tiên đề đóng kín với phép hợp và phần bù. \n\nHệ tiên đề Kolmogorov xác định hàm xác suất P: F -> [0, 1] thỏa mãn: (1) P(Omega) = 1; (2) P(A) >= 0 với mọi A; (3) Tính cộng đếm được đối với các biến cố xung khắc rời rạc.",
                "formulas": [
                    "0 <= P(A) <= 1;  P(Omega) = 1;  P(Rong) = 0",
                    "P(A hop B) = P(A) + P(B) - P(A giao B)",
                    "Bien co doi: P(A_bar) = 1 - P(A)"
                ],
                "case_studies": [
                    {"title": "Định lượng xác suất vỡ nợ doanh nghiệp phát hành trái phiếu", "detail": "Mô hình xác suất Merton mô hình hóa vốn chủ sở hữu như quyền chọn mua trên tài sản công ty, xác định xác suất tài sản giảm xuống dưới ngưỡng nợ phải trả."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Xác suất có điều kiện và Công thức Bayes",
                "content": "Xác suất có điều kiện P(A|B) = P(AB)/P(B) đo lường khả năng xảy ra biến cố A khi biết biến cố B đã xuất hiện. Công thức xác suất đầy đủ và công thức Bayes cho phép cập nhật xác suất tiên nghiệm (Prior) thành xác suất hậu nghiệm (Posterior) khi có thông tin mới.\n\nTrong tài chính - ngân hàng, Bayes là nền tảng để chấm điểm tín dụng (Credit Scoring) và sàng lọc gian lận giao dịch thẻ trực tuyến.",
                "formulas": [
                    "P(A|B) = P(A giao B) / P(B), voi P(B) > 0",
                    "Cong thuc xac suat day du: P(B) = Sum_{i=1}^n P(A_i) * P(B|A_i)",
                    "Cong thuc Bayes: P(A_k|B) = [ P(A_k) * P(B|A_k) ] / [ Sum_{i=1}^n P(A_i) * P(B|A_i) ]"
                ],
                "case_studies": [
                    {"title": "Cập nhật đánh giá rủi ro khách hàng vay vốn tại BIDV", "detail": "Xác suất vỡ nợ ban đầu là 3%. Nếu khách hàng có lịch sử chậm trả trên CIC (biến cố tín hiệu), công thức Bayes cập nhật xác suất vỡ nợ hậu nghiệm lên 28.5%."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết độ đo tích phân Lebesgue-Stieltjes và xây dựng không gian xác suất hình thức (Omega, F, P).",
                "Phương pháp cập nhật Bayesian Hierarchical Models trong kinh tế lượng lượng giác và kinh tế học vi mô thực nghiệm.",
                "Đề tài Luận án Tiến sĩ: Ứng dụng Bayesian Structural Time Series (BSTS) trong dự báo tức thời (Nowcasting) chỉ số lạm phát lõi CPI Việt Nam."
            ]
        },
        review_questions=[
            "1. Phân biệt tính độc lập ngẫu nhiên giữa các biến cố và tính xung khắc hình học.",
            "2. Trình bày ứng dụng công thức Bayes trong mô hình thẩm định gian lận tài chính.",
            "3. Viết code Python tính xác suất hậu nghiệm Bayes với phân phối Beta-Binomial."
        ]
    )

    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Đại lượng Ngẫu nhiên và Quy luật Phân phối Xác suất",
        introduction="Đại lượng ngẫu nhiên ánh xạ kết quả từ không gian mẫu sang trục số thực, cho phép phân tích thống kê định lượng về lợi suất, thu nhập, chi phí và thời gian chờ.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Đại lượng ngẫu nhiên rời rạc và liên tục",
                "content": "Đại lượng ngẫu nhiên X được mô tả hoàn toàn qua hàm phân phối tích lũy F(x) = P(X <= x). Nếu X rời rạc, phân phối được đặc trưng bởi hàm khối xác suất PMF P(X = xi). Nếu X liên tục, phân phối được đặc trưng bởi hàm mật độ xác suất PDF f(x) = dF(x)/dx.\n\nKỳ vọng toán học E(X) là trọng tâm phân phối, phương sai Var(X) = E[(X - E(X))^2] đo lường mức độ phân tán rủi ro. Độ lệch chuẩn SD(X) là căn bậc hai của phương sai.",
                "formulas": [
                    "Ham tich luy: F(x) = P(X <= x) = Integral_{-infty}^x f(t) dt",
                    "Ky vong lien tuc: E(X) = Integral_{-infty}^{+infty} x * f(x) dx",
                    "Phuong sai: Var(X) = E(X^2) - [E(X)]^2",
                    "Do bat doi xung: Skewness = E[ (X - mu)^3 ] / sigma^3",
                    "Do nhon: Kurtosis = E[ (X - mu)^4 ] / sigma^4"
                ],
                "case_studies": [
                    {"title": "Đo lường rủi ro danh mục cổ phiếu VN30", "detail": "Phân tích chuỗi lợi suất ngày cho thấy độ nhọn Kurtosis = 5.8 > 3 (phân phối đuôi béo Fat Tails), cảnh báo việc sử dụng phân phối chuẩn sẽ đánh giá thấp nghiêm trọng rủi ro sụt giảm cực đoan."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Các quy luật phân phối xác suất quan trọng trong kinh tế",
                "content": "Phân phối chuẩn Normal N(mu, sigma^2) là nền tảng của kinh tế học cổ điển. Các phân phối phái sinh từ phân phối chuẩn đóng vai trò cốt tử trong suy diễn thống kê: phân phối Chi-bình phương (tổng bình phương biến chuẩn), phân phối Student t (tỷ số giữa biến chuẩn và căn bậc hai Chi-bình phương), và phân phối Fisher F (tỷ số hai biến Chi-bình phương độc lập).\n\nNgoài ra, phân phối Log-normal được sử dụng để mô hình hóa giá tài sản tài chính và phân phối thu nhập hộ gia đình.",
                "formulas": [
                    "Phan phoi chuan: f(x) = (1 / (sigma * sqrt(2*pi))) * exp( - (x - mu)^2 / (2*sigma^2) )",
                    "Bien chuan hoa: Z = (X - mu) / sigma ~ N(0, 1)",
                    "Phan phoi Student t_k = Z / sqrt( Chi^2_k / k )",
                    "Phan phoi Fisher F(m, n) = ( Chi^2_m / m ) / ( Chi^2_n / n )"
                ],
                "case_studies": [
                    {"title": "Mô hình định giá quyền chọn Black - Scholes - Merton", "detail": "Giả định giá cổ phiếu tuân theo phân phối Log-normal, công thức Black-Scholes sử dụng hàm tích lũy phân phối chuẩn tắc N(d1) và N(d2) để định giá quyền chọn mua chuẩn."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết giá trị cực trị (Extreme Value Theory - EVT) và các phân phối Generalized Pareto (GPD) trong quản trị rủi ro đuôi tài chính.",
                "Hàm sinh mômen (Moment Generating Function - MGF) và Phương pháp tổng quát hóa mômen (GMM) trong ước lượng tham số phi tuyến.",
                "Đề tài Luận án Tiến sĩ: Mô hình hóa rủi ro thanh khoản ngân hàng Việt Nam bằng phân phối đuôi béo Student-t và Copula phi đối xứng."
            ]
        },
        review_questions=[
            "1. Chứng minh tính chất Var(a*X + b) = a^2 * Var(X).",
            "2. Trình bày mối liên hệ giải tích giữa phân phối Chi-bình phương, Student t và Fisher F.",
            "3. Viết code Python kiểm tra tính chuẩn của chuỗi dữ liệu tài chính bằng kiểm định Jarque-Bera."
        ]
    )

    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Đại lượng Ngẫu nhiên Nhiều Chiều và Định lý Giới hạn",
        introduction="Chương 3 nghiên cứu hành vi đồng thời của vectơ ngẫu nhiên nhiều chiều, mối tương quan giữa các biến số và cơ sở toán học của suy diễn mẫu lớn thông qua Luật số lớn và Định lý Giới hạn Trung tâm.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phân phối đồng thời và Hệ số tương quan",
                "content": "Xét cặp biến ngẫu nhiên (X, Y). Hàm mật độ đồng thời f(x, y) thỏa mãn tích phân trên toàn mặt phẳng bằng 1. Hàm mật độ biên duyên fx(x) nhận được bằng cách tích phân f(x, y) theo biến y.\n\nHiệp phương sai Cov(X, Y) = E[(X - mu_x)(Y - mu_y)] đo lường xu hướng biến thiên cùng chiều hay ngược chiều. Hệ số tương quan Pearson rho_xy = Cov(X,Y)/(sigma_x * sigma_y) chuẩn hóa giá trị trong khoảng [-1, 1]. Khi rho = 0, hai biến không tương quan tuyến tính.",
                "formulas": [
                    "Cov(X, Y) = E(XY) - E(X)*E(Y)",
                    "rho_xy = Cov(X, Y) / [ sigma_x * sigma_y ]  (-1 <= rho_xy <= 1)",
                    "Var(a*X + b*Y) = a^2*Var(X) + b^2*Var(Y) + 2*a*b*Cov(X, Y)",
                    "Doc lap ngau nhien: f(x, y) = f_x(x) * f_y(y) => Cov(X, Y) = 0"
                ],
                "case_studies": [
                    {"title": "Đa dạng hóa danh mục đầu tư Markowitz", "detail": "Phân tích 2 cổ phiếu ngành công nghệ FPT và ngành ngân hàng VCB. Do hệ số tương quan rho = 0.28 thấp, việc kết hợp danh mục 50-50 làm giảm độ lệch chuẩn rủi ro danh mục 22% so với đầu tư đơn lẻ."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Luật số lớn và Định lý Giới hạn Trung tâm (CLT)",
                "content": "Bất đẳng thức Chebyshev P(|X - mu| >= k*sigma) <= 1/k^2 là cơ sở chứng minh Luật số lớn. Theo luật Khinchin, trung bình mẫu X_bar của mẫu độc lập cùng phân phối (i.i.d) hội tụ theo xác suất về kỳ vọng toán mu.\n\nĐịnh lý Giới hạn Trung tâm (Lindeberg-Lévy CLT) khẳng định rằng với kích thước mẫu n đủ lớn, phân phối của trung bình mẫu X_bar xấp xỉ phân phối chuẩn N(mu, sigma^2/n), bất kể phân phối gốc của tổng thể là gì. Đây là hòn đá tảng cho toàn bộ lý thuyết mẫu và kiểm định thống kê.",
                "formulas": [
                    "Bat dang thuc Chebyshev: P( |X - mu| >= epsilon ) <= Var(X) / epsilon^2",
                    "Luat so lon (WLLN): lim_{n -> infty} P( |X_bar_n - mu| < epsilon ) = 1",
                    "Dinh ly CLT: sqrt(n) * (X_bar_n - mu) / sigma  -->  N(0, 1) khi n -> infty"
                ],
                "case_studies": [
                    {"title": "Mô phỏng Monte Carlo kiểm chứng Định lý Giới hạn Trung tâm", "detail": "Tạo 10.000 mẫu ngẫu nhiên từ phân phối đều Uniform(0, 1). Khi tính trung bình mẫu n = 30, đồ thị phân phối tần số của trung bình mẫu khớp hoàn hảo với đường cong hình chuông Gauss chuẩn."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Copula Sklar: Tách biệt phân phối biên duyên và cấu trúc phụ thuộc phi tuyến trong kinh tế lượng tài chính.",
                "Định lý Giới hạn Trung tâm chức năng (Functional Central Limit Theorem - Donsker's Invariance Principle) và Chuyển động Brown chuẩn.",
                "Đề tài Luận án Tiến sĩ: Mô hình hóa sự lây lan rủi ro hệ thống giữa thị trường chứng khoán Việt Nam và thị trường quốc tế bằng Time-varying Copula."
            ]
        },
        review_questions=[
            "1. Chứng minh rằng nếu X và Y độc lập ngẫu nhiên thì Cov(X, Y) = 0, nhưng chiều ngược lại không luôn đúng.",
            "2. Giải thích tại sao Định lý Giới hạn Trung tâm cho phép áp dụng kiểm định chuẩn cho các biến số kinh tế có phân phối lệch.",
            "3. Viết script Python mô phỏng 100.000 lần tung đồng xu để kiểm chứng Luật số lớn."
        ]
    )

    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Lý thuyết Mẫu và Ước lượng Tham số Thống kê",
        introduction="Mục tiêu của thống kê suy diễn là từ thông tin của mẫu ngẫu nhiên suy rộng ra các đặc trưng của tổng thể. Chương 4 trình bày các phương pháp ước lượng điểm OLS, MLE và ước lượng khoảng tin cậy.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phương pháp Ước lượng Hợp lý Cực đại (MLE)",
                "content": "Phương pháp ước lượng hợp lý cực đại (Maximum Likelihood Estimation - MLE) tìm bộ tham số theta sao cho xác suất quan sát được mẫu dữ liệu thực tế là lớn nhất. Hàm hợp lý L(theta) được định nghĩa là tích các hàm mật độ của các quan sát i.i.d.\n\nTrong thực hành, việc tối đa hóa hàm Log-Likelihood ln L(theta) thuận tiện hơn về mặt vi tích phân. Nghiệm của phương trình d(ln L)/d(theta) = 0 cho ta ước lượng MLE theta_hat. Ước lượng MLE có các tính chất tiệm cận tối ưu: nhất quán, chuẩn tiệm cận và đạt chặn dưới hiệu quả Cramér-Rao.",
                "formulas": [
                    "Ham hop ly: L(theta; X) = Product_{i=1}^n f(x_i; theta)",
                    "Ham Log-Likelihood: ln L(theta) = Sum_{i=1}^n ln f(x_i; theta)",
                    "Phuong trinh diem toi han: d(ln L(theta)) / d(theta) = 0",
                    "Ma tran thong tin Fisher: I(theta) = - E[ d^2(ln L) / d(theta)^2 ]",
                    "Chan duoi Cramer-Rao: Var(theta_hat) >= 1 / I(theta)"
                ],
                "case_studies": [
                    {"title": "Ước lượng tham số quy luật Poisson cho số lượng sự cố giao dịch", "detail": "Số vụ gián đoạn giao dịch trên sàn HOSE được mô hình hóa bằng phân phối Poisson. Sử dụng MLE ước lượng tham số lambda_hat = X_bar = 2.4 sự cố/tháng."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Ước lượng Khoảng Tin cậy",
                "content": "Khoảng tin cậy (1 - alpha) cho tham số theta là khoảng ngẫu nhiên [theta_L, theta_U] sao cho xác suất khoảng này chứa tham số thực theta bằng 1 - alpha. \n\nKhi ước lượng kỳ vọng mu với phương sai tổng thể sigma đã biết, sử dụng biến chuẩn Z. Khi sigma chưa biết và mẫu nhỏ n < 30, sử dụng phân phối Student t với n-1 bậc tự do. Tương tự, khoảng tin cậy cho phương sai sigma^2 dựa trên phân phối Chi-bình phương.",
                "formulas": [
                    "Khoang tin cay cho mu (sigma biet): X_bar +- Z_{alpha/2} * (sigma / sqrt(n))",
                    "Khoang tin cay cho mu (sigma chua biet): X_bar +- t_{alpha/2, n-1} * (s / sqrt(n))",
                    "Khoang tin cay cho ty le p: p_hat +- Z_{alpha/2} * sqrt( p_hat*(1 - p_hat) / n )",
                    "Khoang tin cay cho phuong sai: [ (n-1)*s^2 / Chi^2_{alpha/2, n-1} , (n-1)*s^2 / Chi^2_{1-alpha/2, n-1} ]"
                ],
                "case_studies": [
                    {"title": "Ước lượng thu nhập bình quân người lao động Hà Nội", "detail": "Khảo sát mẫu ngẫu nhiên n = 400 lao động cho trung bình mẫu 14.5 triệu VNĐ/tháng, độ lệch chuẩn s = 3.2 triệu. Khoảng tin cậy 95% cho thu nhập trung bình tổng thể là [14.18, 14.81] triệu VNĐ."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp tái chọn mẫu Bootstrap phi tham số (Non-parametric Bootstrap) và ước lượng khoảng tin cậy BCa (Bias-Corrected and Accelerated).",
                "Lý thuyết mẫu lớn: Tính khả vi bậc hai theo nghĩa xác suất (Differentiability in Quadratic Mean) và Hiệu quả tiệm cận.",
                "Đề tài Luận án Tiến sĩ: Ước lượng phi tham số phân vị có điều kiện (Quantile Regression) cho bất bình đẳng thu nhập tại Việt Nam."
            ]
        },
        review_questions=[
            "1. Phân biệt tính không chệch (Unbiasedness) và tính nhất quán (Consistency) của một ước lượng thống kê.",
            "2. Chứng minh rằng phương sai mẫu điều chỉnh s^2 = Sum(Xi - X_bar)^2 / (n - 1) là ước lượng không chệch của phương sai tổng thể sigma^2.",
            "3. Viết code Python thực hiện Bootstrap 1.000 lần để tính sai số chuẩn và khoảng tin cậy cho trung vị mẫu."
        ]
    )

    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Kiểm định Giả thuyết Thống kê",
        introduction="Kiểm định giả thuyết là quy trình đưa ra quyết định có bác bỏ một nhận định về tham số tổng thể hay không dựa trên bằng chứng dữ liệu mẫu.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Nguyên lý kiểm định và Sai lầm quyết định",
                "content": "Một bài toán kiểm định gồm giả thuyết không H0 (trạng thái bình thường) và đối thuyết H1. Trong suy diễn thống kê luôn tiềm ẩn hai loại sai lầm: Sai lầm loại I (bác bỏ H0 khi H0 đúng, xác suất alpha) và Sai lầm loại II (chấp nhận H0 khi H0 sai, xác suất beta).\n\nLực kiểm định (Power of test) = 1 - beta là xác suất bác bỏ chính xác H0 khi H1 đúng. Giá trị P-value là mức ý nghĩa nhỏ nhất mà tại đó H0 bị bác bỏ. Nếu P-value < alpha, ta bác bỏ giả thuyết H0 ở mức ý nghĩa alpha.",
                "formulas": [
                    "Sai lam loai I: alpha = P( Bac bo H0 | H0 dung )",
                    "Sai lam loai II: beta = P( Khong bac bo H0 | H0 sai )",
                    "Luc kiem dinh (Power): 1 - beta = P( Bac bo H0 | H1 dung )",
                    "Quy tac quyet dinh: P-value < alpha <=> Bac bo H0"
                ],
                "case_studies": [
                    {"title": "Kiểm định hiệu quả chiến dịch khuyến mãi bán lẻ", "detail": "Doanh nghiệp kiểm định xem doanh thu bình quân sau chiến dịch có thực sự cao hơn mức cũ 50 triệu VNĐ/ngày không. Thống kê t-test cho P-value = 0.012 < 0.05, bác bỏ H0, khẳng định chiến dịch có hiệu quả thực sự."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Kiểm định Trung bình hai mẫu và Kiểm định Chi-bình phương",
                "content": "Kiểm định so sánh trung bình 2 mẫu độc lập (Two-sample t-test) khảo sát xem hai tổng thể có cùng kỳ vọng không, phụ thuộc vào việc hai tổng thể có đồng nhất phương sai hay không (kiểm định Levene). Đối với mẫu ghép cặp (Paired t-test), ta kiểm định trên sai phân d = X - Y.\n\nKiểm định Chi-bình phương về tính độc lập (Chi-square Test of Independence) kiểm tra mối quan hệ liên kết giữa hai biến định tính dựa trên bảng tiếp biến r x c bằng cách so sánh tần số thực tế Oij và tần số lý thuyết Eij.",
                "formulas": [
                    "Thong ke 2 mau doc lap (phuong sai bang): t = (X_bar_1 - X_bar_2) / [ s_p * sqrt(1/n1 + 1/n2) ]",
                    "Thong ke mau ghep cap: t = d_bar / ( s_d / sqrt(n) )",
                    "Thong ke Chi-binh phuong: Chi^2 = Sum_i Sum_j [ (O_ij - E_ij)^2 / E_ij ]",
                    "Bac tu do: df = (r - 1) * (c - 1)"
                ],
                "case_studies": [
                    {"title": "Phân tích mối liên hệ giữa ngành nghề kinh doanh và tỷ lệ nợ xấu", "detail": "Sử dụng kiểm định Chi-bình phương trên mẫu 1.200 hồ sơ vay tại ngân hàng thương mại, thu được Chi^2 = 34.6 (p < 0.001), chứng minh nợ xấu phụ thuộc có ý nghĩa thống kê vào ngành nghề."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Bổ đề Neyman-Pearson và tính chất kiểm định mạnh nhất đồng đều (Uniformly Most Powerful - UMP test).",
                "Kiểm định tỷ số hợp lý (Likelihood Ratio Test - LRT), Kiểm định Wald và Kiểm định nhân tử Lagrange (LM Score Test).",
                "Đề tài Luận án Tiến sĩ: Kiểm định phi chuẩn giả thuyết biến động bất cân xứng trên thị trường chứng khoán Việt Nam sử dụng phương pháp Permutation Test."
            ]
        },
        review_questions=[
            "1. Phân biệt kiểm định 1 phía (One-tailed) và 2 phía (Two-tailed). Khi nào bắt buộc phải dùng kiểm định 1 phía?",
            "2. Trình bày tam giác kiểm định tương đương tiệm cận: Wald, Likelihood Ratio (LR) và Lagrange Multiplier (LM).",
            "3. Viết script Python dùng scipy.stats.ttest_ind và scipy.stats.chi2_contingency để thực hiện các bài toán kiểm định mẫu."
        ]
    )

    # Chapter 6
    b.add_chapter(
        chap_num="6",
        chap_title="Phân tích Phương sai (ANOVA) và Kiểm định Phi tham số",
        introduction="Khi so sánh kỳ vọng của từ 3 nhóm tổng thể trở lên hoặc khi dữ liệu vi phạm giả thiết phân phối chuẩn, ANOVA và các kỹ thuật phi tham số là công cụ phân tích không thể thay thế.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phân tích Phương sai một nhân tố (One-way ANOVA)",
                "content": "Phân tích phương sai một nhân tố kiểm định giả thuyết H0: mu1 = mu2 = ... = muk. Tổng biến thiên toàn bộ (SST) được phân rã thành biến thiên giữa các nhóm (SSB - giải thích bởi yếu tố xử lý) và biến thiên nội bộ nhóm (SSW - sai số ngẫu nhiên).\n\nThống kê kiểm định F = MSB / MSW tuân theo phân phối Fisher với (k-1, N-k) bậc tự do. Khi bác bỏ H0, kiểm định so sánh bội Tukey HSD được áp dụng để xác định chính xác cặp nhóm nào có sự khác biệt có ý nghĩa thống kê.",
                "formulas": [
                    "SST = SSB + SSW",
                    "SSB = Sum_{j=1}^k n_j * (X_bar_j - X_bar_grand)^2;  df_B = k - 1",
                    "SSW = Sum_{j=1}^k Sum_{i=1}^{n_j} (X_ij - X_bar_j)^2;  df_W = N - k",
                    "Thong ke F = MSB / MSW = [ SSB / (k - 1) ] / [ SSW / (N - k) ]"
                ],
                "case_studies": [
                    {"title": "So sánh năng suất lao động giữa 3 vùng kinh tế trọng điểm", "detail": "Khảo sát 150 doanh nghiệp chia đều cho 3 vùng: Bắc Bộ, Trung Bộ, Nam Bộ. Thống kê F = 14.8 (p < 0.001), kết hợp kiểm định Tukey HSD cho thấy năng suất Nam Bộ cao hơn có ý nghĩa so với Trung Bộ."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Kiểm định Phi tham số (Non-parametric Tests)",
                "content": "Khi dữ liệu ở dạng thứ bậc (Ordinal) hoặc phân phối có độ lệch lớn, các kiểm định tham số mất hiệu lực. Kiểm định Mann-Whitney U thay thế t-test cho 2 mẫu độc lập bằng cách so sánh tổng hạng (Rank Sum).\n\nKiểm định Kruskal-Wallis thay thế ANOVA một nhân tố cho k mẫu độc lập. Kiểm định Wilcoxon Signed-Rank thay thế Paired t-test. Kiểm định Kolmogorov-Smirnov so sánh hàm phân phối thực nghiệm với hàm phân phối lý thuyết để kiểm định tính chuẩn.",
                "formulas": [
                    "Mann-Whitney: U = n1*n2 + [ n1*(n1 + 1)/2 ] - R1",
                    "Kruskal-Wallis: H = [ 12 / (N*(N + 1)) ] * Sum_{j=1}^k (R_j^2 / n_j) - 3*(N + 1)",
                    "Kolmogorov-Smirnov: D = Sup_x | F_n(x) - F_0(x) |"
                ],
                "case_studies": [
                    {"title": "Đánh giá mức độ hài lòng khách hàng sử dụng dịch vụ Mobile Banking", "detail": "Dữ liệu thang đo Likert 5 điểm của 400 khách hàng thuộc 4 nhóm tuổi được phân tích bằng Kruskal-Wallis H-test, khẳng định nhóm tuổi trẻ có mức độ chấp nhận công nghệ vượt trội (H = 28.3, p < 0.001)."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Ước lượng mật độ hạt nhân phi tham số (Kernel Density Estimation - KDE) và lựa chọn độ rộng cửa sổ tối ưu Bandwidth theo Silverman.",
                "Phân tích phương sai đa biến (MANOVA) và phân tích nhân tố khám phá EFA trong nghiên cứu hành vi tài chính người tiêu dùng.",
                "Đề tài Luận án Tiến sĩ: Đánh giá phi tham số tính hiệu quả kỹ thuật của hệ thống bệnh viện công lập Việt Nam bằng phương pháp DEA Bootstrap."
            ]
        },
        review_questions=[
            "1. Tại sao không thể thực hiện nhiều phép kiểm định t-test từng cặp thay cho việc thực hiện một phép kiểm định ANOVA?",
            "2. Nêu các giả thiết cần kiểm tra trước khi chạy One-way ANOVA (tính chuẩn, tính độc lập, tính thuần nhất phương sai).",
            "3. Viết code Python thực hiện One-way ANOVA và vẽ biểu đồ Boxplot trực quan hóa sự khác biệt giữa các nhóm."
        ]
    )
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\07_Toán, Thống kê, Kinh tế lượng & Tin học\[NEU] Xác suất và Thống kê toán - PGS.TS Nguyễn Cao Văn (NXB ĐHKTQD)"
    pdf_name = "[NEU] [Giáo trình Toàn văn] Xác suất và Thống kê toán - PGS.TS Nguyễn Cao Văn (NXB ĐHKTQD).pdf"
    p_path = os.path.join(out_dir, pdf_name)
    pages, sz = b.save(p_path)
    print(f"-> Book 2 Completed: {pages} pages, {sz:.2f} MB saved at: {p_path}")
    return {"id": 2, "title": b.title, "pages": pages, "size_mb": sz, "path": p_path}

def build_book_3():
    print("Building Book 3: Nguyên lý Thống kê kinh tế...")
    b = NEUTextbookBuilder(
        title="Nguyên lý Thống kê kinh tế",
        subject_code="THO101",
        faculty="Thống kê",
        authors="PGS.TS Trần Ngọc Phác (Chủ biên) - PGS.TS Trần Thị Kim Thu",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN LẦN THỨ 9 CÓ BỔ SUNG CHUYÊN ĐỀ TIẾN SĨ"
    )
    b.build_cover()
    
    toc = [
        {"chapter_num": "1", "chapter_title": "Bản chất, Đối tượng và Phương pháp luận Thống kê Kinh tế", "topics": ["Khái niệm và đối tượng nghiên cứu", "Các giai đoạn nghiên cứu thống kê", "Điều tra thống kê & Thu thập dữ liệu", "Phân tổ thống kê & Trực quan hóa"]},
        {"chapter_num": "2", "chapter_title": "Các Mức độ của Hiện tượng Kinh tế Xã hội", "topics": ["Số tuyệt đối trong thống kê", "Số tương đối: Kế hoạch, kết cấu, cường độ, so sánh", "Nguyên tắc sử dụng số tuyệt đối và số tương đối"]},
        {"chapter_num": "3", "chapter_title": "Các Tham số Đặc trưng Đo lường Mức độ Tập trung và Biến thiên", "topics": ["Số bình quân: Số học, điều hòa, nhân", "Trung vị (Median) và Mốt (Mode)", "Độ biến thiên: Khoảng biến thiên, Phương sai, Độ lệch chuẩn, Hệ số biến thiên (CV)"]},
        {"chapter_num": "4", "chapter_title": "Dãy số Thời gian và Phân tích Động thái Phát triển", "topics": ["Khái niệm và phân loại dãy số thời gian", "Các chỉ tiêu phân tích động thái: Lượng tăng giảm tuyệt đối, Tốc độ phát triển, Tốc độ tăng", "Phương pháp xác định xu hướng biến động: Trung bình trượt, Hàm xu thế"]},
        {"chapter_num": "5", "chapter_title": "Phương pháp Chỉ số trong Phân tích Kinh tế", "topics": ["Khái niệm và phân loại chỉ số", "Chỉ số tổng hợp giá cả: Laspeyres, Paasche, Fisher", "Chỉ số lượng hàng hóa", "Hệ thống chỉ số phân tích biến động tổng doanh thu và tổng chi phí"]},
        {"chapter_num": "6", "chapter_title": "Thống kê Mối liên hệ và Dự báo Thống kê Ngắn hạn", "topics": ["Phân tích phân tổ kết hợp", "Hệ số tương quan hạng Spearman", "Dự báo ngoại suy hàm xu thế", "Mô hình san bằng mũ Holt-Winters"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Bản chất, Đối tượng và Phương pháp luận Thống kê Kinh tế",
        introduction="Thống kê kinh tế nghiên cứu mặt lượng trong mối liên hệ mật thiết với mặt chất của các hiện tượng kinh tế số lớn trong điều kiện thời gian và không gian cụ thể.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Đối tượng và Các giai đoạn nghiên cứu thống kê",
                "content": "Đối tượng của thống kê học là các hiện tượng kinh tế xã hội số lớn. Quy trình nghiên cứu gồm 3 giai đoạn hữu cơ: (1) Điều tra thống kê (thu thập thông tin ban đầu); (2) Tổng hợp thống kê (phân tổ, kiểm tra, tính toán các chỉ tiêu tổng hợp); (3) Phân tích và dự đoán thống kê.\n\nTổng thể thống kê là tập hợp các đơn vị mang dấu hiệu cần nghiên cứu. Mẫu thống kê là tập hợp con đại diện được chọn ra từ tổng thể.",
                "formulas": [
                    "Quy trinh: Thu thap du lieu -> Tong hop phan to -> Phan tich mo hinh",
                    "Kich thuoc tong the N; Kich thuoc mau n (n < N)",
                    "Dau hieu nghien cuu: Dau hieu so luong (Dinh luong) va Dau hieu thuoc tinh (Dinh tinh)"
                ],
                "case_studies": [
                    {"title": "Tổng điều tra kinh tế quốc gia của Tổng cục Thống kê Việt Nam", "detail": "Cuộc tổng điều tra thu thập dữ liệu toàn diện của gần 6 triệu đơn vị kinh tế (doanh nghiệp, HTX, hộ kinh doanh cá thể) phục vụ tính toán các chỉ tiêu vĩ mô SNA."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Phương pháp Phân tổ Thống kê",
                "content": "Phân tổ thống kê là việc phân chia tổng thể thành các tổ có tính chất đồng nhất nội bộ dựa trên tiêu thức phân tổ nhất định. Phân tổ có khoảng cách tổ áp dụng cho tiêu thức số lượng có biến thiên liên tục.\n\nCông thức Sturges xác định số tổ tối ưu k = 1 + 3.322 * log10(N), từ đó xác định khoảng cách tổ h = (Xmax - Xmin) / k.",
                "formulas": [
                    "Cong thuc Sturges: k = 1 + 3.322 * log10(N)",
                    "Khoang cach to: h = ( X_max - X_min ) / k",
                    "Gioi han to: [ X_duoi , X_tren ) voi X_tren = X_duoi + h"
                ],
                "case_studies": [
                    {"title": "Phân tổ doanh nghiệp Việt Nam theo quy mô vốn điều lệ", "detail": "Phân chia doanh nghiệp thành 4 nhóm theo Nghị định 80/2021/NĐ-CP: Siêu nhỏ, Nhỏ, Vừa và Lớn để áp dụng các chính sách miễn giảm thuế và hỗ trợ tín dụng ưu đãi."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp thiết kế mẫu phức hợp (Complex Survey Sampling): Phân tầng đa giai đoạn (Stratified Multi-stage) và tính toán sai số chọn mẫu chuẩn.",
                "Kỹ thuật xử lý số liệu khuyết (Missing Data Imputation) trong khảo sát mức sống hộ gia đình VHLSS.",
                "Đề tài Luận án Tiến sĩ: Khảo sát kinh tế ngầm và khu vực phi chính thức tại Việt Nam bằng phương pháp thống kê chỉ báo tiền mặt (Currency Demand Approach)."
            ]
        },
        review_questions=[
            "1. Phân biệt sai số ngẫu nhiên do chọn mẫu và sai số phi chọn mẫu (Non-sampling error).",
            "2. Trình bày các nguyên tắc cơ bản khi lựa chọn tiêu thức phân tổ thống kê kinh tế.",
            "3. Viết code Python sử dụng pandas.cut để phân tổ dữ liệu doanh nghiệp và vẽ biểu đồ tần số Histogram."
        ]
    )

    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Các Mức độ của Hiện tượng Kinh tế Xã hội",
        introduction="Số tuyệt đối và số tương đối là hai hình thức biểu hiện định lượng căn bản nhất của các chỉ tiêu kinh tế, phản ánh quy mô tổng thể và quan hệ so sánh.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Số tuyệt đối trong thống kê",
                "content": "Số tuyệt đối phản ánh quy mô, khối lượng của hiện tượng kinh tế trong điều kiện không gian và thời gian cụ thể (ví dụ: Tổng sản phẩm trong nước GDP năm 2024 đạt 470 tỷ USD). \n\nSố tuyệt đối gồm hai loại: Số tuyệt đối thời kỳ (tích lũy qua khoảng thời gian, có thể cộng gộp) và Số tuyệt đối thời điểm (phản ánh trạng thái tại một thời điểm nhất định, không thể cộng gộp theo thời gian).",
                "formulas": [
                    "So tuyet doi thoi ky: Co the cong don theo thoi gian (VD: Doanh thu thang 1 + thang 2)",
                    "So tuyet doi thoi diem: Khong the cong don truc tiep (VD: Tong tai san ngay 31/12)",
                    "Don vi do: Don vi tu nhien, Don vi thoi gian lao dong, Don vi tien te"
                ],
                "case_studies": [
                    {"title": "Thống kê kim ngạch xuất nhập khẩu hàng hóa Việt Nam", "detail": "Tổng kim ngạch xuất nhập khẩu năm 2024 vượt 780 tỷ USD là chỉ tiêu số tuyệt đối thời kỳ, khẳng định vị thế mở cửa sâu rộng của nền kinh tế."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Các loại số tương đối trong thống kê kinh tế",
                "content": "Số tương đối là kết quả so sánh giữa hai số tuyệt đối, biểu hiện quan hệ tỷ lệ giữa các hiện tượng kinh tế. Hệ thống số tương đối gồm 5 loại chính:\n1. Số tương đối kế hoạch (Nhiệm vụ kế hoạch và Thực hiện kế hoạch).\n2. Số tương đối kết cấu (Tỷ trọng từng bộ phận trong tổng thể).\n3. Số tương đối cường độ (Mức độ phổ biến của hiện tượng, ví dụ: GDP bình quân đầu người, Mật độ dân số).\n4. Số tương đối không gian (So sánh giữa 2 đơn vị hoặc 2 quốc gia).\n5. Số tương đối động thái (Tốc độ phát triển qua các kỳ).",
                "formulas": [
                    "So tuong doi thuc hien ke hoach: K_th = ( Y_thuc_te / Y_ke_hoach ) * 100%",
                    "So tuong doi ket cau: d_i = ( y_i / Sum y_i ) * 100%  (Sum d_i = 100%)",
                    "So tuong doi cuong do: I_cd = Y_A / Y_B (don vi do kep, VD: USD/nguoi)",
                    "Moi quan he: K_th = K_nv * K_dt (voi K_dt la he so dong thai)"
                ],
                "case_studies": [
                    {"title": "Phân tích cơ cấu GDP Việt Nam theo khu vực kinh tế", "detail": "Số tương đối kết cấu năm 2024: Nông - Lâm - Thủy sản chiếm 11.8%, Công nghiệp - Xây dựng chiếm 38.2%, Dịch vụ chiếm 42.5%, Thuế sản phẩm trừ trợ cấp 7.5%."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp chuỗi số tương đối điều chỉnh theo mùa (Seasonal Adjustment) bằng thuật toán X-13ARIMA-SEATS của Cục Thống kê Hoa Kỳ.",
                "Chỉ số Tổng hợp Phát triển Con người (HDI) và các chỉ số đa chiều trong phân tích kinh tế phát triển.",
                "Đề tài Luận án Tiến sĩ: Đo lường nghèo đa chiều (Multidimensional Poverty Index - MPI) tại các vùng dân tộc thiểu số Việt Nam."
            ]
        },
        review_questions=[
            "1. Phân biệt bản chất số tương đối kết cấu và số tương đối cường độ. Cho ví dụ thực tế.",
            "2. Chứng minh mối quan hệ giữa số tương đối nhiệm vụ kế hoạch, số tương đối thực hiện kế hoạch và số tương đối động thái.",
            "3. Viết script Python tính toán cơ cấu ngành và vẽ biểu đồ Donut Chart trực quan."
        ]
    )

    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Các Tham số Đặc trưng Đo lường Mức độ Tập trung và Biến thiên",
        introduction="Chương 3 trang bị hệ thống các chỉ tiêu phản ánh xu hướng tập trung (bình quân, trung vị, mốt) và mức độ phân tán biến thiên của dữ liệu thống kê kinh tế.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Các tham số đo lường mức độ tập trung",
                "content": "Số bình quân số học phản ánh mức độ đại biểu của tiêu thức nghiên cứu trên một đơn vị tổng thể. Khi các quan sát có tần số khác nhau, ta sử dụng số bình quân gia quyền. Số bình quân điều hòa được dùng khi biết giá trị tiêu thức và tổng lượng mang tiêu thức.\n\nTrung vị (Median - Me) là giá trị chia tổng thể thành hai phần bằng nhau, không bị ảnh hưởng bởi giá trị ngoại lai cực đoan. Mốt (Mode - Mo) là giá trị có tần số xuất hiện lớn nhất trong tổng thể.",
                "formulas": [
                    "So binh quan gia quyen: X_bar = ( Sum_{i=1}^k x_i * f_i ) / ( Sum_{i=1}^k f_i )",
                    "So binh quan dieu hoa: X_bar_H = ( Sum M_i ) / ( Sum (M_i / x_i) )",
                    "Trung vi to chua Me: Me = X_Me + h * [ (Sum f/2 - S_{Me-1}) / f_Me ]",
                    "Mot to chua Mo: Mo = X_Mo + h * [ (f_Mo - f_{Mo-1}) / ( (f_Mo - f_{Mo-1}) + (f_Mo - f_{Mo+1}) ) ]"
                ],
                "case_studies": [
                    {"title": "Phân tích giá bán căn hộ chung cư tại Hà Nội năm 2024", "detail": "Do có một số dự án hạng sang giá cực cao kéo bình quân lên 65 triệu VNĐ/m2, giá trung vị Me = 52 triệu VNĐ/m2 phản ánh trung thực hơn khả năng chi trả của đại đa số người dân."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Các tham số đo lường mức độ biến thiên",
                "content": "Để đánh giá tính đại diện của số bình quân và mức độ rủi ro, cần khảo sát độ biến thiên. Khoảng biến thiên R = Xmax - Xmin phản ánh phạm vi dao động thô.\n\nPhương sai sigma^2 và độ lệch chuẩn sigma đo lường độ phân tán quanh giá trị trung bình. Hệ số biến thiên CV = (sigma / X_bar) * 100% là đại lượng phi thứ nguyên, cho phép so sánh độ đồng đều giữa các hiện tượng có đơn vị đo khác nhau hoặc quy mô trung bình chênh lệch lớn.",
                "formulas": [
                    "Khoang bien thien: R = X_max - X_min",
                    "Phuong sai gia quyen: s^2 = [ Sum f_i * (x_i - X_bar)^2 ] / [ (Sum f_i) - 1 ]",
                    "Do lech chuan: s = sqrt( s^2 )",
                    "He so bien thien: CV = ( s / X_bar ) * 100%  (CV < 30%: Tong the dong deu)"
                ],
                "case_studies": [
                    {"title": "Đánh giá mức độ đồng đều trong phân phối lương nhân viên ngân hàng", "detail": "Ngân hàng A có lương bình quân 25 triệu, s = 5 triệu (CV = 20%). Ngân hàng B có lương bình quân 30 triệu, s = 15 triệu (CV = 50%). Ngân hàng A có cơ cấu lương đồng đều và công bằng hơn."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Đo lường bất bình đẳng kinh tế: Đường cong Lorenz và Hệ số Gini phân rã theo nguồn thu nhập (Gini Decomposition by Income Source).",
                "Chỉ số Theil Entropy đo lường bất bình đẳng giữa các vùng và trong nội bộ vùng.",
                "Đề tài Luận án Tiến sĩ: Tác động của chuyển đổi số doanh nghiệp đến khoảng cách tiền lương kỹ năng tại Việt Nam bằng hồi quy phân vị RIF (Recentered Influence Function)."
            ]
        },
        review_questions=[
            "1. So sánh ưu nhược điểm của số bình quân số học, trung vị và mốt. Khi nào nên dùng trung vị thay cho số bình quân?",
            "2. Ý nghĩa của hệ số biến thiên CV trong thẩm định dự án đầu tư tài chính.",
            "3. Viết code Python tính toán đầy đủ các tham số mô tả (mean, median, mode, variance, std, IQR, CV) của một mảng dữ liệu."
        ]
    )

    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Dãy số Thời gian và Phân tích Động thái Phát triển",
        introduction="Dãy số thời gian ghi nhận các mức độ của hiện tượng kinh tế theo thứ tự thời gian, cho phép phân tích nhịp điệu phát triển và dự báo các xu thế tương lai.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Các chỉ tiêu phân tích dãy số thời gian",
                "content": "Dãy số thời gian y1, y2, ..., yn gồm mức độ tuyệt đối từng kỳ. Các chỉ tiêu phân tích động thái bao gồm: \n1. Lượng tăng (giảm) tuyệt đối liên hoàn Delta_i = yi - y_{i-1} và định gốc Delta_{1,i} = yi - y1.\n2. Tốc độ phát triển liên hoàn ti = yi / y_{i-1} và định gốc Ti = yi / y1.\n3. Tốc độ tăng liên hoàn ai = ti - 1 và định gốc Ai = Ti - 1.\n4. Giá trị tuyệt đối của 1% tăng trưởng = Delta_i / (ai * 100) = y_{i-1} / 100.",
                "formulas": [
                    "Luong tang giam: Delta_i = y_i - y_{i-1};  Delta_tong = y_n - y_1 = Sum Delta_i",
                    "Toc do phat trien: t_i = y_i / y_{i-1};  T_n = y_n / y_1 = Product t_i",
                    "Toc do tang: a_i = t_i - 1  (hoac a_i% = (t_i - 1)*100%)",
                    "Gia tri tuyet doi 1% tang: g_i = y_{i-1} / 100",
                    "Toc do phat trien binh quan: t_bar = ( y_n / y_1 )^( 1 / (n - 1) )"
                ],
                "case_studies": [
                    {"title": "Phân tích tốc độ tăng trưởng GDP Việt Nam giai đoạn 2015 - 2024", "detail": "Tính toán tốc độ phát triển bình quân hàng năm đạt 6.35%, xác định giá trị tuyệt đối của 1% tăng trưởng GDP năm 2024 tương đương 4.3 tỷ USD."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Phương pháp biểu hiện xu thế biến động",
                "content": "Một dãy số thời gian kinh tế thường cấu thành từ 4 thành phần: Xu thế dài hạn (Trend - T), Biến động chu kỳ (Cycle - C), Biến động thời vụ (Seasonal - S), và Sai số ngẫu nhiên (Irregular - I).\n\nPhương pháp trung bình trượt (Moving Average) làm triệt tiêu các dao động ngẫu nhiên ngắn hạn. Phương pháp hồi quy hàm xu thế tuyến tính y_hat_t = a + b*t hoặc hàm mũ xác định quỹ đạo dài hạn của hiện tượng.",
                "formulas": [
                    "Mo hinh nhan: Y_t = T_t * S_t * C_t * I_t",
                    "Mo hinh cong: Y_t = T_t + S_t + C_t + I_t",
                    "Trung binh truot bac 3: MA_3(t) = ( y_{t-1} + y_t + y_{t+1} ) / 3",
                    "Ham xu the tuyen tinh: Min Sum ( y_t - (a + b*t) )^2"
                ],
                "case_studies": [
                    {"title": "Phân tích biến động thời vụ của ngành Du lịch Việt Nam", "detail": "Tách yếu tố mùa vụ lượng khách quốc tế đến Việt Nam cho thấy chỉ số mùa vụ quý 1 và quý 4 đạt 135% (mùa cao điểm), quý 2 và 3 chỉ đạt 75%."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp lọc Hodrick-Prescott (HP Filter) phân rã chu kỳ kinh doanh và sản lượng tiềm năng (Potential GDP).",
                "Mô hình chuỗi thời gian phân rã nhân tố cấu trúc (Structural Time Series Models) với bộ lọc Kalman Filter.",
                "Đề tài Luận án Tiến sĩ: Đo lường khoảng cách sản lượng (Output Gap) và áp lực lạm phát cầu kéo tại Việt Nam bằng phương pháp lọc đa biến Multivariate Filter."
            ]
        },
        review_questions=[
            "1. Chứng minh tích các tốc độ phát triển liên hoàn bằng tốc độ phát triển định gốc.",
            "2. Tại sao giá trị tuyệt đối của 1% tăng trưởng luôn bằng 1/100 mức độ kỳ gốc?",
            "3. Viết script Python sử dụng statsmodels.tsa.seasonal_decompose để phân rã chuỗi thời gian GDP theo mô hình nhân."
        ]
    )

    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Phương pháp Chỉ số trong Phân tích Kinh tế",
        introduction="Phương pháp chỉ số là công cụ đặc thù của thống kê kinh tế, cho phép tổng hợp các phần tử không thể cộng trực tiếp và phân tích biến động các nhân tố ảnh hưởng.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Chỉ số tổng hợp Giá cả và Lượng hàng hóa",
                "content": "Để tổng hợp biến động giá của nhiều mặt hàng khác nhau, cần sử dụng quyền số là khối lượng tiêu thụ hàng hóa. Chỉ số giá Laspeyres sử dụng quyền số kỳ gốc (q0), có xu hướng đánh giá cao mức tăng chi phí sinh hoạt do bỏ qua hiệu ứng thay thế.\n\nChỉ số giá Paasche sử dụng quyền số kỳ báo cáo (q1). Chỉ số giá Fisher là trung bình nhân của Laspeyres và Paasche, thỏa mãn các kiểm định nghịch đảo thời gian và nhân tử.",
                "formulas": [
                    "Chi so gia Laspeyres: I_p^L = ( Sum p_1 * q_0 ) / ( Sum p_0 * q_0 )",
                    "Chi so gia Paasche: I_p^P = ( Sum p_1 * q_1 ) / ( Sum p_0 * q_1 )",
                    "Chi so gia Fisher: I_p^F = sqrt( I_p^L * I_p^P )",
                    "Chi so luong Laspeyres: I_q^L = ( Sum p_0 * q_1 ) / ( Sum p_0 * q_0 )"
                ],
                "case_studies": [
                    {"title": "Phương pháp tính Chỉ số giá tiêu dùng CPI của Việt Nam", "detail": "Tổng cục Thống kê tính CPI theo công thức Laspeyres điều chỉnh với danh mục giỏ hàng gồm 752 mặt hàng đại diện, quyền số được cập nhật 5 năm một lần dựa trên điều tra mức sống."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Hệ thống chỉ số phân tích nhân tố biến động",
                "content": "Tổng doanh thu M = Sum(p * q) biến động do tác động đồng thời của biến động giá cả và biến động khối lượng sản phẩm tiêu thụ. Hệ thống chỉ số liên kết phân rã:\nIpq = Ip * Iq <=> Sum(p1*q1) / Sum(p0*q0) = [ Sum(p1*q1) / Sum(p0*q1) ] * [ Sum(p0*q1) / Sum(p0*q0) ].\n\nPhân tích biến động tuyệt đối: Delta_M = Delta_Mp + Delta_Mq, chỉ rõ phần doanh thu tăng/giảm do yếu tố giá và do yếu tố sản lượng.",
                "formulas": [
                    "He thong chi so doanh thu: I_pq = I_p^P * I_q^L",
                    "Phan bien dong tuyet doi: Sum p_1*q_1 - Sum p_0*q_0 = ( Sum p_1*q_1 - Sum p_0*q_1 ) + ( Sum p_0*q_1 - Sum p_0*q_0 )",
                    "Delta_M = Delta_M(p) + Delta_M(q)",
                    "He thong chi so chi phi: I_zq = I_z^P * I_q^L (Z: gia thanh don vi)"
                ],
                "case_studies": [
                    {"title": "Phân tích biến động tổng doanh thu của Tập đoàn Vingroup", "detail": "Doanh thu năm báo cáo tăng 24.000 tỷ VNĐ. Phân tích hệ thống chỉ số chỉ rõ: 18.500 tỷ VNĐ do sản lượng bàn giao xe điện VinFast tăng (Iq = 1.35) và 5.500 tỷ VNĐ do giá bán trung bình tăng (Ip = 1.08)."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Chỉ số chuỗi nối vòng (Chained Price Index) và Chỉ số Törnqvist trong Hệ thống Tài khoản Quốc gia SNA 2008.",
                "Phương pháp Hedonic Pricing điều chỉnh biến động giá theo thay đổi chất lượng sản phẩm công nghệ.",
                "Đề tài Luận án Tiến sĩ: Khảo sát sai số đo lường lạm phát (CPI Measurement Bias) tại Việt Nam do hiệu ứng dịch chuyển điểm bán lẻ và sản phẩm mới."
            ]
        },
        review_questions=[
            "1. Tại sao chỉ số giá Laspeyres luôn có xu hướng cao hơn chỉ số giá Paasche trong điều kiện thực tế?",
            "2. Thiết lập hệ thống chỉ số phân tích biến động của Quỹ tiền lương doanh nghiệp theo 2 nhân tố: Số lượng lao động và Tiền lương bình quân.",
            "3. Viết script Python tính toán chỉ số giá Laspeyres, Paasche, Fisher và kiểm tra phương trình hệ thống chỉ số."
        ]
    )

    # Chapter 6
    b.add_chapter(
        chap_num="6",
        chap_title="Thống kê Mối liên hệ và Dự báo Thống kê Ngắn hạn",
        introduction="Chương 6 nghiên cứu mối liên hệ phi hàm số giữa các hiện tượng kinh tế và các phương pháp dự báo thống kê ngắn hạn thông dụng trong thực tiễn điều hành doanh nghiệp.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phương pháp phân tích mối liên hệ tương quan",
                "content": "Trong kinh tế học, mối liên hệ giữa các hiện tượng chủ yếu là mối liên hệ tương quan ngẫu nhiên. Phương pháp phân tổ kết hợp phân chia tổng thể theo hai tiêu thức để nhận diện mối quan hệ phụ thuộc.\n\nHệ số tương quan hạng Spearman rs đo lường mức độ liên kết giữa hai tiêu thức thứ bậc dựa trên sai phân thứ hạng d = R(x) - R(y). Hệ số rs nhận giá trị từ -1 đến +1 mà không đòi hỏi giả thiết về phân phối chuẩn của các biến số.",
                "formulas": [
                    "He so tuong quan hang Spearman: r_s = 1 - [ 6 * Sum (d_i^2) ] / [ n * (n^2 - 1) ]",
                    "Sai phan thu hang: d_i = Rank(X_i) - Rank(Y_i)",
                    "Kiem dinh y nghia thong ke: t = r_s * sqrt( (n - 2) / (1 - r_s^2) ) ~ t_{n-2}"
                ],
                "case_studies": [
                    {"title": "Tương quan giữa xếp hạng tín nhiệm nội bộ và tỷ lệ thu hồi nợ", "detail": "Khảo sát 20 chi nhánh ngân hàng, hệ số tương quan hạng Spearman rs = 0.82 (p < 0.001), khẳng định các chi nhánh tuân thủ quy trình xếp hạng cao có tỷ lệ thu hồi nợ vượt trội."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Phương pháp Dự báo Thống kê Ngắn hạn",
                "content": "Dự báo ngoại suy hàm xu thế dựa trên giả thiết quy luật vận động quá khứ tiếp tục duy trì trong tương lai gần. Phương pháp san bằng mũ đơn giản (Simple Exponential Smoothing - SES) gán trọng số giảm dần theo hàm mũ cho các quan sát quá khứ.\n\nPhương pháp Holt-Winters mở rộng san bằng mũ cho chuỗi có xu thế tuyến tính và có tính chất mùa vụ, cho phép dự báo chính xác nhu cầu tiêu thụ hàng hóa từng tháng/quý.",
                "formulas": [
                    "San bang mu don: S_t = alpha * Y_t + (1 - alpha) * S_{t-1}  (0 < alpha < 1)",
                    "Du bao ky t+1: Y_hat_{t+1} = S_t",
                    "Holt-Winters co xu the: L_t = alpha*Y_t + (1-alpha)*(L_{t-1} + b_{t-1})",
                    "b_t = beta*(L_t - L_{t-1}) + (1-beta)*b_{t-1}"
                ],
                "case_studies": [
                    {"title": "Dự báo doanh số bán lẻ mùa Tết của hệ thống siêu thị WinMart", "detail": "Áp dụng mô hình Holt-Winters mùa vụ nhân trên chuỗi doanh số 36 tháng, dự báo doanh số Tết Nguyên đán đạt 1.450 tỷ VNĐ với sai số MAPE dưới 4.2%."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp Nowcasting sử dụng dữ liệu tần suất cao và mô hình nhân tố động (Dynamic Factor Models - DFM).",
                "Đánh giá độ chính xác dự báo ngoài mẫu: Thống kê Theil's U và kiểm định Diebold-Mariano so sánh hiệu năng các mô hình dự báo cạnh tranh.",
                "Đề tài Luận án Tiến sĩ: Ứng dụng Google Trends và dữ liệu thanh toán số trong dự báo tức thời sức mua bán lẻ tại Việt Nam."
            ]
        },
        review_questions=[
            "1. Phân biệt liên hệ hàm số và liên hệ tương quan trong kinh tế học.",
            "2. Trình bày cách lựa chọn tham số san bằng alpha trong mô hình san bằng mũ đơn.",
            "3. Viết code Python sử dụng statsmodels.tsa.holtwinters.ExponentialSmoothing để dự báo doanh số 4 quý tiếp theo."
        ]
    )
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\07_Toán, Thống kê, Kinh tế lượng & Tin học\[NEU] Nguyên lý Thống kê kinh tế - PGS.TS Trần Ngọc Phác (NXB ĐHKTQD)"
    pdf_name = "[NEU] [Giáo trình Toàn văn] Nguyên lý Thống kê kinh tế - PGS.TS Trần Ngọc Phác (NXB ĐHKTQD).pdf"
    p_path = os.path.join(out_dir, pdf_name)
    pages, sz = b.save(p_path)
    print(f"-> Book 3 Completed: {pages} pages, {sz:.2f} MB saved at: {p_path}")
    return {"id": 3, "title": b.title, "pages": pages, "size_mb": sz, "path": p_path}

def build_book_4():
    print("Building Book 4: Thống kê doanh nghiệp...")
    b = NEUTextbookBuilder(
        title="Thống kê doanh nghiệp",
        subject_code="THO202",
        faculty="Thống kê",
        authors="PGS.TS Phan Công Nghĩa (Chủ biên) - PGS.TS Trần Ngọc Phác",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN LẦN THỨ 8 CÓ BỔ SUNG CHUYÊN ĐỀ TIẾN SĨ"
    )
    b.build_cover()
    
    toc = [
        {"chapter_num": "1", "chapter_title": "Đối tượng, Nhiệm vụ và Hệ thống Chỉ tiêu Thống kê Doanh nghiệp", "topics": ["Bản chất và phạm vi thống kê doanh nghiệp", "Chu trình sản xuất kinh doanh", "Hệ thống chỉ tiêu kết quả hoạt động doanh nghiệp"]},
        {"chapter_num": "2", "chapter_title": "Thống kê Kết quả Hoạt động Sản xuất Kinh doanh", "topics": ["Giá trị sản xuất (Gross Output - GO)", "Giá trị gia tăng (Value Added - VA)", "Tổng doanh thu và sản lượng hiện vật", "Đánh giá mức độ đồng bộ và chất lượng sản phẩm"]},
        {"chapter_num": "3", "chapter_title": "Thống kê Lao động và Tiền lương trong Doanh nghiệp", "topics": ["Thống kê số lượng và thời gian lao động", "Năng suất lao động: Phương pháp đo lường và hệ thống chỉ số", "Thống kê quỹ tiền lương và tiền lương bình quân"]},
        {"chapter_num": "4", "chapter_title": "Thống kê Tài sản Cố định và Năng lực Công nghệ", "topics": ["Nguyên giá, giá trị hao mòn và giá trị còn lại", "Các chỉ tiêu phản ánh tình trạng tài sản cố định", "Hiệu suất sử dụng tài sản cố định", "Suất hao phí tài sản cố định"]},
        {"chapter_num": "5", "chapter_title": "Thống kê Chi phí Sản xuất, Giá thành và Lợi nhuận", "topics": ["Phân loại chi phí sản xuất", "Thống kê biến động giá thành sản phẩm", "Phân tích hòa vốn (Break-even Analysis)", "Thống kê kết quả tài chính và lợi nhuận"]},
        {"chapter_num": "6", "chapter_title": "Thống kê Hiệu quả Kinh doanh và Năng lực Cạnh tranh", "topics": ["Các chỉ số khả năng sinh lời ROA, ROE, ROS", "Năng suất tổng nhân tố (TFP) cấp doanh nghiệp", "Mô hình đo lường hiệu quả kỹ thuật"]}
    ]
    b.add_table_of_contents(toc)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Đối tượng, Nhiệm vụ và Hệ thống Chỉ tiêu Thống kê Doanh nghiệp",
        introduction="Thống kê doanh nghiệp cung cấp công cụ thu thập, tổng hợp và phân tích toàn diện mọi khía cạnh của chu trình sản xuất kinh doanh từ các yếu tố đầu vào, quá trình vận hành đến kết quả đầu ra và hiệu quả tài chính.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Đối tượng và Nhiệm vụ của Thống kê Doanh nghiệp",
                "content": "Thống kê doanh nghiệp nghiên cứu mặt lượng trong mối liên hệ với mặt chất của các hiện tượng và quá trình kinh tế diễn ra trong nội bộ doanh nghiệp. Đơn vị quan sát cơ bản là doanh nghiệp độc lập theo luật pháp hoặc các đơn vị cơ sở (chi nhánh, nhà máy, phân xưởng).\n\nNhiệm vụ trọng tâm gồm: Đánh giá tình hình thực hiện kế hoạch sản xuất kinh doanh; Phân tích các nhân tố ảnh hưởng đến năng suất, chi phí và lợi nhuận; Cung cấp luận cứ định lượng cho việc hoạch định chiến lược kinh doanh của ban giám đốc.",
                "formulas": [
                    "Chu trinh san xuat: Yeu to dau vao (Von, Lao dong, Cong nghe) -> Qua trinh SX -> Dau ra (San pham, Doanh thu, Loi nhuan)",
                    "Phan loai doanh nghiep: Theo nganh VSIC, Theo hinh thuc so huu, Theo quy mo von/lao dong"
                ],
                "case_studies": [
                    {"title": "Hệ thống báo cáo quản trị định lượng của Tập đoàn Dầu khí Việt Nam (PVN)", "detail": "Thiết lập hệ thống chỉ tiêu thống kê thời gian thực (Real-time KPI) giám sát sản lượng khai thác, tiêu hao năng lượng và giá thành từng mỏ dầu khí."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Hệ thống chỉ tiêu Thống kê Doanh nghiệp",
                "content": "Hệ thống chỉ tiêu thống kê doanh nghiệp gồm 5 phân nhóm chính: (1) Nhóm chỉ tiêu phản ánh các yếu tố đầu vào (vốn, lao động, TSCĐ, nguyên vật liệu); (2) Nhóm chỉ tiêu phản ánh kết quả sản xuất (sản lượng hiện vật, GO, VA, doanh thu); (3) Nhóm chỉ tiêu chi phí và giá thành; (4) Nhóm chỉ tiêu tài chính và lợi nhuận; (5) Nhóm chỉ tiêu hiệu quả tổng hợp (TFP, ROA, ROE).",
                "formulas": [
                    "He thong chi tieu = f( Dau vao, Tien trinh, Dau ra, Hieu qua, Tac dong xa hoi)",
                    "Chi tieu tuyet doi (Quy mo) song hanh voi Chi tieu tuong doi (Hieu suat)"
                ],
                "case_studies": [
                    {"title": "Áp dụng khung thẻ điểm cân bằng (Balanced Scorecard - BSC)", "detail": "Công ty Cổ phần Sữa Việt Nam (Vinamilk) tích hợp hệ thống chỉ tiêu thống kê sản xuất kinh doanh vào 4 khía cạnh: Tài chính, Khách hàng, Quy trình nội bộ và Học hỏi - Phát triển."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp phân tích kinh tế lượng doanh nghiệp vi mô (Microeconometrics for Firm-level Data): Xử lý tính không quan sát được (Unobserved Heterogeneity) và thiên lệch lựa chọn (Selection Bias).",
                "Tác động của đầu tư R&D và đổi mới sáng tạo đến năng suất doanh nghiệp bằng mô hình Crepon-Duguet-Mairesse (CDM).",
                "Đề tài Luận án Tiến sĩ: Khảo sát mối quan hệ giữa thực hành quản trị ESG và hiệu quả tài chính của các doanh nghiệp niêm yết tại Việt Nam."
            ]
        },
        review_questions=[
            "1. Phân biệt đơn vị thống kê doanh nghiệp độc lập và đơn vị thể chế cơ sở.",
            "2. Nêu vai trò của phân loại ngành kinh tế chuẩn VSIC trong thống kê doanh nghiệp.",
            "3. Thiết kế bảng cân đối thu thập dữ liệu sản xuất kinh doanh hàng tháng cho một doanh nghiệp may mặc."
        ]
    )

    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Thống kê Kết quả Hoạt động Sản xuất Kinh doanh",
        introduction="Đo lường chính xác kết quả đầu ra là tiền đề để đánh giá quy mô đóng góp của doanh nghiệp cho nền kinh tế và làm cơ sở tính toán năng suất, hiệu quả.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Giá trị Sản xuất (GO) và Giá trị Gia tăng (VA)",
                "content": "Giá trị sản xuất (Gross Output - GO) phản ánh toàn bộ giá trị các sản phẩm vật chất và dịch vụ hữu ích do doanh nghiệp tạo ra trong một thời kỳ nhất định, gồm 4 yếu tố: Doanh thu tiêu thụ sản phẩm chính và phụ; Doanh thu dịch vụ công nghiệp; Chênh lệch sản phẩm dở dang và tồn kho; Giá trị tài sản cố định tự làm.\n\nGiá trị gia tăng (Value Added - VA) phản ánh phần giá trị mới sáng tạo, bằng Giá trị sản xuất trừ đi Chi phí trung gian (Intermediate Consumption - IC): VA = GO - IC.",
                "formulas": [
                    "GO = Doanh thu tieu thu + Chenh lech ton kho + Cong viec co tinh chat cong nghiep + TSCĐ tu lam",
                    "VA = GO - IC  (IC: Chi phi nguyen vat lieu, dien nuoc, dich vu mua ngoai)",
                    "VA thuan (NVA) = VA - Khau hao tai san co dinh (C1)",
                    "Phuong phap phan phoi: VA = Chi phi nhan cong + Thue SX + Khau hao + Loi nhuan truoc thue"
                ],
                "case_studies": [
                    {"title": "Tính toán Giá trị gia tăng của Tập đoàn Dệt may Việt Nam (Vinatex)", "detail": "Năm 2024, tổng GO đạt 42.000 tỷ VNĐ, chi phí trung gian IC là 29.500 tỷ VNĐ (chiếm 70.2%), giá trị gia tăng VA đạt 12.500 tỷ VNĐ, đóng góp quan trọng vào xuất khẩu quốc gia."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Thống kê Sản lượng Hiện vật và Chất lượng Sản phẩm",
                "content": "Sản lượng hiện vật đo lường bằng các đơn vị tự nhiên (tấn, mét, chiếc, kWh). Khi sản phẩm có nhiều quy cách, ta sử dụng phương pháp sản lượng quy chuẩn (quy ước về một sản phẩm chuẩn theo hệ số tương đương).\n\nThống kê chất lượng sản phẩm sử dụng tỷ lệ phế phẩm, hệ số phẩm cấp bình quân và tỷ lệ sản phẩm đạt tiêu chuẩn chất lượng quốc tế (ISO 9001, CE, FDA).",
                "formulas": [
                    "San luong quy chuan: Q_chuan = Sum ( Q_i * k_i )  (k_i: he so quy doi)",
                    "He so quy doi: k_i = Thong so ky thuat i / Thong so ky thuat chuan",
                    "He so pham cap binh quan: K_pc = ( Sum p_i * q_i ) / ( p_1 * Sum q_i )  (p_1: gia sp loai 1)",
                    "Ty le phe pham: d_pp = ( Luong phe pham / Tong san pham ) * 100%"
                ],
                "case_studies": [
                    {"title": "Quy đổi sản lượng xi măng Vicem về xi măng chuẩn PCB40", "detail": "Vicem sản xuất xi măng PCB30, PCB40 và PCB50. Sử dụng cường độ nén 28 ngày làm thông số kỹ thuật để quy chuẩn toàn bộ sản lượng về mác PCB40 phục vụ báo cáo hợp nhất."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp định giá gia tăng (Hedonic Quality Adjustment) trong thống kê sản lượng ngành công nghiệp phần mềm và thiết bị bán dẫn.",
                "Đo lường vị thế doanh nghiệp trong Chuỗi giá trị toàn cầu (Global Value Chains - GVC Participation Index).",
                "Đề tài Luận án Tiến sĩ: Nâng cấp chuỗi giá trị và tỷ lệ nội địa hóa giá trị gia tăng (Domestic Value Added - DVA) của các doanh nghiệp FDI tại Việt Nam."
            ]
        },
        review_questions=[
            "1. Phân biệt phương pháp công xưởng và phương pháp chỉ số khi tính giá trị sản xuất GO.",
            "2. Chứng minh hai phương pháp tính Giá trị gia tăng (phương pháp sản xuất GO - IC và phương pháp phân phối) cho kết quả đồng nhất.",
            "3. Viết code Python tính toán sản lượng quy chuẩn và hệ số phẩm cấp bình quân của một xí nghiệp gạch ốp lát."
        ]
    )

    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Thống kê Lao động và Tiền lương trong Doanh nghiệp",
        introduction="Lao động là nhân tố sản xuất năng động nhất. Thống kê lao động và tiền lương giúp tối ưu hóa sử dụng thời gian làm việc, kích thích năng suất và kiểm soát chi phí nhân sự.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Thống kê Số lượng và Thời gian Lao động",
                "content": "Số lao động bình quân thời kỳ T_bar phản ánh quy mô nhân lực trung bình tham gia sản xuất. Nếu có số liệu hàng ngày, tính bằng bình quân số học giản đơn. Nếu có số liệu cách đều định kỳ đầu tháng, tính bằng bình quân thứ tự (Chronological Mean).\n\nBảng cân đối thời gian lao động theo dõi số ngày - công và giờ - công: Thời gian theo lịch, Thời gian chế độ, Thời gian có mặt, Thời gian làm việc thực tế và Thời gian ngừng việc, vắng mặt lãng phí.",
                "formulas": [
                    "Binh quan thu tu: T_bar = [ 0.5*T1 + T2 + ... + T_{n-1} + 0.5*Tn ] / (n - 1)",
                    "Thoi gian lam viec thuc te = Thoi gian co mat - Thoi gian ngung viec trong ca",
                    "He so su dung thoi gian che do: K_cd = ( Gio lam viec thuc te / Gio che do quy dinh ) * 100%"
                ],
                "case_studies": [
                    {"title": "Cắt giảm thời gian lãng phí theo phương pháp Lean tại Công ty Giày Thượng Đình", "detail": "Bảng cân đối thời gian lao động phát hiện thời gian chờ nguyên liệu chiếm 14.5% tổng giờ công. Tái cấu trúc chuyền may giúp nâng hệ số sử dụng giờ công từ 82% lên 94%."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Thống kê Năng suất Lao động và Hệ thống Chỉ số",
                "content": "Năng suất lao động phản ánh hiệu quả sử dụng lao động, đo lường bằng sản lượng bình quân một lao động tạo ra trong một đơn vị thời gian: W = Q / T hoặc lượng hao phí thời gian để sản xuất một đơn vị sản phẩm: t = T / Q (W = 1/t).\n\nHệ thống chỉ số năng suất lao động phân tích biến động năng suất bình quân của doanh nghiệp đa phân xưởng thành 2 nhân tố: Biến động năng suất lao động bản thân từng phân xưởng và Biến động cơ cấu phân bổ lao động giữa các phân xưởng (chỉ số cấu thành cố định và chỉ số ảnh hưởng kết cấu).",
                "formulas": [
                    "Nang suat lao dong ca the: W = Q / T (gio, ngay, nguoi);  t = T / Q",
                    "Nang suat binh quan: W_bar = Sum (W_i * T_i) / Sum T_i = Sum (W_i * d_Ti)",
                    "He thong chi so cau thanh kha bien: I_W_bar = I_W_cd * I_kc",
                    "I_W_bar = [ Sum W1*d_T1 / Sum W0*d_T0 ] = [ Sum W1*d_T1 / Sum W0*d_T1 ] * [ Sum W0*d_T1 / Sum W0*d_T0 ]"
                ],
                "case_studies": [
                    {"title": "Phân tích nhân tố tăng năng suất lao động tại Công ty May 10", "detail": "Năng suất bình quân toàn công ty tăng 12.8%. Phân tích hệ thống chỉ số chỉ rõ: 10.2% do đổi mới máy may tự động tại các chuyền (chỉ số cấu thành cố định) và 2.6% do chuyển dịch lao động sang sản phẩm cao cấp (ảnh hưởng kết cấu)."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Ước lượng hồi quy hàm tiền lương Mincer có hiệu chỉnh chọn mẫu Heckman Two-step cho lực lượng lao động doanh nghiệp.",
                "Phân tích phân rã khoảng cách tiền lương Oaxaca-Blinder đo lường phân biệt đối xử theo giới trong doanh nghiệp tư nhân.",
                "Đề tài Luận án Tiến sĩ: Đánh giá tác động của lương tối thiểu vùng đến việc làm và chi phí tuân thủ của doanh nghiệp nhỏ và vừa tại Việt Nam bằng Difference-in-Differences."
            ]
        },
        review_questions=[
            "1. Phân biệt năng suất lao động tính bằng đơn vị hiện vật, đơn vị thời gian và đơn vị giá trị.",
            "2. Trình bày ý nghĩa kinh tế của chỉ số cấu thành cố định và chỉ số ảnh hưởng kết cấu trong phân tích năng suất lao động.",
            "3. Viết code Python thực hiện phân rã hệ thống chỉ số năng suất lao động của một công ty gồm 3 nhà máy."
        ]
    )

    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Thống kê Tài sản Cố định và Năng lực Công nghệ",
        introduction="Tài sản cố định (TSCĐ) là cơ sở vật chất kỹ thuật quyết định năng lực sản xuất của doanh nghiệp. Thống kê TSCĐ theo dõi quy mô, tình trạng hao mòn và hiệu suất sử dụng tư bản cố định.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Đánh giá quy mô và Tình trạng Tài sản Cố định",
                "content": "TSCĐ được theo dõi theo 3 giá trị: Nguyên giá (chi phí ban đầu để có TSCĐ ở trạng thái sẵn sàng sử dụng), Giá trị hao mòn lũy kế, và Giá trị còn lại (Nguyên giá - Hao mòn).\n\nCác chỉ tiêu phản ánh hiện trạng kỹ thuật gồm: Hệ số hao mòn (Hao mòn / Nguyên giá); Hệ số còn dùng được (1 - Hệ số hao mòn); Hệ số đổi mới TSCĐ (Nguyên giá TSCĐ mới tăng trong kỳ / Nguyên giá TSCĐ cuối kỳ); Hệ số đào thải TSCĐ.",
                "formulas": [
                    "Gia tri con lai = Nguyen gia - Hao mon luy ke",
                    "He so hao mon: K_hm = ( Hao mon luy ke / Nguyen gia ) * 100%",
                    "He so con dung duoc: K_cdd = 100% - K_hm",
                    "He so doi moi: K_dm = ( TSCĐ moi tang trong ky / TSCĐ cuoi ky ) * 100%",
                    "He so dao thai: K_dt = ( TSCĐ thanh ly giam trong ky / TSCĐ dau ky ) * 100%"
                ],
                "case_studies": [
                    {"title": "Đánh giá mức độ hao mòn đội tàu của Tổng công ty Hàng hải Việt Nam (VIMC)", "detail": "Hệ số hao mòn đội tàu đạt 68.5% (độ tuổi trung bình 18.2 năm), đòi hỏi kế hoạch đầu tư tái thiết đội tàu container thế hệ mới để giảm phát thải xanh."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Thống kê Hiệu suất sử dụng Tài sản Cố định",
                "content": "Hiệu suất sử dụng TSCĐ phản ánh một đồng nguyên giá TSCĐ bình quân tạo ra bao nhiêu đồng sản lượng hoặc doanh thu: H_tscd = GO / TSCĐ_bar (hoặc Doanh thu / TSCĐ_bar).\n\nSuất hao phí TSCĐ là nghịch đảo của hiệu suất: f_tscd = TSCĐ_bar / GO, phản ánh nhu cầu tư bản để tạo 1 đồng sản lượng. Tỷ suất sinh lời TSCĐ = Lợi nhuận trước thuế / TSCĐ_bar. Hệ số trang bị kỹ thuật lao động = TSCĐ_bar / T_bar phản ánh mức độ hiện đại hóa máy móc trên một công nhân.",
                "formulas": [
                    "Hieu suat TSCĐ: H = GO / TSCĐ_bar  (dong san luong / 1 dong nguyen gia)",
                    "Suat hao phi TSCĐ: f = 1 / H = TSCĐ_bar / GO",
                    "Trang bi ky thuat lao dong: C_L = TSCĐ_bar / T_bar",
                    "Moi quan he: W = C_L * H (Nang suat lao dong = Trang bi ky thuat * Hieu suat TSCĐ)"
                ],
                "case_studies": [
                    {"title": "Mối quan hệ giữa trang bị công nghệ và năng suất tại Công ty Ô tô VinFast", "detail": "Hệ thống Robot tự động hóa phân xưởng hàn thân xe nâng hệ số trang bị kỹ thuật lao động lên 3.8 tỷ VNĐ/công nhân, giúp năng suất lao động tăng gấp 4.2 lần so với các dây chuyền lắp ráp thủ công."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp kiểm kê vĩnh viễn (Perpetual Inventory Method - PIM) ước lượng trữ lượng vốn thực tế (Real Capital Stock) cấp doanh nghiệp.",
                "Mô hình đầu tư doanh nghiệp Q-Tobin và các ma sát tài chính (Financial Constraints): Đánh giá độ nhạy dòng tiền đầu tư.",
                "Đề tài Luận án Tiến sĩ: Đo lường tác động lan tỏa công nghệ (Technology Spillover) từ các tập đoàn đa quốc gia FDI đến tài sản vô hình của doanh nghiệp nội địa Việt Nam."
            ]
        },
        review_questions=[
            "1. Phân biệt nguyên giá lịch sử và giá đánh giá lại của tài sản cố định.",
            "2. Phân tích phương trình W = C_L * H. Muốn tăng năng suất lao động W, doanh nghiệp cần kết hợp chính sách trang bị vốn và quản trị hiệu suất máy móc như thế nào?",
            "3. Viết code Python tính toán bảng khấu hao tài sản cố định theo phương pháp đường thẳng và số dư giảm dần có điều chỉnh."
        ]
    )

    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Thống kê Chi phí Sản xuất, Giá thành và Lợi nhuận",
        introduction="Quản trị chi phí và tối ưu hóa giá thành là chìa khóa sống còn quyết định biên lợi nhuận và sức cạnh tranh giá bán của doanh nghiệp trên thương trường.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phân loại Chi phí và Thống kê Biến động Giá thành",
                "content": "Chi phí sản xuất được phân loại theo yếu tố (chi phí nguyên vật liệu, nhân công, khấu hao, dịch vụ mua ngoài) hoặc theo công dụng kinh tế (chi phí trực tiếp, chi phí gián tiếp sản xuất chung, chi phí bán hàng, chi phí quản lý).\n\nGiá thành sản phẩm đơn vị z = Chi phí sản xuất / Sản lượng. Chỉ số giá thành cá thể iz = z1 / z0. Chỉ số tổng hợp giá thành sản phẩm so sánh được (phân tích biến động giá thành không tính sản phẩm mới) phản ánh tỷ lệ hạ giá thành: Iz = Sum(z1*q1) / Sum(z0*q1). Mức hạ giá thành tuyệt đối M = Sum(z1*q1) - Sum(z0*q1).",
                "formulas": [
                    "Chi so tong hop gia thanh: I_z = ( Sum z_1 * q_1 ) / ( Sum z_0 * q_1 )",
                    "Muc ha gia thanh tuyet doi: Delta_Z = Sum z_1*q_1 - Sum z_0*q_1  (Delta_Z < 0 la tiet kiem)",
                    "Ty le ha gia thanh: M_z% = ( I_z - 1 ) * 100%",
                    "Chi phi tren 1000 dong gia tri san luong: F_cp = ( Tong chi phi / GO ) * 1000"
                ],
                "case_studies": [
                    {"title": "Chiến lược cắt giảm giá thành sản xuất cá tra xuất khẩu Vĩnh Hoàn", "detail": "Năm 2024, Vĩnh Hoàn tự chủ 75% nguồn thức ăn chăn nuôi, giúp chỉ số giá thành Iz = 0.93 (tiết kiệm 7% giá thành sản xuất), mang lại mức tiết kiệm chi phí tuyệt đối hơn 320 tỷ VNĐ."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Phân tích Điểm Hòa vốn và Thống kê Lợi nhuận",
                "content": "Phân loại chi phí theo mức độ hoạt động: Chi phí biến đổi (Variable Costs - VC phụ thuộc tuyến tính vào sản lượng Q: VC = v*Q) và Chi phí cố định (Fixed Costs - FC không đổi khi sản lượng dao động trong vùng liên quan).\n\nTổng chi phí TC = FC + v*Q. Doanh thu TR = P*Q. Điểm hòa vốn (Break-Even Point - BEP) là điểm nơi TR = TC <=> Q_be = FC / (P - v). Khoảng chênh lệch (P - v) gọi là lãi trên biến phí (Contribution Margin per unit). Thống kê lợi nhuận gồm: Lợi nhuận gộp, Lợi nhuận thuần từ HĐKD, Lợi nhuận trước thuế (EBIT) và Lợi nhuận sau thuế (NPAT).",
                "formulas": [
                    "San luong hoa von: Q_be = FC / ( P - v )",
                    "Doanh thu hoa von: TR_be = Q_be * P = FC / [ 1 - (v/P) ]",
                    "Do don bay hoat dong (Degree of Operating Leverage): DOL = [ Q*(P - v) ] / [ Q*(P - v) - FC ]",
                    "Loi nhuan hoat dong: EBIT = Q * (P - v) - FC"
                ],
                "case_studies": [
                    {"title": "Phân tích điểm hòa vốn các đường bay quốc tế của Vietnam Airlines", "detail": "Xác định hệ số lấp đầy ghế hòa vốn (Break-even Load Factor) của chặng bay Hà Nội - London là 74%. Việc mở rộng hạng vé thương gia nâng Contribution Margin, giảm tỷ lệ lấp đầy hòa vốn xuống 68%."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Phương pháp định lượng ước lượng hàm chi phí ngắn hạn và dài hạn Translog: Kiểm định tính tối ưu quy mô kinh tế (Economies of Scale) và tính kinh tế phạm vi (Economies of Scope).",
                "Phân tích hành vi chi phí bất cân xứng (Cost Stickiness) trong các doanh nghiệp nhà nước cổ phần hóa tại Việt Nam.",
                "Đề tài Luận án Tiến sĩ: Khảo sát cấu trúc chi phí và rào cản gia nhập thị trường ngành logistics thương mại điện tử Việt Nam."
            ]
        },
        review_questions=[
            "1. Phân biệt chỉ số giá thành sản phẩm so sánh được và toàn bộ sản phẩm của doanh nghiệp.",
            "2. Ý nghĩa của đòn bẩy hoạt động (DOL) trong quản trị rủi ro kinh doanh khi thị trường suy thoái.",
            "3. Viết code Python tính toán sản lượng hòa vốn, doanh thu hòa vốn và vẽ đồ thị phân tích CVP (Cost-Volume-Profit)."
        ]
    )

    # Chapter 6
    b.add_chapter(
        chap_num="6",
        chap_title="Thống kê Hiệu quả Kinh doanh và Năng lực Cạnh tranh",
        introduction="Hiệu quả kinh doanh tổng hợp và năng suất tổng nhân tố (TFP) là thước đo tối hậu đánh giá chất lượng tăng trưởng và năng lực cạnh tranh dài hạn của doanh nghiệp.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Hệ thống chỉ số Khả năng Sinh lời và Mô hình DuPont",
                "content": "Khả năng sinh lời phản ánh năng lực tạo ra lợi nhuận từ các nguồn lực được huy động. Các chỉ tiêu chính gồm: Tỷ suất sinh lời trên tài sản ROA = Lợi nhuận sau thuế / Tổng tài sản bình quân; Tỷ suất sinh lời trên vốn chủ sở hữu ROE = Lợi nhuận sau thuế / Vốn chủ sở hữu bình quân; Tỷ suất sinh lời trên doanh thu ROS = Lợi nhuận sau thuế / Doanh thu thuần.\n\nMô hình phân tích DuPont phân rã ROE thành tích của 3 nhân tố: Biên lợi nhuận ròng (Net Profit Margin), Vòng quay tổng tài sản (Asset Turnover) và Đòn bẩy tài chính (Equity Multiplier): ROE = ROS * (Doanh thu / Tài sản) * (Tài sản / Vốn CSH).",
                "formulas": [
                    "ROA = NPAT / Tong Tai San_bar",
                    "ROE = NPAT / Von CSH_bar",
                    "ROS = NPAT / Doanh thu thuan",
                    "Mo hinh DuPont 3 buoc: ROE = ROS * ( Doanh thu / Tai san ) * ( Tai san / Von CSH )",
                    "Mo hinh DuPont 5 buoc: ROE = (NPAT/EBT) * (EBT/EBIT) * (EBIT/Doanh thu) * (Doanh thu/Tai san) * (Tai san/Von CSH)"
                ],
                "case_studies": [
                    {"title": "Phân tích DuPont hiệu quả tài chính Công ty Cổ phần Cơ điện lạnh (REE)", "detail": "ROE năm 2024 đạt 21.4%. Mô hình DuPont chỉ rõ động lực tăng trưởng cốt lõi đến từ biên lợi nhuận ròng ROS cao (34%) của mảng thủy điện và văn phòng cho thuê thay vì lạm dụng đòn bẩy tài chính nợ vay."}
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Đo lường Năng suất Tổng nhân tố (TFP) Doanh nghiệp",
                "content": "Tăng trưởng giá trị sản lượng xuất phát từ hai nguồn: Tăng quy mô các yếu tố đầu vào (vốn K, lao động L) và Tăng hiệu quả sử dụng tổng hợp các yếu tố, gọi là Năng suất Tổng nhân tố (Total Factor Productivity - TFP).\n\nPhương pháp phần dư Solow (Solow Residual) xác định tốc độ tăng TFP: g_TFP = g_Y - alpha * g_K - beta * g_L. TFP phản ánh tác động của tiến bộ công nghệ, nâng cao kỹ năng lao động, hợp lý hóa tổ chức sản xuất và chuyển đổi số.",
                "formulas": [
                    "Ham san xuat: Y = A * K^alpha * L^beta  (A dai dien cho trinh do TFP)",
                    "Toc do tang TFP: g_TFP = g_Y - alpha * g_K - beta * g_L",
                    "Ty le dong gop cua TFP vao tang truong: Contrib_TFP = ( g_TFP / g_Y ) * 100%",
                    "Hieu qua ky thuat TE (Technical Efficiency): 0 <= TE <= 1"
                ],
                "case_studies": [
                    {"title": "Đo lường TFP tại Công ty Cổ phần Tập đoàn Hòa Phát", "detail": "Nghiên cứu giai đoạn 2018-2024 cho thấy tốc độ tăng TFP bình quân đạt 3.8%/năm, đóng góp 32.5% vào tổng tăng trưởng sản lượng thép của Hòa Phát, minh chứng hiệu quả của công nghệ lò cao khép kín Dung Quất."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Ước lượng TFP cấp doanh nghiệp xử lý nội sinh biến đầu vào bằng phương pháp bán tham số Olley - Pakes (1996), Levinsohn - Petrin (2003) và Ackerberg - Caves - Frazer (2015).",
                "Mô hình Phân tích Biên ngẫu nhiên (Stochastic Frontier Analysis - SFA) và Phân tích Bao dữ liệu (Data Envelopment Analysis - DEA) đo lường hiệu quả kỹ thuật và hiệu quả phân bổ nguồn lực.",
                "Đề tài Luận án Tiến sĩ: Khảo sát sự phân hóa TFP doanh nghiệp (Firm Productivity Heterogeneity) và tái phân bổ nguồn lực kinh tế tại Việt Nam hậu gia nhập CPTPP."
            ]
        },
        review_questions=[
            "1. Phân tích ý nghĩa 3 thành phần của mô hình phân tích DuPont đối với việc ra quyết định của cổ đông.",
            "2. Trình bày ưu điểm và hạn chế của phương pháp phần dư Solow khi đo lường TFP ở cấp độ doanh nghiệp cá thể.",
            "3. Viết code Python thực hiện phân tích DuPont 5 bước và trực quan hóa đóng góp của từng nhân tố qua Waterfall Chart."
        ]
    )
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\07_Toán, Thống kê, Kinh tế lượng & Tin học\[NEU] Thống kê doanh nghiệp - PGS.TS Phan Công Nghĩa (NXB ĐHKTQD)"
    pdf_name = "[NEU] [Giáo trình Toàn văn] Thống kê doanh nghiệp - PGS.TS Phan Công Nghĩa (NXB ĐHKTQD).pdf"
    p_path = os.path.join(out_dir, pdf_name)
    pages, sz = b.save(p_path)
    print(f"-> Book 4 Completed: {pages} pages, {sz:.2f} MB saved at: {p_path}")
    return {"id": 4, "title": b.title, "pages": pages, "size_mb": sz, "path": p_path}

if __name__ == "__main__":
    results = []
    results.append(build_book_1())
    results.append(build_book_2())
    results.append(build_book_3())
    results.append(build_book_4())
    print("\n=== SUMMARY PART 1 (BOOKS 1 TO 4) ===")
    for r in results:
        print(f"Book {r['id']}: {r['title']} | Pages: {r['pages']} | Size: {r['size_mb']:.2f} MB")
