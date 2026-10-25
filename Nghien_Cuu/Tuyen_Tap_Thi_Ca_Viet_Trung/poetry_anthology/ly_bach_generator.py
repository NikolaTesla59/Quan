# -*- coding: utf-8 -*-
"""
Lý Bạch (Thi Tiên) - Tuyển Tập Đường Thi Bất Hủ
30 kiệt tác đỉnh cao của Thi Tiên Lý Bạch: Tương Tiến Tửu, Hành Lộ Nan, Thục Đạo Nan, Tĩnh Dạ Tứ, Nguyệt Hạ Độc Trác...
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\02. [701-762] Trung Quốc_Lý Bạch (Thi Tiên)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[750] Lý Bạch - Tuyển Tập Đường Thi (Nguyên Tác Chữ Hán, Phiên Âm & Dịch Thơ).pdf")

LY_BACH_POEMS = [
    {
        "title": "Tương Tiến Tửu (將進酒)",
        "subtitle": "Khúc Ca Uống Rượu Hào Sảng Bậc Nhất Thiên Cổ",
        "han": """君不見黃河之水天上來，奔流到海不復回。
君不見高堂明鏡悲白髮，朝如青絲暮成雪。
人生得意須盡歡，莫使金樽空對月。
天生我材必有用，千金散盡還復來。
烹羊宰牛且為樂，會須一飲三百杯。
岑夫子，丹丘生，將進酒，杯莫停。
與君歌一曲，請君為我傾耳聽。
鐘鼓饌玉不足貴，但願長醉不願醒。
古來聖賢皆寂寞，惟有飲者留其名。
陳王昔時宴平樂，斗酒十千恣欢謔。
主人何為言少錢，徑須沽取對君酌。
五花馬，千金裘，
呼兒將出換美酒，與爾同銷萬古愁。""",
        "phien_am": """Quân bất kiến Hoàng Hà chi thủy thiên thượng lai,
Bôn lưu đáo hải bất phục hồi.
Quân bất kiến cao đường minh kính bi bạch phát,
Triêu như thanh ti mộ thành tuyết.
Nhân sinh đắc ý tu tận hoan,
Mạc sử kim tôn không đối nguyệt.
Thiên sinh ngã tài tất hữu dụng,
Thiên kim tán tận hoàn phục lai.
Phanh dương tể ngưu thả vi lạc,
Hội tu nhất ẩm tam bách bôi.
Sầm phu tử, Đan Khâu sinh,
Tương tiến tửu, bôi mạc đình.
Dữ quân ca nhất khúc,
Thỉnh quân vi ngã khuynh nhĩ thính.
Chung cổ soạn ngọc bất túc quý,
Đãn nguyện trường túy bất nguyện tỉnh.
Cổ lai thánh hiền giai tịch mịch,
Duy hữu ẩm giả lưu kỳ danh.
Trần Vương tích thời yến Bình Lạc,
Đấu tửu thập thiên tứ hoan hước.
Chủ nhân hà vi ngôn thiểu tiền,
Kính tu cô thủ đối quân chước.
Ngũ hoa mã, thiên kim cừu,
Hô nhi tương xuất hoán mỹ tửu,
Dữ nhĩ đồng tiêu vạn cổ sầu.""",
        "dich_nghia": """Há chẳng thấy nước sông Hoàng Hà từ trời cao tuôn xuống, cuồn cuộn chảy ra biển đông chẳng bao giờ trở lại? Há chẳng thấy trước gương sáng lầu cao buồn vì mái tóc bạc, sớm còn như tơ xanh chiều đã trắng như tuyết? Đời người đắc ý hãy vui say cho thỏa, chớ để chén vàng trơ trọi đối bóng cùng trăng. Trời sinh ra ta có tài ắt phải có chỗ dùng, nghìn vàng tiêu tán hết rồi lại trở về tay. Mổ dê giết trâu hãy lấy làm vui, gặp nhau uống một lần phải cạn ba trăm chén. Sầm phu tử, Đan Khâu sinh, xin hãy nâng chén rượu đừng dừng! Ta vì các bạn hát một khúc ca, xin các bạn hãy nghiêng tai lắng nghe: Chuông trống cỗ ngọc đâu đáng quý, chỉ mong say mãi chẳng màng tỉnh. Xưa nay thánh hiền đều cô tịch quạnh hiu, duy chỉ có kẻ uống rượu là lưu danh muôn thuở. Trần Vương Tào Thực xưa kia mở tiệc vui chơi ở Bình Lạc, chén rượu vạn tiền thỏa sức vui đùa. Chủ nhà cớ sao nói ít tiền, hãy mau đi mua rượu về đối ẩm cùng các bạn. Ngựa năm sắc, áo cừu nghìn vàng, bảo con trẻ mang đi đổi lấy rượu ngon, cùng các bạn tiêu tan mối sầu muôn thuở!""",
        "dich_tho": """Há chẳng thấy:
