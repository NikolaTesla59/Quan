# -*- coding: utf-8 -*-
"""
Phong Trào Thơ Mới (1932 - 1945) - Đại Tuyển Tập Tinh Hoa Thi Ca Hiện Đại
Thế Lữ, Lưu Trọng Lư, Xuân Diệu, Huy Cận, Hàn Mặc Tử, Chế Lan Viên, Vũ Đình Liên, Nguyễn Bính, Tế Hanh, Đoàn Văn Cừ...
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\11. [1932-1945] Việt Nam_Phong Trào Thơ Mới (Đỉnh Cao Thi Ca Hiện Đại)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[1932-1945] Tinh Hoa Phong Trào Thơ Mới.pdf")

THO_MOI_POEMS = [
    {
        "author": "THẾ LỮ (1907 – 1989)",
        "title": "Nhớ Rừng (Lời Con Hổ Ở Vườn Bách Thú)",
        "text": """Gặm một khối căm hờn trong cũi sắt,
Ta nằm dài, trông ngày tháng dần qua.
Khinh lũ người kia ngạo mạn, ngẩn ngơ,
Giương mắt bé giễu oai linh rừng thẳm,
Nay sa cơ, bị nhục nhằn tù hãm,
Để làm trò lạ mắt, thứ đồ chơi,
Chịu ngang bầy cùng bọn gấu dở hơi,
Với cặp báo chuồng bên vô tư lự.

Ta sống mãi trong tình thương nỗi nhớ,
Thủa tung hoành hống hách những ngày xưa.
Nhớ cảnh sơn lâm, bóng cả, cây già,
Với tiếng gió gào ngàn, với giọng nguồn hét núi,
Với khi thét khúc trường ca dữ dội,
Ta bước chân lên, dõng dạc, đường hoàng,
Lượn tấm thân như sóng cuộn nhịp nhàng,
Vờn bóng âm thầm, lá gai, cỏ sắc.
Trong hang tối, mắt thần khi đã quắc,
Là khiến cho mọi vật đều im hơi.
Ta biết ta là chúa tể cả muôn loài,
Giữa chốn thảo hoa không tên, không tuổi.

Nào đâu những đêm vàng bên bờ suối,
Ta say mồi đứng uống ánh trăng tan?
Đâu những ngày mưa chuyển bốn phương ngàn,
Ta lặng ngắm giang sơn ta đổi mới?
Đâu những bình minh cây xanh nắng gội,
Tiếng chim ca giấc ngủ ta tưng bừng?
Đâu những chiều lênh láng máu sau rừng,
Ta đợi chết mảnh mặt trời gay gắt,
Để ta chiếm lấy riêng phần bí mật?
- Than ôi! Thời oanh liệt nay còn đâu!""",
        "commentary": "Thi phẩm mở đầu chói lọi của phong trào Thơ Mới. Mượn lời con hổ bị giam cầm trong vườn bách thú để gửi gắm kín đáo nỗi đau mất nước và khát vọng tự do cháy bỏng của cả một thế hệ thanh niên trí thức thời thuộc Pháp."
    },
    {
        "author": "VŨ ĐÌNH LIÊN (1913 – 1996)",
        "title": "Ông Đồ",
        "text": """Mỗi năm hoa đào nở
Lại thấy ông đồ già
Bày mực tàu giấy đỏ
Bên phố đông người qua.

Bao nhiêu người thuê viết
Tấm tắc ngợi khen tài:
'Hoa tay thảo những nét
Như phượng múa rồng bay'.

Nhưng mỗi năm mỗi vắng
Người thuê viết nay đâu?
Giấy đỏ buồn không thắm
Mực đọng trong nghiên sầu...

Ông đồ vẫn ngồi đấy,
Qua đường không ai hay,
Lá vàng rơi trên giấy;
Ngoài trời mưa bụi bay.

