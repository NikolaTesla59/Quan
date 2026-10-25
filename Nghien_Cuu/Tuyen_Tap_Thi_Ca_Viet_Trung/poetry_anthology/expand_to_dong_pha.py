# -*- coding: utf-8 -*-
"""
Expand Tô Đông Pha with Hậu Xích Bích Phú and additional Tống Từ
"""
import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf
import to_dong_pha_generator

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\05. [1037-1101] Trung Quốc_Tô Đông Pha (Đại Thi Hào Tống Triều)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[1082] Tô Thức - Tuyển Tập Tống Từ & Xích Bích Phú.pdf")

HAU_XICH_BICH = {
    "title": "Hậu Xích Bích Phú (後赤壁賦)",
    "han": """是歲十月之望，步自雪堂，將歸於臨皋。
二客從予，過黃泥之坂。霜露既降，木葉盡脫。
人影在地，仰見明月。顧而樂之，行歌相答。
已而嘆曰：「有客無酒，有酒無餚；月白風清，如此良夜何？」
客曰：「今者薄暮，舉網得魚，巨口細鱗，狀如松江之鱸。顧安所得酒乎？」
歸而謀諸婦。婦曰：「我有斗酒，藏之久矣，以待子不時之需。」
於是攜酒與魚，復遊於赤壁之下。
江流有聲，斷岸千尺。山高月小，水落石出。
曾日月之幾何，而江山不可復識矣！
予乃攝衣而上，履巉巖，披蒙茸，踞虎豹，登虯龍，攀棲鶻之危巢，俯馮夷之幽宮。
蓋二客不能從焉。
劃然長嘯，草木震動，山鳴谷應，風起水湧。
予亦悄然而悲，肅然而恐，凜乎其不可留也。
反而登舟，放乎中流，聽其所止而休焉。
時夜將半，四顧寂寥。
適有孤鶴，橫江東來。翅如車輪，玄裳縞衣，戛然長鳴，掠予舟而西也。
須臾客去，予亦就睡。
夢一道士，羽衣蹁躚，過臨皋之下，揖予而言曰：
「赤壁之遊樂乎？」
問其姓名，俯而不答。
「嗚呼！噫嘻！我知之矣。疇昔之夜，飛鳴而過我者，非子也邪？」
道士顧笑，予亦驚寤。開戶視之，不見其處。""",
    "phien_am": """Thị tuế thập nguyệt chi vọng, bộ tự Tuyết Đường, tương quy vu Lâm Cảo.
Nhị khách tòng dư, quá Hoàng Nê chi bản. Sương lộ ký giáng, mộc diệp tận thoát.
Nhân ảnh tại địa, ngưỡng kiến minh nguyệt. Cố nhi lạc chi, hành ca tương đáp.
Dĩ nhi thán viết: "Hữu khách vô tửu, hữu tửu vô hào; nguyệt bạch phong thanh, như thử lương dạ hà?"
Khách viết: "Kim giả bạc mộ, cử võng đắc ngư, cự khẩu tế lân, trạng như Tùng Giang chi lư. Cố an sở đắc tửu hồ?"
Quy nhi mưu gia phụ. Phụ viết: "Ngã hữu đẩu tửu, tàng chi cửu hĩ, dĩ đãi tử bất thời chi nhu."
Ư thị huề tửu dữ ngư, phục du vu Xích Bích chi hạ.
Giang lưu hữu thanh, đoạn ngạn thiên xích. Sơn cao nguyệt tiểu, thủy lạc thạch xuất.
Tằng nhật nguyệt chi kỷ hà, nhi giang sơn bất khả phục thức hĩ!
Dư nãi nhiếp y nhi thượng, lý tiệm nham, phi mông nhung, cứ hổ báo, đăng cầu long, phan thê cốt chi nguy sào, phủ Phùng Di chi u cung.
Cái nhị khách bất năng tòng yên.
Vạch nhiên trường khiếu, thảo mộc chấn động, sơn minh cốc ứng, phong khởi thủy dũng.
Dư diệc tiếu nhiên nhi bi, túc nhiên nhi khủng, lẫm hồ kỳ bất khả lưu dã.
Phản nhi đăng chu, phóng hồ trung lưu, thính kỳ sở chỉ nhi hưu yên.
Thời dạ tương bán, tứ cố tịch liêu.
Thích hữu cô hạc, hoành giang đông lai. Thí như xa luân, huyền thường hảo y, kiết nhiên trường minh, lược dư chu nhi tây dã.
Tu du khách khứ, dư diệc tựu thụy.
Mộng nhất đạo sĩ, vũ y phiên tiên, quá Lâm Cảo chi hạ, ấp dư nhi ngôn viết:
"Xích Bích chi du lạc hồ?"
Vấn kỳ tính danh, phủ nhi bất đáp.
"Ô hô! Y hi! Ngã tri chi hĩ. Trù tích chi dạ, phi minh nhi quá ngã giả, phi tử dã da?"
Đạo sĩ cố tiếu, dư diệc kinh ngụ. Khai hộ thị chi, bất kiến kỳ xứ.""",
    "dich_nghia": """Đêm rằm tháng mười năm ấy (1082), ta đi bộ từ Tuyết Đường trở về nhà ở Lâm Cảo. Hai người khách đi theo ta, qua con dốc Hoàng Nê. Sương muối đã rơi dày, lá cây rụng sạch trơ trụi cành. Bóng người in trên mặt đất, ngẩng đầu thấy vầng trăng vằng vặc. Nhìn nhau mà lấy làm vui thích, vừa đi vừa hát họa đáp cùng nhau. Rồi sau đó thở dài mà rằng: 'Có khách quý mà không có rượu, có rượu lại không có thức nhắm; trăng thanh gió mát, đêm đẹp dường này biết làm sao đây?'. Khách thưa: 'Chiều hôm nay buông lưới bắt được một con cá lớn, miệng rộng vảy nhỏ, hình dáng tựa như cá vược sông Tùng Giang. Nhưng biết tìm đâu ra rượu bây giờ?'. Trở về bàn cùng vợ hiền. Vợ nói: 'Thiếp có một hũ rượu cất giấu đã lâu, để dành phòng lúc chàng cần đến bất ngờ'. Bèn xách rượu và cá, lại cùng nhau bơi thuyền chơi dưới chân núi Xích Bích. Dòng sông chảy xiết rền vang, bờ đá đứt đoạn đứng sững nghìn thước. Núi cao vút vầng trăng nhỏ bé, nước sông hạ cạn đá ngầm nhô lên. Mới cách tháng bảy chưa được bao lâu, mà non sông cảnh sắc đã đổi thay không nhận ra được nữa! Ta bèn vén áo trèo lên, giẫm lên vách đá lởm chởm, vạch đám cỏ rậm rạp, ngồi xổm trên tảng đá hình hổ báo, trèo lên rễ cây tựa rồng cuộn, với tới tổ chim ưng cheo leo, cúi nhìn xuống cung điện sâu thẳm của thủy thần Phùng Di. Hai người khách không thể trèo theo được. Bỗng cất tiếng huýt sáo dài rền vang, cây cỏ chấn động, núi vang thung lũng dội, gió thổi dữ dội nước trào cuồn cuộn. Ta bỗng thấy lặng lẽ mà buồn, rùng mình mà sợ, lạnh buốt chẳng thể ở lâu được nữa. Bèn quay trở lại bước xuống thuyền, thả trôi giữa dòng nước, mặc cho thuyền dừng ở nơi nào thì nghỉ ở nơi ấy. Lúc ấy đêm sắp tàn canh, nhìn bốn phía quạnh quẽ cô liêu. Chợt có một con hạc trắng lẻ loi bay ngang qua sông từ phía đông tới. Đôi cánh xòe rộng như bánh xe, áo trắng quần đen, cất tiếng kêu dài vang lảnh, lướt sát qua mui thuyền của ta rồi bay vút về phía tây. Một lát sau khách ra về, ta cũng nằm ngủ. Mơ thấy một vị đạo sĩ mặc áo lông chim phấp phới, đi qua dưới lầu Lâm Cảo, vái chào ta mà hỏi rằng: 'Cuộc chơi Xích Bích có vui chăng?'. Ta hỏi họ tên, đạo sĩ cúi đầu không đáp. Ta bỗng kêu lên: 'Than ôi! Ôi chao! Ta biết ra rồi. Đêm qua con hạc trắng bay ngang qua thuyền kêu vang lảnh lướt qua ta, há chẳng phải là bác đó sao?'. Đạo sĩ ngoảnh nhìn ta mỉm cười, ta cũng giật mình thức giấc. Mở cửa nhìn ra ngoài, chẳng thấy bóng đạo sĩ ở nơi đâu nữa!""",
    "dich_tho": """Rằm tháng mười năm ấy trăng tà,
Từ Tuyết Đường về lại Lâm Cảo.
Hai khách theo ta qua sườn dốc,
Sương rơi lá rụng trơ cành cây.
Bóng in trên đất trông trăng sáng,
Hát họa cùng nhau bước ngất ngây.
Thở than: Có bạn không mồi rượu,
Đêm đẹp trăng thanh phí bấy chầy!
Khách rằng: Chiều bắt được cá ngon,
Vảy nhỏ miệng to tựa cá Tùng.
Về hỏi vợ hiền, nàng cười bảo:
'Hũ rượu thiếp giấu tự bấy nay!'
Xách rượu cùng cá ra bờ bến,
Lại chơi Xích Bích dưới trăng vầy.
Sông chảy rền vang bờ đá dựng,
Núi cao trăng nhỏ nước vơi đầy.
Vén áo trèo lên vách đá hiểm,
Cỏ gai rậm rạp bước cheo leo.
Hét dài một tiếng rung muôn ngọn,
Gió nổi sóng dâng dạ lạnh lùng.
Trở lại thuyền nan buông mái đợi,
Đêm khuya quạnh quẽ bóng mênh mông.
Chợt đâu hạc trắng bay ngang bến,
Cánh tựa bánh xe tiếng réo vang!
Khách về ta ngủ giấc mơ màng,
Gặp ông đạo sĩ áo lông chim.
Hỏi ta: 'Chơi Xích Bích vui chăng?'
Hỏi tên người chẳng buồn đáp lời.
Chợt kêu: 'Hạc trắng đêm qua ấy,
Há chẳng phải người cưỡi gió chơi?'
Đạo sĩ cười vang thức giấc mộng,
Mở cửa sương bay vắng bóng người!""",
    "commentary": "Hậu Xích Bích Phú mang màu sắc kỳ ảo, siêu thực với hình tượng con hạc trắng và vị đạo sĩ thần tiên, biểu đạt khát vọng tự do và sự hòa nhập tuyệt đối của tâm hồn vào cõi hư vô huyền diệu."
}

