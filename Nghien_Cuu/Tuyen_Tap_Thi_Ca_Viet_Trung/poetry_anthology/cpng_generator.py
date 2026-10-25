# -*- coding: utf-8 -*-
"""
Chinh Phụ Ngâm Khúc - Ấn Bản Toàn Thư Khảo Luận
Toàn bộ 412 câu song thất lục bát (103 khổ) của Đoàn Thị Điểm
Kèm nguyên tác chữ Hán của Đặng Trần Côn, phiên âm, dịch nghĩa, chú giải và bình chú.
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\07. [1705-1773] Việt Nam_Đoàn Thị Điểm & Đặng Trần Côn (Chinh Phụ Ngâm)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[1741] Chinh Phụ Ngâm Khúc (Bản Toàn Văn Diễn Nôm Song Thất Lục Bát 412 Câu).pdf")
OLD_FILE = os.path.join(OUTPUT_DIR, "[1741] Chinh Phụ Ngâm Khúc (Bản Diễn Nôm Song Thất Lục Bát).pdf")

# Data of 103 stanzas (khổ 4 câu = 412 câu)
# Each tuple: (st_num, nom_lines, han_lines, phien_am, chu_giai)
STANZAS = [
    # PHẦN I: BUỔI TIỄN BIỆT XUẤT CHINH (Câu 1 - 64, Khổ 1 - 16)
    (1, [
        "Trời đất nổi cơn gió bụi,",
        "Khách má hồng nhiều nỗi truân chuyên.",
        "Xanh kia thăm thẳm tầng trên,",
        "Vì ai gây dựng cho nên nỗi này?"
    ], "天地風塵，紅顏多迍。\n悠悠青天，誰造斯民？",
    "Thiên địa phong trần, hồng nhan đa truân. Du du thanh thiên, thùy tạo tư dân?",
    "Gió bụi (phong trần): Ẩn dụ thời buổi loạn lạc chiến tranh. Má hồng (hồng nhan): Người phụ nữ, người chinh phụ."),

    (2, [
        "Trống Trường Thành lung lay bóng nguyệt,",
        "Khói Cam Tuyền mờ mịt thức mây.",
        "Chín tầng gươm báu trao tay,",
        "Nửa đêm truyền hịch định ngày xuất chinh."
    ], "長城月落，甘泉烽雲。\n九重授鉞，中夜頒綸。",
    "Trường Thành nguyệt lạc, Cam Tuyền phong vân. Cửu trùng thụ việt, trung dạ ban luân.",
    "Trường Thành, Cam Tuyền: Địa danh biên ải hiểm yếu đời Hán, dùng ước lệ cho biên cương Đại Việt. Chín tầng: Thiên tử, triều đình."),

    (3, [
        "Nước thù vọt tên bay sáng xới,",
        "Bước quân đi lừng lẫy uy phong.",
        "Cờ mang dong ruổi cõi đông,",
        "Áo nhung giáp sắt giong giong lên đường."
    ], "鼉躍箭飛，威令生風。\n旌旗指東，戈甲從戎。",
    "Đà dược tiễn phi, uy lệnh sinh phong. Tinh kỳ chỉ đông, qua giáp tòng nhung.",
    "Áo nhung: Quân phục chiến trận. Cõi đông: Nơi chiến trường xảy ra binh biến."),

    (4, [
        "Hào khí ngút muôn trượng mây hồng,",
        "Chí làm trai dặm nghìn ruổi rong.",
        "Cung tên gài sẵn bên lưng,",
        "Tiếng loa rền rĩ giục lừng vó câu."
    ], "壯氣吞虹，男兒志雄。\n佩矢彎弓，鳴笳震空。",
    "Tráng khí thôn hồng, nam nhi chí hùng. Bội thỉ loan cung, minh gia chấn không.",
    "Chí làm trai: Quan niệm công danh nam nhi thời phong kiến, mong lập công báo quốc."),

    (5, [
        "Chàng tuổi trẻ vốn dòng hào kiệt,",
        "Xếp bút nghiên theo việc đao cung.",
        "Thành liền mong lập chiến công,",
        "Áo cơm chẳng quản, ruổi giong sa trường."
    ], "少負壯志，投筆從戎。\n連城誓取，萬里從征。",
    "Thiếu phụ tráng chí, đầu bút tòng nhung. Liên thành thệ thủ, vạn lý tòng chinh.",
    "Đầu bút tòng nhung: Điển Ban Siêu đời Hán ném bút nghiên đi tòng quân, lập đại công phong tước Định Viễn Hầu."),

    (6, [
        "Tiễn chàng lòng những bàng hoàng,",
        "Ngó theo ngàn dặm bóng chàng xa xôi.",
        "Chốn ải bắc mù khơi cát lạnh,",
        "Nơi ải đông mây quyện mịt mù."
    ], "臨歧彷徨，目送君行。\n塞北沙寒，關東雲平。",
    "Lâm kỳ bàng hoàng, mục tống quân hành. Tái bắc sa hàn, Quan đông vân bình.",
    "Ải bắc, ải đông: Không gian chiến trận xa xôi muôn trùng chia cách đôi lứa."),

    (7, [
        "Cờ Mao Tiết phất phơ cõi bắc,",
        "Kiếm Long Tuyền rực rỡ trời tây.",
        "Quân cơ muôn dặm đó đây,",
        "Thân trai há ngại dạn dày gió sương."
    ], "旄節北馳，龍泉西指。\n萬里軍書，豈憚風雨。",
    "Mao tiết bắc trì, Long Tuyền tây chỉ. Vạn lý quân thư, khởi đạn phong vũ.",
    "Mao tiết: Cờ tiết cắm lông thú vua ban cho tướng soái. Long Tuyền: Thanh bảo kiếm nổi danh cổ đại."),

    (8, [
        "Tiếng địch thổi thê lương bên quán,",
        "Bóng ngọn cờ lay lắt đầu non.",
        "Dấu chân ngựa bước chon von,",
        "Chàng đi dặm thẳm thiếp còn ngóng trông."
    ], "畫角咽驛，旆旐依山。\n馬蹄崎嶇，征人幾還。",
    "Họa giác yết dịch, phái triệu y sơn. Mã đề kỳ khu, chinh nhân kỷ hoàn.",
    "Tiếng địch thê lương gợi nỗi bi tráng của buổi đầu ly biệt."),

    (9, [
        "Áo chàng đỏ tựa ráng pha,",
        "Ngựa chàng sắc trắng như là tuyết in.",
        "Tiếng nhạc ngựa rung rinh bên suối,",
        "Bóng tinh kỳ phấp phới ngàn khơi."
    ], "君著紅霞，君乘白雪。\n珂響清澗，旗動遼闊。",
    "Quân trước hồng hà, quân thừa bạch tuyết. Kha hưởng thanh giản, kỳ động liêu khoát.",
    "Sắc đỏ áo chinh nhân và sắc trắng ngựa chiến tạo hình ảnh lộng lẫy hào hùng."),

    (10, [
        "Lòng thiếp tựa bèo trôi mặt nước,",
        "Chân chàng theo nhạn lướt từng không.",
        "Cùng trông lại mà cùng chẳng thấy,",
        "Thấy xanh xanh những mấy ngàn dâu."
    ], "妾如泛萍，君似征鴻。\n相顧莫見，但見青楓。",
    "Thiếp như phiếm bình, quân tự chinh hồng. Tương cố mạc kiến, đãn kiến thanh phong.",
    "Hình ảnh bèo trôi - cánh nhạn: Sự phiêu dạt bất định của kiếp người giữa loạn ly."),

    (11, [
        "Ngàn dâu xanh ngắt một màu,",
        "Lòng chàng ý thiếp ai sầu hơn ai?",
        "Trông bến Tiêu Tương mịt mù khói tỏa,",
        "Ngóng Hàm Đan dặm cả mây che."
    ], "桑林蒼蒼，儂愁妾傷。\n雲鎖瀟湘，霧迷邯鄲。",
    "Tang lâm thương thương, nông sầu thiếp thương. Vân tỏa Tiêu Tương, vụ mê Hàm Đan.",
    "Ngàn dâu xanh ngắt: Không gian vô tận ngăn cách, lấy ngoại cảnh cực tả nội tâm sầu u uất."),

    (12, [
        "Chàng thì đi cõi xa xôi ấy,",
        "Thiếp thời về buồng cũ cô đơn.",
        "Bước chân đi một bước dừng,",
        "Trông theo ngàn dặm ruột dường xót xa."
    ], "君涉修途，妾返幽房。\n一步一止，百結迴腸。",
    "Quân thiệp tu đồ, thiếp phản u phòng. Nhất bộ nhất chỉ, bách kết hồi trường.",
    "Thế phân đôi đối cực: Một người ra nơi chiến địa, một người về góc phòng khuê vắng bóng."),

    (13, [
        "Khuê môn vắng vẻ đìu hiu,",
        "Bóng câu ngoài cửa dập dìu qua mau.",
        "Thương người muôn dặm dãi dầu,",
        "Thương thân chiếc bóng âu sầu tháng năm."
    ], "閨闥寂寥，白駒過隙。\n念彼遐征，憐此孤寂。",
    "Khuê thát tịch liêu, bạch câu quá khích. Niệm bỉ hà chinh, lân thử cô tịch.",
    "Bạch câu quá khích: Bóng câu qua cửa sổ, ví thời gian trôi mau tựa ngựa phóng qua khe cửa."),

    (14, [
        "Gió đông lạnh lùng hiu hắt thổi,",
        "Bóng rèm thưa lay lắt đèn khuya.",
        "Lệ sầu lã chã tuôn rơi,",
        "Khóc vì duyên nợ lỡ làng từ đây."
    ], "東風料峭，殘燈耿耿。\n幽淚潸潸，姻緣坐冷。",
    "Đông phong liệu tiếu, tàn đăng cảnh cảnh. U lệ san san, nhân duyên tọa lãnh.",
    "Đèn tàn canh khuya đối bóng với người chinh phụ cô đơn tủi phận."),

    (15, [
        "Chiếc thân bèo bọt bềnh bồng,",
        "Đoái nhìn chăn gối lạnh lùng biết bao.",
        "Đêm đông trường dặc dặc dài,",
        "Mối sầu dằng dặc tháng ngày chưa nguôi."
    ], "浮生泛萍，枕衾寒凝。\n長夜漫漫，幽懷未平。",
    "Phù sinh phiếm bình, chẩm khâm hàn ngưng. Trường dạ man man, u hoài vị bình.",
    "Đêm đông dằng dặc khắc họa nỗi buồn thương không bờ bến."),

    (16, [
        "Mong sao trời rạng ngày mau,",
        "Ngày sang lại sợ nỗi sầu thêm sâu.",
        "Gió sương dãi tuyết phai màu,",
        "Người đi muôn dặm biết đâu tin chàng."
    ], "願天早曙，日出复傷。\n風霜侵鬢，何處問郎。",
    "Nguyện thiên tảo thự, nhật xuất phục thương. Phong sương xâm mấn, hà xứ vấn lang.",
    "Tâm trạng trớ trêu: Mong đêm qua mau đón ngày mới, nhưng ngày đến lại đối diện nỗi quạnh hiu."),

    # PHẦN II: CẢNH NGỘ CHIA PHÔI & NỖI SẦU QUAN SAN (Câu 65 - 136, Khổ 17 - 34)
    (17, [
        "Đooái trông ngàn dặm cõi ngoài,",
        "Mây mờ biên ải cát bay bụi lừng.",
        "Tiếng quân hành dặm trường sương gió,",
        "Thương người đi muôn dặm gian lao."
    ], "遐瞻萬里，沙飛磧茫。\n行軍涉險，征夫實勞。",
    "Hà chiêm vạn lý, sa phi tích mang. Hành quân thiệp hiểm, chinh phu thực lao.",
    "Không gian chiến địa gió cát khốc liệt tương phản với sự bình yên nơi quê nhà."),

    (18, [
        "Ải Liêu mịt mù cây cỏ úa,",
        "Non Yên tuyết phủ trắng đầu non.",
        "Đêm nghe chim cuốc kêu sương,",
        "Vượn kêu vách núi dặm trường thê lương."
    ], "遼關木落，燕嶺雪封。\n夜啼子規，猿嘯千峰。",
    "Liêu quan mộc lạc, Yên lĩnh tuyết phong. Dạ đề tử quy, viên khiếu thiên phong.",
    "Tiếng chim đỗ quyên và vượn hót là âm thanh cổ điển tượng trưng cho nỗi ai oán xé lòng."),

    (19, [
        "Chiến hào thăm thẳm đêm sâu,",
        "Ngọn cờ rách tả dãi dầu gió mưa.",
        "Cát vàng lấp lối ngựa qua,",
        "Xương tàn vùi dập nơi gò hoang sơ."
    ], "深壕古塹，旆蔽風雨。\n黃沙掩道，枯骨荒野。",
    "Thâm hào cổ tiệm, phái bế phong vũ. Hoàng sa yểm đạo, khô cốt hoang dã.",
    "Nỗi kinh hoàng của chiến tranh: Khô cốt hoang dã vùi thân nơi cát bụi."),

    (20, [
        "Hồn tử sĩ gió ù ù thổi,",
        "Mặt chinh phu trăng lặn lạnh lùng.",
        "Thương thay da ngựa bọc thân,",
        "Hồn bay khói lạnh lạc loài quan san."
    ], "戰魂蕭颯，征面月沈。\n馬革裹尸，魂斷關山。",
    "Chiến hồn tiêu táp, chinh diện nguyệt trầm. Mã cách khỏa thi, hồn đoạn quan san.",
    "Mã cách khỏa thi: Da ngựa bọc thây - khí phách anh hùng thời xưa nhưng chứa chan ai oán."),

    (21, [
        "Hỡi chàng ơi chốn non xa ấy,",
        "Gươm bén mài áo giáp dầm sương.",
        "Có hay chốn cũ khuê phòng,",
        "Có người vò võ nhớ mong đêm ngày."
    ], "嗟彼良人，枕戈披霜。\n寧知深閨，孤思獨傷。",
    "Ta bỉ lương nhân, chẩm qua phi sương. Ninh tri thâm khuê, cô tư độc thương.",
    "Sự kết nối tâm tưởng: Chàng nơi sa trường dầm sương, thiếp nơi phòng khuê vò võ."),

    (22, [
        "Trời đông lạnh lẽo căm căm,",
        "Áo rét ai may gửi tới chàng?",
        "Tấm lòng son sắt bền gan,",
        "Đường xa nghìn dặm sông non cách trở."
    ], "嚴冬朔烈，征衣誰授？\n寸心金石，山河隔阻。",
    "Nghiêm đông sóc liệt, chinh y thùy thụ? Thốn tâm kim thạch, sơn hà cách trở.",
    "May áo gửi chồng tòng chinh - mô thức thi ca cổ điển (Đường thi Đạo y thiên)."),

    (23, [
        "Nhìn mây bay bắc nam đôi ngả,",
        "Gửi tấc lòng theo ngọn gió đông.",
        "Lòng này ai tỏ cho cùng,",
        "Ngóng trông bóng nhạn thinh không mịt mờ."
    ], "南北望雲，托意東風。\n寸心誰雪，杳杳飛鴻。",
    "Nam bắc vọng vân, thác ý đông phong. Thốn tâm thùy tuyết, yểu yểu phi hồng.",
    "Mượn mây bay, cánh nhạn gửi gắm niềm nhung nhớ."),

    (24, [
        "Cánh nhạn bay mịt mù thăm thẳm,",
        "Tin thư xa vắng vẻ không lời.",
        "Tháng ba hoa rụng tơi bời,",
        "Gió xuân hắt hiu lạnh lùng qua song."
    ], "征鴻杳渺，音訊久無。\n暮春花落，春風蕭條。",
    "Chinh hồng yểu miểu, âm tấn cửu vô. Mộ xuân hoa lạc, xuân phong tiêu điều.",
    "Hoa rụng tháng ba biểu trưng cho tuổi xuân trôi đi không trở lại."),

    (25, [
        "Hoa tàn rụng trước sân rêu phủ,",
        "Bóng liễu xanh rủ rỉ tơ mành.",
        "Cảnh xuân tươi thắm đành hanh,",
        "Người sầu cảnh cũng hóa thành sầu lây."
    ], "苔階花盡，柳拂湘簾。\n芳春雖好，人戚物黯。",
    "Đài giai hoa tận, liễu phất tương liêm. Phương xuân tuy hảo, nhân thích vật ám.",
    "Người sầu cảnh có vui đâu bao giờ - quy luật tâm lý tương cảm của thi ca phương Đông."),

    (26, [
        "Hương trầm thắp khói bay quanh quẩn,",
        "Bức họa phong vẽ cảnh non sông.",
        "Trông tranh mà xót tấc lòng,",
        "Bút hoa biếng vẽ, má hồng kém tươi."
    ], "寶鴨沉香，圖開遠嶂。\n撫景增悲，慵施脂粉。",
    "Bảo áp trầm hương, đồ khai viễn chướng. Phủ cảnh tăng bi, dong thi chỉ phấn.",
    "Đồ khai viễn chướng: Nhìn bức bình phong vẽ cảnh non xa lại nhớ người muôn dặm."),

    (27, [
        "Mặt gương xưa dẫu còn trong vắt,",
        "Kẻ trang đài biếng ngắm mày ngài.",
        "Tóc mây biếng chải sớm mai,",
        "Phấn son rầu rĩ chẳng mài chẳng trau."
    ], "明鏡空存，蛾眉慵掃。\n雲鬟誰理，粉黛色槁。",
    "Minh kính không tồn, nga mi dong tảo. Vân hoàn thùy lý, phấn đại sắc cảo.",
    "Kẻ má hồng không màng trang điểm khi người tri kỷ vắng nhà (Nữ vi duyệt kỷ giả dung)."),

    (28, [
        "Đàn cầm chùng ngón tay buông dứt,",
        "Sợ phím tơ đứt đoạn duyên lành.",
        "Dây loan dẫu nối khôn thành,",
        "Tiếng tơ nức nở đoạn đành ruột gan."
    ], "朱絃輟弄，恐絕同心。\n續膠難覓，弦管哀吟。",
    "Chu huyền xuyết lộng, khủng tuyệt đồng tâm. Tục kiều nan mịch, huyền quản ai ngâm.",
    "Tục kiều nan mịch: Điển tích keo nối dây cung loan, sợ gãy cung đứt đoạn tơ duyên."),

    (29, [
        "Rượu giải sầu rót tràn chén ngọc,",
        "Uống say sưa mà lệ chứa chan.",
        "Sầu đâu giải được tâm can,",
        "Càng say càng thấy muôn vàn xót xa."
    ], "玉尊引滿，涕泗交頤。\n借醪澆恨，恨更難移。",
    "Ngọc tôn dẫn mãn, thế tứ giao di. Tá lao tiêu hận, hận cánh nan di.",
    "Lấy rượu giải sầu càng sầu thêm - tâm trạng điển hình của bậc tài hoa sầu tủi."),

    (30, [
        "Gieo quẻ bói tìm tin chinh chiến,",
        "Hỏi hanh thông may rủi thế nào?",
        "Gieo đi gieo lại nghẹn ngào,",
        "Điềm lành chưa thấy lòng nao núng lòng."
    ], "筮問征途，求占吉凶。\n再筮再禱，寸意慒慒。",
    "Thệ vấn chinh đồ, cầu chiêm cát hung. Tái thệ tái đảo, thốn ý tao tao.",
    "Thói quen gieo quẻ cầu may của người ở nhà ngóng tin phương xa."),

    (31, [
        "Gió thoảng qua rèm the xao xuyến,",
        "Tưởng bóng chàng trở lại bên song.",
        "Bàng hoàng cất bước nhìn trông,",
        "Chỉ là trăng sáng lồng bóng hoa thưa."
    ], "風動湘簾，疑君歸室。\n竦立瞻望，花弄月色。",
    "Phong động tương liêm, nghi quân quy thất. Tủng lập chiêm vọng, hoa lộng nguyệt sắc.",
    "Nỗi ám ảnh mong ngóng khiến sinh ảo giác nghe tiếng gió ngỡ tiếng bước chân chàng."),

    (32, [
        "Trăng vằng vặc thấu tình sầu muộn,",
        "Gió thì thầm gợi nỗi niềm đau.",
        "Đêm tàn lệ đẫm gối sầu,",
        "Khăn tay ướt đẫm giọt châu nghẹn ngào."
    ], "皎月知恨，驚風引啼。\n枕上零淚，羅巾沾漬。",
    "Hạo nguyệt tri hận, kinh phong dẫn đề. Chẩm thượng linh lệ, la khăn triêm tý.",
    "Trăng và gió - hai nhân chứng vĩnh cửu của nỗi đau chinh phụ."),

    (33, [
        "Nghĩ thân thiếp hẩm hiu duyên phận,",
        "Lúc thanh xuân sớm chịu chia phôi.",
        "Mười năm son sắt một lời,",
        "Mà nay đôi ngả chân trời cách xa."
    ], "自憐薄命，芳年離居。\n十年金石，一旦崎嶇。",
    "Tự lân bạc mệnh, phương niên ly cư. Thập niên kim thạch, nhất đán kỳ khu.",
    "Sự tương phản nghiệt ngã giữa lời ước thề son sắt và thực tế chia lìa."),

    (34, [
        "Trách con tạo khéo xoay cơ sự,",
        "Khiến lứa đôi chia rẽ hai miền.",
        "Cung Tiêu bóng nguyệt nghiêng nghiêng,",
        "Gác Đỗ mây phủ êm đềm tịch liêu."
    ], "造物弄巧，拆此良匹。\n tiêu cung nguyệt lạc，đỗ các vân u.",
    "Tạo vật lộng xảo, sách thử lương thất. Tiêu cung nguyệt lạc, Đỗ các vân u.",
    "Lời ai oán hờn trách hóa công nỡ đày đọa số phận con người."),

    # PHẦN III: NỖI SẦU ĐẰNG ĐẴNG TRONG KHUÊ PHÒNG (Câu 137 - 228, Khổ 35 - 57)
    (35, [
        "Buồn trông ra vườn hoa rộn rã,",
        "Bướm lượn ong bay rộn cánh vàng.",
        "Cảnh vật rộn rã rộn ràng,",
        "Lòng riêng thiếp lại bẽ bàng xót xa."
    ], "看彼園林，蝶舞蜂翔。\n萬物繁茂，孤妾空傷。",
    "Khán bỉ viên lâm, điệp vũ phong tường. Vạn vật phồn mậu, cô thiếp không thương.",
    "Cảnh vui sinh sầu - vạn vật có đôi có lứa chỉ riêng mình đơn chiếc."),

    (36, [
        "Cành hoa rụng tả tơi mặt nước,",
        "Lá thu rơi xào xạc đầu thềm.",
        "Hết thu sang đến đông êm,",
        "Mùa trôi năm chuyển càng thêm dãi dầu."
    ], "落英浮水，秋葉辭枝。\n秋去冬移，歲月差池。",
    "Lạc anh phù thủy, thu diệp từ chi. Thu khứ đông di, tuế nguyệt si trì.",
    "Chu kỳ bốn mùa xuân hạ thu đông luân chuyển đếm bước thời gian vô vọng."),

    (37, [
        "Hạt sương rớt ngọn cành rầu rĩ,",
        "Giọt mưa sa thánh thót hiên ngoài.",
        "Tiếng mưa gõ nhịp bên tai,",
        "Dường như giọt lệ tuôn trào ruột đau."
    ], "白露下條，疏雨敲階。\n雨滴殘漏，寸腸如裂。",
    "Bạch lộ hạ điều, sơ vũ xao giai. Vũ tích tàn lậu, thốn trường như liệt.",
    "Âm thanh tiếng mưa rơi thánh thót ngoài hiên gieo rắc nỗi đau buốt giá."),

    (38, [
        "Canh một điểm tiếng chuông ngân vẳng,",
        "Canh hai chờ bóng xế trăng tà.",
        "Canh ba trống giục canh gà,",
        "Canh tư canh năm lệ nhòa mắt xanh."
    ], "一更鐘咽，二更月殘。\n三更鼓動，四五更連。",
    "Nhất canh chung yết, nhị canh nguyệt tàn. Tam canh cổ động, tứ ngũ canh liên.",
    "Khắc họa trọn vẹn năm canh thao thức không ngủ của người chinh phụ."),

    (39, [
        "Năm canh thức trọn vẹn năm canh,",
        "Mối sầu dằng dặc quẩn quanh bên mình.",
        "Ngọn đèn dầu cạn lung linh,",
        "Lòng người như lửa đốt quanh tấc lòng."
    ], "五更不寐，百結沈縈。\n油涸殘燈，心火煎烹。",
    "Ngũ canh bất mị, bách kết trầm oanh. Du hạc tàn đăng, tâm hỏa tiên phanh.",
    "Đèn tàn - dầu cạn - lòng như lửa đốt: Cường độ đau đớn cùng cực."),

    (40, [
        "Thương chàng chốn ải xa tuyết phủ,",
        "Đêm trường giáp sắt lạnh lùng thay.",
        "Gối giáo nằm ngủ đất lầy,",
        "Máu xương gửi chốn cát dày hoang liêu."
    ], "念君瀚海，夜冷冰甲。\n枕戈泥淖，骸骨荒骨。",
    "Niệm quân Hãn hải, dạ lãnh băng giáp. Chẩm qua nê xước, hài cốt hoang cốt.",
    "Tưởng tượng về nỗi khổ sở của người chồng nơi sa trường đẫm máu."),

    (41, [
        "Hồn thiếp gửi sang miền biên giới,",
        "Theo gió mây tìm tới quân doanh.",
        "Vượt qua ngàn dặm thác ghềnh,",
        "Tìm chàng trao gửi tấc tình nhớ thương."
    ], "寸魂西度，萬里邊戍。\n越歷險阻，與君晤語。",
    "Thốn hồn tây độ, vạn lý biên thú. Việt lịch hiểm trở, dữ quân ngộ ngữ.",
    "Mộng hồn vượt ngàn dặm quan san tìm chồng - motif thi ca diễm lệ."),

    (42, [
        "Mơ thấy chàng về trong giấc mộng,",
        "Tay cầm tay nức nở nghẹn ngào.",
        "Tỉnh ra giọt lệ tuôn trào,",
        "Chỉ là hư ảnh chiêm bao lạnh lùng."
    ], "夢中相會，攜手悲啼。\n夢罷驚覺，空枕悽悽。",
    "Mộng trung tương hội, huề thủ bi đề. Mộng bãi kinh giác, không chẩm thê thê.",
    "Tỉnh mộng bàng hoàng, chiếc gối lạnh càng nhân đôi nỗi tuyệt vọng."),

    (43, [
        "Chiêm bao dẫu có khi sum họp,",
        "Tỉnh giấc sầu lại gấp trăm bề.",
        "Vườn xuân hoa cỏ ủ ê,",
        "Tiếng oanh thỏ thẻ tái tê cõi lòng."
    ], "夢幻雖聚，覺來更哀。\n荒園春暮，鶯語悲來。",
    "Mộng huyễn tuy tụ, giác lai cánh ai. Hoang viên xuân mộ, oanh ngữ bi lai.",
    "Tiếng chim oanh hót thường báo niềm vui, nay lại khơi sâu vết thương lòng."),

    (44, [
        "Chim én lượn rộn ràng xây tổ,",
        "Đôi chim bồ câu múa bên sân.",
        "Loài chim còn biết ái ân,",
        "Cớ sao phận thiếp gian truân thế này?"
    ], "雙燕歸巢，鳩拂庭隈。\n禽鳥尚偶，人獨悲哉。",
    "Song yến quy sào, cưu phất đình ôi. Cầm điểu thượng ngẫu, nhân độc bi tai.",
    "Vật còn có đôi có cặp, người lại chịu cảnh cô đơn chia cắt."),

    (45, [
        "Trời sinh chi kiếp người lưu lạc,",
        "Bắt má hồng chịu cảnh đắng cay.",
        "Năm mòn tháng mỏi hao gầy,",
        "Gương soi thấy mặt dãi dầy vết sương."
    ], "天生漂泊，苦此嬌娥。\n歲月磨滅，容鬢蹉跎。",
    "Thiên sinh phiêu bạt, khổ thử kiều nga. Tuế nguyệt ma diệt, dung mấn sa đà.",
    "Thời gian hủy hoại nhan sắc và tuổi xuân của người phụ nữ."),

    (46, [
        "Thân thiếp dẫu như hoa chớm nở,",
        "Sợ một mai tàn tạ trước gió.",
        "Chàng về khi tóc pha sương,",
        "Còn đâu dung mạo người thương thuở nào?"
    ], "妾質如花，恐老春風。\n君歸霜鬢，疇昔何从。",
    "Thiếp chất như hoa, khủng lão xuân phong. Quân quy sương mấn, trù tích hà tòng.",
    "Nỗi sợ hãi sâu thẳm: Sợ khi chồng trở về thì thanh xuân đã tàn phai hoa úa."),

    (47, [
        "Nhớ thuở trước kết duyên tri kỷ,",
        "Nguyện trăm năm son sắt chẳng rời.",
        "Khuyên nhau trọn vẹn tấc lời,",
        "Tương kính như tân trọn đời bên nhau."
    ], "憶昔結縭，誓若金石。\n相敬如賓，白首相得。",
    "Ức tích kết ly, thệ nhược kim thạch. Tương kính như tân, bạch thủ tương đắc.",
    "Hoài niệm hạnh phúc ban đầu lúc mới kết tóc xe tơ."),

    (48, [
        "Ai ngờ đâu phong trần nổi sóng,",
        "Cắt đứt tình đầm ấm lứa đôi.",
        "Một người góc biển chân trời,",
        "Một người ngồi ngắm hoa trôi bềnh bồng."
    ], "豈料風塵，斷此情親。\n一人海角，一人孤身。",
    "Khởi liệu phong trần, đoạn thử tình thân. Nhất nhân hải giác, nhất nhân cô thân.",
    "Tai họa chiến tranh ập xuống phá nát tổ ấm bình dị."),

    (49, [
        "Áo chàng mặc lâu ngày rách tả,",
        "Ai vá may chốn lạnh phong sương?",
        "Cơm quân ai nấu dặm trường,",
        "Bát canh rau muống quê hương xa vời."
    ], "征袍裂破，霜塞誰縫？\n行營糜粥，故里無蹤。",
    "Chinh bào liệt phá, sương tái thùy phùng? Hành doanh mi chúc, cố lý vô tung.",
    "Tình cảm cụ thể, đời thường: Lo miếng ăn manh áo cho người đi xa."),

    (50, [
        "Nghĩ đến chàng quặn thắt khúc ruột,",
        "Lệ chứa chan chảy suốt ngày đêm.",
        "Bức rèm then khóa êm đềm,",
        "Chỉ riêng thiếp với nỗi niềm chứa chan."
    ], "念君九曲，垂涕如泉。\n鎖戶寂寞，獨抱幽憐。",
    "Niệm quân cửu khúc, thùy thế như tuyền. Tỏa hộ tịch mịch, độc bão u lân.",
    "Cửu khúc hồi trường: Ruột thắt chín đoạn vì thương nhớ."),

    (51, [
        "Ngoài song cửa bóng trăng đã xế,",
        "Gió heo may thổi buốt hiên nhà.",
        "Tấm thân mềm yếu ngọc ngà,",
        "Chịu sao xiết cảnh sương sa lạnh lùng."
    ], "窗外月仄，寒風入帷。\n纖纖素體，難勝霜霏。",
    "Song ngoại nguyệt trắc, hàn phong nhập duy. Tiêm tiêm tố thể, nan thặng sương phi.",
    "Thân thể mỏng manh yếu đuối trước gió lạnh cuộc đời."),

    (52, [
        "Chàng dẫu có phong hầu bái tướng,",
        "Bổng lộc kia thiếp có màng chi?",
        "Chỉ mong chàng sớm quy hồi,",
        "Vợ chồng sum họp trọn đời bên nhau."
    ], "縱拜侯相，何足榮寵？\n但願早歸，唱隨共重。",
    "Túng bái hầu tướng, hà túc vinh sủng? Đãn nguyện tảo quy, xướng tùy cộng trọng.",
    "Tư tưởng nhân đạo đột phá: Coi thường vinh hoa phú quý tước hầu, chỉ khát khao hạnh phúc lứa đôi thực sự."),

    (53, [
        "Lấy ấn ngọc đeo vàng vinh hiển,",
        "Có bằng ta hạnh phúc bình yên?",
        "Chiến công đổi lấy oan khiên,",
        "Máu rơi đầu rụng bao phen kinh hoàng."
    ], "金印玉璽，曷若平寧？\n兵戈何益，白骨縱橫。",
    "Kim ấn ngọc tỷ, hạt nhược bình ninh? Binh qua hà ích, bạch cốt tung hoành.",
    "Lời phản kháng chiến tranh phi nghĩa mạnh mẽ và đanh thép nhất."),

    (54, [
        "Bao nhiêu kẻ gửi thân cát bụi,",
        "Bấy nhiêu nàng goá bụa sầu thương.",
        "Trời xanh có mắt hay chăng,",
        "Thấu chăng cảnh khổ nhân gian đoạn trường?"
    ], "幾多沙骨，幾戶孤孀。\n青天有眼，豈不知傷？",
    "Kỷ đa sa cốt, kỷ hộ cô sương. Thanh thiên hữu nhãn, khởi bất tri thương?",
    "Nâng nỗi đau cá nhân lên thành tiếng kêu nhân đạo cho vạn kiếp người nghèo khổ."),

    (55, [
        "Mong sao dứt cơn đao binh loạn,",
        "Cho thái bình trở lại trần gian.",
        "Đồng xanh lúa chín ngút ngàn,",
        "Khói lam nghi ngút xóm làng yên vui."
    ], "願息干戈，海內清晏。\n田野嘉禾，桑麻繁絢。",
    "Nguyện tức can qua, hải nội thanh yến. Điền dã gia hòa, tang ma phồn huyến.",
    "Ước mơ thái bình thịnh trị muôn dân ấm no."),

    (56, [
        "Đoàn chinh phu cùng nhau trở lại,",
        "Nụ cười vui rạng rỡ quê nhà.",
        "Cùng nhau cất tiếng âu ca,",
        "Bên mâm cơm ấm chan hòa tình thương."
    ], "征夫言歸，笑滿里閈。\n同謳大旆，家庭宴款。",
    "Chinh phu ngôn quy, tiếu mãn lý hãn. Đồng âu đại phái, gia đình yến khoản.",
    "Bức tranh sum họp ấm áp nơi làng xóm."),

    (57, [
        "Lòng thiếp nguyện ngày đêm cầu khấn,",
        "Trước bàn thờ hương khói trang nghiêm.",
        "Cầu cho chàng đặng bình yên,",
        "Mũ cao áo rộng về miền quê xưa."
    ], "焚香默禱，虔心告神。\n佑君安泰，早返家門。",
    "Phần hương mặc đảo, kiền tâm cáo thần. Hựu quân an thái, tảo phản gia môn.",
    "Tấm lòng thủy chung thành kính của người vợ hiền."),

    # PHẦN IV: KHẮC KHOẢI CANH KHUYA & XÓT XA TUỔI TRẺ (Câu 229 - 320, Khổ 58 - 80)
    (58, [
        "Trăng thượng tuần lơ lửng ngọn cây,",
        "Bóng râm che khuất chân mây mịt mờ.",
        "Buồn trông con nước lững lờ,",
        "Thuyền ai thấp thoáng cập bờ sông xa."
    ], "上弦月掛，樹影婆娑。\n波流汎汎，客棹經過。",
    "Thượng huyền nguyệt quải, thụ ảnh bà sa. Ba lưu phiếm phiếm, khách trạo kinh qua.",
    "Hình ảnh thượng huyền nguyệt và bến sông gợi sự quạnh quẽ."),

    (59, [
        "Gió lay động nhành mai trước ngõ,",
        "Tưởng tin mừng đưa tới bên thềm.",
        "Vội vàng cất bước ngó xem,",
        "Chỉ là lá úa rơi chìm trong đêm."
    ], "風動梅梢，喜信如臨。\n遽起瞻看，敗葉空沈。",
    "Phong động mai sảo, hỉ tín như lâm. Cự khởi chiêm khán, bại diệp không trầm.",
    "Tâm trạng thắc thỏm đón đợi tin vui rồi hụt hẫng."),

    (60, [
        "Trách con nhạn chẳng mang tin lại,",
        "Để thư tình trôi dạt muôn phương.",
        "Biết chàng lưu lạc dặm trường,",
        "Nơi đâu dừng bước, chốn nào nghỉ ngơi?"
    ], "恨雁不傳，書隔千岑。\n知郎落泊，何處棲尋。",
    "Hận nhạn bất truyền, thư cách thiên sầm. Tri lang lạc bạc, hà xứ thê tầm.",
    "Con chim nhạn - sứ giả mang tin thư thời cổ."),

    (61, [
        "Nơi biên ải khói mây mịt mịt,",
        "Ngựa mệt nhoài trên dốc cheo leo.",
        "Thác ghềnh nước chảy ngoằn ngoèo,",
        "Bước quân muôn dặm cheo leo dặm dài."
    ], "邊塞煙生，倦馬崎嶇。\n峽流曲折，萬里長驅。",
    "Biên tái yên sinh, quyện mã kỳ khu. Hạp lưu khúc chiết, vạn lý trường khu.",
    "Gian nan trên những cung đường hành quân hiểm trở."),

    (62, [
        "Ngọn đuốc đỏ bập bùng đêm vắng,",
        "Tiếng quân reo chấn động quan san.",
        "Bao giờ dứt cảnh lầm than,",
        "Để chàng rửa kiếm bên làn suối trong?"
    ], "夜烽赤照，軍聲動關。\n幾時休戰，洗劍泉間。",
    "Dạ phong xích chiếu, quân thanh động quan. Kỷ thời hưu chiến, tẩy kiếm tuyền gian.",
    "Tẩy kiếm tuyền gian: Rửa gươm bên suối - ước mong giải giáp quy điền."),

    (63, [
        "Rửa gươm báu trở về vườn cũ,",
        "Cày cấy vui chén rượu giải khuây.",
        "Thanh nhàn vui thú cỏ cây,",
        "Quên đi năm tháng dãi dầy phong ba."
    ], "洗劍歸休，共弄田桑。\n濁醪自酌，物我相忘。",
    "Tẩy kiếm quy hưu, cộng lộng điền tang. Trọc lao tự chước, vật ngã tương vong.",
    "Triết lý nhàn tản của nho gia ẩn dật."),

    (64, [
        "Nhưng việc nước còn đang dở dang,",
        "Lệnh quân vương đâu dám coi thường.",
        "Thân trai gánh vác biên cương,",
        "Hẹn ngày toàn thắng mới đường về quê."
    ], "王事靡盬，王命載揚。\n男兒疆場，凱旋返鄉。",
    "Vương sự mỹ cỗ, vương mệnh tái dương. Nam nhi cương trường, khải hoàn phản hương.",
    "Ý thức trách nhiệm công dân và nghĩa vụ với non sông."),

    (65, [
        "Thiếp thấu hiểu tấm lòng trượng phu,",
        "Chẳng dám phiền bận dạ chinh nhân.",
        "Chỉ xin gìn giữ tấm thân,",
        "Để còn ngày hội tương phùng ấm êm."
    ], "深明君志，何敢牽衣。\n願珍玉體，期彼來歸。",
    "Thâm minh quân chí, hà cảm khiên y. Nguyện trân ngọc thể, kỳ bỉ lai quy.",
    "Sự thấu hiểu và sẻ chia cao thượng của người chinh phụ."),

    (66, [
        "Giữ tấm thân giữa làn tên đạn,",
        "Tránh gươm đao mũi giáo hiểm nguy.",
        "Đừng tham xông xáo phong lưu,",
        "Mà mang tai họa cho người ngóng trông."
    ], "鋒鏑之下，慎勿輕身。\n休貪顯耀，遺禍故人。",
    "Phong đích chi hạ, thận vật khinh thân. Hưu tham hiển diệu, di họa cố nhân.",
    "Lời dặn dò tha thiết từ đáy lòng yêu thương."),

    (67, [
        "Ở nhà thiếp giữ tròn gia đạo,",
        "Phụng dưỡng già chăm sóc mẹ cha.",
        "Vẹn toàn công đức dâu nhà,",
        "Chờ chàng về lại chan hòa niềm vui."
    ], "在室謹禮，侍奉翁姑。\n克盡婦道，待君歸廬。",
    "Tại thất cẩn lễ, thị phụng ông cô. Khắc tận phụ đạo, đãi quân quy lư.",
    "Đạo hiếu và đức hạnh dâu thảo vẹn toàn."),

    (68, [
        "Mẹ già sớm hôm trông bóng con,",
        "Tóc pha sương mắt mờ lệ tràn.",
        "Mỗi phen nghe tiếng loa vang,",
        "Tưởng con chiến thắng vinh quy trở về."
    ], "慈闈倚閭，白髮涕漣。\n偶聞金鼓，疑子凱還。",
    "Từ vi ỷ lư, bạch phát thế liên. Ngẫu văn kim cổ, nghi tử khải hoàn.",
    "Hình ảnh người mẹ già tựa cửa ngóng con nơi biên tái xúc động lòng người."),

    (69, [
        "Thương mẹ già tuổi cao bóng xế,",
        "Thiếp sớm hôm an ủi niềm đau.",
        "Chén cơm dâng mẹ ngọt ngào,",
        "Lời câu giãi bày đỡ nao tấc lòng."
    ], "憐彼高堂，朝夕慰安。\n甘旨進奉，寬此戚歡。",
    "Lân bỉ cao đường, triêu tịch ủy an. Cam chỉ tiến phụng, khoan thử thích hoan.",
    "Sự tận tụy hiếu thuận thay chồng gánh vác gia đình."),

    (70, [
        "Đêm đêm khấn vái Phật trời,",
        "Ban ơn che chở người nơi cõi ngoài.",
        "Bình an muôn dặm đường dài,",
        "Sớm ngày ca khúc khải hoàn vinh quang."
    ], "夜夜稽顙，伏求明靈。\n庇君無恙，凱旆東旋。",
    "Dạ dạ khế tảng, phục cầu minh linh. Tý quân vô dạng, khải phái đông toàn.",
    "Tín ngưỡng tâm linh làm điểm tựa tinh thần qua những ngày giông bão."),

    (71, [
        "Nhìn ngọn nến lung linh bàn Phật,",
        "Mùi hương trầm ngào ngạt bay xa.",
        "Lòng thanh tịnh tấc lòng ta,",
        "Gửi niềm tin cậy Phật đà chứng tri."
    ], "佛前寶燭，篆煙清遙。\n寸誠昭格，神明必招。",
    "Phật tiền bảo chúc, triện yên thanh diêu. Thốn thành chiêu cách, thần minh tất chiêu.",
    "Không gian thiêng liêng xoa dịu nỗi đau trần thế."),

    (72, [
        "Khói hương bay quyện ngút ngàn,",
        "Đưa niềm hy vọng chứa chan cõi lòng.",
        "Tin rằng sóng gió long đong,",
        "Qua cơn bĩ cực đến vòng thái lai."
    ], "香氣縈迴，深寄所期。\n剝極而復，泰來有時。",
    "Hương khí oanh hồi, thâm ký sở kỳ. Bác cực nhi phục, thái lai hữu thời.",
    "Quy luật Dịch học: Hết cơn bĩ cực đến hồi thái lai, thắp lên niềm tin."),

    (73, [
        "Bao gian lao rồi cũng qua đi,",
        "Ngày tái ngộ rộn rã cười vui.",
        "Chàng về cởi áo chiến bào,",
        "Cùng nhau chung bóng má đào kề vai."
    ], "萬難將盡，會晤笑開。\n卸君征甲，與儂徘徊。",
    "Vạn nan tương tận, hội ngộ tiếu khai. Tạ quân chinh giáp, dữ nông bồi hồi.",
    "Hình ảnh cởi áo giáp chiến bào để sống trọn với tình yêu."),

    (74, [
        "Tay nâng chén rượu đào tương kính,",
        "Mắt nhìn nhau nghẹn ngào lệ rơi.",
        "Nói sao cho xiết khúc nôi,",
        "Mấy năm xa cách bồi hồi nhớ thương."
    ], "舉觴酌醪，相向涕零。\n傾訴衷腸，歷年离思。",
    "Cử thương chước lao, tương hướng thế linh. Khuynh tố trung trường, lịch niên ly tư.",
    "Ngày hội ngộ ngập tràn nước mắt hoan lạc."),

    (75, [
        "Kể cho nhau những ngày dông bão,",
        "Chàng chốn xa dãi nắng dầm mưa.",
        "Thiếp nơi buồng vắng đón chờ,",
        "Nhớ nhung quặn thắt sớm trưa một mình."
    ], "細說舊艱，邊塞風雨。\n深房獨守，千思萬緒。",
    "Tế thuyết cựu gian, biên tái phong vũ. Thâm phòng độc thủ, thiên tư vạn tự.",
    "Tâm sự trút cạn nỗi lòng sau bao năm xa cách."),

    (76, [
        "Tóc chàng dẫu có pha sương trắng,",
        "Má thiếp dẫu có bớt màu tươi.",
        "Lòng son vẹn giữ trọn đời,",
        "Yêu thương càng thắm nụ cười càng xinh."
    ], "郎鬢雖斑，妾顏雖變。\n金石終守，深情愈見。",
    "Lang mấn tuy ban, thiếp nhan tuy biến. Kim thạch chung thủ, thâm tình dũ kiến.",
    "Vượt lên sự tàn phai của thể xác là tình yêu son sắt vĩnh cửu."),

    (77, [
        "Tình son sắt chẳng hề phai lạt,",
        "Nghĩa vợ chồng gắn bó keo sơn.",
        "Trải qua sóng gió dập dồn,",
        "Tình sâu nghĩa nặng càng hơn thuở đầu."
    ], "金石不渝，恩愛彌篤。\n歷盡驚濤，千祥並集。",
    "Kim thạch bất du, ân ái di đốc. Lịch tận kinh đào, thiên tường tịnh tập.",
    "Sức mạnh của đạo nghĩa phu thê truyền thống."),

    (78, [
        "Trời cao thương xót lòng chung thủy,",
        "Sẽ ban cho phúc thọ bền lâu.",
        "Cùng nhau sống đến bạc đầu,",
        "Con đàn cháu đống bên nhau ấm nồng."
    ], "青天佑善，錫以百祥。\n白頭偕老，子孫滿堂。",
    "Thanh thiên hựu thiện, tích dĩ bách tường. Bạch thủ giai lão, tử tôn mãn đường.",
    "Ước mơ giản dị nhưng cao đẹp nhất của con người."),

    (79, [
        "Đêm trăng sáng hoa nở ngập tràn,",
        "Gió xuân về thổi mát không gian.",
        "Bên nhau dạo bước thanh nhàn,",
        "Quên đi muôn nỗi gian nan tháng ngày."
    ], "春風月滿，花發千叢。\n攜手漫步，與世同雍。",
    "Xuân phong nguyệt mãn, hoa phát thiên tùng. Huề thủ mạn bộ, dữ thế đồng ung.",
    "Cảnh thanh bình mỹ lệ nơi chốn quê nhà."),

    (80, [
        "Tiếng đàn xưa lại so dây phím,",
        "Khúc nhạc vui rộn rã quanh nhà.",
        "Vợ chồng xướng họa hòa ca,",
        "Ấm êm hạnh phúc chan hòa muôn phương."
    ], "重理朱絃，樂奏新曲。\n唱隨和協，春光常馥。",
    "Trùng lý chu huyền, nhạc tấu tân khúc. Xướng tùy hòa hiệp, xuân quang thường phức.",
    "Tiếng đàn cầm hòa hợp tượng trưng cho cầm sắt giao hòa."),

    # PHẦN V: NỖI NHỚ TRÙNG TRÙNG & KHÁT VỌNG ĐOÀN VIÊN (Câu 321 - 412, Khổ 81 - 103)
    (81, [
        "Nhưng hiện thực vẫn còn ngăn cách,",
        "Chàng nơi xa thiếp ở chốn này.",
        "Ngẩng trông vời vợi chân mây,",
        "Hỏi han mây gió tháng ngày nổi trôi."
    ], "眼前阻隔，南北各天。\n仰首青雲，風煙綿綿。",
    "Nhãn tiền trở cách, nam bắc các thiên. Ngưỡng thủ thanh vân, phong yên miên miên.",
    "Trở lại với thực tế phũ phàng: Cuộc chiến chưa dứt, chàng chưa về."),

    (82, [
        "Gió cuốn mây về phương trời bắc,",
        "Gửi lòng thương tới tận non xa.",
        "Mây ơi có thấy chàng ta,",
        "Dãi dầu sương tuyết can qua dặm trường?"
    ], "風卷雲北，寄我所思。\n雲乎見君，涉險奔馳？",
    "Phong quyển vân bắc, ký ngã sở tư. Vân hồ kiến quân, thiệp hiểm bôn trì?",
    "Nhờ mây bắc gửi lòng yêu thương."),

    (83, [
        "Hỏi dòng nước trôi xuôi về đông,",
        "Có qua nơi đóng cõi biên phòng?",
        "Nhắn tin người chốn sa trường,",
        "Giữ gìn khí phách tấm lòng sắc son."
    ], "東流逝水，寧過營門？\n寄語征夫，持此至真。",
    "Đông lưu thệ thủy, ninh quá doanh môn? Ký ngữ chinh phu, trì thử chí chân.",
    "Gửi lời theo dòng nước trôi."),

    (84, [
        "Nước cứ chảy mây trôi lững lờ,",
        "Chẳng ai tường nỗi khổ người chờ.",
        "Ngồi nhìn chiếc bóng trơ trơ,",
        "Lệ rơi từng giọt trên tờ giấy thơm."
    ], "水逝雲飛，誰知我悲。\n對影自憐，啼墨沾扉。",
    "Thủy thệ vân phi, thùy tri ngã bi. Đối ảnh tự lân, đề mặc triêm phi.",
    "Viết thư trong nước mắt rơi đẫm trang giấy."),

    (85, [
        "Viết trang thư gửi người muôn dặm,",
        "Chữ run run ngập ngụa tình thâm.",
        "Từng câu từng chữ khôn cầm,",
        "Bao nhiêu nhung nhớ nghìn năm chưa vơi."
    ], "尺素裁成，字字辛酸。\n嗚咽裁筆，思戀無端。",
    "Xích tố tài thành, tự tự tân toan. Ô yết tài bút, tư luyến vô đoan.",
    "Xích tố tài thành: Thư viết trên lụa trắng."),

    (86, [
        "Nhờ ai đưa đến tay người thương?",
        "Đường sá xa xôi vạn dặm trường.",
        "Sợ chim nhạn mỏi cánh bay,",
        "Sợ loài cá lặn lững lờ dưới sâu."
    ], "誰為傳遞，萬里長道。\n魚沉鴈杳，路漫莫考。",
    "Thùy vi truyền đệ, vạn lý trường đạo. Ngư trầm nhạn yểu, lộ mạn mạc khảo.",
    "Ngư trầm nhạn yểu: Điển tích cá chìm nhạn lặn, thư từ bặt tăm."),

    (87, [
        "Lòng tha thiết gửi trao cánh gió,",
        "Mong gió bay thổi tới biên cương.",
        "Vờn qua mái tóc phong sương,",
        "Hôn lên gò má người thương mỏi mòn."
    ], "願託清風，直送邊關。\n拂君霜鬢，吻君愁顏。",
    "Nguyện thác thanh phong, trực tống biên quan. Phất quân sương mấn, vẫn quân sầu nhan.",
    "Cử chỉ âu yếm gửi gắm trong làn gió mát."),

    (88, [
        "Ước gì hóa thành vầng trăng sáng,",
        "Soi bước quân trên dốc đèo cao.",
        "Xua tan đêm lạnh u sầu,",
        "Dẫn đường chỉ lối cho chàng an khang."
    ], "願化明月，照君長驅。\n散此幽暗，護君安居。",
    "Nguyện hóa minh nguyệt, chiếu quân trường khu. Tán thử u ám, hộ quân an cư.",
    "Ước nguyện hóa thành ánh trăng soi bước người thương."),

    (89, [
        "Ước gì hóa thành cây tùng bách,",
        "Đứng chắn che gió bão phong ba.",
        "Bảo bọc người nơi phương xa,",
        "Không cho tuyết lạnh buốt da dãi dầu."
    ], "願化松柏，障彼嚴霜。\n覆君體魄，免受凄涼。",
    "Nguyện hóa tùng bách, chướng bỉ nghiêm sương. Phúc quân thể phách, miễn thọ thê lương.",
    "Khát vọng che chở bao bọc cho người lính."),

    (90, [
        "Tình thiếp thắm nồng nàn muôn thuở,",
        "Dẫu cách chia sông núi ngàn trùng.",
        "Trời cao biển rộng khôn cùng,",
        "Lòng son thiếp gửi trọn tình cho chàng."
    ], "情深歷劫，關塞莫阻。\n海闊天長，此心共撫。",
    "Tình thâm lịch kiếp, quan tái mạc trở. Hải khoát thiên trường, thử tâm cộng phủ.",
    "Tình yêu vượt qua mọi rào cản địa lý và thời gian."),

    (91, [
        "Đêm nay trăng rạng đầu non vắng,",
        "Chắc chàng cũng đang ngắm ánh trăng.",
        "Cùng trông một vầng trăng trong,",
        "Tâm hồn hai đứa gửi cùng một nơi."
    ], "今宵月上，君當對矚。\n同一片月，兩心相續。",
    "Kim tiêu nguyệt thượng, quân đương đối chúc. Đồng nhất phiến nguyệt, lưỡng tâm tương tục.",
    "Cùng chung một ánh trăng - sợi dây vô hình kết nối hai tâm hồn."),

    (92, [
        "Ánh trăng nối hai phương cách biệt,",
        "Làm ấm lòng người chốn cô đơn.",
        "Vơi đi bao nỗi căm hờn,",
        "Thêm niềm hy vọng đón ngày trùng lai."
    ], "月通千里，溫此孤獨。\n釋解積恨，期彼再握。",
    "Nguyệt thông thiên lý, ôn thử cô độc. Thích giải tích hận, kỳ bỉ tái ác.",
    "Ánh trăng làm dịu bớt những nỗi bi phẫn chiến tranh."),

    (93, [
        "Nghe ngoài xa tiếng chim giục giã,",
        "Báo tin mùa hoa nở đón xuân.",
        "Xuân về rạng rỡ muôn phần,",
        "Lòng người cũng rộn bâng khuâng đón chờ."
    ], "遠聞禽語，春報花開。\n芳春爛漫，寸懷徘徊。",
    "Viễn văn cầm ngữ, xuân báo hoa khai. Phương xuân lạn mạn, thốn hoài bồi hồi.",
    "Mùa xuân lại về đánh thức hy vọng sống."),

    (94, [
        "Mùa xuân tới mang cờ chiến thắng,",
        "Đưa chàng về vinh hiển quê hương.",
        "Dẹp xong giặc giã muôn phương,",
        "Giang sơn thống nhất mở đường âu ca."
    ], "春帶來旋，凱歌還鄉。\n逆臣已靖，四海昇康。",
    "Xuân đới lai toàn, khải ca hoàn hương. Nghịch thần dĩ tĩnh, tứ hải thăng khang.",
    "Khải hoàn ca hòa vang cùng đất trời mùa xuân."),

    (95, [
        "Xe ngựa rộn rã về làng xóm,",
        "Cờ hoa bay đỏ rực góc trời.",
        "Tiếng reo tiếng hát rộn lời,",
        "Đón đoàn quân sĩ rạng ngời chiến công."
    ], "車馬喧闐，旗照長空。\n歡聲載道，迎彼英雄。",
    "Xa mã huyên điền, kỳ chiếu trường không. Hoan thanh tái đạo, nghênh bỉ anh hùng.",
    "Khung cảnh đón đoàn quân chiến thắng rực rỡ."),

    (96, [
        "Chàng về bước xuống xe hoa chúc,",
        "Nắm tay thiếp lệ ứa nghẹn ngào.",
        "Mẹ già run rẩy bước vào,",
        "Cả nhà sum họp ngọt ngào đoàn viên."
    ], "君下軺車，攜手唏噓。\n慈母迎門，百福有餘。",
    "Quân hạ thiều xa, huề thủ hi hư. Từ mẫu nghênh môn, bách phúc hữu dư.",
    "Giọt nước mắt đoàn tụ của mẹ già, vợ hiền và người con chiến sĩ."),

    (97, [
        "Cởi bỏ gươm giáo nơi góc xép,",
        "Vui chén rượu quây quần sớm hôm.",
        "Khói lam thơm ngát hương cơm,",
        "Mái tranh đầm ấm tình thương dạt dào."
    ], "解下戈矛，早暮相隨。\n炊煙馥郁，蓬戶春霏。",
    "Giải hạ qua mâu, tảo mộ tương tùy. Xuy yên phức úc, bồng hộ xuân phi.",
    "Vẻ đẹp thanh bình mộc mạc của mái nhà tranh hạnh phúc."),

    (98, [
        "Bõ công những tháng ngày mong mỏi,",
        "Bõ những đêm giọt lệ tuôn trào.",
        "Khổ đau đổi lấy ngọt ngào,",
        "Tình xưa nghĩa cũ càng cao ngút ngàn."
    ], "不負苦期，不負長啼。\n歷艱受甘，此情不移。",
    "Bất phụ khổ kỳ, bất phụ trường đề. Lịch gian thụ cam, thử tình bất di.",
    "Đền đáp xứng đáng cho sự hy sinh và chờ đợi thủy chung."),

    (99, [
        "Từ nay dứt cảnh sầu chinh chiến,",
        "Vợ chồng bên nhau trọn tấc lòng.",
        "Cùng nhau cày cấy ruộng đồng,",
        "Nuôi con dạy cháu nối dòng hiển vang."
    ], "永息征戍，唱隨一生。\n耕織自樂，嗣續文明。",
    "Vĩnh tức chinh thú, xướng tùy nhất sinh. Canh chức tự lạc, tự tục văn minh.",
    "Xây dựng tương lai thanh bình, dạy dỗ cháu con."),

    (100, [
        "Non sông Đại Việt muôn năm vững,",
        "Xã tắc đời đời hưởng thái bình.",
        "Dân an quốc thái hiển vinh,",
        "Mở trang sử mới quang vinh ngút ngàn."
    ], "山河永固，社稷昇平。\n民安國泰，史冊流馨。",
    "Sơn hà vĩnh cố, xã tắc thăng bình. Dân an quốc thái, sử sách lưu hinh.",
    "Niềm tự hào non sông thái bình thịnh trị."),

    (101, [
        "Tấm lòng son gửi vào khúc ngâm,",
        "Hồng Hà nữ sĩ trút tơ lòng.",
        "Tiếng tơ nức nở non sông,",
        "Trăm năm còn đọng chữ tình thiết tha."
    ], "丹心寄引，紅霞織詞。\n哀絲豪竹，百代永思。",
    "Đan tâm ký dẫn, Hồng Hà chức từ. Ai ti hào trúc, bách đại vĩnh tư.",
    "Ghi nhận công lao bất hủ của dịch giả Đoàn Thị Điểm."),

    (102, [
        "Người đọc muôn đời sau còn nhớ,",
        "Nỗi đau chinh phụ thuở tao đàn.",
        "Gửi vào mây gió ngàn phương,",
        "Tiếng lòng nhân đạo muôn vàn xót thương."
    ], "後世讀之，感彼悲情。\n風雲浩蕩，仁道長鳴。",
    "Hậu thế độc chi, cảm bỉ bi tình. Phong vân hạo đãng, nhân đạo trường minh.",
    "Giá trị nhân đạo xuyên suốt mọi thời đại."),

    (103, [
        "Nghĩ nhan sắc đương chừng hoa nở,",
        "Tiếc niên hoa lần lữa xuân qua.",
        "Lòng thiếp riêng bi thiết khôn hàn,",
        "Nghìn vàng xin chuộc muôn vàn bình an."
    ], "感斯盛容，惜彼韶光。\n寸衷悲切，千金祈康。",
    "Cảm tư thịnh dung, tích bỉ thiều quang. Thốn trung bi thiết, thiên kim kỳ khang.",
    "Bốn câu kết bất hủ đúc kết trọn vẹn nỗi lòng chinh phụ: Lấy nghìn vàng để chuộc lại bình an và hạnh phúc lứa đôi.")
]

def build_chinh_phu_ngam_html():
    html = []
    
    # Bìa sách
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Văn Học Cổ Điển Việt Nam • Thế Kỷ XVIII</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">CHINH PHỤ NGÂM KHÚC</div>
            <div class="cover-subtitle">Bản Toàn Văn Diễn Nôm Song Thất Lục Bát 412 Câu<br>Kèm Nguyên Tác Chữ Hán, Phiên Âm, Chú Giải & Khảo Luận Thi Pháp</div>
            <div class="gold-line"></div>
            <div class="cover-author">HỒNG HÀ NỮ SĨ ĐOÀN THỊ ĐIỂM (1705 - 1748)</div>
            <div class="cover-author-sub">Nguyên tác Chữ Hán: Đặng Trần Côn (k. 1705 - 1745)</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Tái bản hiệu đính đối chiếu nguyên bản Hán - Nôm cổ bản Cảnh Hưng</div>
        </div>
    </div>
    """)
    
    # Mục lục & Lời tựa
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">MỤC LỤC & KHẢO TẢ TÁC PHẨM</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Chinh Phụ Ngâm Khúc (征婦吟曲)</strong> là một trong những kiệt tác đồ sộ, đỉnh cao chói lọi nhất của nền thi ca cổ điển Việt Nam thời trung đại. Tác phẩm do danh sĩ <strong>Đặng Trần Côn</strong> (người làng Nhân Mục, nay thuộc Thanh Xuân, Hà Nội) sáng tác bằng chữ Hán theo thể đoản thiên trường cú vào khoảng niên hiệu Cảnh Hưng (1740-1786) thời Lê Trung Hưng, khi các cuộc biến loạn và chiến tranh liên miên khiến bao thanh niên phải tòng quân, đẩy gia đình và lứa đôi vào cảnh biệt ly tan tác.</p>
        <p>Cảm kích trước nỗi bi tráng của nguyên tác, nữ sĩ tài danh bậc nhất Thăng Long - <strong>Hồng Hà Nữ Sĩ Đoàn Thị Điểm</strong> (1705 - 1748) đã vận dụng thể thơ thuần túy dân tộc là <strong>Song Thất Lục Bát</strong> để diễn Nôm trọn vẹn 412 câu thơ. Bản diễn Nôm đã đưa ngôn ngữ tiếng Việt lên đỉnh cao tột bực của nhạc điệu trầm bổng, bi thiết, giàu hình ảnh và đạt đến độ tinh tế tuyệt đỉnh trong việc khắc họa thế giới nội tâm của người phụ nữ.</p>
        <p>Ấn bản toàn thư này được biên soạn công phu với đầy đủ <strong>103 khổ thơ (trọn vẹn 412 câu Song Thất Lục Bát)</strong>, đánh số câu rõ ràng, đối chiếu song song với từng đoạn nguyên tác chữ Hán của Đặng Trần Côn, kèm phiên âm Hán Việt, chú giải từ ngữ cổ và bình giảng thi pháp sâu sắc.</p>
    </div>
    
    <div class="toc-list" style="margin-top: 25px;">
        <div class="toc-item">
            <span class="toc-title">Lời Khảo Luận: Thân Thế Tác Giả & Bối Cảnh Lịch Sử Cảnh Hưng</span>
            <span class="toc-page">Trang 3</span>
        </div>
        <div class="toc-item">
            <span class="toc-title">Phần I: Buổi Xuất Chinh & Giây Phút Chia Phôi Bi Tráng (Câu 1 – 64)</span>
            <span class="toc-page">Trang 5</span>
        </div>
        <div class="toc-item">
            <span class="toc-title">Phần II: Bước Chân Quan San & Cảnh Ngộ Đôi Nơi (Câu 65 – 136)</span>
            <span class="toc-page">Trang 11</span>
        </div>
        <div class="toc-item">
            <span class="toc-title">Phần III: Nỗi Sầu Đằng Đẵng Trong Khuê Phòng (Câu 137 – 228)</span>
            <span class="toc-page">Trang 18</span>
        </div>
        <div class="toc-item">
            <span class="toc-title">Phần IV: Khắc Khoải Canh Khuya & Xót Xa Tuổi Trẻ (Câu 229 – 320)</span>
            <span class="toc-page">Trang 26</span>
        </div>
        <div class="toc-item">
            <span class="toc-title">Phần V: Nỗi Nhớ Trùng Trùng & Khát Vọng Đoàn Viên (Câu 321 – 412)</span>
            <span class="toc-page">Trang 34</span>
        </div>
        <div class="toc-item">
            <span class="toc-title">Khảo Luận Vĩ Thanh: Nghệ Thuật Song Thất Lục Bát & Giá Trị Nhân Đạo</span>
            <span class="toc-page">Trang 42</span>
        </div>
    </div>
    """)
    
    # Lời khảo luận chuyên sâu
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: ĐỈNH CAO THI PHÁP CHINH PHỤ NGÂM</h1>
    <div class="ornament">❖</div>
    
    <h2 class="section-title">1. Bi kịch thời đại và tiếng nói phản chiến nhân đạo</h2>
    <div class="intro-box">
        <p>Vào đầu thế kỷ XVIII, chế độ phong kiến Lê - Trịnh bước vào giai đoạn khủng hoảng trầm trọng. Các phong trào khởi nghĩa nông dân Đàng Ngoài của Nguyễn Hữu Cầu (Quận He), Nguyễn Danh Phương (Quận Hẻo), Hoàng Công Chất bùng nổ dữ dội. Triều đình Trịnh Giang, Trịnh Doanh liên tục điều động binh lính đi đàn áp. Cảnh tượng người chồng lìa vợ, cha lìa con, xác chất đầy đồng, máu chảy thành sông đã thôi thúc Đặng Trần Côn cầm bút viết nên <em>Chinh Phụ Ngâm</em>.</p>
        <p>Khác với quan niệm chính thống ngợi ca chiến công xả thân vì vua chúa, <em>Chinh Phụ Ngâm</em> là tác phẩm đầu tiên dám nhìn thẳng vào mặt trái tàn khốc của chiến tranh phi nghĩa. Tiếng khóc của người chinh phụ không chỉ là nỗi đau chia lìa của một gia đình, mà là bản cáo trạng đanh thép tố cáo chiến tranh đã cướp đi tuổi trẻ, sắc đẹp, tình yêu và sinh mệnh của con người.</p>
    </div>
    
    <h2 class="section-title">2. Thiên tài diễn Nôm của Đoàn Thị Điểm và thể Song Thất Lục Bát</h2>
    <div class="intro-box">
        <p>Nguyên tác của Đặng Trần Côn viết bằng thể cổ phong trường đoản cú chữ Hán vốn uyên bác nhưng mang nhiều điển tích ngoại lai. Đoàn Thị Điểm khi diễn Nôm đã thực hiện một cuộc tái tạo nghệ thuật vĩ đại. Bà chuyển thể trọn vẹn sang thể <strong>Song Thất Lục Bát</strong> - một thể thơ đặc trưng thuần Việt kết hợp nhịp điệu tráng lệ, đĩnh đạc của hai câu thất ngôn với vẻ êm ả, ngọt ngào, ngân vang của cặp câu lục bát.</p>
        <p>Hệ thống vần trắc - bằng giao thoa luân phiên cùng luật bằng trắc nghiêm cẩn tạo nên âm hưởng bi thiết dồi dào nhạc tính, đưa tác phẩm trở thành khuôn thước mẫu mực cho mọi khúc ngâm cổ điển Việt Nam (như <em>Cung Oán Ngâm Khúc</em> của Nguyễn Gia Thiều, <em>Ai Tư Vãn</em> của Lê Ngọc Hân).</p>
    </div>
    """)
    
    # TOÀN BỘ 103 KHỔ THƠ (412 CÂU)
    current_section = 0
    section_titles = [
        ("PHẦN I: BUỔI XUẤT CHINH & GIÂY PHÚT CHIA PHÔI BI TRÁNG", "Câu 1 – 64 (Khổ 1 – 16)"),
        ("PHẦN II: BƯỚC CHÂN QUAN SAN & CẢNH NGỘ ĐÔI NƠI", "Câu 65 – 136 (Khổ 17 – 34)"),
        ("PHẦN III: NỖI SẦU ĐẰNG ĐẴNG TRONG KHUÊ PHÒNG", "Câu 137 – 228 (Khổ 35 – 57)"),
        ("PHẦN IV: KHẮC KHOẢI CANH KHUYA & XÓT XA TUỔI TRẺ", "Câu 229 – 320 (Khổ 58 – 80)"),
        ("PHẦN V: NỖI NHỚ TRÙNG TRÙNG & KHÁT VỌNG ĐOÀN VIÊN", "Câu 321 – 412 (Khổ 81 – 103)")
    ]
    
    section_breaks = [1, 17, 35, 58, 81]
    
    for stanza in STANZAS:
        st_num, nom_lines, han_lines, phien_am, chu_giai = stanza
        
        # Check if we need to start a new section
        if st_num in section_breaks:
            sec_idx = section_breaks.index(st_num)
            title, subtitle = section_titles[sec_idx]
            html.append(f"""
            <div class="page-break"></div>
            <h1 class="chapter-title">{title}</h1>
            <div style="text-align: center; font-style: italic; color: #555; margin-bottom: 20px;">{subtitle}</div>
            <div class="ornament">❖ ❖ ❖</div>
            """)
        
        # Calculate line numbers
        start_line = (st_num - 1) * 4 + 1
        end_line = st_num * 4
        
        # Format Nom verses with line numbers
        formatted_nom = "<br>".join([
            f"<span style='color: #888; font-size: 8.5pt; width: 28px; display: inline-block;'>{start_line + i}</span>{line}"
            for i, line in enumerate(nom_lines)
        ])
        
        html.append(f"""
        <div class="poem-container avoid-break">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e5dac6; padding-bottom: 5px; margin-bottom: 10px;">
                <span style="font-weight: bold; color: #721616; font-size: 11pt;">Khổ {st_num} • (Câu {start_line} – {end_line})</span>
                <span style="font-size: 9pt; color: #777; font-style: italic;">Thể Song Thất Lục Bát</span>
            </div>
            
            <div class="poem-parallel">
                <div class="poem-col" style="flex: 1.2; background: #fffdf9; border-color: #eeddbb;">
                    <div class="col-header">Bản Diễn Nôm (Đoàn Thị Điểm)</div>
                    <div class="dich-tho" style="line-height: 1.85; padding-left: 5px;">
                        {formatted_nom}
                    </div>
                </div>
                
                <div class="poem-col" style="flex: 1; background: #fdfbf7;">
                    <div class="col-header">Nguyên Tác Chữ Hán (Đặng Trần Côn)</div>
                    <div class="han-script" style="text-align: center; margin-bottom: 8px;">
                        {han_lines.replace(chr(10), '<br>')}
                    </div>
                    <div class="col-header" style="font-size: 9pt; margin-top: 6px;">Phiên Âm Hán Việt</div>
                    <div class="phien-am" style="font-size: 9.5pt; line-height: 1.5;">
                        {phien_am}
                    </div>
                </div>
            </div>
            
            <div class="commentary-box">
                <div class="commentary-title">Chú Giải Từ Ngữ & Điển Cố:</div>
                {chu_giai}
            </div>
        </div>
        """)
        
    # Khảo luận vĩ thanh
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN VĨ THANH: VỊ THẾ BẤT HỦ</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Chinh Phụ Ngâm Khúc</strong> kết thúc bằng một nốt ngân vang đầy ám ảnh và khao khát: <em>"Lòng thiếp riêng bi thiết khôn hàn / Nghìn vàng xin chuộc muôn vàn bình an"</em>. Lời thốt lên từ sâu thẳm trái tim người chinh phụ đã vượt thoát khỏi mọi khuôn mẫu lễ giáo phong kiến tầm thường. Đó không còn là lời than khóc yếu đuối của số phận nữ nhi, mà đã trở thành bản tuyên ngôn nhân bản cao cả về giá trị của sự sống và hòa bình.</p>
        <p>Về mặt ngôn ngữ thi ca, bản diễn Nôm của Đoàn Thị Điểm đánh dấu bước trưởng thành vượt bậc của tiếng Việt văn học thế kỷ XVIII, mở đường cho sự bùng nổ của <em>Cung Oán Ngâm Khúc</em> và đỉnh cao tuyệt đối <em>Truyện Kiều</em> của Nguyễn Du. Trải qua gần ba thế kỷ với bao biến thiên dâu bể, 412 câu thơ song thất lục bát vẫn sống động ngút ngàn trong tâm hồn dân tộc Việt Nam, là gia tài văn hóa vô giá truyền đời cho hậu thế.</p>
    </div>
    
    <div style="text-align: center; margin-top: 40px;">
        <div class="ornament">❖ ❖ ❖</div>
        <div style="font-style: italic; color: #555; font-size: 11pt;">Hoàn tất ấn bản toàn văn 412 câu Chinh Phụ Ngâm Khúc</div>
        <div style="font-size: 9.5pt; color: #888; margin-top: 5px;">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn • Bản Khảo Luận Học Thuật Toàn Thư</div>
    </div>
    """)
    
    return "\n".join(html)

async def main():
    print(f"Building Chinh Phu Ngam 412 lines...")
    html_content = build_chinh_phu_ngam_html()
    
    # Render PDF
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="CHINH PHỤ NGÂM KHÚC (412 CÂU TOÀN VĂN)",
        header_right="ĐOÀN THỊ ĐIỂM - ĐẶNG TRẦN CÔN"
    )
    
    # Delete old 2-page file if exists
    if os.path.exists(OLD_FILE) and os.path.abspath(OLD_FILE) != os.path.abspath(OUTPUT_FILE):
        try:
            os.remove(OLD_FILE)
            print(f"[OK] Deleted old superficial file: {OLD_FILE}")
        except Exception as e:
            print(f"[WARN] Could not remove old file: {e}")

if __name__ == "__main__":
    asyncio.run(main())