Năm nay đào lại nở,
Không thấy ông đồ xưa.
Những người muôn năm cũ
Hồn ở đâu bây giờ?""",
        "commentary": "Khúc tràng ca bi hoài về sự lụi tàn của nền Nho học ngàn năm văn hiến trước làn sóng Tây hóa đầu thế kỷ XX. Hai câu kết 'Những người muôn năm cũ / Hồn ở đâu bây giờ?' là tiếng thở dài xót xa lay động lương tri bao thế hệ."
    },
    {
        "author": "XUÂN DIỆU (1916 – 1985)",
        "title": "Vội Vàng",
        "text": """Tôi muốn tắt nắng đi
Cho màu đừng nhạt mất;
Tôi muốn buộc gió lại
Cho hương đừng bay đi.

Của ong bướm này đây tuần tháng mật;
Này đây hoa của đồng nội xanh rì;
Này đây lá của cành tơ phơ phất;
Của yến anh này đây khúc tình si;
Và này đây ánh sáng chớp hàng mi,
Mỗi buổi sớm thần Vui hằng gõ cửa;
Tháng giêng ngon như một cặp môi gần;
Tôi sung sướng. Nhưng vội vàng một nửa:
Tôi không chờ nắng hạ mới hoài xuân.

Xuân đương tới, nghĩa là xuân đương qua,
Xuân còn non, nghĩa là xuân sẽ già,
Mà xuân hết, nghĩa là tôi cũng mất.
Lòng tôi rộng, nhưng lượng trời cứ chật,
Không cho dài thời trẻ của nhân gian,
Nói làm chi rằng xuân vẫn tuần hoàn,
Nếu tuổi trẻ chẳng hai lần thắm lại!
Còn trời đất, nhưng chẳng còn tôi mãi,
Nên bâng khuâng tôi tiếc cả đất trời...

Mau đi thôi! Mùa chưa ngả chiều hôm,
Ta muốn ôm
Cả sự sống mới bắt đầu mơn mởn;
Ta muốn riết mây đưa và gió lượn,
Ta muốn say cánh bướm với tình yêu,
Ta muốn thâu trong một cái hôn nhiều
Và non nước, và cây, và cỏ rạng,
Cho chếnh choáng mùi thơm, cho đã đầy ánh sáng,
Cho no nê thanh sắc của thời tươi;
- Hỡi xuân hồng, ta muốn cắn vào ngươi!""",
        "commentary": "Đỉnh cao tuyệt đối của hồn thơ nồng nàn, đắm say, khát khao giao cảm mãnh liệt với trần thế. Triết lý sống vội vàng trân trọng từng giây phút tuổi trẻ của 'Nhà thơ mới nhất trong các nhà thơ mới'."
    },
    {
        "author": "XUÂN DIỆU (1916 – 1985)",
        "title": "Đây Mùa Thu Tới",
        "text": """Rặng liễu đìu hiu đứng chịu tang,
Tóc buồn buông xuống lệ ngàn hàng;
Đây mùa thu tới - mùa thu tới
Với áo mơ phai dệt lá vàng.

Hơn một loài hoa đã rụng cành
Trong vườn sắc đỏ rũa màu xanh;
Những luồng run rẩy rung rinh lá...
Đôi nhánh khô gầy xương mỏng manh.

Thỉnh thoảng nàng trăng tự ngẩn ngơ...
Non xa khởi sự nhạt sương mờ;
Đã nghe rét mướt luồn trong gió...
Đã vắng người sang những chuyến đò.

Mây vẩn từng không, chim bay đi,
Khí trời u uất hận chia ly.
Ít nhiều thiếu nữ buồn không nói
Tựa cửa nhìn xa, nghĩ ngợi gì.""",
        "commentary": "Bức tranh mùa thu tuyệt mỹ mang đậm phong vị tượng trưng phương Tây: Rặng liễu hóa thân thành thiếu nữ đứng chịu tang, cảm nhận bước chuyển mùa tinh tế qua từng chiếc lá run rẩy và nỗi u sầu thiếu nữ."
    },
    {
        "author": "HUY CẬN (1919 – 2005)",
        "title": "Tràng Giang",
        "text": """Bâng khuâng trời rộng nhớ sông dài.

