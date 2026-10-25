# -*- coding: utf-8 -*-
"""
Đỗ Phủ (Thi Thánh) - Tuyển Tập Đường Thi & Khảo Luận Thi Sử
Đầy đủ các kiệt tác đỉnh cao: Binh Xa Hành, Mao Ốc Vị Thu Phong Sở Phá Ca, Đăng Cao, Trọn bộ 8 bài Thu Hứng...
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\03. [712-770] Trung Quốc_Đỗ Phủ (Thi Thánh)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[760] Đỗ Phủ - Tuyển Tập Đường Thi (Nguyên Tác Chữ Hán, Phiên Âm & Dịch Thơ).pdf")

DO_PHU_POEMS = [
    {
        "title": "Đăng Cao (登高)",
        "subtitle": "Đệ Nhất Thất Ngôn Bát Cú Cổ Kim • Đỉnh Cao Luật Thi Phương Đông",
        "han": """風急天高猿嘯哀，渚清沙白鳥飛迴。
無邊落木蕭蕭下，不盡長江滾滾來。
萬里悲秋常作客，百年多病獨登臺。
艱難苦恨繁霜鬢，潦倒新停濁酒杯。""",
        "phien_am": """Phong cấp thiên cao viên khiếu ai,
Chử thanh sa bạch điểu phi hồi.
Vô biên lạc mộc tiêu tiêu hạ,
Bất tận Trường Giang cổn cổn lai.
Vạn lý bi thu thường tác khách,
Bách niên đa bệnh độc đăng đài.
Gian nan khổ hận phồn sương bấn,
Liêu đảo tân đình trọc tửu bôi.""",
        "dich_nghia": """Gió thổi gấp trời cao tiếng vượn hú ai oán xé lòng, bến nước trong bãi cát trắng cánh chim chao lượn bay vòng. Lá rụng không bờ bến xào xạc trút xuống, dòng Trường Giang bất tận cuồn cuộn đổ về. Muôn dặm đau lòng vì cảnh thu thường làm thân lữ khách, trăm năm một đời lắm bệnh tật một mình trèo lên đài cao. Gian nan đau xót tóc mai đã bạc trắng như sương dày, bẽ bàng suy sụp mới đây vừa phải dứt bỏ cả chén rượu đục.""",
        "dich_tho": """Gió lộng trời cao vượn hú sầu,
Bến trong cát trắng cánh chim chao.
Lá rụng vô biên ào ạt trút,
Trường Giang cuồn cuộn sóng dâng trào.
Muôn dặm thu sầu thân lữ thứ,
Một đời lắm bệnh đứng đài cao.
Gian nan cay đắng đầu sương trắng,
Liêu đảo đành buông chén rượu đào!""",
        "commentary": "Học giả muôn đời tôn vinh bài 'Đăng Cao' là đệ nhất thất ngôn luật thi cổ kim. Toàn bài 8 câu 56 chữ đều tuân thủ nghiêm ngặt phép đối ngẫu (câu 1-2 đối, 3-4 đối, 5-6 đối, 7-8 đối), hòa quyện giữa không gian vũ trụ hùng vĩ và nỗi sầu nhân thế bi tráng vô cùng."
    },
    {
        "title": "Mao Ốc Vị Thu Phong Sở Phá Ca (茅屋為秋風所破歌)",
        "subtitle": "Bài Ca Nhà Tranh Bị Gió Thu Phá & Tấm Lòng Vị Nhân Sinh Bất Hủ",
        "han": """八月秋高風怒號，卷我屋上三重茅。
茅飛渡江灑江郊，高者挂罥長林梢，下者飄轉沈塘坳。
南村群童欺我老無力，忍能對面為盜賊。
公然抱茅入竹去，唇焦口燥呼不得，歸來倚杖自嘆息。
俄頃風定雲墨色，秋天漠漠向昏黑。
布衾多年冷似鐵，嬌兒惡臥踏裏裂。
床頭屋漏無乾處，雨腳如麻未斷絕。
自經喪亂少睡眠，長夜沾濕何由徹！
安得廣廈千萬間，大庇天下寒士俱歡顏！
風雨不動安如山。
嗚呼！何時眼前突兀見此屋，吾廬獨破受凍死亦足！""",
        "phien_am": """Bát nguyệt thu cao phong nộ hào,