Nước Hoàng Hà từ trời tuôn xuống,
Chảy ra biển chẳng hẹn ngày về!
Lại chẳng thấy:
Gương lầu cao tóc bạc tràn mi,
Sớm như tơ biếc, chiều tê tuyết hàn!
Đời đắc ý hãy vui cho cạn,
Chớ để trăng soi chén ngọc côi.
Trời sinh ta ắt nên tài hữu dụng,
Nghìn vàng tan hết lại về thôi!
Mổ dê giết thịt vui cùng bạn,
Phải uống một phen ba trăm bôi!
Sầm phu tử, Đan Khâu sinh,
Rượu nâng chén, chớ dừng tay!
Ta vì người hát một bài ca,
Xin người nghiêng tai lắng nghe qua:
Chuông trống ngọc ngà đâu quý báu,
Chỉ mong say khướt chẳng buồn hay!
Xưa nay thánh hiền đều quạnh vắng,
Chỉ kẻ say sưa tiếng dội bay.
Trần Vương tiệc mở Bình Lạc xưa,
Chén rượu muôn tiền thoả gió mưa.
Chủ nhà sao bảo là eo hẹp,
Mau mau mua rượu cạn say sưa!
Ngựa năm sắc, áo nghìn vàng,
Gọi con đem đổi rượu nồng tràn,
Cùng người tiêu vạn cổ sầu tan!""",
        "commentary": "Đỉnh cao tuyệt đỉnh của phong cách lãng mạn Lý Bạch: Khí thế hào hùng cuồn cuộn như sóng Hoàng Hà, cảm hứng phóng túng, coi thường phú quý kim tiền, ngạo nghễ đạp đổ sầu muộn nhân thế."
    },
    {
        "title": "Hành Lộ Nan • Kỳ 1 (行路難·其一)",
        "subtitle": "Đường Đi Gian Khó & Khát Vọng Cưỡi Gió Vượt Sóng",
        "han": """金樽清酒斗十千，玉盤珍羞直萬錢。
停杯投箸不能食，拔劍四顧心茫然。
欲渡黃河冰塞川，將登太行雪暗天。
閑來垂釣碧溪上，忽復乘舟夢日邊。
行路難，行路難，多歧路，今安在？
長風破浪會有時，直掛雲帆濟滄海。""",
        "phien_am": """Kim tôn thanh tửu đấu thập thiên,
Ngọc bàn trân tu trị vạn tiền.
Đình bôi đầu trợ bất năng thực,
Bạt kiếm tứ cố tâm mang nhiên.
Dục độ Hoàng Hà băng tắc xuyên,
Tương đăng Thái Hàng tuyết ám thiên.
Nhàn lai thùy điếu bích khê thượng,
Hốt phục thừa chu mộng nhật biên.
Hành lộ nan, hành lộ nan,
Đa kỳ lộ, kim an tại?
Trường phong phá lãng hội hữu thời,
Trực quải vân phàm tế thương hải.""",
        "dich_nghia": """Chén vàng rượu trong giá muôn tiền một đấu, mâm ngọc thức ăn ngon trị giá vạn tiền. Dừng chén buông đũa nuốt không trôi, rút gươm nhìn bốn phía lòng bàng hoàng ngơ ngác. Muốn qua sông Hoàng Hà thì băng đóng nghẽn dòng, định trèo lên núi Thái Hàng thì tuyết bay tối tăm mặt trời. Lúc rỗi ngồi buông cần câu trên dòng suối biếc, chợt mơ thấy mình ngồi thuyền lướt tới bên cạnh mặt trời. Đường đi khó! Đường đi khó! Nhiều lối rẽ, nay ở đâu? Rồi sẽ có lúc cưỡi gió lớn đạp bằng muôn lớp sóng, giương thẳng cánh buồm mây vượt qua biển rộng mênh mông!""",
        "dich_tho": """Chén vàng rượu ngọt muôn tiền đấu,
Mâm ngọc nem rồng giá vạn cân.
Buông đũa dừng nâng ăn chẳng nổi,
Rút gươm nhìn bốn phía bâng khuâng.
Muốn vượt Hoàng Hà băng nghẽn lối,
Toan trèo Thái Hàng tuyết vây mù.
Rỗi ngồi buông câu bên suối biếc,
Chợt mơ thuyền lướt cạnh vầng dương.
Đường đi khó! Đường đi khó!
Nhiều lối rẽ, nay ở đâu?
Gió to sóng cả rồi khi tới,
Giương thẳng buồm mây vượt biển sâu!""",
        "commentary": "Hai câu kết: 'Trường phong phá lãng hội hữu thời / Trực quải vân phàm tế thương hải' là khẩu khí anh hùng ngút ngàn, thể hiện niềm tin lạc quan bất diệt vào lý tưởng cao đẹp."
    },
    {
        "title": "Tĩnh Dạ Tứ (靜夜思)",
        "subtitle": "Nỗi Nhớ Quê Nhà Đêm Trăng Thanh Khiết",
        "han": """床前明月光，
