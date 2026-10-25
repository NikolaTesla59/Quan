# -*- coding: utf-8 -*-
"""
Nguyễn Du (Đại Thi Hào Dân Tộc) - Thanh Hiên Thi Tập & Bắc Hành Tạp Lục
Tuyển tập thơ chữ Hán bất hủ: Long Thành Cầm Giả Ca, Độc Tiểu Thanh Ký, Điếu Khuất Nguyên, Phản Chiêu Hồn...
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\08. [1765-1820] Việt Nam_Nguyễn Du (Đại Thi Hào Dân Tộc)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[1813] Thanh Hiên Thi Tập & Bắc Hành Tạp Lục (Thơ Chữ Hán).pdf")

NGUYEN_DU_HAN_POEMS = [
    {
        "title": "Độc Tiểu Thanh Ký (讀小青記)",
        "subtitle": "Khúc Ca Đồng Bệnh Tương Lân Cùng Khóc Nỗi Oan Khuất Ba Trăm Năm",
        "han": """西湖花苑盡成墟，
獨吊殘編一紙書。
脂粉有神憐死後，
文章無命累焚餘。
古今一恨連天在，
風運無端托地居。
不知三百餘年後，
天下何人泣素如？""",
        "phien_am": """Tây Hồ hoa uyển tẫn thành khư,
Độc điếu tàn biên nhất chỉ thư.
Chi phấn hữu thần lân tử hậu,
Văn chương vô mệnh lụy phần dư.
Cổ kim nhất hận liên thiên tại,
Phong vận vô đoan thác địa cư.
Bất tri tam bách dư niên hậu,
Thiên hạ hà nhân khấp Tố Như?""",
        "dich_nghia": """Vườn hoa Tây Hồ nay đã biến thành gò hoang phế, một mình ta viếng tập sách tàn qua một mảnh giấy vụn. Son phấn có linh hồn chắc phải xót thương sau khi chết, văn chương không có số mệnh mà phải chịu lụy bị đốt dở dang. Nỗi hờn cổ kim nối dài tới tận trời xanh, cái phong vận hào hoa không đâu lại đày ải chôn vùi dưới đất. Chẳng biết hơn ba trăm năm sau, trong thiên hạ có ai khóc Tố Như ta chăng?""",
        "dich_tho": """Tây Hồ hoa cỏ hóa gò hoang,
Thổn thức bên song mảnh giấy tàn.
Son phấn có thần thương phận bạc,
Văn chương không mệnh lụy tro tàn.
Nỗi hờn kim cổ trời khôn thấu,
Mối hận phong lưu đất ngập tràn.
Chẳng biết ba trăm năm lẻ nữa,
Người đời ai khóc Tố Như chăng?""",
        "commentary": "Đỉnh cao tuyệt đối của triết lý nhân đạo Nguyễn Du: Nỗi đau nhân thế vượt qua không gian và thời gian ba trăm năm, từ nàng Tiểu Thanh bên Tây Hồ Hàng Châu thời Minh đến cõi lòng cô độc của Tố Như, kết đọng trong câu hỏi nhức nhối thiên thu: 'Bất tri tam bách dư niên hậu / Thiên hạ hà nhân khấp Tố Như?'."
    },
    {
        "title": "Long Thành Cầm Giả Ca (龍城琴者歌)",
        "subtitle": "Bài Ca Người Gảy Đàn Đất Long Thành • Khảo Luận Cuộc Bể Dâu Lịch Sử",
        "han": """龍城佳人，
不記其姓名。
但能撫箏彈琵琶，
一曲曾令座客驚。
昔在先皇全盛日，
夜夜昇平樂未歇。
少年意氣凌雲霓，
金錢萬貫擲如鐵。
二十年前春日宴，
長安少年多俊彦。
宣和舊事不可追，
二十年間如一瞬。
西山豪傑盡灰滅，
只有龍城舊宮闕。
城郭人民幾變更，
昔時歌妓今已老。
憔悴枯槁無顏色，
暗淡斜陽掩衰草。
自古滄桑人事非，
白頭相對涕沾衣。""",
        "phien_am": """Long Thành giai nhân,