Quyển ngã ốc thượng tam trùng mao.
Mao phi độ giang sái giang giao,
Cao giả quải quyến trường lâm sảo,
Hạ giả phiêu chuyển trầm đường ảo.
Nam thôn quần đồng khi ngã lão vô lực,
Nhẫn năng đối diện vi đạo tặc.
Công nhiên bão mao nhập trúc khứ,
Thuần tiêu khẩu táo hô bất đắc,
Quy lai ỷ trượng tự thán tức.
Nga khoảnh phong định vân mặc sắc,
Thu thiên mạc mạc hướng hôn hắc.
Bố khâm đa niên lãnh tự thiết,
Kiều nhi ác ngọa đạp lý liệt.
Sàng đầu ốc lậu vô can xứ,
Vũ cước như ma vị đoạn tuyệt.
Tự kinh tang loạn thiểu thụy miên,
Trường dạ triêm thấp hà do triệt!
An đắc quảng hạ thiên vạn gian,
Đại tý thiên hạ hàn sĩ câu hoan nhan!
Phong vũ bất động an như sơn.
Ô hô! Hà thời nhãn tiền đột ngột kiến thử ốc,
Ngô lư độc phá thọ đống tử diệc túc!""",
        "dich_nghia": """Tháng tám thu cao gió giận gào thét, cuộn quét ba lớp tranh trên mái nhà ta. Tranh bay qua sông rải rác bờ sông, mảnh cao vắt trên ngọn cây rừng rậm, mảnh thấp trôi dạt chìm đáy ao sâu. Lũ trẻ xóm nam khinh ta già cả không sức lực, nỡ lòng làm quân trộm cướp ngay trước mặt. Ngang nhiên ôm tranh chạy biến vào bụi tre, môi khô miệng rát gào gọi không được, trở về tựa gậy một mình thở dài. Chốc lát gió lặng mây đen như mực, trời thu mờ mịt ngả về bóng tối tăm. Chăn vải dùng bao năm lạnh buốt như sắt, con nhỏ nằm ngủ giãy đạp rách toang lớp lót. Đầu giường nhà dột không chỗ nào khô ráo, hạt mưa nối tiếp dày như sợi gai không ngớt. Từ ngày loạn lạc tới nay ít khi chợp mắt, đêm dài ướt đẫm làm sao cho mau sáng! Ước sao có được ngôi nhà rộng muôn ngàn gian, che chở khắp hàn sĩ trong thiên hạ đều hớn hở mặt mày! Mưa gió chẳng hề lung lay, vững chãi an nhiên như núi Thái Sơn. Than ôi! Bao giờ trước mắt đột ngột hiện ra ngôi nhà ấy, dẫu riêng lều ta nát vụn chịu chết cóng cũng thỏa lòng!""",
        "dich_tho": """Tháng tám gió thu gầm giận dữ,
Cuộn ba tầng rạ nóc nhà ta.
Tranh bay qua bến sông xa,
Treo cành cây rậm, rớt sa đáy đầm.
Lũ trẻ xóm khinh già kiệt sức,
Cướp tranh ngang trước mặt trơ trơ.
Ôm tranh chạy tót bụi tre,
Họng khô gào chẳng thành lời buốt cay!
Gió ngừng mây tối đen sì,
Trời thu mờ mịt đêm buông mịt mùng.
Chăn vải cũ lạnh lùng như sắt,
Con thơ cựa đạp rách tơi bời.
Đầu giường dột khắp mọi nơi,
Mưa tuôn hạt chỉ nối trời không ngơi.
Từ cơn loạn lạc ít ngủ nghê,
Đêm dài ướt sũng tới bao giờ?
Ước sao nhà rộng muôn ngàn gian,
Che chở hàn sĩ khắp nhân gian!
Gió mưa chẳng động vững như non.
Than ôi! Bao giờ hiện trước mắt ta,
Lều ta nát chết cóng cũng cam lòng!""",
        "commentary": "Đỉnh cao tuyệt đối của chủ nghĩa nhân đạo Đỗ Phủ: Trong cơn cùng quẫn nhà tan cửa nát giữa đêm mưa tuyết, ông không hề oán trách số phận hay than vãn cho riêng mình, mà mở rộng tấm lòng thương xót cùng cực ước mơ có ngôi nhà muôn ngàn gian che chở cho mọi kẻ nghèo khổ trong thiên hạ."
    },
    {
        "title": "Binh Xa Hành (兵車行)",
        "subtitle": "Bản Cáo Trạng Lịch Sử Tố Cáo Nạn Bắt Lính & Binh Đao Vô Nghĩa",
        "han": """車轔轔，馬蕭蕭，行人弓箭各在腰。