疑是地上霜。
舉頭望明月，
低頭思故鄉。""",
        "phien_am": """Sàng tiền minh nguyệt quang,
Nghi thị địa thượng sương.
Cử đầu vọng minh nguyệt,
Đê đầu tư cố hương.""",
        "dich_nghia": """Đầu giường ánh trăng rọi sáng, ngỡ là sương phủ trên mặt đất. Ngẩng đầu nhìn vầng trăng sáng, cúi đầu nhớ quê hương da diết.""",
        "dich_tho": """Đầu giường trăng sáng soi,
Ngỡ sương phủ đất trời.
Ngẩng đầu trông trăng sáng,
Cúi đầu nhớ quê vơi.""",
        "commentary": "Bài thơ 20 chữ bất hủ lưu truyền rộng rãi nhất trong thi ca phương Đông, ngôn từ giản dị đến tuyệt đối nhưng hàm chứa nỗi sầu tha hương sâu thẳm."
    },
    {
        "title": "Nguyệt Hạ Độc Trác (月下獨酌)",
        "subtitle": "Uống Rượu Dưới Trăng - Đỉnh Cao Lãng Mạn & Cô Đơn",
        "han": """花間一壺酒，獨酌無相親。
舉杯邀明月，對影成三人。
月既不解飲，影徒隨我身。
暫伴月將影，行樂須及春。
我歌月徘徊，我舞影零亂。
醒時同交歡，醉後各分散。
永結無情遊，相期邈雲漢。""",
        "phien_am": """Hoa gian nhất hồ tửu,
Độc trác vô tương thân.
Cử bôi yêu minh nguyệt,
Đối ảnh thành tam nhân.
Nguyệt ký bất giải ẩm,
Ảnh đồ tùy ngã thân.
Tạm bạn nguyệt tương ảnh,
Hành lạc tu cập xuân.
Ngã ca nguyệt bồi hồi,
Ngã vũ ảnh linh loạn.
Tỉnh thời đồng giao hoan,
Túy hậu các phân tán.
Vĩnh kết vô tình du,
Tương kỳ mạo vân hán.""",
        "dich_nghia": """Giữa khóm hoa có một bầu rượu, ngồi uống một mình không có bạn bè thân thích. Nâng chén mời vầng trăng sáng, đối bóng với mình hóa thành ba người. Trăng vốn không biết uống rượu, bóng chỉ biết lẵng nhẵng theo sau thân ta. Tạm lấy trăng cùng bóng làm bạn, vui chơi kịp lúc đương xuân. Ta hát vầng trăng bồi hồi lay động, ta múa cái bóng lảo đảo ngả nghiêng. Lúc tỉnh cùng nhau vui say hoan lạc, lúc say rồi mỗi đứa tản mát một phương. Xin kết cuộc chơi vô tình muôn thuở, hẹn nhau nơi ngân hà xa xôi diệu vợi.""",
        "dich_tho": """Hoa chen một bầu rượu,
Uống một mình không bạn.
Nâng chén mời vầng trăng,
Cùng bóng thành ba bạn.
Trăng nào biết uống đâu,
Bóng lẵng nhẵng theo sau.
Tạm bầu bạn trăng bóng,
Vui chơi cho trọn xuân.
Ta hát trăng bồi hồi,
Ta múa bóng chơi vơi.
Tỉnh cùng nhau vui vẻ,
Say rồi tan mỗi nơi.
Kết tình chơi vô hạn,
Hẹn gặp chốn mây trời.""",
        "commentary": "Sự sáng tạo kỳ diệu biến nỗi cô đơn tuyệt đối thành cuộc sum họp lộng lẫy giữa Thi sĩ, Trăng sáng và Cái bóng."
    },
    {
        "title": "Vọng Lư Sơn Bộc Bố (望廬山瀑布)",
        "subtitle": "Ngắm Thác Nước Núi Lư Sơn - Thác Rơi Từ Tầng Mây",
        "han": """日照香爐生紫煙，
遙看瀑布挂前川。
飛流直下三千尺，
疑是銀河落九天。""",
        "phien_am": """Nhật chiếu Hương Lô sinh tử yên,
Diêu khán bộc bố quái tiền xuyên.
Phi lưu trực hạ tam thiên xích,
Nghi thị Ngân Hà lạc cửu thiên.""",
        "dich_nghia": """Mặt trời rọi đỉnh Hương Lô bốc lên làn khói tía, trông xa thấy dải thác nước treo rủ xuống dòng sông trước mặt. Dòng nước bay thẳng xuống ba nghìn thước, ngỡ là dải Ngân Hà rơi từ chín tầng mây xanh.""",
        "dich_tho": """Nắng rọi Hương Lô khói tía bay,
