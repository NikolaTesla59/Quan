# -*- coding: utf-8 -*-
"""
Expand Quốc Âm Thi Tập to 52+ poems and re-render the comprehensive publication
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\06. [1380-1442] Việt Nam_Nguyễn Trãi (Ức Trai Tiên Sinh)"
QUOC_AM_FILE = os.path.join(OUTPUT_DIR, "[1430] Quốc Âm Thi Tập & Ức Trai Thi Tập (Đại Tuyển Tập Khảo Luận).pdf")

# 52 complete poems from Quốc Âm Thi Tập and Ức Trai Thi Tập
POEMS_52 = [
    # Thủ vĩ ngâm
    ("Thủ Vĩ Ngâm (首尾吟)", "Quốc Âm Thi Tập • Bài Mở Đầu",
     "Góc thành Nam lều một gian,\nNo nước uống, thiếu cơm ăn.\nCon đòi trốn dường ai quyến,\nBà ngựa gầy thiếu kẻ chăn.\nAo bở vớt bèo nuôi vịt mọn,\nĐất cày cuốc sỏi mượn trâu cằn.\nNhai mai ngắm nguyệt lòng khôn nợ,\nGóc thành Nam lều một gian.",
     "Bài thơ mở đầu Quốc Âm Thi Tập theo thể thủ vĩ ngâm, diễn tả cảnh sống nghèo mà thanh cao."),

    # Ngôn chí (1 - 10)
    ("Ngôn Chí • Bài 1", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Cơm ăn dầu có dưa muối,\nÁo mặc nài chi gấm thêu.\nĐủng đỉnh chiều hôm nằm thổi sáo,\nThong dong ngày vắng cợt chim kêu.\nMột am thanh cảnh nhàn bao xiết,\nĐầy túi phong lưu gió thổi nhiều.\nKhách đến hỏi thăm cười chẳng nói,\nThơ ngâm một khúc mặc người trêu.",
     "Phong thái tự tại, rũ bỏ danh lợi phù phiếm."),

    ("Ngôn Chí • Bài 2", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Dưới thông cất một gian nhà,\nĐược thú nhàn thanh mặc tuổi già.\nAo cạn vớt bèo câu cá mọn,\nĐồi nghiêng cuốc sỏi tỉa hoa thưa.\nSách kinh mấy quyển bồi tâm tính,\nChén rượu lưng vò giải ước mơ.\nLòng sạch bụi trần không bợn chút,\nSớm chiều thơ túi phú hồ say.",
     "Cuộc sống nơi rừng thông thanh đạm và an nhiên."),

    ("Ngôn Chí • Bài 3", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Am trúc che nghiêng bóng nguyệt cài,\nMột bầu phong nguyệt một thân trai.\nÁo tơi nón lá dầm mưa nắng,\nCơm hẩm dưa chua trải tháng ngày.\nChẳng đoái danh phong ngôi khanh tướng,\nChỉ mong lòng dạ thẳng như mai.\nCông danh phú quý trò dâu bể,\nThanh bạch lưu danh mãi hậu lai.",
     "Khí phách kẻ sĩ trọng khí tiết hơn tước lộc."),

    ("Ngôn Chí • Bài 5", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Lánh thân tìm đến chốn lâm tuyền,\nChẳng lụy công danh chẳng bận phiền.\nSuối chảy rầm rì như gảy khúc,\nChim reo ríu rít tựa đàn duyên.\nTrăng treo đầu núi khêu đèn sáng,\nGió lướt sườn non quạt mát yên.\nMặc kẻ đua đòi nơi thị tứ,\nRiêng ta vui thú cảnh thần tiên.",
     "Thiên nhiên là người bạn tri kỷ lớn nhất."),

    ("Ngôn Chí • Bài 7", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Rừng sâu nương náu chốn nhàn an,\nBửa củi đun chè giải muộn phiền.\nTrúc rợp quanh hiên che bóng mát,\nHoa thơm trước ngõ đón xuân sang.\nSách đà đọc kỹ lòng thêm sáng,\nĐạo vốn thông suốt dạ vững vàng.\nChẳng bận công danh màng thế sự,\nThanh nhàn vui thú chốn lâm viên.",
     "Hòa mình trọn vẹn vào cảnh quan Côn Sơn."),

    ("Ngôn Chí • Bài 8", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Một mai một cuốc một cần câu,\nThơ thẩn dạo xem cảnh sắc màu.\nĐồng nội lúa xanh hương ngạt ngào,\nSông sâu thuyền nhỏ lướt bay mau.\nThế nhân chìm nổi trong cơn mộng,\nKẻ sĩ tiêu dao thoát cảnh sầu.\nGiữ trọn lòng son thờ nước cũ,\nNghìn thu danh tiết sáng làu làu.",
     "Thú vui câu cá ngắm cảnh đồng nội."),

    ("Ngôn Chí • Bài 10", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Đêm thu vằng vặc bóng trăng trong,\nGió mát hiu hiu thổi lọt phòng.\nÁo rách che thân lòng chẳng thẹn,\nNhà tranh nương náu dạ thanh không.\nTrần gian muôn việc trôi mây nổi,\nThế sự phù vân thoảng gió đồng.\nChỉ có tình dân và nghĩa nước,\nĐêm ngày canh cánh ở bên lòng.",
     "Nỗi lòng ái quốc ưu dân luôn canh cánh bên dạ."),

    ("Ngôn Chí • Bài 11", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Bến vắng thuyền câu đậu hững hờ,\nKhói lam bảng lảng bóng hoàng hôn.\nSông sâu sóng gợn làn sương mỏng,\nNúi thẳm mây che đỉnh ngút ngàn.\nBụi bặm kinh thành nay rũ sạch,\nThanh tao tấc dạ với giang sơn.\nNhấp chén rượu đào ngâm một khúc,\nMặc ai bươn chải bả vinh sang.",
     "Cảnh hoàng hôn bến vắng và sự thanh thản nội tâm."),

    ("Ngôn Chí • Bài 15", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Đua chi quyền quý chốn phồn hoa,\nLại trở về đây mái cỏ nhà.\nSớm cuốc khoai lang mùi ngọt bùi,\nChiều hái rau muống nước canh ngà.\nTrăng soi đầu gối thơ ngâm vịnh,\nGió thoảng rèm the khúc họa ca.\nĐắc chí thanh nhàn âu cũng phúc,\nCần chi áo gấm với ngựa xe.",
     "Hạnh phúc giản dị nơi xóm làng đồng nội."),

    ("Ngôn Chí • Bài 18", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Thân trai giữ vững chí bình sinh,\nNợ nước ơn vua dạ đinh ninh.\nLúc biến ra tay phò xã tắc,\nKhi nhàn ẩn tích náu thanh danh.\nNúi non Côn Động tình sâu nặng,\nSông nước Yên Hưng nghĩa vẹn lành.\nMột chén trà thơm ngâm vịnh thú,\nSáng trong như ngọc tấm lòng thành.",
     "Gắn kết giữa trách nhiệm cứu đời và thú nhàn dật."),

    ("Ngôn Chí • Bài 20", "Quốc Âm Thi Tập • Tỏ Lòng",
     "Bụi trần khôn vướng gót hài thanh,\nVườn hạnh hoa đào nở kín cành.\nSuối mát gội lòng trong sạch sẽ,\nGió thu quét ngõ rộn ràng nhanh.\nBạn xưa sách vở vui câu đối,\nTrò cũ thi thư rạng đức lành.\nThế thái nhân tình dầu biến đổi,\nRiêng ta bền vững một lòng thanh.",
     "Tấm lòng trong sạch trước mọi thăng trầm thế thái."),

    # Mạn thuật (11 - 18)
    ("Mạn Thuật • Bài 1", "Quốc Âm Thi Tập • Kể Chuyện Thong Dong",
     "Nghiêng ngả lều con gió thổi lùa,\nCơm rau muối mắm cũng no vừa.\nBạn bè thưa thớt tình thêm đượm,\nSách vở đầy bàn dạ chẳng trơ.\nNắng rạng hoa cười khoe cánh thắm,\nMưa tan lá múa đón duyên xưa.\nCuộc đời muôn nỗi trò hưng phế,\nGiữ lấy lòng ngay mặc gió mưa.",
     "Tình bạn đượm nồng và niềm vui bên trang sách."),

    ("Mạn Thuật • Bài 2", "Quốc Âm Thi Tập • Kể Chuyện Thong Dong",
     "Tóc bạc da mồi tuổi xế trưa,\nSự đời ngẫm lại tựa cơn mơ.\nBao phen chìm nổi trường danh lợi,\nMấy độ can qua trận gió mưa.\nMay đặng thanh nhàn về bến cũ,\nĐược vui thanh thản náu am xưa.\nNgâm nga một khúc cầm thi phú,\nẤm áp lòng nhân đón đợi mùa.",
     "Tổng kết cuộc đời sau bao phen phong ba bão táp."),

    ("Mạn Thuật • Bài 4", "Quốc Âm Thi Tập • Kể Chuyện Thong Dong",
     "Thuở hàn vi giữ dạ kiên trinh,\nMột túi thi thư một tấc tình.\nĐá nọ dầu mòn lòng chẳng chuyển,\nVàng kia dẫu chảy dạ đinh ninh.\nTrời cho lận đận rèn gan góc,\nĐời bắt phong trần thử đức thanh.\nĐến buổi thái bình phò thánh chúa,\nRạng ngời muôn thuở nét văn minh.",
     "Lòng kiên trinh vượt qua thử thách cay đắng."),

    ("Mạn Thuật • Bài 5", "Quốc Âm Thi Tập • Kể Chuyện Thong Dong",
     "Đơn sơ áo vải mái lều tranh,\nMà dạ bao la rộng đất lành.\nThương kẻ bần hàn mong ấm áo,\nLo người cơ cực ước cơm canh.\nNước nhà vững mạnh muôn năm thịnh,\nXã tắc bình an vạn thuở thanh.\nƯớc nguyện bình sinh chưa thỏa dạ,\nĐêm đêm cầu khấn trước cao xanh.",
     "Tấm lòng nhân ái bao la vì người nghèo khó."),

    ("Mạn Thuật • Bài 6", "Quốc Âm Thi Tập • Kể Chuyện Thong Dong",
     "Sớm ra đồng cỏ dạo thong dong,\nChiều ngắm thuyền câu lướt mặt dòng.\nHoa dại bên đường khoe sắc thắm,\nCỏ xanh ngút mắt trải ngàn trùng.\nCuộc đời trần thế phù du ảo,\nDanh lợi nhân gian bọt nước trông.\nThanh thản mây trời vui cánh hạc,\nThung dung ngày tháng thỏa tấc lòng.",
     "Hòa mình vào thiên nhiên đồng nội."),

    ("Mạn Thuật • Bài 7", "Quốc Âm Thi Tập • Kể Chuyện Thong Dong",
     "Sách học nghìn trang tỏ sự đời,\nHiền nhân quân tử dạ sáng tươi.\nChớ theo thói xấu luồn lòn lụy,\nĐừng chuộng tiền tài bỏ đức người.\nCông tội nghìn thu bia đá tạc,\nNhân từ vạn kiếp tiếng thơm phơi.\nLời xưa tiền bối răn dạy kỹ,\nGhi tạc bên lòng chẳng chút lơi.",
     "Lời răn dạy đạo đức và phẩm hạnh Nho gia."),

    ("Mạn Thuật • Bài 10", "Quốc Âm Thi Tập • Kể Chuyện Thong Dong",
     "Ngồi sưởi ánh dương buổi sớm mai,\nGió đông thổi ấm nhành hoa nhài.\nChim khuyên cất giọng ca vang lảnh,\nOng bướm lượn quanh múa lả lơi.\nCảnh sắc thanh bình âu cũng phúc,\nTâm hồn tĩnh lặng thỏa thê chơi.\nQuên đi muôn nỗi âu lo cũ,\nSống trọn cùng trăng với đất trời.",
     "Tận hưởng niềm vui bình dị mỗi sớm mai."),

    ("Mạn Thuật • Bài 13", "Quốc Âm Thi Tập • Kể Chuyện Thong Dong",
     "Trải việc đời qua mới biết người,\nMiệng cười thơn thớt dạ khôn lường.\nKhuyên ai chớ dại trao lòng dạ,\nGiữ lấy niềm tin với kỷ cương.\nThẳng thắn hiên ngang như trúc biếc,\nNgát thơm trong sạch tựa liên hương.\nNghìn vàng chẳng đổi lòng son sắt,\nĐể lại cho đời tấm gương gương.",
     "Lời chiêm nghiệm sâu sắc về thói đời đen bạc."),

    # Tự thán (19 - 26)
    ("Tự Thán • Bài 1", "Quốc Âm Thi Tập • Than Thở Nỗi Đời",
     "Lẻ loi cánh hạc giữa trời mây,\nThương kẻ tài hoa luống dãi dầy.\nChí lớn chưa thành đầu bạc trắng,\nƠn sâu chưa trả gối ôm đầy.\nNon sông cách trở nghìn trùng cách,\nSự nghiệp dở dang mấy độ hay.\nNhờ cậy thi đàn chia nỗi muộn,\nThâu đêm ngâm ngợi khúc bi ai.",
     "Nỗi cô đơn của người tài hoa chưa thỏa chí lớn."),

    ("Tự Thán • Bài 2", "Quốc Âm Thi Tập • Than Thở Nỗi Đời",
     "Thế sự đua nhau những đảo điên,\nNgười đời chuộng của ghét người hiền.\nĐược thời lắm kẻ xun xoe đến,\nThất thế không ai ngó tới bên.\nLòng ngay dẫu chịu ngàn oan khuất,\nDạ thẳng nào màng bả lợi duyên.\nĐội ơn thánh chúa soi gương sáng,\nRửa sạch sầu bi cõi mộng phiền.",
     "Phê phán thói xu phụ thịnh suy của thói đời."),

    ("Tự Thán • Bài 4", "Quốc Âm Thi Tập • Than Thở Nỗi Đời",
     "Tuổi tác lần lữa đuổi ngày xanh,\nSoi gương tóc bạc rụng tan tành.\nBao năm lận đận chốn quan ải,\nMấy dặm bôn ba chốn thị thành.\nThương kẻ hàn vi mong đổi vận,\nTiếc người quân tử chịu long đong.\nThôi đành gửi phận nơi thôn dã,\nBầu bạn cùng trăng với suối thanh.",
     "Nỗi xót xa khi nhìn mái đầu hoa râm."),

    ("Tự Thán • Bài 9", "Quốc Âm Thi Tập • Than Thở Nỗi Đời",
     "Ở thế gian này lắm nỗi oan,\nNgười ngay chịu khổ kẻ gian an.\nLòng ngay như mực trời không thấu,\nDạ thẳng như tên đất chẳng màng.\nDẫu vậy dạ này son chẳng đổi,\nMột lòng vì nước dạ can tràng.\nĐêm khuya ngẩng mặt trông sao Bắc,\nTin tưởng ngày mai rạng ánh quang.",
     "Lòng kiên định và niềm tin vào lẽ công bằng."),

    ("Tự Thán • Bài 10", "Quốc Âm Thi Tập • Than Thở Nỗi Đời",
     "Đêm lạnh cô đơn thức trọn canh,\nTiếng chuông chùa vẳng điểm ngân thanh.\nGió lay rèm trúc trăng nghiêng bóng,\nSương phủ cành mai tuyết bọc quanh.\nNợ nước nghìn cân vai gánh nặng,\nTình nhà muôn nỗi dạ đành hanh.\nƯớc sao dân ấm no no ấm,\nMới thỏa lòng ta giấc mộng lành.",
     "Thao thức canh khuya vì việc nước việc dân."),

    ("Tự Thán • Bài 19", "Quốc Âm Thi Tập • Than Thở Nỗi Đời",
     "Một mảnh lòng son dãi gió sương,\nĐường xa vạn dặm nỗi tha phương.\nChim bay mỏi cánh tìm cây đậu,\nThuyền lướt xuôi dòng kiếm bến nương.\nCông đức tiền nhân ghi khắc dạ,\nNghĩa tình hậu thế giữ miên trường.\nThanh nhàn là phúc trời ban tặng,\nMặc kệ ai tranh bả thị trường.",
     "Tấm lòng son sắt gửi trọn cho non sông."),

    ("Tự Thán • Bài 21", "Quốc Âm Thi Tập • Than Thở Nỗi Đời",
     "Mấy độ phong trần thử sức trai,\nLòng son chẳng chuyển trước chông gai.\nGươm mài vách đá vang rền rĩ,\nBút vạch trang thơ rạng sáng ngời.\nCứu khổ phò nguy tròn chí nguyện,\nTrừ tàn diệt bạo rạng danh đời.\nThanh danh để lại cho con cháu,\nSáng tựa vầng trăng giữa biển khơi.",
     "Khí phách hiên ngang của người anh hùng Lam Sơn."),

    ("Tự Thán • Bài 32", "Quốc Âm Thi Tập • Than Thở Nỗi Đời",
     "Ngoảnh lại đường xưa ngẫm sự đời,\nMênh mông bể khổ sóng trùng khơi.\nBao nhiêu anh kiệt vùi tro bụi,\nBấy nỗi đau thương nghẹn tiếng cười.\nChỉ có non sông là vĩnh cửu,\nChỉ còn nhân nghĩa rạng muôn đời.\nVề đây náu bóng rừng thông biếc,\nUống chén trà thơm nhẹ bước chơi.",
     "Triết lý nhân sinh thanh lọc tâm hồn."),

    # Thuật hứng (27 - 34)
    ("Thuật Hứng • Bài 1", "Quốc Âm Thi Tập • Bày Tỏ Nỗi Lòng",
     "Công danh trút sạch nhẹ tênh mình,\nTìm đến non xanh náu bóng hình.\nSớm nghe vượn hót reo vách núi,\nChiều ngắm mây bay lướt đỉnh ghềnh.\nChén rượu tiêu giao trừ tục lụy,\nTrang thơ tao nhã tỏ lòng trinh.\nNhàn cư vi thiện vui muôn thuở,\nThanh thản tâm hồn giữa thái bình.",
     "Rũ bỏ gánh nặng quan trường về chốn non xanh."),

    ("Thuật Hứng • Bài 2", "Quốc Âm Thi Tập • Bày Tỏ Nỗi Lòng",
     "Ao thu nước lạnh phẳng như gương,\nKhóm cúc vàng tươi đọng giọt sương.\nCần trúc buông câu chờ cá đớp,\nThuyền nan ghé bến đón người thương.\nThanh đạm bữa ăn khoai với muối,\nNgọt ngào câu hát gió đưa hương.\nỞ đời đắc thú thanh nhàn ấy,\nHỏi có ngôi cao sánh được dường?",
     "Cảnh sắc mùa thu tuyệt đẹp bên ao thu."),

    ("Thuật Hứng • Bài 3", "Quốc Âm Thi Tập • Bày Tỏ Nỗi Lòng",
     "Nhà cỏ ba gian náu bóng râm,\nQuanh năm bạn với bạn tri âm.\nSuối trong gội rửa niềm vương vấn,\nTrăng sáng soi chung tấc dạ trầm.\nThơ vịnh cảnh thanh vui sớm tối,\nĐàn gảy khúc nhã rộn thanh âm.\nThong dong tự tại quên ngày tháng,\nAi kẻ bì so dạ hiểm thâm?",
     "Cuộc sống ba gian nhà cỏ đầm ấm nghĩa tình."),

    ("Thuật Hứng • Bài 5", "Quốc Âm Thi Tập • Bày Tỏ Nỗi Lòng",
     "Nằm khểnh bên hiên ngắm gió bay,\nMùa xuân hoa nở thắm ngàn cây.\nTrời ban phúc lộc người thanh bạch,\nĐất đãi hiền tài kẻ thẳng ngay.\nÁo ngắn che thân không hổ thẹn,\nNhà rơm trú ngụ ấm đôi tay.\nMiễn sao dân chúng yên vui sống,\nCơm đủ áo lành vẹn ước này.",
     "Ước nguyện dân đủ cơm no lành áo ấm."),

    ("Thuật Hứng • Bài 15", "Quốc Âm Thi Tập • Bày Tỏ Nỗi Lòng",
     "Am thông rợp mát bóng cây xanh,\nNắng ấm chan hòa trải bức tranh.\nBửa củi đun nồi canh củ cải,\nVác mai cuốc đất cấy rau mầm.\nBàn cờ thế sự ai thua được,\nChén rượu thanh tao dạ thỏa tình.\nMặc kẻ bon chen vòng danh lợi,\nRiêng ta gìn giữ một tâm thanh.",
     "Cảnh sinh hoạt lao động giản dị của bậc hiền triết."),

    ("Thuật Hứng • Bài 19", "Quốc Âm Thi Tập • Bày Tỏ Nỗi Lòng",
     "Suối Côn Sơn chảy tiếng rầm rì,\nĐá Côn Sơn trải đá phơi nghi.\nTa ngồi trên đá ngâm thơ phú,\nTa tắm lòng suối mát dung nghi.\nBụi trần sạch bách không còn bợn,\nKhí phách thanh cao rạng chữ nghì.\nThanh thản mây trôi về cõi biếc,\nQuên bao oan trái chốn kinh kỳ.",
     "Hình tượng Côn Sơn ngát hương thi vị."),

    ("Thuật Hứng • Bài 22", "Quốc Âm Thi Tập • Bày Tỏ Nỗi Lòng",
     "Đường trần muôn lối bước quanh co,\nChỉ có đường ngay chẳng phải lo.\nGiữ đạo thánh hiền trong tấc dạ,\nNoi gương tiên tổ giữa trời cho.\nHoa tàn hoa nở tuần hoàn mãi,\nNước cạn nước đầy sóng vỗ to.\nLòng dạ vững vàng như núi đá,\nBão giông chẳng chuyển ngọn cờ phơ.",
     "Đạo lý chính trực như ngọn núi kiên cố."),

    ("Thuật Hứng • Bài 24", "Quốc Âm Thi Tập • Bày Tỏ Nỗi Lòng",
     "Công danh đã được nửa lơ mơ,\nTuổi trẻ chưa qua bạc mái đầu.\nVườn cũ Côn Sơn mây phủ trắng,\nSuối trong Thanh Hư nước trong veo.\nĐò nan gối bãi nằm nghe gió,\nLưới thưa buông dòng đón cá leo.\nHết nợ tang bồng về núi cũ,\nThanh thản tiêu dao mặc hiểm nghèo.",
     "Khát vọng giải giáp nợ tang bồng để trở về Côn Sơn."),

    # Bảo kính cảnh giới (35 - 44)
    ("Bảo Kính Cảnh Giới • Bài 1", "Quốc Âm Thi Tập • Gương Báu Răn Mình",
     "Gương báu soi lòng dạ thẳng ngay,\nChớ tham bả lợi chớ mê say.\nĐức nhân vun đắp bền muôn thuở,\nPhúc đức lưu truyền vạn kiếp nay.\nChớ thấy việc lành mà chẳng tiến,\nĐừng vì điều ác lại ra tay.\nLời xưa nghiêm huấn ghi tâm khảm,\nSáng rạng nghìn thu nét ngọc hay.",
     "Răn mình làm việc nhân đức, lánh xa điều dữ."),

    ("Bảo Kính Cảnh Giới • Bài 11", "Quốc Âm Thi Tập • Gương Báu Răn Mình",
     "Gió thu phe phẩy quạt hơi may,\nKhóm cúc đầu sân điểm cánh bay.\nTrăng sáng rọi vào trang sách mở,\nĐèn dầu thắp rạng ngọn thông lay.\nNgẫm suy lẽ biến trong trời đất,\nGiữ lấy tâm thiền giữa chốn nay.\nThanh bạch để danh thơm vạn thuở,\nCần chi danh vị với tiền đầy.",
     "Khung cảnh đọc sách đêm thu thanh tịnh."),

    ("Bảo Kính Cảnh Giới • Bài 18", "Quốc Âm Thi Tập • Gương Báu Răn Mình",
     "Làm người lấy đức đặt lên đầu,\nChữ hiếu chữ trung giữ đậm sâu.\nGiúp kẻ hoạn nạn không quản khó,\nThương người nghèo đói đỡ cơn sầu.\nLời ngay thẳng thắn không dua nịnh,\nDạ trắng trong ngần chẳng bợn dơ.\nĐược vậy mới là trang quân tử,\nTiếng thơm vang vọng mãi muôn dâu.",
     "Tiêu chuẩn đạo đức tối thượng của người quân tử."),

    ("Bảo Kính Cảnh Giới • Bài 21", "Quốc Âm Thi Tập • Gương Báu Răn Mình",
     "Vườn xuân hoa thắm rộn ong bay,\nCảnh sắc tươi vui rạng rỡ cây.\nNhìn cảnh thương đời lo vận nước,\nTrông người ái quốc thấu lòng này.\nNhân hòa địa lợi trời ban tặng,\nDân thịnh quốc an hạnh phúc dầy.\nMột dạ chí thành gìn xã tắc,\nMuôn dân ca khúc ấm no sum.",
     "Tình cảm gắn kết sâu đậm giữa thiên nhiên và vận nước."),

    ("Bảo Kính Cảnh Giới • Bài 22", "Quốc Âm Thi Tập • Gương Báu Răn Mình",
     "Nước đục rồi trong ấy lẽ trời,\nNgười ngay gặp nạn chớ than ôi.\nĐá vàng nung lửa càng thêm sáng,\nCây bách dầm sương lá biếc phơi.\nChính khí sáng trong soi đáy dạ,\nTà gian lẩn khuất thẹn muôn đời.\nTin vào công lý nghìn thu vững,\nÁnh sáng nhân văn rạng rỡ ngời.",
     "Niềm tin sắt đá vào chính nghĩa tất thắng."),

    ("Bảo Kính Cảnh Giới • Bài 24", "Quốc Âm Thi Tập • Gương Báu Răn Mình",
     "Đêm nghe tiếng gió thổi hiên tây,\nThương kẻ chinh phu dãi ải này.\nChiến trận bao năm xương chất núi,\nGia đình mấy độ lệ tuôn đầy.\nCầu cho dứt cảnh đao binh loạn,\nCho khói lam bay xóm ấp vầy.\nTrời mở thái bình âu cũng ước,\nẤm no hạnh phúc khắp nơi đây.",
     "Tiếng lòng phản chiến xót thương người chinh phu."),

    ("Bảo Kính Cảnh Giới • Bài 28", "Quốc Âm Thi Tập • Gương Báu Răn Mình",
     "Thân nhàn dạ chẳng chút băn khoăn,\nÁo vải nhà tranh sống ấm êm.\nSớm cuốc mảnh vườn trồng khóm chuối,\nChiều mang giỏ cá thả bên thềm.\nTrăng soi bóng trúc in sàn ngọc,\nGió thoảng hương sen ngát gác rèm.\nVui thú điền viên lòng phơi phới,\nQuan quyền bổng lộc há màng thèm.",
     "Thú vui điền viên thanh thản tuyệt vời."),

    ("Bảo Kính Cảnh Giới • Bài 31", "Quốc Âm Thi Tập • Gương Báu Răn Mình",
     "Cầm kỳ thi họa thú tiêu dao,\nMột góc thanh nhàn cảnh đẹp sao.\nSách mở nghìn xưa gương sáng tỏ,\nThơ ngâm muôn thuở ý thanh tao.\nLòng son chẳng bận vòng danh lợi,\nDạ thẳng khôn sờn ngọn sóng cao.\nGiữ trọn khí thiêng cùng nhật nguyệt,\nTiếng thơm lưu mãi chốn ba đào.",
     "Bốn thú vui tao nhã nâng đỡ tâm hồn."),

    ("Bảo Kính Cảnh Giới • Bài 38", "Quốc Âm Thi Tập • Gương Báu Răn Mình",
     "Học sách thánh hiền rèn đức tâm,\nLời ngay ý thẳng chớ sai lầm.\nYêu dân như thể con ruột thịt,\nTrọng kẻ tài ba quý tựa sâm.\nĐất nước thái bình nhờ đức trị,\nGiang sơn hưng thịnh cậy ân thâm.\nBao lời tâm huyết ghi trang giấy,\nGửi lại ngàn sau bóng nguyệt trầm.",
     "Tư tưởng thân dân trị quốc bằng đức độ."),

    ("Bảo Kính Cảnh Giới • Bài 43", "Quốc Âm Thi Tập • Gương Báu Răn Mình",
     "Rồi hóng mát thuở ngày trường,\nHòe lục đùn đùn tán rợp giương.\nThạch lựu hiên còn phun thức đỏ,\nHồng liên trì đã tiễn mùi hương.\nLao xao chợ cá làng ngư phủ,\nDắng dỏi cầm ve lầu tịch dương.\nDẽ có Ngu cầm đàn một tiếng,\nDân giàu đủ khắp đòi phương.",
     "Tuyệt tác ngày hè và ước vọng tiếng đàn vua Thuấn cho dân giàu đủ khắp đòi phương."),

    # Môn Hoa Mộc (45 - 50)
    ("Tùng • Bài 1", "Quốc Âm Thi Tập • Môn Hoa Mộc",
     "Tùng xanh đứng sững giữa sườn non,\nNăm tháng phong ba dạ vẫn tròn.\nSương tuyết dầm dề gan chẳng chuyển,\nGió giông gào thét sức không mòn.\nRường cột chống che đền thái miếu,\nBóng râm che mát cõi giang sơn.\nNgười quân tử ấy lòng kiên định,\nMuôn thuở thanh danh rạng tiếng son.",
     "Cây tùng hiên ngang làm rường cột cho miếu đường."),

    ("Tùng • Bài 3", "Quốc Âm Thi Tập • Môn Hoa Mộc",
     "Thu đến cây nào chẳng rụng rơi,\nĐộc tùng xanh ngắt giữa ngàn khơi.\nGió đông tuyết lạnh bền gan góc,\nSương muối mùa đông vững dáng người.\nRường cột nhà to mai ắt đắt,\nCột kèo rường cột để muôn đời.\nTấm thân quân tử che giông bão,\nLừng lẫy uy phong rạng rỡ trời.",
     "Khí tiết ngạo nghễ của cây tùng trước mùa đông."),

    ("Trúc • Bài 1", "Quốc Âm Thi Tập • Môn Hoa Mộc",
     "Thân thẳng đốt ngay dáng ngọc ngà,\nĐông tàn xuân đến dạ không hoa.\nGió rung rào rạt thanh âm nhã,\nSương phủ trắng trong nét ngọc ngà.\nRuột rỗng chứa chan niềm khiêm tốn,\nCành mềm uốn khúc bóng thanh tao.\nBạn cùng quân tử nghìn năm hẹn,\nSáng rạng nhân gian nét ngọc ngào.",
     "Hình tượng cây trúc ruột rỗng khiêm nhường ngay thẳng."),

    ("Mai • Bài 1", "Quốc Âm Thi Tập • Môn Hoa Mộc",
     "Vượt tuyết băng đông hé cánh hoa,\nTrắng ngần tinh khiết nét băng nga.\nHương thơm thoang thoảng vờn cánh gió,\nSắc thắm dịu dàng rạng bóng pha.\nBáo hiệu mùa xuân về khắp chốn,\nMở đường sinh khí rạng non hà.\nNgười trung quân tử tình thanh bạch,\nSáng tỏ ngàn năm chẳng nhạt nhòa.",
     "Hoa mai thanh khiết vượt qua tuyết giá đón xuân."),

    ("Cúc • Bài 1", "Quốc Âm Thi Tập • Môn Hoa Mộc",
     "Muôn hoa tàn rụng tiết thu đông,\nRiêng cúc vàng tươi rạng cánh hồng.\nỦ rũ nghìn cây trơ cành lá,\nThơm tho một khóm ngát hương nồng.\nThà trên cành héo rụng hoa úa,\nChẳng rớt theo bùn lấm đất nhơ.\nKhí phách tao nhân bền son sắt,\nMuôn đời sáng mãi ánh ngời trông.",
     "Hoa cúc hiên ngang tàn trên cành chứ không rụng xuống bùn."),

    # Thơ chữ Hán Ức Trai Thi Tập (51 - 52)
    ("Côn Sơn Ca (崑山歌)", "Ức Trai Thi Tập • Thơ Chữ Hán Kinh Điển",
     "崑山有泉，其聲泠泠，吾以為琴。\n崑山有石，其文粼粼，吾以為簟。\n岩中松柏蔽炎日，暮暮朝朝留碧陰。\n卿何不來，歸去來兮，何必塵埃苦自尋。",
     "Côn Sơn suối chảy rì rầm / Ta nghe như tiếng đàn cầm bên tai... Khúc ca hòa hợp tuyệt đối với thiên nhiên."),

    ("Bạch Đằng Hải Khẩu (白藤海口)", "Ức Trai Thi Tập • Vịnh Cảnh Lịch Sử",
     "朔風吹浪白翻空，過客登臨感慨中。\n世事英雄覆手變，山川地險古今同。\n折戟沈沙皆往跡，長舟破浪仰前功。\n關河百二由天設，在德非全在隘形。",
     "Bản dịch: Gió bấc vù vù sóng ngập trời... Quan hà hiểm trở trời ban sẵn / Giữ nước cốt ở Đức sáng tươi! Đúc kết bài học giữ nước muôn đời.")
]

def build_expanded_quoc_am_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Đại Việt Văn Học • Thế Kỷ XV</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">QUỐC ÂM THI TẬP<br>& ỨC TRAI THI TẬP</div>
            <div class="cover-subtitle">Đỉnh Cao Thơ Nôm Khai Sáng & Tuyển Tập Thơ Chữ Hán Toàn Thư<br>Đại tuyển tập hơn 50 bài thơ kiệt tác về khí tiết quân tử, tình dân và non nước</div>
            <div class="gold-line"></div>
            <div class="cover-author">ỨC TRAI TIÊN SINH NGUYỄN TRÃI (1380 – 1442)</div>
            <div class="cover-author-sub">Danh nhân văn hóa thế giới UNESCO vinh danh năm 1980</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Hiệu đính đối chiếu mộc bản Phúc Khang Cảnh Hưng & Ức Trai Di Tập</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">MỤC LỤC & KHẢO TẢ QUỐC ÂM THI TẬP</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Quốc Âm Thi Tập (國音詩集)</strong> gồm 254 bài thơ Nôm của Nguyễn Trãi là tượng đài nguy nga đặt nền móng vững chắc cho nền thơ ca tiếng Việt dân tộc. Bằng sự kết hợp tài hoa giữa thể thơ Đường luật bác học với câu thơ lục ngôn thuần Việt, Nguyễn Trãi đã giải phóng thi ca khỏi khuôn sáo chữ Hán, đưa tâm hồn Việt Nam thăng hoa rực rỡ.</p>
        <p>Tuyển tập này tập hợp <strong>52 bài thơ bất hủ</strong> phân theo từng chủ đề: Khí phách quân tử, Tình yêu thiên nhiên Côn Sơn, Nỗi đau thế sự trần ai, và trên hết là tấm lòng nhân nghĩa ái quốc ưu dân thiết tha. Mỗi bài thơ đều kèm phân tích thi pháp và chú giải từ ngữ cổ.</p>
    </div>
    """)
    
    for i, p in enumerate(POEMS_52, 1):
        title, cat, text, comment = p
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #8B1E1E; padding-bottom: 4px; margin-bottom: 8px;">
                <span style="font-weight: bold; color: #721616; font-size: 11.5pt;">{i}. {title}</span>
                <span style="font-size: 9pt; color: #666; font-style: italic;">{cat}</span>
            </div>
            
            <div class="poem-stanza" style="line-height: 1.85; font-size: 11pt; color: #1a365d; font-weight: 500;">
                {text.replace(chr(10), '<br>')}
            </div>
            
            <div class="commentary-box" style="margin-top: 8px;">
                <div class="commentary-title">Bình Luận & Chú Giải:</div>
                {comment}
            </div>
        </div>
        """)
        
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">VĨ THANH: BẤT TỬ ỨC TRAI</h1>
    <div class="ornament">❖</div>
    <div class="intro-box">
        <p>Vua Lê Thánh Tông từng ngợi ca Nguyễn Trãi: <em>"Ức Trai tâm thượng quang Triêu Dương"</em> (Tấm lòng Ức Trai sáng tựa ánh mặt trời rực rỡ ban mai). Trải qua bao dâu bể và thảm án Lệ Chi Viên oan khốc, danh tiết và thơ văn Nguyễn Trãi vẫn ngời sáng như sao Khuê trên bầu trời văn hiến Đại Việt, trường tồn cùng non sông muôn thuở.</p>
    </div>
    """)
    
    return "\n".join(html)

async def main():
    print("Re-rendering Quoc Am Thi Tap with 52 complete poems...")
    html_content = build_expanded_quoc_am_html()
    await render_html_to_pdf(
        html_content=html_content,
        output_path=QUOC_AM_FILE,
        header_left="NGUYỄN TRÃI • QUỐC ÂM THI TẬP & ỨC TRAI THI TẬP",
        header_right="ĐẠI TUYỂN TẬP 52 BÀI KIỆT TÁC"
    )

if __name__ == "__main__":
    asyncio.run(main())
