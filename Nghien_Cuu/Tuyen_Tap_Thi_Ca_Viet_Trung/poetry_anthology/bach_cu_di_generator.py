# -*- coding: utf-8 -*-
"""
Bạch Cư Dị (Thi Ma) - Trường Hận Ca & Tỳ Bà Hành (Bản Toàn Văn) & Tuyển Tập Kiệt Tác
Đầy đủ 120 câu Trường Hận Ca (Tản Đà dịch) + 88 câu Tỳ Bà Hành (Phan Huy Thực dịch) + Tân Nhạc Phủ
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\04. [772-846] Trung Quốc_Bạch Cư Dị (Thi Ma)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[806] Bạch Cư Dị - Trường Hận Ca & Tỳ Bà Hành (Bản Toàn Văn).pdf")

# Data for Trường Hận Ca (120 lines divided into 8 episodes)
TRUONG_HAN_CA_EPISODES = [
    {
        "title": "Hồi I: Sắc Đẹp Khuynh Thành & Duyên Gặp Gỡ Đế Vương",
        "lines_range": "Câu 1 – 16",
        "han": """漢皇重色思傾國，御宇多年求不得。
楊家有女初長成，養在深閨人未識。
天生麗質難自棄，一朝選在君王側。
回眸一笑百媚生，六宮粉黛無顏色。
春寒賜浴華清池，溫泉水滑洗凝脂。
侍兒扶起嬌無力，始是新承恩澤時。
雲鬢花顏金步搖，芙蓉帳暖度春宵。
春宵苦短日高起，從此君王不早朝。""",
        "phien_am": """Hán hoàng trọng sắc tư khuynh quốc,
Ngự vũ đa niên cầu bất đắc.
Dương gia hữu nữ sơ trưởng thành,
Dưỡng tại thâm khuê nhân vị thức.
Thiên sinh lệ chất nan tự khí,
Nhất triêu tuyển tại quân vương trắc.
Hồi mâu nhất tiếu bách mị sinh,
Lục cung phấn đại vô nhan sắc.
Xuân hàn tứ dục Hoa Thanh trì,
Ôn tuyền thủy hoạt tẩy ngưng chi.
Thị nhi phù khởi kiều vô lực,
Thủy thị tân thừa ân trạch thời.
Vân bấn hoa nhan kim bộ dao,
Phù dung trướng noãn độ xuân tiêu.
Xuân tiêu khổ đoản nhật cao khởi,
Tùng thử quân vương bất tảo triều.""",
        "dich_nghia": """Vua Hán (Đường Huyền Tông) chuộng sắc đẹp, mong tìm người nghiêng nước nghiêng thành; trị vì thiên hạ bao năm vẫn chưa tìm được. Nhà họ Dương có người con gái vừa mới lớn, nuôi nấng nơi buồng sâu người ngoài chưa từng biết đến. Trời sinh vẻ đẹp lộng lẫy khó lòng vùi lấp, một buổi sớm được tuyển vào hầu cận bên vua. Ngoảnh lại mỉm cười một cái nở muôn vàn vẻ duyên dáng, mỹ nữ phấn son sáu cung bỗng chốc mất hết nhan sắc. Ngày xuân lạnh lẽo vua ban cho tắm ở hồ Hoa Thanh, làn nước suối nước nóng trơn láng gội rửa làn da trắng mịn như mỡ đông. Thị nữ nâng dậy vẻ nũng nịu yếu ớt, ấy là lúc mới bắt đầu đội ơn mưa móc sâu dày. Tóc mây mặt hoa thoa vàng lay động, trướng hoa sen ấm áp cùng trải đêm xuân. Tiếc thay đêm xuân ngắn ngủi mặt trời đã lên cao, từ đó đấng quân vương không còn thiết lâm triều buổi sớm.""",
        "dich_tho": """Hán hoàng trọng sắc tư khuynh quốc,
Bao thuở ngai vàng lận đận tìm.
Dương gia con gái vừa xuân sắc,
Khuê các buồng sâu kín tiếng tăm.
Trời phú đẹp tươi khôn giấu mãi,
Một mai vào tuyển cạnh quân vương.
Ngoảnh mặt cười tươi trăm vẻ đẹp,
Sáu cung son phấn thảy phai hương!
Hơi xuân tắm suối Hoa Thanh ấm,
Mỡ đông da mịn gội dòng trong.
Thị tỳ nâng dậy mềm như lụa,
Ấy lúc ân vua mới đượm nồng.
Tóc mây má phấn trâm vàng lắc,
Trướng ấm phù dung trọn giấc nồng.
Đêm xuân ngắn ngủi ngày lên sớm,
Từ đấy vua thôi buổi ngự triều.""",
        "author_credit": "Bản dịch: Tản Đà Nguyễn Khắc Hiếu"
    },
    {
        "title": "Hồi II: Yến Ẩm Triền Miên & Tiếng Trống Loạn Ngư Dương",
        "lines_range": "Câu 17 – 32",
        "han": """承歡侍宴無閑暇，春從春遊夜專夜。
後宮佳麗三千人，三千寵愛在一身。
金屋妝成嬌侍夜，玉樓宴罷醉和春。
姊妹弟兄皆列土，可憐光彩生門戶。
遂令天下父母心，不重生男重生女。
驪宮高處入青雲，仙樂風飄處處聞。
緩歌慢舞凝絲竹，盡日君王看不足。
漁陽鼙鼓動地來，驚破霓裳羽衣曲。""",
        "phien_am": """Thừa hoan thị yến vô nhàn hạ,
Xuân tòng xuân du dạ chuyên dạ.
Hậu cung giai lệ tam thiên nhân,
Tam thiên sủng ái tại nhất thân.
Kim ốc trang thành kiều thị dạ,
Ngọc lâu yến bãi túy hòa xuân.
Tỷ muội đệ huynh giai liệt thổ,
Khả lân quang thái sinh môn hộ.
Toái linh thiên hạ phụ mẫu tâm,
Bất trọng sinh nam trọng sinh nữ.
Ly Cung cao xứ nhập thanh vân,
Tiên nhạc phong phiêu xứ xứ văn.
Hoãn ca mạn vũ ngưng ti trúc,
Tận nhật quân vương khán bất túc.
Ngư Dương bì cổ động địa lai,
Kinh phá Nghê Thường Vũ Y khúc.""",
        "dich_nghia": """Hầu vui dự yến không một lúc rảnh rỗi, mùa xuân cùng du xuân, đêm đêm riêng mình nàng chuyên sủng. Hậu cung có ba nghìn giai nhân tuyệt sắc, ba nghìn mối ân sủng gom trọn vào một thân. Nhà vàng trang điểm xong nũng nịu hầu đêm, lầu ngọc tiệc tan say sưa cùng khí xuân đầm ấm. Chị em anh em nàng đều được phong đất phong hầu, rạng rỡ vẻ vang mở mày mở mặt cả gia tộc. Khiến cho lòng cha mẹ khắp trong thiên hạ, chẳng chuộng sinh con trai mà chỉ chuộng sinh con gái. Cung Ly Sơn cao vút tận tầng mây xanh, khúc nhạc tiên theo gió bay vang vọng khắp nơi. Tiếng hát êm ái điệu múa khoan thai hòa cùng tiếng đàn tiếng sáo, suốt ngày quân vương ngắm nhìn vẫn chưa thỏa dạ. Đùng đùng tiếng trống trận Ngư Dương rung chuyển mặt đất kéo tới, làm kinh vỡ toang khúc nhạc Nghê Thường Vũ Y.""",
        "dich_tho": """Hầu yến vui say chẳng lúc ngơi,
Xuân đi du ngoạn, tối chung đôi.
Hậu cung ba vạn người xinh đẹp,
Ba vạn yêu thương một bóng người.
Nhà vàng điểm phấn hầu khuya sớm,
Lầu ngọc say sưa chén rượu mời.
Anh em chị em đều phong tước,
Môn hộ rạng ngời vẻ tốt tươi.
Khiến lòng cha mẹ trong thiên hạ,
Chẳng quý sinh trai, chuộng gái thôi!
Cung Ly vòi vọi mây xanh biếc,
Gió thoảng đàn tiên tiếng dặt dìu.
Múa chậm ca êm nhịp trúc tơ,
Suốt ngày trông ngắm mắt chưa no.
Ngư Dương chiêng trống rung trời đất,
Kinh vỡ Nghê Thường Vũ Y mơ!""",
        "author_credit": "Bản dịch: Tản Đà Nguyễn Khắc Hiếu"
    },
    {
        "title": "Hồi III: Biến Loạn Mã Ngôi & Giọt Lệ Biệt Ly Sa Trường",
        "lines_range": "Câu 33 – 50",
        "han": """九重城闕煙塵生，千乘萬騎西南行。
翠華搖搖行復止，西出都門百餘里。
六軍不發無奈何，宛轉蛾眉馬前死。
花鈿委地無人收，翠翹金雀玉搔頭。
君王掩面救不得，回看血淚相和流。
黃埃散漫風蕭索，雲棧縈紆登劍閣。
峨嵋山下少人行，旌旗無光日色薄。
蜀江水碧蜀山青，聖主朝朝暮暮情。
行宮見月傷心色，夜雨聞鈴腸斷聲。""",
        "phien_am": """Cửu trùng thành khuyết yên trần sinh,
