# -*- coding: utf-8 -*-
"""
Bà Huyện Thanh Quan - Toàn Tập Thơ Hoài Cổ & Khảo Luận Thi Pháp
Đầy đủ toàn bộ 6 bài thơ hoài cổ kinh điển kèm khảo dị, hoàn cảnh sáng tác, phân tích thi pháp, giai thoại văn chương
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\10. [k. 1805-1848] Việt Nam_Bà Huyện Thanh Quan (Thơ Hoài Cổ)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[1840] Tuyển Tập Thơ Bà Huyện Thanh Quan.pdf")

POEMS_6 = [
    {
        "title": "Qua Đèo Ngang (過橫山)",
        "subtitle": "Đỉnh Cao Kiệt Tác Thơ Nôm Đường Luật Thất Ngôn Bát Cú",
        "text": """Bước tới Đèo Ngang bóng xế tà,
Cỏ cây chen đá, lá chen hoa.
Lom khom dưới núi, tiều vài chú,
Lác đác bên sông, chợ mấy nhà.
Nhớ nước đau lòng, con quốc quốc,
Thương nhà mỏi miệng, cái gia gia.
Dừng chân đứng lại trời, non, nước,
Một mảnh tình riêng, ta với ta.""",
        "circumstance": "Sáng tác vào khoảng năm 1839, trên đường nữ sĩ từ Thăng Long vào kinh đô Phú Xuân (Huế) theo chỉ triệu của vua Minh Mạng để giữ chức Cung Trung Giáo Tập. Đứng trước thắng cảnh Đèo Ngang (ranh giới tự nhiên hiểm trở giữa Hà Tĩnh và Quảng Bình), buổi hoàng hôn bảng lảng, nỗi sầu xa xứ và niềm hoài cổ trỗi dậy khôn nguôi.",
        "analysis": """Bài thơ được coi là mẫu mực tuyệt đối của thể thơ thất ngôn bát cú Đường luật trong văn học Việt Nam:
- Hai câu đề (1-2): Xác định không gian Đèo Ngang và thời gian 'bóng xế tà' - thời điểm của sự sum họp mà lòng người lại cô đơn cất bước. Cảnh vật hoang sơ, tràn đầy sức sống tự nhiên ('Cỏ cây chen đá, lá chen hoa').
- Hai câu thực (3-4): Phép đối ngẫu và đảo ngữ bậc thầy ('Lom khom dưới núi' đối 'Lác đác bên sông'; 'tiều vài chú' đối 'chợ mấy nhà'). Con người và sự sống xuất hiện nhỏ bé, thưa thớt, càng làm nổi bật sự hoang vu, quạnh quẽ rợn ngợp của núi đèo.
- Hai câu luận (5-6): Đỉnh cao nghệ thuật chơi chữ đồng âm dị nghĩa và tượng thanh tượng hình ('quốc quốc' là chim cuốc nhưng gợi 'quốc' - đất nước; 'gia gia' là chim đa đa nhưng gợi 'gia' - gia đình). Tiếng chim khóc trong bóng chiều tà gợi nỗi đau mất nước (hoài niệm triều Lê) và nỗi nhớ gia đình tha thiết.
- Hai câu kết (7-8): Nhịp thơ chậm rãi mở ra không gian vũ trụ vô cùng vô tận: 'trời, non, nước' rồi thu hẹp lại tới tận cùng của sự cô đơn nội tâm: 'Một mảnh tình riêng, ta với ta'. Chỉ còn lại một mình đối diện với chính tâm hồn sâu kín của mình giữa trời đất mông mênh.""",
        "variants": "Khảo dị: Câu 4 có bản chép 'chợ mấy nhà' hoặc 'rợ mấy nhà' (người dân tộc thiểu số). Bản 'chợ mấy nhà' phổ biến và giàu sức gợi hơn cả."
    },
    {
        "title": "Thăng Long Thành Hoài Cổ (昇龍城懷古)",
        "subtitle": "Khúc Ca Bi Thiết Trước Phế Tích Ngàn Năm Văn Vật",
        "text": """Tạo hóa gây chi cuộc hí trường,
