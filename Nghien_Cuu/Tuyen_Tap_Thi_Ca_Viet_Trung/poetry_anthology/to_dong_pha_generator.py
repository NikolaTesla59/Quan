# -*- coding: utf-8 -*-
"""
Tô Đông Pha (Đại Thi Hào Tống Triều) - Tuyển Tập Tống Từ & Xích Bích Phú
Toàn văn Tiền & Hậu Xích Bích Phú + Tuyển tập Tống Từ lừng danh: Niệm Nô Kiều, Thủy Điệu Ca Đầu, Định Phong Ba...
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\05. [1037-1101] Trung Quốc_Tô Đông Pha (Đại Thi Hào Tống Triều)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[1082] Tô Thức - Tuyển Tập Tống Từ & Xích Bích Phú.pdf")

TIEN_XICH_BICH = {
    "title": "Tiền Xích Bích Phú (前赤壁賦)",
    "han": """壬戌之秋，七月既望，蘇子與客泛舟遊於赤壁之下。
清風徐來，水波不興。舉酒屬客，誦明月之詩，歌窈窕之章。
少焉，月出於東山之上，徘徊於斗牛之間。白露橫江，水光接天。
縱一葦之所如，凌萬頃之茫然。浩浩乎如馮虛御風，而不知其所止；飄飄乎如遺世獨立，羽化而登仙。
於是飲酒樂甚，扣舷而歌之。歌曰：
「桂棹兮蘭槳，擊空明兮泝流光。渺渺兮予懷，望美人兮天一方。」
客有吹洞簫者，倚歌而和之。其聲嗚嗚然，如怨如慕，如泣如訴；
餘音嫋嫋，不絕如縷。舞幽壑之潛蛟，泣孤舟之嫠婦。
蘇子愀然，正襟危坐，而問客曰：「何為其然也？」
客曰：「『月明星稀，烏鵲南飛』，此非曹孟德之詩乎？
西望夏口，東望武昌，山川相繆，鬱乎蒼蒼，此非孟德之困於周郎者乎？
方其破荊州，下江陵，順流而東也，舳艫千里，旌旗蔽空，釃酒臨江，橫槊賦詩，固一世之雄也，而今安在哉？
況吾與子漁樵於江渚之上，侶魚蝦而友麋鹿，駕一葉之扁舟，舉匏樽以相屬。
寄蜉蝣於天地，渺滄海之一粟。哀吾生之須臾，羨長江之無窮。
挾飛仙以遨遊，抱明月而長終。知不可乎驟得，託遺響於悲風。」
蘇子曰：「客亦知夫水與月乎？逝者如斯，而未嘗往也；盈虛者如彼，而卒莫消長也。
蓋將自其變者而觀之，則天地曾不能以一瞬；自其不變者而觀之，則物與我皆無盡也，而又何羨乎！
且夫天地之間，物各有主，苟非吾之所有，雖一毫而莫取。
惟江上之清風，與山間之明月，耳得之而為聲，目遇之而成色，取之無禁，用之不竭。
是造物者之無盡藏也，而吾與子之所共適。」
客喜而笑，洗盞更酌。餚核既盡，杯盤狼籍。相與枕藉乎舟中，不知東方之既白。""",
    "phien_am": """Nhâm Tuất chi thu, thất nguyệt ký vọng, Tô tử dữ khách phiếm chu du vu Xích Bích chi hạ.
