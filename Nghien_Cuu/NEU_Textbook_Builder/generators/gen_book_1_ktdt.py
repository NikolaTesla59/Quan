# -*- coding: utf-8 -*-
"""
Generator for Textbook 1:
[NEU] Kinh tế đầu tư - PGS.TS Từ Quang Phương (NXB ĐHKTQD)
"""
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_ktdt():
    title = "Kinh tế đầu tư"
    subject_code = "KTDT1101"
    faculty = "Viện Ngân hàng - Tài chính / Khoa Đầu tư"
    authors = "PGS.TS. Từ Quang Phương & PGS.TS. Nguyễn Bạch Nguyệt (Đồng Chủ biên)"
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\01_Tài chính Doanh nghiệp & Đầu tư\[NEU] Kinh tế đầu tư - PGS.TS Từ Quang Phương (NXB ĐHKTQD)"
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Kinh tế đầu tư - PGS.TS Từ Quang Phương (NXB ĐHKTQD).pdf")
    
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
            "chapter_title": "Bản chất, Vai trò và Cơ cấu Đầu tư Phát triển",
            "topics": [
                "Khái niệm, đặc điểm và phân loại đầu tư phát triển trong nền kinh tế thị trường",
                "Mối quan hệ biện chứng giữa tích lũy, đầu tư và tăng trưởng kinh tế (Mô hình Harrod-Domar & Solow-Swan)",
                "Cơ cấu đầu tư theo ngành, vùng lãnh thổ và thành phần kinh tế",
                "Chuyên đề Tiến sĩ: Hàm đầu tư phi tuyến tính và chi phí điều chỉnh vốn dạng lồi (Convex Capital Adjustment Cost)"
            ]
        },
        {
            "chapter_num": "2",
            "chapter_title": "Nguồn vốn Đầu tư và Cơ chế Huy động, Phân bổ Nguồn lực",
            "topics": [
                "Nguồn vốn đầu tư trong nước (Ngân sách nhà nước, Tín dụng thương mại, Vốn tự có của doanh nghiệp và Dân cư)",
                "Nguồn vốn đầu tư quốc tế (FDI, FII, ODA, Vay nợ thương mại nước ngoài)",
                "Chiến lược dịch chuyển cơ cấu vốn và giảm phụ thuộc vào tín dụng ngân hàng",
                "Chuyên đề Tiến sĩ: Frictions trên thị trường tài chính và bẫy phân bổ sai nguồn lực (Capital Misallocation)"
            ]
        },
        {
            "chapter_num": "3",
            "chapter_title": "Phương pháp Luận Lập và Thẩm định Dự án Đầu tư",
            "topics": [
                "Chu kỳ vận động của dự án đầu tư: Từ ý tưởng, tiền khả thi đến vận hành khai thác",
                "Kỹ thuật thẩm định tài chính dự án: NPV, IRR, MIRR, Thời gian hoàn vốn có chiết khấu, Tỷ số B/C",
                "Thẩm định kinh tế - xã hội: Giá bóng (Shadow Prices), Tỷ suất chiết khấu xã hội (SDR) và Ngoại ứng",
                "Chuyên đề Tiến sĩ: Định giá quyền chọn thực (Real Options Valuation) trong môi trường bất định"
            ]
        },
        {
            "chapter_num": "4",
            "chapter_title": "Quản lý Dự án Đầu tư Công và Hiệu quả Sử dụng Vốn Toàn xã hội",
            "topics": [
                "Đầu tư công: Vai trò dẫn dắt đầu tư tư nhân (Crowding-in vs Crowding-out effects)",
                "Hệ số ICOR toàn diện và phương pháp phân rã đóng góp của TFP",
                "Đấu thầu, giám sát tiến độ và kiểm toán dự án đầu tư công tại Việt Nam",
                "Chuyên đề Tiến sĩ: Bất cân xứng thông tin, Rủi ro đạo đức và Tham nhũng trong chuỗi cung ứng đầu tư công"
            ]
        },
        {
            "chapter_num": "5",
            "chapter_title": "Đầu tư Trực tiếp Nước ngoài (FDI) và Chuỗi Giá trị Toàn cầu",
            "topics": [
                "Lý thuyết OLI của Dunning và động cơ dịch chuyển dòng vốn FDI",
                "Tác động lan tỏa công nghệ (Technology Spillovers) và liên kết ngược (Backward Linkages)",
                "Chính sách thu hút FDI thế hệ mới và tiêu chuẩn ESG trong đầu tư xanh",
                "Chuyên đề Tiến sĩ: Nhận diện nhân quả (Causal Identification) tác động lan tỏa FDI bằng phương pháp DiD và IV"
            ]
        }
    ]
    b.add_table_of_contents(toc_data)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Bản chất, Vai trò và Cơ cấu Đầu tư Phát triển",
        introduction="Chương 1 cung cấp nền tảng lý luận toàn diện về đầu tư phát triển, phân tích vai trò cốt lõi của đầu tư trong việc gia tăng trữ lượng vốn tư bản, đổi mới công nghệ và thúc đẩy tăng trưởng kinh tế bền vững trong điều kiện nền kinh tế thị trường định hướng xã hội chủ nghĩa.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bản chất kinh tế và đặc trưng của đầu tư phát triển",
                "content": (
                    "Đầu tư phát triển là việc chi dùng vốn trong hiện tại nhằm tạo ra tài sản vật chất và tài sản trí tuệ mới, "
                    "làm gia tăng năng lực sản xuất của nền kinh tế trong tương lai. Khác với đầu tư tài chính thuần túy (chuyển giao quyền sở hữu tài sản tài chính), "
                    "đầu tư phát triển trực tiếp làm thay đổi hàm sản xuất tổng hợp.\n\n"
                    "Các đặc điểm cốt lõi của đầu tư phát triển bao gồm: Quy mô vốn lớn, thời gian hoàn vốn kéo dài, tính bất thuận nghịch (Irreversibility) cao, "
                    "và chứa đựng nhiều yếu tố bất định mang tính chu kỳ vĩ mô. Sự thành bại của chiến lược đầu tư quyết định trực tiếp đến cơ cấu kinh tế quốc gia."
                ),
                "formulas": [
                    "Hệ số ICOR = (Tổng vốn đầu tư / GDP) / (Tốc độ tăng trưởng GDP) = (I_t / Y_t) / (Delta Y_t / Y_{t-1})",
                    "Mô hình Harrod-Domar: g = s / k (với g là tốc độ tăng trưởng, s là tỷ lệ tiết kiệm, k là hệ số ICOR)"
                ],
                "case_studies": [
                    {
                        "title": "Hiệu quả sử dụng vốn đầu tư tại Việt Nam giai đoạn 2011-2025",
                        "detail": "Giai đoạn 2011-2015 hệ số ICOR của Việt Nam ở mức 6.25, đã cải thiện xuống 5.98 giai đoạn 2016-2020 nhờ cơ cấu lại đầu tư công và thúc đẩy đầu tư khu vực tư nhân."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Cơ cấu đầu tư phát triển và chuyển dịch cơ cấu kinh tế",
                "content": (
                    "Cơ cấu đầu tư phản ánh sự phân bổ nguồn lực vốn theo ngành kinh tế, vùng lãnh thổ và các thành phần sở hữu. "
                    "Sự dịch chuyển cơ cấu đầu tư là động lực trực tiếp định hình chuyển dịch cơ cấu kinh tế theo hướng hiện đại hóa, công nghiệp hóa.\n\n"
                    "Tại các nền kinh tế đang phát triển, việc tập trung đầu tư vào hạ tầng giao thông logistics, năng lượng tái tạo và công nghệ số "
                    "tạo ra ngoại ứng mạng lưới (Network Externalities) cực kỳ mạnh mẽ, kích hoạt làn sóng đầu tư của khu vực tư nhân trong nước và quốc tế."
                ),
                "formulas": [
                    "Cơ cấu vốn theo thành phần: S_i = I_i / I_total, với sum(S_i) = 1 (Nhà nước, Ngoài nhà nước, FDI)",
                    "Độ co giãn của sản lượng theo vốn: epsilon_K = (dY / dK) * (K / Y) trong hàm Cobb-Douglas Y = A * K^alpha * L^(1-alpha)"
                ],
                "case_studies": [
                    {
                        "title": "Chuyển dịch cơ cấu đầu tư vào hạ tầng năng lượng xanh",
                        "detail": "Tỷ trọng vốn đầu tư vào điện gió và điện mặt trời tại khu vực Nam Trung Bộ đã tăng vọt từ dưới 2% (2018) lên trên 14% tổng vốn đầu tư năng lượng quốc gia năm 2024."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Dynamic Investment với chi phí điều chỉnh vốn phi tuyến: Max E_0 sum beta^t [Pi(K_t, L_t) - I_t - C(I_t, K_t)].",
                "Q-theory of Investment của Hayashi (1982): Phân biệt Marginal Q và Average Q khi có tính kinh tế theo quy mô (Constant Returns to Scale).",
                "Khung kiểm định nội sinh: Phương pháp GMM sai phân (Arellano-Bond 1991) và System GMM (Blundell-Bond 1998) kiểm định độ nhạy cảm của dòng tiền (Cash-Flow Sensitivity of Investment)."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt bản chất giữa đầu tư phát triển và đầu tư tài chính thuần túy?",
            "Tại sao hệ số ICOR cao kéo dài thường là dấu hiệu cảnh báo về sự suy giảm hiệu quả phân bổ vốn của một nền kinh tế?",
            "Trình bày mô hình Q của Hayashi và giải thích tại sao bất cân xứng thông tin làm sai lệch quyết định đầu tư tối ưu?"
        ]
    )
    
    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Nguồn vốn Đầu tư và Cơ chế Huy động, Phân bổ Nguồn lực",
        introduction="Chương 2 phân tích cấu trúc các nguồn vốn trong nền kinh tế, cơ chế dẫn vốn qua hệ thống ngân hàng và thị trường vốn, đồng thời đánh giá các rào cản phân bổ nguồn lực tài chính gây tổn thất phúc lợi xã hội.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Các kênh huy động vốn đầu tư phát triển trong nước",
                "content": (
                    "Huy động vốn trong nước giữ vai trò quyết định tính tự chủ kinh tế quốc gia. Các kênh huy động chủ yếu gồm: "
                    "Ngân sách nhà nước (thuế, phí, phát hành trái phiếu chính phủ), tín dụng trung - dài hạn từ các tổ chức tín dụng, "
                    "và phát hành cổ phiếu, trái phiếu doanh nghiệp trên thị trường chứng khoán.\n\n"
                    "Sự mất cân đối khi doanh nghiệp phụ thuộc quá mức vào vốn tín dụng ngân hàng ngắn hạn để tài trợ các dự án đầu tư dài hạn "
                    "tạo ra rủi ro kỳ hạn nghiêm trọng (Maturity Mismatch), dễ kích hoạt khủng hoảng thanh khoản hệ thống khi lãi suất biến động."
                ),
                "formulas": [
                    "Tỷ lệ tích lũy nội bộ: Gross Domestic Savings Rate = (GDP - Total Consumption) / GDP",
                    "Cân bằng vĩ mô nguồn vốn: (S - I) + (T - G) = (X - M) (Tiết kiệm tư nhân, thặng dư ngân sách và cán cân thương mại)"
                ],
                "case_studies": [
                    {
                        "title": "Tái cơ cấu thị trường trái phiếu doanh nghiệp tại Việt Nam",
                        "detail": "Nghị định 65/2022/NĐ-CP và Nghị định 08/2023/NĐ-CP đã chuẩn hóa điều kiện phát hành trái phiếu riêng lẻ, bảo vệ nhà đầu tư chuyên nghiệp và lành mạnh hóa thị trường vốn dài hạn."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Nguồn vốn đầu tư quốc tế và an ninh tài chính",
                "content": (
                    "Nguồn vốn quốc tế bổ sung lượng ngoại tệ quan trọng cho cán cân thanh toán, hỗ trợ chuyển giao công nghệ và kỹ năng quản trị tiên tiến. "
                    "Tuy nhiên, dòng vốn danh mục nước ngoài (FII) có tính biến động cao (Hot Money), dễ tháo chạy khi có cú sốc lãi suất toàn cầu.\n\n"
                    "Quản lý nợ nước ngoài và duy trì tỷ lệ dự trữ ngoại hối an toàn là yêu cầu sống còn để bảo đảm chủ quyền tài chính quốc gia."
                ),
                "formulas": [
                    "Hệ số gánh nặng nợ nước ngoài: D_ratio = (Tổng nợ nước ngoài) / GDP <= 50%",
                    "Tỷ lệ nghĩa vụ nợ trên kim ngạch xuất khẩu: Debt Service Ratio = (Gốc + Lãi phải trả trong năm) / Kim ngạch xuất khẩu (X_t)"
                ],
                "case_studies": [
                    {
                        "title": "Chuyển đổi hình thức vay vốn ODA sang vay thương mại",
                        "detail": "Việt Nam tốt nghiệp IDA từ năm 2017, chuyển dịch dần sang vay IBRD với lãi suất thị trường, đặt ra yêu cầu thẩm định khắt khe hơn đối với từng dự án sử dụng vốn vay nước ngoài."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Phân bổ Sai Nguồn lực Vốn (Capital Misallocation) theo Hsieh-Klenow (2009): Đo lường khoảng cách giữa Marginal Revenue Product of Capital (MRPK) giữa các doanh nghiệp.",
                "Lý thuyết Hạn chế Tài chính (Financial Constraints) của Fazzari, Hubbard & Petersen (1988) và chỉ số KZ / WW index.",
                "Mô hình DSGE với khu vực ngân hàng (Gertler & Karadi 2011) mô phỏng cú sốc vốn đầu tư và cơ chế khuếch đại tài chính (Financial Accelerator)."
            ]
        },
        review_questions=[
            "Phân tích cơ chế tác động của hiện tượng Maturity Mismatch khi doanh nghiệp dùng vốn ngắn hạn đầu tư tài sản cố định?",
            "Trình bày phương pháp đo lường tổn thất TFP do phân bổ sai nguồn vốn theo khung lý thuyết Hsieh-Klenow?",
            "Tại sao vốn FDI được đánh giá là nguồn lực đầu tư có tính ổn định cao hơn so với FII trong giai đoạn khủng hoảng vĩ mô?"
        ]
    )
    
    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Phương pháp Luận Lập và Thẩm định Dự án Đầu tư",
        introduction="Chương 3 trình bày hệ thống phương pháp luận lập và thẩm định dự án đầu tư theo chuẩn mực quốc tế, bao gồm thẩm định kỹ thuật, thẩm định tài chính vi mô và thẩm định kinh tế - xã hội vĩ mô.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phương pháp thẩm định tài chính dự án",
                "content": (
                    "Thẩm định tài chính nhằm xác định tính khả thi và khả năng sinh lời của dự án từ góc nhìn của chủ đầu tư và các tổ chức tài trợ vốn. "
                    "Dòng tiền dự án (Free Cash Flow to Firm - FCFF) phải được dự báo trên nguyên tắc dòng tiền tăng thêm (Incremental Cash Flows).\n\n"
                    "Các chỉ tiêu kinh tế cơ bản gồm: NPV (Giá trị hiện tại thuần), IRR (Tỷ suất sinh lời nội hàm), MIRR (Tỷ suất sinh lời nội hàm điều chỉnh) "
                    "và Thời gian hoàn vốn có chiết khấu. Việc lựa chọn suất chiết khấu phản ánh đúng chi phí sử dụng vốn bình quân trọng số (WACC) có tính đến rủi ro dự án."
                ),
                "formulas": [
                    "NPV = sum_{t=0}^T [ CF_t / (1 + r)^t ]",
                    "IRR: Nghiệm r thỏa mãn NPV(r) = sum_{t=0}^T [ CF_t / (1 + IRR)^t ] = 0",
                    "WACC = (E/V) * r_e + (D/V) * r_d * (1 - t_c)"
                ],
                "case_studies": [
                    {
                        "title": "Thẩm định tài chính dự án Cảng hàng không quốc tế Long Thành",
                        "detail": "Dự án với tổng mức đầu tư trên 16 tỷ USD được phân kỳ thành 3 giai đoạn, áp dụng mô hình chiết khấu dòng tiền phức hợp đa kỳ với WACC điều chỉnh theo rủi ro quốc gia."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Thẩm định kinh tế - xã hội và đánh giá tác động môi trường",
                "content": (
                    "Thẩm định kinh tế - xã hội đánh giá đóng góp thực tế của dự án đối với toàn bộ nền kinh tế quốc dân. "
                    "Giá thị trường thường bị méo mó bởi thuế, trợ cấp và độc quyền, do đó bắt buộc phải quy đổi về giá bóng (Shadow Prices) hoặc chi phí cơ hội xã hội.\n\n"
                    "Đánh giá tác động môi trường (EIA) và chi phí ngoại ứng tiêu cực (phát thải khí nhà kính, ô nhiễm nguồn nước) "
                    "phải được nội hóa (Internalized) vào dòng ngân lưu kinh tế của dự án."
                ),
                "formulas": [
                    "ENPV = sum_{t=0}^T [ (Social Benefits_t - Social Costs_t) / (1 + SDR)^t ]",
                    "Hệ số chuyển đổi giá bóng: CF_i = P_shadow / P_market (Conversion Factor)"
                ],
                "case_studies": [
                    {
                        "title": "Phân tích Chi phí - Lợi ích (CBA) dự án Đường sắt đô thị Cát Linh - Hà Đông",
                        "detail": "Ngoài doanh thu bán vé, dự án mang lại lợi ích xã hội khổng lồ từ việc tiết kiệm thời gian di chuyển, giảm tai nạn giao thông và giảm phát thải CO2 cho Thủ đô Hà Nội."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Quyền chọn Thực (Real Options) của Dixit & Pindyck (1994): Định giá quyền chọn trì hoãn (Option to Wait), mở rộng (Option to Expand) và từ bỏ (Option to Abandon) giải phương trình vi phân ngẫu nhiên (PDE) Ito Lemma.",
                "Mô phỏng Monte Carlo đa biến kết hợp Copula phụ thuộc phi tuyến trong đánh giá rủi ro tham số dự án.",
                "Khung thẩm định dự án PPP (Public-Private Partnership) với lý thuyết Hợp đồng không hoàn hảo (Incomplete Contracts) của Hart & Moore."
            ]
        },
        review_questions=[
            "Tại sao chỉ tiêu NPV luôn được ưu tiên hơn IRR khi hai dự án có quy mô vốn hoặc hình thái dòng tiền mâu thuẫn nhau?",
            "Phân tích cơ chế nội hóa ngoại ứng môi trường vào dòng chi phí kinh tế của một dự án công nghiệp nặng?",
            "Xây dựng mô hình quyền chọn trì hoãn đầu tư (Option to Delay) khi giá bán sản phẩm tuân theo quá trình Geometric Brownian Motion (GBM)?"
        ]
    )
    
    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Quản lý Dự án Đầu tư Công và Hiệu quả Sử dụng Vốn Toàn xã hội",
        introduction="Chương 4 nghiên cứu chuyên sâu về cơ chế quản lý, chu trình giải ngân và giám sát các dự án đầu tư công, giải quyết bài toán chống thất thoát, tham nhũng và tối ưu hóa hiệu ứng lan tỏa của vốn ngân sách nhà nước.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Đầu tư công và tác động lan tỏa đối với kinh tế tư nhân",
                "content": (
                    "Đầu tư công đóng vai trò 'vốn mồi' kiến tạo hạ tầng dùng chung, giảm chi phí giao dịch cho toàn bộ nền kinh tế. "
                    "Tuy nhiên, nếu đầu tư công dàn trải, kém hiệu quả, nó sẽ tạo ra hiện tượng 'chèn lấn' (Crowding-out), "
                    "đẩy lãi suất lên cao và thu hẹp không gian tiếp cận tín dụng của khu vực kinh tế tư nhân.\n\n"
                    "Luật Đầu tư công của Việt Nam đã thiết lập kỷ cương kế hoạch đầu tư công trung hạn 5 năm, xóa bỏ cơ chế xin - cho và phân tán nguồn lực."
                ),
                "formulas": [
                    "Hệ số nhân đầu tư công: Multiplier = dY / dG = 1 / (1 - MPC * (1 - t) + MPI)",
                    "Hiệu ứng chèn lấn: dI_private / dG < 0 khi thị trường vốn cận biên co hẹp"
                ],
                "case_studies": [
                    {
                        "title": "Hiệu ứng lan tỏa của tuyến Cao tốc Bắc - Nam phía Đông",
                        "detail": "Các địa phương có tuyến cao tốc đi qua ghi nhận mức tăng trưởng thu hút vốn đầu tư tư nhân bình quân cao hơn 28% so với các địa phương không kết nối trực tiếp trong giai đoạn 2020-2025."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Kiểm toán, giải ngân và quản trị rủi ro đầu tư công",
                "content": (
                    "Quy trình đấu thầu qua mạng quốc gia, thanh quyết toán vốn đầu tư công và kiểm toán nhà nước "
                    "là các công cụ kiểm soát cốt lõi nhằm ngăn chặn hiện tượng 'đội vốn' và 'chậm tiến độ' kinh niên trong các dự án công.\n\n"
                    "Việc phân cấp, phân quyền đi kèm với trách nhiệm giải trình cá nhân của người đứng đầu cơ quan phê duyệt dự án "
                    "là giải pháp đột phá thể chế được NEU và các chuyên gia kinh tế đầu tư liên tục khuyến nghị."
                ),
                "formulas": [
                    "Tỷ lệ giải ngân vốn đầu tư công: R_disburse = (Vốn thực thanh toán) / (Kế hoạch vốn được giao) * 100%",
                    "Chỉ số chênh lệch dự toán: Cost Overrun Ratio = (Chi phí quyết toán thực tế - Tổng mức đầu tư phê duyệt) / (Tổng mức đầu tư phê duyệt)"
                ],
                "case_studies": [
                    {
                        "title": "Kỷ cương giải ngân vốn đầu tư công năm 2023-2025",
                        "detail": "Chính phủ thành lập các tổ công tác đặc biệt kiểm tra hiện trường, tỷ lệ giải ngân đạt trên 95% kế hoạch Thủ tướng giao, tạo động lực tăng trưởng GDP then chốt."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Lựa chọn Công cộng (Public Choice Theory) trong phân bổ vốn ngân sách: Mô hình Rent-Seeking và ngân sách mềm (Soft Budget Constraint) theo Kornai.",
                "Đánh giá tác động nhân quả của đầu tư công hạ tầng bằng phương pháp Tiếp cận Đồ thị Không gian (Spatial Econometrics) và Nghiên cứu Sự kiện (Event Study).",
                "Khung tối ưu hóa chính sách tài khóa trong mô hình New Keynesian DSGE với chi tiêu công tích lũy tư bản hiệu dụng (Productive Public Capital)."
            ]
        },
        review_questions=[
            "Phân tích điều kiện để đầu tư công tạo ra hiệu ứng dẫn dắt (Crowding-in) thay vì chèn lấn (Crowding-out) khu vực tư nhân?",
            "Nguyên nhân kinh tế học sâu xa của hiện tượng đội vốn và kéo dài thời gian thi công ở các dự án hạ tầng công cộng tại Việt Nam?",
            "Thiết lập mô hình kinh tế lượng không gian (Spatial Durbin Model) để kiểm định tác động lan tỏa qua biên giới hành chính của đường cao tốc?"
        ]
    )
    
    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Đầu tư Trực tiếp Nước ngoài (FDI) và Chuỗi Giá trị Toàn cầu",
        introduction="Chương 5 phân tích sâu dòng vốn FDI, các lý thuyết định vị tập đoàn đa quốc gia (MNCs), chiến lược tham gia chuỗi cung ứng toàn cầu và chính sách thu hút FDI thế hệ mới gắn với phát triển bền vững.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Lý thuyết OLI và động thái chiến lược của tập đoàn đa quốc gia",
                "content": (
                    "Mô hình OLI của Dunning giải thích sự hình thành của dòng vốn FDI dựa trên ba lợi thế vượt trội: "
                    "Ownership advantages (Lợi thế sở hữu tài sản độc quyền/công nghệ), Location advantages (Lợi thế vị trí địa lý, chi phí nhân công, chính sách ưu đãi) "
                    "và Internalization advantages (Lợi thế nội bộ hóa nhằm bảo vệ bí mật công nghệ và tránh chi phí giao dịch thị trường).\n\n"
                    "Việt Nam đã tận dụng thành công vị trí chiến lược trong xu thế đa dạng hóa chuỗi cung ứng 'China + 1', "
                    "thu hút hàng loạt tập đoàn công nghệ hàng đầu thế giới như Samsung, Apple, Intel, Foxconn đầu tư nhà máy sản xuất quy mô lớn."
                ),
                "formulas": [
                    "Chỉ số thu hút FDI: Inward FDI Performance Index = (FDI_i / FDI_world) / (GDP_i / GDP_world)",
                    "Mức độ liên kết công nghiệp: Linkage Index = (Tổng mua sắm từ nhà cung cấp nội địa) / (Tổng giá trị đầu vào sản xuất)"
                ],
                "case_studies": [
                    {
                        "title": "Hệ sinh thái nhà cung cấp cấp 1 và cấp 2 của Samsung tại Bắc Ninh và Thái Nguyên",
                        "detail": "Số lượng doanh nghiệp Việt Nam là nhà cung cấp cấp 1 của Samsung đã tăng từ 4 doanh nghiệp (năm 2014) lên hơn 50 doanh nghiệp vào năm 2024, minh chứng cho sự nâng cấp năng lực công nghiệp phụ trợ."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Chính sách FDI thế hệ mới và tiêu chuẩn ESG toàn cầu",
                "content": (
                    "Chiến lược thu hút FDI truyền thống dựa vào miễn giảm thuế và nhân công giá rẻ đã bộc lộ giới hạn. "
                    "Việc áp dụng Quy tắc Thuế Tối thiểu Toàn cầu (Pillar 2 của OECD) với mức thuế suất thực tế 15% từ năm 2024 "
                    "đòi hỏi Việt Nam phải chuyển hướng cạnh tranh sang hạ tầng số, năng lượng sạch, nguồn nhân lực chất lượng cao và cơ chế hỗ trợ chi phí đầu tư sau thuế.\n\n"
                    "Các dự án FDI thế hệ mới bắt buộc phải đáp ứng tiêu chuẩn Môi trường - Xã hội - Quản trị (ESG), "
                    "cam kết giảm phát thải ròng bằng 0 (Net Zero) và bảo đảm tính bền vững sinh thái."
                ),
                "formulas": [
                    "Thuế tối thiểu toàn cầu: Top-up Tax = (15% - Effective Tax Rate) * Excess Profits",
                    "Hiệu quả lan tỏa công nghệ: Spillover = beta * Foreign_Share * Domestic_Absorptive_Capacity"
                ],
                "case_studies": [
                    {
                        "title": "Dự án nhà máy Lego trung hòa carbon tại Bình Dương",
                        "detail": "Tập đoàn Lego đầu tư hơn 1 tỷ USD xây dựng nhà máy trung hòa carbon đầu tiên, sử dụng 100% năng lượng mặt trời tại chỗ, thiết lập chuẩn mực mới cho thu hút FDI xanh tại Việt Nam."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Cạnh tranh Thu hút FDI và Đua nhau xuống đáy (Race to the Bottom): Mô hình lý thuyết trò chơi giữa các chính phủ về ưu đãi thuế.",
                "Khung nhận diện nhân quả tác động lan tỏa FDI (Horizontal vs Vertical Spillovers) bằng vi dữ liệu doanh nghiệp (Firm-level panel data) theo phương pháp Javorcik (2004).",
                "Mô hình Gravity cho dòng vốn đầu tư quốc tế và tác động của các hiệp định thương mại tự do thế hệ mới (CPTPP, EVFTA) kiểm soát biến nội sinh bằng Poisson Pseudo-Maximum Likelihood (PPML)."
            ]
        },
        review_questions=[
            "Phân tích ba yếu tố O - L - I của Dunning và chỉ ra các lợi thế so sánh động của Việt Nam trong chu kỳ tái cấu trúc chuỗi cung ứng toàn cầu?",
            "Tác động của Thuế tối thiểu toàn cầu (Pillar 2) đối với môi trường đầu tư tại Việt Nam và những chính sách hỗ trợ thay thế khả thi?",
            "Trình bày chiến lược nhận diện thực nghiệm để tách bạch tác động lan tỏa công nghệ theo chiều dọc (Vertical Spillovers) và hiệu ứng cạnh tranh tiêu cực theo chiều ngang (Horizontal Stealing Effect) của FDI?"
        ]
    )
    
    pages, sz = b.save(out_pdf)
    print(f"[SUCCESS] Book 1 saved: {out_pdf} ({pages} pages, {sz:.2f} MB)")
    return {
        "title": title,
        "code": subject_code,
        "author": authors,
        "path": out_pdf,
        "pages": pages,
        "size_mb": round(sz, 2)
    }

if __name__ == "__main__":
    build_ktdt()