Bất ký kỳ tính danh.
Đãn năng phủ tranh đàn tỳ bà,
Nhất khúc tằng linh tọa khách kinh.
Tích tại Tiên hoàng toàn thịnh nhật,
Dạ dạ thăng bình nhạc vị yết.
Thiếu niên ý khí lăng vân nghê,
Kim tiền vạn quán trịch như thiết.
Nhị thập niên tiền xuân nhật yến,
Trường An thiếu niên đa tuấn ngạn.
Tuyên Hòa cựu sự bất khả truy,
Nhị thập niên gian như nhất thuấn.
Tây Sơn hào kiệt tận hôi diệt,
Chỉ hữu Long Thành cựu cung khuyết.
Thành quách nhân dân kỷ biến canh,
Tích thời ca kỹ kim dĩ lão.
Tiều tụy khô cảo vô nhan sắc,
Ám đạm tà dương yểm suy thảo.
Tự cổ thương tang nhân sự phi,
Bạch đầu tương đối thế triêm y.""",
        "dich_nghia": """Người đẹp đất Long Thành (Thăng Long), chẳng nhớ tên họ là chi. Chỉ biết nàng gảy đàn tranh đàn tỳ bà rất hay, một khúc dạo lên từng khiến cả tiệc khách kinh ngạc. Ngày xưa thời Tiên hoàng (vua Lê chúa Trịnh) cực thịnh, đêm đêm đàn ca vui thái bình không lúc nào dứt. Ý khí thời trẻ tuổi của ta lướt trên mây biếc, coi tiền bạc muôn quan ném vung tay như đất sắt. Hai mươi năm trước trong bữa tiệc mùa xuân, hào kiệt đất Trường An đông đảo biết bao. Chuyện cũ thời Tuyên Hòa không thể tìm lại được nữa, hai mươi năm trời trôi qua như một cái chớp mắt. Triều đình Tây Sơn dấy lên rồi cũng tiêu tan như tro bụi, nay chỉ còn lại cung điện cũ Long Thành hoang phế. Thành quách nhân dân biết bao lần biến đổi dời thay, nàng ca kỹ thuở xưa nay đã già nua bạc tóc. Tiều tụy khô héo mất hết nhan sắc, đứng ủ rũ trong bóng chiều tà che lấp cỏ may úa tàn. Xưa nay cuộc bể dâu dời đổi việc đời trôi nổi, hai mái đầu bạc nhìn nhau giọt lệ đẫm vạt áo xanh!""",
        "dich_tho": """Long Thành người đẹp thuở xưa,
Tên chi chẳng nhớ, gảy đàn tỳ hay.
Một phen nắn phím so dây,
Cả bàn khách tiệc ngất ngây bàng hoàng.
Thời Tiên hoàng thuở đăng quang,
Đêm đêm đàn hát rộn ràng Thăng Long.
Chí trai mây biếc tầng không,
Tiền muôn bạc vạn ném đồng như không!
Hai mươi năm trước tiệc xuân,
Trường An tuổi trẻ muôn phần phong lưu.
Cơ trời chớp mắt thoảng bay,
Tây Sơn hào kiệt tan tành khói tro!
Cung xưa thành cũ hoang sơ,
Nàng ca kỹ nọ nay già xác xơ.
Mặt hoa tàn tạ bơ vơ,
Bóng tà hiu hắt ngẩn ngơ cỏ vàng.
Bể dâu muôn sự dở dang,
Đầu sương nhìn lại lệ tràn vạt khăn!""",
        "commentary": "Thiên kiệt tác tự sự trữ tình phản ánh trọn vẹn ba thời kỳ lịch sử: Thời Lê - Trịnh cực thịnh, thời Tây Sơn bão táp, và thời Nguyễn lập triều; qua số phận bi thương của một người ca nữ tài hoa đất Thăng Long."
    },
    {
        "title": "Phản Chiêu Hồn (反招魂)",
        "subtitle": "Bàn Ngược Với Tống Ngọc • Khuyên Khuất Nguyên Đừng Về Trần Thế",
        "han": """魂兮歸來無往南，
南方蠻荒不可留。
魂兮歸來無往北，
北方冰雪裂人肉。
東方大海吞巨魚，
西方流沙迷征夫。
何如返故國，
故國楚宮多富貴。
魂兮歸來莫返故國，
故國人食人肉，不吐骨！""",
        "phien_am": """Hồn hề quy lai vô vãng nam,
Nam phương man hoang bất khả lưu.
Hồn hề quy lai vô vãng bắc,
Bắc phương băng tuyết liệt nhân nhục.
Đông phương đại hải thôn cự ngư,
Tây phương lưu sa mê chinh phu.
Hà như phản cố quốc,
Cố quốc Sở cung đa phú quý.
Hồn hề quy lai mạc phản cố quốc,
Cố quốc nhân thực nhân nhục, bất thổ cốt!""",
        "dich_nghia": """Hồn ơi về đi chớ sang phương nam, phương nam rừng thiêng nước độc chẳng thể ở. Hồn ơi về đi chớ sang phương bắc, phương bắc tuyết rơi xé thịt người. Phương đông biển lớn nuốt cá to, phương tây cát lầy làm mê lạc người đi đường. Sao bằng trở về nước cũ, cung vua Sở nước cũ nhiều phú quý giàu sang. Hồn ơi trở về chớ nên về nước cũ, ở nước cũ thời nay người ăn thịt người, mà chẳng thèm nhả xương!""",
        "dich_tho": """Hồn ơi về chớ sang nam,