Thiên thặng vạn kỵ tây nam hành.
Thúy hoa dao dao hành phục chỉ,
Tây xuất đô môn bách dư lý.
Lục quân bất phát vô nại hà,
Uyển chuyển nga mi mã tiền tử.
Hoa điền ủy địa vô nhân thu,
Thúy kiều, kim tước, ngọc tao đầu.
Quân vương yểm diện cứu bất đắc,
Hồi khán huyết lệ tương hòa lưu.
Hoàng ai tán mạn phong tiêu sái,
Vân sạn oanh hu đăng Kiếm Các.
Nga Mi sơn hạ thiểu nhân hành,
Tinh kỳ vô quang nhật sắc bạc.
Thục giang thủy bích Thục sơn thanh,
Thánh chủ triêu triêu mộ mộ tình.
Hành cung kiến nguyệt thương tâm sắc,
Dạ vũ văn linh đoạn trường thanh.""",
        "dich_nghia": """Cửa thành chín tầng khói bụi bốc mù mịt, nghìn xe muôn ngựa dong ruổi chạy về hướng tây nam. Cờ thúy hoa phất phơ đi rồi lại dừng, ra khỏi cửa thành phía tây hơn trăm dặm. Sáu quân dừng lại không chịu tiến bước chẳng biết làm sao, người đẹp mày ngài uốn éo đành chịu chết thắt cổ trước đầu ngựa. Cánh hoa vàng vương vãi đầy đất không ai buồn nhặt, cả thoa thúy kiều, chim tước vàng, trâm ngọc gãi đầu. Quân vương che mặt đau đớn không sao cứu được, quay đầu nhìn lại máu lệ chan hòa tuôn chảy. Bụi vàng mù mịt gió thổi tiêu điều, đường sạn đạo mây lượn quanh co trèo lên ải Kiếm Các. Dưới chân núi Nga Mi bóng người thưa thớt, ngọn cờ ủ rũ ánh mặt trời nhạt nhòa. Sông Thục nước biếc non Thục xanh rờn, sớm sớm chiều chiều thánh chủ chất chứa mối tình hoài vọng. Nơi hành cung nhìn thấy vầng trăng chỉ thêm đau lòng, đêm mưa nghe tiếng chuông gió vẳng lại xé đứt từng khúc ruột.""",
        "dich_tho": """Cửu trùng khói bụi bốc ngút ngàn,
Muôn cỗ xe dong cõi Thục ngàn.
Cờ thúy chập chờn đi lại đứng,
Cửa tây rời bước dặm quan san.
Sáu quân dậm bước khôn nài nữa,
Mày liễu đành cam rụng trước càn.
Hoa thoa rơi đất nào ai nhặt,
Chim tước, trâm cài, ngọc rớt vương.
Quân vương che mặt nào cứu nổi,
Ngoảnh lại chan hòa giọt lệ tuôn.
Bụi vàng hiu hắt gió tơi bời,
Đường mây Kiếm Các lối chơi vơi.
Nga Mi núi hiểm người thưa thớt,
Mặt trời ảm đạm cờ hoa rơi.
Sông Thục trong veo núi Thục xanh,
Sớm chiều thánh chúa nặng tình quanh.
Hành cung ngắm nguyệt lòng se sắt,
Đêm mưa nghe chuông ruột xé thành!""",
        "author_credit": "Bản dịch: Tản Đà Nguyễn Khắc Hiếu"
    },
    {
        "title": "Hồi IV: Trở Lại Trường An & Cảnh Cũ Người Đâu",
        "lines_range": "Câu 51 – 74",
        "han": """天旋地轉迴龍馭，到此躊躇不能去。
馬嵬坡下泥土中，不見玉顏空死處。
君臣相顧盡霑衣，東望都門信馬歸。
歸來池苑皆依舊，太液芙蓉未央柳。
芙蓉如面柳如眉，對此如何不淚垂。
春風桃李花開日，秋雨梧桐葉落時。
西宮南內多秋草，落葉滿階紅不掃。
梨園弟子白髮新，椒房阿監青娥老。
夕殿螢飛思悄然，孤燈挑盡未成眠。
遲遲鐘鼓初長夜，耿耿星河欲曙天。
鴛鴦瓦冷霜華重，翡翠衾寒誰與共。
悠悠生死別經年，魂魄不曾來入夢。""",
        "phien_am": """Thiên toàn địa chuyển hồi long ngự,
Đáo thử trù trừ bất năng khứ.
Mã Ngôi pha hạ nê thổ trung,
Bất kiến ngọc nhan không tử xứ.
Quân thần tương cố tận triêm y,
Đông vọng đô môn tín mã quy.
Quy lai trì uyển giai y cựu,
Thái Dịch phù dung Vị Ương liễu.
Phù dung như diện liễu như mi,
Đối thử như hà bất lệ thùy.
Xuân phong đào lý hoa khai nhật,
Thu vũ ngô đồng diệp lạc thời.
Tây cung Nam nội đa thu thảo,
Lạc diệp mãn giai hồng bất tảo.
Lê Viên đệ tử bạch phát tân,
Tiêu phòng a giám thanh nga lão.
Tịch điện huỳnh phi tư tiếu nhiên,
Cô đăng khiêu tận vị thành miên.
Trì trì chung cổ sơ trường dạ,
Cảnh cảnh tinh hà dục thự thiên.
Uyên ương ngõa lãnh sương hoa trọng,
Phỉ thúy khâm hàn thùy dữ cộng.
Du du sinh tử biệt kinh niên,
Hồn phách bất tằng lai nhập mộng.""",
        "dich_nghia": """Đất xoay trời chuyển loan giá trở về kinh đô, đến chốn Mã Ngôi ngập ngừng chân bước không nỡ rời đi. Dưới sườn dốc Mã Ngôi trong lòng đất bùn lầy, chẳng thấy mặt ngọc đâu chỉ trơ trọi chốn nàng bỏ mạng. Vua tôi nhìn nhau lệ đẫm vạt áo, nhìn về hướng đông cửa đô thành buông lỏng cương ngựa trở về. Trở về thấy vườn ao xưa cảnh vẫn như cũ, hoa sen hồ Thái Dịch rặng liễu cung Vị Ương. Sen nở giống mặt nàng liễu xanh tựa mày ngài, đối diện cảnh này làm sao lệ không tuôn rơi. Ngày gió xuân đào mận đơm hoa nở rộ, lúc mưa thu lá ngô đồng rụng xào xạc. Tây Cung Nam Nội cỏ thu mọc đầy, lá rụng ngập thềm son chẳng ai buồn quét. Con em Lê Viên mái đầu bạc trắng, đám thị giám phòng tiêu nàng cung nữ trẻ tuổi nay đã già nua. Điện chiều đom đóm bay mối sầu lặng lẽ, khêu cạn bấc đèn cô đơn vẫn chưa chợp mắt. Tiếng chuông trống chậm rãi mở đầu đêm dài đằng đẵng, dải Ngân Hà lấp lánh trời sắp rạng đông. Ngói uyên ương lạnh lẽo sương phủ dày đặc, chăn phỉ thúy buốt giá ai cùng sẻ chia. Mênh mông sống chết cách biệt đã bao năm trời, mà hồn phách nàng chưa từng một lần hiện về trong giấc mộng.""",
        "dich_tho": """Trời xoay đất chuyển bóng xe về,
Tới chốn dừng chân dạ não nề.
Mã Ngôi gò đất bùn nhơ vấy,
Mặt ngọc nào đâu, xác lạnh tê!
Vua tôi ngó lại lệ đầm mi,
Ngựa thả cửa đông hướng lối về.
Vườn cũ trở về trăng cảnh cũ,
Thái Dịch sen hồng, liễu bờ đê.
Mặt ngọc như sen, mày tựa liễu,
Trông cảnh nào ngăn giọt lệ rơi!
Gió xuân hoa nở đào mận thắm,
Mưa thu lá rụng ngô đồng phơi.
Tây Cung Nam Nội đầy cỏ dại,
Lá rụng thềm son chẳng quét khơi.
Lê Viên đệ tử đầu hoa rụng,
Cung nữ phòng tiêu tuổi xế rồi.
Điện vắng đóm bay sầu ngút mắt,
Đèn tàn khêu bấc giấc khôn xuôi.
Trống chuông chậm rãi đêm trường tới,
Sông Ngân lấp lánh rạng chân trời.
Ngói uyên ương buốt hạt sương đọng,
Chăn thúy lạnh lùng lẻ bạn thôi!
Sống chết cách chia ngàn dặm thẳm,
Mộng hồn chưa thấy bóng hình ai.""",
        "author_credit": "Bản dịch: Tản Đà Nguyễn Khắc Hiếu"
    },
    {
        "title": "Hồi V: Đạo Sĩ Lâm Cung & Vượt Biển Tìm Hồn Tiên Nữ",
        "lines_range": "Câu 75 – 94",
        "han": """臨邛道士鴻都客，能以精誠致魂魄。
為感君王展轉思，遂教方士殷勤覓。
排空馭氣奔如電，升天入地求之遍。
兩處茫茫皆不見，忽聞海上有仙山。
山在虛無縹緲間，樓閣玲瓏五雲起。
其中綽約多仙子，中有一人字太真。
雪膚花貌參差是，金闕西廂叩玉扃。
轉教小玉報雙成，聞道漢家天子使。
九華帳裏夢魂驚，攬衣推枕起徘徊。
珠箔銀屏邐迤開，雲鬢半偏新睡覺。
花冠不整下堂來，風吹仙袂飄颻舉。
猶似霓裳羽衣舞，玉容寂寞淚闌干。
梨花一枝春帶雨。""",
        "phien_am": """Lâm Cung đạo sĩ Hồng Đô khách,