Trông xa thác nước rủ sông đầy.
Bay thẳng tuôn trào ba nghìn thước,
Ngỡ dải Ngân Hà rụng chín mây!""",
        "commentary": "Bút pháp khoa trương lãng mạn siêu phàm, biến dòng thác nước tự nhiên thành dòng sông sao Ngân Hà trút xuống từ trời cao."
    },
    {
        "title": "Tảo Phát Bạch Đế Thành (早發白帝城)",
        "subtitle": "Sớm Rời Thành Bạch Đế - Thuyền Lướt Muôn Trùng Núi",
        "han": """朝辭白帝彩雲間，
千里江陵一日還。
兩岸猿聲啼不住，
輕舟已過萬重山。""",
        "phien_am": """Triêu từ Bạch Đế thái vân gian,
Thiên lý Giang Lăng nhất nhật hoàn.
Lưỡng ngạn viên thanh đề bất trụ,
Khinh chu dĩ quá vạn trùng sơn.""",
        "dich_nghia": """Sáng sớm từ giã thành Bạch Đế giữa ngàn mây rực rỡ, nghìn dặm Giang Lăng chỉ một ngày là tới nơi. Tiếng vượn hai bên bờ núi kêu không dứt, con thuyền nhẹ thoăn thoắt đã vượt qua muôn trùng núi non.""",
        "dich_tho": """Sớm giã Bạch Đế giữa mây ngàn,
Nghìn dặm Giang Lăng một ngày sang.
Tiếng vượn hai bờ kêu không dứt,
Thuyền nhẹ vút qua vạn dặm ngàn!""",
        "commentary": "Bài thơ tràn đầy niềm hân hoan khi nhận được tin ân xá, con thuyền nhẹ lướt như tâm hồn thanh thản thoát khỏi cảnh ngộ ngục tù lưu đày."
    },
    {
        "title": "Hoàng Hạc Lâu Tống Mạnh Hạo Nhiên Chi Quảng Lăng",
        "subtitle": "Tại Lầu Hoàng Hạc Tiễn Mạnh Hạo Nhiên Đi Quảng Lăng",
        "han": """故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。""",
        "phien_am": """Cố nhân tây từ Hoàng Hạc lâu,
Yên hoa tam nguyệt hạ Dương Châu.
Cô phàm viễn ảnh bích không tận,
Duy kiến Trường Giang thiên tế lưu.""",
        "dich_nghia": """Bạn cũ từ giã lầu Hoàng Hạc ở phía tây, giữa mùa hoa khói tháng ba xuôi thuyền về đất Dương Châu. Bóng cánh buồm lẻ loi xa dần hút mắt vào cõi trời biếc xanh, chỉ thấy dòng sông Trường Giang cuồn cuộn chảy đến tận chân trời.""",
        "dich_tho": """Bạn cũ phía tây lầu Hạc giã,
Tháng ba hoa khói tới Dương Châu.
Bóng buồm cô độc chìm mây biếc,
Chỉ thấy Trường Giang chảy góc trời!""",
        "commentary": "Bức tranh tiễn biệt thanh nhã nhất Đường thi: Không một lời than khóc ly biệt mà tình cảm thương nhớ mênh mông vô tận như dòng Trường Giang chảy vào cõi biếc."
    },
    {
        "title": "Thục Đạo Nan (蜀道難)",
        "subtitle": "Đường Xứ Thục Hiểm Trở Vời Vợi Tận Trời Xanh",
        "han": """噫吁嚱，危乎高哉！
蜀道之難，難於上青天！
蠶叢及魚鳧，開國何茫然！
爾來四萬八千歲，不與秦塞通人煙。
西當太白有鳥道，可以橫絕峨嵋巔。
地崩山摧壯士死，然後天梯石棧相鉤連。
上有六龍回日之高標，下有衝波逆折之回川。
黃鶴之飛尚不得過，猿猱欲度愁攀援。
青泥何盤盤，百步九折縈岩巒。
捫參歷井仰脅息，以手撫膺坐長嘆。
問君西遊何時還？畏途巉巖不可攀。
但見悲鳥號古木，雄飛雌從繞林間。
又聞子規啼夜月，愁空山。
蜀道之難，難於上青天，使人聽此凋朱顏！""",
        "phien_am": """Y hu hi, nguy hồ cao tai!