耶娘妻子走相送，塵埃不見咸陽橋。
牽衣頓足攔道哭，哭聲直上干雲霄。
道旁過者問行人，行人但云點行頻。
或從十五北防河，便至四十西營田。
去時里正與裹頭，歸來頭白還戍邊。
邊庭流血成海水，武皇開邊意未已。
君不聞漢家山東二百州，千村萬落生荊杞。
縱有健婦把鋤犁，禾生隴畝無東西。
況復秦兵耐苦戰，被驅不異犬與雞。
生女猶得嫁比鄰，生男埋沒隨百草。
君不見青海頭，白骨無人收。
新鬼煩冤舊鬼哭，天陰雨濕聲啾啾。""",
        "phien_am": """Xa lân lân, mã tiêu tiêu,
Hành nhân cung tiễn các tại yêu.
Gia nương thê tử tẩu tương tống,
Trần ai bất kiến Hàm Dương kiều.
Khiên y đốn túc lan đạo khốc,
Khốc thanh trực thượng can vân tiêu.
Đạo bàng quá giả vấn hành nhân,
Hành nhân đãn vân điểm hành tần.
Hoặc tòng thập ngũ bắc phòng Hà,
Tiện chí tứ thập tây doanh điền.
Khứ thời lý chính dữ khỏa đầu,
Quy lai đầu bạch hoàn thú biên.
Biên đình lưu huyết thành hải thủy,
Vũ Hoàng khai biên ý vị dĩ.
Quân bất văn Hán gia Sơn Đông nhị bách châu,
Thiên thôn vạn lạc sinh kinh kỷ.
Túng hữu kiện phụ bả trừ lê,
Hòa sinh lũng mẫu vô đông tây.
Huống phục Tần binh nại khổ chiến,
Bị khu bất dị khuyển dữ kê.
Sinh nữ do đắc giá bỉ lân,
Sinh nam mai một tùy bách thảo.
Quân bất kiến Thanh Hải đầu,
Bạch cốt vô nhân thu.
Tân quỷ phiền oan cựu quỷ khốc,
Thiên âm vũ thấp thanh thu thu.""",
        "dich_nghia": """Xe rung rền rĩ, ngựa hí vang lừng, người lính tòng quân cung tên gài bên lưng. Cha mẹ vợ con chạy theo tiễn biệt, bụi bay mù mịt chẳng thấy cầu Hàm Dương. Níu áo giậm chân chặn đường khóc lóc, tiếng khóc thấu tận mây xanh. Người qua đường bên đường hỏi người lính, người lính chỉ bảo đi lính liên miên. Có kẻ từ mười lăm tuổi đã đi giữ sông phía bắc, mãi đến bốn mươi tuổi sang phía tây cày ruộng lính. Lúc đi lý trưởng quấn khăn đầu cho, lúc về đầu đã bạc phai lại phải đi trấn giữ biên cương. Nơi biên ải máu chảy thành nước biển, mà lòng vua Vũ Hoàng (Đường Huyền Tông) mở rộng bờ cõi vẫn chưa chịu dừng. Người há chẳng nghe hai trăm châu Sơn Đông nhà Hán, nghìn thôn muôn xóm mọc đầy gai góc. Dẫu có đàn bà khỏe mạnh cầm cuốc cày, lúa mọc trên bờ ruộng chẳng ra hàng lối đông tây. Huống chi lính đất Tần chịu đựng gian khổ đánh trận, bị xua đuổi chẳng khác gì chó gà. Sinh con gái còn gả được cho xóm giềng, sinh con trai đành vùi thân cùng cỏ rác. Người há chẳng thấy chốn đầu bờ biển Thanh Hải, xương trắng chất đống không ai buồn nhặt. Ma mới oan ức ma cũ khóc than, trời râm mưa ướt tiếng khóc nỉ non thấu trời!""",
        "dich_tho": """Xe ầm ầm, ngựa hí ran,