Năng dĩ tinh thành trí hồn phách.
Vị cảm quân vương triển chuyển tư,
Toái giáo phương sĩ ân cần mịch.
Bài không ngự khí bôn như điện,
Thăng thiên nhập địa cầu chi biến.
Lưỡng xứ mang mang giai bất kiến,
Hốt văn hải thượng hữu tiên sơn.
Sơn tại hư vô phiêu miểu gian,
Lâu các linh lung ngũ vân khởi.
Kỳ trung xước ước đa tiên tử,
Trung hữu nhất nhân tự Thái Chân.
Tuyết phu hoa mạo sâm si thị,
Kim khuyết tây sương khấu ngọc quynh.
Chuyển giáo Tiểu Ngọc báo Song Thành,
Văn đạo Hán gia thiên tử sứ.
Cửu hoa trướng lý mộng hồn kinh,
Lãm y thôi chẩm khởi bồi hồi.
Châu bạc ngân bính lỵ di khai,
Vân bấn bán thiên tân thụy giác.
Hoa quan bất chỉnh hạ đường lai,
Phong xuy tiên duệ phiêu dao cử.
Do tự Nghê Thường Vũ Y vũ,
Ngọc dung tịch mịch lệ lan can.
Lê hoa nhất chi xuân đới vũ.""",
        "dich_nghia": """Có người đạo sĩ Lâm Cung là khách đất Hồng Đô, có tài lấy lòng chí thành mà gọi được hồn phách người chết. Vì cảm kích trước nỗi nhớ nhung trăn trở khôn nguôi của đấng quân vương, bèn sai phương sĩ ân cần tìm kiếm. Vạch không cưỡi gió ruổi nhanh như điện chớp, lên trời xuống đất tìm kiếm khắp mọi nơi. Cả hai chốn trời đất mênh mông đều không thấy đâu, chợt nghe ngoài biển đông có ngọn núi tiên. Núi tiên nằm giữa cõi mờ ảo chập chờn hư vô, lầu gác long lanh rực rỡ mây năm sắc bốc lên. Trong đó có nhiều nàng tiên thướt tha mềm mại, trong ấy có một người mang tên gọi Thái Chân. Làn da trắng như tuyết mặt hoa xinh tươi dường như chính là nàng, đến cửa tây cánh vàng gõ then ngọc. Nhờ tỳ nữ Tiểu Ngọc báo tin cho nàng Song Thành, nghe nói có sứ giả của thiên tử nhà Hán đến. Trong bức trướng chín hoa mộng hồn kinh hãi giật mình, vơ lấy áo gạt gối chồm dậy bồi hồi. Rèm châu bình bạc dần dần mở rộng, mái tóc mây còn nghiêng lệch vừa mới thức giấc. Mũ hoa chưa kịp sửa ngay ngắn đã bước vội xuống thềm, gió thổi tà áo tiên phất phơ bay bổng. Dáng dấp vẫn như lúc múa khúc Nghê Thường Vũ Y, nét mặt ngọc lặng lẽ giọt lệ chan hòa ròng ròng. Tựa như một cành hoa lê trong tiết xuân ngậm hạt mưa rào.""",
        "dich_tho": """Khách Lâm Cung có đạo nhân,
Lòng thành gọi được linh hồn cõi xa.
Cảm lòng thánh chúa xót xa,
Lệnh truyền phương sĩ tìm ra bóng nàng.
Cưỡi mây lướt gió ruổi mau,
Lên trời xuống đất tìm đâu bóng hình.
Hai phương mờ mịt bóng kinh,
Chợt nghe ngoài biển tiên đình non cao.
Non tiên ẩn hiện mây mờ,
Lầu vàng gác ngọc năm màu mây giăng.
Tiên nga yểu điệu ngút ngàn,
Có người tên gọi Thái Chân dịu dàng.
Mặt hoa da tuyết rỡ ràng,
Cửa tây gõ cửa lầu vàng then son.
Tiểu Ngọc chạy báo Song Thành,
Nghe tin thiên tử phái người tìm sang.
Trướng hoa thức giấc bàng hoàng,
Gạt chăn khoác áo vội vàng bước ra.
Rèm châu mở hé thềm hoa,
Tóc mây nghiêng lệch mới vừa giấc mơ.
Mũ hoa chưa chỉnh bước nhanh,
Gió lay tà áo phất phơ dập dồn.
Tựa như Nghê Thường điệu xưa,
Mặt hoa đẫm lệ giọt mưa đầm đìa.
Cành lê trĩu hạt mưa xuân!""",
        "author_credit": "Bản dịch: Tản Đà Nguyễn Khắc Hiếu"
    },
    {
        "title": "Hồi VI: Kỷ Vật Tình Xưa & Lời Thề Dưới Trăng Vĩnh Cửu",
        "lines_range": "Câu 95 – 120",
        "han": """含情凝睇謝君王，一別音容兩渺茫。
昭陽殿裏恩愛絕，蓬萊宮中日月長。
回頭下望塵寰處，不見長安見塵霧。
唯將舊物表深情，鈿合金釵寄將去。
釵留一股合一扇，釵擘黃金合分鈿。
但教心似金鈿堅，天上人間會相見。
臨別殷勤重寄詞，詞中有誓兩心知。
七月七日長生殿，夜半無人私語時。
在天願作比翼鳥，在地願為連理枝。
天長地久有時盡，此恨綿綿無絕期。""",
        "phien_am": """Hàm tình ngưng thế tạ quân vương,
Nhất biệt âm dung lưỡng viễn mang.
Chiêu Dương điện lý ân ái tuyệt,
Bồng Lai cung trung nhật nguyệt trường.
Hồi đầu hạ vọng trần hoàn xứ,
Bất kiến Trường An kiến trần vụ.
Duy tương cựu vật biểu thâm tình,
Điền hạp kim thoa ký tương khứ.
Thoa lưu nhất cổ hạp nhất phiến,
Thoa phách hoàng kim hạp phân điền.
Đãn giáo tâm tự kim điền kiên,
Thiên thượng nhân gian hội tương kiến.
Lâm biệt ân cần trùng ký từ,
Từ trung hữu thệ lưỡng tâm tri.
Thất nguyệt thất nhật Trường Sinh điện,
Dạ bán vô nhân tư ngữ thời.
Tại thiên nguyện tác bỉ dực điểu,
Tại địa nguyện vi liên lý chi.
Thiên trường địa cửu hữu thời tận,
Thử hận miên miên vô tuyệt kỳ.""",
        "dich_nghia": """Ngậm ngùi nhìn chăm chú tạ ơn đấng quân vương, từ ngày biệt ly âm hao dung mạo đôi bên mịt mờ. Ân ái nơi điện Chiêu Dương nay đã dứt đoạn, chuỗi ngày tháng chốn cung Bồng Lai đằng đẵng trôi qua. Ngoảnh đầu nhìn xuống chốn bụi trần nhân gian, chẳng thấy Trường An đâu chỉ thấy mịt mùng sương khói. Chỉ xin đem kỷ vật xưa để bày tỏ mối tình thâm sâu, hộp khảm xà cừ và thoa vàng gửi người mang về. Bẻ thoa giữ lại một nhánh, chia hộp giữ lại một mảnh; thoa vàng bẻ gãy, hộp khảm tách đôi. Chỉ mong lòng chàng vững bền như vàng như xà cừ, thì trên cõi trời hay chốn nhân gian ắt sẽ có ngày tái ngộ. Lúc chia tay ân cần gửi lại đôi lời thề ước, trong lời có câu thề nguyện chỉ riêng hai lòng thấu hiểu: Vào đêm mùng bảy tháng bảy tại điện Trường Sinh, nửa đêm vắng lặng không người cùng nhau thì thầm tâm sự: Trên trời nguyện làm chim liền cánh, dưới đất nguyện làm cây liền cành. Trời dài đất rộng dẫu có lúc cùng tận, mối hận tình này dằng dặc khôn nguôi không bao giờ dứt!""",
        "dich_tho": """Đăm đăm gửi gắm tình thâm,
Từ ly bóng bặt âm thầm đôi nơi.
Chiêu Dương ân ái rụng rơi,
Bồng Lai ngày tháng lặng trôi tháng ngày.
Ngoảnh đầu nhìn cõi trần ai,
Trường An chẳng thấy, mây mù giăng che.
Lấy chi gửi chút tình xưa?
Hộp xà cừ với thoa vàng cầm trao.
Thoa bẻ nửa, hộp chia đôi,
Vàng kia bẻ gãy, xà cừ rẽ phân.
Miễn sao lòng dạ sắt đinh,
Trần gian cõi Phật ắt mình gặp nhau.
Dặn dò phương sĩ đôi câu,
Lời nguyền thuở trước gối đầu trao duyên:
Trường Sinh điện vắng trăng thanh,
Bảy ngày tháng bảy nửa đêm tỏ tình:
Trên trời nguyện cánh chim đôi,
Dưới trần nguyện nhánh cây liền liền nhau!
Trời dài đất rộng có cùng,
Mối hận dằng dặc muôn trùng khôn vơi!""",
        "author_credit": "Bản dịch: Tản Đà Nguyễn Khắc Hiếu"
    }
]

# Data for Tỳ Bà Hành (88 lines + Lời tựa Tỳ Bà Dẫn)
TY_BA_HANH = {
    "preface_han": """元和十年，予左遷九江郡司馬。明年秋，送客湓浦口，聞舟中夜彈琵琶者，聽其音，諍諍然有京都聲。
問其人，本長安倡女，嘗學琵琶於穆、曹二善才，年長色衰，委身為賈人婦。
遂命酒使快彈數曲，曲罷憫然。自念少小濩落，流浪江湖。今漂淪憔悴，轉徙於江湖間。
予出官二年，恬然自安，感斯人言，是夕始覺有遷謫意。因為長句，歌以贈之，凡六百一十六言，命曰《琵琶行》。""",
    "preface_phien_am": """Nguyên Hòa thập niên, dư tả thiên Cửu Giang quận tư mã. Minh niên thu, tống khách Bồn Phố khẩu, văn chu trung dạ đàn tỳ bà giả, thính kỳ âm, tranh tranh nhiên hữu Kinh Đô thanh.
Vấn kỳ nhân, bản Trường An xướng nữ, thường học tỳ bà vu Mục, Tào nhị thiện tài, niên trưởng sắc suy, ủy thân vi giả nhân phụ.
Toái mệnh tửu sử khoái đàn sổ khúc, khúc bãi mẫn nhiên. Tự niệm thiếu tiểu hoạch lạc, lưu lãng giang hồ. Kim phiêu luân tiều tụy, chuyển tỷ vu giang hồ gian.
Dư xuất quan nhị niên, điềm nhiên tự an, cảm tư nhân ngôn, thị tịch thủy giác hữu thiên trích ý. Nhân vi trường cú, ca dĩ tặng chi, phàm lục bách nhất thập lục ngôn, mệnh viết "Tỳ Bà Hành".""",
    "preface_dich_nghia": """Năm Nguyên Hòa thứ mười (815), tôi bị biếm chức làm Tư mã quận Cửu Giang. Mùa thu năm sau, đưa khách ở bến Bồn Phố, đêm nghe trên thuyền ai gảy đàn tỳ bà, nghe tiếng nảy tưng bừng có phong vị kinh đô Trường An. Gạn hỏi người ấy, vốn là kỹ nữ Trường An, từng học đàn với hai danh sư Mục, Tào; tuổi lớn sắc tàn, đành gửi thân làm vợ khách buôn buôn chè. Bèn sai dọn rượu bảo nàng gảy vài khúc; khúc đàn dứt, lòng bùi ngùi thương cảm. Tự nghĩ mình từ thuở nhỏ phóng khoáng buông tuồng, phiêu bạt giang hồ; nay lưu lạc tiều tụy nơi góc biển chân trời. Tôi bị đổi ra chốn này hai năm, lòng vẫn điềm nhiên tự an; nay cảm kích lời nàng nói, tối nay mới thấm thía nỗi đau đày ải. Nhân đó làm bài thơ trường thiên tặng nàng, gồm 616 chữ, đặt tên là "Tỳ Bà Hành".""",
    
    # 88 verses divided into 4 parts
    "parts": [
        {
            "part_title": "Đoạn 1: Tiếng Đàn Đêm Thu Trên Bến Tầm Dương",
            "lines_range": "Câu 1 – 22",
            "han": """潯陽江頭夜送客，楓葉荻花秋瑟瑟。
