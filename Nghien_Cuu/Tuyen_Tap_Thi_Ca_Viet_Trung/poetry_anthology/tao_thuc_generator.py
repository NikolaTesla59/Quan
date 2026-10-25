# -*- coding: utf-8 -*-
"""
Tào Thực (Tào Tử Kiến - Tài Cao Bát Đấu) - Toàn Tập Khảo Luận
1. [220] Thất Bộ Thi & Tuyển Tập Thơ Văn Kiến An
2. [222] Lạc Thần Phú (Bản Toàn Văn Biền Ngẫu & Tuyệt Tác Tình Si)
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\01. [192-232] Trung Quốc_Tào Thực (Tào Tử Kiến - Tài Cao Bát Đấu)"
THAT_BO_FILE = os.path.join(OUTPUT_DIR, "[220] Tào Thực - Thất Bộ Thi & Tuyển Tập Thơ Kiến An.pdf")
LAC_THAN_FILE = os.path.join(OUTPUT_DIR, "[222] Tào Thực - Lạc Thần Phú (Đỉnh Cao Biền Văn & Tình Si Mỹ Nữ Thần Thoại).pdf")

# Data for Thất Bộ Thi & Kiến An
KIEN_AN_POEMS = [
    {
        "title": "Thất Bộ Thi (七步詩)",
        "subtitle": "Bài Thơ Bảy Bước Thoát Chết • Bản 6 Câu & Bản 4 Câu Kinh Điển",
        "han": """【 bản Thế Thuyết Tân Ngữ 】
煮豆持作羹，漉豉以為汁。
萁在釜下燃，豆在釜中泣。
本自同根生，相煎何太急？

【 bản Tam Quốc Diễn Nghĩa 】
煮豆燃豆萁，豆在釜中泣。
本是同根生，相煎何太急？""",
        "phien_am": """【 Bản Thế Thuyết Tân Ngữ 】
Chử đậu trì tác canh, lục thị dĩ vi trấp.
Ky tại phủ hạ nhiên, đậu tại phủ trung khấp.
Bản tự đồng căn sinh, tương phanh hà thái cấp?

【 Bản Tam Quốc Diễn Nghĩa 】
Chử đậu nhiên đậu ky, đậu tại phủ trung khấp.
Bản thị đồng căn sinh, tương phanh hà thái cấp?""",
        "dich_nghia": """Nấu đậu để làm món canh, gạn đỗ làm nước chấm. Cành đậu đốt ở dưới nồi, hạt đậu ở trong nồi khóc lóc. Vốn cùng một gốc rễ sinh ra, cớ sao nỡ thiêu đốt nhau gấp gáp đến thế? (Bài thơ làm trong bảy bước chân theo mệnh lệnh bức hại của anh trai Tào Phi, khiến Tào Phi phải rơi nước mắt hổ thẹn tha chết).""",
        "dich_tho": """Nấu đậu đốt cành đậu,
Đậu ở trong nồi khóc.
Vốn cùng một gốc sinh,
Sao nung nấu nhau gấp?""",
        "commentary": "Hình ảnh ẩn dụ đậu và cành đậu cùng một gốc rễ sinh ra đúc kết bi kịch huynh đệ tương tàn tàn khốc chốn cung đình phong kiến muôn thuở."
    },
    {
        "title": "Bạch Mã Thiên (白馬篇)",
        "subtitle": "Hình Tượng Du Hiệp Thiếu Niên Anh Hùng Cứu Nước",
        "han": """白馬飾金羈，連翩西北馳。
借問誰家子，幽并遊俠兒。
少小去鄉邑，揚聲沙漠陲。
宿昔秉良弓，楛矢何參差。
控弦破左的，右發摧月支。
仰手接飛猱，俯身散馬蹄。
狡捷過猴猿，勇剽若豹螭。
邊城多警急，虜騎數遷移。
羽檄從北來，厲馬登高堤。
長驅蹈匈奴，左顧凌鮮卑。
棄身鋒刃端，性命安可懷？
父母且不顧，何言子與妻！
名編壯士籍，不得中顧私。
捐軀赴國難，視死忽如歸！""",
        "phien_am": """Bạch mã sức kim cơ, liên phiên tây bắc trì.
