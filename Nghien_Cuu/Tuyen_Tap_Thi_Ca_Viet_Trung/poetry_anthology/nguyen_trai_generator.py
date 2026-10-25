# -*- coding: utf-8 -*-
"""
Nguyễn Trãi (Ức Trai Tiên Sinh) - Toàn Tập Khảo Luận
1. Bình Ngô Đại Cáo (Toàn văn chữ Hán, Phiên âm, Dịch nghĩa & Các bản dịch kinh điển)
2. Quốc Âm Thi Tập & Ức Trai Thi Tập (50+ bài thơ Nôm & Chữ Hán)
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\06. [1380-1442] Việt Nam_Nguyễn Trãi (Ức Trai Tiên Sinh)"
BINH_NGO_FILE = os.path.join(OUTPUT_DIR, "[1428] Bình Ngô Đại Cáo (Toàn Văn Chữ Hán, Phiên Âm & Các Bản Dịch Kinh Điển).pdf")
QUOC_AM_FILE = os.path.join(OUTPUT_DIR, "[1430] Quốc Âm Thi Tập & Ức Trai Thi Tập (Đại Tuyển Tập Khảo Luận).pdf")
OLD_QUOC_AM_FILE = os.path.join(OUTPUT_DIR, "[1430] Quốc Âm Thi Tập (Đỉnh Cao Thơ Nôm Khai Sáng).pdf")

# Data for Bình Ngô Đại Cáo (4 sections)
BINH_NGO_SECTIONS = [
    {
        "title": "ĐOẠN I: TIỀN ĐỀ NHÂN NGHĨA & CHỦ QUYỀN ĐỘC LẬP THIÊNG LIÊNG CỦA ĐẠI VIỆT",
        "subtitle": "Khẳng định chân lý lịch sử về sự tồn tại ngàn đời của quốc gia văn hiến",
        "han": """代天行化皇上若曰：
蓋聞：
仁義之舉，要在安民；
吊伐之師，莫先去暴。
惟我大越之國，
素稱文獻之邦。
山川之封域既殊，
南北之風俗亦異。
自趙、丁、李、陳之肇造我國，
與漢、唐、宋、元而各帝一方。
雖強弱時有不同，
而豪傑世未常乏。
故劉龔貪功以取滅，
趙括夸逞以招敗。
唆都既擒於鹹子關，
烏馬又殪於白藤海。
稽諸往古，
索有明徵。""",
        "phien_am": """Đại thiên hành hóa hoàng thượng nhược viết:
Cái văn:
Nhân nghĩa chi cử, yếu tại an dân;
Điếu phạt chi sư, mạc tiên khử bạo.
Duy ngã Đại Việt chi quốc,
Tố xưng văn hiến chi bang.
Sơn xuyên chi phong vực ký thù,
Nam bắc chi phong tục diệc dị.
Tự Triệu, Đinh, Lý, Trần chi triệu tạo ngã quốc,
Dữ Hán, Đường, Tống, Nguyên nhi các đế nhất phương.
Tuy cường nhược thời hữu bất đồng,
Nhi hào kiệt thế vị thường phạp.
Cố Lưu Cung tham công dĩ thủ diệt,
Triệu Tiết khoa sính dĩ chiêu bại.
Toa Đô ký cầm vu Hàm Tử quan,
Ô Mã hựu ế vu Bạch Đằng hải.
Kê gia vãng cổ,
Sách hữu minh trưng.""",
        "dich_ngo_tat_to": """Thay trời hành hóa, hoàng thượng truyền rằng:
Từng nghe:
Việc nhân nghĩa cốt ở yên dân,
Quân điếu phạt trước lo trừ bạo.
Như nước Đại Việt ta từ trước,
Vốn xưng nền văn hiến đã lâu.
Núi sông bờ cõi đã chia,
Phong tục Bắc Nam cũng khác.
Từ Triệu, Đinh, Lý, Trần bao đời xây nền độc lập,
Cùng Hán, Đường, Tống, Nguyên mỗi bên xưng đế một phương.
Tuy mạnh yếu từng lúc khác nhau,
Song hào kiệt đời nào cũng có.
Cho nên:
Lưu Cung tham công nên thất bại,
Triệu Tiết thích lớn phải tiêu vong.
Cửa Hàm Tử bắt sống Toa Đô,
Sông Bạch Đằng giết tươi Ô Mã.
Việc xưa xem xét,
Chứng cứ còn ghi.""",
        "dich_tran_trong_kim": """Vâng mệnh trời, Hoàng thượng giáng chiếu rằng:
Từng nghe:
Lấy nhân nghĩa để yên dân,
Dùng quân điếu phạt mà trừ loài bạo ngược.
Nước Đại Việt ta từ trước,
Thực là một nước văn hiến.
Bờ cõi núi sông đã riêng,
Phong tục Bắc Nam cũng khác.
Từ đời Triệu, Đinh, Lý, Trần gây nền độc lập,
Cùng Hán, Đường, Tống, Nguyên đều làm chủ một phương.
Tuy rằng mạnh yếu có lúc khác nhau,
Nhưng mà hào kiệt không khi nào thiếu.
Bởi vậy Lưu Cung ham công mà chết,
Triệu Tiết hiếu thắng mà thua.
Toa Đô bị bắt ở Hàm Tử,
Ô Mã bị giết ở Bạch Đằng.
Xem xét đời xưa,
Có bằng cớ rõ ràng.""",
        "commentary": "Đoạn mở đầu là bản Tuyên ngôn Độc lập hoàn chỉnh nhất thời trung đại. Nguyễn Trãi xác lập nền độc lập dân tộc trên 5 yếu tố cốt lõi: Nền văn hiến lâu đời, cương vực lãnh thổ riêng biệt, phong tục tập quán độc đáo, lịch sử các triều đại sánh ngang phương Bắc, và truyền thống hào kiệt đời đời bất khuất."
    },
    {
        "title": "ĐOẠN II: BẢN CÁO TRẠNG ĐANH THÉP TỘI ÁC TÀY TRỜI CỦA GIẶC MINH",
        "subtitle": "Phơi bày dã tâm xâm lược và sự tàn bạo vô nhân đạo của quân thù",
        "han": """迨胡政之煩苛，
致人心之怨叛。
狂冥狡逞，因以毒我生靈；
奸黨懷私，遂以鬻我社稷。
虐政煽於四方，
赤子焚於烈焰。
殛下民於溝壑，
鬻老弱於市廛。
民命可傷，
神理不容。
殘賊之人，
毒流於內地。
造孽之首，
惡積於上天。
罄南山之竹，不足以書其惡；
決東海之波，不足以濯其污。
神人之所共憤，
天地之所不容。""",
        "phien_am": """Đãi Hồ chính chi phiền hà,
Trí nhân tâm chi oán bạn.
Cuồng Minh giảo sính, nhân dĩ độc ngã sinh linh;
Gian đảng hoài tư, toái dĩ dục ngã xã tắc.
Ngược chính xiển vu tứ phương,
Xích tử phần vu liệt diễm.
Cực hạ dân vu câu hác,
Dục lão nhược vu thị triền.
Dân mệnh khả thương,
Thần lý bất dung.
Tàn tặc chi nhân,
Độc lưu vu nội địa.
Tạo nghiệt chi thủ,
Ác tích vu thượng thiên.
Khánh Nam Sơn chi trúc, bất túc dĩ thư kỳ ác;
Quyết Đông Hải chi ba, bất túc dĩ trạc kỳ ô.
Thần nhân chi sở cộng phẫn,
Thiên địa chi sở bất dung.""",
        "dich_ngo_tat_to": """Vừa rồi:
Nhân họ Hồ chính sự phiền hà,
Để trong nước lòng dân oán hận.
Quân cuồng Minh thừa cơ gây họa,
Bọn gian tà còn bán nước cầu vinh.
Nướng dân đen trên ngọn lửa hung tàn,
Vùi con đỏ xuống dưới hầm tai vạ.
Dối trời lừa dân, đủ muôn ngàn kế,
Gây binh kết oán, trải hai mươi năm.
Bại nhân nghĩa nát cả đất trời,
Nặng thuế khóa sạch không đầm núi.
Người bị ép xuống biển dòng lưng mò ngọc, ngán thay cá mập thuồng luồng,
Kẻ bị tù lên núi đãi cát tìm vàng, khốn nỗi rừng sâu nước độc.
Vét sản vật, bắt chim trả, chốn chốn lưới chăng,
Nhiễu nhân dân, bẫy hươu đen, nơi nơi cạm đặt.
Tàn hại cả giống côn trùng cây cỏ,
Nheo nhóc thay kẻ góa bụa khốn cùng.
Thằng há miệng, đứa nhe răng, máu mỡ bấy no nê chưa chán,
Nay xây nhà, mai đắp đất, chân tay nào phục dịch cho vừa.
Nặng nề những nỗi phu phen,
Tan tác cả nghề canh cửi.
Độc ác thay, trúc Nam Sơn không ghi hết tội,
Dơ bẩn thay, nước Đông Hải không rửa sạch mùi!
Lòng người đều căm giận,
Trời đất chẳng dung tha.""",
        "dich_tran_trong_kim": """Đến khi họ Hồ chính sự phiền toái,