EXTRA_TONG_TU = [
    {
        "title": "Giang Thành Tử • Ất Mão Dạ Mộng (江城子·乙卯正月二十日夜記夢)",
        "subtitle": "Mười Năm Sống Chết Đôi Đường • Khóc Người Vợ Trẻ Vương Phất",
        "han": """十年生死兩茫茫，不思量，自難忘。
千里孤墳，無處話淒涼。
縱使相逢應不識，塵滿面，鬢如霜。
夜來幽夢忽還鄉，小軒窗，正梳妝。
相顧無言，惟有淚千行。
料得年年腸斷處，明月夜，短松岡。""",
        "phien_am": """Thập niên sinh tử lưỡng mang mang,
Bất tư lượng, tự nan vong.
Thiên lý cô phần, vô xứ thoại thê lương.
Túng sử tương phùng ứng bất thức,
Trần mãn diện, bấn như sương.
Dạ lai u mộng hốt hoàn hương,
Tiểu hiên song, chính sơ trang.
Tương cố vô ngôn, duy hữu lệ thiên hàng.
Liệu đắc niên niên đoạn trường xứ,
Minh nguyệt dạ, đoản tùng cương.""",
        "dich_nghia": """Mười năm sống chết đôi đường cách biệt mênh mông, chẳng hề nghĩ ngợi tới mà tự đáy lòng khó thể nào quên. Ngôi mộ cô đơn cách xa nghìn dặm, không có nơi nào để giãi bày nỗi thê lương. Dẫu cho có gặp lại nhau chắc nàng cũng chẳng nhận ra ta, bởi mặt mày phủ đầy bụi bặm phong trần, mái tóc mai đã bạc trắng như sương. Đêm qua giấc mộng sâu kín bỗng đưa ta trở về quê nhà, nơi khung cửa sổ nhỏ năm xưa nàng đang ngồi chải tóc điểm trang. Hai người nhìn nhau không thốt nên lời, chỉ có nghìn hàng nước mắt tuôn rơi. Liệu biết rằng năm này qua năm khác chốn xé đứt từng khúc ruột, chính là đêm trăng sáng vằng vặc trên ngọn đồi thông thấp chôn cất mộ nàng!""",
        "dich_tho": """Mười năm sống chết cách đôi đường,
Chẳng nghĩ suy mà nhớ khôn cùng.
Nghìn dặm mộ côi sầu ai tỏ?
Gặp lại ắt nàng chẳng nhận ta:
Bụi phủ đầy mặt, tóc hoa râm!
Đêm qua mộng mị về quê cũ,
Bên cửa sổ nhỏ nàng điểm trang.
Nhìn nhau chẳng nói nên lời được,
Chỉ có tuôn trào giọt lệ tuôn.
Năm năm thắt ruột nơi đồi vắng,
Đêm trăng soi sáng rặng thông cằn!""",
        "commentary": "Thiên kiệt tác điệu vong (khóc vợ) cảm động nhất trong văn học Trung Hoa. Nỗi đau mười năm vẫn tươi nguyên như thuở ban đầu, giọt nước mắt câm nín trong mơ lay động triệu trái tim."
    },
    {
        "title": "Đề Tây Lâm Bích (題西林壁)",
        "subtitle": "Đề Vách Chùa Tây Lâm • Triết Lý Nhìn Núi Lư Sơn",
        "han": """橫看成嶺側成峰，
遠近高低各不同。
不識廬山真面目，
只緣身在此山中。""",
        "phien_am": """Hoành khán thành lĩnh trắc thành phong,
Viễn cận cao đê các bất đồng.
Bất thức Lư Sơn chân diện mục,
Chỉ duyên thân tại thử sơn trung.""",
        "dich_nghia": """Nhìn ngang thấy dãy núi thoai thoải nhìn nghiêng thấy ngọn núi nhọn hoắt, trông xa ngắm gần đứng trên cao nhìn xuống thấp mỗi góc độ đều khác nhau. Không nhận ra được bộ mặt chân thực của núi Lư Sơn, chỉ vì chính thân mình đang nằm ở trong lòng ngọn núi ấy!""",
        "dich_tho": """Nhìn ngang thành dãy dọc thành non,
Gần xa cao thấp thảy vuông tròn.
Chẳng rõ Lư Sơn hình sắc thật,
Chỉ vì mình ở giữa lòng non!""",
        "commentary": "Bốn câu thơ triết học sâu sắc: Muốn thấu hiểu chân lý sự vật phải có cái nhìn toàn diện khách quan từ bên ngoài, nếu chỉ đắm chìm trong định kiến chủ quan cục bộ thì không bao giờ thấy được 'chân diện mục' của đời sống."
    }
]