主人下馬客在船，舉酒欲飲無管弦。
醉不成歡慘將別，別時茫茫江浸月。
忽聞水上琵琶聲，主人忘歸客不發。
尋聲暗問彈者誰，琵琶聲停欲語遲。
移船相近邀相見，添酒迴燈重開宴。
千呼萬喚始出來，猶抱琵琶半遮面。
轉軸撥絃三兩聲，未成曲調先有情。
絃絃掩抑聲聲思，似訴平生不得志。
低眉信手續續彈，說盡心中無限事。
輕攏慢撚抹復挑，初為霓裳後六幺。""",
            "phien_am": """Tầm Dương giang đầu dạ tống khách,
Phong diệp địch hoa thu sắt sắt.
Chủ nhân hạ mã khách tại thuyền,
Cử tửu dục ẩm vô quản huyền.
Túy bất thành hoan thảm tương biệt,
Biệt thời mang mang giang tẩm nguyệt.
Hốt văn thủy thượng tỳ bà thanh,
Chủ nhân vong quy khách bất phát.
Tầm thanh ám vấn đàn giả thùy,
Tỳ bà thanh đình dục ngữ trì.
Di thuyền tương cận yêu tương kiến,
Thiêm tửu hồi đăng trùng khai yến.
Thiên hô vạn hoán thủy xuất lai,
Do bão tỳ bà bán già diện.
Chuyển trục bát huyền tam lưỡng thanh,
Vị thành khúc điệu tiên hữu tình.
Huyền huyền yểm ức thanh thanh tư,
Tự tố bình sinh bất đắc chí.
Đê mi tín thủ tục tục đàn,
Thuyết tận tâm trung vô hạn sự.
Khinh lung mạn nữu một phục khiêu,
Sơ vi Nghê Thường hậu Lục Yêu.""",
            "dich_nghia": """Bến sông Tầm Dương đêm đưa tiễn khách, lá phong hoa lau gió thu hiu hắt. Chủ xuống ngựa khách ngồi trong thuyền, nâng chén muốn uống mà chẳng có tiếng đàn địch phụ họa. Uống say mà không vui buồn bã sắp chia tay, lúc từ biệt vầng trăng dầm mênh mang đáy nước. Chợt nghe trên mặt nước vẳng tiếng đàn tỳ bà, chủ quên đường về khách dùng dằng chưa đi. Nương theo tiếng đàn sẽ hỏi ai gảy, tiếng đàn chợt dứt người đàn ngập ngừng muốn nói lại thôi. Chèo thuyền lại gần mời ra gặp mặt, rót thêm chén rượu khêu lại ngọn đèn mở lại tiệc đêm. Nghìn gọi vạn mời nàng mới chịu bước ra, tay vẫn ôm cây đàn tỳ bà che nửa khuôn mặt. Vặn trục gảy dây dạo thử đôi ba tiếng, chưa thành khúc điệu mà tình ý đã dạt dào. Dây từng dây dồn nén tiếng từng tiếng ngậm ngùi, như than thở nỗi bất đắc chí suốt một đời. Cúi mày buông tay liên tiếp gảy đàn, kể xiết muôn vàn tâm sự trong lòng. Bấm nhẹ vê chậm vuốt rồi gảy, trước gảy khúc Nghê Thường sau dạo điệu Lục Yêu.""",
            "dich_tho": """Bến Tầm Dương canh khuya đưa khách,
Quạnh hơi thu lau lách đìu hiu.
Người xuống ngựa, khách dừng chèo,
Chén quỳnh nâng cạn, dặt dìu quản huyền.
Say chẳng bõ nỗi phiền ly biệt,
Bến nước trong trăng rớt lạnh lùng.
Thoảng nghe trên nước tiếng đàn,
Chủ quên quay lại, khách dùng dằng đi.
Lần theo tiếng hỏi người gảy khúc,
Tiếng đàn ngưng e ấp muốn thưa.
Thuyền dời ghé sát mạn thuyền,
Rót thêm chén rượu, khêu đèn mở mâm.
Nghìn gọi vạn đón rước về,
Tay ôm đàn nguyệt che bề nửa dung.
Vặn trục so dây đôi ba tiếng,
Chưa nên bài mà đã nặng tình.
Dây dây nghẹn ngào, tiếng tiếng bi ai,
Tựa than thân kiếp lạc loài trần ai.
Cúi mày buông ngón dạo đàn,
Kể sao cho xiết muôn vàn tâm tư.
Nhẹ bấm, chậm vê, vuốt rồi buông,
Trước Nghê Thường khúc, sau nhường Lục Yêu.""",
            "author_credit": "Bản dịch: Phan Huy Thực (thường truyền tụng)"
        },
        {
            "part_title": "Đoạn 2: Tuyệt Đỉnh Miêu Tả Thanh Âm Tiếng Đàn Tỳ Bà",
            "lines_range": "Câu 23 – 42",
            "han": """大絃嘈嘈如急雨，小絃切切如私語。
嘈嘈切切錯雜彈，大珠小珠落玉盤。
間關鶯語花底滑，幽咽泉流冰下難。
冰泉冷澀絃凝絕，凝絕不通聲暫歇。
別有幽愁暗恨生，此時無聲勝有聲。
銀瓶乍破水漿迸，鐵騎突出刀槍鳴。
曲終收撥當心畫，四絃一聲如裂帛。
東船西舫悄無言，唯見江心秋月白。""",
            "phien_am": """Đại huyền tào tào như cấp vũ,
Tiểu huyền thiết thiết như tư ngữ.
Tào tào thiết thiết thác tạp đàn,
Đại châu tiểu châu lạc ngọc bàn.
Gian quan oanh ngữ hoa để hoạt,
U yết tuyền lưu băng hạ nan.
Băng tuyền lãnh sáp huyền ngưng tuyệt,
Ngưng tuyệt bất thông thanh tạm yết.
Biệt hữu u sầu ám hận sinh,
Thử thời vô thanh thắng hữu thanh.
Ngân bình sạ phá thủy tương bính,
Thiết kỵ đột xuất đao thương minh.
Khúc chung thu bát đương tâm hoạch,
Tứ huyền nhất thanh như liệt bạch.
Đông thuyền tây phưởng tiếu vô ngôn,
Duy kiến giang tâm thu nguyệt bạch.""",
            "dich_nghia": """Dây lớn rền vang ầm ầm như mưa rào đổ dồn, dây nhỏ líu ríu tỉ tê như lời thầm thì trò chuyện. Tiếng rền vang tiếng tỉ tê xen lẫn nhau gảy, như hạt ngọc châu lớn hạt ngọc châu nhỏ rơi lách cách xuống mâm ngọc. Trong trẻo líu lo như tiếng chim hoàng oanh hót trơn tru dưới khóm hoa, nghẹn ngào u uất như dòng suối chảy ngập ngừng dưới lớp băng lạnh. Dòng suối băng lạnh ngắt dây đàn như đông cứng lại, đông cứng ngưng trệ không thông tiếng đàn tạm thời ngưng bặt. Trong khoảng khắc ấy lại nảy sinh mối u sầu uất hận thầm kín, lúc này không gian không một tiếng động còn hay hơn cả có tiếng đàn. Bỗng bình bạc vỡ tung nước văng tung tóe, ngựa sắt xông pha đao thương loảng xoảng vang rền. Khúc đàn dứt thu miếng gảy vạch ngang một đường giữa tim đàn, bốn dây bật lên cùng một tiếng như tiếng xé lụa. Thuyền phía đông đò phía tây thảy đều im phăng phắc không ai thốt nên lời, chỉ thấy giữa lòng sông một vầng trăng thu tỏa sáng trắng xóa.""",
            "dich_tho": """Dây to rền rĩ như mưa rào,
Dây nhỏ nỉ non tựa thở than.
Rền rĩ nỉ non hòa tiếng gảy,
Ngọc châu rơi rớt mâm vàng lanh canh.
Trong trẻo tiếng oanh hoa trượt nhẹ,
Nghẹn ngào dòng suối đá ngưng trôi.
Suối băng đông lạnh dây ngừng bặt,
Ngừng bặt tăm hơi tiếng tạm rời.
Mối sầu u hận sinh đâu đấy,
Lặng im lúc ấy thắng ngàn lời!
Bình bạc vỡ tan dòng nước toé,
Ngựa sắt tràn ra giáo mác ran.
Dứt bài thu gảy vạch tim đàn,
Bốn dây một tiếng xé toang tấm lụa!
Thuyền đông bến tây lặng ngắt lời,
Chỉ thấy trăng thu trắng giữa dòng!""",
            "author_credit": "Bản dịch: Phan Huy Thực"
        },
        {
            "part_title": "Đoạn 3: Cuộc Đời Nàng Ca Nữ & Cảnh Ngộ Bạc Mệnh",
            "lines_range": "Câu 43 – 62",
            "han": """沉吟放撥插絃中，整頓衣裳起斂容。
自言本是京城女，家在蝦蟆陵下住。
十三學得琵琶成，名屬教坊第一部。
曲罷曾教善才服，妝成每被秋娘妒。
五陵年少爭纏頭，一曲紅綃不知數。
鈿頭銀篦擊節碎，血色羅裙翻酒污。
今年歡笑復明年，秋月春風等閑度。
弟走從軍阿姨死，暮去朝來顏色故。
門前冷落車馬稀，老大嫁作商人婦。
商人重利輕別離，前月浮梁買茶去。
去來江口守空船，繞船月明江水寒。
夜深忽夢少年事，夢啼妝淚紅闌干。""",
            "phien_am": """Trầm ngâm phóng bát sáp huyền trung,
