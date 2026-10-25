# -*- coding: utf-8 -*-
"""
Expand Phong Trào Thơ Mới with 10 more immortal poems
"""
import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf
import tho_moi_generator

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\11. [1932-1945] Việt Nam_Phong Trào Thơ Mới (Đỉnh Cao Thi Ca Hiện Đại)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[1932-1945] Tinh Hoa Phong Trào Thơ Mới.pdf")

EXTRA_THO_MOI = [
    {
        "author": "XUÂN DIỆU (1916 – 1985)",
        "title": "Thơ Duyên",
        "text": """Chiều mộng hoà thơ trên nhánh duyên,
Cây me ríu rít cặp chim chuyền.
Đổ trời xanh ngọc qua muôn lá,
Thu đến - nơi nơi động tiếng huyền.

Con đường nhỏ nhỏ gió xiêu xiêu,
Lả lả cành hoang nắng trở chiều.
Buổi ấy lòng ta nghe ý bạn,
Lần đầu rung động nỗi thương yêu.

Em bước điềm nhiên không vướng chân,
Anh đi lững đững chẳng theo gần.
Vô tâm - nhưng giữa bài thơ dịu,
Anh với em như một cặp vần.

Mây biếc về đâu bay gấp gấp,
Con cò trên ruộng cánh phân vân.
Chim nghe trời rộng giang thêm cánh,
Hoa lạnh chiều thưa sương xuống dần.

Ai hay tuy chẳng hẹn hò nhau,
Mà đã lòng ta chạm bước đầu?
Rung rẩy tơ lòng ngơ ngẩn đón,
Trời thu ngát ngọc thấu ngàn sâu.""",
        "commentary": "Thi phẩm hòa điệu diệu kỳ giữa thiên nhiên và tâm hồn đôi lứa: 'Anh với em như một cặp vần' - sự giao cảm tự nhiên tinh tế đến nghẹn ngào."
    },
    {
        "author": "HUY CẬN (1919 – 2005)",
        "title": "Ngậm Ngùi",
        "text": """Tay anh em hãy tựa đầu,
Cho anh nghe nặng trái sầu rụng rơi.
Tiếng mùa thu gió thổi vơi,
Lá ngô rụng cánh sương rơi lạnh lùng.

Ngủ đi em, mộng chưa tùng,
Hồn anh phiêu dạt giữa chừng khói sương.
Đời là muôn nỗi vấn vương,
Duyên là giọt lệ dặm trường chia phôi.

Ngủ đi cho gió ngừng trôi,
Cho trăng ngừng sáng cho đời ngừng cay.
Tay anh ấp ủ bàn tay,
Ru em tròn giấc đọa đày trần ai...""",
        "commentary": "Giai điệu du dương êm ả của thể thơ lục bát ru hồn người vào cõi mộng ảo u sầu, mang vẻ đẹp cổ điển đằm thắm."
    },
    {
        "author": "CHẾ LAN VIÊN (1920 – 1989)",
        "title": "Trên Đường Về (Điêu Tàn)",
        "text": """Tự thuở mở lòng yêu nước lạ,
Tìm thăm Chàm dấu tích hoang sơ.
Đường về xa lắc trong sương gió,
Ngắm bóng tháp Chàm đứng ngẩn ngơ.

Tháp cổ rêu phong màu xám ngắt,
Tượng thần rạn vỡ nét uy nghiêm.
Đâu người vũ nữ vòng eo uốn?
Đâu tiếng đàn xưa khúc nguyệt chìm?

Gió hú ngàn lau sầu quạnh quẽ,
Xương tàn vùi dập chốn sa trường.
Chiến tranh tàn phá nghìn năm trước,
Để lại lòng ta nỗi xót thương!

Hỡi giống dân Hời nay ở đâu?
Hồn ma vất vưởng cõi trời sâu!
Ta nghe trong gió lời than thở,
Máu đọng thềm son dạ nghẹn ngào!""",
        "commentary": "Đại diện tiêu biểu của Trường thơ Loạn với thế giới ma quái, kinh dị hoài niệm vương quốc Chiêm Thành điêu tàn đổ nát, bộc lộ nỗi đau mất nước thẳm sâu."
    },
    {
        "author": "ĐOÀN VĂN CỪ (1913 – 2004)",
        "title": "Chợ Tết",
        "text": """Dải mây trắng đỏ dần trên đỉnh núi,
Sương hồng lam ôm ấp nóc nhà tranh.
Con trâu đen đứng vờn theo chân núi,
Nghe tiếng gà gáy giục buổi tàn canh.

Người các ấp tưng bừng ra chợ Tết,
Họ vui vẻ kéo hàng trên cỏ biếc.
Những thằng cu áo đỏ chạy lon xon,
Vài cụ già chống gậy bước lom khom.

Cô thôn nữ mắt nhung môi đỏ thắm,
Nón lá nghiêng che suối tóc đen tuyền.
Bà lão bán trầu cau cười móm mém,
Thầy đồ ngồi viết đối chữ như rồng.

Chợ tưng bừng rực rỡ sắc màu xuân,
Ánh nắng ấm chan hòa trên mặt bến.
Chiều dần buông chợ vãn khách quay về,
Dấu hài hoa in nhẹ lối đồng quê.""",
        "commentary": "Bức tranh dân gian rực rỡ sắc màu về hội chợ quê ngày Tết miền Bắc, giàu phong vị cổ truyền mộc mạc."
    },
    {
        "author": "ANH THƠ (1921 – 2005)",
        "title": "Chiều Xuân",
        "text": """Mưa đổ bụi êm đềm trên bến vắng,
Đò biếng lười nằm mặc nước sông trôi.
Quán tranh đứng im lìm trong bóng lặng,
Bên chòm xoan hoa tím rụng tơi bời.

Ngoài đường đê cỏ non tràn ngút mắt,
Đàn sáo đen sà xuống rỉa lông tơ.
Trâu chậm chạp nhai rơm bên bờ suối,
Cánh đồng chiều êm ả tựa trang thơ.

Trong đồng lúa cô nàng cào cỏ dại,
Nón nghiêng che vạt áo cánh thâm mềm.
Chốc chốc lại ngước nhìn trời mưa bụi,
Miệng mỉm cười đón gió thoảng êm đềm.""",
        "commentary": "Nét vẽ tinh tế, tĩnh lặng đậm chất nữ tính về khung cảnh đồng quê miền Bắc trong làn mưa bụi mùa xuân."
    },
    {
        "author": "NGUYỄN BÍNH (1918 – 1966)",
        "title": "Lỡ Bước Sang Ngang",
        "text": """Mẹ ơi! Con bước sang ngang,
Thuyền hoa tách bến lỡ làng duyên xưa.
Trời làm chi trận gió mưa,
Để cho dang dở ước mơ thuở nào?

Sông sâu sóng vỗ ba đào,
Con đò cách trở phương nào người thương?
Áo hồng cởi lại quê hương,
Khăn tang gói trọn đoạn trường từ đây!

Trách ai se sợi chỉ hồng,
Để cho cay đắng tơ lòng dở dang.
Ngậm ngùi nuốt lệ sang ngang,
Trăm năm gửi bóng mây ngàn viễn phương!""",
        "commentary": "Khúc tràng ca bi thương của người phụ nữ lỡ duyên lỡ bước, lời thơ mộc mạc dân dã thấm sâu vào hồn dân tộc."
    },
    {
        "author": "NGUYỄN NHƯỢC PHÁP (1914 – 1938)",
        "title": "Em Đi Chùa Hương",
        "text": """Hôm nay em đi chùa Hương,
Hoa cỏ mờ hơi sương.
Cùng thầy me em dậy,
Vấn đầu soi gương trong.

Khăn nhỏ, đuôi gà cao,
Em đeo dải yếm đào.
Quần nĩnh, áo the thắm,
Tay cầm cành sen ngào.

Đò qua bến đò xưa,
Người đông như hội mưa.
Em thẹn thùng cúi mặt,
Chẳng dám nhìn người đưa.

Nam mô A Di Đà!
Cầu Phật ban duyên hòa.
Cho em cùng người ấy,
Trọn đời kết trăm hoa!""",
        "commentary": "Nét thơ trong sáng, hồn nhiên, dí dỏm như nụ cười thiếu nữ ngày xuân trẩy hội Chùa Hương."
    },
    {
        "author": "BÍCH KHÊ (1916 – 1946)",
        "title": "Tỳ Bà",
        "text": """Nàng tuyết sĩ trăng hoa,
Dưới hoa tỳ bà.
Ô hay buồn vương cây ngô đồng,
Vàng rơi vàng rơi thu mênh mông!

Khúc tỳ bà ngân nga,
Trăng thu lồng bóng hoa.
Hồn xưa đâu tá hỡi mỹ nhân?
Sương trắng bay mờ cõi trầm luân.

Tơ đồng rung rinh lệ ngọc tràn,
Gió lạnh đầu non buốt tiếng đàn.
Vàng rơi, vàng rơi, thu vàng rơi,
Buồn trôi, sầu trôi, lệ ngậm ngùi!""",
        "commentary": "Đỉnh cao của trường phái tượng trưng và nhạc điệu ngôn từ trong phong trào Thơ Mới: 'Vàng rơi vàng rơi thu mênh mông'."
    }
]

async def run_expansion():
    print("Expanding Tho Moi publication with 8 more immortal poems...")
    tho_moi_generator.THO_MOI_POEMS.extend(EXTRA_THO_MOI)
    html_content = tho_moi_generator.build_tho_moi_html()
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="PHONG TRÀO THƠ MỚI (1932 - 1945)",
        header_right="ĐẠI TUYỂN TẬP TINH HOA THI CA TOÀN BẢN"
    )

if __name__ == "__main__":
    asyncio.run(run_expansion())