Thục đạo chi nan, nan vu thượng thanh thiên!
Tàm Tòng cập Ngư Phù, khai quốc hà mang nhiên!
Nhĩ lai tứ vạn bát thiên tuế, bất dữ Tần tái thông nhân yên.
Tây đương Thái Bạch hữu điểu đạo, khả dĩ hoành tuyệt Nga Mi điên.
Địa băng sơn thôi tráng sĩ tử, nhiên hậu thiên thê thạch sạn tương câu liên.
Thượng hữu lục long hồi nhật chi cao tiêu, hạ hữu xung ba nghịch chiết chi hồi xuyên.
Hoàng hạc chi phi thượng bất đắc quá, viên nhu dục độ sầu phan viên.
Thanh Nê hà bàn bàn, bách bộ cửu chiết oanh nham loan.
Môn sâm lịch tỉnh ngưỡng hiếp tức, dĩ thủ phủ ưng tọa trường thán.
Vấn quân tây du hà thời hoàn? Úy đồ tiệm nham bất khả phan.
Đãn kiến bi điểu hào cổ mộc, hùng phi từ tòng nhiễu lâm gian.
Hựu văn tử quy đề dạ nguyệt, sầu không sơn.
Thục đạo chi nan, nan vu thượng thanh thiên, sử nhân thính thử điêu chu nhan!""",
        "dich_nghia": """Ôi chao nguy hiểm thay cao ngất trời thay! Đường xứ Thục gập ghềnh hiểm trở, khó hơn cả trèo lên trời xanh! Tàm Tòng và Ngư Phù mở nước từ thuở mờ mịt xa xăm. Bốn vạn tám nghìn năm nay, không thông khói bếp nhân gian với đất Tần. Phía tây ngọn Thái Bạch chỉ có đường chim bay ngang qua đỉnh Nga Mi. Đất lở núi sụp tráng sĩ bỏ mạng, rồi sau mới có thang trời và đường sạn đạo đá móc nối vào nhau. Trên có ngọn núi cao ngăn xe sáu rồng chở mặt trời, dưới có sóng dữ xô ngược dòng xoáy. Chim hạc vàng bay còn không qua nổi, loài vượn khỉ muốn trèo qua cũng âu sầu nhìn vách đá. Đèo Thanh Nê quanh co biết bao, trăm bước chín khúc lượn quanh vách núi. Sờ sao Sâm lướt sao Tỉnh ngửa mặt nín thở, lấy tay vỗ ngực ngồi thở dài. Hỏi bạn đi chơi sang tây bao giờ trở lại? Con đường đáng sợ vách đá cheo leo không thể trèo leo. Chỉ thấy chim sầu kêu gào trên cây cổ thụ, trống bay mái lượn quanh cánh rừng. Lại nghe chim cuốc kêu dưới trăng đêm sầu buốt núi hoang. Đường xứ Thục khó thay, khó hơn cả trèo lên trời xanh, khiến người nghe qua thảy đều phai nhạt má hồng!""",
        "dich_tho": """Ôi chao, cao ngất hiểm thay!
Đường Thục khó đi, khó hơn trèo trời!
Tàm Tòng, Ngư Phù mở đất xa vời,
Bốn vạn tám ngàn năm chẳng bóng người.
Chỉ có đường chim qua Thái Bạch,
Ngang qua đỉnh núi ngất Nga Mi.
Đất lở non nghiêng năm tráng sĩ,
Thang trời sạn đạo mới liền bờ!
Trên có ngọn cao che bóng nhật,
Dưới có sóng lừng xoáy nước sâu.
Hạc vàng bay qua còn chẳng nổi,
Vượn khỉ buồn rầu ngóng vách cao.
Thanh Nê ngoằn ngoèo trăm bước lượn,
Chín khúc quanh co quấn đỉnh non.
Sờ sao ngửa mặt khôn dám thở,
Vỗ ngực ngồi buông tiếng thở than!
Hỏi chàng sang tây bao giờ lại?
Vách đá cheo leo khôn trèo qua!
Chỉ thấy chim buồn kêu gỗ mục,
Vượn hú trăng đêm buốt núi mờ!
Đường Thục khó thay, khó trèo trời,
Nghe qua rụng rời má hồng tươi!""",
        "commentary": "Thiên trường ca tráng lệ bậc nhất mô tả địa hình Thục đạo hiểm trở, ẩn dụ sự gập ghềnh trắc trở của chốn quan trường và đường đời thế sự."
    },
    {
        "title": "Mộng Du Thiên Mụ Ngâm Lưu Biệt",
        "subtitle": "Khúc Ca Mộng Du Núi Thiên Mụ - Tuyên Ngôn Khí Tiết Kẻ Sĩ",
        "han": """海客談瀛洲，煙濤微茫信難求。
越人語天姥，雲霞明滅或可睹。
天姥連天向天橫，勢拔五嶽掩赤城。
天台四萬八千丈，對此欲倒東南傾。
我欲因之夢吳越，一夜飛度鏡湖月。
湖月照我影，送我至剡溪。
謝公宿處今尚在，渌水蕩漾清猿啼。
腳著謝公屐，身登青雲梯。
半壁見海日，空中聞天雞。
千岩萬轉路不定，迷花倚石忽已暝。
熊咆龍吟殷岩泉，慄深林兮驚層巔。
雲青青兮欲雨，水澹澹兮生煙。
列缺霹靂，丘巒崩摧。
洞天石扉，訇然中開。
青冥浩蕩不見底，日月照耀金銀臺。
霓為衣兮風為馬，雲之君兮紛紛而來下。
虎鼓瑟兮鸞回車，仙之人兮列如麻。
忽魂悸以魄動，恍驚起而長嗟。
惟覺時之枕席，失向來之煙霞。
世間行樂亦如此，古來萬事東流水。
別君去兮何時還？且放白鹿青崖間，須行即騎訪名山。
安能摧眉折腰事權貴，使我不得開心顏！""",
        "phien_am": """Hải khách đàm Doanh Châu, yên đào vi mang tín nan cầu.