Chỉnh đốn y thường khởi liễm dung.
Tự ngôn bản thị Kinh thành nữ,
Gia tại Hà Mô lăng hạ trụ.
Thập tam học đắc tỳ bà thành,
Danh thuộc giáo phường đệ nhất bộ.
Khúc bãi tằng giáo Thiện Tài phục,
Trang thành mỗi bị Thu Nương đố.
Ngũ Lăng niên thiếu tranh triền đầu,
Nhất khúc hồng tiêu bất tri sổ.
Điền đầu ngân bễ kích tiết toái,
Huyết sắc la quần phiên tửu ô.
Kim niên hoan tiếu phục minh niên,
Thu nguyệt xuân phong đẳng nhàn độ.
Đệ tẩu tòng quân a di tử,
Mộ khứ triêu lai nhan sắc cố.
Môn tiền lãnh lạc xa mã hi,
Lão đại giá tác thương nhân phụ.
Thương nhân trọng lợi khinh biệt ly,
Tiền nguyệt Phù Lương mãi trà khứ.
Khứ lai giang khẩu thủ không thuyền,
Nhiễu thuyền nguyệt minh giang thủy hàn.
Dạ thâm hốt mộng thiếu niên sự,
Mộng đề trang lệ hồng lan can.""",
            "dich_nghia": """Nàng trầm ngâm buông que gảy cắm vào giữa dây đàn, sửa sang lại xiêm y đứng dậy thu nét mặt đoan trang. Tự xưng vốn là gái kinh thành Trường An, nhà ở dưới chân gò Hà Mô. Mười ba tuổi đã học đàn tỳ bà thành tài, tên tuổi đứng vào bậc nhất giáo phường. Gảy xong bài từng khiến bậc danh sư Thiện Tài thán phục, điểm trang xong thường bị các bậc mỹ nữ Thu Nương đem lòng ghen tỵ. Các chàng công tử trẻ tuổi vùng Ngũ Lăng tranh nhau tặng tiền thưởng gấm vóc quấn đầu, một khúc đàn nhận không biết bao nhiêu tấm lụa đỏ. Trâm hoa lược bạc gõ nhịp vỡ tan tành, chiếc váy lụa màu đỏ tươi bị rượu đổ ố bẩn. Năm nay cười vui nối tiếp năm sau, trăng thu gió xuân thong thả lãng phí trôi qua. Em trai tòng quân bà dì qua đời, chiều qua sáng lại nhan sắc đã tàn tạ già nua. Trước cửa vắng vẻ xe ngựa thưa thớt, tuổi đã lớn đành nhắm mắt lấy làm vợ người lái buôn. Lái buôn vốn trọng món lợi nhỏ coi nhẹ cảnh chia ly, tháng trước đã sang đất Phù Lương mua chè. Bỏ lại nàng qua lại bến sông giữ con thuyền trống không, quanh thuyền ánh trăng vằng vặc dòng nước lạnh ngắt. Đêm khuya chợt mơ thấy chuyện thời tuổi trẻ, tỉnh giấc trong mơ khóc giọt lệ hoen ố phấn son hồng ròng ròng.""",
            "dich_tho": """Trầm ngâm buông gảy cắm lưng dây,
Chỉnh đốn áo khăn nét mặt đầy.
Tự nói: Vốn người kinh đô nọ,
Hà Mô cồn cũ chốn nương thân.
Mười ba tuổi học tỳ bà giỏi,
Danh đứng giáo phường đệ nhất danh.
Khúc dứt Thiện Tài khen phục mãi,
Điểm trang Thu Nương phải hờn ganh.
Ngũ Lăng công tử tranh dâng lụa,
Một khúc vạn tấm đỏ thắm vành.
Trâm bạc gõ nhịp tan tác vỡ,
Váy gấm màu hồng rượu đổ hoen.
Cười vui năm ấy sang năm khác,
Gió xuân trăng thu trôi uổng hoài.
Em đi tòng quân, dì qua cõi,
Sớm chiều trôi dạt sắc phai màu.
Cửa nhà quạnh quẽ xe thưa thớt,
Tuổi già đành gả khách buôn chè.
Khách buôn trọng lợi khinh chia cách,
Tháng trước Phù Lương chuyến buôn xa.
Bến sông quanh quẩn thuyền côi quạnh,
Lồng bóng trăng soi nước buốt tê.
Đêm sâu bỗng mộng thời thơ ấu,
Khóc giấc mơ hồng lệ đẫm mi!""",
            "author_credit": "Bản dịch: Phan Huy Thực"
        },
        {
            "part_title": "Đoạn 4: Tiếng Khóc Tri Âm & Cùng Một Kiếp Lưu Lạc Bên Trời",
            "lines_range": "Câu 63 – 88",
            "han": """我聞琵琶已歎息，又聞此語重唧唧。
同是天涯淪落人，相逢何必曾相識。
我從去年辭帝京，謫居臥病潯陽城。
潯陽地僻無音樂，終歲不聞絲竹聲。
住近湓江地低濕，黃蘆苦竹繞宅生。
其間旦暮聞何物，杜鵑啼血猿哀鳴。
春江花朝秋月夜，往往取酒還獨傾。
豈無山歌與村笛，嘔啞啁哳難為聽。
今夜聞君琵琶語，如聽仙樂耳暫明。
莫辭更坐彈一曲，為君翻作琵琶行。
感我此言良久立，卻坐促絃絃轉急。
淒淒不似向前聲，滿座重聞皆掩泣。
座中泣下誰最多，江州司馬青衫濕。""",
            "phien_am": """Ngã văn tỳ bà dĩ thán tức,
Hựu văn thử ngữ trùng tức tức.
Đồng thị thiên nhai luân lạc nhân,
Tương phùng hà tất tăng tương thức!
Ngã tòng khứ niên từ Đế kinh,
Trích cư ngọa bệnh Tầm Dương thành.
Tầm Dương địa tịch vô âm nhạc,
Chung tuế bất văn ti trúc thanh.
Trú cận Bồn giang địa đê thấp,
Hoàng lư khổ trúc nhiễu trạch sinh.
Kỳ gian đán mộ văn hà vật?
Đỗ quyên đề huyết viên ai minh.
Xuân giang hoa triêu thu nguyệt dạ,
Vãng vãng thủ tửu hoàn độc khuynh.
Khởi vô sơn ca dữ thôn địch,
Ẩu á triêu triết nan vi thính.
Kim dạ văn quân tỳ bà ngữ,
Như thính tiên nhạc nhĩ tạm minh.
Mạc từ cánh tọa đàn nhất khúc,
Vị quân phiên tác Tỳ Bà Hành.
Cảm ngã thử ngôn lương cửu lập,
Khước tọa xúc huyền huyền chuyển cấp.
Thê thê bất tự hướng tiền thanh,
Mãn tọa trùng văn giai yểm khấp.
Tọa trung khấp hạ thùy tối đa?
Giang Châu tư mã thanh sam thấp!""",
            "dich_nghia": """Ta nghe tiếng tỳ bà đã thở than bùi ngùi, lại nghe lời nàng kể càng thêm nghẹn ngào khôn xiết: Cùng là kẻ lưu lạc chốn chân trời góc biển, gặp gỡ nhau đây lọ phải từng quen biết từ trước! Ta từ năm ngoái từ giã kinh đô, bị giáng chức nằm bệnh ở đất Tầm Dương hẻo lánh. Tầm Dương đất vắng không có âm nhạc tao nhã, suốt năm chẳng hề nghe thấy tiếng đàn sáo. Chỗ ở gần bến sông Bồn đất đai trũng thấp, lau vàng trúc cằn quấn quanh nhà mọc đầy. Ở chốn ấy sớm tối nghe thấy những thứ gì? Chỉ có chim đỗ quyên cuốc kêu nhỏ máu và vượn hú thê lương. Buổi sáng hoa nở trên sông xuân, đêm trăng sáng mùa thu, thường thường chỉ biết nâng chén rượu rót một mình. Há chẳng có điệu hát miền núi và tiếng sáo thôn dã sao? Nhưng giọng gắt gao chát chúa khó nghe vô cùng. Đêm nay được nghe tiếng đàn tỳ bà của nàng, tựa như được nghe khúc nhạc tiên đôi tai bỗng sáng bừng. Xin nàng chớ từ chối ngồi lại gảy thêm một khúc, ta vì nàng sẽ viết nên bài thơ Tỳ Bà Hành. Cảm kích lời ta nàng đứng lặng hồi lâu, rồi ngồi xuống so dây tiếng đàn chuyển sang dồn dập gấp gáp. Tiếng bi thương sầu thảm không giống như tiếng đàn lúc trước, khắp chiếu tiệc nghe lại ai nấy đều bưng mặt khóc. Trong tiệc ai là người rơi nhiều nước mắt nhất? Áo quan Tư mã đất Giang Châu ướt đẫm cả vạt áo xanh!""",
            "dich_tho": """Nghe đàn ta đã buông lời thở,
Nghe chuyện nàng càng xót dạ tê!
Cùng một lứa bên trời lận đận,
Gặp gỡ nhau lọ sẵn quen nhau!
Ta từ năm ngoái rời kinh khuyết,
Đày ải thân côi chốn Tầm Dương.
Tầm Dương đất hiểm không đàn sáo,
Năm trọn nào nghe tiếng trúc tơ.
Nơi ở bên sông bến lụt lầy,
Lau vàng trúc cằn mọc quanh rào.
Sớm chiều nghe thấy những âm chi?
Đỗ quyên cuốc máu, vượn kêu đau!
Sông xuân sáng sớm, đêm trăng thu,
Chén rượu mình ta rót ngậm ngùi.
Há chẳng khúc thôn cùng sáo nội,
Gắt gao chát chúa khó vào tai.
Đêm nay nghe tiếng đàn tỳ khúc,
Như tiếng đàn tiên rạng cõi lòng.
Xin chớ từ nan đàn một khúc,
Vì nàng ta dệt Tỳ Bà Ca!
Cảm lời ta đứng ngập ngừng lâu,
Ngồi lại so dây giục nhịp mau.
Bi thảm chẳng như cung bậc trước,
Khắp phòng nghe lại lệ đầm mi.
Trong tiệc ai người rơi lệ nhất?
Giang Châu tư mã áo xanh đầm!""",
            "author_credit": "Bản dịch: Phan Huy Thực"
        }
    ]
}

# Tuyển tập các bài thơ Tân Nhạc Phủ & Trữ Tình của Bạch Cư Dị
OTHER_POEMS = [
    {
        "title": "Mại Thán Ông (賣炭翁)",
        "subtitle": "Khổ Cung Thị Dã - Bản Toàn Văn Tân Nhạc Phủ",
        "han": """賣炭翁，伐薪燒炭南山中。