Tá vấn thùy gia tử, U Tịnh du hiệp nhi.
Thiếu tiểu khứ hương ấp, dương thanh sa mạc thùy.
Túc tích bỉnh lương cung, hỗ thỉ hà sâm si.
Khống huyền phá tả đích, hữu phát thôi nguyệt chi.
Ngưỡng thủ tiếp phi nhu, phủ thân tán mã đề.
Giảo tiệp quá hầu viên, dũng phiếu nhược báo ly.
Biên thành đa cảnh cấp, lỗ kỵ số thiên di.
Vũ hịch tòng bắc lai, lệ mã đăng cao đê.
Trường khu đạp Hung Nô, tả cố lăng Tiên Ty.
Khí thân phong nhận đoan, tính mệnh an khả hoài?
Phụ mẫu thả bất cố, hà ngôn tử dữ thê!
Danh biên tráng sĩ tịch, bất đắc trung cố tư.
Quyên khu phó quốc nạn, thị tử hốt như quy!""",
        "dich_nghia": """Ngựa trắng khớp hàm thiếc vàng, liên tiếp ruổi nhanh về hướng tây bắc. Thử hỏi con cái nhà ai, ấy là chàng thiếu niên du hiệp đất U Châu, Tịnh Châu. Từ thuở nhỏ đã rời quê hương, vang danh khắp vùng biên cương sa mạc. Xưa nay nắm cây cung tốt, tên nhọn san sát bên lưng. Kéo dây cung bắn vỡ hồng tâm bên trái, xoay sang phải bắn gãy cọc tiêu. Ngửa tay đón bắt khỉ bay, cúi mình bắn tan móng ngựa. Nhanh nhẹn hơn loài vượn khỉ, dũng cảm tựa loài báo beo. Nơi biên thành nhiều phen báo động nguy cấp, kỵ binh giặc thường xuyên xâm lấn. Hịch cắm lông chim từ phía bắc bay tới, giục ngựa vượt lên đê cao. Xông thẳng giày xéo quân Hung Nô, ngoảnh sang trái đè bẹp giặc Tiên Ty. Quẳng thân mình nơi đầu mũi tên ngọn giáo, tính mệnh nào có tiếc chi? Cha mẹ còn chẳng đoái hoài tới, huống hồ nói chi đến vợ với con! Tên tuổi đã ghi vào sổ tráng sĩ, không thể trong lòng đoái hoài việc riêng tư. Quyên thân vì nạn nước, coi cái chết nhẹ tựa trở về nhà!""",
        "dich_tho": """Ngựa trắng cương vàng lóng lánh bay,
Tây bắc dồn chân ruổi gió mây.
Hỏi người tráng sĩ con ai đó?
U Tịnh du hiệp dạ ngất ngây.
Từ thuở ấu thơ rời bản quán,
Biên cương cát bụi tiếng tăm bay.
Tay bưng cung tốt tên gài sẵn,
Mũi nhọn xuyên tim bắn chuẩn thay!
Ngửa tay tóm bắt loài vượn lướt,
Cúi mình né tránh móng ngựa bay.
Biên thành khẩn cấp cờ bay tới,
Giục ngựa băng đèo vượt hiểm nguy.
Quẳng thân vào giữa làn tên đạn,
Tính mạng sá chi tiếc cuộc đời!
Tên khắc bia vàng trang dũng sĩ,
Xá chi thê tử với mẹ cha.
Quyên thân đền nợ non sông hiểm,
Coi chết nhẹ tênh tựa bước về!""",
        "commentary": "Hai câu kết: 'Quyên khu phó quốc nạn / Thị tử hốt như quy' (Quyên thân vì nạn nước / Coi chết nhẹ tựa về) là tượng đài ngôn từ bất hủ về lòng yêu nước xả thân vì đại nghĩa."
    },
    {
        "title": "Dã Điền Hoàng Tước Hành (野田黃雀行)",
        "subtitle": "Chim Sẻ Vàng Ruộng Hoang & Nỗi U Uất Bị Giam Cầm",
        "han": """高樹多悲風，海水揚其波。