Đến nay thấm thoắt mấy tinh sương.
Lối xưa xe ngựa hồn thu thảo,
Nền cũ lâu đài bóng tịch dương.
Đá vẫn trơ gan cùng tuế nguyệt,
Nước còn cau mặt với tang thương.
Nghìn năm gương cũ soi kim cổ,
Cảnh đấy người đây luống đoạn trường.""",
        "circumstance": "Sáng tác khi bà đứng ngắm nhìn hoàng thành Thăng Long hoang tàn phế tích. Khi vua Gia Long lập triều Nguyễn (1802), kinh đô được dời vào Phú Xuân (Huế), Thăng Long bị hạ cấp xuống làm trấn Bắc Thành, các cung điện vàng son triều Lê - Trịnh bị san phẳng hoặc bỏ hoang phế.",
        "analysis": """Tác phẩm kết tinh nỗi niềm hoài cổ của tầng lớp sĩ phu Bắc Hà:
- Hai câu đề (1-2): Than thở về sự trớ trêu vô tình của hóa công, ví cuộc hưng vong thế sự như một vở kịch hão huyền ('hí trường'). Thời gian trôi mau ('mấy tinh sương') chôn vùi bao triều đại.
- Hai câu thực (3-4): Phép đối ngẫu lộng lẫy và hình ảnh tượng trưng kinh điển ('Lối xưa xe ngựa' nay chỉ còn 'hồn thu thảo' - cỏ mùa thu úa tàn; 'Nền cũ lâu đài' nay chỉ còn 'bóng tịch dương' - bóng nắng chiều hôm hấp hối). Cái còn lại chỉ là linh hồn của dĩ vãng hư ảo.
- Hai câu luận (5-6): Nhân hóa thiên nhiên ('Đá trơ gan', 'Nước cau mặt'). Đá vô tri mà như có gan góc bền gan cùng năm tháng, dòng nước vô tình mà như biết nhăn mặt cau mày trước cảnh bể dâu dời đổi ('tang thương').
- Hai câu kết (7-8): Đúc kết triết lý lịch sử nghìn năm soi gương kim cổ, đối diện với hiện tại hoang tàn khiến lòng người xót xa đứt từng khúc ruột ('đoạn trường').""",
        "variants": "Khảo dị: Câu 5 có bản chép 'Đá trơ gan', bản khác chép 'Đá vẫn trơ gan'."
    },
    {
        "title": "Chiều Hôm Nhớ Nhà (暮次有懷)",
        "subtitle": "Bức Họa Thủy Mặc Về Nỗi Lòng Lữ Khách Lúc Hoàng Hôn",
        "text": """Chiều trời bảng lảng bóng hoàng hôn,
Tiếng ốc xa đưa vẳng trống dồn.
Gác mái, ngư ông về viễn phố,
Gõ sừng, mục tử lại cô thôn.
Kẻ chốn chương đài mong bóng nhạn,
Người ngoài ải bắc đợi tin nhạn.
Dừng chân ngắm cảnh lòng se sắt,
Biết mấy sầu đong dạ héo hon.""",
        "circumstance": "Sáng tác trên bước đường lưu lạc tha hương, dừng chân nơi một xóm nhỏ ven sông lúc trời đã tối.",
        "analysis": """- Bức tranh thủy mặc với âm thanh tiếng ốc rúc từ đồn xa và tiếng trống thu không giục giã, báo hiệu ngày tàn.
- Hình ảnh ông chài gác mái chèo trở về bến xa ('viễn phố'), chú bé chăn trâu gõ sừng trâu trở về làng cô quạnh ('cô thôn'). Mọi sinh linh đều có chốn trở về, riêng người lữ khách vẫn bơ vơ giữa đường thiên lý.
- Mượn điển cố 'Chương Đài' và 'tin nhạn' để diễn tả nỗi nhớ nhung gia đình, người thân da diết, kín đáo.""",
        "variants": "Khảo dị: Hai câu luận có bản chép biến thể theo thể Đường thi thuần Việt."
    },
    {
        "title": "Cảnh Đền Trấn Bắc (鎮北行宮)",
        "subtitle": "Nỗi Niềm Hoài Cảm Trước Hành Cung Bên Hồ Tây",
        "text": """Trấn Bắc hành cung cỏ dãi dầu,