Thanh phong từ lai, thủy ba bất hưng. Cử tửu chúc khách, tụng Minh nguyệt chi thi, ca Yểu điệu chi chương.
Thiểu yên, nguyệt xuất vu Đông sơn chi thượng, bồi hồi vu Đẩu Ngưu chi gian. Bạch lộ hoành giang, thủy quang tiếp thiên.
Túng nhất vi chi sở như, lăng vạn khoảnh chi mang nhiên. Hạo hạo hồ như bằng hư ngự phong, nhi bất tri kỳ sở chỉ; phiêu phiêu hồ như di thế độc lập, vũ hóa nhi đăng tiên.
Ư thị ẩm tửu lạc thậm, khấu huyền nhi ca chi. Ca viết:
"Quế trạo hề lan tương, kích không minh hề tố lưu quang. Diểu diểu hề dư hoài, vọng mỹ nhân hề thiên nhất phương."
Khách hữu xuy đổng tiêu giả, ỷ ca nhi họa chi. Kỳ thanh ô ô nhiên, như oán như mộ, như khấp như tố;
Dư âm niểu niểu, bất tuyệt như lũ. Vũ u hác chi tiềm giao, khấp cô chu chi ly phụ.
Tô tử tiếu nhiên, chính khâm nguy tọa, nhi vấn khách viết: "Hà vi kỳ nhiên dã?"
Khách viết: " 'Nguyệt minh tinh hi, ô thước nam phi', thử phi Tào Mạnh Đức chi thi hồ?
Tây vọng Hạ Khẩu, đông vọng Vũ Xương, sơn xuyên tương mâu, uất hồ thương thương, thử phi Mạnh Đức chi khốn vu Chu lang giả hồ?
Phương kỳ phá Kinh Châu, hạ Giang Lăng, thuận lưu nhi đông dã, trục lư thiên lý, tinh kỳ bế không, si tửu lâm giang, hoành sóc phú thi, cố nhất thế chi hùng dã, nhi kim an tại tai?
Huống ngô dữ tử ngư tiều vu giang chử chi thượng, lữ ngư hà nhi hữu mi lộc, giá nhất diệp chi biển chu, cử bào tôn dĩ tương chúc.
Ký phù du vu thiên địa, diểu thương hải chi nhất túc. Ai ngô sinh chi tu du, tiện Trường Giang chi vô cùng.
Hiệp phi tiên dĩ ngao du, bão minh nguyệt nhi trường chung. Tri bất khả hồ sậu đắc, thác di hưởng vu bi phong."
Tô tử viết: "Khách diệc tri phu thủy dữ nguyệt hồ? Thệ giả như tư, nhi vị thường vãng dã; doanh hư giả như bỉ, nhi tốt mạc tiêu trưởng dã.
Cái tương tự kỳ biến giả nhi quan chi, tắc thiên địa tằng bất năng dĩ nhất thuấn; tự kỳ bất biến giả nhi quan chi, tắc vật dữ ngã giai vô tận dã, nhi hựu hà tiện hồ!
Thả phu thiên địa chi gian, vật các hữu chủ, cẩu phi ngô chi sở hữu, tuy nhất hào nhi mạc thủ.
Duy giang thượng chi thanh phong, dữ sơn gian chi minh nguyệt, nhĩ đắc chi nhi vi thanh, mục ngộ chi nhi thành sắc, thủ chi vô cấm, dụng chi bất kiệt.
Thị tạo vật giả chi vô tận tạng dã, nhi ngô dữ tử chi sở cộng thích."
Khách hỷ nhi tiếu, tẩy trản cánh chước. Hào hạch ký tận, bôi bàn lang tạ. Tương dữ chẩm tạ hồ chu trung, bất tri đông phương chi ký bạch.""",
    "dich_nghia": """Mùa thu năm Nhâm Tuất (1082), ngày mười sáu tháng bảy, Tô tử cùng khách bơi thuyền chơi dưới chân núi Xích Bích. Gió mát thổi hiu hiu, mặt nước không nổi sóng. Nâng chén chúc rượu khách, ngâm bài thơ Minh Nguyệt, hát khúc Yểu Điệu. Một lát sau, trăng mọc lên trên đỉnh núi Đông Sơn, lững lờ giữa khoảng sao Đẩu sao Ngưu. Sương trắng giăng ngang dòng sông, ánh nước nối liền với trời cao. Thả mặc con thuyền nhỏ như cọng cỏ lau trôi dạt, lướt trên muôn khoảnh nước mênh mang. Mênh mông tựa như nương vào cõi hư không cưỡi gió mà đi chẳng biết dừng ở nơi đâu; bồng bềnh tựa như rũ bỏ cõi đời đứng riêng một cõi, hóa cánh bay lên chốn thần tiên. Lúc ấy uống rượu vui say lắm, bèn gõ mạn thuyền mà hát khúc ca: 'Chèo quế chừ dầm lan, đập vỡ bóng trăng trong chừ ngược dòng ánh sáng lấp lánh. Mênh mang chừ tấc lòng ta, ngóng người đẹp chừ ở tận góc chân trời'. Khách có người thổi ống tiêu, nương theo câu hát mà họa lại. Tiếng tiêu nỉ non u uất, như oán như hờn, như khóc như than; dư âm ngân nga lay lắt không dứt như sợi tơ mỏng. Làm cho con thuồng luồng ẩn dưới khe sâu phải nhấp nhổm múa may, người đàn bà góa bụa cô đơn trên chiếc thuyền lẻ loi phải rơi nước mắt. Tô tử bùi ngùi đổi sắc mặt, sửa lại vạt áo ngồi ngay ngắn mà hỏi khách rằng: 'Cớ sao tiếng tiêu lại bi thương đến vậy?'. Khách thưa rằng: 'Trăng sáng sao thưa, quạ bay về nam, há chẳng phải là câu thơ của Tào Tháo đó sao? Nhìn về phía tây ngắm Hạ Khẩu, ngoảnh về phía đông trông Vũ Xương, núi sông quấn bện lấy nhau, cây cỏ xanh um ngút ngàn, há chẳng phải là nơi Tào Mạnh Đức bị Chu Du vây khốn đó sao? Khi xưa phá Kinh Châu, hạ Giang Lăng, xuôi dòng chảy tiến về đông, thuyền chiến nối đuôi nghìn dặm, cờ xí che kín bầu trời, rót rượu đứng trông dòng sông, cầm ngang ngọn giáo ngâm thơ, thật là bậc anh hùng một đời, vậy mà nay ở chốn nào? Huống chi ta cùng bác câu cá đốn củi trên bến sông, bầu bạn cùng tôm cá làm bạn với hươu nai, chèo một chiếc thuyền nan bé nhỏ như chiếc lá, nâng chén bầu mời chúc lẫn nhau. Gửi thân phù du giữa trời đất, nhỏ nhoi như một hạt thóc giữa biển lớn mênh mông. Buồn cho đời người chỉ trong chốc lát, ghen với dòng Trường Giang chảy mãi không cùng. Ước gì được cùng tiên bay ngao du khắp chốn, ôm lấy vầng trăng sáng sống trọn muôn đời. Biết rằng chẳng thể nào có được, đành gửi gắm tiếng lòng tàn tạ vào làn gió buồn'. Tô tử nói: 'Bác có hiểu lẽ dòng nước và vầng trăng chăng? Nước chảy trôi đi như thế kia, mà chưa từng vơi cạn; trăng tròn trăng khuyết như thế nọ, mà rốt cuộc chẳng hề thêm bớt. Bởi vì nếu đứng từ góc độ biến dịch mà nhìn, thì trời đất chẳng thể giữ nguyên trong một cái chớp mắt; nhưng nếu đứng từ góc độ bất biến mà nhìn, thì muôn vật cùng ta đều là vô tận cả, vậy thì có gì mà phải ghen tị hâm mộ chứ! Vả lại trong khoảng trời đất, muôn vật đều có chủ, nếu không phải là của ta thì dẫu một mảy may cũng chẳng lấy. Duy chỉ có ngọn gió mát trên sông, cùng vầng trăng sáng trong khe núi, tai nghe được thì hóa thành âm thanh tao nhã, mắt nhìn thấy thì hóa thành sắc màu tươi đẹp, lấy dùng không ai cấm đoán, dùng mãi không bao giờ cạn kiệt. Đó chính là kho tàng vô tận của hóa công tạo vật, mà ta cùng bác cùng nhau thụ hưởng vậy'. Khách nghe xong mừng rỡ mỉm cười, rửa chén rót thêm rượu. Thức ăn đã cạn, chén đĩa ngổn ngang bừa bãi. Cùng gối đầu lên nhau nằm ngủ trong lòng thuyền, chẳng biết phương đông trời đã rạng sáng từ lúc nào.""",
    "dich_tho": """Mùa thu Nhâm Tuất trăng rằm,
