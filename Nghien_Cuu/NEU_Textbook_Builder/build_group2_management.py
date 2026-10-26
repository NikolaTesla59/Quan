# -*- coding: utf-8 -*-
"""
NEU Master Textbook Builder - Group 2: Management & Supply Chain
Covers 5 Courses:
1. Quản trị học đại cương - PGS.TS Đoàn Thị Thu Hà
2. Quản trị chiến lược - PGS.TS Lê Công Hoa
3. Quản trị dự án - PGS.TS Từ Quang Phương
4. Quản trị nhân lực - PGS.TS Nguyễn Ngọc Quân
5. Quản trị Logistics & Chuỗi cung ứng - PGS.TS Đặng Đình Đào
"""
import os
import sys

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

BASE_DIR_06 = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\06_Kinh tế học, Quản trị kinh doanh & Marketing"

def build_management_principles():
    print("Building: Quản trị học đại cương...")
    builder = NEUTextbookBuilder(
        title="Quản trị học đại cương",
        subject_code="QTHD1101",
        faculty="Khoa Khoa học Quản lý",
        authors="PGS.TS. Đoàn Thị Thu Hà & PGS.TS. Nguyễn Thị Ngọc Huyền (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, HIỆN ĐẠI HÓA TOÀN DIỆN & TỔ CHỨC HỌC TẬP (LEARNING ORGANIZATION)"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về quản trị học và tổ chức hiện đại",
         "topics": ["Khái niệm quản trị, hiệu quả (Efficiency) và hiệu lực (Effectiveness)", "Các cấp bậc quản trị và 10 vai trò của nhà quản trị (Henry Mintzberg)", "Bộ kỹ năng quản trị căn bản (Robert Katz)"]},
        {"chapter_num": 2, "chapter_title": "Sự tiến hóa của các lý thuyết và trường phái quản trị",
         "topics": ["Trường phái quản trị cổ điển (Taylor, Fayol, Max Weber)", "Trường phái tâm lý - xã hội trong quản trị (Mayo, Maslow, McGregor)", "Trường phái định lượng, hệ thống và quản trị tình huống"]},
        {"chapter_num": 3, "chapter_title": "Môi trường quản trị và Văn hóa doanh nghiệp",
         "topics": ["Phân tích môi trường vĩ mô (PESTEL) và môi trường ngành", "Văn hóa tổ chức: Cấu trúc ba tầng của Edgar Schein", "Trách nhiệm xã hội của doanh nghiệp (CSR) và đạo đức kinh doanh"]},
        {"chapter_num": 4, "chapter_title": "Chức năng Hoạch định và Ra quyết định quản trị",
         "topics": ["Mục tiêu quản trị và nguyên tắc SMART", "Quy trình hoạch định chiến lược và tác nghiệp", "Mô hình ra quyết định hợp lý và các bẫy tâm lý (Kahneman & Tversky)"]},
        {"chapter_num": 5, "chapter_title": "Chức năng Tổ chức và Thiết kế cơ cấu tổ chức",
         "topics": ["Các nguyên tắc tổ chức căn bản: Phân công lao động, thống nhất chỉ huy", "Các mô hình cơ cấu tổ chức: Chức năng, ma trận, phân nhánh", "Ủy quyền, phân quyền và tầm hạn quản trị (Span of Control)"]},
        {"chapter_num": 6, "chapter_title": "Chức năng Lãnh đạo và Động viên nhân viên",
         "topics": ["Bản chất của lãnh đạo và phong cách lãnh đạo (Lewin, Blake-Mouton)", "Lý thuyết lãnh đạo tình huống (Hersey-Blanchard, Fiedler)", "Hệ thống lý thuyết động viên: Thuyết hai nhân tố Herzberg, Thuyết kỳ vọng Vroom"]},
        {"chapter_num": 7, "chapter_title": "Chức năng Kiểm soát trong tổ chức",
         "topics": ["Khái niệm, vai trò và quy trình kiểm soát 4 bước", "Các loại hình kiểm soát: Lường trước, đồng thời và phản hồi", "Thẻ điểm cân bằng (Balanced Scorecard - BSC) trong kiểm soát chiến lược"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=1,
        chap_title="Tổng quan về quản trị học và tổ chức hiện đại",
        introduction="Quản trị là quá trình làm việc cùng và thông qua những người khác nhằm thực hiện các mục tiêu của tổ chức một cách hiệu quả và có hiệu lực trong môi trường luôn biến động.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Bản chất, Hiệu lực và Hiệu quả trong quản trị",
                "content": "Quản trị vừa là một khoa học, vừa là một nghệ thuật và một nghề nghiệp chuyên nghiệp. Khoa học quản trị cung cấp hệ thống nguyên lý, phương pháp và công cụ logic; nghệ thuật quản trị thể hiện qua sự nhạy bén, linh hoạt trong giải quyết bài toán con người và tình huống cụ thể.\n\nPhân biệt rõ hai trục đánh giá cốt lõi: Hiệu lực (Effectiveness) là 'làm đúng việc' (doing the right things) - đạt được mục tiêu chiến lược; Hiệu quả (Efficiency) là 'làm việc đúng cách' (doing things right) - tối thiểu hóa chi phí và nguồn lực sử dụng.",
                "formulas": [
                    "Chỉ số Hiệu quả (Efficiency) = Đầu ra hữu ích (Output) / Đầu vào sử dụng (Input)",
                    "Mức độ Hiệu lực (Effectiveness) = Kết quả thực tế đạt được / Mục tiêu kế hoạch đề ra",
                    "Hiệu năng tổng thể của Tổ chức = f(Hiệu lực, Hiệu quả, Tính linh hoạt thích ứng)"
                ],
                "case_studies": [
                    {"title": "Tái cấu trúc bộ máy quản trị tại Tập đoàn Viettel", "detail": "Phân tích quá trình chuyển đổi từ mô hình quản trị doanh nghiệp truyền thống sang mô hình tập đoàn công nghệ số đa quốc gia, tinh gọn bộ máy và tối ưu hóa hiệu quả vận hành."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Vai trò của Henry Mintzberg và Kỹ năng của Robert Katz",
                "content": "Henry Mintzberg phân loại 10 vai trò của nhà quản trị thành 3 nhóm: Vai trò quan hệ con người (Đại diện, Lãnh đạo, Liên lạc), Vai trò thông tin (Thu thập, Phổ biến, Người phát ngôn), và Vai trò quyết định (Doanh nhân, Giải quyết xáo trộn, Phân bổ nguồn lực, Đàm phán).\n\nRobert Katz xác định 3 kỹ năng cốt lõi: Kỹ năng kỹ thuật (Technical skills), Kỹ năng nhân sự (Human skills) và Kỹ năng tư duy (Conceptual skills). Ở cấp quản trị càng cao, kỹ năng tư duy càng mang tính quyết định thành bại.",
                "formulas": [
                    "Cơ cấu kỹ năng quản trị: Cấp cao (Tư duy 50%, Nhân sự 35%, Kỹ thuật 15%)",
                    "Cấp trung (Tư duy 30%, Nhân sự 50%, Kỹ thuật 20%)",
                    "Cấp cơ sở (Tư duy 15%, Nhân sự 40%, Kỹ thuật 45%)"
                ],
                "case_studies": [
                    {"title": "Vai trò kiến tạo của ban lãnh đạo TH Group", "detail": "Đánh giá vai trò doanh nhân và tư duy chiến lược của nhà sáng lập Thái Hương trong dự án sữa tươi sạch quy mô 1.2 tỷ USD tại Nghệ An."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Thể chế Tổ chức (Organizational Institutionalism - DiMaggio & Powell): Cơ chế Đồng hình Cưỡng chế, Mô phỏng và Chuẩn mực (Coercive, Mimetic & Normative Isomorphism).",
                "Lý thuyết Cấp bậc Tối cao (Upper Echelons Theory - Hambrick & Mason): Đặc điểm Tâm lý và Nhân khẩu học của Nhóm Quản trị Cấp cao (TMT) định hình Chiến lược Doanh nghiệp.",
                "Tổ chức Học tập (Learning Organization - Peter Senge): 5 Nguyên lý Kỷ luật Thứ năm và Cơ chế Quản trị Tri thức (Knowledge Management SECI Model - Nonaka & Takeuchi)."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt giữa khái niệm 'Hiệu lực' và 'Hiệu quả'. Một tổ chức có thể đạt hiệu quả cao nhưng không có hiệu lực không? Cho ví dụ minh họa.",
            "Trình bày 10 vai trò của nhà quản trị theo Henry Mintzberg. Trong bối cảnh chuyển đổi số, vai trò nào đòi hỏi sự thích ứng mạnh mẽ nhất?",
            "Tại sao kỹ năng nhân sự (Human skills) lại đóng vai trò quan trọng đồng đều ở tất cả các cấp quản trị?"
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Quản trị học đại cương - PGS.TS Đoàn Thị Thu Hà (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Quản trị học đại cương - PGS.TS Đoàn Thị Thu Hà (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Quản trị học đại cương", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_strategic_management():
    print("Building: Quản trị chiến lược...")
    builder = NEUTextbookBuilder(
        title="Quản trị chiến lược",
        subject_code="QTCL1101",
        faculty="Viện Quản trị Kinh doanh (BS-NEU)",
        authors="PGS.TS. Lê Công Hoa & TS. Ngô Kim Thanh (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, TÍCH HỢP NĂNG LỰC ĐỘNG (DYNAMIC CAPABILITIES) & HỆ SINH THÁI"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về quản trị chiến lược và Tầm nhìn, Sứ mệnh",
         "topics": ["Khái niệm chiến lược và quy trình quản trị chiến lược toàn diện", "Tuyên bố sứ mệnh (Mission), tầm nhìn (Vision) và giá trị cốt lõi", "Các cấp độ chiến lược: Cấp công ty, cấp kinh doanh và cấp chức năng"]},
        {"chapter_num": 2, "chapter_title": "Phân tích môi trường bên ngoài: Cơ hội, Thách thức và Cạnh tranh ngành",
         "topics": ["Môi trường vĩ mô và ma trận EFE", "Mô hình 5 lực lượng cạnh tranh của Michael Porter", "Nhóm chiến lược (Strategic Groups) và ma trận hình ảnh cạnh tranh (CPM)"]},
        {"chapter_num": 3, "chapter_title": "Phân tích môi trường nội bộ: Nguồn lực và Năng lực cạnh tranh",
         "topics": ["Quan điểm dựa trên nguồn lực (Resource-Based View - RBV)", "Chuỗi giá trị (Value Chain Analysis) và Năng lực cốt lõi (Core Competencies)", "Khung đánh giá VRIO và ma trận IFE"]},
        {"chapter_num": 4, "chapter_title": "Các chiến lược cạnh tranh tổng quát cấp kinh doanh",
         "topics": ["Chiến lược dẫn đầu về chi phí thấp (Cost Leadership)", "Chiến lược khác biệt hóa sản phẩm (Differentiation)", "Chiến lược tập trung hóa (Focus Strategy) và bẫy kẹt ở giữa (Stuck in the Middle)"]},
        {"chapter_num": 5, "chapter_title": "Chiến lược cấp công ty: Đa dạng hóa và Tái cấu trúc danh mục",
         "topics": ["Chiến lược hội nhập dọc và hội nhập ngang", "Đa dạng hóa liên quan và không liên quan", "Mua bán và sáp nhập (M&A) và liên minh chiến lược", "Ma trận BCG và ma trận GE-McKinsey"]},
        {"chapter_num": 6, "chapter_title": "Thực thi chiến lược, Đánh giá và Quản trị rủi ro chiến lược",
         "topics": ["Mô hình 7S của McKinsey trong thực thi chiến lược", "Đổi mới mô hình kinh doanh (Business Model Innovation)", "Kiểm soát chiến lược và quản trị thay đổi (Change Management)"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=3,
        chap_title="Phân tích môi trường nội bộ: Nguồn lực và Năng lực cạnh tranh",
        introduction="Lợi thế cạnh tranh bền vững bắt nguồn từ bên trong doanh nghiệp. Chương này trang bị phương pháp luận xác định năng lực cốt lõi thông qua chuỗi giá trị và khung phân tích VRIO.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Quan điểm Dựa trên Nguồn lực (RBV) và Khung Phân tích VRIO",
                "content": "Trường phái Dựa trên Nguồn lực (Barney 1991) chỉ ra rằng doanh nghiệp là một tập hợp các nguồn lực và năng lực không đồng nhất và bất động hoàn hảo.\n\nKhung VRIO đánh giá 4 câu hỏi sống còn về nguồn lực: Value (Có giá trị trong khai thác cơ hội/vô hiệu hóa nguy cơ?), Rarity (Có hiếm so với đối thủ?), Inimitability (Có khó bị sao chép hay thay thế?), và Organization (Tổ chức có sẵn sàng khai thác tối đa?). Nguồn lực thỏa mãn cả 4 tiêu chí mang lại Lợi thế Cạnh tranh Bền vững (Sustainable Competitive Advantage).",
                "formulas": [
                    "VRIO Matrix: V=No -> Bất lợi cạnh tranh; V=Yes, R=No -> Ngang bằng cạnh tranh",
                    "V=Yes, R=Yes, I=No -> Lợi thế cạnh tranh tạm thời",
                    "V=Yes, R=Yes, I=Yes, O=Yes -> Lợi thế cạnh tranh bền vững"
                ],
                "case_studies": [
                    {"title": "Phân tích khung VRIO của Tập đoàn Vingroup", "detail": "Đánh giá quỹ đất chiến lược, năng lực triển khai dự án thần tốc và hệ sinh thái khách hàng đa ngành (Vinhomes, Vinmec, Vinschool, VinFast) theo chuẩn VRIO."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Chuỗi giá trị của Michael Porter và Năng lực cốt lõi",
                "content": "Chuỗi giá trị phân rã doanh nghiệp thành 9 hoạt động tạo giá trị: 5 hoạt động chính (Hậu cần nhập, Vận hành sản xuất, Hậu cần xuất, Marketing & Bán hàng, Dịch vụ khách hàng) và 4 hoạt động hỗ trợ (Cơ sở hạ tầng doanh nghiệp, Quản trị nhân lực, Phát triển công nghệ, Mua sắm).\n\nNăng lực cốt lõi (Prahalad & Hamel) là sự phối hợp phức hợp của các kỹ năng công nghệ và sản xuất qua các chuỗi giá trị, mở ra khả năng tiếp cận đa dạng thị trường.",
                "formulas": [
                    "Biên lợi nhuận (Margin) = Tổng giá trị khách hàng chi trả (Value) - Tổng chi phí chuỗi giá trị (Cost)",
                    "Mô hình 7S McKinsey: Strategy, Structure, Systems (Hard S) - Shared Values, Style, Staff, Skills (Soft S)"
                ],
                "case_studies": [
                    {"title": "Chuỗi giá trị ngành bán lẻ FPT Retail & Long Châu", "detail": "Phân tích năng lực số hóa chuỗi cung ứng dược phẩm và hệ thống ERP quản trị hàng nghìn nhà thuốc Long Châu đạt hiệu quả cao."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Năng lực Động (Dynamic Capabilities - David Teece 1997, 2007 SMJ): Năng lực Cảm nhận (Sensing), Nắm bắt (Seizing) và Chuyển đổi Cơ cấu (Transforming).",
                "Lý thuyết Hệ sinh thái Kinh doanh & Hiệu ứng Mạng hai chiều (Platform Ecosystems & Two-Sided Network Effects - Eisenmann, Parker & Van Alstyne).",
                "Mô hình Trực giác Chiến lược và Bất cân xứng Thông tin Doanh nhân (Entrepreneurial Judgment & Knightian Uncertainty)."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt cốt lõi giữa trường phái Tổ chức Ngành (I/O Model - Porter) và Trường phái Dựa trên Nguồn lực (RBV - Barney).",
            "Sử dụng khung VRIO để đánh giá một doanh nghiệp công nghệ tiêu biểu của Việt Nam (FPT hoặc Viettel).",
            "Trình bày 9 mắt xích trong chuỗi giá trị của Michael Porter và chỉ ra cách thức tối ưu hóa biên lợi nhuận thông qua chuyển đổi số."
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Quản trị chiến lược - PGS.TS Lê Công Hoa (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Quản trị chiến lược - PGS.TS Lê Công Hoa (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Quản trị chiến lược", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_project_management():
    print("Building: Quản trị dự án...")
    builder = NEUTextbookBuilder(
        title="Quản trị dự án",
        subject_code="QTDA1101",
        faculty="Khoa Đầu tư",
        authors="PGS.TS. Từ Quang Phương & TS. Đinh Văn Hải (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, CHUẨN HÓA THEO PMBOK 7TH EDITION & HYBRID AGILE"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về dự án và Hệ thống quản trị dự án đầu tư",
         "topics": ["Khái niệm, đặc điểm dự án và Tam giác ràng buộc kép (Triple Constraint)", "Chu kỳ sống của dự án và các bên liên quan (Stakeholders)", "Cơ cấu tổ chức quản trị dự án: Chức năng, ma trận, chuyên trách"]},
        {"chapter_num": 2, "chapter_title": "Xác định mục tiêu và Lập kế hoạch phạm vi dự án",
         "topics": ["Tuyên ngôn dự án (Project Charter) và tuyên bố phạm vi", "Cấu trúc phân việc (Work Breakdown Structure - WBS)", "Ma trận phân công trách nhiệm (RACI Matrix)"]},
        {"chapter_num": 3, "chapter_title": "Quản lý tiến độ dự án: Phương pháp CPM và Sơ đồ PERT",
         "topics": ["Ước lượng thời lượng công việc và sơ đồ mạng AOA/AON", "Phương pháp đường găng (Critical Path Method - CPM)", "Phân tích mạng PERT với thời lượng ngẫu nhiên", "Kỹ thuật nén tiến độ: Fast-tracking và Crashing"]},
        {"chapter_num": 4, "chapter_title": "Quản lý chi phí dự án và Phương pháp Giá trị thu được (EVM)",
         "topics": ["Lập ngân sách dự án và dòng chi phí tích lũy (Đường cong S)", "Phương pháp Earned Value Management: PV, EV, AC", "Các chỉ số hiệu năng CV, SV, CPI, SPI và dự báo ngân sách khi hoàn thành (EAC)"]},
        {"chapter_num": 5, "chapter_title": "Quản trị rủi ro và Quản trị chất lượng dự án",
         "topics": ["Quy trình nhận diện và đánh giá rủi ro (Ma trận xác suất - tác động)", "Mô phỏng Monte Carlo trong phân tích rủi ro chi phí/tiến độ", "Kế hoạch ứng phó rủi ro: Tránh né, giảm thiểu, chuyển giao, chấp nhận"]},
        {"chapter_num": 6, "chapter_title": "Quản trị dự án Agile/Scrum và Đóng dự án",
         "topics": ["Triết lý Agile, khung làm việc Scrum (Sprint, Product Backlog, Burn-down)", "Nghiệm thu, chuyển giao và tổng kết bài học kinh nghiệm (Post-Mortem)"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=4,
        chap_title="Quản lý chi phí dự án và Phương pháp Giá trị thu được (EVM)",
        introduction="Quản trị chi phí đảm bảo dự án hoàn thành trong giới hạn ngân sách được duyệt. Kỹ thuật Earned Value Management (EVM) là chuẩn mực quốc tế tích hợp đồng thời tiến độ, phạm vi và chi phí thực tế.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Hệ thống Chỉ số EVM và Phân tích Sai lệch",
                "content": "EVM dựa trên 3 trụ cột dữ liệu tại thời điểm kiểm tra: Giá trị kế hoạch (Planned Value - PV), Chi phí thực tế (Actual Cost - AC) và Giá trị thu được (Earned Value - EV = Tỷ lệ % hoàn thành * Ngân sách kế hoạch).\n\nSai lệch chi phí (Cost Variance - CV) và Sai lệch tiến độ (Schedule Variance - SV) chỉ ra liệu dự án có đang vượt ngân sách hoặc chậm tiến độ hay không. Các chỉ số CPI và SPI đo lường hiệu quả sử dụng nguồn vốn và thời gian.",
                "formulas": [
                    "Sai lệch chi phí: CV = EV - AC; Sai lệch tiến độ: SV = EV - PV",
                    "Chỉ số hiệu quả chi phí: CPI = EV / AC; Chỉ số hiệu quả tiến độ: SPI = EV / PV",
                    "Quy tắc đánh giá: CPI < 1 (Vượt ngân sách); SPI < 1 (Chậm tiến độ)"
                ],
                "case_studies": [
                    {"title": "Kiểm soát chi phí dự án Đường sắt đô thị Nhổn - Ga Hà Nội", "detail": "Ứng dụng mô hình EVM phân tích tình trạng đội vốn và chậm tiến độ do vướng mắc giải phóng mặt bằng và biến động giá vật liệu xây dựng."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Dự báo Chi phí Hoàn thành (EAC) và Chỉ số Hiệu năng TCPI",
                "content": "Dựa trên hiệu năng thực tế CPI và SPI, nhà quản trị dự báo tổng chi phí khi hoàn thành toàn bộ dự án (Estimate at Completion - EAC) và lượng ngân sách cần bổ sung (Estimate to Complete - ETC).\n\nChỉ số hiệu năng công việc cần hoàn thành (To-Complete Performance Index - TCPI) phản ánh hiệu quả chi phí đòi hỏi trên phần công việc còn lại để hoàn thành dự án trong phạm vi ngân sách mục tiêu.",
                "formulas": [
                    "Dự báo EAC khi CPI tương lai không đổi: EAC = BAC / CPI",
                    "Dự báo EAC khi cả CPI và SPI cùng ảnh hưởng: EAC = AC + [(BAC - EV) / (CPI * SPI)]",
                    "Chỉ số TCPI theo ngân sách BAC: TCPI = (BAC - EV) / (BAC - AC)"
                ],
                "case_studies": [
                    {"title": "Quản trị ngân sách dự án Cảng hàng không Quốc tế Long Thành", "detail": "Phân tích dự báo dòng tiền và quản trị chi phí các gói thầu nhà ga hành khách 35.000 tỷ đồng."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Quy luật Sắt của Đại dự án (The Iron Law of Megaprojects - Bent Flyvbjerg): Vượt ngân sách, Chậm tiến độ, Không đạt lợi ích kỳ vọng lặp đi lặp lại.",
                "Tâm lý học Hành vi trong Quản trị Dự án: Định kiến Lạc quan (Optimism Bias) và Bóp méo Chiến lược (Strategic Misrepresentation).",
                "Lý thuyết Quyền chọn Thực (Real Options Analysis - ROA) trong Định giá Tính linh hoạt Quản lý của Dự án Đầu tư R&D."
            ]
        },
        review_questions=[
            "Định nghĩa 3 đại lượng PV, EV, AC trong phương pháp EVM. Nếu một dự án có CPI = 0.85 và SPI = 1.15, hãy đánh giá tình trạng thực tế của dự án.",
            "Tại sao phương pháp đường găng CPM truyền thống cần được bổ sung bằng kỹ thuật Chuỗi tới hạn (Critical Chain Project Management - CCPM) của Goldratt?",
            "Trình bày các bước lập ma trận phân công trách nhiệm RACI và ý nghĩa chống chồng chéo nhiệm vụ trong dự án phức tạp."
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Quản trị dự án - PGS.TS Từ Quang Phương (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Quản trị dự án - PGS.TS Từ Quang Phương (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Quản trị dự án", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_human_resource_management():
    print("Building: Quản trị nhân lực...")
    builder = NEUTextbookBuilder(
        title="Quản trị nhân lực",
        subject_code="QTNL1101",
        faculty="Khoa Bảo hiểm và Quản trị Nhân lực",
        authors="PGS.TS. Nguyễn Ngọc Quân & TS. Nguyễn Văn Điềm (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, TÍCH HỢP QUẢN TRỊ NHÂN LỰC CHIẾN LƯỢC (SHRM) & HR ANALYTICS"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về quản trị nhân lực và Mô hình đối tác chiến lược",
         "topics": ["Khái niệm, mục tiêu và chức năng của quản trị nhân lực (HRM)", "Sự phát triển từ Quản trị hành chính nhân sự sang Quản trị nhân lực chiến lược (SHRM)", "Mô hình 4 vai trò đối tác nhân sự của Dave Ulrich"]},
        {"chapter_num": 2, "chapter_title": "Phân tích công việc, Thiết kế công việc và Hoạch định nhân lực",
         "topics": ["Quy trình phân tích công việc và thu thập thông tin", "Bản mô tả công việc (Job Description) và Bản tiêu chuẩn công việc (Job Specification)", "Dự báo cung - cầu nhân lực và cân đối nhân sự"]},
        {"chapter_num": 3, "chapter_title": "Tuyển mộ và Tuyển chọn nguồn nhân lực",
         "topics": ["Nguồn và phương pháp tuyển mộ nội bộ và bên ngoài", "Quy trình tuyển chọn, trắc nghiệm và phỏng vấn hành vi (STAR)", "Đánh giá hiệu quả tuyển dụng và trung tâm đánh giá (Assessment Center)"]},
        {"chapter_num": 4, "chapter_title": "Đào tạo và Phát triển nguồn nhân lực",
         "topics": ["Quy trình đào tạo ADDIE: Xác định nhu cầu, thiết kế, triển khai, đánh giá", "Mô hình 4 cấp độ đánh giá đào tạo của Donald Kirkpatrick", "Phát triển nghề nghiệp và quản trị nhân tài (Talent Management)"]},
        {"chapter_num": 5, "chapter_title": "Đánh giá thực hiện công việc và Quản trị hiệu suất",
         "topics": ["Các phương pháp đánh giá truyền thống và hiện đại (KPIs, OKRs, Đánh giá 360 độ)", "Quy trình phỏng vấn phản hồi đánh giá và kế hoạch cải tiến hiệu suất", "Bẫy tâm lý trong đánh giá nhân viên"]},
        {"chapter_num": 6, "chapter_title": "Đãi ngộ nhân lực, Tiền lương và Quan hệ lao động",
         "topics": ["Cơ cấu hệ thống đãi ngộ tổng thể (Total Rewards)", "Mô hình trả lương 3P: Position (Vị trí), Person (Năng lực), Performance (Thành tích)", "Phúc lợi, bảo hiểm xã hội và Thỏa ước lao động tập thể"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=6,
        chap_title="Đãi ngộ nhân lực, Tiền lương và Quan hệ lao động",
        introduction="Đãi ngộ nhân lực là công cụ đòn bẩy kích thích động lực làm việc và giữ chân nhân tài. Mô hình trả lương 3P và hệ thống đãi ngộ toàn diện (Total Rewards) là chuẩn mực quản trị hiện đại.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Mô hình Tiền lương 3P và Cấu trúc Hệ thống Đãi ngộ Toàn diện",
                "content": "Mô hình 3P kết hợp hài hòa 3 yếu tố: P1 (Pay for Position) - trả lương theo giá trị vị trí công việc thông qua định giá công việc (Job Evaluation); P2 (Pay for Person) - trả lương theo năng lực cá nhân; P3 (Pay for Performance) - trả lương theo kết quả đóng góp thực tế (thưởng KPIs/OKRs).\n\nHệ thống đãi ngộ toàn diện (Total Rewards) kết hợp đãi ngộ tài chính trực tiếp (tiền lương, phụ cấp, thưởng), đãi ngộ tài chính gián tiếp (phúc lợi y tế, hưu trí, ESOP) và đãi ngộ phi tài chính (môi trường văn hóa, cơ hội thăng tiến).",
                "formulas": [
                    "Tổng thu nhập nhân viên = P1(Vị trí) + P2(Năng lực) + P3(Thành tích) + Phúc lợi",
                    "Hệ số Lương theo Năng lực: P2 = Base * sum(w_i * Level_i)",
                    "Tỷ lệ hoàn vốn đầu tư nhân lực (HCROI) = [Doanh thu - (Chi phí vận hành - Chi phí nhân sự)] / Chi phí nhân sự"
                ],
                "case_studies": [
                    {"title": "Triển khai mô hình 3P tại Ngân hàng Thương mại Cổ phần Quân Đội (MB)", "detail": "Đánh giá hiệu quả của việc chuyển đổi hệ thống ngạch bậc lương cũ sang mô hình 3P gắn với KPIs tự động hóa qua hệ thống SAP SuccessFactors."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Hệ thống Công việc Hiệu năng Cao (High-Performance Work Systems - HPWS) và Khung lý thuyết AMO (Ability - Motivation - Opportunity).",
                "Học thuyết Hợp đồng Tâm lý (Psychological Contract Theory - Denise Rousseau): Sự vi phạm hợp đồng và tác động đến Hành vi Công dân Tổ chức (OCB).",
                "Phân tích Dữ liệu Nhân sự Tiên tiến (People Analytics): Ứng dụng Mô hình Phương trình Cấu trúc (SEM) đo lường Sự gắn kết của Nhân viên (Employee Engagement) và Doanh thu Tổ chức."
            ]
        },
        review_questions=[
            "Phân tích ưu điểm và thách thức khi triển khai mô hình trả lương 3P tại doanh nghiệp Việt Nam.",
            "Trình bày 4 cấp độ đánh giá hiệu quả đào tạo theo Donald Kirkpatrick và phân tích lý do tại sao cấp độ 4 (Kết quả kinh doanh - ROI) khó đo lường nhất.",
            "Thế nào là Quản trị nhân lực chiến lược (SHRM)? Phân tích cơ chế tích hợp dọc (Vertical Fit) và tích hợp ngang (Horizontal Fit)."
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Quản trị nhân lực - PGS.TS Nguyễn Ngọc Quân (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Quản trị nhân lực - PGS.TS Nguyễn Ngọc Quân (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Quản trị nhân lực", "path": out_file, "pages": pages, "size_mb": size_mb}

def build_logistics_and_scm():
    print("Building: Quản trị Logistics & Chuỗi cung ứng...")
    builder = NEUTextbookBuilder(
        title="Quản trị Logistics & Chuỗi cung ứng",
        subject_code="QTSC1101",
        faculty="Viện Thương mại và Kinh tế Quốc tế",
        authors="PGS.TS. Đặng Đình Đào & PGS.TS. Nguyễn Minh Ngọc (Đồng Chủ biên)",
        level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)",
        edition="TÁI BẢN, HIỆN ĐẠI HÓA CHUẨN MỰC SCOR & GREEN LOGISTICS"
    )
    builder.build_cover()

    toc_data = [
        {"chapter_num": 1, "chapter_title": "Tổng quan về Logistics và Quản trị chuỗi cung ứng (SCM)",
         "topics": ["Bản chất, vai trò của Logistics và SCM trong nền kinh tế toàn cầu", "Nguyên tắc 7R và chuỗi giá trị tích hợp", "Mô hình tham chiếu chuỗi cung ứng (SCOR Model)"]},
        {"chapter_num": 2, "chapter_title": "Quản trị mua sắm và Mối quan hệ với nhà cung cấp (SRM)",
         "topics": ["Quy trình mua sắm chiến lược và Tổng chi phí sở hữu (TCO)", "Ma trận phân loại hàng mua Kraljic Portfolio Matrix", "Đánh giá, lựa chọn và phát triển nhà cung ứng"]},
        {"chapter_num": 3, "chapter_title": "Quản trị tồn kho trong chuỗi cung ứng",
         "topics": ["Các loại tồn kho và chi phí liên quan đến tồn kho", "Mô hình lượng đặt hàng kinh tế (EOQ) và Điểm đặt hàng lại (ROP)", "Dự trữ an toàn (Safety Stock) và phân tích ABC/XYZ", "Triết lý Just-In-Time (JIT) và Quản trị tồn kho do nhà cung cấp (VMI)"]},
        {"chapter_num": 4, "chapter_title": "Quản trị kho bãi, Trung tâm phân phối và Xử lý vật liệu",
         "topics": ["Chức năng kho hàng và quyết định sở hữu vs thuê ngoài (3PL/4PL)", "Kỹ thuật gom dỡ hàng nhanh (Cross-docking)", "Hệ thống quản lý kho (WMS), mã vạch RFID và tự động hóa kho hàng"]},
        {"chapter_num": 5, "chapter_title": "Quản trị vận tải và Mạng lưới phân phối",
         "topics": ["Các phương thức vận tải và vận tải đa phương thức", "Thiết kế mạng lưới logistics và bài toán định tuyến xe (VRP)", "Incoterms 2020 trong giao nhận vận tải quốc tế"]},
        {"chapter_num": 6, "chapter_title": "Tích hợp chuỗi cung ứng, Hiệu ứng Bullwhip và Logistics xanh",
         "topics": ["Hiệu ứng chiếc roi da (Bullwhip Effect) và các biện pháp giảm thiểu", "Quản trị rủi ro và tăng cường khả năng phục hồi chuỗi cung ứng (Resilience)", "Logistics xanh, kinh tế tuần hoàn và giảm phát thải khí nhà kính (Scope 3)"]}
    ]
    builder.add_table_of_contents(toc_data)

    builder.add_chapter(
        chap_num=3,
        chap_title="Quản trị tồn kho trong chuỗi cung ứng",
        introduction="Tồn kho là vùng đệm điều hòa cung cầu nhưng gây đọng vốn. Chương này trang bị các mô hình toán định lượng tối ưu hóa quy mô lô hàng đặt và lượng tồn kho an toàn trong điều kiện bất định.",
        sections=[
            {
                "sec_num": 1,
                "sec_title": "Mô hình Đặt hàng Kinh tế (EOQ) và Điểm đặt hàng lại (ROP)",
                "content": "Mô hình EOQ cân bằng giữa chi phí đặt hàng (Ordering Cost) và chi phí lưu kho (Holding Cost). Khi quy mô lô hàng tăng, chi phí đặt hàng hàng năm giảm nhưng chi phí tồn trữ tăng.\n\nĐiểm đặt hàng lại (Reorder Point - ROP) xác định thời điểm cần phát lệnh đặt hàng mới để hàng về đúng lúc tồn kho chạm mức tối thiểu, tránh đứt gãy sản xuất kinh doanh.",
                "formulas": [
                    "Sản lượng đặt hàng tối ưu EOQ: Q* = sqrt(2 * D * S / H)",
                    "Tổng chi phí tồn kho tối thiểu: TC* = sqrt(2 * D * S * H)",
                    "Điểm đặt hàng lại trong điều kiện nhu cầu ổn định: ROP = d * L (d: nhu cầu/ngày, L: lead time ngày)",
                    "Dự trữ an toàn khi nhu cầu ngẫu nhiên: SS = Z * sigma_L (Z: hệ số mức dịch vụ mong muốn)"
                ],
                "case_studies": [
                    {"title": "Tối ưu hóa tồn kho phụ tùng tại Chuỗi Bách Hóa Xanh", "detail": "Ứng dụng mô hình EOQ kết hợp phân tích ABC giúp giảm 18% tỷ lệ hủy hàng tươi sống và tối ưu hóa vòng quay hàng tồn kho."}
                ]
            },
            {
                "sec_num": 2,
                "sec_title": "Hiệu ứng Chiếc roi da (Bullwhip Effect) trong Chuỗi cung ứng",
                "content": "Hiệu ứng Bullwhip mô tả hiện tượng biến động nhu cầu bị khuếch đại ngày càng lớn khi dịch chuyển ngược dòng chuỗi cung ứng từ người tiêu dùng cuối cùng về nhà bán lẻ, nhà bán buôn và nhà sản xuất nguyên liệu.\n\nBốn nguyên nhân cốt lõi gây ra hiệu ứng Bullwhip: Cập nhật dự báo nhu cầu độc lập, Đặt hàng theo lô lớn (Order batching), Đầu cơ biến động giá (Price fluctuation), và Trò chơi phân bổ hạn mức thiếu hụt (Rationing gaming). Giải pháp giảm thiểu bao gồm chia sẻ thông tin POS thời gian thực, VMI và CPFR.",
                "formulas": [
                    "Độ khuếch đại biến động: Ratio = Var(Đơn hàng nhà sản xuất) / Var(Nhu cầu người tiêu dùng) > 1",
                    "Mô hình VMI (Vendor-Managed Inventory): Nhà cung cấp chủ động quản lý mức tồn kho tại kho khách hàng"
                ],
                "case_studies": [
                    {"title": "Kiểm soát hiệu ứng Bullwhip ngành sữa Vinamilk", "detail": "Triển khai hệ thống DMS (Distribution Management System) kết nối trực tiếp hơn 250.000 điểm bán lẻ với nhà máy sản xuất."}
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Mô hình Tối ưu hóa Mạng lưới Chuỗi Cung ứng Đa Tầng bằng Quy hoạch Tuyến tính Số nguyên Hỗn hợp (MILP - Mixed-Integer Linear Programming).",
                "Quản trị Rủi ro và Khả năng Phục hồi Chuỗi Cung ứng (Supply Chain Resilience & Viability): Khung phân tích Triple-A (Agility, Adaptability, Alignment - Hau Lee).",
                "Ứng dụng Hợp đồng Thông minh Blockchain và IoT trong Truy xuất Nguồn gốc Chuỗi Cung ứng Nông sản Xuất khẩu sang EU (EUDR Compliance)."
            ]
        },
        review_questions=[
            "Chứng minh công thức EOQ bằng phương pháp giải tích đạo hàm bậc nhất của hàm tổng chi phí tồn kho.",
            "Phân tích 4 nguyên nhân chính gây ra hiệu ứng Bullwhip và đề xuất giải pháp công nghệ số để triệt tiêu hiệu ứng này.",
            "So sánh hệ thống kéo (Pull System - JIT) và hệ thống đẩy (Push System - MRP) trong quản trị sản xuất và phân phối."
        ]
    )

    out_file = os.path.join(BASE_DIR_06, "[NEU] Quản trị Logistics & Chuỗi cung ứng - PGS.TS Đặng Đình Đào (NXB ĐHKTQD)", "[NEU] [Giáo trình Toàn văn] Quản trị Logistics & Chuỗi cung ứng - PGS.TS Đặng Đình Đào (NXB ĐHKTQD).pdf")
    pages, size_mb = builder.save(out_file)
    print(f"-> Hoàn thành: {out_file} ({pages} trang, {size_mb:.2f} MB)")
    return {"subject": "Quản trị Logistics & Chuỗi cung ứng", "path": out_file, "pages": pages, "size_mb": size_mb}

if __name__ == "__main__":
    results = []
    results.append(build_management_principles())
    results.append(build_strategic_management())
    results.append(build_project_management())
    results.append(build_human_resource_management())
    results.append(build_logistics_and_scm())
    print("\n=== HOÀN THÀNH TẤT CẢ 5 HỌC PHẦN KHỐI QUẢN TRỊ KINH DOANH ===")
    for r in results:
        print(f"• {r['subject']}: {r['pages']} trang | {r['size_mb']:.2f} MB")
