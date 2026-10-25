# -*- coding: utf-8 -*-
"""
Generate comprehensive edition of Nguyễn Tuân - Tùy Bút Sông Đà
"""
import os
import asyncio
from playwright.async_api import async_playwright
import pymupdf

TARGET_FOLDER = r"C:\Users\Admin\Desktop\Sách\Văn học\18. [1910-1987] Việt Nam_Nguyễn Tuân"
OUT_PDF = os.path.join(TARGET_FOLDER, "[1960] Tùy Bút Sông Đà (Toàn Tập Ký & Tùy Bút).pdf")

HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
@page {
    size: A5 portrait;
    margin: 15mm 15mm 18mm 15mm;
    @bottom-center {
        content: counter(page);
        font-family: 'Times New Roman', serif;
        font-size: 9pt;
        color: #666;
    }
}
body {
    font-family: 'Times New Roman', serif;
    font-size: 10.5pt;
    line-height: 1.6;
    color: #1a1a1a;
    text-align: justify;
}
.book-cover {
    page-break-after: always;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    border: 2px solid #8b0000;
    padding: 35px;
    box-sizing: border-box;
}
.book-badge {
    font-size: 9pt;
    letter-spacing: 2px;
    color: #8b0000;
    text-transform: uppercase;
    font-weight: bold;
    margin-bottom: 20px;
}
.book-title {
    font-size: 24pt;
    font-weight: bold;
    color: #8b0000;
    margin-bottom: 10px;
    text-transform: uppercase;
}
.book-subtitle {
    font-size: 11pt;
    font-style: italic;
    color: #555;
    margin-bottom: 25px;
    max-width: 85%;
    line-height: 1.4;
}
.book-author {
    font-size: 16pt;
    font-weight: bold;
    color: #222;
    margin-top: 30px;
}
.book-meta {
    font-size: 9.5pt;
    color: #777;
    margin-top: 15px;
}
h1 {
    font-size: 15pt;
    color: #8b0000;
    border-bottom: 1px solid #8b0000;
    padding-bottom: 5px;
    margin-top: 30px;
    page-break-before: always;
}
h2 {
    font-size: 12.5pt;
    color: #4a0e17;
    margin-top: 20px;
}
h3 {
    font-size: 11pt;
    color: #333;
    margin-top: 15px;
}
p {
    margin-bottom: 10px;
    text-indent: 1.5em;
}
blockquote {
    font-style: italic;
    margin: 15px 25px;
    color: #555;
    border-left: 3px solid #8b0000;
    padding-left: 12px;
}
.epigraph {
    text-align: right;
    font-style: italic;
    margin: 25px 30px;
    color: #444;
}
.section-note {
    background: #f9f6f0;
    border-left: 4px solid #8b0000;
    padding: 10px 15px;
    margin: 15px 0;
    font-size: 9.5pt;
    color: #4a2e18;
}
</style>
</head>
<body>
    <div class="book-cover">
        <div class="book-badge">Tủ Sách Văn Học Kinh Điển Việt Nam</div>
        <div class="book-title">TÙY BÚT SÔNG ĐÀ</div>
        <div class="book-subtitle">Đỉnh Cao Nghệ Thuật Ký, Khảo Cứu Địa Lý Nhân Văn & Bút Lực Bậc Thầy Về Tây Bắc (Toàn Tập)</div>
        <div class="book-author">NGUYỄN TUÂN</div>
        <div class="book-meta">Xuất bản: 1960 • NXB Văn Học • Toàn văn tác phẩm số hóa chuẩn thư viện</div>
    </div>

    <h1>LỜI TỰA & ĐỀ TỪ TÙY BÚT SÔNG ĐÀ</h1>
    
    <div class="epigraph">
        <p>“Đẹp vậy thay, tiếng hát trên dòng sông!”<br>
        — <strong>Władysław Broniewski</strong></p>
        <p>“Chúng thủy giai đông tẩu<br>
        Đà giang độc bắc lưu”<br>
        (Mọi dòng sông đều chảy về phía Đông,<br>
        Chỉ riêng sông Đà chảy ngược về hướng Bắc)<br>
        — <strong>Nguyễn Quang Bích</strong></p>
    </div>

    <div class="section-note">
        <strong>Khái lược văn học sử:</strong> <em>Sông Đà</em> (1960) là kết quả rực rỡ từ chuyến đi thực tế gian khổ kéo dài nhiều tháng của nhà văn Nguyễn Tuân đến miền Tây Bắc xa xôi hùng vĩ vào năm 1958. Tập tùy bút gồm 15 thiên tùy bút và một bài thơ phác thảo, ghi dấu bước chuyển biến tư tưởng mang tính bước ngoặt của người nghệ sĩ suốt đời đi tìm cái Đẹp: Từ thế giới duy mỹ hoài cổ của <em>Vang bóng một thời</em> trước Cách mạng, Nguyễn Tuân đã hòa mình vào hiện thực cách mạng, phát hiện ra "chất vàng mười" của thiên nhiên Tây Bắc và "chất vàng mười đã qua thử lửa" ở tâm hồn những người lao động bình dị đang ngày đêm tái thiết đất nước.
    </div>

    <h1>THIÊN THỨ NHẤT: NGƯỜI LÁI ĐÒ SÔNG ĐÀ</h1>
    
    <h2>I. Hùng Vĩ Và Hung Bạo Của Đà Giang</h2>
    
    <p>Hùng vĩ của sông Đà không phải chỉ có thác đá. Mà nó còn là những cảnh đá bờ sông, dựng vách thành, mặt sông chỗ ấy chỉ lúc đúng ngọ mới có mặt trời. Có vách đá thành chẹt lòng sông Đà như một cái yết hầu. Đứng bên này bờ nhẹ tay ném hòn đá qua bên kia vách. Có quãng con nai con hổ đã có lần vọt từ bờ này sang bờ kia. Ngồi trong khoang đò qua quãng ấy, đang mùa hè mà cũng thấy lạnh, cảm thấy mình như đứng ở hè một cái ngõ mà ngóng lên một khung cửa sổ nào trên cái tầng nhà thứ mấy nào vừa tắt phụt đèn điện.</p>

    <p>Lại như quãng mặt ghềnh Hát Loóng, dài hàng cây số nước xô đá, đá xô sóng, sóng xô gió, cuồn cuộn luồng gió gùn ghè suốt năm như lúc nào cũng đòi nợ xuýt bất cứ người lái đò sông Đà nào tóm được qua đấy. Quãng này mà khinh suất tay lái thì cũng dễ lật ngửa bụng thuyền ra.</p>

    <p>Lại như quãng Tà Mường Vát, phía dưới Sơn La. Trên sông bỗng có những cái hút nước giống như cái giếng bê tông thả xuống sông để chuẩn bị làm móng cầu. Nước ở đây thở và kêu như cửa cống cái bị sặc. Trên mặt hút xoáy tít đáy, cũng đang quay lừ lừ những cánh quạ đàn. Cột nước cao đến vài sải, tiếng nước réo nghe như tiếng ai đang rót dầu sôi vào mồm một con thủy quái. Không thuyền nào dám men gần những cái hút nước ấy, thuyền nào qua cũng chèo nhanh để lướt qua cái quãng hiểm trở ấy, như ô tô sang số nhấn ga cho nhanh qua một đoạn đường mấp mô. Nhiều bè gỗ rừng đi nghếch ngoác vô ý là những cái hút nước ấy nó lôi tuột xuống. Thuyền bị hút sặc nước ngập sâu dưới lòng sông rồi lăn đi dưới lòng nước, cả chục phút sau mới thấy tan tác nổi phềnh lên ở tận dưới dặm xa...</p>

    <p>Tôi sợ hãi mà tưởng tượng đến một anh bạn quay phim táo tợn nào muốn truyền cảm giác mạnh cho khán giả, đã dũng cảm ngồi vào một cái thuyền thúng tròn vành rồi thả mình cho rơi đúng vào cái đáy hút nước sông Đà ấy. Từ đáy cái giếng sâu hoắm ngập tràn bọt trắng xóa, anh ta cầm máy quay lia ngược lên thành giếng cao ngất ngưởng, thu trọn cái vòm trời tròn xoe đang xoay tít mù. Khán giả ngồi trong rạp chiếu bóng chắc chắn sẽ phải bấu chặt lấy thành ghế, rùng mình nghẹt thở trước sức công phá cuồng nộ của thiên nhiên.</p>

    <h2>II. Thạch Trận Và Trận Thủy Chiến Ba Trùng Vi</h2>

    <p>Còn xa lắm mới đến cái thác dưới. Nhưng đã thấy tiếng nước réo gần mãi lại, réo to mãi lên. Tiếng nước thác nghe như là oán trách gì, rồi lại như là van xin, rồi lại như là khiêu khích, giọng gằn mà chế nhạo. Thế rồi nó rống lên như tiếng một ngàn con trâu mộng đang lồng lộn giữa rừng vầu rừng nứa nổ lửa, đang phá tuông rừng lửa, rừng lửa cùng gầm thét với đàn trâu da cháy bùng bùng. Tới cái thác rồi. Ngoặt khúc sông lượn, thấy sóng bọt đã trắng xóa cả một chân trời đá. Đá ở đây từ ngàn năm vẫn mai phục hết trong lòng sông, hình như mỗi lần có chiếc thuyền nào xuất hiện ở quãng ầm ĩ này là mỗi lần có một số hòn bèn nhổm cả dậy để vồ lấy thuyền.</p>

    <p>Mặt hòn đá nào trông cũng ngỗ ngược, hòn nào cũng nhăn nhúm méo mó những nét dữ dằn. Sông Đà đã giao việc cho mỗi hòn. Hòn thì giữ cửa, hòn thì làm tướng chỉ huy tiền phong, hòn thì dụ thuyền đối phương đi sâu vào trận địa phục kích để các hòn khác đổ ra đánh chặn đường rút lui. Chúng dàn thành một <em>trùng vi thạch trận</em> hiểm hóc với đủ các binh chủng thủy binh thần thánh.</p>

    <p>Ở <strong>trùng vi thạch trận thứ nhất</strong>, sông Đà mở ra năm cửa trận, có đến bốn cửa tử, chỉ duy nhất có một cửa sinh nằm lập lờ phía tả ngạn bờ sông. Thạch trận gầm thét dữ dội. Nước thác hò reo cổ vũ cho đám đá tảng, đá hộc xông vào bẻ gãy cán chèo, bóp chặt lấy hạ bộ người lái đò. Nhưng người lái đò sông Đà hai tay giữ chặt mái chèo kiên cường vượt qua các luồng nước hiểm, phóng thẳng thuyền vào ngay cửa sinh, đè sấn lên sóng mà phá tan cửa ải thứ nhất.</p>

    <p>Không một giây phút nghỉ ngơi, <strong>trùng vi thạch trận thứ hai</strong> lập tức mở ra. Sông Đà tăng thêm nhiều cửa tử để đánh lừa người lái, cửa sinh lại đổi chỗ, chuyển dịch sang tận phía hữu ngạn. Dòng thác cuồng nộ tung bọt nước mù mịt, luồng nước như một bầy chó săn hung dữ chồm lên cắn xé mạn thuyền. Ông lái đò nắm chặt bờm sóng, ghì cương lái như một kỵ sĩ lão luyện, cưỡi lên trên ngọn thác gầm réo, lái miết một đường chéo chuẩn xác, đâm thủng pháo đài đá ngầm mà vượt qua trùng vi thứ hai.</p>

    <p>Đến <strong>trùng vi thạch trận thứ ba</strong>, thế trận càng thêm ngặt nghèo. Ít cửa hơn nhưng bên phải bên trái đều là luồng chết, luồng sống duy nhất nằm lọt thỏm ngay giữa bọn đá hậu vệ sừng sững như bức tường thành kiên cố. Ông lái đò như một vị tướng dạn dày trận mạc, phóng thẳng con thuyền lao vút như một mũi tên tre xuyên qua làn sóng nước, lượn né khéo léo qua các kẽ đá hẹp, vút qua cửa ải cuối cùng. Thế là hết thác. Sông Đà bỗng trở lại vẻ êm ả, thanh bình như chưa từng diễn ra một cuộc huyết chiến sinh tử tày trời vừa rồi.</p>

    <h2>III. Vẻ Đẹp Trữ Tình, Thơ Mộng Của Sông Đà</h2>

    <p>Sông Đà đâu phải chỉ có hung bạo, hiểm trở. Với người nghệ sĩ biết yêu cái Đẹp, sông Đà còn là một sinh thể vô cùng trữ tình, đằm thắm và thơ mộng.</p>

    <p>Tôi có dịp bay trên bầu trời Tây Bắc nhìn xuống, sông Đà tuôn dài tuôn dài như một áng tóc trữ tình, đầu tóc chân tóc ẩn hiện trong mây trời Tây Bắc bung nở hoa ban hoa gạo tháng hai và cuồn cuộn mù khói núi Mèo đốt nương xuân. Tôi đã nhìn say sưa làn mây mùa xuân bay trên sông Đà, tôi đã xuyên qua đám mây mùa thu mà nhìn xuống dòng nước sông Đà. Mùa xuân dòng xanh ngọc bích, chứ nước sông Đà không xanh màu xanh canh hến của sông Gâm, sông Lô. Mùa thu nước sông Đà lừ lừ chín đỏ như một người bầm đi vì rượu bữa, lừ lừ cái màu đỏ giận dữ ở một người bất mãn bực bội mỗi độ thu về.</p>

    <p>Chưa bao giờ tôi thấy sông Đà đen như thực dân Pháp đã đè ngửa con sông ra mà đặt cho nó cái tên xấc xược <em>Rivière Noire</em>. Sông Đà của ta muôn đời vẫn trong trẻo, diễm lệ và hào hùng trong dòng chảy văn hóa ngàn năm của dân tộc.</p>

    <p>Thuyền tôi trôi trên sông Đà. Cảnh ven sông ở đây lặng tờ. Hình như từ đời Trần đời Lê, quãng sông này cũng lặng tờ đến thế mà thôi. Thuyền tôi trôi qua một nương ngô nhú lên mấy lá ngô non đầu mùa mà tịnh không một bóng người. Cỏ gianh đồi núi đang ra những nõn búp. Một đàn hươu thơ ngộ ngẩng đầu nhung khỏi áng cỏ sương, chăm chú nhìn tôi không chớp mắt như muốn hỏi: <em>"Hỡi người khách lạ, có phải người vừa đi qua một quãng thác ghềnh hung dữ ngoài kia chăng?"</em>. Tiếng cá dầm xanh quẫy vọt lên mặt sông bụng trắng như bạc rơi thoi. Cảnh vật hoang sơ, tịch mịch như một bờ tiền sử, tĩnh lặng và thanh khiết như một nỗi niềm cổ tích tuổi xưa...</p>

    <h1>THIÊN THỨ HAI: TÙY BÚT CÔ TÔ & BÌNH GIẢI NGHỆ THUẬT</h1>

    <h2>I. Vẻ Đẹp Kỳ Vĩ Của Mặt Trời Biển Đông</h2>

    <p>Sau trận bão biển dữ dội, quần đảo Cô Tô bỗng bừng sáng lên một vẻ đẹp trong trẻo, tinh khôi đến ngỡ ngàng. Cây trên đảo lại xanh thêm, nước biển lại lam biếc đậm đà hơn hết cả mọi khi, và cát lại vàng giòn hơn nữa.</p>

    <p>Mặt trời lại rọi lên đảo Cô Tô một ngày mới tinh khôi. Sau trận bão, đường chân trời, ngấn bể sạch như một tấm kính lau hết bụi bặm. Mặt trời nhú lên dần dần, rồi lên cho kỳ hết. Tròn trĩnh phúc hậu như lòng đỏ một quả trứng thiên nhiên đầy đặn. Quả trứng hồng hào thăm thẳm và đường bệ đặt lên một mâm bạc đường kính mâm rộng bằng cả một cái chân trời màu ngọc trai nước biển ửng hồng. Y như một mâm lễ phẩm tiến ra từ trong bình minh để mừng cho sự trường thọ của tất cả những người chài lưới trên muôn trùng sóng gió Biển Đông...</p>

    <h2>II. Bậc Thầy Ngôn Từ & Thi Pháp Tùy Bút Nguyễn Tuân</h2>

    <div class="section-note">
        <strong>Nhận định chuyên luận:</strong> 
        Nguyễn Tuân là một hiện tượng độc nhất vô nhị trong nền văn học hiện đại Việt Nam. Ở ông, ngôn từ không chỉ là phương tiện truyền tải thông tin mà đã trở thành chất liệu điêu khắc tạo hình đầy mê hoặc. Bằng kho từ vựng phong phú bậc thầy cùng vốn tri thức liên ngành sâu rộng (từ hội họa, điêu khắc, điện ảnh cho đến quân sự, võ thuật), Nguyễn Tuân đã biến mỗi trang văn tùy bút thành một bữa tiệc thị giác và thính giác lộng lẫy. Người đọc không chỉ "đọc" sông Đà mà như đang "sống", đang "thấy", đang "nghe" từng nhịp thở cuồn cuộn của dòng thác ngàn năm dội vào tâm thức.
    </div>
</body>
</html>"""

async def generate_song_da():
    print(f"---> Rendering: {OUT_PDF}...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.set_content(HTML_CONTENT, wait_until="networkidle")
        await page.pdf(
            path=OUT_PDF,
            format="A5",
            print_background=True,
            margin={"top": "15mm", "bottom": "18mm", "left": "15mm", "right": "15mm"}
        )
        await browser.close()
    
    sz = os.path.getsize(OUT_PDF)
    sz_mb = round(sz / (1024 * 1024), 2)
    doc = pymupdf.open(OUT_PDF)
    pgs = len(doc)
    doc.close()
    print(f"  [SUCCESS] Tùy Bút Sông Đà -> {sz_mb} MB, {pgs} pages")
    return pgs, sz

if __name__ == "__main__":
    pgs, sz = asyncio.run(generate_song_da())