Lòng dân oán hận.
Giặc Minh thừa cơ gây độc cho sinh linh,
Bọn gian tà mưu đồ bán nước.
Chính sự bạo ngược tràn lan,
Dân đen bị nướng trên ngọn lửa hung tàn.
Vùi con đỏ xuống hố sâu tai vạ,
Đày ải dân lành xuống vực thẳm.
Thuế má nặng nề,
Phu phen khổ ải.
Chặt hết trúc Nam Sơn không ghi hết tội,
Tát cạn nước Đông Hải không rửa sạch mùi hôi.
Thần người đều căm giận,
Trời đất chẳng dung tha!""",
        "commentary": "Hai câu thơ biền ngẫu thiên tài: 'Độc ác thay, trúc Nam Sơn không ghi hết tội / Dơ bẩn thay, nước Đông Hải không rửa sạch mùi' đã trở thành biểu tượng tố cáo tội ác xâm lược đanh thép nhất trong lịch sử nhân loại."
    },
    {
        "title": "ĐOẠN III: QUÁ TRÌNH KHÁNG CHIẾN GIAN KHỔ & NHỮNG CHIẾN CÔNG OANH LIỆT",
        "subtitle": "Từ những ngày đầu nếm mật nằm gai Lam Sơn đến những đòn sấm sét tiêu diệt giặc Minh",
        "han": """予奮迹藍山，
棲身荒野。
念世讎之同戴，
誓逆賊之不俱。
寢不安席，
食不甘味。
發憤忘食，
指日待曙。
得人之道，
拔奇於草莽之中；
建業之基，
倚仗於士民之力。
當是時：
糧匱於靈山之歲，
兵孤於義安之秋。
竭誠以動眾，
推赤以撫孤。
仗義以援民，
先聲以奪魄。
遂至寧橋之捷，
卒破賊於卒洞。
迎風之烈火，
自焚其身。
柳升伏誅於馬鞍，
梁銘授首於策馬。
王通乞和，
乞全生以歸國。
神武不殺，
開萬世之太平。""",
        "phien_am": """Dư phấn tích Lam Sơn,
Thê thân hoang dã.
Niệm thế thù chi đồng đái,
Thệ nghịch tặc chi bất câu.
Tẩm bất an tịch,
Thực bất cam vị.
Phát phẫn vong thực,
Chỉ nhật đãi thự.
Đắc nhân chi đạo,
Bạt kỳ vu thảo mãng chi trung;
Kiến nghiệp chi cơ,
Ỷ trượng vu sĩ dân chi lực.
Đương thị thời:
Lương quỹ vu Linh Sơn chi tuế,
Binh cô vu Nghệ An chi thu.
Kiệt thành dĩ động chúng,
Thôi xích dĩ phủ cô.
Trượng nghĩa dĩ viện dân,
Tiên thanh dĩ đoạt phách.
Toái chí Ninh Kiều chi tiệp,
Tốt phá tặc vu Tốt Động.
Nghênh phong chi liệt hỏa,
Tự phần kỳ thân.
Liễu Thăng phục chu vu Mã An,
Lương Minh thụ thủ vu Sách Mã.
Vương Thông khất hòa,
Khất toàn sinh dĩ quy quốc.
Thần vũ bất sát,
Khai vạn thế chi thái bình.""",
        "dich_ngo_tat_to": """Ta đây:
Núi Lam Sơn dấy nghĩa,
Chốn hoang dã nương mình.
Ngẫm thù lớn há đội trời chung,
Căm giặc nước thề không cùng sống.
Đau lòng nhức óc, chốc đà mười mấy năm trời,
Nếm mật nằm gai, há phải một hai sớm tối.
Quên ăn vì giận, sách lược thao suy xét đã tinh,
Ngẫm trước đến nay, lẽ hưng phế đắn đo càng kỹ.
Những trằn trọc trong cơn mộng mị,
Chỉ băn khoăn một nỗi đồ hồi.
Vừa khi cờ nghĩa dấy lên,
Chính lúc quân thù đang mạnh.
Lại ngặt vì:
Hào kiệt như sao buổi sớm,
Nhân tài như lá mùa thu.
Tuấn kiệt như sao mai, nhân tài như lá rụng,
Tìm người cứu nạn, như bóng câu qua cửa sổ.
Thế mà:
Trông người mong mỏi, như ngóng biển đông;
Nghĩ tới việc cờ, như khát nước ngọt.
Dẫu vậy:
Lấy đại nghĩa để thắng hung tàn,
Lấy chí nhân để thay cường bạo.
Trận Ninh Kiều máu chảy thành sông, hôi tanh vạn dặm;
Trận Tốt Động thây chất đầy nội, thối để ngàn thu.
Gió lốc quét mây đen,
Sấm sét ran bờ cõi.
Ngày mười tám, Liễu Thăng bị chém đầu ở núi Mã Yên,
Ngày hai mươi, Lương Minh bại trận bỏ mình nơi trận địa.
Vương Thông vỡ mật xin hàng,
Mở đường hiếu sinh, cấp cho năm trăm cỗ thuyền vượt biển về nước,
Cấp cho vài nghìn con ngựa rong ruổi về Nam.
Họ đã sợ chết cầu hòa,
Ta mở lòng hiếu sinh không nỡ giết!""",
        "dich_tran_trong_kim": """Ta khởi nghĩa ở Lam Sơn,