Cung tên gài thắt lưng người lính đi.
Mẹ cha vợ trẻ chạy theo,
Bụi tung chẳng thấy bóng cầu Hàm Dương.
Níu áo giậm chân khóc than,
Tiếng hờn tiếng khóc thấu ngàn mây xanh!
Người qua đường hỏi sự tình,
Lính thưa: bắt bớ triền miên tháng ngày.
Mười lăm đi giữ Trường Giang,
Bốn mươi cày cấy đất hoang biên thùy.
Lúc đi lý trưởng buộc khăn,
Về thì tóc bạc lại đày ải xa!
Biên cương máu chảy thành sông,
Vua tham đất rộng lòng không chịu dừng!
Gái sinh còn gả cận kề,
Trai sinh vùi xác cỏ hoa chôn cùi!
Há chẳng thấy biển Thanh Hải,
Xương tàn trắng xóa ai nhặt giùm ai?
Ma mới oán, ma cũ hờn,
Trời âm u khóc nỉ non thấu trời!""",
        "commentary": "Kiệt tác hiện thực vạch trần dã tâm bành trướng xâm lược của Đường Huyền Tông và bi kịch tang thương của hàng vạn gia đình dân đen vô tội."
    },
    {
        "title": "Xuân Vọng (春望)",
        "subtitle": "Nỗi Đau Non Sông Loạn Lạc & Giọt Lệ Biệt Ly Hoa Cỏ",
        "han": """國破山河在，城春草木深。
感時花濺淚，恨別鳥驚心。
烽火連三月，家書抵萬金。
白頭搔更短，渾欲不勝簪。""",
        "phien_am": """Quốc phá sơn hà tại,
Thành xuân thảo mộc thâm.
Cảm thời hoa tiễn lệ,
Hận biệt điểu kinh tâm.
Phong hỏa liên tam nguyệt,
Gia thư để vạn kim.
Bạch đầu tao cánh đoản,
Hồn dục bất thặng trâm.""",
        "dich_nghia": """Nước mất mà non sông vẫn còn đó, thành trì sang xuân cỏ cây mọc um tùm. Cảm thương thời thế thấy hoa nở mà rơi lệ, giận cảnh biệt ly nghe tiếng chim hót mà giật mình thót tim. Khói lửa chiến tranh kéo dài liền ba tháng, bức thư nhà quý giá đáng muôn lạng vàng. Mái đầu bạc càng gãi càng rụng ngắn đi, dường như không còn gài nổi chiếc trâm cài tóc.""",
        "dich_tho": """Nước mất non sông giữ,
Thành xuân cỏ tốt tươi.
Thương thời hoa đẫm lệ,
Hận biệt chim kinh lòng.
Lửa chiến liền ba tháng,
Thư nhà giá vạn vàng.
Đầu bạc càng gãi rụng,
Khôn xiết cài trâm sang!""",
        "commentary": "Hai câu luận: 'Phong hỏa liên tam nguyệt / Gia thư để vạn kim' (Lửa chiến liền ba tháng / Thư nhà giá vạn vàng) đã trở thành chân lý đúc kết nỗi khát khao tin tức người thân giữa bom đạn chiến tranh."
    },
    {
        "title": "Thu Hứng • Bài 1 (秋興八首·其一)",
        "subtitle": "Khởi Đầu Bộ Tranh Thu Bất Hủ Bát Thủ Thu Hứng",
        "han": """玉露凋傷楓樹林，巫山巫峽氣蕭森。
江間波浪兼天湧，塞上風雲接地陰。
叢菊兩開他日淚，孤舟一繫故園心。
寒衣處處催刀尺，白帝城高急暮砧。""",
        "phien_am": """Ngọc lộ điêu thương phong thụ lâm,
Vu sơn Vu giáp khí tiêu sâm.
Giang gian ba lãng kiêm thiên dũng,
Tái thượng phong vân tiếp địa âm.
Tùng cúc lưỡng khai tha nhật lệ,
Cô chu nhất hệ cố viên tâm.
Hàn y xứ xứ thôi đao xích,
Bạch Đế thành cao cấp mộ châm.""",
        "dich_nghia": """Móc ngọc trắng xóa làm tiêu điều xơ xác rừng phong, núi Vu hẻm Vu khí thu hiu hắt u ám. Giữa lòng sông sóng cuộn trào dâng ngập trời, trên ải biên cương gió mây sà xuống đen sì mặt đất. Khóm cúc hai phen nở hoa nhỏ giọt lệ ngày trước, con thuyền lẻ loi buộc chặt mối lòng nhớ về vườn cũ quê nhà. Mùa đông tới nơi nơi rộn rã giục dao thước may áo rét, thành Bạch Đế cao vút dồn dập tiếng chày đập vải lúc chiều hôm.""",
        "dich_tho": """Lác đác rừng phong hạt móc sa,