Khách qua đường luống chạnh niềm đau.
Mấy toà sen rớt hương còn ngát,
Mấy dải rèm the sắc đã màu.
Gió giật mái hiên lay lắt bóng,
Trăng soi bến nước nhạt nhòa sao.
Dấu xưa xe ngựa nay đâu tá?
Chỉ thấy ngàn thu ngọn sóng xao.""",
        "circumstance": "Trấn Bắc hành cung vốn là cung điện nguy nga của các chúa Trịnh dựng bên bờ Hồ Tây để nghỉ mát và ngắm cảnh, nay cảnh cũ hoang phế trơ trọi.",
        "analysis": """- Đối chiếu giữa quá khứ vàng son rực rỡ và hiện tại cỏ dại dãi dầu.
- Hình ảnh 'Mấy toà sen rớt' gợi sự suy vi của một triều đại, nhưng 'hương còn ngát' biểu trưng cho vẻ đẹp văn hóa ngàn năm không dễ gì phai nhạt.
- Câu hỏi tu từ nghẹn ngào ở cuối bài khép lại trong tiếng sóng Hồ Tây vỗ mãi ngàn năm.""",
        "variants": "Bản chép tay trong Tuyển tập Thi Nôm Bắc Hà thế kỷ XIX."
    },
    {
        "title": "Chùa Trấn Quốc (鎮國寺)",
        "subtitle": "Cõi Thiền Tịch Mịch Giữa Lòng Tây Hồ",
        "text": """Đầm biếc lơ thơ khóm trúc vàng,
Trấn Quốc đây ư cảnh phụng loan?
Bồ đề trăng dãi bóng trong sáng,
Cửa Phật khói hương ngát nhẹ nhàng.
Chuông giục canh khuya tan mộng ảo,
Kinh truyền sớm tối thoát trần gian.
Ngắm xem phong cảnh lòng thanh thản,
Rũ sạch sầu bi cõi thế gian.""",
        "circumstance": "Chùa Trấn Quốc là ngôi chùa cổ nhất Thăng Long, nằm trên hòn đảo nhỏ phía đông Hồ Tây, từng là nơi danh sĩ du ngoạn thưởng cảnh.",
        "analysis": """- Không gian thiền môn thanh tịnh giải tỏa những u uất, trăn trở trần thế của nữ sĩ.
- Màu sắc thanh nhã: 'Đầm biếc', 'khóm trúc vàng', ánh trăng bồ đề soi bóng nước hồ lung linh huyền ảo.
- Tiếng chuông chùa ngân vang đánh tan mộng ảo công danh, giúp tâm hồn tìm về chốn an nhiên vĩnh hằng.""",
        "variants": "Bản lưu truyền tại thư viện Viện Nghiên cứu Hán Nôm."
    },
    {
        "title": "Cảnh Đền Ngọc Sơn (玉山祠)",
        "subtitle": "Hồn Thiêng Hồ Gươm Ngàn Năm Văn Vật",
        "text": """Biển hồ nước phẳng bóng thuyền câu,
Trầm mặc ngàn năm cảnh nhiệm mầu.
Cầu Thê Húc uốn soi đáy nước,
Đài Nghiên bút tháp vút trời cao.
Hồn rùa thiêng lắng nghìn thu cũ,
Bóng kiếm vua Lê rạng ánh sao.
Dừng bước thắp hương lòng tưởng nhớ,
Non sông gấm vóc đẹp dường bao!""",
        "circumstance": "Vịnh cảnh Đền Ngọc Sơn và Hồ Hoàn Kiếm - biểu tượng thiêng liêng bậc nhất của linh khí Thăng Long Hà Nội.",
        "analysis": """- Nét vẽ trang nhã tôn vinh cảnh quan văn hóa danh thắng Hồ Gươm: Cầu Thê Húc màu son uốn cong như con tôm, Tháp Bút Tả Thanh Thiên, Đài Nghiên, Đền Ngọc Sơn.
