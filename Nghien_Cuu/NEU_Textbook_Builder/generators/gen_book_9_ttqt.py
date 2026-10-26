# -*- coding: utf-8 -*-
"""
Generator for Textbook 9:
[NEU] Thanh toán quốc tế - PGS.TS Nguyễn Thị Tường Anh (NXB ĐHKTQD)
"""
import sys
import os

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
from neu_engine import NEUTextbookBuilder

def build_ttqt():
    title = "Thanh toán quốc tế"
    subject_code = "TTQT1102"
    faculty = "Viện Ngân hàng - Tài chính / Khoa Kinh tế quốc tế"
    authors = "PGS.TS. Nguyễn Thị Tường Anh & TS. Nguyễn Văn Tiến (Đồng Chủ biên)"
    
    out_dir = r"C:\Users\Admin\Desktop\Giáo trình Kinh tế\05_Tài chính Quốc tế\[NEU] Thanh toán quốc tế - PGS.TS Nguyễn Thị Tường Anh (NXB ĐHKTQD)"
    out_pdf = os.path.join(out_dir, "[NEU] [Giáo trình Toàn văn] Thanh toán quốc tế - PGS.TS Nguyễn Thị Tường Anh (NXB ĐHKTQD).pdf")
    
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
            "chapter_title": "Tổng quan về Thanh toán Quốc tế và Điều kiện Thương mại Incoterms 2020",
            "topics": [
                "Khái niệm, đặc điểm và vai trò của thanh toán quốc tế trong chuỗi cung ứng toàn cầu",
                "Hệ thống viễn thông liên ngân hàng tài chính quốc tế SWIFT (Cấu trúc điện MT103, MT202, MT700 và chuẩn ISO 20022 MX)",
                "Quy tắc Incoterms 2020 của Phòng Thương mại Quốc tế (ICC): Phân chia rủi ro, chi phí và trách nhiệm giữa người bán và người mua (EXW, FOB, CFR, CIF, CPT, CIP, DAP, DDP)",
                "Chuyên đề Tiến sĩ: Bất cân xứng Thông tin và Xung đột Lợi ích trong Hợp đồng Ngoại thương Xuyên Biên giới"
            ]
        },
        {
            "chapter_num": "2",
            "chapter_title": "Phương tiện Thanh toán Quốc tế và Bộ Chứng từ Thương mại",
            "topics": [
                "Công cụ tài chính: Hối phiếu thương mại (Bill of Exchange theo Luật ULB 1930), Kỳ phiếu (Promissory Note) và Séc quốc tế",
                "Bộ chứng từ hàng hóa: Hóa đơn thương mại (Commercial Invoice), Phiếu đóng gói (Packing List), Chứng nhận xuất xứ (C/O)",
                "Chứng từ vận tải: Vận đơn đường biển (Ocean Bill of Lading - B/L), Vận đơn hàng không (AWB) và Chứng từ bảo hiểm hàng hóa",
                "Chuyên đề Tiến sĩ: Tính chất Trừu tượng và Lưu thông của Công cụ Chuyển nhượng (Negotiable Instruments Law)"
            ]
        },
        {
            "chapter_num": "3",
            "chapter_title": "Các Phương thức Thanh toán Quốc tế Cơ bản: Chuyển tiền và Nhờ thu",
            "topics": [
                "Phương thức Chuyển tiền quốc tế (Remittance): Chuyển tiền bằng điện (T/T), Chuyển tiền trả trước vs Trả sau, Rủi ro đối tác",
                "Phương thức Nhờ thu (Collection of Payment) theo Quy tắc Thống nhất về Nhờ thu URC 522 của ICC",
                "Nhờ thu phiếu trơn (Clean Collection) và Nhờ thu kèm chứng từ (Documentary Collection: D/P trả ngay, D/A chấp nhận hối phiếu)",
                "Chuyên đề Tiến sĩ: Lý thuyết Trò chơi trong Lựa chọn Phương thức Thanh toán Ngoại thương giữa Xuất khẩu và Nhập khẩu"
            ]
        },
        {
            "chapter_num": "4",
            "chapter_title": "Phương thức Tín dụng Chứng từ (L/C) và Tập quán UCP 600, ISBP 745",
            "topics": [
                "Bản chất độc lập của L/C: Cam kết trả tiền có điều kiện không thể hủy ngang của Ngân hàng Phát hành (Issuing Bank)",
                "Các loại L/C phổ biến: L/C xác nhận (Confirmed L/C), L/C chuyển nhượng (Transferable L/C), L/C giáp lưng (Back-to-Back L/C), L/C tuần hoàn",
                "Quy tắc Thống nhất Thực hành Tín dụng Chứng từ UCP 600 và Tiêu chuẩn Kiểm tra Chứng từ Thực hành Ngân hàng Quốc tế ISBP 745",
                "Quy trình kiểm tra chứng từ theo nguyên tắc 'Phù hợp bề mặt nghiêm ngặt' (Strict Compliance)",
                "Chuyên đề Tiến sĩ: Ngoại lệ Gian lận trong L/C (Fraud Exception Rule) và Án lệ Quốc tế"
            ]
        },
        {
            "chapter_num": "5",
            "chapter_title": "Bảo lãnh Quốc tế, Thư Tín dụng Dự phòng và Tài trợ Thương mại (Trade Finance)",
            "topics": [
                "Bảo lãnh ngân hàng độc lập theo Quy tắc URDG 758: Bảo lãnh dự thầu, Bảo lãnh thực hiện hợp đồng, Bảo lãnh hoàn trả tiền ứng trước",
                "Thư tín dụng dự phòng (Standby L/C) theo Quy tắc ISP98",
                "Các sản phẩm tài trợ thương mại hiện đại: Bao thanh toán quốc tế (Factoring theo GRIF), Chiết khấu miễn truy đòi (Forfaiting), Tài trợ chuỗi cung ứng (SCF)",
                "Chuyên đề Tiến sĩ: Ứng dụng Blockchain / Hợp đồng Thông minh (Smart Contracts) trong Thanh toán Quốc tế và Tuân thủ Chống rửa tiền (AML/CFT)"
            ]
        }
    ]
    b.add_table_of_contents(toc_data)
    
    # Chapter 1
    b.add_chapter(
        chap_num="1",
        chap_title="Tổng quan về Thanh toán Quốc tế và Điều kiện Thương mại Incoterms 2020",
        introduction="Chương 1 trang bị kiến thức nền tảng về hệ thống thanh toán quốc tế, chuẩn mạng điện Swift liên ngân hàng và giải mã chi tiết các điều kiện cơ sở giao hàng Incoterms 2020 của Phòng Thương mại Quốc tế (ICC).",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bản chất của thanh toán quốc tế và mạng lưới SWIFT",
                "content": (
                    "Thanh toán quốc tế là quá trình thực hiện các nghĩa vụ chi trả và quyền lợi tài chính phát sinh từ các hoạt động thương mại, "
                    "đầu tư, dịch vụ giữa các chủ thể ở các quốc gia khác nhau thông qua hệ thống ngân hàng trung gian. "
                    "Khác với thanh toán nội địa, thanh toán quốc tế bị chi phối bởi các hệ thống luật pháp khác nhau, "
                    "tồn tại rủi ro tỷ giá, rủi ro quốc gia và rủi ro bất tín nhiệm giữa các bên cách xa nhau về mặt địa lý.\n\n"
                    "Mạng lưới SWIFT (Society for Worldwide Interbank Financial Telecommunication) kết nối hơn 11,000 định chế tài chính tại hơn 200 quốc gia. "
                    "Hệ thống điện chuẩn hóa gồm các nhóm điện: Nhóm 1 (Điện chuyển tiền khách hàng MT103), Nhóm 2 (Chuyển tiền liên ngân hàng MT202), "
                    "Nhóm 4 (Nhờ thu MT400), Nhóm 7 (Tín dụng chứng từ MT700, MT707) và đang chuyển đổi toàn diện sang chuẩn dữ liệu ISO 20022 XML (MX)."
                ),
                "formulas": [
                    "Cấu trúc Mã định danh ngân hàng BIC/SWIFT Code: 8 hoặc 11 ký tự (4 ký tự tên ngân hàng, 2 ký tự quốc gia, 2 ký tự địa phương, 3 ký tự chi nhánh)",
                    "Nguyên tắc chuyển đổi ISO 20022: pacs.008 thay thế MT103, pacs.009 thay thế MT202"
                ],
                "case_studies": [
                    {
                        "title": "Vai trò của hệ thống thanh toán SWIFT và rủi ro bị ngắt kết nối",
                        "detail": "Việc các ngân hàng Nga bị loại khỏi hệ thống SWIFT năm 2022 đã làm tê liệt các giao dịch thương mại xuyên biên giới, thúc đẩy các quốc gia đẩy mạnh nghiên cứu các hệ thống thanh toán thay thế độc lập (như CIPS của Trung Quốc và SPFS của Nga)."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Giải mã Quy tắc Thương mại Quốc tế Incoterms 2020",
                "content": (
                    "Incoterms do Phòng Thương mại Quốc tế (ICC) ban hành nhằm chuẩn hóa điểm chuyển giao rủi ro, phân chia chi phí vận tải, bảo hiểm "
                    "và nghĩa vụ làm thủ tục hải quan xuất nhập khẩu giữa người bán và người mua trong hợp đồng ngoại thương. "
                    "Incoterms 2020 gồm 11 điều kiện, chia làm hai nhóm: "
                    "Nhóm áp dụng cho mọi phương thức vận tải (EXW, FCA, CPT, CIP, DAP, DPU, DDP); và Nhóm chỉ áp dụng cho vận tải biển và đường thủy nội địa (FAS, FOB, CFR, CIF).\n\n"
                    "Điểm mới quan trọng của Incoterms 2020: Nâng mức bảo hiểm mặc định của điều kiện CIP lên mức tối đa ICC (A); "
                    "thay thế DAT bằng DPU (Giao tại địa điểm dỡ hàng); và bổ sung tùy chọn cấp vận đơn B/L có ghi chú 'On Board' cho người bán trong điều kiện FCA."
                ),
                "formulas": [
                    "Quan hệ cấu thành giá xuất khẩu: Giá CIF = Giá FOB + Cước vận tải đường biển (F) + Phí bảo hiểm hàng hải (I)",
                    "Phân bổ chi phí và rủi ro: Trong FOB/CFR/CIF, rủi ro chuyển giao từ người bán sang người mua ngay khi hàng được xếp an toàn lên tàu tại cảng bốc hàng."
                ],
                "case_studies": [
                    {
                        "title": "Thói quen xuất FOB - nhập CIF của các doanh nghiệp xuất nhập khẩu Việt Nam",
                        "detail": "Hơn 80% doanh nghiệp xuất khẩu Việt Nam lựa chọn điều kiện giao hàng FOB (để đối tác ngoại tự thuê tàu và mua bảo hiểm) khiến ngành vận tải biển và bảo hiểm nội địa mất đi nguồn doanh thu khổng lồ, đặt ra yêu cầu phải chuyển dần sang xuất khẩu giá CIF."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Hợp đồng Ngoại thương Không hoàn hảo (Incomplete Contracts) của Grossman, Hart & Moore trong bối cảnh tranh chấp chuỗi cung ứng toàn cầu.",
                "Mô hình Lựa chọn Điều kiện Giao hàng Incoterms: Phân tích đánh đổi giữa Chi phí Giao dịch (Transaction Costs) và Sức mạnh Đàm phán Thị trường.",
                "Rủi ro Cấm vận Địa chính trị (Geopolitical Sanctions) và Tuân thủ Tuân thủ Quy định Cấm vận Quốc tế (OFAC / EU Sanctions Screening)."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt cốt lõi giữa hai điều kiện giao hàng CIF và CIP trong Incoterms 2020 về phạm vi bảo hiểm và phương thức vận tải?",
            "Tại sao trong điều kiện CFR và CIF, người bán chịu chi phí vận chuyển đến cảng đến nhưng rủi ro tổn thất hàng hóa lại chuyển sang người mua ngay tại cảng bốc hàng?",
            "Trình bày cấu trúc bức điện chuẩn MT700 mở thư tín dụng chứng từ trên mạng SWIFT và giải thích ý nghĩa của trường 40A (Form of Documentary Credit)?"
        ]
    )
    
    # Chapter 2
    b.add_chapter(
        chap_num="2",
        chap_title="Phương tiện Thanh toán Quốc tế và Bộ Chứng từ Thương mại",
        introduction="Chương 2 phân tích cơ sở pháp lý của các công cụ chuyển nhượng nợ và chuẩn mực kiểm tra tính hợp lệ của bộ chứng từ thương mại quốc tế theo tập quán ngân hàng toàn cầu.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Hối phiếu thương mại và công cụ chuyển nhượng",
                "content": (
                    "Hối phiếu thương mại (Bill of Exchange / Draft) là mệnh lệnh trả tiền vô điều kiện bằng văn bản do một người (Người ký phát - Drawer) "
                    "lập cho một người khác (Người bị ký phát - Drawee), yêu cầu người này khi nhìn thấy hối phiếu hoặc tại một ngày xác định trong tương lai "
                    "phải trả một số tiền nhất định cho một người thứ ba (Người thụ hưởng - Payee) hoặc theo lệnh của người này.\n\n"
                    "Hối phiếu có ba đặc tính pháp lý tuyệt đối: Tính trừu tượng (tách rời khỏi hợp đồng thương mại cơ sở); "
                    "Tính bắt buộc trả tiền (người bị ký phát sau khi ký chấp nhận phải trả tiền vô điều kiện); và Tính lưu thông (có thể chuyển nhượng tự do bằng thủ tục ký phát - Endorsement)."
                ),
                "formulas": [
                    "Các loại ký hậu hối phiếu: Ký hậu để trắng (Blank Endorsement), Ký hậu theo lệnh (Order Endorsement), Ký hậu hạn chế (Restrictive Endorsement)",
                    "Luật điều chỉnh hối phiếu: Luật Thống nhất về Hối phiếu Geneva 1930 (ULB) và Luật Hối phiếu Anh 1882 (BEA)"
                ],
                "case_studies": [
                    {
                        "title": "Nghiệp vụ chiết khấu hối phiếu xuất khẩu tại các NHTM Việt Nam",
                        "detail": "Các ngân hàng thương mại nhận chiết khấu miễn truy đòi đối với các hối phiếu kỳ hạn đã được các ngân hàng uy tín quốc tế chấp nhận thanh toán, cung cấp nguồn vốn lưu động tức thì cho doanh nghiệp xuất khẩu thủy sản và dệt may."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Bộ chứng từ hàng hóa và chứng từ vận tải quốc tế",
                "content": (
                    "Trong thanh toán quốc tế, các ngân hàng giao dịch dựa trên chứng từ chứ không giao dịch bằng hàng hóa. "
                    "Bộ chứng từ xuất nhập khẩu chuẩn bao gồm: Hóa đơn thương mại (Commercial Invoice - mô tả chính xác hàng hóa, đơn giá và tổng giá trị); "
                    "Phiếu đóng gói (Packing List - chi tiết quy cách đóng gói, trọng lượng tịnh Net Weight và trọng lượng cả bì Gross Weight); "
                    "Giấy chứng nhận xuất xứ (Certificate of Origin - C/O form AK, EV, D để hưởng thuế quan ưu đãi FTA);\n\n"
                    "Chứng từ vận tải then chốt là Vận đơn đường biển (Bill of Lading - B/L), đóng ba chức năng pháp lý: "
                    "1. Biên lai nhận hàng của người chuyên chở; 2. Bằng chứng của hợp đồng vận tải đường biển; 3. Chứng từ sở hữu hàng hóa (Document of Title cho phép định đoạt chuyển nhượng hàng)."
                ),
                "formulas": [
                    "Điều kiện B/L hợp lệ theo UCP 600: Clean Bill of Lading (Vận đơn hoàn hảo không có ghi chú khuyết tật bao bì), Shipped on Board (Đã bốc hàng lên tàu)",
                    "Ký hậu B/L: To Order of Shipper ký hậu để trắng cho phép người cầm vận đơn gốc được quyền nhận hàng tại cảng dỡ"
                ],
                "case_studies": [
                    {
                        "title": "Rủi ro mất quyền kiểm soát hàng do phát hành vận đơn Surrendered B/L",
                        "detail": "Một doanh nghiệp xuất khẩu hạt điều Việt Nam đồng ý giao hàng bằng điện giao hàng (Surrendered B/L) trước khi nhận đủ tiền thanh toán qua T/T, dẫn tới bị đối tác nước ngoài chiếm đoạt hàng hóa mà không thanh toán tiền."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Pháp lý về Quyền Sở hữu Chứng từ (Lex Mercatoria và Document of Title Doctrine): So sánh Hệ thống Thông luật (Common Law) và Dân luật (Civil Law) về Chuyển quyền Sở hữu Vận đơn.",
                "Chuyển đổi số Chứng từ Ngoại thương: Luật Mẫu UNCITRAL về Bản ghi Điện tử có Thể Chuyển nhượng (MLETR 2017) và Vận đơn Đường biển Điện tử (e-B/L).",
                "Mô hình Kinh tế lượng Lượng hóa Lợi ích Thuế quan Ưu đãi của Giấy Chứng nhận Xuất xứ (C/O Utilization Rates) trong các Hiệp định RCEP và CPTPP."
            ]
        },
        review_questions=[
            "Phân tích ba đặc tính pháp lý cốt lõi của hối phiếu thương mại theo Luật Thống nhất Geneva (ULB 1930)?",
            "Trình bày ba chức năng pháp lý của Vận đơn đường biển (Ocean Bill of Lading) và giải thích tại sao Vận đơn hàng không (AWB) không phải là chứng từ sở hữu hàng hóa?",
            "Thế nào là một vận đơn hoàn hảo (Clean Bill of Lading) theo quy định của Điều 27 UCP 600?"
        ]
    )
    
    # Chapter 3
    b.add_chapter(
        chap_num="3",
        chap_title="Các Phương thức Thanh toán Quốc tế Cơ bản: Chuyển tiền và Nhờ thu",
        introduction="Chương 3 phân tích quy trình nghiệp vụ, cơ cấu rủi ro và điều kiện áp dụng của các phương thức thanh toán chuyển tiền quốc tế và phương thức nhờ thu theo cẩm nang URC 522 của ICC.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Phương thức Chuyển tiền quốc tế (Remittance)",
                "content": (
                    "Chuyển tiền quốc tế là phương thức mà trong đó khách hàng (Người trả tiền / Nhà nhập khẩu) yêu cầu ngân hàng phục vụ mình "
                    "trích tiền từ tài khoản để chuyển cho người thụ hưởng (Nhà xuất khẩu) ở nước ngoài qua hệ thống viễn thông SWIFT (T/T - Telegraphic Transfer). "
                    "Hai hình thức thực hiện: Chuyển tiền trả trước (T/T in Advance: Nhà xuất khẩu nhận tiền trước rồi mới giao hàng - rủi ro tuyệt đối thuộc về nhà nhập khẩu); "
                    "và Chuyển tiền trả sau (T/T in Arrears: Nhà nhập khẩu nhận hàng trước rồi mới chuyển tiền - rủi ro tuyệt đối thuộc về nhà xuất khẩu).\n\n"
                    "Phương thức này chỉ nên áp dụng giữa các công ty mẹ - con trong cùng tập đoàn hoặc các đối tác làm ăn lâu năm có uy tín tuyệt đối."
                ),
                "formulas": [
                    "Quy trình T/T: Ký hợp đồng -> Giao hàng / Nhận hàng -> Lập lệnh chuyển tiền (Application for Fund Transfer) -> Phát điện SWIFT MT103 -> Báo Có tài khoản người thụ hưởng"
                ],
                "case_studies": [
                    {
                        "title": "Rủi ro lừa đảo hacker xâm nhập email thay đổi tài khoản nhận tiền T/T",
                        "detail": "Nhiều doanh nghiệp xuất nhập khẩu Việt Nam bị hacker tấn công hộp thư điện tử giả mạo đối tác, gửi thông báo thay đổi số tài khoản thụ hưởng sang một ngân hàng thứ ba, gây thiệt hại hàng trăm nghìn USD."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Phương thức Nhờ thu theo Quy tắc URC 522",
                "content": (
                    "Phương thức Nhờ thu (Collection of Payment) là phương thức mà sau khi hoàn thành nghĩa vụ giao hàng, "
                    "người xuất khẩu ủy thác cho ngân hàng phục vụ mình thu hộ tiền từ người nhập khẩu căn cứ vào hối phiếu và bộ chứng từ. "
                    "Toàn bộ quy trình tuân thủ Quy tắc Thống nhất về Nhờ thu (URC 522 của ICC). "
                    "Hai hình thức nhờ thu: Nhờ thu phiếu trơn (Clean Collection - ngân hàng chỉ thu hộ hối phiếu không kèm chứng từ giao hàng, rủi ro cực cao); "
                    "và Nhờ thu kèm chứng từ (Documentary Collection).\n\n"
                    "Nhờ thu kèm chứng từ gồm hai điều kiện giao chứng từ: "
                    "D/P (Documents Against Payment - Giao chứng từ khi thanh toán tiền mặt ngay); và D/A (Documents Against Acceptance - Giao chứng từ khi người mua ký chấp nhận hối phiếu kỳ hạn)."
                ),
                "formulas": [
                    "Rủi ro phương thức nhờ thu: Ngân hàng chỉ đóng vai trò trung gian thu hộ chứng từ, TUYỆT ĐỐI KHÔNG CHỊU TRÁCH NHIỆM BẢO ĐẢM THANH TOÁN nếu nhà nhập khẩu từ chối nhận hàng hoặc từ chối trả tiền.",
                    "So sánh D/P vs D/A: D/P an toàn hơn cho người bán vì người mua phải trả tiền mới lấy được bộ chứng từ gốc để đi nhận hàng."
                ],
                "case_studies": [
                    {
                        "title": "Vụ lừa đảo 100 container hạt điều xuất khẩu sang Ý năm 2022",
                        "detail": "Các doanh nghiệp Việt Nam xuất khẩu hạt điều áp dụng phương thức nhờ thu D/P qua ngân hàng Ý, nhưng đối tác lừa đảo đã dùng thủ đoạn tinh vi chiếm đoạt bộ chứng từ gốc trong quá trình chuyển phát nhanh quốc tế để nhận hàng tại cảng trước khi ngân hàng thu tiền."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Lý thuyết Trò chơi Thanh toán Thương mại: Ma trận Trả thưởng giữa Chuyển tiền Trả trước, Chuyển tiền Trả sau, Nhờ thu D/P và L/C trong Điều kiện Cạnh tranh Không hoàn hảo.",
                "Rủi ro Tín dụng Đối tác (Counterparty Credit Risk) trong Tài trợ Ngoại thương: Mô hình Ước lượng Tác động của Thể chế Pháp lý Quốc gia Người Nhập khẩu (Rule of Law Index) đến Lựa chọn Phương thức Thanh toán.",
                "Chi phí Vốn Tài trợ Chuỗi Cung ứng và Tối ưu hóa Dòng tiền Doanh nghiệp Xuất nhập khẩu."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt căn bản về rủi ro giữa điều kiện nhờ thu D/P (Documents Against Payment) và D/A (Documents Against Acceptance)?",
            "Trách nhiệm pháp lý của các ngân hàng tham gia phương thức nhờ thu theo quy định của URC 522 là gì?",
            "Tại sao phương thức chuyển tiền T/T trả sau lại được các nhà nhập khẩu ưa chuộng nhất nhưng lại là phương thức rủi ro nhất đối với nhà xuất khẩu?"
        ]
    )
    
    # Chapter 4
    b.add_chapter(
        chap_num="4",
        chap_title="Phương thức Tín dụng Chứng từ (L/C) và Tập quán UCP 600, ISBP 745",
        introduction="Chương 4 là trọng tâm của môn học, phân tích chuyên sâu phương thức Tín dụng chứng từ (Letter of Credit - L/C), nguyên tắc cam kết độc lập của ngân hàng phát hành và kỹ thuật kiểm tra chứng từ theo UCP 600 và ISBP 745.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bản chất pháp lý và các bên tham gia phương thức L/C",
                "content": (
                    "Thư tín dụng (L/C) là văn bản cam kết trả tiền không thể hủy ngang của Ngân hàng Phát hành (Issuing Bank) theo yêu cầu của Người xin mở L/C (Nhà nhập khẩu), "
                    "cam kết sẽ trả một số tiền nhất định cho Người thụ hưởng (Nhà xuất khẩu) nếu người này xuất trình được một bộ chứng từ hợp lệ, "
                    "phù hợp hoàn toàn với các điều khoản và điều kiện quy định trong thư tín dụng.\n\n"
                    "Hai nguyên tắc pháp lý tối thượng chi phối L/C: "
                    "1. Nguyên tắc Độc lập (Independence Principle theo Điều 4 UCP 600): L/C hoàn toàn độc lập và tách biệt khỏi hợp đồng ngoại thương cơ sở; "
                    "2. Nguyên tắc Giao dịch Chứng từ (Documentary Principle theo Điều 5 UCP 600): Các bên liên quan chỉ giao dịch trên cơ sở chứng từ, không giao dịch bằng hàng hóa thực tế."
                ),
                "formulas": [
                    "Các bên tham gia L/C: Applicant (Người mở), Issuing Bank (Ngân hàng phát hành), Advising Bank (Ngân hàng thông báo), Beneficiary (Người thụ hưởng), Confirming Bank (Ngân hàng xác nhận nếu có)",
                    "Thời hạn kiểm tra chứng từ: Ngân hàng có tối đa 5 ngày làm việc ngân hàng tiếp sau ngày xuất trình để kiểm tra và quyết định chấp nhận hay từ chối thanh toán (Điều 14b UCP 600)"
                ],
                "case_studies": [
                    {
                        "title": "Bảo lãnh L/C xác nhận đối với các thị trường có rủi ro chính trị cao",
                        "detail": "Khi doanh nghiệp Việt Nam xuất khẩu gạo sang các nước châu Phi, họ yêu cầu L/C phải được xác nhận (Confirmed L/C) bởi một ngân hàng hàng đầu châu Âu (như BNP Paribas, Deutsche Bank) để triệt tiêu hoàn toàn rủi ro vỡ nợ của ngân hàng phát hành nội địa."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Tập quán kiểm tra chứng từ theo UCP 600 và ISBP 745",
                "content": (
                    "Nguyên tắc kiểm tra chứng từ là 'Phù hợp bề mặt' (Strict Compliance): Dữ liệu trên chứng từ không được mâu thuẫn với dữ liệu trên chính chứng từ đó, "
                    "với các chứng từ khác được quy định trong L/C và với quy định của UCP 600. "
                    "Tập quán Quốc tế về Kiểm tra Chứng từ Thực hành Ngân hàng ISBP 745 diễn giải chi tiết các tình huống sai sót: "
                    "Lỗi chính tả không làm sai lệch ý nghĩa không bị coi là bất hợp lệ; tên hàng trên hóa đơn thương mại phải khớp hoàn toàn với mô tả hàng trong L/C, "
                    "trong khi trên các chứng từ khác có thể mô tả chung chung miễn không mâu thuẫn.\n\n"
                    "Khi phát hiện chứng từ bất hợp lệ (Discrepancies), Ngân hàng Phát hành có quyền từ chối thanh toán bằng cách phát điện thông báo từ chối (MT734) "
                    "nêu rõ toàn bộ các lỗi phát hiện trong thời hạn 5 ngày làm việc."
                ),
                "formulas": [
                    "Dung sai số lượng và giá trị: Cho phép dung sai +/- 5% đối với số lượng hàng rời không đóng bao, và cho phép dung sai +/- 10% nếu có từ 'About' hoặc 'Approximately' (Điều 30 UCP 600)"
                ],
                "case_studies": [
                    {
                        "title": "Bị từ chối thanh toán L/C do chứng từ bất hợp lệ",
                        "detail": "Một doanh nghiệp xuất khẩu thủy sản bị ngân hàng Hàn Quốc từ chối thanh toán lô hàng 800,000 USD do ngày phát hành chứng thư bảo hiểm sau ngày bốc hàng lên tàu trên vận đơn đường biển, vi phạm nghiêm trọng Điều 28e UCP 600."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Ngoại lệ Gian lận trong L/C (Fraud Exception Rule): Nguyên tắc Sztejn v. J. Henry Schroder Banking Corp (1941) và Tiêu chuẩn Bằng chứng Gian lận Rõ ràng (Clear and Egregious Fraud) để Tòa án ban hành Lệnh Cấm Thanh toán (Injunction).",
                "Chuyển đổi Chuẩn mực L/C Điện tử: eUCP phiên bản 2.0 và Khung Pháp lý Hợp đồng Thông minh Tự động Kích hoạt Thanh toán (Smart L/C).",
                "Khoảng trống Tài trợ Thương mại Toàn cầu (Global Trade Finance Gap theo Báo cáo ADB) và Rào cản Tiếp cận L/C của Doanh nghiệp Vừa và Nhỏ (SMEs)."
            ]
        },
        review_questions=[
            "Phân tích nguyên tắc tính độc lập của Thư tín dụng chứng từ (L/C) theo quy định của Điều 4 UCP 600?",
            "Trình bày quy trình xử lý của Ngân hàng Phát hành khi bộ chứng từ xuất trình có điểm bất hợp lệ (Discrepancy) theo Điều 16 UCP 600?",
            "Phân tích án lệ kinh điển Sztejn (1941) và chỉ ra các điều kiện để Tòa án có thể can thiệp đình chỉ nghĩa vụ thanh toán L/C của ngân hàng phát hành?"
        ]
    )
    
    # Chapter 5
    b.add_chapter(
        chap_num="5",
        chap_title="Bảo lãnh Quốc tế, Thư Tín dụng Dự phòng và Tài trợ Thương mại (Trade Finance)",
        introduction="Chương 5 hoàn thiện các sản phẩm dịch vụ ngân hàng quốc tế cao cấp: Bảo lãnh ngân hàng theo URDG 758, Thư tín dụng dự phòng (Standby L/C) và các kỹ thuật tài trợ chuỗi cung ứng hiện đại.",
        sections=[
            {
                "sec_num": "1",
                "sec_title": "Bảo lãnh ngân hàng quốc tế và Standby L/C",
                "content": (
                    "Bảo lãnh ngân hàng quốc tế độc lập (Independent Demand Guarantee) là cam kết bằng văn bản của ngân hàng phát hành "
                    "cam kết trả tiền cho người thụ hưởng ngay khi nhận được văn bản yêu cầu đòi tiền hợp lệ kèm theo tuyên bố người được bảo lãnh vi phạm nghĩa vụ hợp đồng. "
                    "Quy tắc Thống nhất về Bảo lãnh Yêu cầu URDG 758 của ICC là chuẩn mực toàn cầu chi phối nghiệp vụ này. "
                    "Các loại bảo lãnh phổ biến: Bảo lãnh dự thầu (Bid Bond), Bảo lãnh thực hiện hợp đồng (Performance Bond), "
                    "Bảo lãnh hoàn trả tiền ứng trước (Advance Payment Bond) và Bảo lãnh bảo hành (Warranty Bond).\n\n"
                    "Thư tín dụng dự phòng (Standby L/C) theo Quy tắc ISP98 có bản chất tương tự bảo lãnh độc lập, "
                    "đóng vai trò là phương tiện thanh toán dự phòng khi người xin mở không hoàn thành nghĩa vụ cam kết."
                ),
                "formulas": [
                    "Bảo lãnh theo yêu cầu (Demand Guarantee): Trả tiền ngay khi nhận được yêu cầu đòi tiền đầu tiên (First Demand) mà không cần phán quyết của trọng tài hoặc tòa án.",
                    "Giá trị bảo lãnh dự thầu: Thường từ 1% đến 3% giá gói thầu; Bảo lãnh thực hiện hợp đồng từ 5% đến 10% giá trị hợp đồng."
                ],
                "case_studies": [
                    {
                        "title": "Phát hành Bảo lãnh Quốc tế cho nhà thầu EPC tại các dự án nhà máy nhiệt điện",
                        "detail": "Các ngân hàng quốc tế lớn (như Citi, Standard Chartered, HSBC) phối hợp với các NHTM Việt Nam phát hành bảo lãnh đối ứng (Counter-Guarantee) và bảo lãnh thực hiện hợp đồng trị giá hàng chục triệu USD cho các nhà thầu thi công hạ tầng trọng điểm quốc gia."
                    }
                ]
            },
            {
                "sec_num": "2",
                "sec_title": "Các sản phẩm tài trợ thương mại hiện đại (Trade Finance)",
                "content": (
                    "Tài trợ thương mại cung cấp thanh khoản và giảm thiểu rủi ro cho toàn bộ chu kỳ thương mại quốc tế. "
                    "Các sản phẩm nổi bật bao gồm: "
                    "1. Bao thanh toán quốc tế (International Factoring theo Quy tắc GRIF): Doanh nghiệp xuất khẩu bán lại các khoản phải thu thương mại ngắn hạn cho đơn vị bao thanh toán (Factor) để nhận ngay tiền ứng trước và chuyển giao rủi ro thu nợ;\n\n"
                    "2. Chiết khấu miễn truy đòi (Forfaiting): Ngân hàng mua đứt các công cụ nợ trung - dài hạn (hối phiếu, kỳ phiếu) có bảo lãnh thanh toán của ngân hàng với mức chiết khấu cố định, xóa bỏ hoàn toàn rủi ro tín dụng cho nhà xuất khẩu; "
                    "3. Tài trợ Chuỗi cung ứng (Supply Chain Finance - SCF) dựa trên uy tín tín dụng của doanh nghiệp đầu chuỗi (Anchor Buyer)."
                ),
                "formulas": [
                    "Số tiền giải ngân Factoring: Advance Amount = Khoản phải thu * Tỷ lệ ứng trước (thường 80-85%) - Phí dịch vụ bao thanh toán",
                    "Forfaiting Discount: Số tiền nhận được = Mệnh giá Hối phiếu / (1 + r * t/360)"
                ],
                "case_studies": [
                    {
                        "title": "Triển khai Tài trợ Chuỗi cung ứng số tại Ngân hàng Quân đội (MB)",
                        "detail": "MB xây dựng nền tảng SCF kỹ thuật số kết nối tự động với các nhà máy sản xuất xe máy Honda và ô tô Toyota, giải ngân vốn lưu động tức thì trong 2 giờ cho hàng trăm nhà cung cấp linh kiện vệ tinh cấp 1 và cấp 2."
                    }
                ]
            }
        ],
        advanced_phd_seminar={
            "topics": [
                "Ứng dụng Công nghệ Sổ cái Phân tán (Distributed Ledger Technology - DLT) và Blockchain trong Tài trợ Thương mại: Nền tảng Marco Polo, Contour và e-Presentation.",
                "Tuân thủ Phòng chống Rửa tiền và Tài trợ Khủng bố (AML/CFT) trong Tài trợ Ngoại thương: Khung Giám sát Rửa tiền Dựa trên Thương mại (Trade-Based Money Laundering - TBML) của FATF.",
                "Mô hình Tối ưu hóa Rủi ro Tín dụng Chuỗi Cung ứng Đa Tầng bằng Thuật toán Học sâu (Deep Learning Credit Scoring)."
            ]
        },
        review_questions=[
            "Phân tích sự khác biệt về tính chất pháp lý giữa Bảo lãnh ngân hàng độc lập theo URDG 758 và Bảo lãnh phụ thuộc truyền thống trong luật dân sự?",
            "Trình bày cơ chế hoạt động của nghiệp vụ Bao thanh toán quốc tế hai đầu mối (Two-Factor System) theo quy tắc của FCI?",
            "Làm thế nào để phát hiện các dấu hiệu bất thường của hành vi Rửa tiền Dựa trên Thương mại (TBML) thông qua việc ghi khống giá trên hóa đơn xuất nhập khẩu?"
        ]
    )
    
    pages, sz = b.save(out_pdf)
    print(f"[SUCCESS] Book 9 saved: {out_pdf} ({pages} pages, {sz:.2f} MB)")
    return {
        "title": title,
        "code": subject_code,
        "author": authors,
        "path": out_pdf,
        "pages": pages,
        "size_mb": round(sz, 2)
    }

if __name__ == "__main__":
    build_ttqt()