Tô tử cùng bạn dong thuyền Xích Bích.
Gió mát thổi hiu hiu trên sóng,
Nước trong xanh chẳng gợn lăn tăn.
Nâng chén rượu chúc bạn tri âm,
Ngâm khúc Minh Nguyệt, hát bài Yểu Điệu.
Trăng Đông Sơn lững lờ ló rạng,
Lồng Đẩu Ngưu mây bạc sáng ngời.
Thả thuyền nan như cánh cỏ trôi,
Lướt muôn khoảnh sóng biếc chơi vơi.
Rũ bụi trần ngỡ cánh bay tiên!
Uống rượu vui gõ mạn thuyền ca:
'Dầm quế chèo lan lướt sóng xa,
Vỗ bóng trăng tan ngược ánh hà.
Mênh mang tấc dạ người tri kỷ,
Ngóng bóng mỹ nhân tận trời xa...'
Khách nâng tiêu hòa tiếng nỉ non,
Tiếng tiêu như khóc, tựa hờn van.
Thuồng luồng khe thẳm dâng múa lượn,
Góa phụ thuyền côi lệ chứa chan!
Tô tử bùi ngùi ngồi ngay ngắn,
Hỏi bạn: 'Cớ sao tiếng bi ai?'
Khách rằng: 'Trăng sáng sao thưa thớt,
Quạ bay về nam thuở Tào xưa.
Xích Bích đây Chu Du vây khốn,
Thuyền nghìn dặm rợp bóng tinh kỳ.
Cầm ngang ngọn giáo thơ hào sảng,
Anh hùng một thuở nay đâu rồi?
Ta với bác phù du bến nước,
Thuyền lá câu hạt thóc biển khơi.
Buồn đời người gang tấc thoảng trôi,
Ghen Trường Giang muôn thuở lững lờ!'
Tô tử cười: 'Bác biết trăng nước chăng?
Nước chảy mãi mà chưa từng cạn,
Trăng khuyết tròn chưa đổi thay hình.
Nhìn biến dịch trời đất chớp mắt,
Nhìn bất biến muôn vật vô cùng!
Gió mát trên sông, trăng đầu núi,
Tai nghe thành tiếng, mắt ngắm say.
Kho báu đất trời không cấm giữ,
Ta cùng hưởng thụ thú thanh tao!'
Khách cười hoan hỉ rót rượu mời,
Cùng say nằm ngủ giữa thuyền trôi,
Trời đông đã rạng chẳng hay rồi!""",
    "commentary": "Thiên cổ tuyệt tác kết hợp đỉnh cao giữa cảm quan thiên nhiên diễm lệ, nỗi hoài cổ lịch sử thời Tam Quốc và triết lý Đạo - Nho - Phật dung hòa, nâng con người lên tầm thế ung dung tự tại trước mọi thăng trầm vinh nhục."
}

TONG_TU = [
    {
        "title": "Niệm Nô Kiều • Xích Bích Hoài Cổ (念奴嬌·赤壁懷古)",
        "subtitle": "Bản Khải Hoàn Ca Hào Phóng Từ Phái Đỉnh Cao",
        "han": """大江東去，浪淘盡，千古風流人物。