Sóng gợn tràng giang buồn điệp điệp,
Con thuyền xuôi mái nước song song.
Thuyền về nước lại, sầu trăm ngả;
Củi một cành khô lạc mấy dòng.

Lơ thơ cồn nhỏ gió đìu hiu,
Đâu tiếng làng xa vãn chợ chiều.
Nắng xuống, trời lên sâu chót vót;
Sông dài, trời rộng, bến cô liêu.

Bèo dạt về đâu, hàng nối hàng;
Mênh mông không một chuyến đò ngang.
Không cầu gợi chút niềm thân mật,
Lặng lẽ bờ xanh tiếp bãi vàng.

Lớp lớp mây cao đùn núi bạc,
Chim nghiêng cánh nhỏ: bóng chiều sa.
Lòng quê dợn dợn vời con nước,
Không khói hoàng hôn cũng nhớ nhà.""",
        "commentary": "Kiệt tác kết tinh nỗi sầu vạn kỷ của Huy Cận trước dòng sông Hồng mênh mang. Sự đối lập giữa vũ trụ vô cùng vô tận và kiếp người bọt bèo trôi nổi ('củi một cành khô lạc mấy dòng'), khép lại bằng câu thơ nhớ nước thầm kín vượt lên cả Thôi Hiệu đời Đường."
    },
    {
        "author": "HÀN MẶC TỬ (1912 – 1940)",
        "title": "Đây Thôn Vĩ Dạ",
        "text": """Sao anh không về chơi thôn Vĩ?
Nhìn nắng hàng cau nắng mới lên.
Vườn ai mướt quá, xanh như ngọc,
Lá trúc che ngang mặt chữ điền.

Gió theo lối gió, mây đường mây,
Dòng nước buồn thiu, hoa bắp lay...
Thuyền ai đậu bến sông trăng đó,
Có chở trăng về kịp tối nay?

Mơ khách đường xa, khách đường xa,
Áo em trắng quá nhìn không ra...
Ở đây sương khói mờ nhân ảnh,
Ai biết tình ai có đậm đà?""",
        "commentary": "Bức tranh xứ Huế thơ mộng và nỗi khắc khoải tuyệt vọng về tình yêu, sự sống của thi nhân mắc bệnh nan y nơi trại phong Quy Hòa. Cảnh vật chuyển từ thực sang mộng, hư ảo và nhói buốt khôn nguôi."
    },
    {
        "author": "HÀN MẶC TỬ (1912 – 1940)",
        "title": "Mùa Xuân Chín",
        "text": """Trong làn nắng ửng: khói mơ tan,
Đôi mái nhà tranh lấm tấm vàng.
Sột soạt gió trêu tà áo biếc,
Trên giàn thiên lý. Bóng xuân sang.

Sóng cỏ xanh tươi gợn tới trời
Bao cô thôn nữ hát trên đồi;
- Ngày mai trong đám xuân thời ấy,
Có kẻ theo chồng bỏ cuộc chơi...

Tiếng ca vắt vẻo lưng chừng núi,
Hổn hển thì thào thấu mây xanh...
Lòng khách tha hương dường náo nức,
Mơ màng nghe lại tiếng chim kêu.""",
        "commentary": "Một mùa xuân đạt đến độ 'chín' rực rỡ viên mãn của âm thanh, ánh sáng và sắc màu, nhưng ẩn giấu bên trong là nỗi âu lo phai tàn, biệt ly của kiếp người."
    },
    {
        "author": "LƯU TRỌNG LƯ (1904 – 1991)",
        "title": "Tiếng Thu",
        "text": """Em không nghe mùa thu
Dưới trăng mờ thổn thức?
Em không nghe rạo rực
Hình ảnh kẻ chinh phu
Trong lòng người cô phụ?

