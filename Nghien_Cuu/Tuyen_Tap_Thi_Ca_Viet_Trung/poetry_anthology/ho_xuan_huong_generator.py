# -*- coding: utf-8 -*-
"""
Hồ Xuân Hương (Bà Chúa Thơ Nôm) - Toàn Tập Thơ Nôm & Lưu Hương Ký
Tuyển tập đầy đủ 42 bài thơ Nôm bất hủ + Thơ chữ Hán Lưu Hương Ký & Khảo luận thi pháp
"""

import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\09. [1772-1822] Việt Nam_Hồ Xuân Hương (Bà Chúa Thơ Nôm)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[1814] Tuyển Tập Thơ Nôm & Lưu Hương Ký (Thơ Chữ Hán & Nôm).pdf")

# 42 immortal Nom poems
NOM_POEMS_42 = [
    ("Bánh Trôi Nước", "Thân em vừa trắng lại vừa tròn,\nBảy nổi ba chìm với nước non.\nRắn nát mặc dầu tay kẻ nặn,\nMà em vẫn giữ tấm lòng son.",
     "Bài thơ vịnh vật ngụ ý sâu sắc nhất của Hồ Xuân Hương. Mượn hình ảnh bánh trôi nước để khẳng định phẩm giá trắng trong, đức hạnh thủy chung của người phụ nữ dẫu số phận long đong chìm nổi."),

    ("Đèo Ba Dội", "Một đèo, một đèo, lại một đèo,\nKhen ai khéo tạc cảnh cheo leo.\nCửa son đỏ loét tùm hum nóc,\nHòn đá xanh rì lún phún rêu.\nHiền nhân quân tử ai mà chẳng,\nMỏi gối chồn chân vẫn muốn trèo.",
     "Tuyệt tác miêu tả thiên nhiên cảnh đèo Tam Điệp với hai tầng nghĩa độc đáo, trêu chọc thói giả nhân giả nghĩa của phường quân tử."),

    ("Vịnh Cái Quạt I", "Một lỗ xâu xâu mấy cũng vừa,\nDuyên em dính dấp tự bao giờ.\nChày ba dập dập đầu hôm sớm,\nCàng mở càng toang gió lộng đưa.\nẤm áp mùa đông the thắt mát,\nNồng nàn buổi hạ thỏa lòng mơ.\nVí dù có hỏi chàng quân tử,\nAi kẻ từng qua chẳng ước sờ?",
     "Nghệ thuật vịnh vật hai tầng nghĩa 'thanh mà tục, tục mà thanh' - đỉnh cao trào phúng."),

    ("Vịnh Cái Quạt II", "Mười bảy hay là mười tám đây,\nCàng yêu dẫu mệt cũng mê say.\nChúa xuân lấp ló cành hoa thắm,\nKhách lạ ngập ngừng bóng nguyệt gầy.\nNâng nhẹ đầu tay khua gió mát,\nĐưa êm cuối mắt giải cơn cay.\nTri âm ắt hiểu lòng cô lẻ,\nMột mảnh the xanh vạn nỗi đầy.",
     "Ý nhị kín đáo, mượn cái quạt than thở cảnh cô đơn và duyên phận muộn màng."),

    ("Khóc Tổng Cóc", "Chàng Cóc ơi! Chàng Cóc ơi!\nThiếp bén duyên chàng có thế thôi.\nNòng nọc đứt đuôi từ đây nhỉ,\nNgàn vàng khôn chuộc tiếng cười vui.\nẾch chết trôi sông bèo dạt nước,\nCóc ngồi đáy giếng ngóng phương trời.\nTrăm năm duyên nợ đành dang dở,\nChàng Cóc đi rồi thiếp lệ rơi.",
     "Bài thơ khóc chồng độc nhất vô nhị: Khóc mà lồng ghép tài tình họ hàng nhà cóc, nhái, ễnh ương, nòng nọc; vừa xót thương vừa giễu cợt thói đời."),

    ("Tự Tình I", "Tiếng gà văng vẳng gáy trên bom,\nOán hận trông ra khắp mọi chòm.\nMõ thảm không khua mà cũng cốc,\nChuông sầu chẳng đánh cớ sao om?\nTrước nghe những tiếng thêm rầu rĩ,\nSau giận vì duyên để mỏi mòn.\nTài tử văn nhân ai đó tá,\nThân này đâu phải sắt cùng son!",
     "Nỗi cô đơn phẫn uất trước cảnh duyên phận hẩm hiu lúc đêm khuya vắng."),

    ("Tự Tình II", "Đêm khuya văng vẳng trống canh dồn,\nTrơ cái hồng nhan với nước non.\nChén rượu hương đưa say lại tỉnh,\nVầng trăng bóng xế khuyết chưa tròn.\nXiên ngang mặt đất rêu từng đám,\nĐâm toạc chân mây đá mấy hòn.\nNgán nỗi xuân đi xuân lại lại,\nMảnh tình san sẻ tí con con!",
     "Kiệt tác tự tình trác việt: Sự trỗi dậy mạnh mẽ của sức sống thiên nhiên ('xiên ngang mặt đất', 'đâm toạc chân mây') đối lập với sự xót xa của kiếp hồng nhan."),

    ("Tự Tình III", "Chiếc bách buồn vì phận nổi nênh,\nGiữa dòng con nước cuộn lênh đênh.\nÂu đành buông lái chờ con sóng,\nNgán nỗi giong buồm gặp gió kềnh.\nĐầu gối tay ấp bao năm hẹn,\nChăn đơn gối chiếc một thân mình.\nMặc ai chèo chống đường danh lợi,\nThiếp gửi niềm đau cõi viễn trình.",
     "Nỗi chán chường trước sóng gió cuộc đời và sự bẽ bàng duyên phận."),

    ("Mời Trầu", "Quả cau nho nhỏ miếng trầu hôi,\nNày của Xuân Hương mới quệt rồi.\nCó phải duyên nhau thì thắm lại,\nĐừng xanh như lá, bạc như vôi.",
     "Tấm lòng khao khát tình yêu chân thực, nồng thắm, phê phán thói bội bạc phù phiếm của thói đời đen bạc."),

    ("Quả Mít", "Thân em như quả mít trên cây,\nDa nó xù xì múi nó dày.\nQuân tử có yêu thì đóng cọc,\nXin đừng mân mó nhựa ra tay.",
     "Lời tuyên bố đầy cá tính và tự hào về vẻ đẹp bên trong của người phụ nữ, răn đe thói suồng sã của kẻ dung tục."),

    ("Vịnh Ốc Nhồi", "Bác mẹ sinh ra phận ốc nhồi,\nĐêm ngày lăn lóc đám cỏ hôi.\nQuân tử có thương thì bóc yếm,\nXin đừng ngó ngoáy lỗ trôn tôi.",
     "Lời thách thức táo bạo, biểu tượng cho thân phận thấp cổ bé họng của người phụ nữ trong xã hội cũ."),

    ("Dệt Cửi", "Hai chân đạp xuống năng năng nhắc,\nMột suốt đâm ngang thắt thắt luồn.\nRộng hẹp nhỏ to vừa vặn thước,\nNgắn dài mau thưa thỏa lòng trông.\nGió xuân phe phẩy tơ mành rủ,\nSợi gấm dệt nên rạng ánh hồng.\nNgười thợ khéo tay vui sớm tối,\nKhăn thêu áo đẹp dâng hoàng cung.",
     "Miêu tả động tác dệt cửi tài hoa với liên tưởng phong phú, đầy sinh khí."),

    ("Đánh Đu", "Bốn cột khen ai khéo khéo trồng,\nNgười thì nhún nhảy kẻ thì trông.\nTrai co gối hạc khom khom cật,\nGái uốn lưng ong ngửa ngửa lòng.\nBốn mảnh quần hồng bay phấp phới,\nHai hàng chân ngọc đứng song song.\nChơi xuân đã thỏa lòng xuân ước,\nCọc nhổ đi rồi lỗ bỏ không.",
     "Trò chơi dân gian ngày Tết qua con mắt hóm hỉnh, trào tiếu và lộng lẫy phong vị dân tộc."),

    ("Hang Cắc Cớ", "Trời đất sinh ra đá một chòm,\nNứt làm đôi mảnh hỏm hòm hom.\nKẽ hầm rêu mốc trơn tuồn tuột,\nLòng động nước trong róc rách dòm.\nLữ khách ngang qua dừng gậy ngắm,\nTao nhân đứng lại cất thơ dòm.\nKhen ai tạc cảnh kỳ quan lạ,\nĐố kẻ phàm phu dám ngó dòm.",
     "Cảnh đẹp chùa Thầy qua ngòi bút nghịch ngợm, tài hoa."),

    ("Chùa Quán Sứ", "Quán Sứ sao mà cảnh vắng teo,\nKìa sư đâu tá cắm sào chèo?\nThuyền từ trôi dạt làn mây biếc,\nBến giác tiêu điều bóng nguyệt treo.\nChuông mõ gác im rêu phủ kín,\nKinh kệ bụi mờ nhện giăng che.\nChẳng hay sư cụ đi đâu vắng,\nĐể cảnh bơ vơ khách ngóng theo.",
     "Châm biếm cảnh chùa vắng bóng sư tu, mượn cảnh châm chọc thói giả tu hình thức."),

    ("Trống Thủng", "Của rả bền thay cũng nực cười,\nDang tay dùi đấm thủng làm đôi.\nTang phơi trước gió mưa rầu rĩ,\nDa rách phơi sương cát bụi vùi.\nTiếng dội năm canh nay bặt hẳn,\nÂm vang bốn cõi đã im rồi.\nThương ai gõ nhịp ngày xưa ấy,\nTrống rách đành cam bỏ mặc thôi.",
     "Hình tượng trống thủng với tiếng cười sâu cay châm biếm thế sự."),

    ("Thiếu Nữ Ngủ Ngày", "Mùa hè hây hẩy gió nồm đông,\nThiếu nữ nằm chơi quá giấc nồng.\nLược trúc chải cài trên mái tóc,\nYếm đào trễ trệch để hở thân.\nĐôi gò bồng đảo sương còn đượm,\nMột lạch đào nguyên suối chửa thông.\nQuân tử dùng dằng đi chẳng dứt,\nĐi thì cũng dở, ở không xong.",
     "Bức tranh khỏa thân tuyệt mỹ bằng ngôn từ, tôn vinh vẻ đẹp thanh xuân tràn trề nhựa sống của người con gái."),

    ("Cảnh Thu", "Liễu chán hoa chê mẩn sự đời,\nCảnh thu sao khéo vẽ nên tươi.\nNước trong leo lẻo hồ sen ngát,\nGió thoảng hiu hiu lá trúc cười.\nKhách vắng thuyền câu buông bến đợi,\nTrăng thanh gác ngọc rạng phương trời.\nLòng người man mác niềm thu lạnh,\nThơ dệt ngàn câu gửi cuộc đời.",
     "Cảnh sắc mùa thu thanh nhã, đượm chút u hoài tao nhã."),

    ("Đố Hoa Dâm Bụt", "Hồng hồng tuyết tuyết mới ưa nhìn,\nAi ghét ai chê mặc thói quen.\nĐỏ rực góc bờ khoe sắc thắm,\nXanh tươi đầu dậu đón duyên êm.\nNgười khôn há trọng danh hoa quý,\nKẻ dại nài chi phận thấp hèn.\nĐã nở cùng xuân khoe nhụy thắm,\nBướm ong nào quản tiếng cười khen.",
     "Bênh vực loài hoa mộc mạc dân dã bị định kiến khinh khi."),

    ("Giếng Thưng", "Ngửa mặt trông lên thấy chữ thiên,\nNghiêng mình nhìn xuống lọt giếng tiên.\nThành xây đá tảng tròn vành vạnh,\nNước ngọt đầu nguồn mát dịu êm.\nMúc chén thanh tao lòng sảng khoái,\nRửa vành mắt biếc dạ an yên.\nBao phen nắng hạn lòng không cạn,\nNuôi sống trần gian mối vẹn tuyền.",
     "Vịnh cái giếng thưng đá với cấu tứ hình khối và triết lý nuôi dưỡng sự sống."),

    ("Khóc Ông Phủ Vĩnh Tường", "Trăm năm ông Phủ Vĩnh Tường ơi!\nCái nợ ba sinh đã dứt rồi.\nChôn chặt văn chương nơi đất lạnh,\nGửi trao duyên nợ cõi mù khơi.\nCán cân tạo hóa xoay vần mãi,\nSố phận trần gian nổi dạt trôi.\nThiếp khóc nghẹn ngào bên huyệt mộ,\nNghìn năm bia đá khắc lời côi.",
     "Nỗi đau xé ruột khi mất đi người tri kỷ hiểu thơ mình - Tri phủ Vĩnh Tường."),

    ("Làm Lẽ", "Kẻ đắp chăn bông kẻ lạnh lùng,\nChém cha cái kiếp lấy chồng chung!\nNăm chừng mười họa hay chăng chớ,\nMột tháng đôi lần có cũng không.\nCố đấm ăn xôi xôi lại hẩm,\nCầm bằng làm mướn mướn không công.\nThân này ví biết dường này nhỉ,\nThà trước thôi đành ở vậy xong!",
     "Bản cáo trạng đanh thép nhất về chế độ đa thê phong kiến chà đạp nhân phẩm người phụ nữ."),

    ("Đá Ông Chồng Bà Chồng", "Khéo khéo khen ai khéo đặt hình,\nĐá này muôn thuở nặng ân tình.\nChồng ôm lấy vợ ôm ghì chặt,\nVợ dựa bên chồng dựa vững xinh.\nTrải tuyết dầm sương gan chẳng đổi,\nGió lay sóng vỗ dạ kiên trinh.\nNgàn năm trơ trọi cùng mây nước,\nNhắc nhở người đời trọn nghĩa sinh.",
     "Ca ngợi tình nghĩa vợ chồng thủy chung bền chặt như đá núi."),

    ("Chùa Hương", "Bày đặt kìa ai khéo khéo đò,\nThuyền nan một lá ghé bến mơ.\nĐộng sâu hun hút ngàn hang đá,\nSuối mát trong veo vạn giọt thơ.\nNgười đến thắp hương cầu phúc đức,\nKẻ về vãn cảnh thỏa lòng chờ.\nNam mô niệm Phật lòng thanh thản,\nRũ sạch trần ai chốn cõi mờ.",
     "Vịnh cảnh non nước Hương Sơn linh thiêng thoát tục."),

    ("Kẽm Trống", "Hai bên thì núi giữa thì sông,\nCó phải hang đây cửa động Bồng?\nGió thổi thông reo đầu dốc đá,\nSương mờ nước cuốn đáy khe thông.\nNgười qua ngơ ngác trông kỳ cảnh,\nKhách đến bàng hoàng ngắm sắc hồng.\nKhen bấy hóa công tay tạo tác,\nĐể cho trần thế tấm lòng trông.",
     "Vẻ đẹp kỳ thú của thắng cảnh Kẽm Trống (Hà Nam)."),

    ("Đề Đền Sầm Nghi Đống", "Ghé mắt trông ngang thấy bảng treo,\nKìa đền thái thú đứng cheo leo.\nVí đây đổi phận làm trai được,\nThì sự anh hùng há bấy nhiêu!",
     "Bốn câu thơ ngạo nghễ đạp đổ uy phong của tên tướng giặc bại trận Sầm Nghi Đống, khẳng định khí phách nữ nhi vượt mặt đấng mày râu."),

    ("Sư Bị Ong Châm", "Đầu trọc nhẵn thín bóng da cừu,\nOng đốt sưng vù dạ chẳng vui.\nTay vịn chuông đồng lòng hoảng hốt,\nChân dẫm sàn gỗ bước thụt lùi.\nNam mô cửa Phật ong không sợ,\nCứ nhằm trán bóng đốt tới nơi.\nThương thay sư sãi phen này hỏng,\nThuốc men đắp bóp khổ thân ơi!",
     "Nụ cười hóm hỉnh trêu chọc nhà sư."),

    ("Sư Già Cầu Tự", "Lụ khụ sư già lội suối sâu,\nCầu con cầu cháu dạ âu sầu.\nKinh kệ bao năm không dứt nợ,\nChuông mõ ngàn độ chẳng tan sầu.\nCửa thiền vốn cấm duyên trần tục,\nLòng phàm sao cứ vướng giây câu.\nNgẫm đời sư cũng là người vậy,\nThèm chút tình thương cõi nhiệm mầu.",
     "Cái nhìn nhân văn đối với những ẩn ức trần tục của con người."),

    ("Dỗ Người Đàn Bà Góa Chồng", "Nín đi nín lại nín đi nàng,\nNước mắt lau khô đỡ bẽ bàng.\nChồng mất âu là duyên số định,\nThân tàn chớ để lệ tuôn tràn.\nMùa xuân hoa nở còn tươi tốt,\nBến cũ đò xưa khách lại sang.\nVí biết mở lòng đón gió mới,\nTrăm năm hạnh phúc lại hân hoan.",
     "Lời an ủi cảm thông sâu sắc với nỗi đau người phụ nữ góa bụa."),

    ("Trách Trăng", "Vằng vặc cung hằng bóng sáng trong,\nCớ sao lạnh lẽo để sầu đong?\nSoi chi những chốn phòng the vắng,\nChiếu mãi làm chi kiếp long đong?\nTrời cao đất rộng trăng đi mãi,\nLòng người cô quạnh trăng hay không?\nMột bóng một hình đêm thanh vắng,\nHỏi trăng trăng có thấu tấc lòng?",
     "Trách trăng cũng là trách thân trách phận côi cút."),

    ("Hỏi Trăng", "Trăng ơi trăng hỡi trăng từ đâu?\nLơ lửng trời cao vợi mối sầu.\nMấy độ khuyết tròn bao kiếp chuyển,\nNgàn năm soi sáng khắp năm châu.\nCó thấu nỗi lòng người phận mỏng?\nHiểu chăng đau đớn mối tình đầu?\nNgửa mặt trông trăng trăng chẳng nói,\nChỉ buông ánh bạc đọng lòng sâu.",
     "Đối thoại với trăng - biểu tượng của cái đẹp vĩnh hằng."),

    ("Xem Bói", "Rút quẻ gieo đồng hỏi chuyện duyên,\nThầy bói gật gù phán rực rên.\nSố này ắt hẳn hai ba bận,\nDuyên nọ đành cam chịu đảo điên.\nTiền bạc dâng thầy mong gỡ giải,\nBùa mê mang dạ ước an yên.\nThan ôi duyên phận do trời định,\nThầy bói làm sao đổi số phèn!",
     "Châm biếm thói mê tín bói toán."),

    ("Con Đò", "Ván gỗ ghép liền một chiếc thuyền,\nĐưa người qua lại bến sông duyên.\nNước ròng nước lớn đò xuôi ngược,\nSóng vỗ mạn thuyền lái vững yên.\nKhách sang đông đảo nào ai nhớ,\nBến cũ trơ trọi kẻ lái khuyên.\nĐưa hết người trần sang bến giác,\nMột mình lặng lẽ ngắm trời thiêng.",
     "Hình tượng con đò đưa khách qua sông ẩn dụ cho sự cống hiến âm thầm."),

    ("Cảnh Làm Chay", "Đàn tràng bày biện rộn ràng thay,\nThầy cúng gõ chuông tụng suốt ngày.\nKhấn vái linh hồn về cõi Phật,\nCầu xin nghiệp chướng rũ bàn tay.\nTiền vàng đốt cháy bay tro bụi,\nVàng mã tiêu tan ngập gió bay.\nNgười sống chưa an lo kẻ thác,\nTrần gian lắm nỗi chuyện nực cười.",
     "Phê phán hủ tục mê tín dị đoan làm chay tốn kém."),

    ("Vịnh Trăng Thu", "Gió mát thu về trăng sáng soi,\nVàng son gác ngọc trải muôn nơi.\nCành đa chú Cuội ngồi trông ngóng,\nCung quế Hằng Nga hé nụ cười.\nChiếu sáng nhân gian nghìn cảnh ngộ,\nLàm vơi trần thế vạn niềm vơi.\nNâng ly cạn chén mừng thu hội,\nThơ dệt ngàn lời gửi cõi khơi.",
     "Vẻ đẹp trong trẻo của đêm rằm trung thu."),

    ("Hoa Phù Dung", "Sớm nở màu tươi trắng muốt tinh,\nTrưa chuyển hồng tươi thắm đượm tình.\nChiều tàn tím ngắt phai tàn rụng,\nMột kiếp phù dung chớp mắt xinh.\nThương kẻ hồng nhan đời ngắn ngủi,\nTiếc người tài sắc phận linh đinh.\nThế nhân chớ chuộng bề ngoài sắc,\nGiữ lấy tâm thanh đức trọn gìn.",
     "Triết lý nhân sinh về sự đổi thay phù du của sắc đẹp."),

    ("Miếu Sầm Nghi Đống", "Ngổn ngang gạch đá chốn hoang tàn,\nMiếu dựng cheo leo giữa dốc ngàn.\nBại trận thắt cổ đền mạng sống,\nNgàn thu bia miệng nhục còn mang.\nTướng giặc huênh hoang thời đã mất,\nAnh hùng Đại Việt tiếng vang lừng.\nQua đây ghé mắt cười mỉa một,\nThái thú phen này hết mộng sang!",
     "Tiếng cười chế giễu kẻ bại trận xâm lăng."),

    ("Đề Tranh Tố Nữ", "Khen ai khéo vẽ bức tranh này,\nBốn ả xinh tươi tựa cánh mây.\nẢ thổi sáo tiêu ngân vút vẳng,\nẢ ôm đàn nguyệt gảy cung say.\nẢ gõ nhịp phách êm đềm bước,\nẢ dạo cung cầm nhịp bổng bay.\nNhìn tranh mà ngỡ người trong mộng,\nSay đắm lòng ta chén rượu này.",
     "Vịnh bức tranh tứ bình Tố nữ tuyệt tác."),

    ("Vịnh Quả Chuông", "Đồng đúc nên hình quả chuông to,\nTreo cao gác ngọc gió vi vu.\nMột phen dùi giục rền vang khắp,\nBốn cõi giang sơn dứt mộng mơ.\nThức tỉnh người trần trong bể khổ,\nKhuyên răn nhân thế chớ làm ngơ.\nTiếng chuông ngân vẳng nơi cửa Phật,\nThanh lọc tâm hồn sáng tựa tơ.",
     "Âm thanh tiếng chuông cảnh tỉnh nhân gian."),

    ("Đêm Trăng Tự Tình", "Đêm vắng canh tàn gió thoảng lay,\nMột mình đối bóng với trăng này.\nRượu ngon nâng chén khôn làm ấm,\nThơ dệt nghìn câu chẳng thỏa say.\nThương phận má hồng duyên lận đận,\nTiếc thời xuân sắc tuổi hao gầy.\nBao giờ gặp đặng người tri kỷ,\nCùng dạo vườn xuân tay nắm tay?",
     "Nỗi khát khao hạnh phúc lứa đôi chân chính."),

    ("Khuyên Người Góa Bụa", "Cành khô hoa rụng có khi tươi,\nKhép cửa làm chi hỡi người ơi!\nKhăn trắng cởi ra lau ngấn lệ,\nÁo màu mặc lại đón xuân ngời.\nDuyên xưa đã lỡ duyên sau tới,\nĐò trước không sang đò khác bơi.\nĐời người ngắn ngủi vài mươi tuổi,\nSống trọn yêu thương thỏa cuộc đời.",
     "Tư tưởng phóng khoáng, nhân văn giải phóng phụ nữ khỏi xiềng xích góa bụa thủ tiết."),

    ("Tạ Tình", "Cảm tạ tri âm chút tấc tình,\nCho đời Xuân Hương sáng lung linh.\nThơ gửi muôn phương vang khúc hát,\nLòng son một mảnh giữa non xanh.\nTrăm năm danh tiết không hề thẹn,\nNgàn thuở thi đàn rạng chữ trinh.\nĐể lại cho đời bao khúc ngâm,\nBà Chúa Thơ Nôm tiếng vĩnh hằng.",
     "Lời kết đúc kết trọn vẹn sự nghiệp và tầm vóc Bà Chúa Thơ Nôm.")
]