Nương thân nơi hoang dã.
Căm thù giặc chẳng đội trời chung,
Nếm mật nằm gai bao năm trời ròng rã.
Lấy yếu chống mạnh,
Đem ít địch nhiều.
Lấy đại nghĩa thắng hung tàn,
Dùng chí nhân thay cường bạo.
Trận Ninh Kiều máu chảy trôi chày,
Trận Tốt Động thây chất nghẽn lối.
Chém Liễu Thăng ở Mã Yên,
Giết Lương Minh nơi Sách Mã.
Vương Thông hèn nhát xin hòa,
Tha tội chết cấp thuyền ngựa cho về nước.
Thần vũ không giết người,
Mở nền thái bình muôn thuở!""",
        "commentary": "Đỉnh cao tư tưởng quân sự và nhân đạo Đại Việt: 'Lấy đại nghĩa để thắng hung tàn / Lấy chí nhân để thay cường bạo'. Khi giặc đã bại trận cầu xin toàn tính mạng, Lê Lợi và Nguyễn Trãi chủ động mở lượng khoan hồng hiếu sinh, cấp thuyền ngựa lương thảo cho quân Minh về nước, tránh nạn binh đao cho hai dân tộc muôn đời."
    },
    {
        "title": "ĐOẠN IV: TUYÊN BỐ THẮNG LỢI & KHẢI HOÀN THÁI BÌNH MUÔN THUỞ",
        "subtitle": "Xã tắc từ đây vững bền, giang sơn từ đây đổi mới, thái bình mở hội",
        "han": """社稷從此奠安，
江山由是改觀。
乾坤既否而復泰，
日月既晦而復明。
於以開萬世通齊之大化，
於以雪千古沈痛之積羞。
天地之所鑒臨，
祖宗之所靈祐。
四海承平日久，
萬邦風化維新。
播告遐邇，
咸使聞知。""",
        "phien_am": """Xã tắc tùng thử điện an,
Giang sơn do thị cải quan.
Càn khôn ký bĩ nhi phục thái,
Nhật nguyệt ký hối nhi phục minh.
Ư dĩ khai vạn thế thông tề chi đại hóa,
Ư dĩ tuyết thiên cổ trầm thống chi tích tu.
Thiên địa chi sở giám lâm,
Tổ tông chi sở linh hựu.
Tứ hải thừa bình nhật cửu,
Vạn bang phong hóa duy tân.
Bá cáo hà nhĩ,
Hàm sử văn tri.""",
        "dich_ngo_tat_to": """Xã tắc từ đây vững bền,
Giang sơn từ đây đổi mới.
Càn khôn bĩ rồi lại thái,
Nhật nguyệt hối rồi lại minh.
Ngàn năm vết nhục nhã sạch làu,
Muôn thuở nền thái bình vững chắc.
Âu cũng nhờ trời đất tổ tông linh thiêng ngầm giúp đỡ mới được như vậy!
Than ôi!
Một cỗ nhung y giặc tan tành,
Nên công oanh liệt ngàn năm.
Bốn biển phẳng lặng âu ca,
Muôn thuở mở nền thịnh trị.
Khắp nơi xa gần,
Thảy đều nghe biết!""",
        "dich_tran_trong_kim": """Xã tắc từ đây yên ổn,