async def run_expansion():
    print("Expanding To Dong Pha publication with Hau Xich Bich and Tong Tu...")
    # Add to to_dong_pha_generator
    to_dong_pha_generator.TONG_TU.extend(EXTRA_TONG_TU)
    
    html = []
    # Bìa
    html.append(to_dong_pha_generator.build_to_dong_pha_html())
    
    # Thêm Hậu Xích Bích Phú
    html.append(f"""
    <div class="page-break"></div>
    <h1 class="chapter-title">HẬU XÍCH BÍCH PHÚ (後 赤 壁 賦)</h1>
    <div style="text-align: center; font-style: italic; color: #555; margin-bottom: 20px;">Trăng Rằm Tháng Mười & Giấc Mộng Hạc Trắng Thần Tiên</div>
    <div class="ornament">❖ ❖ ❖</div>
    
    <div class="poem-container avoid-break">
        <div class="poem-parallel">
            <div class="poem-col" style="flex: 1.15; background: #fffdfa; border-color: #e5dac6;">
                <div class="col-header">Bản Dịch Thơ Phú</div>
                <div class="dich-tho" style="line-height: 1.85; font-size: 11pt; padding: 4px 6px;">
                    {HAU_XICH_BICH['dich_tho'].replace(chr(10), '<br>')}
                </div>
            </div>
            
            <div class="poem-col" style="flex: 1; background: #faf8f5;">
                <div class="col-header">Nguyên Tác Chữ Hán</div>
                <div class="han-script" style="text-align: justify; margin-bottom: 8px; font-size: 10.5pt; line-height: 1.7;">
                    {HAU_XICH_BICH['han'].replace(chr(10), '<br><br>')}
                </div>
            </div>
        </div>
        
        <div class="commentary-box" style="margin-top: 15px;">
            <div class="commentary-title">Dịch Nghĩa Toàn Văn Hậu Xích Bích Phú:</div>
            <div style="line-height: 1.6; margin-bottom: 8px;">{HAU_XICH_BICH['dich_nghia'].replace(chr(10), '<br><br>')}</div>
            <div class="commentary-title">Bình Luận Triết Lý:</div>
            <div>{HAU_XICH_BICH['commentary']}</div>
        </div>
    </div>
    """)
    
    full_html = "\n".join(html)
    await render_html_to_pdf(
        html_content=full_html,
        output_path=OUTPUT_FILE,
        header_left="TÔ ĐÔNG PHA • TUYỂN TẬP TỐNG TỪ & XÍCH BÍCH PHÚ",
        header_right="TIỀN & HẬU XÍCH BÍCH PHÚ TOÀN BẢN"
    )

if __name__ == "__main__":
    asyncio.run(run_expansion())