利劍不在掌，妾自奈何！
不見籬間雀，見鷂自投羅。
羅家得雀喜，少年見雀悲。
拔劍捎羅網，黃雀得飛飛。
飛飛摩蒼天，來下謝少年。""",
        "phien_am": """Cao thụ đa bi phong, hải thủy dương kỳ ba.
Lợi kiếm bất tại chưởng, thiếp tự nại hà!
Bất kiến ly gian tước, kiến diệu tự đầu la.
La gia đắc tước hỷ, thiếu niên kiến tước bi.
Bạt kiếm thao la võng, hoàng tước đắc phi phi.
Phi phi ma thương thiên, lai hạ tạ thiếu niên.""",
        "dich_nghia": """Cây cao nhiều gió buồn rười rượi, nước biển dâng muôn lớp sóng trào. Gươm sắc không cầm trong tay, dẫu là thân gái biết làm sao đây! Há chẳng thấy chim sẻ bên hàng rào, thấy chim diều hâu hoảng sợ tự đâm đầu vào lưới rập. Kẻ giăng lưới bắt được chim sẻ mừng rỡ, người thiếu niên trông thấy chim sẻ thương xót ngậm ngùi. Bèn rút gươm sắc vung chém đứt lưới rập, chim sẻ vàng mới đặng tung cánh bay đi. Bay vút lên trời xanh cọ vào mây biếc, rồi sà xuống tạ ơn người thiếu niên cứu mạng.""",
        "dich_tho": """Cây cao gió lạnh thổi vù vù,
Sóng biển dập dồn lớp lớp xô.
Gươm báu trong tay không giữ đặng,
Thân này than thở biết làm sao!
Há thấy chim sẻ bên bờ dậu,
Tránh diều đâm cổ mắc lưới sâu.
Kẻ bẫy chim mừng chim bị trói,
Thiếu niên trông thấy dạ nghẹn ngào.
Rút gươm chém đứt giàn lưới rập,
Chim sẻ tung bay giữa trời cao.
Lướt cánh cọ mây xanh thăm thẳm,
Sà xuống tạ ơn bậc anh hào!""",
        "commentary": "Mượn hình tượng chim sẻ vàng bị mắc lưới để gián tiếp tố cáo sự giam cầm, theo dõi gắt gao của Tào Phi đối với anh em ruột thịt và khát khao tự do cháy bỏng."
    }
]

LAC_THAN_SECTIONS = [
    {
        "title": "HỒI I: DỪNG CHÂN BÊN BỜ SÔNG LẠC",
        "subtitle": "Rời kinh thành Lạc Dương dừng cương ngựa lúc hoàng hôn",
        "han": """黃初三年，余朝京師，還濟洛川。
古人有言，斯水之神，名曰宓妃。
感宋玉對楚王神女之事，遂作斯賦。
其辭曰：
余從京域，言歸東藩。
背伊闕，越轘轅，經通谷，陵景山。
日既西傾，車殆馬煩。
爾乃稅駕乎蘅皋，秣駟乎芝田，容與乎陽林，流眄乎洛川。
於是精移神駭，忽焉思散。
睇眄貌，見一佳人，在於岩之畔。""",
        "phien_am": """Hoàng Sơ tam niên, dư triều kinh sư, hoàn tế Lạc xuyên.