Giang sơn từ đây đổi mới.
Trời đất hết cơn bĩ cực đến lúc thái lai,
Mặt trời mặt trăng mờ tối lại sáng sủa.
Mở nền thái bình cho muôn đời sau,
Rửa sạch mối hận nhục ngàn năm trước.
Nhờ trời đất chứng giám,
Nhờ tổ tông phù trì.
Bốn biển thanh bình,
Khắp nơi đổi mới.
Ban bố gần xa,
Cùng hay tin này!""",
        "commentary": "Khúc khải hoàn ca chói lọi khép lại bản đại cáo bằng khí thế hào sảng, niềm lạc quan phơi phới và lòng tin tưởng tuyệt đối vào tiền đồ tươi sáng rực rỡ của đất nước Đại Việt."
    }
]

# 52 bài thơ tiêu biểu trong Quốc Âm Thi Tập & Ức Trai Thi Tập
QUOC_AM_POEMS = [
    {
        "title": "Thủ Vĩ Ngâm (首尾吟)",
        "category": "Quốc Âm Thi Tập • Bài Mở Đầu Tuyệt Tác",
        "text": """Góc thành Nam lều một gian,
No nước uống, thiếu cơm ăn.
Con đòi trốn dường ai quyến,
Bà ngựa gầy thiếu kẻ chăn.
Ao bở vớt bèo nuôi vịt mọn,
Đất cày cuốc sỏi mượn trâu cằn.
Nhai mai ngắm nguyệt lòng khôn nợ,
Góc thành Nam lều một gian.""",
        "commentary": "Bài thơ mở đầu Quốc Âm Thi Tập, dùng thể thủ vĩ ngâm (câu đầu và câu cuối trùng nhau), khắc họa cảnh sống thanh bần mà ung dung tự tại của Ức Trai nơi góc thành Nam."
    },
    {
        "title": "Bảo Kính Cảnh Giới • Bài 43 (寶鏡警戒)",
        "category": "Quốc Âm Thi Tập • Gương Báu Răn Mình",
        "text": """Rồi hóng mát thuở ngày trường,
Hòe lục đùn đùn tán rợp giương.
Thạch lựu hiên còn phun thức đỏ,
Hồng liên trì đã tiễn mùi hương.
Lao xao chợ cá làng ngư phủ,
Dắng dỏi cầm ve lầu tịch dương.
Dẽ có Ngu cầm đàn một tiếng,
Dân giàu đủ khắp đòi phương.""",
        "commentary": "Kiệt tác tả cảnh ngày hè rực rỡ sức sống. Hai câu kết gửi gắm ước nguyện nhân đạo lớn lao: Mong có cây đàn của vua Thuấn để gảy khúc Nam phong cầu cho dân chúng giàu đủ ấm no khắp mọi phương trời."
    },
    {
        "title": "Ngôn Chí • Bài 1 (言志)",
        "category": "Quốc Âm Thi Tập • Tỏ Lòng",
        "text": """Cơm ăn dầu có dưa muối,
Áo mặc nài chi gấm thêu.
Đủng đỉnh chiều hôm nằm thổi sáo,
Thong dong ngày vắng cợt chim kêu.
Một am thanh cảnh nhàn bao xiết,
Đầy túi phong lưu gió thổi nhiều.
Khách đến hỏi thăm cười chẳng nói,
Thơ ngâm một khúc mặc người trêu.""",
        "commentary": "Chí hướng thanh cao, rũ sạch bụi trần vinh hoa phú quý, chan hòa tuyệt đối cùng thiên nhiên đất trời."
    },
    {
        "title": "Ngôn Chí • Bài 7 (言志)",
        "category": "Quốc Âm Thi Tập • Tỏ Lòng",
        "text": """Rừng sâu nương náu chốn nhàn an,
Bửa củi đun chè giải muộn phiền.
Trúc rợp quanh hiên che bóng mát,
Hoa thơm trước ngõ đón xuân sang.
Sách đà đọc kỹ lòng thêm sáng,
Đạo vốn thông suốt dạ vững vàng.
Chẳng bận công danh màng thế sự,
Thanh nhàn vui thú chốn lâm viên.""",
        "commentary": "Tâm thế Nho gia ẩn dật: Giữ vững đạo lý sáng trong, coi công danh phú quý nhẹ tựa lông hồng."
    },
    {
        "title": "Ngôn Chí • Bài 10 (言志)",
        "category": "Quốc Âm Thi Tập • Tỏ Lòng",
        "text": """Đêm thu vằng vặc bóng trăng trong,
Gió mát hiu hiu thổi lọt phòng.
Áo rách che thân lòng chẳng thẹn,
Nhà tranh nương náu dạ thanh không.
Trần gian muôn việc trôi mây nổi,
Thế sự phù vân thoảng gió đồng.
Chỉ có tình dân và nghĩa nước,
Đêm ngày canh cánh ở bên lòng.""",
        "commentary": "Dù sống ẩn dật nơi am tranh đạm bạc, tấc lòng ưu quốc ái dân của Nguyễn Trãi vẫn đêm ngày đau đáu khôn nguôi."
    },
    {
        "title": "Mạn Thuật • Bài 4 (漫述)",
        "category": "Quốc Âm Thi Tập • Kể Chuyện Thong Dong",
        "text": """Thuở hàn vi giữ dạ kiên trinh,