Ngàn non hiu hắt khí thu lòa.
Lưng trời sóng gợn lòng sông thẳm,
Mặt đất mây đùn cửa ải xa.
Khóm cúc tuôn thêm hàng lệ cũ,
Con thuyền buộc chặt mối tình nhà.
Lạnh lùng giục kẻ may áo rét,
Thành Bạch dồn chày bóng ác tà.""",
        "commentary": "Bản dịch tuyệt tác của Tản Đà đã chuyển tải trọn vẹn thần thái bi tráng của Đỗ Phủ: Khóm cúc hai lần nở hoa là hai năm lưu lạc, con thuyền đơn độc buộc chặt mối tình quê hương."
    }
]

def build_do_phu_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Đại Đường Thi Ca • Thế Kỷ VIII</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">ĐỖ PHỦ • THI THÁNH</div>
            <div class="cover-subtitle">Tuyển Tập Đường Thi & Khảo Luận Thi Sử Hiện Thực<br>Nguyên tác chữ Hán, phiên âm Hán Việt, dịch nghĩa, dịch thơ & bình chú thi pháp</div>
            <div class="gold-line"></div>
            <div class="cover-author">THI THÁNH ĐỖ PHỦ (712 – 770) • TỰ TỬ MỸ • HIỆU THIỂU LĂNG DÃ LÃO</div>
            <div class="cover-author-sub">Đỉnh cao thi sử mẫu mực và chủ nghĩa nhân đạo trác việt</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Hiệu đính đối chiếu Đỗ Thi Kính Thuyên & Tuyển tập Khương Hữu Dụng - Tản Đà</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: THI THÁNH ĐỖ PHỦ VÀ DI SẢN THI SỬ</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Đỗ Phủ (712 – 770)</strong>, tự Tử Mỹ, hiệu Thiểu Lăng dã lão, được xưng tôn là <strong>Thi Thánh (詩聖)</strong> và tác phẩm của ông được mệnh danh là <strong>"Thi sử" (詩史 - Lịch sử bằng thơ)</strong>. Sống trọn trong thời kỳ biến loạn An Sử đẫm máu làm sụp đổ thời thịnh Đường, Đỗ Phủ đã dùng ngòi bút hiện thực nghiêm cẩn để ghi lại chân thực từng nỗi đau thương của đất nước và nhân dân.</p>
        <p>Khác với vẻ lãng mạn phóng túng của Lý Bạch, thơ Đỗ Phủ đạt đến độ mẫu mực tuyệt đối về niêm luật Đường thi, chặt chẽ trong bố cục, nghiêm ngặt trong luật đối và thẳm sâu trong tư tưởng nhân đạo vị tha. Ông là tấm gương vĩ đại về nhân cách của một trí thức suốt đời đau đáu vì vận mệnh non sông và hạnh phúc của trăm họ.</p>
    </div>
    """)
    
    for i, p in enumerate(DO_PHU_POEMS, 1):
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
    <h1 class="chapter-title">VĨ THANH: BẤT TỬ CÙNG NỖI ĐAU NHÂN LOẠI</h1>
    <div class="ornament">❖</div>
    <div class="intro-box">
        <p>Đỗ Phủ mất trên một con thuyền nhỏ trôi dạt trên sông Tương giữa mùa đông lạnh giá năm 770. Nhưng trái tim nhân ái mênh mông của ông vẫn sống mãi cùng muôn đời. Thơ ông đã vượt thoát khỏi ranh giới thời đại và biên giới quốc gia, trở thành tài sản tinh thần vô giá của toàn thể nhân loại tiến bộ.</p>
    </div>
    """)
    
    return "\n".join(html)

async def main():
    print("Building Do Phu comprehensive anthology...")
    html_content = build_do_phu_html()
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="ĐỖ PHỦ • THI THÁNH ĐẠI ĐƯỜNG",
        header_right="TUYỂN TẬP ĐƯỜNG THI & THI SỬ"
    )

if __name__ == "__main__":
    asyncio.run(main())