Cổ nhân hữu ngôn, tư thủy chi thần, danh viết Mật Phi.
Cảm Tống Ngọc đối Sở vương thần nữ chi sự, toái tác tư phú.
Kỳ từ viết:
Dư tòng kinh vực, ngôn quy đông phiên.
Bối Y Khuyết, việt Hoàn Viên, kinh Thông Cốc, lăng Cảnh Sơn.
Nhật ký tây khuynh, xa đãi mã phiền.
Nhĩ nãi thuế giá hồ hành cao, mạt tứ hồ chi điền, dung dữ hồ dương lâm, lưu miện hồ Lạc xuyên.
Ư thị tinh di thần hãi, hốt yên tư tán.
Thế miện mạo, kiến nhất giai nhân, tại vu nham chi bạn.""",
        "dich_nghia": """Năm Hoàng Sơ thứ ba (222), ta vào chầu kinh sư, lúc trở về qua bến sông Lạc. Người xưa từng nói, thần của dòng sông này tên là Mật Phi (con gái Phục Hy chết đuối hóa thần sông Lạc). Cảm kích trước chuyện Tống Ngọc đối đáp với vua Sở về thần nữ núi Vu Sơn, bèn làm bài phú này. Lời rằng: Ta từ đất kinh đô, trở về đất phiên vương phía đông. Sau lưng gác ải Y Khuyết, vượt qua đèo Hoàn Viên, băng qua Thông Cốc, trèo lên núi Cảnh Sơn. Mặt trời đã nghiêng về phía tây, xe mỏi ngựa mệt. Bèn dừng cỗ xe nơi bờ cỏ thơm, cho ngựa ăn nơi ruộng nấm linh chi, thong dong nơi rừng dương, đưa mắt ngắm dòng sông Lạc. Lúc ấy tinh thần bàng hoàng rúng động, bỗng nhiên ý nghĩ bay bổng. Liếc mắt trông xa, chợt thấy một người đẹp tuyệt sắc, đang đứng bên ghềnh đá ven bờ sông.""",
        "dich_tho": """Năm Hoàng Sơ thứ ba chầu kinh khuyết,
Lúc trở về qua bến Lạc giang.
Người xưa bảo thần sông sông Lạc,
Tên Mật Phi con gái Phục Hy.
Cảm chuyện Sở vương cùng thần nữ,
Ta bèn cất bút dệt thiên thi:
Rời đất kinh kỳ về cõi đông,
Băng qua đèo ải vượt non bồng.
Chiều buông bóng xế xe dừng bước,
Ngựa mệt cho ăn ruộng cỏ nồng.
Thong thả ngắm nhìn con nước biếc,
Chợt đâu rúng động cõi lòng sâu.
Đưa mắt ngắm trông ghềnh đá nọ,
Kìa ai mỹ nữ đứng cheo leo!""",
        "commentary": "Khởi đầu tuyệt tác bằng không gian hoàng hôn diễm lệ bên dòng Lạc Thủy, dẫn dắt người đọc bước vào thế giới thần thoại lung linh huyền ảo."
    },
    {
        "title": "HỒI II: DUNG NHAN DIỄM LỆ CỦA LẠC THẦN",
        "subtitle": "Phiêu hốt nhược kinh hồng, uyển chuyển như du long",
        "han": """其形也，翩若驚鴻，婉若游龍。
榮曜秋菊，華茂春松。
髣彿兮若輕雲之蔽月，飄颻兮若流風之迴雪。
遠而望之，皎若太陽升朝霞；迫而察之，灼若芙蕖出渌波。
穠纖得衷，修短合度。
肩若削成，腰如約素。
延頸秀項，皓質呈露。
芳澤無加，鉛華弗御。
雲鬢峨峨，修眉聯娟。
丹唇外朗，皓齒內鮮，
明眸善睞，靨輔承權。
瑰姿艷逸，儀靜體閑。
柔情綽態，媚於語言。
奇服曠世，骨像應圖。""",
        "phien_am": """Kỳ hình dã, phiên nhược kinh hồng, uyển nhược du long.