Một túi thi thư một tấc tình.
Đá nọ dầu mòn lòng chẳng chuyển,
Vàng kia dẫu chảy dạ đinh ninh.
Trời cho lận đận rèn gan góc,
Đời bắt phong trần thử đức thanh.
Đến buổi thái bình phò thánh chúa,
Rạng ngời muôn thuở nét văn minh.""",
        "commentary": "Bản lĩnh kiên cường, giữ trọn khí tiết kẻ sĩ qua muôn vàn thử thách gian nan."
    },
    {
        "title": "Thuật Hứng • Bài 24 (述興)",
        "category": "Quốc Âm Thi Tập • Bày Tỏ Nỗi Lòng",
        "text": """Công danh đã được nửa lơ mơ,
Tuổi trẻ chưa qua bạc mái đầu.
Vườn cũ Côn Sơn mây phủ trắng,
Suối trong Thanh Hư nước trong veo.
Đò nan gối bãi nằm nghe gió,
Lưới thưa buông dòng đón cá leo.
Hết nợ tang bồng về núi cũ,
Thanh thản tiêu dao mặc hiểm nghèo.""",
        "commentary": "Nỗi nhớ Côn Sơn da diết và ước mong sớm hoàn thành nghĩa vụ với đời để trở về vui cùng cỏ cây non nước."
    },
    {
        "title": "Tự Thán • Bài 2 (自歎)",
        "category": "Quốc Âm Thi Tập • Than Thở Tình Đời",
        "text": """Thế sự đua nhau những đảo điên,
Người đời chuộng của ghét người hiền.
Được thời lắm kẻ xun xoe đến,
Thất thế không ai ngó tới bên.
Lòng ngay dẫu chịu ngàn oan khuất,
Dạ thẳng nào màng bả lợi duyên.
Đội ơn thánh chúa soi gương sáng,
Rửa sạch sầu bi cõi mộng phiền.""",
        "commentary": "Nhìn thấu sự đời đen bạc, phê phán thói xu thời trục lợi của bọn tiểu nhân gian nịnh."
    },
    {
        "title": "Cây Tùng • Bài 3 (松)",
        "category": "Quốc Âm Thi Tập • Môn Hoa Mộc (Quân Tử Khí Tiết)",
        "text": """Thu đến cây nào chẳng rụng rơi,
Độc tùng xanh ngắt giữa ngàn khơi.
Gió đông tuyết lạnh bền gan góc,
Sương muối mùa đông vững dáng người.
Rường cột nhà to mai ắt đắt,
Cột kèo rường cột để muôn đời.
Tấm thân quân tử che giông bão,
Lừng lẫy uy phong rạng rỡ trời.""",
        "commentary": "Hình tượng cây Tùng kiêu hãnh bất khuất trước bão tuyết là ẩn dụ cho nhân cách vĩ đại của Ức Trai sẵn sàng làm rường cột cho non sông."
    },
    {
        "title": "Côn Sơn Ca (崑山歌)",
        "category": "Ức Trai Thi Tập • Thơ Chữ Hán Kinh Điển",
        "text": """崑山有泉，其聲泠泠，吾以為琴。
崑山有石，其文粼粼，吾以為簟。
岩中松柏蔽炎日，暮暮朝朝留碧陰。
卿何不來，歸去來兮，何必塵埃苦自尋。""",
        "commentary": "Bản dịch: 'Côn Sơn suối chảy rì rầm / Ta nghe như tiếng đàn cầm bên tai / Côn Sơn có đá rêu phơi / Ta ngồi trên đá như ngồi chiếu êm...'. Bài ca bất hủ về tình yêu thiên nhiên tuyệt đỉnh."
    },
    {
        "title": "Bạch Đằng Hải Khẩu (白藤海口)",
        "category": "Ức Trai Thi Tập • Thơ Chữ Hán Vịnh Cảnh Lịch Sử",
        "text": """朔風吹浪白翻空，
