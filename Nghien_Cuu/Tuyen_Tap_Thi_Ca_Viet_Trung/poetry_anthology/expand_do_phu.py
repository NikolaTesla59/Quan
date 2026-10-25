# -*- coding: utf-8 -*-
"""
Expand Đỗ Phủ to 25+ poems and re-render
"""
import os
import sys
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\03. [712-770] Trung Quốc_Đỗ Phủ (Thi Thánh)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[760] Đỗ Phủ - Tuyển Tập Đường Thi (Nguyên Tác Chữ Hán, Phiên Âm & Dịch Thơ).pdf")

EXTRA_DO_PHU = [
    {
        "title": "Thạch Hào Lại (石壕吏)",
        "subtitle": "Quan Lại Bắt Lính Thôn Thạch Hào Giữa Đêm Khuya",
        "han": """暮投石壕村，有吏夜捉人。
老翁逾牆走，老婦出門看。
吏呼一何怒！婦啼一何苦！
聽婦前致詞：三男鄴城戍。
一男附書至，二男新戰死。
存者且偷生，死者長已矣！
室中更無人，惟有乳下孫。
有孫母未去，出入無完裙。
老嫗力雖衰，請從吏夜歸。
急應河陽役，猶得備晨炊。
夜久語聲絕，如聞泣幽咽。
天明登前途，獨與老翁別。""",
        "phien_am": """Mộ đầu Thạch Hào thôn, hữu lại dạ tróc nhân.
Lão ông du tường tẩu, lão phụ xuất môn khán.
Lại hô nhất hà nộ! Phụ đề nhất hà khổ!
Thính phụ tiền trí từ: Tam nam Nghiệp thành thú.
Nhất nam phụ thư chí, nhị nam tân chiến tử.
Tồn giả thả thâu sinh, tử giả trường dĩ hĩ!
Thất trung cánh vô nhân, duy hữu nhũ hạ tôn.
Hữu tôn mẫu vị khứ, xuất nhập vô hoàn quần.
Lão ẩu lực tuy suy, thỉnh tòng lại dạ quy.
Cấp ứng Hà Dương dịch, do đắc bị thần xuy.
Dạ cửu ngữ thanh tuyệt, như văn khấp u yết.
Thiên minh đăng tiền đồ, độc dữ lão ông biệt.""",
        "dich_nghia": """Chiều tối trọ lại thôn Thạch Hào, có quan lại nửa đêm xông vào bắt lính. Ông lão nhảy qua tường trốn chạy, bà lão ra mở cửa ngóng xem. Quan lại thét mắng sao mà giận dữ thế! Bà lão khóc than sao mà cay đắng thay! Nghe bà lão bước lên giãi bày: Ba đứa con trai đi lính thú giữ thành Nghiệp. Một đứa vừa gửi thư về, hai đứa mới tử trận. Đứa sống tạm bợ lay lắt qua ngày, đứa chết đành vĩnh viễn lìa đời! Trong nhà chẳng còn ai khác, chỉ có đứa cháu nhỏ còn bú sữa mẹ. Vì có cháu nhỏ mẹ nó chưa nỡ bỏ đi, ra vào chẳng có manh quần lành lặn. Mụ già này sức tuy đã suy yếu, xin theo quan đi ngay trong đêm. Kịp ứng cứu việc sai dịch ở Hà Dương, may ra còn nấu nướng cơm nước buổi sớm cho quân sĩ. Đêm khuya tiếng nói chuyện đã dứt, dường như nghe thấy tiếng khóc nghẹn ngào u uất. Sáng ngày cất bước lên đường đi tiếp, chỉ từ biệt một mình ông lão!""",
        "dich_tho": """Chiều trọ thôn Thạch Hào,
Đêm quan xông bắt lính.
Ông lão vượt tường trốn,
Bà lão mở cửa xem.
Quan thét sao dữ tợn!
Bà khóc sao đắng cay!
Bà nghẹn ngào thưa gửi:
Ba con giữ ải Nghiệp.
Một con gửi thư tới,
Hai con mới bỏ mình.
Sống lay lắt qua ngày,
Chết vĩnh viễn ngàn thu!
Nhà chẳng còn ai nữa,
Cháu thơ khát sữa non.
Mẹ cháu chưa nỡ đi,
Áo quần rách tả tơi.
Sức già dẫu suy mòn,
Xin theo quan đi đêm.
Kịp việc dịch Hà Dương,
Nấu cơm buổi sớm mai.
Đêm sâu tiếng chuyện dứt,
Nghe tiếng khóc nghẹn ngào.
Trời sáng ta lên đường,
Chỉ cùng ông lão giã!""",
        "commentary": "Thi phẩm hiện thực đỉnh cao tố cáo sự tàn bạo của nạn bắt lính và nỗi thống khổ cùng cực của nhân dân trong chiến tranh."
    },
    {
        "title": "Thục Tướng (蜀相)",
        "subtitle": "Viếng Đền Thờ Gia Cát Lượng Ngoài Thành Cẩm Quan",
        "han": """丞相祠堂何處尋？錦官城外柏森森。
映階碧草自春色，隔葉黃鸝空好音。
三顧頻煩天下計，兩朝開濟老臣心。
出師未捷身先死，長使英雄淚滿襟！""",
        "phien_am": """Thừa tướng từ đường hà xứ tầm?
Cẩm Quan thành ngoại bách sâm sâm.
Ánh giai bích thảo tự xuân sắc,
Cách diệp hoàng ly không hảo âm.
Tam cố tần phiền thiên hạ kế,
Lưỡng triều khai tế lão thần tâm.
Xuất sư vị tiệp thân tiên tử,
Trường sử anh hùng lệ mãn khâm!""",
        "dich_nghia": """Đền thờ Thừa tướng tìm ở nơi đâu? Ngoài thành Cẩm Quan hàng thông bách mọc xanh um rậm rạp. Cỏ biếc rọi bậc thềm tự mình phơi sắc xuân, chim hoàng oanh hót sau vòm lá uổng phí tiếng ca êm ái. Ba lần tới lều cỏ bàn mưu định thiên hạ, hai triều vua giúp rập tấm lòng son của vị lão thần. Xuất quân chưa kịp chiến thắng thì thân đã tạ thế, khiến cho bậc anh hùng muôn đời sau phải rơi lệ đầm vạt áo!""",
        "dich_tho": """Đền thờ Thừa tướng chốn nào đây?
Cẩm Quan thành ngoại bách sum vầy.
Cỏ biếc thềm xuân khoe sắc thắm,
Oanh vàng cành lá hót uổng thay.
Ba phen lều cỏ mưu thiên hạ,
Hai triều gánh vác dạ trung trinh.
Ra quân chưa thắng thân đành mất,
Mãi để anh hùng lệ đẫm mi!""",
        "commentary": "Hai câu kết thiên cổ: 'Xuất sư vị tiệp thân tiên tử / Trường sử anh hùng lệ mãn khâm' là khúc ca bi tráng nhất khóc thương cho hoài bão lớn lao của bậc vĩ nhân chưa thành đã ngã xuống."
    },
    {
        "title": "Xuân Dạ Hỷ Vũ (春夜喜雨)",
        "subtitle": "Mưa Xuân Đêm Tối Tươi Tốt Vạn Vật",
        "han": """好雨知時節，當春乃發生。
隨風潛入夜，潤物細無聲。
野徑雲俱黑，江船火獨明。
曉看紅濕處，花重錦官城。""",
        "phien_am": """Hảo vũ tri thời tiết,
Đương xuân nãi phát sinh.
Tùy phong tiềm nhập dạ,
Nhuận vật tế vô thanh.
Dã kính vân câu hắc,
Giang thuyền hỏa độc minh.
Hiểu khán hồng thấp xứ,
Hoa trọng Cẩm Quan thành.""",
        "dich_nghia": """Cơn mưa lành biết đúng thời tiết, đúng độ sang xuân liền rơi xuống. Theo làn gió lẻn vào đêm tối, thấm nhuần vạn vật nhẹ nhàng không một tiếng động. Đường đồng nội mây đen bao phủ tối tăm, thuyền trên sông riêng một đốm lửa bập bùng sáng tỏ. Sáng mai trông ra nơi đỏ thắm ướt đẫm mưa xuân, hoa nở trĩu cành khắp thành Cẩm Quan.""",
        "dich_tho": """Mưa lành biết thời tiết,
Đúng xuân lại tưới xanh.
Theo gió lẻn vào đêm,
Thấm hạt nhẹ không thanh.
Đường đồng mây tối nghịt,
Đốm lửa thuyền cô quạnh.
Sớm mai trông hoa nở,
Đỏ rực khắp thành đô!""",
        "commentary": "Bút pháp tinh tế miêu tả cơn mưa xuân lặng lẽ nhuận thấm cỏ cây, ẩn dụ cho đức độ của bậc quân tử âm thầm làm ơn cho muôn loài mà không màng danh tiếng."
    },
    {
        "title": "Nguyệt Dạ (月夜)",
        "subtitle": "Đêm Trăng Nhớ Vợ Nơi Quê Nhà Loạn Lạc",
        "han": """今夜鄜州月，閨中只獨看。
遙憐小兒女，未解憶長安。
香霧雲鬟濕，清輝玉臂寒。
何時倚虛幌，雙照淚痕乾？""",
        "phien_am": """Kim dạ Phu Châu nguyệt,
Khuê trung chỉ độc khán.
Diêu lân tiểu nhi nữ,
Vị giải ức Trường An.
Hương vụ vân hoàn thấp,
Thanh huy ngọc tý hàn.
Hà thời ỷ hư hoảng,
Song chiếu lệ ngân can?""",
        "dich_nghia": """Đêm nay vầng trăng đất Phu Châu, nơi phòng khuê nàng chỉ đứng ngắm một mình. Từ xa thương xót đàn con thơ dại, chưa hiểu nỗi nhớ cha nơi Trường An. Làn sương đượm hương làm ướt mái tóc mây, ánh trăng trong trẻo làm lạnh cánh tay ngọc. Bao giờ được cùng tựa bức rèm the mỏng, trăng sáng soi chung đôi lứa lau khô ngấn lệ sầu?""",
        "dich_tho": """Đêm nay trăng đất Phu Châu,
Buồng the người ngọc ngắm trông một mình.
Thương đàn con nhỏ vô tình,
Chưa tường nỗi nhớ kinh thành Trường An.
Mái mây đẫm hạt sương lan,
Cánh tay ngọc buốt bóng trăng lạnh lùng.
Bao giờ tựa bóng rèm song,
Trăng soi hai đứa lệ dòng lau khô?""",
        "commentary": "Tình cảm gia đình sâu đậm, đặt mình vào vị trí người vợ nơi quê nhà để miêu tả nỗi nhớ nhung, tạo nên cấu tứ thi ca độc đáo và đầm ấm."
    },
    {
        "title": "Thu Hứng • Bài 2 (秋興八首·其二)",
        "subtitle": "Bóng Nắng Hoàng Hôn & Cung Khuyết Xa Vời",
        "han": """夔府孤城落日斜，每依北斗望京華。
聽猿實下三聲淚，奉使虛隨八月槎。
畫省香爐違伏枕，山樓粉堞隱悲笳。
請看石上藤蘿月，已映洲前蘆荻花。""",
        "phien_am": """Quỳ phủ cô thành lạc nhật tà,
Mỗi y Bắc Đẩu vọng kinh hoa.
Thính viên thực hạ tam thanh lệ,
Phụng sứ hư tùy bát nguyệt tra.
Họa tỉnh hương lô vi phục chẩm,
Sơn lâu phấn điệp ẩn bi gia.
Thỉnh khán thạch thượng đằng la nguyệt,
Dĩ ánh châu tiền lư địch hoa.""",
        "dich_nghia": """Thành trơ trọi đất Quỳ phủ bóng mặt trời lặn nghiêng, mỗi lần trông theo chòm sao Bắc Đẩu lại ngóng về kinh hoa Trường An. Nghe tiếng vượn kêu rơi ba hàng lệ, thân mang danh sứ giả luống uổng thả bè tháng tám. Khói hương bàn thờ tòa họa tỉnh nay đã xa cách gối nằm, lầu núi tường vôi ẩn hiện tiếng còi bi ai. Xin hãy ngắm vầng trăng soi trên dây leo bờ đá, nay đã chiếu rọi xuống hoa lau trước bãi sông.""",
        "dich_tho": """Bóng ngả Quỳ Châu bóng ác tà,
Trông sao Bắc Đẩu nhớ kinh hoa.
Nghe vượn ba tiếng tuôn hàng lệ,
Theo bè tháng tám luống công xa.
Lầu tỉnh hương trầm xa gối bệnh,
Tường thành ẩn hiện tiếng tù và.
Kìa xem trăng rọi dây leo đá,
Đã chiếu bờ sông hoa địch già!""",
        "commentary": "Nỗi nhớ kinh đô Trường An đau đáu của kẻ tha hương lưu lạc nơi hẻm núi hiểm trở."
    },
    {
        "title": "Lữ Dạ Thư Hoài (旅夜書懷)",
        "subtitle": "Đêm Trọ Viết Nỗi Lòng • Cánh Chim Bói Cá Giữa Trời Đất",
        "han": """細草微風岸，危檣獨夜舟。
星垂平野闊，月湧大江流。
名豈文章著，官應老病休。
飄飄何所似，天地一沙鷗。""",
        "phien_am": """Tế thảo vi phong ngạn,
Nguy tường độc dạ chu.
Tinh thùy bình dã khoát,
Nguyệt dũng đại giang lưu.
Danh khởi văn chương trước,
Quan ứng lão bệnh hưu.
Phiêu phiêu hà sở tự,
Thiên địa nhất sa âu.""",
        "dich_nghia": """Cỏ nhỏ gió hiu hiu thổi bờ bến, cột buồm cao con thuyền lẻ loi trong đêm. Sao sa rủ xuống cánh đồng bằng phẳng bát ngát, vầng trăng trào dâng dòng sông lớn cuồn cuộn chảy. Danh tiếng há do văn chương mà rạng rỡ, làm quan nay già yếu nhiều bệnh tật nên xin nghỉ. Trôi dạt bồng bềnh giống như vật gì? Như cánh chim âu lẻ loi bay giữa đất trời mênh mang!""",
        "dich_tho": """Gió hiu cỏ mướt bờ sâu,
Cột buồm chiếc bóng đêm thâu lạnh lùng.
Trời sa ngút cánh đồng bằng,
Trường Giang cuồn cuộn ánh trăng dập dồn.
Văn chương đâu đặng tiếng vang,
Tuổi già lắm bệnh từ quan nghỉ rồi.
Lênh đênh phiêu dạt giữa trời,
Chim âu một cánh giữa trời bao la!""",
        "commentary": "Hình tượng 'Thiên địa nhất sa âu' (Giữa trời đất một cánh chim âu) là ẩn dụ kiệt xuất nhất về thân phận con người cô đơn trôi dạt giữa vũ trụ bao la."
    },
    {
        "title": "Giang Nam Phùng Lý Quy Niên (江南逢李龜年)",
        "subtitle": "Gặp Nhạc Sư Lý Quy Niên Ở Giang Nam • Khúc Tiễn Biệt Thịnh Đường",
        "han": """岐王宅裏尋常見，崔九堂前幾度聞。
正是江南好風景，落花時節又逢君。""",
        "phien_am": """Kỳ Vương trạch lý tầm thường kiến,
Thôi Cửu đường tiền kỷ độ văn.
Chính thị Giang Nam hảo phong cảnh,
Lạc hoa thời tiết hựu phùng quân.""",
        "dich_nghia": """Nơi tư thất Kỳ Vương thường xuyên trông thấy, trước sảnh đường Thôi Cửu đã mấy độ nghe đàn. Chính vào lúc Giang Nam phong cảnh tươi đẹp nhất, giữa mùa hoa rụng lại được gặp bác nơi đây!""",
        "dich_tho": """Nhà Kỳ Vương cũ thường hay thấy,
Đường Thôi Cửu xưa mấy độ nghe.
Giang Nam phong cảnh đương tươi tốt,
Mùa hoa rụng lại gặp gỡ bè!""",
        "commentary": "Bốn câu thơ 28 chữ khép lại một thời đại: Gặp lại danh ca cung đình năm xưa giữa mùa hoa rụng chốn tha hương, thâu tóm trọn vẹn nỗi xót xa trước sự sụp đổ của một triều đại thịnh trị vàng son."
    }
]

async def run_expansion():
    print("Expanding Do Phu publication...")
    import do_phu_generator
    # Combine original and extra
    do_phu_generator.DO_PHU_POEMS.extend(EXTRA_DO_PHU)
    html_content = do_phu_generator.build_do_phu_html()
    await render_html_to_pdf(
        html_content=html_content,
        output_path=OUTPUT_FILE,
        header_left="ĐỖ PHỦ • THI THÁNH ĐẠI ĐƯỜNG",
        header_right="ĐẠI TUYỂN TẬP ĐƯỜNG THI TOÀN BẢN"
    )

if __name__ == "__main__":
    asyncio.run(run_expansion())