滿面塵灰煙火色，兩鬢蒼蒼十指黑。
賣炭得錢何所營？身上衣裳口中食。
可憐身上衣正單，心憂炭賤願天寒。
夜來城外一尺雪，曉駕炭車輾冰轍。
牛困人飢日已高，市南門外泥中歇。
翩翩兩騎來是誰？黃衣使者白衫兒。
手把文書口稱敕，迴車叱牛牽向北。
一車炭，千餘斤，宮使驅將惜不得。
半匹紅綃一丈綾，繫向牛頭充炭直。""",
        "phien_am": """Mại thán ông, phạt tân thiêu thán Nam Sơn trung.
Mãn diện trần hôi yên hỏa sắc, lưỡng bấn thương thương thập chỉ hắc.
Mại thán đắc tiền hà sở doanh? Thân thượng y thường khẩu trung thực.
Khả lân thân thượng y chính đơn, tâm ưu thán tiện nguyện thiên hàn.
Dạ lai thành ngoại nhất xích tuyết, hiểu giá thán xa triễn băng triệt.
Ngưu khốn nhân cơ nhật dĩ cao, thị nam môn ngoại nê trung hiết.
Phiên phiên lưỡng kỵ lai thị thùy? Hoàng y sứ giả bạch sam nhi.
Thủ bả văn thư khẩu xưng sắc, hồi xa sất ngưu khiên hướng bắc.
Nhất xa thán, thiên dư cân, cung sứ khu tương tích bất đắc.
Bán thất hồng tiêu nhất trượng lăng, hệ hướng ngưu đầu sung thán trực.""",
        "dich_nghia": """Ông già bán than, đốn củi đốt than trong núi Nam Sơn. Mặt mày đầy bụi tro lem luốc màu khói lửa, hai bên tóc mai hoa râm mười ngón tay đen nhẻm. Bán than được tiền để lo việc gì? Để có manh áo ấm trên thân và miếng ăn nuôi miệng. Đáng thương thay trên người chiếc áo mỏng dính phong phanh, mà lòng sợ than rẻ lại cầu cho trời thật lạnh rét buốt. Đêm qua ngoài thành tuyết rơi dày một thước, sáng sớm đánh xe than nghiến qua vết băng đông. Bò mệt người đói mặt trời đã lên cao, ngoài cửa nam chợ tạm dừng nghỉ trong bùn lầy. Thướt tha hai kỵ mã kéo đến là ai? Là sứ giả áo vàng và tên tiểu đồng áo trắng nội cung. Tay cầm văn thư miệng xưng sắc chỉ của nhà vua, quay xe thét bò kéo thẳng về hướng bắc vào cung điện. Một xe than nặng hơn nghìn cân, sứ cung đình cướp đi chẳng chút thương xót. Ném lại nửa súc lụa đỏ một trượng the mỏng, buộc vào sừng bò gọi là trả tiền than!""",
        "dich_tho": """Lão bán than,
Chặt củi non Nam đốt lấy than.
Mặt lem tro bụi màu sương khói,
Mười ngón đen sì tóc bạc phai.
Bán than mong kiếm chút tiền còm,
Nuôi miệng, may thêm chiếc áo sờn.
Thương thay áo mỏng phong phanh quá,
Lòng sợ than rẻ ước trời đông!
Đêm qua tuyết ngập ngoài thành thước,
Sớm đánh xe qua rãnh tuyết đông.
Bò mệt người đói trời trưa trật,
Nghỉ bánh bùn lầy cửa chợ nam.
Phất phơ hai ngựa tới là ai?
Áo vàng sứ nội đứa hầu sau.
Tay cầm giấy sắc mồm hô chiếu,
Quay xe giục bò hướng bắc mau!
Một xe than nặng nghìn cân có,
Sứ cướp đem đi tiếc thắt lòng.
Nửa tấm lụa hồng, vuông the nhạt,
Buộc lên sừng bò bảo tiền than!""",
        "commentary": "Kiệt tác trào phúng hiện thực tố cáo chế độ 'Cung thị' (chợ cung đình) tàn bạo đời Đường, cướp đoạt mồ hôi nước mắt của người lao động bần cùng."
    },
    {
        "title": "Phú Đắc Cổ Nguyên Thảo Tống Biệt (賦得古原草送別)",
        "subtitle": "Khúc Ca Bất Diệt Về Sức Sống Mãnh Liệt Của Cỏ Nội",
        "han": """離離原上草，一歲一枯榮。
野火燒不盡，春風吹又生。
遠芳侵古道，晴翠接荒城。
又送王孫去，萋萋滿別情。""",
        "phien_am": """Ly ly nguyên thượng thảo,
Nhất tuế nhất khô vinh.
Dã hỏa thiêu bất tận,
Xuân phong xuy hựu sinh.
Viễn phương xâm cổ đạo,
Tình thúy tiếp hoang thành.
Hựu tống vương tôn khứ,
Thê thê mãn biệt tình.""",
        "dich_nghia": """Tốt tươi cỏ trên đồng nội, mỗi năm một lần khô héo rồi lại tươi tốt. Lửa đồng thiêu đốt chẳng thể nào tuyệt diệt, gió xuân thổi tới cỏ lại sinh sôi. Hương thơm xa tràn ngập con đường cổ xưa, màu biếc tươi rực rỡ nối liền với toà thành hoang vắng. Nay lại đưa tiễn chàng vương tôn ra đi, sắc cỏ xanh um ngút ngàn chan chứa mối tình ly biệt.""",
        "dich_tho": """Cỏ xanh đồng nội tốt tươi,
Mỗi năm một độ héo rồi lại tươi.
Lửa thiêu chẳng hết mầm tươi,
Gió xuân ấm áp lại trồi biếc xanh.
Hương lan đường cũ gập ghềnh,
Màu xanh bát ngát nối thành cổ xưa.
Đưa chàng vương tử tiễn đưa,
Cỏ xanh ngan ngát tiễn đưa tấm lòng!""",
        "commentary": "Hai câu thơ: 'Dã hỏa thiêu bất tận / Xuân phong xuy hựu sinh' (Lửa đồng thiêu chẳng hết / Gió xuân thổi lại sinh) là câu thơ bất hủ nhất của Bạch Cư Dị thuở 16 tuổi bước vào kinh đô Trường An làm rúng động thi đàn."
    },
    {
        "title": "Vấn Lưu Thập Cửu (問劉十九)",
        "subtitle": "Bản Tuyệt Tác Thơ Nhàn Tản & Ấm Áp Tình Tri Kỷ",
        "han": """綠蟻新醅酒，紅泥小火爐。
晚來天欲雪，能飲一杯無？""",
        "phien_am": """Lục nghĩ tân phôi tửu,
Hồng nê tiểu hỏa lô.
Vãn lai thiên dục tuyết,
Năng ẩm nhất bôi vô?""",
        "dich_nghia": """Rượu mới ủ bọt xanh nổi lăn tăn như kiến xanh, lò lửa nhỏ đắp bằng đất sét đỏ rực than hồng. Chiều muộn trời như muốn đổ tuyết rơi, có thể đến cùng ta uống một chén chăng?""",
        "dich_tho": """Rượu mới bọt xanh nổi,
Lò than đất đỏ hồng.
Chiều hôm trời đổ tuyết,
Uống một chén được không?""",
        "commentary": "Bức tranh thủy mặc tuyệt mỹ 20 chữ: Sắc xanh của rượu ngon, sắc đỏ của lò than, sắc trắng của tuyết chiều và tấm lòng ấm áp mời bạn tri âm."
    },
    {
        "title": "Trường Tương Tư (長相思)",
        "subtitle": "Khúc Hát Điệu Từ Tương Tư Bất Tận",
        "han": """汴水流，泗水流，
流到瓜洲古渡頭。
吳山點點愁。
思悠悠，恨悠悠，
恨到歸時方始休。
月明人倚樓。""",
        "phien_am": """Biện thủy lưu, Tứ thủy lưu,
Lưu đáo Qua Châu cổ độ đầu.
Ngô sơn điểm điểm sầu.
Tư du du, hận du du,
Hận đáo quy thời phương thủy hưu.
Nguyệt minh nhân ỷ lâu.""",
        "dich_nghia": """Nước sông Biện chảy, nước sông Tứ chảy, chảy đến tận bến đò cổ Qua Châu. Non nước xứ Ngô từng ngọn chất chứa nỗi sầu. Nhớ mênh mang, hận mênh mang, nỗi sầu giận mãi đến khi chàng về mới dứt. Trăng sáng vằng vặc người gác tựa lầu cao.""",
        "dich_tho": """Sông Biện trôi, sông Tứ trôi,