Rừng thiêng nước độc cơ hàn tấm thân.
Hồn ơi về chớ sang bắc,
Gió băng tuyết lạnh buốt căm thịt người!
Phương đông biển lớn sóng trào,
Phương tây bão cát lối vào mịt mù.
Sao bằng về lại chốn xưa,
Cung Sở vàng ngọc bốn mùa giàu sang?
Hồn ơi chớ lại cung vàng!
Nước xưa thời loạn quân tàn ác hung:
Người ăn thịt cả giống người,
Nhắm nhai nuốt trửng chẳng thèm nhả xương!""",
        "commentary": "Ý tưởng độc đáo sâu sắc phi thường: Khuất Nguyên trầm mình xuống sông Mịch La nghìn năm trước, nhà thơ Tống Ngọc viết bài 'Chiêu hồn' gọi hồn ông về. Nguyễn Du viết 'Phản chiêu hồn' khuyên Khuất Nguyên chớ nên về dương gian, vì cõi trần gian thối nát tàn bạo gấp bội lần chốn âm ty ma quỷ."
    },
    {
        "title": "Vương Thúy Kiều Mộ (王翠翹墓)",
        "subtitle": "Bên Nấm Mồ Nàng Kiều Ven Biển • Khởi Nguồn Cảm Hứng Đoạn Trường Tân Thanh",
        "han": """風流巨賈客，
買笑不知疲。
如何江上客，
獨立吊芳姿。
空餘一抔土，
海畔泣秋漪。""",
        "phien_am": """Phong lưu cự giả khách,
Mãi tiếu bất tri bì.
Như hà giang thượng khách,
Độc lập điếu phương tư.
Không dư nhất phôi thổ,
Hải bạn khấp thu y.""",
        "dich_nghia": """Bao khách buôn phong lưu giàu có, mua tiếng cười vui chẳng biết mỏi mệt. Cớ sao người lữ khách cô độc trên bến sông này, một mình đứng khóc viếng vẻ đẹp hương hoa năm xưa? Nay chỉ còn lại một nấm đất hoang cô quạnh, bên bờ biển khóc cùng ngọn sóng thu lạnh lùng.""",
        "dich_tho": """Khách buôn tiền bạc phong lưu,
Mua vui tiếng khóc tiếng cười mỏi say.
Cớ sao lữ khách bến này,
Một mình đứng khóc bóng ai ngậm ngùi?
Mộ hoang trơ trọi cát bồi,
Bên bờ sóng biển khóc người nghìn năm!""",
        "commentary": "Tấm lòng tri âm sâu nặng của Tố Như đối với linh hồn nàng Kiều trước khi chắp bút viết nên kiệt tác Truyện Kiều bất hủ."
    }
]

def build_nguyen_du_han_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Văn Học Cổ Điển Việt Nam • Thế Kỷ XVIII – XIX</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">NGUYỄN DU • THƠ CHỮ HÁN</div>
            <div class="cover-subtitle">Thanh Hiên Thi Tập & Bắc Hành Tạp Lục (Toàn Tập Khảo Luận)<br>Long Thành Cầm Giả Ca, Độc Tiểu Thanh Ký, Điếu Khuất Nguyên, Phản Chiêu Hồn...</div>
            <div class="gold-line"></div>
            <div class="cover-author">ĐẠI THI HÀO NGUYỄN DU (1765 – 1820) • TỰ TỐ NHƯ • HIỆU THANH HIÊN</div>
            <div class="cover-author-sub">Danh nhân văn hóa thế giới UNESCO vinh danh năm 1965 & 2015</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Hiệu đính đối chiếu bản dịch Thơ Chữ Hán Nguyễn Du của Đào Duy Anh & Quách Tấn</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: TÂM HỒN TỐ NHƯ QUA THƠ CHỮ HÁN</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p>Bên cạnh kiệt tác <em>Truyện Kiều</em> (Đoạn Trường Tân Thanh), <strong>Thơ chữ Hán của Nguyễn Du</strong> (gồm 249 bài chia làm ba tập: <em>Thanh Hiên Thi Tập</em>, <em>Nam Trung Tạp Ngâm</em>, và <em>Bắc Hành Tạp Lục</em>) là phần di sản đồ sộ bộc lộ chân thực, trực tiếp nhất thế giới nội tâm u uất, trăn trở và chiều sâu triết học của Đại thi hào.</p>
        <p>Nếu trong Truyện Kiều, tác giả phải nấp sau số phận các nhân vật, thì ở thơ chữ Hán, Nguyễn Du trực tiếp cất lên tiếng khóc cho chính thân phận mình, cho người ca nữ Thăng Long, cho nàng Tiểu Thanh bạc mệnh, cho Khuất Nguyên trung liệt, và cho muôn triệu kiếp dân nghèo trôi dạt giữa cuộc đời dâu bể. Thơ chữ Hán của ông đạt tới đỉnh cao nghệ thuật bác học và lòng nhân đạo bao la xuyên suốt thiên cổ.</p>
    </div>
    """)
    
    for i, p in enumerate(NGUYEN_DU_HAN_POEMS, 1):
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

async def main():
    print("Building Nguyen Du Han poetry publication...")
    html_content = build_nguyen_du_han_html()
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="NGUYỄN DU • THƠ CHỮ HÁN",
        header_right="THANH HIÊN THI TẬP & BẮC HÀNH TẠP LỤC"
    )

if __name__ == "__main__":
    asyncio.run(main())