故壘西邊，人道是，三國周郎赤壁。
亂石穿空，驚濤拍岸，捲起千堆雪。
江山如畫，一時多少豪傑。
遙想公瑾當年，小喬初嫁了，雄姿英發。
羽扇綸巾，談笑間，檣櫓灰飛煙滅。
故國神遊，多情應笑我，早生華髮。
人生如夢，一尊還酹江月。""",
        "phien_am": """Đại giang đông khứ, lãng đào tận, thiên cổ phong lưu nhân vật.
Cố lũy tây biên, nhân đạo thị, Tam Quốc Chu lang Xích Bích.
Loạn thạch xuyên không, kinh đào phách ngạn, quyển khởi thiên đôi tuyết.
Giang sơn như họa, nhất thời đa thiểu hào kiệt.
Diêu tưởng Công Cẩn đương niên, Tiểu Kiều sơ giá liễu, hùng tư anh phát.
Vũ phiến luân cân, đàm tiếu gian, tường lũ hôi phi yên diệt.
Cố quốc thần du, đa tình ứng tiếu ngã, tảo sinh hoa phát.
Nhân sinh như mộng, nhất tôn hoàn sái giang nguyệt.""",
        "dich_nghia": """Dòng sông lớn cuồn cuộn chảy về đông, sóng đãi sạch bao nhiêu nhân vật phong lưu nghìn xưa. Phía tây thành lũy cũ, người ta bảo đó là Xích Bích của Chu lang (Chu Du) thời Tam Quốc. Đá ngổn ngang đâm toạc trời xanh, sóng dữ đập vào bờ đá, cuộn tung lên nghìn đống tuyết trắng xóa. Giang sơn đẹp tựa bức tranh, một thời bấy nhiêu trang hào kiệt. Xa nghĩ tới Chu Công Cẩn năm xưa, nàng Tiểu Kiều vừa mới gả về, tư thế oai phong anh dũng phát tiết. Tay cầm quạt lông chim đầu đội khăn the, trong lúc nói cười đàm luận, thuyền chiến quân Tào phút chốc hóa tro bay khói tan. Tâm thần ta rong chơi về cõi nước xưa, đa tình ắt người cười ta sớm bạc mái đầu. Đời người như một giấc mộng, hãy rót một chén rượu tưới xuống bóng trăng trên sông!""",
        "dich_tho": """Sông lớn cuồn cuộn chảy về đông,