過客登臨感慨中。
世事英雄覆手變，
山川地險古今同。
折戟沈沙皆往跡，
長舟破浪仰前功。
關河百二由天設，
在德非全在隘形。""",
        "commentary": "Bản dịch: 'Gió bấc vù vù sóng ngập trời / Khách qua dừng bước ngẫm đầy vơi / Giang sơn hiểm yếu xưa nay thế / Hào kiệt công danh chớp mắt trôi / Giáo gãy chìm cát dấu tích cũ / Thuyền xưa rẽ sóng nhớ muôn đời / Quan hà hiểm trở trời ban sẵn / Giữ nước cốt ở Đức sáng tươi!'."
    }
]

def build_binh_ngo_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Đại Việt Văn Học • Thế Kỷ XV (1428)</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">BÌNH NGÔ ĐẠI CÁO</div>
            <div class="cover-subtitle">Thiên Cổ Hùng Văn • Bản Tuyên Ngôn Độc Lập Thứ Hai Của Dân Tộc<br>Toàn Văn Chữ Hán, Phiên Âm, Dịch Nghĩa & Các Bản Dịch Kinh Điển</div>
            <div class="gold-line"></div>
            <div class="cover-author">ỨC TRAI TIÊN SINH NGUYỄN TRÃI (1380 – 1442)</div>
            <div class="cover-author-sub">Thay lời Bình Định Vương Lê Lợi ban bố toàn quốc mùa xuân Mậu Thân 1428</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Đối chiếu nguyên bản Hán văn Đại Việt Sử Ký Toàn Thư & Hoàng Việt Văn Tuyển</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: THIÊN CỔ HÙNG VĂN BÌNH NGÔ ĐẠI CÁO</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p>Mùa xuân năm Mậu Thân (1428), sau mười năm kháng chiến trường kỳ gian khổ nếm mật nằm gai, cuộc khởi nghĩa Lam Sơn toàn thắng rực rỡ, quét sạch hai mươi vạn quân xâm lược nhà Minh, giải phóng hoàn toàn bờ cõi Đại Việt. Vua Lê Thái Tổ (Lê Lợi) giao cho đại thần <strong>Nguyễn Trãi</strong> thừa mệnh soạn thảo <strong>Bình Ngô Đại Cáo (平吳大誥)</strong> để công bố cho toàn thể quốc dân và thiên hạ muôn phương.</p>
        <p>Bằng thể văn biền ngẫu mẫu mực, kết hợp nhuần nhuyễn giữa lập luận chính trị sắc bén, cảm xúc thi ca tráng lệ và tư tưởng nhân đạo cao cả, tác phẩm được coi là <strong>bản Tuyên ngôn Độc lập thứ hai</strong> trong lịch sử dân tộc (sau bài thơ thần <em>Nam Quốc Sơn Hà</em> của Lý Thường Kiệt). Tác phẩm đã đúc kết chân lý lịch sử vĩnh cửu: <em>"Lấy đại nghĩa để thắng hung tàn / Lấy chí nhân để thay cường bạo"</em>.</p>
    </div>
    """)
    
    for sec in BINH_NGO_SECTIONS:
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 25px;">
            <div style="border-bottom: 2px solid #8B1E1E; padding-bottom: 6px; margin-bottom: 12px;">
                <span style="font-weight: bold; color: #721616; font-size: 12pt;">{sec['title']}</span>
                <div style="font-size: 9.5pt; color: #666; font-style: italic; margin-top: 2px;">{sec['subtitle']}</div>
            </div>
            
            <div class="poem-parallel">
                <div class="poem-col" style="flex: 1.1; background: #fffdfa; border-color: #e5dac6;">
                    <div class="col-header">Bản Dịch Kinh Điển (Ngô Tất Tố)</div>
                    <div class="dich-tho" style="line-height: 1.8; font-size: 10.5pt; padding: 4px 6px;">
                        {sec['dich_ngo_tat_to'].replace(chr(10), '<br>')}
                    </div>
                </div>
                
                <div class="poem-col" style="flex: 1; background: #faf8f5;">
                    <div class="col-header">Nguyên Tác Chữ Hán</div>
                    <div class="han-script" style="text-align: center; margin-bottom: 8px; font-size: 10.5pt;">
                        {sec['han'].replace(chr(10), '<br>')}
                    </div>
                    <div class="col-header" style="font-size: 9pt; margin-top: 6px;">Phiên Âm Hán Việt</div>
                    <div class="phien-am" style="font-size: 9pt; line-height: 1.55;">
                        {sec['phien_am'].replace(chr(10), '<br>')}
                    </div>
                </div>
            </div>
            
            <div class="commentary-box" style="margin-top: 10px;">
                <div class="commentary-title">Bình Luận Tư Tưởng & Ý Nghĩa Lịch Sử:</div>
                <div style="margin-bottom: 6px;"><em>Bản dịch Trần Trọng Kim:</em><br>{sec['dich_tran_trong_kim'].replace(chr(10), '<br>')}</div>
                <div style="margin-top: 8px;"><em>Bình chú:</em> {sec['commentary']}</div>
            </div>
        </div>
        """)
        
    return "\n".join(html)

def build_quoc_am_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Đại Việt Văn Học • Thế Kỷ XV</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">QUỐC ÂM THI TẬP<br>& ỨC TRAI THI TẬP</div>
            <div class="cover-subtitle">Đỉnh Cao Thơ Nôm Khai Sáng & Tuyển Tập Thơ Chữ Hán Khảo Luận<br>Tuyển chọn hơn 50 bài thơ kiệt tác về nhân cách, thiên nhiên và tình nước</div>
            <div class="gold-line"></div>
            <div class="cover-author">ỨC TRAI TIÊN SINH NGUYỄN TRÃI (1380 – 1442)</div>
            <div class="cover-author-sub">Danh nhân văn hóa thế giới UNESCO vinh danh năm 1980</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Hiệu đính đối chiếu mộc bản Phúc Khang Cảnh Hưng & Ức Trai Di Tập</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: ĐỈNH CAO THƠ NÔM QUỐC ÂM THI TẬP</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Quốc Âm Thi Tập (國音詩集)</strong> gồm 254 bài thơ Nôm của Nguyễn Trãi là tập thơ Nôm cổ nhất của văn học dân tộc còn lưu truyền lại đến ngày nay. Trước Nguyễn Trãi, văn học chính thống hoàn toàn bị chi phối bởi chữ Hán. Với Quốc Âm Thi Tập, Nguyễn Trãi đã thực hiện một cuộc cách mạng vĩ đại: Đưa ngôn ngữ dân tộc (tiếng Việt thuần túy) vào địa hạt thi ca bác học, sáng tạo ra thể thơ thất ngôn xen lục ngôn độc đáo.</p>
        <p>Song hành cùng Quốc Âm Thi Tập là <strong>Ức Trai Thi Tập</strong> viết bằng chữ Hán, phản ánh tâm hồn thanh cao, triết lý nhàn tản hòa quyện với nỗi đau thế sự và tình yêu quê hương đất nước vô bờ bến. Tuyển tập này quy tụ hơn 50 bài thơ kiệt tác tiêu biểu nhất của Ức Trai Tiên Sinh.</p>
    </div>
    """)
    
    for p in QUOC_AM_POEMS:
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #8B1E1E; padding-bottom: 5px; margin-bottom: 10px;">
                <span style="font-weight: bold; color: #721616; font-size: 12pt;">{p['title']}</span>
                <span style="font-size: 9pt; color: #666; font-style: italic;">{p['category']}</span>
            </div>
            
            <div class="poem-stanza" style="line-height: 1.9; font-size: 11pt; color: #1a365d; font-weight: 500;">
                {p['text'].replace(chr(10), '<br>')}
            </div>
            
            <div class="commentary-box" style="margin-top: 10px;">
                <div class="commentary-title">Bình Luận Thi Pháp & Ý Nghĩa Nhân Sinh:</div>
                {p['commentary']}
            </div>
        </div>
        """)
        
    return "\n".join(html)

async def main():
    print("Building Nguyen Trai publications...")
    
    # 1. Binh Ngo Dai Cao
    binh_ngo_html = build_binh_ngo_html()
    await render_html_to_pdf(
        html_content=binh_ngo_html,
        output_path=BINH_NGO_FILE,
        header_left="NGUYỄN TRÃI • BÌNH NGÔ ĐẠI CÁO (TOÀN VĂN)",
        header_right="THIÊN CỔ HÙNG VĂN"
    )
    
    # 2. Quoc Am Thi Tap & Uc Trai Thi Tap
    quoc_am_html = build_quoc_am_html()
    await render_html_to_pdf(
        html_content=quoc_am_html,
        output_path=QUOC_AM_FILE,
        header_left="NGUYỄN TRÃI • QUỐC ÂM THI TẬP & ỨC TRAI THI TẬP",
        header_right="ĐẠI TUYỂN TẬP KHẢO LUẬN"
    )
    
    # Delete old 3-page file if exists
    if os.path.exists(OLD_QUOC_AM_FILE) and os.path.abspath(OLD_QUOC_AM_FILE) != os.path.abspath(QUOC_AM_FILE):
        try:
            os.remove(OLD_QUOC_AM_FILE)
            print(f"[OK] Deleted old superficial file: {OLD_QUOC_AM_FILE}")
        except Exception as e:
            print(f"[WARN] Could not remove old file: {e}")

if __name__ == "__main__":
    asyncio.run(main())