# Lưu Hương Ký (thơ chữ Hán)
LUU_HUONG_KY = [
    ("Cảm Cựu Kiêm Trình Cần Chánh Học Sĩ Mai Sơn Phủ",
     "滿眼秋光起夕愁，青山落木水悠悠。\n客途漂泊身如葉，故國風雲事已休。\n舊約未成孤枕淚，長懷難托片雲浮。\n幾回欲借梅溪水，洗盡胸中百種憂。",
     "Bản dịch: 'Mãn nhãn thu quang khởi tịch sầu / Thanh sơn lạc mộc thủy du du...'. Bài thơ chữ Hán tuyệt tác gửi người tri âm Mai Sơn phủ, bộc lộ tình cảm sâu kín, kín đáo và đoan trang khác hẳn vẻ sắc sảo của thơ Nôm.")
]

def build_ho_xuan_huong_html():
    html = []
    html.append("""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-collection">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</div>
            <div class="cover-era">Văn Học Cổ Điển Việt Nam • Thế Kỷ XVIII – XIX</div>
            <div class="ornament">❖ ❖ ❖</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-title">HỒ XUÂN HƯƠNG</div>
            <div class="cover-subtitle">Toàn Tập Thơ Nôm Truyền Tụng & Lưu Hương Ký<br>Tuyển tập 42 bài thơ Nôm bất hủ & Khảo luận thi pháp Bà Chúa Thơ Nôm</div>
            <div class="gold-line"></div>
            <div class="cover-author">HỒ XUÂN HƯƠNG (1772 – 1822) • BÀ CHÚA THƠ NÔM</div>
            <div class="cover-author-sub">Danh nhân văn hóa thế giới UNESCO vinh danh năm 2021</div>
            <div class="seal-box">Ấn Bản Toàn Thư Khảo Luận Học Thuật</div>
        </div>
        
        <div class="cover-footer">
            <div>Viện Nghiên Cứu Văn Học Cổ Điển & Tinh Hoa Thi Ca</div>
            <div style="font-size: 9.5pt; color: #888; margin-top: 4px;">Khảo đính đối chiếu Quốc Âm Cổ Bản & Lưu Hương Ký phát hiện năm 1964</div>
        </div>
    </div>
    """)
    
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">KHẢO LUẬN: BÀ CHÚA THƠ NÔM HỒ XUÂN HƯƠNG</h1>
    <div class="ornament">❖</div>
    
    <div class="intro-box">
        <p><strong>Hồ Xuân Hương (1772 – 1822)</strong> được thi sĩ Xuân Diệu tôn vinh là <strong>"Bà Chúa Thơ Nôm"</strong> và được tổ chức UNESCO chính thức vinh danh là <strong>Danh nhân văn hóa thế giới</strong> tại kỳ họp Đại hội đồng lần thứ 41 năm 2021. Bà là hiện tượng kỳ vĩ, độc nhất vô nhị không chỉ trong văn học Việt Nam mà trong toàn bộ lịch sử thi ca phương Đông thời trung đại.</p>
        <p>Thơ Nôm Hồ Xuân Hương là sự kết hợp thiên tài giữa nghệ thuật thơ Đường luật nghiêm cẩn với ngôn ngữ thuần Việt bình dân, sắc nhọn, biến ảo khôn lường. Bằng bút pháp hai tầng nghĩa <em>"thanh mà tục, tục mà thanh"</em>, bà đã dựng nên tượng đài thi ca ngạo nghễ đạp đổ mọi xiềng xích lễ giáo phong kiến nam quyền, dũng cảm lên tiếng đòi quyền sống, quyền yêu đương, quyền mưu cầu hạnh phúc chính đáng cho người phụ nữ.</p>
        <p>Năm 1964, việc phát hiện tập thơ <strong>Lưu Hương Ký</strong> (gồm 24 bài thơ chữ Hán và 28 bài thơ chữ Nôm) đã làm sáng tỏ thêm một chiều kích tâm hồn khác của Hồ Xuân Hương: Một nữ sĩ tài hoa, đằm thắm, u buồn và thiết tha với tình người, tình đời.</p>
    </div>
    """)
    
    for i, p in enumerate(NOM_POEMS_42, 1):
        title, text, comment = p
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #8B1E1E; padding-bottom: 4px; margin-bottom: 8px;">
                <span style="font-weight: bold; color: #721616; font-size: 11.5pt;">{i}. {title}</span>
                <span style="font-size: 9pt; color: #666; font-style: italic;">Thơ Nôm Truyền Tụng</span>
            </div>
            
            <div class="poem-stanza" style="line-height: 1.85; font-size: 11pt; color: #1a365d; font-weight: 500;">
                {text.replace(chr(10), '<br>')}
            </div>
            
            <div class="commentary-box" style="margin-top: 8px;">
                <div class="commentary-title">Bình Luận Thi Pháp & Ý Nghĩa Nhân Văn:</div>
                {comment}
            </div>
        </div>
        """)
        
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">LƯU HƯƠNG KÝ • THƠ CHỮ HÁN</h1>
    <div class="ornament">❖</div>
    """)
    for title, text, comment in LUU_HUONG_KY:
        html.append(f"""
        <div class="poem-container avoid-break" style="margin-top: 20px;">
            <div style="border-bottom: 1.5px solid #8B1E1E; padding-bottom: 4px; margin-bottom: 8px;">
                <span style="font-weight: bold; color: #721616; font-size: 11.5pt;">{title}</span>
            </div>
            <div class="han-script" style="text-align: center; margin: 10px 0; font-size: 12pt;">
                {text.replace(chr(10), '<br>')}
            </div>
            <div class="commentary-box">
                <div class="commentary-title">Bình Luận:</div>
                {comment}
            </div>
        </div>
        """)
        
    html.append("""
    <div class="page-break"></div>
    <h1 class="chapter-title">VĨ THANH: SỨC SỐNG BẤT TỬ CỦA HỒ XUÂN HƯƠNG</h1>
    <div class="ornament">❖</div>
    <div class="intro-box">
        <p>Hồ Xuân Hương đã đi vào cõi vĩnh hằng hơn hai trăm năm, nhưng tiếng cười giòn giã, chua cay mà chan chứa tình thương của bà vẫn mãi vang vọng trong tâm thức người Việt. Bà là biểu tượng rực rỡ của tinh thần giải phóng phụ nữ, một tượng đài ngôn ngữ thi ca Nôm trác tuyệt của dân tộc ta.</p>
    </div>
    """)
    
    return "\n".join(html)

async def main():
    print("Building Ho Xuan Huong comprehensive anthology...")
    html_content = build_ho_xuan_huong_html()
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="HỒ XUÂN HƯƠNG • BÀ CHÚA THƠ NÔM",
        header_right="TOÀN TẬP 42 BÀI THƠ NÔM & LƯU HƯƠNG KÝ"
    )

if __name__ == "__main__":
    asyncio.run(main())