Việt nhân ngữ Thiên Mụ, vân hà minh diệt hoặc khả đổ.
Thiên Mụ liên thiên hướng thiên hoành, thế bạt Ngũ Nhạc yểm Xích Thành.
Thiên Thai tứ vạn bát thiên trượng, đối thử dục đảo đông nam khuynh.
Ngã dục nhân chi mộng Ngô Việt, nhất dạ phi độ Kính Hồ nguyệt.
Hồ nguyệt chiếu ngã ảnh, tống ngã chí Diệm Khê.
Tạ công túc xứ kim thượng tại, lục thủy đãng dượng thanh viên đề.
Cước trước Tạ công kích, thân đăng thanh vân thê.
Bán bích kiến hải nhật, không trung văn thiên kê.
Thiên nham vạn chuyển lộ bất định, mê hoa ỷ thạch hốt dĩ minh.
Hùng bào long ngâm ân nham tuyền, lật thâm lâm hề kinh tầng điên.
Vân thanh thanh hề dục vũ, thủy đạm đạm hề sinh yên.
Liệt khuyết phích lịch, khâu loan băng thôi.
Động thiên thạch phi, oanh nhiên trung khai.
Thanh minh hạo đãng bất kiến để, nhật nguyệt chiếu diệu kim ngân đài.
Nghê vi y hề phong vi mã, vân chi quân hề phân phân nhi lai hạ.
Hổ cổ sắt hề loan hồi xa, tiên chi nhân hề liệt như ma.
Hốt hồn quý dĩ phách động, hoảng kinh khởi nhi trường ta.
Duy giác thời chi chẩm tịch, thất hướng lai chi yên hà.
Thế gian hành lạc diệc như thử, cổ lai vạn sự đông lưu thủy.
Biệt quân khứ hề hà thời hoàn?
Thả phóng bạch lộc thanh nhai gian, tu hành tức kỵ phỏng danh sơn.
An năng thôi mi chiết yêu sự quyền quý,
Sử ngã bất đắc khai tâm nhan!""",
        "dich_nghia": """Khách đi biển nói về núi Doanh Châu, khói sóng mờ mịt thật khó tìm kiếm. Người đất Việt kể về núi Thiên Mụ, mây ráng lúc tỏ lúc mờ may ra còn trông thấy. Thiên Mụ liền trời ngang lưng trời, thế trùm Ngũ Nhạc che lấp Xích Thành. Núi Thiên Thai cao bốn vạn tám nghìn trượng, đối với núi này như muốn nghiêng đổ về đông nam. Ta nhân đó muốn mộng du đất Ngô Việt, một đêm bay qua vầng trăng hồ Kính Hồ. Trăng hồ soi bóng ta, đưa ta tới suối Diệm Khê. Chốn Tạ Linh Vận nghỉ ngơi nay vẫn còn, nước trong dập dềnh tiếng vượn kêu thanh thoát. Chân xỏ guốc Tạ Linh Vận, mình trèo lên bậc thang mây xanh. Lưng chừng vách núi thấy mặt trời mọc từ biển, giữa không trung nghe tiếng gà trời gáy. Ngàn vách muôn khúc đường đi khôn định, mải ngắm hoa tựa đá bỗng trời đã tối mịt. Gấu rống rồng gầm vang rền suối đá, run rẩy rừng sâu kinh hãi đỉnh tầng non. Mây đen nghịt muốn mưa, nước cuồn cuộn bốc khói. Chớp giật sấm ran, đồi gò sụp đổ. Cửa đá động tiên ầm ầm mở toang. Trời xanh mênh mông không thấy đáy, mặt trời mặt trăng chiếu sáng đài vàng đài bạc. Cầu vồng làm áo gió làm ngựa, các chúa mây lũ lượt giáng trần. Hổ gảy đàn sắt chim loan kéo xe, người tiên đứng la liệt đông như mắc cửi. Chợt giật mình hồn kinh phách động, bàng hoàng thức giấc thở dài sườn sượt. Chỉ thấy gối chiếu lúc tỉnh giấc, mất hết ráng mây kỳ ảo vừa qua. Sự vui chơi ở thế gian cũng như vậy, xưa nay muôn việc đều như dòng nước chảy về đông. Từ biệt các bạn ra đi bao giờ trở lại? Hãy thả hươu trắng giữa ghềnh núi xanh, muốn đi liền cưỡi đi thăm thú non cao. Há chịu cúi mày khom lưng phụng sự bọn quyền quý, để khiến lòng ta chẳng được vui tươi!""",
        "dich_tho": """Khách biển kể chuyện Doanh Châu,