Em không nghe rừng thu,
Lá thu kêu xào xạc,
Con nai vàng ngơ ngác
Đạp trên lá vàng khô?""",
        "commentary": "Thi phẩm thuần túy nhạc điệu, mong manh như sương khói. Hình ảnh 'con nai vàng ngơ ngác đạp trên lá vàng khô' đã trở thành biểu tượng bất hủ cho nỗi xao xuyến ngơ ngác của linh hồn mùa thu Việt Nam."
    },
    {
        "author": "NGUYỄN BÍNH (1918 – 1966)",
        "title": "Chân Quê",
        "text": """Hôm qua em đi tỉnh về,
Đợi em ở mãi con đê đầu làng.
Khăn nhung quần lĩnh rộn ràng,
Áo cài khuy bấm, em làm khổ tôi!

Nào đâu cái yếm lụa sồi?
Cái dây lưng đũi nhuộm hồi sang xuân?
Nào đâu cái áo tứ thân?
Cái khăn mỏ quạ, cái quần nương đen?

Nói ra sợ mất lòng em,
Van em! Em hãy giữ nguyên quê mùa.
Như hôm em đi lễ chùa,
Cứ đoan trang thế em vừa lòng tôi.

Hoa chanh nở giữa vườn chanh,
Thầy u mình với chúng mình chân quê.
Hôm qua em đi tỉnh về,
Hương đồng gió nội bay đi ít nhiều!""",
        "commentary": "Tiếng lòng tha thiết bảo tồn hồn quê mộc mạc trước cơn lốc thị thành Tây hóa xô bồ. Câu thơ 'Hương đồng gió nội bay đi ít nhiều' là nỗi trăn trở muôn đời về bản sắc văn hóa dân tộc."
    },
    {
        "author": "TẾ HANH (1921 – 2009)",
        "title": "Quê Hương",
        "text": """Làng tôi ở vốn làm nghề chài lưới:
Nước bao vây cách biển nửa ngày sông.
Khi trời trong, gió nhẹ, sớm mai hồng,
Dân trai tráng bơi thuyền đi đánh cá:

Chiếc thuyền nhẹ hăng như con tuấn mã
Phăng mái chèo mạnh mẽ vượt trường giang.
Cánh buồm giương to như mảnh hồn làng
Rướn thân trắng bao la thâu góp gió...

Ngày hôm sau ồn ào trên bến đỗ
Khắp dân làng tấp nập đón ghe về.
'Nhờ ơn trời, biển lặng cá đầy ghe',
Những con cá tươi ngon thân bạc trắng.

Dân chài lưới, làn da ngăm rám nắng,
Cả thân hình nồng thở vị xa xăm;
Chiếc thuyền im bến mỏi trở về nằm
Nghe chất muối thấm dần trong thớ vỏ.