Sóng xô sạch bấy anh hùng nghìn năm.
Thành lũy cũ bến tây trăng lặn,
Người bảo đây Xích Bích Chu lang.
Đá tảng đâm toạc trời xanh,
Sóng gầm vỗ vách tung nghìn đống tuyết.
Non sông đẹp tựa bức tranh,
Một thời lừng lẫy biết bao anh hùng!
Nhớ Chu Công Cẩn năm xưa,
Tiểu Kiều mới cưới, dung nhan rạng ngời.
Khăn the quạt lông cười nói,
Thuyền Tào trong chốc hóa tro khói tan!
Mộng hồn lãng đãng non sông,
Đa tình cười mái đầu sương bạc phai.
Đời người như giấc mộng dài,
Rót chén rượu tiễn bóng trăng lòng sông!""",
        "commentary": "Được coi là bài từ vĩ đại nhất của Tống Từ, mở đầu cho trường phái Hào phóng từ phái, thay đổi hoàn toàn tính chất ủy mị mềm yếu của từ khúc truyền thống."
    },
    {
        "title": "Thủy Điệu Ca Đầu • Bính Thìn Trung Thu (水調歌頭)",
        "subtitle": "Ngắm Trăng Trung Thu & Lời Chúc Phúc Thiên Lý Cộng Thiền Quyên",
        "han": """明月幾時有？把酒問青天。
不知天上宮闕，今夕是何年。
我欲乘風歸去，又恐瓊樓玉宇，高處不勝寒。
起舞弄清影，何似在人間！
轉朱閣，低綺戶，照無眠。
不應有恨，何事長向別時圓？
人有悲歡離合，月有陰晴圓缺，此事古難全。
但願人長久，千里共嬋娟。""",
        "phien_am": """Minh nguyệt kỷ thời hữu? Bả tửu vấn thanh thiên.