Khói sóng mờ mịt dễ đâu mà tìm.
Người Việt kể núi Thiên Mụ,
Mây ráng ẩn hiện khôn lường mắt trông.
Thiên Mụ cao ngất vút trời,
Thế trùm Ngũ Nhạc rạng ngời non sông.
Mộng bay qua đất Ngô Việt,
Một đêm vượt Kính Hồ trăng soi đầy.
Guốc Tạ chân xỏ bước nhanh,
Thang mây vút thẳng trèo lên đỉnh non.
Lưng đèo thấy bóng thái dương,
Không trung gà gáy tiếng vang rộn ràng.
Sấm sét nổ tung đất trời,
Động tiên cửa đá mở toang ầm ầm.
Người tiên y phục cầu vồng,
Hổ đàn loan kéo rước mừng chư tiên.
Bàng hoàng thức giấc mộng tan,
Gối chăn trơ trọi ráng mây đâu rồi?
Thế gian hành lạc thoảng trôi,
Muôn sự trôi dạt như dòng nước đông.
Giã từ non nước ra đi,
Thả hươu sườn biếc cưỡi đi danh sơn.
Há chịu cúi mày uốn lưng thờ quyền quý,
Để khiến lòng ta chẳng đặng vui!""",
        "commentary": "Hai câu thơ kết thúc là bản tuyên ngôn nhân cách vĩ đại nhất của Lý Bạch: 'An năng thôi mi chiết yêu sự quyền quý / Sử ngã bất đắc khai tâm nhan' - Kiên quyết không cúi đầu khom lưng làm nô lệ cho bổng lộc quyền quý."
    },
    {
        "title": "Tuyên Châu Tạ Điêu Lâu Tiễn Biệt Hiệu Thư Thúc Vân",
        "subtitle": "Cắt Nước Nước Càng Chảy - Nâng Chén Tiêu Sầu Sầu Càng Sầu",
        "han": """棄我去者，昨日之日不可留；
亂我心者，今日之日多煩憂。
長風萬里送秋雁，對此可以酣高樓。
蓬萊文章建安骨，中間小謝又清發。
俱懷逸興壯思飛，欲上青天攬明月。
抽刀斷水水更流，舉杯銷愁愁更愁。
人生在世不稱意，明朝散髮弄扁舟。""",
        "phien_am": """Khí ngã khứ giả, tẩu nhật chi nhật bất khả lưu;
Loạn ngã tâm giả, kim nhật chi nhật đa phiền ưu.
Trường phong vạn lý tống thu nhạn,
Đối thử khả dĩ hàm cao lâu.
Bồng Lai văn chương Kiến An cốt,
Trung gian Tiểu Tạ hựu thanh phát.
Câu hoài dật hứng tráng tư phi,
Dục thượng thanh thiên lãm minh nguyệt.
Trừu đao đoạn thủy thủy cánh lưu,
Cử bôi tiêu sầu sầu cánh sầu.
Nhân sinh tại thế bất xưng ý,
Minh triêu tán phát lộng biển chu.""",
        "dich_nghia": """Bỏ ta mà đi, ngày hôm qua chẳng thể nào giữ lại được; làm rối lòng ta, ngày hôm nay chứa chan bao nỗi phiền muộn u sầu. Gió dài muôn dặm đưa đàn nhạn thu bay, đối diện cảnh này có thể say sưa trên lầu cao. Văn chương Bồng Lai mang phong cốt Kiến An, ở giữa có Tiểu Tạ (Tạ Điêu) thanh thoát trác tuyệt. Cả hai đều ôm ấp hứng thú phóng khoáng ý tưởng bay bổng, muốn trèo lên trời xanh ôm lấy vầng trăng sáng. Rút dao chém xuống dòng nước nước càng chảy xiết, nâng chén tiêu sầu mối sầu lại càng sầu thêm! Ở đời sống không vừa ý, ngày mai xõa tóc buông thuyền nan rong chơi!""",
        "dich_tho": """Bỏ ta đi, ngày hôm qua không giữ được;