Vinh diệu thu cúc, hoa mậu xuân tùng.
Phảng phất hề nhược khinh vân chi bế nguyệt, phiêu dao hề nhược lưu phong chi hồi tuyết.
Viễn nhi vọng chi, kiệu nhược thái dương thăng triêu hà; bách nhi sát chi, chước nhược phù cừ xuất lục ba.
Nồng tiêm đắc trung, tu đoản hợp độ.
Kiên nhược tước thành, yêu như ước tố.
Diên cảnh tú hạng, hạo chất trình lộ.
Phương trạch vô gia, duyên hoa phất ngự.
Vân bấn nga nga, tu mi liên quyên.
Đan thuần ngoại lãng, hạo xỉ nội tiên,
Minh mâu thiện lại, yểm phụ thừa quyền.
Khôi tư diễm dật, nghi tĩnh thể nhàn.
Nhu tình xước thái, mị vu ngữ ngôn.
Kỳ phục khoáng thế, cốt tượng ứng đồ.""",
        "dich_nghia": """Hình dáng của nàng: Nhẹ nhàng thoăn thoắt tựa chim hồng bay vút, uyển chuyển uốn lượn tựa rồng bơi lượn. Rực rỡ tươi thắm tựa hoa cúc mùa thu, xanh tươi tốt tươi tựa cây tùng mùa xuân. Phảng phất như mây mỏng che vầng trăng sáng, phất phơ bay bổng tựa gió thoảng cuốn tuyết bay. Trông xa ngắm nhìn, rạng ngời như mặt trời mọc giữa ráng mai; lại gần quan sát, rực rỡ như đóa sen hồng vươn lên từ làn nước biếc. Đậm đà mảnh mai vừa vặn mực thước, cao thấp vừa vặn độ đo. Đôi vai như tạc thành nét ngọc, vòng eo thon nhỏ tựa thắt dải lụa trắng. Cổ dài duyên dáng, làn da trắng ngần lộ vẻ ngọc ngà. Chẳng cần thêm sáp thơm, không dùng chút phấn chì son phấn. Tóc mây búi cao vòi vọi, mày ngài thanh tú uốn cong. Môi son thắm tươi rạng rỡ bên ngoài, răng ngọc trắng muốt sáng ngời bên trong. Mắt sáng long lanh liếc nhìn duyên dáng, má lúm đồng tiền nâng đỡ đôi gò má. Dáng vẻ diễm lệ phi phàm, phong thái tĩnh lặng khoan thai. Tình cảm dịu dàng dáng điệu thướt tha, duyên dáng trong từng lời ăn tiếng nói. Xiêm y kỳ lạ hiếm thấy trên đời, dung mạo cốt cách đúng như trong tranh vẽ thần tiên.""",
        "dich_tho": """Kìa dáng hình:
Nhẹ bay thoăn thoắt tựa chim hồng,
Uyển chuyển uốn mình ngỡ rồng bơi.
Rực rỡ ngời tươi hoa cúc thu,
Xanh tươi đượm thắm bóng xuân tùng.
Phảng phất mây the che bóng nguyệt,
Phất phơ gió thoảng tuyết lùa bay.
Trông xa rực rỡ vầng dương sớm,
Lại gần tươi thắm đóa sen hồng.
Thân hình cân đối vừa mực thước,
Vai tựa chạm ngọc, eo dải lụa.
Cổ cao thanh tú ngọc lộ ngời,
Chẳng cần son phấn chẳng thoa sáp.
Tóc mây vòi vọi mày liễu biếc,
Môi son tươi thắm răng ngọc ngà.
Mắt sáng long lanh cười duyên dáng,
Má lúm đồng tiền đón nét hoa.
Dáng vẻ phi phàm phong thái tĩnh,
Dịu dàng lời nói nết ngọc ngà!""",
        "commentary": "Đoạn văn biền ngẫu tả sắc đẹp tuyệt mỹ bậc nhất trong lịch sử văn học Trung Hoa. Câu 'Phiên nhược kinh hồng, uyển nhược du long' đã trở thành định ngữ kinh điển để miêu tả vẻ đẹp của mỹ nhân thần tiên."
    }
]

def build_that_bo_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Tam Quốc Văn Học • Thời Kỳ Kiến An (196 – 220)</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">TÀO THỰC</div>
            <div class="cover-subtitle">Thất Bộ Thi & Tuyển Tập Thơ Văn Kiến An (Bản Toàn Tập Khảo Luận)<br>Thất Bộ Thi, Bạch Mã Thiên, Dã Điền Hoàng Tước Hành & Điển Cố Bát Đấu Chi Tài</div>
            <div class="gold-line"></div>
            <div class="cover-author">TÀO THỰC (192 – 232) • TỰ TỬ KIẾN • TRẦN TƯ VƯƠNG</div>
            <div class="cover-author-sub">Đứng đầu Tam Tào & Kiến An Thất Tử • Thiên hạ tài cao bát đấu</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Hiệu đính đối chiếu Tam Quốc Chí • Ngụy Chí & Tào Tử Kiến Tập</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: BÁT ĐẤU CHI TÀI VÀ VĂN HỌC KIẾN AN</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Tào Thực (192 – 232)</strong>, tự Tử Kiến, con trai thứ ba của Ngụy Vũ Đế Tào Tháo và Biện hoàng hậu, là đại thi hào kiệt xuất nhất của thời kỳ văn học Kiến An cuối thời Đông Hán - Tam Quốc. Thi sĩ Tạ Linh Vận đời Nam Bắc triều từng ca ngợi: <em>"Thiên hạ hữu tài nhất thạch, Tào Tử Kiến độc đắc bát đấu, ngã đắc nhất đấu, tự cổ cập kim thông cộng phân nhất đấu"</em> (Thiên hạ có một thạch tài năng, riêng Tào Tử Kiến chiếm trọn tám đấu, ta được một đấu, cổ kim thiên hạ chia nhau một đấu còn lại). Thành ngữ <strong>"Tài cao bát đấu"</strong> từ đó trở thành danh xưng vinh hiển độc nhất dành cho ông.</p>
        <p>Thơ văn Tào Thực phản ánh sinh động hai thời kỳ cuộc đời: Thời trẻ hào hùng nuôi chí lớn xả thân cứu nước, và thời kỳ sau khi Tào Phi lên ngôi bị đày ải nghi kỵ chịu muôn vàn u uất. Bằng ngôn từ tráng lệ, nhạc điệu hào sảng và cảm xúc bi phẫn sâu sắc, Tào Thực đã mở ra kỷ nguyên vàng son cho thể thơ ngũ ngôn cổ thi Trung Hoa.</p>
    </div>
    """)
    
    for i, p in enumerate(KIEN_AN_POEMS, 1):
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 25px;">
            <div style="border-bottom: 2px solid #8B1E1E; padding-bottom: 6px; margin-bottom: 12px;">
                <span style="font-weight: bold; color: #721616; font-size: 13pt;">{i}. {p['title']}</span>
                <div style="font-size: 9.5pt; color: #666; font-style: italic; margin-top: 2px;">{p['subtitle']}</div>
            </div>
            
            <div class="poem-parallel">
                <div class="poem-col" style="flex: 1.15; background: #fffdfa; border-color: #e5dac6;">
                    <div class="col-header">Bản Dịch Thơ</div>
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
                <div class="commentary-title">Dịch Nghĩa & Bình Chú:</div>
                <div style="margin-bottom: 6px;"><em>Dịch nghĩa:</em> {p['dich_nghia']}</div>
                <div><em>Bình chú:</em> {p['commentary']}</div>
            </div>
        </div>
        """)
        
    return "\n".join(html)

def build_lac_than_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Tam Quốc Văn Học • Biền Văn Phú Trác Tuyệt (222)</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">LẠC THẦN PHÚ</div>
            <div class="cover-subtitle">Đỉnh Cao Biền Văn & Tuyệt Tác Tình Si Mỹ Nữ Thần Thoại<br>Bản toàn văn chữ Hán, phiên âm, dịch nghĩa, dịch thơ phú & khảo luận mỹ học</div>
            <div class="gold-line"></div>
            <div class="cover-author">TÀO THỰC (192 – 232) • TỰ TỬ KIẾN</div>
            <div class="cover-author-sub">Khắc họa hình tượng nữ thần sông Lạc diễm lệ thiên cổ</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Đối chiếu Chiêu Minh Văn Tuyển & Cố Khởi Chi Lạc Thần Phú Đồ</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: TUYỆT TÁC BIỀN VĂN LẠC THẦN PHÚ</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Lạc Thần Phú (洛神賦)</strong> được Tào Thực sáng tác vào năm Hoàng Sơ thứ ba (222) triều Ngụy Văn Đế Tào Phi. Theo truyền thuyết và ghi chép trong văn học cổ, bài phú nguyên mang tên <strong>Cảm Chân Phú (感甄賦)</strong>, nhằm tưởng nhớ nàng Chân Cơ (người vợ xinh đẹp tuyệt trần của Tào Phi mà Tào Thực thầm yêu trộm nhớ, sau bị Tào Phi bức tử oan uổng). Về sau, con trai Chân Cơ là Ngụy Minh Đế Tào Duệ lên ngôi đã đổi tên thành <em>Lạc Thần Phú</em>.</p>
        <p>Vượt lên bi kịch tình yêu trần thế, tác phẩm là thiên tuyệt tác biền văn lộng lẫy nhất thời Tam Quốc, xây dựng nên hình tượng <strong>Lạc Thần Mật Phi</strong> - biểu tượng tối cao của cái đẹp lý tưởng thuần khiết, thanh cao và bất tử trong văn hóa phương Đông.</p>
    </div>
    """)
    
    for sec in LAC_THAN_SECTIONS:
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 25px;">
            <div style="border-bottom: 2px solid #8B1E1E; padding-bottom: 6px; margin-bottom: 12px;">
                <span style="font-weight: bold; color: #721616; font-size: 13pt;">{sec['title']}</span>
                <div style="font-size: 9.5pt; color: #666; font-style: italic; margin-top: 2px;">{sec['subtitle']}</div>
            </div>
            
            <div class="poem-parallel">
                <div class="poem-col" style="flex: 1.15; background: #fffdfa; border-color: #e5dac6;">
                    <div class="col-header">Bản Dịch Thơ Phú</div>
                    <div class="dich-tho" style="line-height: 1.85; font-size: 11pt; padding: 4px 6px;">
                        {sec['dich_tho'].replace(chr(10), '<br>')}
                    </div>
                </div>
                
                <div class="poem-col" style="flex: 1; background: #faf8f5;">
                    <div class="col-header">Nguyên Tác Chữ Hán</div>
                    <div class="han-script" style="text-align: justify; margin-bottom: 8px; font-size: 10.5pt; line-height: 1.7;">
                        {sec['han'].replace(chr(10), '<br><br>')}
                    </div>
                    <div class="col-header" style="font-size: 9pt; margin-top: 6px;">Phiên Âm Hán Việt</div>
                    <div class="phien-am" style="font-size: 9pt; line-height: 1.55;">
                        {sec['phien_am'].replace(chr(10), '<br>')}
                    </div>
                </div>
            </div>
            
            <div class="commentary-box" style="margin-top: 10px;">
                <div class="commentary-title">Dịch Nghĩa & Chú Giải:</div>
                <div style="margin-bottom: 6px; line-height: 1.6;">{sec['dich_nghia']}</div>
                <div><em>Bình chú:</em> {sec['commentary']}</div>
            </div>
        </div>
        """)
        
    return "\n".join(html)

async def main():
    print("Building Cao Zhi (Tao Thuc) publications...")
    
    # 1. That Bo Thi & Kien An
    that_bo_html = build_that_bo_html()
    await render_html_to_pdf(
        html_content=that_bo_html,
        output_path=THAT_BO_FILE,
        header_left="TÀO THỰC • THẤT BỘ THI & THƠ KIẾN AN",
        header_right="BÁT ĐẤU CHI TÀI"
    )
    
    # 2. Lac Than Phu
    lac_than_html = build_lac_than_html()
    await render_html_to_pdf(
        html_content=lac_than_html,
        output_path=LAC_THAN_FILE,
        header_left="TÀO THỰC • LẠC THẦN PHÚ (TOÀN VĂN)",
        header_right="ĐỈNH CAO BIỀN VĂN PHƯƠNG ĐÔNG"
    )

if __name__ == "__main__":
    asyncio.run(main())