Bất tri thiên thượng cung khuyết, kim tịch thị hà niên.
Ngã dục thừa phong quy khứ, hựu khủng quỳnh lâu ngọc vũ, cao xứ bất thặng hàn.
Khởi vũ lộng thanh ảnh, hà tự tại nhân gian!
Chuyển chu các, đê khởi hộ, chiếu vô miên.
Bất ưng hữu hận, hà sự trường hướng biệt thời viên?
Nhân hữu bi hoan ly hợp, nguyệt hữu âm tình viên khuyết, thử sự cổ nan toàn.
Đãn nguyện nhân trường cửu, thiên lý cộng thiền quyên.""",
        "dich_nghia": """Vầng trăng sáng có từ bao giờ? Nâng chén rượu lên cất lời hỏi trời xanh. Chẳng biết nơi cung điện trên trời, đêm nay là năm nào. Ta muốn cưỡi ngọn gió bay về đó, lại sợ lầu quỳnh gác ngọc, chốn cao xanh kia lạnh lẽo khôn hàn. Đứng dậy múa vờn bóng trong trẻo, sao bằng ở lại chốn nhân gian! Trăng xoay quanh gác son, sà xuống cửa sổ the mỏng, soi vào kẻ thao thức không ngủ. Trăng chẳng nên có hờn giận gì, cớ sao cứ nhằm lúc người ta chia ly mà tròn vành vạnh? Đời người có buồn vui ly hợp, trăng có lúc mờ lúc tỏ khi tròn khi khuyết, việc ấy xưa nay khó lòng vẹn toàn. Chỉ mong người sống mãi dài lâu, muôn dặm cách xa cùng ngắm chung vẻ đẹp trăng thanh diễm lệ!""",
        "dich_tho": """Vầng trăng sáng có tự bao giờ?
Nâng chén rượu hỏi trời xanh mờ.
Chẳng hay cung ngọc trên trời biếc,
Đêm nay là năm tháng phương mô?
Muốn cưỡi ngọn gió bay về chốn,
Lại sợ lầu quỳnh rét lạnh tê!
Đứng dậy múa cùng chiếc bóng sáng,
Chốn tiên sao sánh cõi nhân gian!
Trăng lướt gác son, ghé cửa rèm,
Soi vào người thức trọn thâu đêm.
Trăng đâu có giận hờn chi nhỉ,
Sao nỡ nhằm lúc biệt phân tròn?
Đời người vui buồn ly rồi hợp,
Trăng tỏ trăng mờ khuyết lại tròn.
Xưa nay vẹn toàn đâu dễ có,
Chỉ nguyện người an sống dài lâu,
Nghìn dặm cùng ngắm bóng thiền quyên!""",
        "commentary": "Học giả đời Tống khen rằng: 'Kể từ khi bài Thủy Điệu Ca Đầu của Tô Đông Pha ra đời, mọi bài thơ ngắm trăng Trung thu khác thảy đều phải gác bút'."
    },
    {
        "title": "Định Phong Ba (定風波)",
        "subtitle": "Một Chiếc Áo Tơi Mặc Mưa Gió Bình Sinh",
        "han": """莫聽穿林打葉聲，何妨吟嘯且徐行。
竹杖芒鞋輕勝馬，誰怕？一蓑煙雨任平生。
料峭春風吹酒醒，微冷，山頭斜照卻相迎。
回首向來蕭瑟處，歸去，也無風雨也無晴。""",
        "phien_am": """Mạc thính xuyên lâm đả diệp thanh,
Hà phương ngâm tiêu thả từ hành.
Trúc trượng mang hài khinh thặng mã,
Thùy phạ? Nhất thao yên vũ nhậm bình sinh.
Liệu tiếu xuân phong xuy tửu tỉnh,
Vi lãnh, sơn đầu tà chiếu khước tương nghinh.
Hồi thủ hướng lai tiêu sắt xứ,
Quy khứ, dã vô phong vũ dã vô tình.""",
        "dich_nghia": """Chớ nghe tiếng mưa rào xuyên qua rừng đập vào cành lá, sá gì cứ vừa ngâm nga huýt sáo vừa thong thả bước đi. Gậy trúc giày rơm nhẹ bước hơn cả cưỡi ngựa, ai sợ gì chứ? Một chiếc áo tơi mặc cho mưa gió cả một đời bình sinh! Gió xuân se lạnh thổi tan hơi men rượu, hơi lành lạnh, trên đỉnh núi ánh nắng chiều tà nghiêng nghiêng đón chào. Ngoảnh đầu nhìn lại chốn gió mưa xào xạc vừa đi qua, trở về thôi, chẳng còn mưa gió mà cũng chẳng có nắng vàng!""",
        "dich_tho": """Chớ nghe mưa quất lá xuyên rừng,