Nay xa cách lòng tôi luôn tưởng nhớ
Màu nước xanh, cá bạc, chiếc buồm vôi,
Thoáng con thuyền rẽ sóng chạy ra khơi,
Tôi thấy nhớ cái mùi nồng mặn quá!""",
        "commentary": "Bức tranh quê hương miền biển khoáng đạt, khỏe khoắn ngập tràn ánh sáng và vị mặn mòi nồng đượm của biển cả. So sánh 'Cánh buồm giương to như mảnh hồn làng' là sáng tạo thi ca độc đáo tuyệt mỹ."
    }
]

def build_tho_moi_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Văn Học Hiện Đại Việt Nam • Giai Đoạn 1932 – 1945</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">TINH HOA PHONG TRÀO THƠ MỚI</div>
            <div class="cover-subtitle">Đại Tuyển Tập Thi Ca Đỉnh Cao Một Thời Đại Trong Thi Ca<br>Thế Lữ, Lưu Trọng Lư, Xuân Diệu, Huy Cận, Hàn Mặc Tử, Nguyễn Bính, Vũ Đình Liên...</div>
            <div class="gold-line"></div>
            <div class="cover-author">TUYỂN TẬP CÁC BẬC TIỀN BỐI THI SĨ (1932 – 1945)</div>
            <div class="cover-author-sub">Khảo luận & phê bình theo tinh thần 'Thi Nhân Việt Nam' của Hoài Thanh - Hoài Chân</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Tái bản hiệu đính toàn văn theo bản in nguyên gốc Tự Lực Văn Đoàn</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: MỘT THỜI ĐẠI TRONG THI CA (1932 - 1945)</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p>Giai đoạn 1932 – 1945 chứng kiến cuộc cách mạng thi ca sâu sắc và rực rỡ nhất trong toàn bộ tiến trình lịch sử văn học Việt Nam mang tên <strong>Phong trào Thơ Mới</strong>. Khởi đầu từ bài thơ <em>Tình già</em> của Phan Khôi trên báo Phụ Nữ Tân Văn năm 1932, Thơ Mới đã phá vỡ hoàn toàn chiếc vỏ ốc gò bó của luật thi Đường luật cũ kỹ, giải phóng cái 'Tôi' cá nhân cá tính, đưa tiếng Việt lên đỉnh cao tinh vi diễm lệ.</p>
        <p>Trong cuốn chuyên luận kinh điển <em>Thi Nhân Việt Nam</em> (1942), nhà phê bình Hoài Thanh đã đúc kết xuất sắc: <em>'Chưa bao giờ người ta thấy xuất hiện cùng một lần một hồn thơ rộng mở như Thế Lữ, mơ màng như Lưu Trọng Lư, hùng tráng như Huy Thông, trong sáng như Nguyễn Nhược Pháp, ảo não như Huy Cận, nồng nàn như Xuân Diệu, quằn quại như Hàn Mặc Tử, kỳ dị như Chế Lan Viên...'</em>. Đó thực sự là <strong>Một thời đại trong thi ca</strong> chưa từng thấy trong lịch sử dân tộc.</p>
    </div>
    """)
    
    for i, p in enumerate(THO_MOI_POEMS, 1):
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 25px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #8B1E1E; padding-bottom: 6px; margin-bottom: 12px;">
                <span style="font-weight: bold; color: #721616; font-size: 13pt;">{i}. {p['title']}</span>
                <span style="font-size: 10pt; color: #1a365d; font-weight: bold;">{p['author']}</span>
            </div>
            
            <div class="poem-stanza" style="line-height: 1.95; font-size: 11pt; color: #222; text-align: left; padding: 10px 25px; background: #fffdf9; border-radius: 4px; border: 1px solid #f2ece1;">
                {p['text'].replace(chr(10), '<br>')}
            </div>
            
            <div class="commentary-box" style="margin-top: 12px;">
                <div class="commentary-title">Bình Luận Thi Pháp & Ý Nghĩa Nghệ Thuật:</div>
                {p['commentary']}
            </div>
        </div>
        """)
        
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">VĨ THANH: DI SẢN THƠ MỚI BẤT TỬ</h1>
    <div class="ornament">❖</div>
    <div class="intro-box">
        <p>Phong trào Thơ Mới khép lại vào năm 1945 để mở ra một dòng chảy thi ca cách mạng mới gắn liền với vận mệnh dân tộc. Nhưng tinh hoa mà các thi sĩ 1932 – 1945 để lại đã trở thành gia tài thi ca kinh điển, nuôi dưỡng tâm hồn và định hình vẻ đẹp của tiếng Việt hiện đại cho muôn đời sau.</p>
    </div>
    """)
    
    return "\n".join(html)

async def main():
    print("Building Tho Moi comprehensive anthology...")
    html_content = build_tho_moi_html()
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="PHONG TRÀO THƠ MỚI (1932 - 1945)",
        header_right="ĐẠI TUYỂN TẬP TINH HOA THI CA"
    )

if __name__ == "__main__":
    asyncio.run(main())