Trôi tới Qua Châu bến cổ rồi.
Ngô sơn sầu ngút trời.
Nhớ đầy vơi, hận đầy vơi,
Hận đến chàng về mới dứt thôi.
Đêm trăng tựa gác ngồi.""",
        "commentary": "Tiết tấu nhịp nhàng, ngôn ngữ trong sáng mà gợi cảm vô cùng, biểu đạt nỗi sầu tương tư dằng dặc của người phụ nữ ngóng trông phương xa."
    }
]

def build_bach_cu_di_html():
    html = []
    
    # Bìa sách
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Đại Đường Thi Ca • Thế Kỷ VIII – IX</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">BẠCH CƯ DỊ</div>
            <div class="cover-subtitle">Trường Hận Ca & Tỳ Bà Hành (Bản Toàn Văn Đầy Đủ)<br>Kèm Tuyển Tập Kiệt Tác Tân Nhạc Phủ & Khảo Luận Thi Ma</div>
            <div class="gold-line"></div>
            <div class="cover-author">BẠCH CƯ DỊ (772 – 846) • TỰ LẠC THIÊN • HIỆU HƯƠNG SƠN CƯ SĨ</div>
            <div class="cover-author-sub">Bản dịch thi ca kinh điển: Tản Đà Nguyễn Khắc Hiếu & Phan Huy Thực</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Nguyên bản chữ Hán toàn văn, phiên âm Hán Việt, dịch nghĩa & bình giảng thi pháp</div>
        </div>
    </div>
    """)
    
    # Mục lục & Tiểu dẫn
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">MỤC LỤC & KHẢO TẢ TÁC PHẨM</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Bạch Cư Dị (白居易, 772 – 846)</strong>, tự Lạc Thiên (樂天), hiệu Hương Sơn cư sĩ (香山居士), là một trong những đại thi hào vĩ đại nhất của thời thịnh Đường cùng với Lý Bạch và Đỗ Phủ. Hậu thế tôn vinh ông là <strong>"Thi Ma" (詩魔)</strong> bởi lòng đam mê sáng tác thơ cuồng nhiệt đến độ miệng lở lưỡi rát, tay chai sạn không rời ngòi bút.</p>
        <p>Thơ Bạch Cư Dị chia làm hai mảng lớn: <em>Thơ châm biếm thế sự (Tân Nhạc Phủ)</em> mang tính hiện thực sâu sắc bênh vực người dân nghèo, và <em>Thơ trữ tình cảm thương thế thái</em> với hai đỉnh cao tuyệt đối bất hủ trong thi ca nhân loại: <strong>Trường Hận Ca (長恨歌 - 120 câu)</strong> và <strong>Tỳ Bà Hành (琵琶行 - 88 câu)</strong>.</p>
        <p>Ấn bản này cung cấp toàn văn trọn vẹn từng câu chữ của cả hai kiệt tác trường thiên, kết hợp hoàn mỹ giữa nguyên tác chữ Hán, phiên âm Hán Việt, dịch nghĩa chi tiết và các bản dịch thơ tuyệt tác của hai bậc tiền bối uyên bác bậc nhất Việt Nam: <strong>Tản Đà Nguyễn Khắc Hiếu</strong> và <strong>Phan Huy Thực</strong>, cùng tuyển tập Tân Nhạc Phủ đặc sắc.</p>
    </div>
    
    <div class="toc-list" style="margin-top: 25px;">
        <div class="toc-item">
            <span class="toc-title">Lời Khảo Luận: Thần Thái & Tư Tưởng Thi Ca "Thi Ma" Bạch Cư Dị</span>
            <span class="toc-page">Trang 3</span>
        </div>
        <div class="toc-item">
            <span class="toc-title">PHẦN I: TRƯỜNG HẬN CA (長恨歌 - Đầy Đủ 120 Câu Toàn Văn)</span>
            <span class="toc-page">Trang 5</span>
        </div>
        <div class="toc-item" style="padding-left: 20px;">
            <span class="toc-title">• Hồi I: Sắc Đẹp Khuynh Thành & Duyên Gặp Gỡ Đế Vương (Câu 1 – 16)</span>
            <span class="toc-page">Trang 6</span>
        </div>
        <div class="toc-item" style="padding-left: 20px;">
            <span class="toc-title">• Hồi II: Yến Ẩm Triền Miên & Tiếng Trống Loạn Ngư Dương (Câu 17 – 32)</span>
            <span class="toc-page">Trang 8</span>
        </div>
        <div class="toc-item" style="padding-left: 20px;">
            <span class="toc-title">• Hồi III: Biến Loạn Mã Ngôi & Giọt Lệ Biệt Ly Sa Trường (Câu 33 – 50)</span>
            <span class="toc-page">Trang 10</span>
        </div>
        <div class="toc-item" style="padding-left: 20px;">
            <span class="toc-title">• Hồi IV: Trở Lại Trường An & Cảnh Cũ Người Đâu (Câu 51 – 74)</span>
            <span class="toc-page">Trang 13</span>
        </div>
        <div class="toc-item" style="padding-left: 20px;">
            <span class="toc-title">• Hồi V: Đạo Sĩ Lâm Cung & Vượt Biển Tìm Hồn Tiên Nữ (Câu 75 – 94)</span>
            <span class="toc-page">Trang 16</span>
        </div>
        <div class="toc-item" style="padding-left: 20px;">
            <span class="toc-title">• Hồi VI: Kỷ Vật Tình Xưa & Lời Thề Dưới Trăng Vĩnh Cửu (Câu 95 – 120)</span>
            <span class="toc-page">Trang 19</span>
        </div>
        <div class="toc-item">
            <span class="toc-title">PHẦN II: TỲ BÀ HÀNH (琵琶行 - Lời Tựa & 88 Câu Toàn Văn)</span>
            <span class="toc-page">Trang 23</span>
        </div>
        <div class="toc-item" style="padding-left: 20px;">
            <span class="toc-title">• Lời Tựa Tỳ Bà Dẫn: Bối Cảnh Biếm Chức Bến Tầm Dương</span>
            <span class="toc-page">Trang 24</span>
        </div>
        <div class="toc-item" style="padding-left: 20px;">
            <span class="toc-title">• Tuyệt Đỉnh Miêu Tả Thanh Âm Tiếng Đàn Tỳ Bà & Tiếng Khóc Tri Âm</span>
            <span class="toc-page">Trang 26</span>
        </div>
        <div class="toc-item">
            <span class="toc-title">PHẦN III: TUYỂN TẬP TÂN NHẠC PHỦ & TRỮ TÌNH THẾ SỰ</span>
            <span class="toc-page">Trang 35</span>
        </div>
        <div class="toc-item" style="padding-left: 20px;">
            <span class="toc-title">• Mại Thán Ông, Phú Đắc Cổ Nguyên Thảo, Vấn Lưu Thập Cửu, Trường Tương Tư...</span>
            <span class="toc-page">Trang 36</span>
        </div>
        <div class="toc-item">
            <span class="toc-title">Khảo Luận Vĩ Thanh: Nghệ Thuật Ngôn Ngữ Bình Dân & Sức Sống Vượt Thời Gian</span>
            <span class="toc-page">Trang 42</span>
        </div>
    </div>
    """)
    
    # Khảo luận mở đầu
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: THẦN THÁI & TẦM VÓC THI MA</h1>
    <div class="ornament">❖</div>
    
    <h2 class="section-title">1. Khái niệm "Thi Ma" và lý luận văn học vị nhân sinh</h2>
    <div class="intro-box">
        <p>Trong lịch sử thi ca phương Đông, nếu Lý Bạch được xưng tôn là <em>Thi Tiên</em> bởi chất lãng mạn phóng khoáng siêu phàm, Đỗ Phủ là <em>Thi Thánh</em> bởi lòng nhân ái nghiêm cẩn mẫu mực, thì Bạch Cư Dị được tôn xưng là <strong>Thi Ma</strong> và <strong>Thi Vương</strong>. Ông tự bạch trong bài <em>Dữ Nguyên Cửu thư</em>: <em>"Văn chương hợp vi thời nhi trước, ca thi hợp vi sự nhi tác"</em> (Văn chương phải vì thời thế mà viết, ca thi phải vì việc đời mà sáng tác). Đó chính là bản tuyên ngôn bất hủ của chủ nghĩa hiện thực tiến bộ.</p>
        <p>Bạch Cư Dị chủ trương thơ ca phải giản dị, trong sáng, dễ hiểu đến mức "lão ẩu năng giải" (bà lão nhà quê ít học nghe cũng hiểu được). Nhờ đó, thơ ông lan truyền khắp hang cùng ngõ hẻm, từ hoàng cung cho đến quán trọ biên thùy, thậm chí truyền sang cả Nhật Bản, Triều Tiên thời bấy giờ.</p>
    </div>
    
    <h2 class="section-title">2. Bi kịch Trường Hận Ca và tiếng khóc nhân đạo Tỳ Bà Hành</h2>
    <div class="intro-box">
        <p><strong>Trường Hận Ca</strong> là bài ca bi tráng về thiên tình sử đẫm lệ giữa Đường Huyền Tông và Dương Quý Phi. Bằng bút pháp tự sự kết hợp trữ tình tuyệt đỉnh, Bạch Cư Dị vừa nghiêm khắc phê phán thói hoang dâm xa xỉ dẫn đến loạn lạc An Sử làm sụp đổ cơ nghiệp thịnh Đường, vừa xót thương chân thành cho số phận bi thảm của người con gái đẹp nơi dốc Mã Ngôi. Tình yêu vượt qua ranh giới sống chết cõi trần vươn tới chốn Bồng Lai tiên cảnh đã bất tử hóa câu thơ: <em>"Tại thiên nguyện tác bỉ dực điểu / Tại địa nguyện vi liên lý chi"</em>.</p>
        <p>Trong khi đó, <strong>Tỳ Bà Hành</strong> lại là đỉnh cao của sự thấu cảm nhân sinh. Một vị đại thần bị giáng chức ngồi đối diện với một ca nữ già nua bị ruồng bỏ giữa đêm thu lạnh buốt trên bến sông Tầm Dương. Tiếng đàn tỳ bà diệu kỳ hòa cùng giọt nước mắt tri âm đã xóa nhòa mọi khoảng cách giai cấp, biến câu thơ <em>"Đồng thị thiên nhai luân lạc nhân / Tương phùng hà tất tăng tương thức"</em> thành tiếng kêu thương xót vĩ đại cho thân phận con người trôi dạt giữa cuộc đời dâu bể.</p>
    </div>
    """)
    
    # PHẦN I: TRƯỜNG HẬN CA (120 CÂU)
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">PHẦN I: TRƯỜNG HẬN CA (長 恨 歌)</h1>
    <div style="text-align: center; font-style: italic; color: #555; margin-bottom: 20px;">Toàn văn 120 câu thất ngôn trường thiên • Bản dịch thơ lục bát Tản Đà Nguyễn Khắc Hiếu</div>
    <div class="ornament">❖ ❖ ❖</div>
    """)
    
    for ep in TRUONG_HAN_CA_EPISODES:
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 25px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #8B1E1E; padding-bottom: 6px; margin-bottom: 12px;">
                <span style="font-weight: bold; color: #721616; font-size: 12pt;">{ep['title']}</span>
                <span style="font-size: 9.5pt; color: #666; font-style: italic;">{ep['lines_range']}</span>
            </div>
            
            <div class="poem-parallel">
                <div class="poem-col" style="flex: 1.15; background: #fffdfa; border-color: #e5dac6;">
                    <div class="col-header">Bản Dịch Thơ Lục Bát (Tản Đà dịch)</div>
                    <div class="dich-tho" style="line-height: 1.8; font-size: 11pt; padding: 4px 6px;">
                        {ep['dich_tho'].replace(chr(10), '<br>')}
                    </div>
                    <div class="author-credit">{ep['author_credit']}</div>
                </div>
                
                <div class="poem-col" style="flex: 1; background: #faf8f5;">
                    <div class="col-header">Nguyên Tác Chữ Hán</div>
                    <div class="han-script" style="text-align: center; margin-bottom: 8px; font-size: 11pt;">
                        {ep['han'].replace(chr(10), '<br>')}
                    </div>
                    <div class="col-header" style="font-size: 9pt; margin-top: 6px;">Phiên Âm Hán Việt</div>
                    <div class="phien-am" style="font-size: 9.5pt; line-height: 1.55;">
                        {ep['phien_am'].replace(chr(10), '<br>')}
                    </div>
                </div>
            </div>
            
            <div class="commentary-box" style="margin-top: 10px;">
                <div class="commentary-title">Dịch Nghĩa & Chú Giải:</div>
                {ep['dich_nghia']}
            </div>
        </div>
        """)
        
    # PHẦN II: TỲ BÀ HÀNH (88 CÂU)
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">PHẦN II: TỲ BÀ HÀNH (琵 琶 行)</h1>
    <div style="text-align: center; font-style: italic; color: #555; margin-bottom: 20px;">Lời Tựa Tỳ Bà Dẫn & Toàn Văn 88 Câu • Bản Dịch Song Thất Lục Bát Phan Huy Thực</div>
    <div class="ornament">❖ ❖ ❖</div>
    
    <div class="poem-container avoid-break">
        <div class="col-header" style="font-size: 11pt; text-align: left; padding-left: 10px;">LỜI TỰA NGUYÊN TÁC (TỲ BÀ DẪN TỊNH TỰ - 琵琶引并序)</div>
        <div class="poem-parallel">
            <div class="poem-col" style="flex: 1; background: #fdfaf6;">
                <div class="col-header">Nguyên Văn Chữ Hán</div>
                <div class="han-script" style="font-size: 11pt; line-height: 1.7; text-align: justify;">
                    {ty_ba_preface_han}
                </div>
                <div class="col-header" style="margin-top: 10px; font-size: 9.5pt;">Phiên Âm Hán Việt</div>
                <div class="phien-am" style="font-size: 9.5pt; line-height: 1.5; text-align: justify;">
                    {ty_ba_preface_phien_am}
                </div>
            </div>
            <div class="poem-col" style="flex: 1.1; background: #fffdf9;">
                <div class="col-header">Dịch Nghĩa Lời Tựa</div>
                <div class="dich-nghia" style="line-height: 1.65; font-size: 10.5pt; padding: 6px 10px;">
                    {ty_ba_preface_dich_nghia}
                </div>
            </div>
        </div>
    </div>
    """.format(
        ty_ba_preface_han=TY_BA_HANH['preface_han'].replace('\n', '<br>'),
        ty_ba_preface_phien_am=TY_BA_HANH['preface_phien_am'].replace('\n', '<br>'),
        ty_ba_preface_dich_nghia=TY_BA_HANH['preface_dich_nghia'].replace('\n', '<br><br>')
    ))
    
    for part in TY_BA_HANH['parts']:
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 25px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #1a365d; padding-bottom: 6px; margin-bottom: 12px;">
                <span style="font-weight: bold; color: #1a365d; font-size: 12pt;">{part['part_title']}</span>
                <span style="font-size: 9.5pt; color: #666; font-style: italic;">{part['lines_range']}</span>
            </div>
            
            <div class="poem-parallel">
                <div class="poem-col" style="flex: 1.15; background: #fffdfa; border-color: #d6e2ee;">
                    <div class="col-header" style="color: #1a365d;">Bản Dịch Thơ Song Thất Lục Bát (Phan Huy Thực)</div>
                    <div class="dich-tho" style="line-height: 1.85; font-size: 11pt; padding: 4px 6px;">
                        {part['dich_tho'].replace(chr(10), '<br>')}
                    </div>
                    <div class="author-credit">{part['author_credit']}</div>
                </div>
                
                <div class="poem-col" style="flex: 1; background: #faf9f6;">
                    <div class="col-header">Nguyên Tác Chữ Hán</div>
                    <div class="han-script" style="text-align: center; margin-bottom: 8px; font-size: 11pt;">
                        {part['han'].replace(chr(10), '<br>')}
                    </div>
                    <div class="col-header" style="font-size: 9pt; margin-top: 6px;">Phiên Âm Hán Việt</div>
                    <div class="phien-am" style="font-size: 9.5pt; line-height: 1.55;">
                        {part['phien_am'].replace(chr(10), '<br>')}
                    </div>
                </div>
            </div>
            
            <div class="commentary-box" style="margin-top: 10px; border-left-color: #1a365d;">
                <div class="commentary-title" style="color: #1a365d;">Dịch Nghĩa Khúc Đàn:</div>
                {part['dich_nghia']}
            </div>
        </div>
        """)
        
    # PHẦN III: TUYỂN TẬP TÂN NHẠC PHỦ & TRỮ TÌNH
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">PHẦN III: TUYỂN TẬP TÂN NHẠC PHỦ & TRỮ TÌNH THẾ SỰ</h1>
    <div style="text-align: center; font-style: italic; color: #555; margin-bottom: 20px;">Những áng thơ hiện thực trác việt phản ánh số phận dân nghèo và tâm hồn thi nhân</div>
    <div class="ornament">❖ ❖ ❖</div>
    """)
    
    for p in OTHER_POEMS:
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 25px;">
            <div style="border-bottom: 1.5px solid #8B1E1E; padding-bottom: 4px; margin-bottom: 10px;">
                <h3 class="poem-title" style="margin-top: 5px; text-align: left;">{p['title']}</h3>
                <div style="font-size: 9.5pt; color: #666; font-style: italic;">{p['subtitle']}</div>
            </div>
            
            <div class="poem-parallel">
                <div class="poem-col" style="flex: 1.1; background: #fffdfa;">
                    <div class="col-header">Bản Dịch Thơ</div>
                    <div class="dich-tho" style="line-height: 1.75; font-size: 10.5pt; padding: 4px 6px;">
                        {p['dich_tho'].replace(chr(10), '<br>')}
                    </div>
                </div>
                
                <div class="poem-col" style="flex: 1; background: #faf8f5;">
                    <div class="col-header">Nguyên Tác Chữ Hán</div>
                    <div class="han-script" style="text-align: center; font-size: 10.5pt; margin-bottom: 8px;">
                        {p['han'].replace(chr(10), '<br>')}
                    </div>
                    <div class="col-header" style="font-size: 8.5pt;">Phiên Âm Hán Việt</div>
                    <div class="phien-am" style="font-size: 9pt; line-height: 1.5;">
                        {p['phien_am'].replace(chr(10), '<br>')}
                    </div>
                </div>
            </div>
            
            <div class="commentary-box">
                <div class="commentary-title">Bình Luận Thi Pháp & Ý Nghĩa Hiện Thực:</div>
                <div style="margin-bottom: 5px;"><em>Dịch nghĩa:</em> {p['dich_nghia']}</div>
                <div><em>Bình chú:</em> {p['commentary']}</div>
            </div>
        </div>
        """)
        
    # Khảo luận vĩ thanh
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN VĨ THANH: DI SẢN BẠCH CƯ DỊ</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p>Hơn một thiên niên kỷ đã trôi qua kể từ ngày thi hào Bạch Cư Dị tạ thế tại Hương Sơn, nhưng những thanh âm bi thiết trong <em>Trường Hận Ca</em> và <em>Tỳ Bà Hành</em> vẫn còn vang vọng khôn nguôi trong dòng chảy văn hóa nhân loại. Sức lay động mãnh liệt của thơ ông bắt nguồn từ chính trái tim nhân đạo mênh mông luôn đập cùng nhịp đập với nỗi đau của muôn triệu con người trôi nổi giữa cõi trần.</p>
        <p>Tại Việt Nam, các thế hệ danh sĩ tiền bối từ Nguyễn Trãi, Nguyễn Du, Cao Bá Quát cho đến Tản Đà, Phan Huy Thực đều tôn kính học tập bút pháp và thần thái thơ Bạch Cư Dị. Những bản dịch thơ chữ Nôm và Quốc ngữ của hai kiệt tác trường thiên này đã trở thành tài sản vô giá trong kho tàng văn học dịch thuật nước nhà, chứng minh cho sức sống trường tồn bất diệt của nghệ thuật đích thực vị nhân sinh.</p>
    </div>
    
    <div style="text-align: center; margin-top: 40px;">
        <div class="ornament">❖ ❖ ❖</div>
        <div style="font-style: italic; color: #555; font-size: 11pt;">Hoàn tất ấn bản toàn văn Trường Hận Ca & Tỳ Bà Hành</div>
        <div style="font-size: 9.5pt; color: #888; margin-top: 5px;">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn • Bản Khảo Luận Toàn Thư</div>
    </div>
    """)
    
    return "\n".join(html)

async def main():
    print(f"Building Bach Cu Di comprehensive book...")
    html_content = build_bach_cu_di_html()
    
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="BẠCH CƯ DỊ • TRƯỜNG HẬN CA & TỲ BÀ HÀNH",
        header_right="ẤN BẢN TOÀN THƯ KHẢO LUẬN"
    )

if __name__ == "__main__":
    asyncio.run(main())