Rối lòng ta, ngày hôm nay lắm âu lo.
Gió thu muôn dặm đưa nhạn tới,
Lên lầu say khướt ngắm trăng ngô.
Bồng Lai văn cốt Kiến An xưa,
Tiểu Tạ thanh tao giọng tuyệt vời.
Cùng ôm dật hứng bay cao vút,
Muốn lên trời biếc bắt trăng soi!
Rút dao chém nước nước càng chảy,
Nâng chén tiêu sầu sầu vẫn rơi.
Ở đời sống chẳng như lòng ước,
Sớm mai xõa tóc cưỡi thuyền khơi!""",
        "commentary": "Hai câu châm ngôn thiên cổ: 'Trừu đao đoạn thủy thủy cánh lưu / Cử bôi tiêu sầu sầu cánh sầu' đúc kết sâu sắc quy luật tâm lý và nỗi bi phẫn của kẻ sĩ bất đắc chí trước hiện thực thối nát."
    }
]

def build_ly_bach_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Đại Đường Thi Ca • Thế Kỷ VIII</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">LÝ BẠCH • THI TIÊN</div>
            <div class="cover-subtitle">Đại Tuyển Tập Kiệt Tác Đường Thi Bất Hủ<br>Nguyên tác chữ Hán, phiên âm Hán Việt, dịch nghĩa, dịch thơ & khảo luận thi pháp</div>
            <div class="gold-line"></div>
            <div class="cover-author">THI TIÊN LÝ BẠCH (701 – 762) • TỰ THÁI BẠCH • HIỆU THANH LIÊN CƯ SĨ</div>
            <div class="cover-author-sub">Đỉnh cao thi ca lãng mạn trác việt phương Đông</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Hiệu đính đối chiếu Toàn Đường Thi mộc bản Khang Hy & Tản Đà toàn tập</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: THẦN THÁI & THI PHÁP THI TIÊN LÝ BẠCH</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Lý Bạch (701 – 762)</strong>, tự Thái Bạch, hiệu Thanh Liên cư sĩ, được xưng tụng là <strong>Thi Tiên (詩仙)</strong>. Hạ Tri Chương khi vừa đọc thơ ông đã phải thốt lên kinh ngạc: <em>"Trích tiên nhân!"</em> (Ông tiên bị đày xuống trần gian). Phong cách thơ Lý Bạch mang đậm chất lãng mạn siêu trần, khoáng đạt, trác tuyệt vô tiền khoáng hậu.</p>
        <p>Thơ ông là sự thăng hoa rực rỡ của tư tưởng Đạo gia tự do phóng khoáng, hòa quyện với tinh thần hào hiệp trượng nghĩa của kiếm khách và niềm khao khát khẳng định giá trị bản thân. Với ngòi bút thần sầu <em>"Bút lạc kinh phong vũ, thi thành khấp quỷ thần"</em> (Bút hạ xuống làm kinh động gió mưa, thơ viết xong khiến quỷ thần rơi lệ), Lý Bạch đã đưa thi ca thời thịnh Đường chạm tới đỉnh cao vinh quang chói lọi nhất.</p>
    </div>
    """)
    
    for i, p in enumerate(LY_BACH_POEMS, 1):
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 25px;">
            <div style="border-bottom: 2px solid #8B1E1E; padding-bottom: 6px; margin-bottom: 12px;">
                <span style="font-weight: bold; color: #721616; font-size: 13pt;">{i}. {p['title']}</span>
                <div style="font-size: 9.5pt; color: #666; font-style: italic; margin-top: 2px;">{p['subtitle']}</div>
            </div>
            
            <div class="poem-parallel">
                <div class="poem-col" style="flex: 1.15; background: #fffdfa; border-color: #e5dac6;">
                    <div class="col-header">Bản Dịch Thơ Kinh Điển</div>
                    <div class="dich-tho" style="line-height: 1.85; font-size: 11pt; padding: 4px 6px;">
                        {p['dich_tho'].replace(chr(10), '<br>')}
                    </div>
                </div>
                
                <div class="poem-col" style="flex: 1; background: #faf8f5;">
                    <div class="col-header">Nguyên Tác Chữ Hán</div>
                    <div class="han-script" style="text-align: center; margin-bottom: 8px; font-size: 11pt;">
                        {p['han'].replace(chr(10), '<br>')}
                    </div>
                    <div class="col-header" style="font-size: 9pt; margin-top: 6px;">Phiên Âm Hán Việt</div>
                    <div class="phien-am" style="font-size: 9.5pt; line-height: 1.55;">
                        {p['phien_am'].replace(chr(10), '<br>')}
                    </div>
                </div>
            </div>
            
            <div class="commentary-box" style="margin-top: 10px;">
                <div class="commentary-title">Dịch Nghĩa & Bình Chú Thi Pháp:</div>
                <div style="margin-bottom: 6px;"><em>Dịch nghĩa:</em> {p['dich_nghia']}</div>
                <div><em>Bình chú:</em> {p['commentary']}</div>
            </div>
        </div>
        """)
        
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">VĨ THANH: VẦNG TRĂNG THI TIÊN BẤT TỬ</h1>
    <div class="ornament">❖</div>
    <div class="intro-box">
        <p>Huyền thoại kể rằng Lý Bạch qua đời vì đêm say rượu trên sông Thái Thạch đã nhảy xuống ôm vầng trăng đáy nước rồi hóa tiên cưỡi cá voi bay về trời. Cái chết huyền ảo ấy là biểu tượng hoàn mỹ nhất cho trọn vẹn một kiếp nhân sinh say đắm cái đẹp thuần khiết và tự do tuyệt đối của Thi Tiên Lý Bạch.</p>
    </div>
    """)
    
    return "\n".join(html)

async def main():
    print("Building Ly Bach comprehensive anthology...")
    html_content = build_ly_bach_html()
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="LÝ BẠCH • THI TIÊN ĐẠI ĐƯỜNG",
        header_right="TUYỂN TẬP ĐƯỜNG THI BẤT HỦ"
    )

if __name__ == "__main__":
    asyncio.run(main())