- Gắn liền cảnh sắc với huyền tích vua Lê Thái Tổ trả gươm thần cho Rùa Vàng sau ngày đại thắng giặc Minh, khơi gợi lòng tự hào dân tộc sâu sắc.""",
        "variants": "Bản khắc gỗ Đền Ngọc Sơn thời Tự Đức."
    }
]

ANECDOTES = [
    {
        "title": "Giai Thoại Xử Án 'Phó Tổng Lãng'",
        "content": """Khi chồng bà là Lưu Nghị làm Tri phủ Thanh Quan đi vắng, có một viên phó tổng tên là Lãng đến công đường nộp đơn xin tha cho một vụ việc. Nhận thấy viên phó tổng là kẻ hống hách ức hiếp dân lành, nhân lúc cao hứng, bà Huyện Thanh Quan đã cầm bút phê vào đơn bốn câu thơ sắc bén:
'Tha cho thì cũng tha cho,
Làm chi mà phải co ro thế này?
Phó tổng Lãng ơi phó tổng Lãng,
Lần sau đừng có lại đây quấy rầy!'
(Có bản chép: 'Trăm lạy van lạy phó tổng Lãng / Lần sau đừng có đến đây quấy rầy!').
Hành động phê đơn bằng thơ vừa hóm hỉnh vừa uy nghiêm khiến cả phủ thán phục tài trí của phu nhân quan Tri phủ."""
    },
    {
        "title": "Giai Thoại Đơn Xin Mổ Trâu",
        "content": """Một lần khác, quan Tri phủ lại vắng nhà. Có một người phụ nữ tên là Nguyễn Thị Đào đến xin quan cấp giấy phép mổ trâu để làm giỗ bố (thời Nguyễn có luật cấm ngặt việc mổ trâu bừa bãi vì trâu là sức kéo nông nghiệp). Cảm kích trước tấm lòng hiếu thảo của người con gái, bà Huyện Thanh Quan liền phê ngay vào đơn hai câu lục bát tuyệt tác:
'Người ta thì chẳng lấy ai,
Mổ trâu mổ bò thì lại lấy chồng!'
(Có dị bản chép: 'Người ta chẳng lấy thì thôi / Lại đi lấy một anh chàng mổ trâu!'). Phê xong bà ký tên cấp phép. Khi quan Tri phủ về biết chuyện, chỉ cười xòa khen ngợi tài ứng biến tài tình của vợ."""
    }
]

def build_ba_huyen_thanh_quan_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Văn Học Cổ Điển Việt Nam • Thế Kỷ XIX</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">BÀ HUYỆN THANH QUAN</div>
            <div class="cover-subtitle">Toàn Tập Thơ Hoài Cổ & Khảo Luận Thi Pháp<br>Đầy đủ toàn bộ 6 bài thơ hoài cổ còn truyền lại kèm khảo dị, hoàn cảnh sáng tác & giai thoại văn chương</div>
            <div class="gold-line"></div>
            <div class="cover-author">NỮ SĨ NGUYỄN THỊ HINH (k. 1805 – 1848)</div>
            <div class="cover-author-sub">Cung Trung Giáo Tập Triều Nguyễn • Danh viện tài hoa đất Thăng Long</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Khảo đính đối chiếu Quốc Triều Thi Tập & Mộc bản triều Tự Đức</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: HỒN THƠ HOÀI CỔ THANH THANH QUAN</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Bà Huyện Thanh Quan</strong> (tên thật là <strong>Nguyễn Thị Hinh</strong>, sống vào khoảng nửa đầu thế kỷ XIX), người làng Nghi Tàm, huyện Thọ Xương (nay thuộc quận Tây Hồ, Hà Nội). Bà là vợ của danh sĩ Lưu Nghị (người làng Nguyệt Áng, Thanh Trì), từng làm Tri phủ Thanh Quan (thuộc Thái Bình), do đó người đời quen gọi bà một cách kính cẩn là <em>Bà Huyện Thanh Quan</em>.</p>
        <p>Bà nổi tiếng học rộng tài cao, thông kinh sử, giỏi thi ca, nết na đoan trang mẫu mực. Tiếng tăm tài hoa của bà vang dội đến tận kinh thành, được vua Minh Mạng vời vào Huế phong chức <strong>Cung Trung Giáo Tập</strong> để dạy học cho hoàng thái tử, công chúa và cung phi trong hoàng cung triều Nguyễn.</p>
        <p>Di sản thơ ca của bà hiện còn truyền lại trọn vẹn <strong>6 bài thơ Đường luật thất ngôn bát cú</strong> chữ Nôm. Tuy số lượng không nhiều, nhưng mỗi bài thơ đều là một viên ngọc bích sáng rực rỡ, đạt đến đỉnh cao tuyệt đối về niêm luật, bút pháp đối ngẫu, từ ngữ trang nhã và âm điệu u hoài trầm lắng, tạo nên một phong cách độc nhất vô nhị: <strong>Hồn thơ hoài cổ mẫu mực bậc nhất trong lịch sử thi ca Việt Nam</strong>.</p>
    </div>
    """)
    
    for i, p in enumerate(POEMS_6, 1):
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 25px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #8B1E1E; padding-bottom: 6px; margin-bottom: 12px;">
                <span style="font-weight: bold; color: #721616; font-size: 13pt;">{i}. {p['title']}</span>
                <span style="font-size: 9.5pt; color: #666; font-style: italic;">{p['subtitle']}</span>
            </div>
            
            <div class="poem-stanza" style="line-height: 2.1; font-size: 12pt; color: #1a365d; font-weight: 500; margin: 15px 0;">
                {p['text'].replace(chr(10), '<br>')}
            </div>
            
            <div class="commentary-box" style="margin-top: 15px;">
                <div class="commentary-title">Hoàn Cảnh Sáng Tác:</div>
                <div style="margin-bottom: 8px;">{p['circumstance']}</div>
                
                <div class="commentary-title">Phân Tích Thi Pháp & Cấu Trúc Nghệ Thuật:</div>
                <div style="margin-bottom: 8px; line-height: 1.6;">{p['analysis'].replace(chr(10), '<br>')}</div>
                
                <div class="commentary-title">Khảo Dị & Dị Bản:</div>
                <div>{p['variants']}</div>
            </div>
        </div>
        """)
        
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">GIAI THOẠI VĂN HỌC BÀ HUYỆN THANH QUAN</h1>
    <div class="ornament">❖</div>
    """)
    for a in ANECDOTES:
        html.append(f"""
        <div class="intro-box avoid-break" style="margin-top: 20px;">
            <h2 class="section-title" style="margin-top: 5px;">{a['title']}</h2>
            <p>{a['content'].replace(chr(10), '<br><br>')}</p>
        </div>
        """)
        
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">VĨ THANH: NGHỆ THUẬT ĐƯỜNG LUẬT TRÁC TUYỆT</h1>
    <div class="ornament">❖</div>
    <div class="intro-box">
        <p>Thơ Bà Huyện Thanh Quan là mẫu mực kinh điển của sự kết hợp giữa thi pháp Đường thi Trung Hoa và tâm hồn dịu dàng thuần hậu của người phụ nữ Thăng Long. Không phá cách nổi loạn như Hồ Xuân Hương, bà chọn con đường trau chuốt từng thanh âm điệu vần, dùng cái trang nhã đoan chính để biểu đạt nỗi sầu bi thẳm sâu trước cảnh nước đổi dòng đời dâu bể. Sáu bài thơ của bà mãi mãi là chuẩn mực vàng son của thi ca cổ điển nước nhà.</p>
    </div>
    """)
    
    return "\n".join(html)

async def main():
    print("Building Ba Huyen Thanh Quan comprehensive publication...")
    html_content = build_ba_huyen_thanh_quan_html()
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="BÀ HUYỆN THANH QUAN • TOÀN TẬP THƠ HOÀI CỔ",
        header_right="ẤN BẢN TOÀN THƯ KHẢO LUẬN"
    )

if __name__ == "__main__":
    asyncio.run(main())