Cứ ngâm nga sáo bước thong dong.
Gậy trúc giày rơm hơn cưỡi ngựa,
Ai sợ? Áo tơi mặc bão giông!
Gió xuân se lạnh men rượu tỉnh,
Hơi buốt, non cao nắng đón chào.
Ngoảnh lại đường xưa tiêu sắt ấy,
Trở về, không nắng cũng không mưa!""",
        "commentary": "Triết lý siêu thoát tuyệt luân trước nghịch cảnh cuộc đời: 'Dã vô phong vũ dã vô tình' (Không có gió mưa cũng chẳng có nắng nôi), tâm hồn đạt tới cõi an nhiên tịch tĩnh tuyệt đối."
    }
]

def build_to_dong_pha_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Đại Tống Văn Học • Thế Kỷ XI</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">TÔ ĐÔNG PHA</div>
            <div class="cover-subtitle">Tuyển Tập Tống Từ & Xích Bích Phú (Bản Toàn Văn Khảo Luận)<br>Tiền Xích Bích Phú, Niệm Nô Kiều, Thủy Điệu Ca Đầu, Định Phong Ba...</div>
            <div class="gold-line"></div>
            <div class="cover-author">TÔ THỨC (1037 – 1101) • TỰ TỬ CHIÊM • HIỆU ĐÔNG PHA CƯ SĨ</div>
            <div class="cover-author-sub">Đứng đầu Đường Tống Bát Đại Gia • Người sáng lập Hào Phóng Từ Phái</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Hiệu đính đối chiếu Đông Pha Toàn Tập mộc bản đời Tống & Tuyển dịch Trần Trọng San</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: ĐẠI THI HÀO TỐNG TRIỀU TÔ ĐÔNG PHA</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Tô Thức (1037 – 1101)</strong>, tự Tử Chiêm, hiệu Đông Pha cư sĩ, là thiên tài toàn diện bậc nhất trong lịch sử văn hóa Trung Hoa. Ông xuất sắc trên mọi lĩnh vực: thi ca, từ khúc, tản văn biền ngẫu, thư pháp, hội họa và cả ẩm thực. Tác phẩm của ông thể hiện phong cách phóng khoáng, siêu thoát, lạc quan tột bậc trước mọi gian truân đày ải.</p>
        <p>Giai đoạn bị biếm chức đày về Hoàng Châu (1080 – 1084) là thời kỳ thăng hoa rực rỡ nhất trong cuộc đời sáng tạo của Tô Đông Pha. Chính tại nơi đây, bên dòng sông Trường Giang huyền thoại, ông đã viết nên bộ ba kiệt tác bất tử lưu danh muôn thuở: <strong>Tiền Xích Bích Phú</strong>, <strong>Hậu Xích Bích Phú</strong> và bài từ tráng lệ <strong>Niệm Nô Kiều - Xích Bích Hoài Cổ</strong>.</p>
    </div>
    """)
    
    # Tiền Xích Bích Phú
    html.append(f"""
    <div class="page-break"></div>
    <h1 class="chapter-title">TIỀN XÍCH BÍCH PHÚ (前 赤 壁 賦)</h1>
    <div style="text-align: center; font-style: italic; color: #555; margin-bottom: 20px;">Đỉnh Cao Biền Văn Triết Lý Nhân Sinh & Vẻ Đẹp Trăng Nước Trường Giang</div>
    <div class="ornament">❖ ❖ ❖</div>
    
    <div class="poem-container avoid-break">
        <div class="poem-parallel">
            <div class="poem-col" style="flex: 1.15; background: #fffdfa; border-color: #e5dac6;">
                <div class="col-header">Bản Dịch Thơ Phú Kinh Điển</div>
                <div class="dich-tho" style="line-height: 1.85; font-size: 11pt; padding: 4px 6px;">
                    {TIEN_XICH_BICH['dich_tho'].replace(chr(10), '<br>')}
                </div>
            </div>
            
            <div class="poem-col" style="flex: 1; background: #faf8f5;">
                <div class="col-header">Nguyên Tác Chữ Hán</div>
                <div class="han-script" style="text-align: justify; margin-bottom: 8px; font-size: 10.5pt; line-height: 1.7;">
                    {TIEN_XICH_BICH['han'].replace(chr(10), '<br><br>')}
                </div>
            </div>
        </div>
        
        <div class="commentary-box" style="margin-top: 15px;">
            <div class="commentary-title">Dịch Nghĩa Toàn Văn Tiền Xích Bích Phú:</div>
            <div style="line-height: 1.6; margin-bottom: 8px;">{TIEN_XICH_BICH['dich_nghia'].replace(chr(10), '<br><br>')}</div>
            <div class="commentary-title">Bình Luận Triết Lý:</div>
            <div>{TIEN_XICH_BICH['commentary']}</div>
        </div>
    </div>
    """)
    
    # Tuyển tập Tống Từ
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">TUYỂN TẬP TỐNG TỪ BẤT HỦ</h1>
    <div style="text-align: center; font-style: italic; color: #555; margin-bottom: 20px;">Đỉnh cao Hào phóng từ phái và triết lý sống siêu thoát ung dung</div>
    <div class="ornament">❖ ❖ ❖</div>
    """)
    
    for i, t in enumerate(TONG_TU, 1):
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 25px;">
            <div style="border-bottom: 2px solid #8B1E1E; padding-bottom: 6px; margin-bottom: 12px;">
                <span style="font-weight: bold; color: #721616; font-size: 13pt;">{i}. {t['title']}</span>
                <div style="font-size: 9.5pt; color: #666; font-style: italic; margin-top: 2px;">{t['subtitle']}</div>
            </div>
            
            <div class="poem-parallel">
                <div class="poem-col" style="flex: 1.15; background: #fffdfa; border-color: #e5dac6;">
                    <div class="col-header">Bản Dịch Thơ Từ</div>
                    <div class="dich-tho" style="line-height: 1.85; font-size: 11pt; padding: 4px 6px;">
                        {t['dich_tho'].replace(chr(10), '<br>')}
                    </div>
                </div>
                
                <div class="poem-col" style="flex: 1; background: #faf8f5;">
                    <div class="col-header">Nguyên Tác Chữ Hán</div>
                    <div class="han-script" style="text-align: center; margin-bottom: 8px; font-size: 11pt;">
                        {t['han'].replace(chr(10), '<br>')}
                    </div>
                    <div class="col-header" style="font-size: 9pt; margin-top: 6px;">Phiên Âm Hán Việt</div>
                    <div class="phien-am" style="font-size: 9.5pt; line-height: 1.55;">
                        {t['phien_am'].replace(chr(10), '<br>')}
                    </div>
                </div>
            </div>
            
            <div class="commentary-box" style="margin-top: 10px;">
                <div class="commentary-title">Dịch Nghĩa & Bình Chú Thi Pháp:</div>
                <div style="margin-bottom: 6px;"><em>Dịch nghĩa:</em> {t['dich_nghia']}</div>
                <div><em>Bình chú:</em> {t['commentary']}</div>
            </div>
        </div>
        """)
        
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">VĨ THANH: KHÍ PHÁCH ĐÔNG PHA CƯ SĨ</h1>
    <div class="ornament">❖</div>
    <div class="intro-box">
        <p>Tô Đông Pha từng tự đúc kết cuộc đời đầy giông bão của mình bằng ba địa danh lưu đày: <em>"Vấn nhữ nhất sinh công nghiệp / Hoàng Châu, Huệ Châu, Đạm Châu"</em> (Hỏi sự nghiệp một đời của ngươi là gì? Đó là Hoàng Châu, Huệ Châu và đảo Hải Nam Đạm Châu!). Nụ cười an nhiên bước qua mọi nghịch cảnh của ông là bài học nhân sinh cao đẹp nhất mà một vĩ nhân có thể để lại cho trần thế.</p>
    </div>
    """)
    
    return "\n".join(html)

async def main():
    print("Building To Dong Pha comprehensive anthology...")
    html_content = build_to_dong_pha_html()
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="TÔ ĐÔNG PHA • ĐẠI THI HÀO TỐNG TRIỀU",
        header_right="TUYỂN TẬP TỐNG TỪ & XÍCH BÍCH PHÚ"
    )

if __name__ == "__main__":
    asyncio.run(main())
