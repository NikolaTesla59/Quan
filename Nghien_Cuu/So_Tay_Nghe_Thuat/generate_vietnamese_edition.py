# -*- coding: utf-8 -*-
"""
Full Vietnamese Master Edition Compiler for:
[Bản Dịch Tiếng Việt] Louis Bonnafont - Muôn Hạng Dân Bắc Kỳ (Types Tonkinois 1903)
"""
import os
import sys
import shutil
import pymupdf

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch")
from book_builder import BookBuilder

def build_full_book():
    builder = BookBuilder(
        title="Muôn Hạng Dân Bắc Kỳ",
        subtitle="Types Tonkinois (Hà Nội 1903) - Bản Dịch Toàn Văn & Khảo Luận Lịch Sử"
    )
    
    # Cover image path
    cover_img = r"C:\Users\Admin\.gemini\antigravity\scratch\page_3.png"
    builder.build_cover(cover_img)
    
    # ---------------------------------------------------------
    # Trang 1: Lời giới thiệu khảo cứu & Bối cảnh lịch sử
    # ---------------------------------------------------------
    builder.new_page(running_header="KHẢO LUẬN LỊCH SỬ & GIỚI THIỆU TÁC PHẨM")
    
    builder.add_center(builder.y_pos + 10, "LỜI GIỚI THIỆU KHẢO CỨU", builder.font_bold, 15)
    builder.add_center(builder.y_pos + 28, "BỨC TRANH XÃ HỘI HỌC VỀ CON NGƯỜI BẮC KỲ ĐẦU THẾ KỶ XX", builder.font_italic, 10.5)
    builder.y_pos += 42
    builder.curr_page.draw_line(pymupdf.Point(builder.margin_l, builder.y_pos - 8), pymupdf.Point(builder.margin_r, builder.y_pos - 8), color=(0.7, 0.3, 0.2), width=1)
    
    intro_p1 = (
        "Năm 1903, tại nhà in F.-H. Schneider danh tiếng ở Hà Nội, tác phẩm Types Tonkinois (nghĩa đen: 'Các kiểu người Bắc Kỳ', "
        "bản dịch tiếng Việt thường được biết đến với tên gọi 'Muôn Hạng Dân Bắc Kỳ' hay 'Người Bắc Kỳ') của tác giả Louis Bonnafont chính thức ra đời. "
        "Đây là một trong những trước tác độc đáo, sống động và đậm chất trào phúng nhất về đời sống xã hội miền Bắc Việt Nam trong buổi giao thời đầy biến động."
    )
    builder.add_text_block(intro_p1, builder.font_reg, 10, line_height=14.5, indent=15, space_after=10)
    
    intro_p2 = (
        "Khác với những công trình nghiên cứu hàn lâm kinh viện nặng về phong tục, địa chí của Gustave Dumoutier (như 'Tiểu luận về dân Bắc Kỳ') "
        "hay ghi chép viễn chinh quân sự của Bác sĩ Charles-Édouard Hocquard ('Một chiến dịch ở Bắc Kỳ'), Louis Bonnafont tiếp cận xã hội dưới góc nhìn "
        "của một nhà báo, một ký giả tự do đã rong ruổi suốt mười lăm năm khắp mọi nẻo đường làng quê và góc phố Hà Nội. "
        "Ông không phác họa bức tranh qua những số liệu thống kê khô khan, mà bằng 75 bức chân dung sống động, sắc nét, lột tả chân thực tâm lý, thói quen, "
        "manh áo, miếng cơm của từng tầng lớp con người nơi đây."
    )
    builder.add_text_block(intro_p2, builder.font_reg, 10, line_height=14.5, indent=15, space_after=10)
    
    intro_p3 = (
        "Điểm đặc biệt tạo nên giá trị bất hủ cho tác phẩm chính là sự cộng hưởng giữa ngòi bút châm biếm sâu cay của Bonnafont và những nét vẽ trác tuyệt "
        "của các họa sĩ tài hoa thời bấy giờ như E. Ronjat và Cézard. Mỗi trang viết là một lát cắt hiện thực: từ nét bệ vệ, hách dịch của viên quan phụ mẫu "
        "cho đến thân phận mòn mỏi của kiếp cu li kéo xe; từ sự lanh lợi láu cá của những chú bồi bàn cho đến sự khắc khổ nhẫn nhục của người nhà quê tần tảo."
    )
    builder.add_text_block(intro_p3, builder.font_reg, 10, line_height=14.5, indent=15, space_after=10)
    
    intro_p4 = (
        "LƯU Ý VỀ LĂNG KÍNH THỜI ĐẠI: Đọc Louis Bonnafont hôm nay, độc giả cần nhận thức rõ lăng kính và thế giới quan thực dân của tác giả đầu thế kỷ XX. "
        "Bên cạnh sự quan sát tinh tế và lòng trắc ẩn trước nỗi cơ cực của tầng lớp lao động, ngòi bút của ông không tránh khỏi những định kiến bề trên, "
        "cách nhìn có phần cay nghiệt và sự giễu nhại mang tính thực dân. Tuy nhiên, chính sự 'thẳng thừng không che đậy' ấy lại biến tác phẩm thành một "
        "nguồn tư liệu sử liệu vô giá, giúp chúng ta nhìn thấu diện mạo trần trụi của xã hội Việt Nam thời thuộc địa mà các bộ sử chính thống của triều Nguyễn "
        "hay báo cáo hành chính của Phủ Toàn quyền đều bỏ qua."
    )
    builder.add_text_block(intro_p4, builder.font_italic, 9.5, line_height=14, indent=15, space_after=12)

    # ---------------------------------------------------------
    # Trang 2: Mục lục toàn thư 75 hạng người
    # ---------------------------------------------------------
    builder.new_page(running_header="MỤC LỤC TOÀN BỘ 75 HẠNG NGƯỜI BẮC KỲ")
    builder.add_center(builder.y_pos + 10, "MỤC LỤC TOÀN BỘ 75 HẠNG NGƯỜI", builder.font_bold, 14)
    builder.add_center(builder.y_pos + 26, "HỆ THỐNG PHÂN LOẠI XÃ HỘI BẮC KỲ ĐẦU THẾ KỶ XX (1903)", builder.font_italic, 10)
    builder.y_pos += 40
    builder.curr_page.draw_line(pymupdf.Point(builder.margin_l, builder.y_pos - 8), pymupdf.Point(builder.margin_r, builder.y_pos - 8), color=(0.7, 0.3, 0.2), width=1)
    
    toc_groups = [
        ("I. TẦNG LỚP QUAN CHỨC, CƯỜNG HÀO & CHỨC DỊCH", [
            ("Le Mandarin", "Quan lại triều đình / Quan phụ mẫu (Trang 52)"),
            ("Le Dignitaire", "Đại thần / Vị chức sắc danh giá (Trang 35)"),
            ("Le Notable", "Hương hào / Kỳ mục làng xã (Trang 64)"),
            ("Femme de fonctionnaire", "Bà lớn / Vợ quan chức (Trang 38)")
        ]),
        ("II. TẦNG LỚP THẦY KÝ, THÔNG NGÔN & TRÍ THỨC MỚI", [
            ("L'Interprète", "Thầy thông ngôn / Thông phán (Trang 44)"),
            ("Le Scribe", "Thầy ký / Thư ký công sở (Trang 82)"),
            ("L'Instituteur / L'Institutrice", "Thầy giáo / Cô giáo bản xứ (Trang 42, 43)"),
            ("Le Télégraphiste", "Nhân viên điện tín (Trang 88)")
        ]),
        ("III. LỰC LƯỢNG QUÂN BINH, CẢNH SÁT & AN NINH", [
            ("Le Linh", "Lính tập / Lính khố đỏ (Trang 48)"),
            ("Le Linh-co", "Lính cơ địa phương / Lính lệ (Trang 49)"),
            ("L'Agent de police", "Cảnh sát tuần tra thị thành (Trang 3)"),
            ("Le Milicien", "Lính bảo an / Dân binh (Trang 59)"),
            ("L'Espion", "Mật thám / Tay chỉ điểm (Trang 37)"),
            ("Le Biffin", "Lính lê dương / Lính bộ binh Pháp (Trang 5)"),
            ("Le Pirate", "Giặc cướp / Nghĩa quân kháng chiến (Trang 73)"),
            ("Le Prisonnier", "Tù nhân khổ sai (Trang 74)")
        ]),
        ("IV. TẦNG LỚP BỒI BÀN & PHỤC VỤ TƯ GIA PHÁP", [
            ("Le Boy", "Thằng bồi / Bồi bàn tư gia (Trang 9)"),
            ("Le Boy cuisine", "Bồi bếp / Phụ bếp (Trang 11)"),
            ("Le Boy panka", "Thằng bé kéo quạt trần (Trang 12)"),
            ("Le Cuisinier", "Đầu bếp nấu món Tây (Trang 34)"),
            ("Le Maître d'hôtel", "Quản gia khách sạn / Nhà hàng (Trang 51)"),
            ("Le Groom", "Thằng chạy việc / Chân sai vặt (Trang 41)"),
            ("Le Garçon de café", "Bồi quán cà phê phố Tây (Trang 40)")
        ]),
        ("V. TẦNG LỚP LAO ĐỘNG CỰC NHỌC & CU LI KHUÂN VÁC", [
            ("Le Coolie", "Cu li kéo xe tay / Phu phen (Trang 26)"),
            ("Le Caï-coolies", "Cai cu li / Trùm thầu phu (Trang 14)"),
            ("Le Coolie femelle", "Nữ cu li / Phụ nữ làm phu gánh gồng (Trang 28)"),
            ("Le Coolie tinette", "Cu li dọn thùng phân / Vệ sinh đô thị (Trang 30)"),
            ("Le Coolie tram", "Cu li kéo xe gòn / Đường ray (Trang 31)"),
            ("Le Portefaix", "Phu khuân vác bến tàu (Trang 76)"),
            ("Le Mineur", "Thợ mỏ than / Thợ mỏ sông Hồng (Trang 60)"),
            ("L'Ouvrier", "Thợ thủ công đô thị (Trang 68)"),
            ("Le Passeur", "Người lái đò qua sông (Trang 70)")
        ]),
        ("VI. THÔN QUÊ & ĐỜI SỐNG NÔNG DÂN", [
            ("Le Nhaqué", "Người nhà quê / Nông dân đồng chiêm trũng (Trang 62)"),
            ("La Ba-gia", "Bà già thôn dã nhai trầu (Trang 4)"),
            ("Le Tâcheron", "Thợ khoán / Lao động mùa vụ (Trang 87)")
        ]),
        ("VII. PHỤ NỮ & ĐỜI SỐNG THỊ DÂN", [
            ("La Con-gaïe", "Cô gái bản xứ / Phụ nữ Việt (Trang 25)"),
            ("La Madame indigène", "Bà đầm bản xứ / Vợ nhân tình quan Tây (Trang 50)"),
            ("La Nourrice / Bonne d'enfants", "Bà vú nuôi / Vú em (Trang 7, 65)"),
            ("La Changeuse de monnaie", "Bà đổi tiền trinh, tiền kẽm góc chợ (Trang 17)"),
            ("La Chanteuse", "Cô đầu / Đào hát ca trù (Trang 18)"),
            ("La Courtisane", "Kỹ nữ / Gái làng chơi (Trang 32)"),
            ("La Revendeuse", "Bà buôn chuyến / Bán hàng rong (Trang 80)"),
            ("La Marchande de crochets", "Cô hàng bán móc màn phố Paul-Bert (Trang 55)")
        ]),
        ("VIII. TÍN NGƯỠNG, TẬP TỤC & VĂN NGHỆ", [
            ("Le Bonze", "Thầy chùa / Nhà sư tu hành (Trang 8)"),
            ("Le Ma-qui", "Tục trừ tà & Tín ngưỡng ma quỷ (Trang 53)"),
            ("Cérémonial religieux", "Nghi thức tôn giáo cúng tế (Trang 16)"),
            ("L'Acteur", "Kép hát tuồng / Diễn viên sân khấu (Trang 1)"),
            ("Le Musicien ambulant", "Nghệ nhân hát xẩm / Nhạc công dạo (Trang 61)"),
            ("Le Têt", "Tết Nguyên Đán truyền thống (Trang 89)")
        ])
    ]
    
    for g_title, items in toc_groups:
        if builder.y_pos + 15 + len(items)*13 > builder.margin_b:
            builder.new_page(running_header="MỤC LỤC TOÀN BỘ 75 HẠNG NGƯỜI BẮC KỲ")
        builder.curr_tw.append(pymupdf.Point(builder.margin_l, builder.y_pos), g_title, font=builder.font_bold, fontsize=10)
        builder.y_pos += 14
        for fr_name, vn_name in items:
            t_line = f"• {fr_name}: {vn_name}"
            builder.curr_tw.append(pymupdf.Point(builder.margin_l + 12, builder.y_pos), t_line, font=builder.font_reg, fontsize=8.8)
            builder.y_pos += 12.5
        builder.y_pos += 4

    # ---------------------------------------------------------
    # Trang 3: Lời tựa của tác giả Louis Bonnafont (1903)
    # ---------------------------------------------------------
    builder.new_page(running_header="LỜI TỰA NGUYÊN BẢN CỦA TÁC GIẢ (HÀ NỘI 1903)")
    builder.add_center(builder.y_pos + 12, "LỜI TỰA NGUYÊN BẢN CỦA TÁC GIẢ", builder.font_bold, 14)
    builder.add_center(builder.y_pos + 28, "VIẾT TẠI HÀ NỘI, THÁNG 12 NĂM 1903", builder.font_italic, 10.5)
    builder.y_pos += 42
    builder.curr_page.draw_line(pymupdf.Point(builder.margin_l, builder.y_pos - 8), pymupdf.Point(builder.margin_r, builder.y_pos - 8), color=(0.7, 0.3, 0.2), width=1)
    
    preface_fr = (
        "« Ce sont des individualités qui vont défiler sous vos yeux, depuis le riche mandarin vénal, "
        "jusqu'au coolie bête de somme, que j'ai patiemment étudiées un peu partout au Tonkin, depuis quelque quinze ans.\n\n"
        "J'ai toujours pris pour sujet d'analyse celle de ces individualités qui me paraissait le plus se rapprocher de la généralité.\n\n"
        "Mon but sera atteint si je puis faire voir le peuple annamite tel qu'il est. »\n\n"
        "— L. B. (Louis Bonnafont) — Hanoï, décembre 1903."
    )
    builder.add_text_block(preface_fr, builder.font_italic, 10, line_height=15, indent=20, space_after=15)
    
    builder.add_center(builder.y_pos + 5, "BẢN DỊCH VIỆT NGỮ", builder.font_bold, 11)
    builder.y_pos += 22
    
    preface_vn = (
        "\"Những cá nhân sắp lần lượt diễu qua trước mắt quý độc giả đây — từ viên quan lại giàu có đục khoét cho đến kiếp cu li thân trâu ngựa — "
        "đều là những gương mặt mà tôi đã kiên trì quan sát, nghiên cứu khắp mọi nẻo đất Bắc Kỳ trong suốt mười lăm năm qua.\n\n"
        "Tôi luôn chọn làm đối tượng phân tích những cá nhân mang tính đại diện điển hình nhất cho số đông.\n\n"
        "Mục đích của tôi coi như đạt được nếu có thể phác họa để quý vị nhìn thấy con người An Nam đúng như chân dung thực tế của họ.\"\n\n"
        "— L. B. (Louis Bonnafont) — Hà Nội, tháng 12 năm 1903."
    )
    builder.add_text_block(preface_vn, builder.font_reg, 10.5, line_height=15, indent=20, space_after=20)
    
    # ---------------------------------------------------------
    # Function to add illustrated chapter
    # ---------------------------------------------------------
    def add_chapter_with_plate(title_vn, title_fr, img_filename, text_vn, commentary_vn=None):
        builder.new_page(running_header=f"MUÔN HẠNG DÂN BẮC KỲ  •  {title_vn.upper()}")
        
        # Chapter title box
        builder.curr_page.draw_rect(pymupdf.Rect(builder.margin_l, builder.y_pos, builder.margin_r, builder.y_pos + 38), color=(0.6, 0.25, 0.15), fill=(0.98, 0.96, 0.93), width=0.8)
        builder.add_center(builder.y_pos + 15, title_vn.upper(), builder.font_bold, 13)
        builder.add_center(builder.y_pos + 29, f"NGUYÊN BẢN: {title_fr.upper()}", builder.font_italic, 9.5)
        builder.y_pos += 48
        
        # Check image
        img_path = os.path.join(r"C:\Users\Admin\.gemini\antigravity\scratch\pages_extracted", img_filename)
        if not os.path.exists(img_path):
            img_path = os.path.join(r"C:\Users\Admin\.gemini\antigravity\scratch", img_filename)
            
        if os.path.exists(img_path):
            # Insert illustration image centered
            img_w = 260
            img_h = 280
            img_rect = pymupdf.Rect((builder.page_w - img_w)/2, builder.y_pos, (builder.page_w + img_w)/2, builder.y_pos + img_h)
            builder.curr_page.insert_image(img_rect, filename=img_path)
            builder.curr_page.draw_rect(img_rect, color=(0.7, 0.5, 0.3), width=0.6)
            builder.y_pos += img_h + 12
            
            caption = f"Hình minh họa nguyên bản của E. Ronjat & Cézard (Hà Nội, 1903)"
            builder.add_center(builder.y_pos, caption, builder.font_italic, 8)
            builder.y_pos += 16
        
        # Chapter Translation Text
        builder.add_text_block(text_vn, builder.font_reg, 10, line_height=14.5, indent=15, space_after=10)
        
        # Commentary / Historical Notes
        if commentary_vn:
            if builder.y_pos + 60 > builder.margin_b:
                builder.new_page(running_header=f"MUÔN HẠNG DÂN BẮC KỲ  •  {title_vn.upper()}")
            builder.y_pos += 6
            builder.curr_page.draw_line(pymupdf.Point(builder.margin_l, builder.y_pos), pymupdf.Point(builder.margin_r, builder.y_pos), color=(0.8, 0.5, 0.3), width=0.5)
            builder.y_pos += 10
            builder.curr_tw.append(pymupdf.Point(builder.margin_l, builder.y_pos), "★ BÌNH LUẬN & CHÚ GIẢI SỬ LIỆU:", font=builder.font_bold, fontsize=9.5)
            builder.y_pos += 13
            builder.add_text_block(commentary_vn, builder.font_italic, 9, line_height=13.5, indent=10, space_after=8)

    # ---------------------------------------------------------
    # Chương 1: Kép hát (L'Acteur)
    # ---------------------------------------------------------
    text_actor = (
        "Kép hát ngỡ rằng thời của mình đã tới. — Hễ vừa vung thanh đại đao sáng loáng, khoác lên mình bộ trang phục rực rỡ lóng lánh "
        "và tuôn ra những tràng thoại đầy hình tượng, anh ta liền tự coi mình là bậc thiên tài hay một vị bán thần; "
        "khi tiếng cồng tiếng chũm chọe nổi lên rộn rã, anh ta oai vệ tiến ra sân khấu sau toán quân cầm cờ xí, ngỡ mình là bậc đại tướng quân, "
        "bước đi uy nghi dõng dạc và ném về phía khán giả một ánh nhìn thách thức.\n\n"
        "Nếu chẳng may quên tuồng — chuyện này xảy ra khá thường xuyên — anh ta bèn nghiêng người với vẻ hách dịch về phía người nhắc tuồng, "
        "kẻ đang ngồi xổm cách đó vài bước, đọc thầm vở kịch theo từng nhịp diễn của các vai.\n\n"
        "Sang các vai hài kịch, phong thái đổi khác, mọi thứ xoay vần: hễ một câu bông đùa hóm hỉnh bật ra làm cả rạp cười ồ lên, "
        "kép hát cũng hòa vào tiếng cười của đám đông và chỉ dừng lại khi khán giả ngừng cười. Cứ thế, giữa người xem và kẻ đứng trên sân khấu "
        "hình thành một sợi dây giao cảm mật thiết, một luồng sinh khí kích thích tài ứng biến của đào kép và khiến người nghe dễ lòng bao dung.\n\n"
        "Danh vọng, thanh danh hay nghệ thuật thực chất là những mối bận tâm thứ yếu của kép hát. Sau cái khát khao gây chấn động khán phòng, "
        "điều duy nhất khiến anh ta bồn chồn chính là tiền bán vé (tiền thu rạp). Vừa nhẩm nghĩ về vai diễn — vai mà anh ta vẫn đinh ninh mình "
        "đang thủ diễn đầy tôn nghiêm — đôi mắt anh ta vừa lấm lét đảo quanh khán phòng, thầm tính toán xem phần tiền chia được sau đêm diễn "
        "sẽ đủ nuôi sống mình được bao nhiêu bữa cơm."
    )
    comm_actor = (
        "Bức tranh miêu tả sân khấu tuồng cổ Bắc Kỳ đầu thế kỷ XX. Louis Bonnafont đã nhìn thấu sự tương phản trớ trêu giữa vẻ hào nhoáng, "
        "oai phong lẫm liệt của các bậc quân vương, tướng soái trên sân khấu và cuộc sống bấp bênh, nghèo túng ngoài đời thực của người nghệ sĩ dân gian. "
        "Nghệ thuật tuồng thời bấy giờ vừa mang tính ước lệ cao, vừa phụ thuộc hoàn toàn vào những đồng tiền cắc quyên góp của khán giả làng xã."
    )
    add_chapter_with_plate("Kép Hát", "L'Acteur", "page_007.png", text_actor, comm_actor)

    # ---------------------------------------------------------
    # Chương 2: Quan lại (Le Mandarin)
    # ---------------------------------------------------------
    text_mandarin = (
        "Chiếm một vị thế tột bực trong tâm thức của thứ dân — một đối tượng vừa khiến người ta khiếp sợ, mà hễ họa hoằn lắm mới có vị tỏ ra công minh "
        "thì lập tức được dân chúng tôn sùng như thần thánh — viên quan lại, dẫu mang phẩm hàm cao quý và xuất thân từ tầng lớp lẽ ra phải nêu gương "
        "về đạo đức và phẩm hạnh công dân, phần lớn thời gian rốt cuộc cũng chỉ là một kẻ đầy tham vọng, lọc lõi mưu mô và ranh mãnh.\n\n"
        "Tấm gương mà viên quan nêu ra cho đám thuộc hạ dưới trướng, và đám này cũng vội vã học đòi làm theo hết sức bình sinh, có thể tóm gọn "
        "trong câu châm ngôn ngắn ngủi: 'Bàn tay vơ vào chẳng bao giờ vơ ra'.\n\n"
        "Người dân An Nam đã quá đỗi quen với việc bị các đấng quan trên — từ quan to đến lại nhỏ — vặt tỉa bòn rút; thói tục ấy cổ xưa đến mức "
        "và dường như tự nhiên đến nỗi, nếu có một vị quan tòa nào mà không ăn của đút, dân chúng sẽ thấy thật kỳ quặc và ngỡ như đầu óc quan có phần ngớ ngẩn.\n\n"
        "Viên quan chỉ dung nạp vào vòng thân cận vài ba kẻ tháo vát, ưa xu nịnh mưu mô, những tay chân tâm phúc luôn biết lợi dụng uy thế của quan "
        "để thỏa mãn tư lợi riêng. Sống cuộc đời vương giả, khinh bỉ kẻ hèn mọn, vơ vét của dân miễn sao tiền bạc đầy túi, dửng dưng với việc công, "
        "miệng ngọt ngào đãi bôi giả tạo với các quan chức đại diện nước Pháp, biến cả tỉnh lỵ mình cai quản thành một bồ thóc khổng lồ để ra sức "
        "bòn vét cho kỳ kiệt — đó chính là diện mạo chân thực của quan lại An Nam, từ phẩm trật cao nhất đến chức quan thấp nhất."
    )
    comm_mandarin = (
        "Bonnafont không ngần ngại bóc trần sự mục ruỗng của hệ thống quan lại phong kiến triều Nguyễn dưới chế độ bảo hộ của Pháp. "
        "Viên quan lúc này rơi vào thế lưỡng diện: vừa luồn cúi, xum xoe trước các thanh tra, công sứ Pháp, vừa tiếp tục duy trì bộ máy bóc lột, "
        "hạch sách người dân cùng khổ ở địa phương. Cụm từ châm biếm sâu cay 'dân thấy quan không ăn đút lót thì ngỡ quan ngớ ngẩn' phản ánh một "
        "thực trạng đau đớn về văn hóa hối lộ đã ăn sâu vào nếp sống thời bấy giờ."
    )
    add_chapter_with_plate("Quan Lại Triều Đình", "Le Mandarin", "page_063.png", text_mandarin, comm_mandarin)

    # ---------------------------------------------------------
    # Chương 3: Thầy Thông Ngôn (L'Interprète)
    # ---------------------------------------------------------
    text_interpreter = (
        "Thầy thông ngôn là mắt xích trung gian tối cần thiết nhưng cũng là kẻ khuynh đảo quyền lực bậc nhất trong guồng máy cai trị thuộc địa. "
        "Đứng giữa một bên là viên quan Pháp không biết một chữ tiếng bản xứ và một bên là đám dân chúng An Nam ngơ ngác không hiểu tiếng Tây, "
        "thầy thông nắm trong tay sinh mệnh, tiền tài và số phận của bao người.\n\n"
        "Chỉ cần dịch chệch đi nửa lời, thêm bớt một câu giải thích, thầy có thể biến trắng thành đen, biến tội nhân thành kẻ vô can và ngược lại. "
        "Khoác lên mình bộ âu phục hay chiếc áo dài the khăn đóng bóng bẩy, chân đi giày tây láng coong, thầy thông ngôn đi đứng nghênh ngang, "
        "nửa coi thường các viên quan bản xứ thủ cựu, nửa mỉm cười kín đáo trước sự ngây thơ của các ông Tây vừa chân ướt chân ráo sang xứ bảo hộ.\n\n"
        "Mọi đơn từ khiếu nại, mọi giao dịch thương mại hay tố tụng kiện cáo đều phải qua tay thầy. Vì lẽ đó, túi áo của thầy thông chẳng bao giờ rỗng, "
        "và tiếng tăm của thầy nơi chốn nha môn lẫy lừng không kém gì quan phụ mẫu."
    )
    comm_interpreter = (
        "Tầng lớp thông ngôn, ký lục xuất hiện như sản phẩm đặc thù của chế độ thực dân. Nhờ nắm giữ độc quyền về ngôn ngữ (tiếng Pháp), "
        "họ hình thành nên một tầng lớp 'trí thức thực dụng' mới, thường xuyên lợi dụng sự bất đồng ngôn ngữ giữa chính quyền thuộc địa và người dân "
        "để trục lợi cá nhân, tạo nên nhiều giai thoại châm biếm trong văn học hiện thực Việt Nam đầu thế kỷ XX."
    )
    add_chapter_with_plate("Thầy Thông Ngôn", "L'Interprète", "plate_9.png", text_interpreter, comm_interpreter)

    # ---------------------------------------------------------
    # Chương 4: Cu Li Kéo Xe & Phu Phen (Le Coolie)
    # ---------------------------------------------------------
    text_coolie = (
        "Cu li là một sinh linh nằm ở khoảng giữa con người và loài súc vật thồ hàng.\n\n"
        "Về hình dáng bên ngoài, anh ta là một con người; nhưng về công năng gánh vác, anh ta đảm nhiệm trọn vẹn chức phận của loài vật kéo cày thồ nặng. "
        "Ở đây, tôi muốn nói đến những phu khuân vác bám theo các đoàn quân viễn chinh suốt nhiều tháng ròng rã nơi rừng thiêng nước độc, "
        "chứ không đơn thuần là cánh cu li xe tay chốn phố xá — những kẻ ngày càng trở nên khó tính và đôi lúc còn dám ra điều kiện mặc cả trước khi cất bước.\n\n"
        "Người phu khuân vác có một ưu thế vượt trội so với lừa và la: anh ta có thể luồn lách qua những hẻm núi hiểm trở, những đầm lầy hiểm hóc mà loài vật "
        "phải chịu trói chân; anh ta lại cực kỳ dễ nuôi, chỉ cần nắm cơm đùm rau muống chấm tương mà mỗi ngày có thể cắn răng chạy bộ từ ba mươi đến ba mươi lăm cây số. "
        "Gầy gò, nhem nhuốc, khoác trên mình manh áo rách tả tơi, anh ta vừa chạy lon ton từng bước ngắn vừa chẳng bao giờ quên rút chiếc điếu cày bằng tre "
        "ra rít một hơi thuốc lào mỗi khi đoàn người tạm dừng nghỉ chân.\n\n"
        "Hễ nghe tiếng súng nổ đầu tiên nơi chiến trường, anh ta lập tức vứt phịch gánh hàng hay hòm đạn xuống đất rồi lủi nhanh vào bụi rậm ẩn nấp; "
        "đến khi tiếng súng dứt, anh ta lại lục tục chui ra... trừ phi anh ta đã men theo đường mòn trốn biệt tăm về làng. "
        "Thỉnh thoảng, người ta phải khích lệ lòng nhiệt thành của anh ta bằng những biện pháp cứng rắn răn đe, bởi người ta càng nhân từ đối đãi, "
        "anh ta lại càng chểnh mảng bước đi.\n\n"
        "Đối với chúng ta, người cu li là một lực lượng trợ thủ đắc lực không thể thiếu; và trong những cuộc hành quân thần tốc khắc nghiệt, "
        "chuyện nhìn thấy vài ba người phu ngã gục bên vệ đường rồi vĩnh viễn không bao giờ gượng dậy được nữa là điều chẳng hề hiếm hoi..."
    )
    comm_coolie = (
        "Một trong những đoạn văn tàn nhẫn và trần trụi nhất trong cuốn sách. Bonnafont đã lột tả số phận bi thảm của hàng vạn phu phen, "
        "cu li bị bắt lính, bắt phu để phục vụ cho các chiến dịch bình định và xây dựng công trình thuộc địa (như tuyến đường sắt răng cưa, đường sắt Bắc - Nam). "
        "Ngôn từ ví von người cu li như 'loài vật thồ hàng' phản ánh sự tàn bạo của chế độ thuộc địa, nhưng đồng thời cũng là bản cáo trạng lịch sử đanh thép "
        "về sự bóc lột sức lao động cùng cực của người Việt thời bấy giờ."
    )
    add_chapter_with_plate("Cu Li & Phu Khuân Vác", "Le Coolie", "page_035.png", text_coolie, comm_coolie)

    # ---------------------------------------------------------
    # Chương 5: Thằng Bồi Tư Gia (Le Boy) & Thằng Kéo Quạt (Le Boy Panka)
    # ---------------------------------------------------------
    text_boy = (
        "Thằng bồi là cái bóng không thể tách rời trong mọi ngôi nhà của người Âu kiều tại xứ Bắc Kỳ. "
        "Từ sáng sớm tinh mơ đến đêm khuya thanh vắng, nó lăng xăng chạy quanh: dọn bữa điểm tâm, đánh xi bóng loáng đôi giày da, là thẳng nếp áo sơ mi trắng, "
        "và lắng nghe mọi hiệu lệnh của ông chủ Tây.\n\n"
        "Nó nói thứ tiếng Pháp bồi kỳ dị — thứ ngôn ngữ chắp vá giữa các động từ nguyên mẫu và danh từ cụt lủn, thế nhưng ông chủ và thằng bồi lại hiểu nhau "
        "đến từng chân tơ kẽ tóc. Nó biết rõ ông chủ thích uống loại rượu nào, mấy giờ về nhà, và quý cô nào đang khiến trái tim ông chủ xao xuyến. "
        "Mọi khoản chi tiêu chợ búa hàng ngày đều qua tay nó, và dĩ nhiên, chẳng có bữa chợ nào mà thằng bồi lại quên 'nhón' lại vài hào tiền cắc bỏ túi riêng.\n\n"
        "Bên cạnh thằng bồi phòng là 'thằng bé kéo quạt' (Le boy panka). Giữa mùa hè Hà Nội oi ả hầm hập như lò lửa, chiếc quạt vải khổng lồ treo trên trần nhà "
        "chỉ đung đưa nhịp nhàng nhờ vào sợi dây thừng nối ra góc hiên — nơi một đứa bé An Nam ngồi co ro kéo dây đều đặn từ giờ này qua giờ khác. "
        "Mắt nó nhắm nghiền vì buồn ngủ, tay nó kéo theo quán tính như một chiếc máy sống, và chỉ cần nhịp quạt ngưng bặt một giây, một tiếng quát tháo sấm sét "
        "từ trong phòng sẽ lập tức đánh thức nó dậy."
    )
    comm_boy = (
        "Chiếc quạt panka và tầng lớp bồi bàn là nét sinh hoạt đặc thù của người da trắng tại các xứ thuộc địa nhiệt đới trước khi có điện và quạt máy. "
        "Hình ảnh đứa trẻ kéo quạt cặm cụi dưới cái nóng thiêu đốt phản ánh sự phân tầng giai cấp sâu sắc giữa lối sống hưởng thụ của kẻ cai trị "
        "và lao động rẻ mạt của trẻ em bản xứ."
    )
    add_chapter_with_plate("Thằng Bồi & Thằng Bé Kéo Quạt", "Le Boy & Le Boy Panka", "plate_9.png", text_boy, comm_boy)

    # ---------------------------------------------------------
    # Chương 6: Người Nhà Quê (Le Nhaqué)
    # ---------------------------------------------------------
    text_nhaque = (
        "Người nhà quê chính là người nông dân xứ Bắc Kỳ. Họ thuộc về đồng quê thôn dã, và trọn đời chỉ cặm cụi với mấy mẫu ruộng chiêm mùa, "
        "mảnh nương khoai sắn hay đôi ba khúc rạch bắt cá tôm.\n\n"
        "Ở vào cái thế như con lừa của triết gia Buridan — vừa đói vừa khát mà đành chịu chết mòn chết mỏi giữa một bên là chậu nước trong và một bên "
        "là máng cỏ khô — người nhà quê bị kẹp giữa hai làn đạn: một bên là giặc cướp (nghĩa quân kháng Pháp) đến đòi tiền lương thảo, "
        "và một bên là đám quan chức chính quyền bảo hộ đè đầu siết thuế; họ chẳng dám hé răng theo phe nào, và rốt cuộc luôn là kẻ giơ đầu chịu báng "
        "làm vật tế thần cho cả đôi bên.\n\n"
        "Chất phác, sợ sệt, sùng bái mê tín, người nhà quê chẳng bao giờ muốn rời bước khỏi lũy tre làng và gắn chặt cuộc đời mình với ngôi đình, ngôi chùa cổ kính. "
        "Vào những ngày hạn hán, dưới cái nắng chang chang như thiêu như đốt, anh ta như một cỗ máy tự động, cần mẫn múc từng gầu nước đổ vào ruộng lúa cằn. "
        "Dễ thỏa mãn với chút ít sản vật đạm bạc vì anh ta hầu như chưa từng biết đến sự tiện nghi của văn minh Tây phương, anh ta cứ thế bình thản sống êm đềm "
        "bên vợ dại con thơ, và quả thực cũng thấy mình hạnh phúc — bởi người đời thực sự hạnh phúc một khi họ tin rằng mình đang hạnh phúc.\n\n"
        "Luôn ngả theo kẻ mạnh hơn, người nhà quê sẽ chẳng ngần ngại phục vụ cho đại cuộc của chúng ta dẫu có phải liều rơi đầu, nếu anh ta tin chắc rằng "
        "có thể tìm thấy ở chúng ta một chỗ dựa chở che vững chắc chống lại những cuộc cướp bóc của các toán vũ trang, cũng như ngăn chặn những thói nhũng nhiễu, "
        "ức hiếp tàn bạo của đám cường hào chức dịch bản xứ."
    )
    comm_nhaque = (
        "Thuật ngữ 'Nhaqué' (Nhà quê) vốn là từ ngữ chỉ người nông dân Việt Nam mà người Pháp phiên âm lại và thường dùng với hàm ý miệt thị chốn đô thành. "
        "Tuy nhiên, qua ngòi bút Bonnafont, thân phận bi kịch của người nông dân vùng đồng bằng sông Hồng hiện lên vô cùng xót xa: bị mắc kẹt giữa sưu cao thuế nặng "
        "của thực dân và sự đàn áp của cường hào làng xã, họ thu mình sau lũy tre làng như cách duy nhất để sinh tồn."
    )
    add_chapter_with_plate("Người Nhà Quê / Nông Dân", "Le Nhaqué", "page_073.png", text_nhaque, comm_nhaque)

    # ---------------------------------------------------------
    # Chương 7: Cô Đầu & Đào Hát Ca Trù (La Chanteuse)
    # ---------------------------------------------------------
    text_chanteuse = (
        "Xin chớ vội lầm tưởng rằng tôi sắp sửa miêu tả trước mắt quý vị một nàng nữ thần săn bắn Diane kiều diễm, tự hào phô diễn đôi chân tuyệt mỹ "
        "hay khuôn ngực lấp ló sau làn sa mỏng; cũng đừng đem nàng so sánh với những cô đào lẳng lơ chốn sàn diễn Paris, khoác chiếc váy ngắn khêu gợi "
        "và buông lời lúng liếng đẩy đưa. Nàng đào hát nơi đây đích thực là một cô gái thành thị của chốn buồng khuê hơn là một nghệ sĩ kịch nghệ.\n\n"
        "Cái nơi mà nàng thủ diễn trọn vẹn nhất vai trò của mình, than ôi, lại chính là dưới tấm màn ngủ buông rủ trong phòng the kín đáo.\n\n"
        "Tài nghệ chuyên môn của nàng thực chất chỉ vỏn vẹn trong vài cử chỉ lười nhác phe phẩy chiếc quạt lụa, đôi ba động tác uốn lượn yêu kiều của cánh tay, "
        "vài khúc ngâm nga ru hồn êm ái đệm theo tiếng gõ phách lách cách và tiếng đàn đáy trầm đục của bác kép già ngồi xếp bằng bên cạnh. "
        "Đó là tất cả vốn liếng ngón nghề của nàng.\n\n"
        "Nàng không màng đến việc làm say mê cả khán phòng bằng kỹ nghệ thanh nhạc đỉnh cao; mục đích tối thượng của nàng là làm sao khiến cho quan khách "
        "say men rượu nếp, đắm chìm trong làn khói phù dung ngây ngất, để rồi ngoan ngoãn dốc cạn túi tiền thưởng cho nàng những phong bao hậu hĩnh."
    )
    comm_chanteuse = (
        "Bức tranh miêu tả không gian nhà hát cô đầu (ca trù) tại Hà Nội thời kỳ biến tướng đầu thế kỷ XX (khu vực phố Vạn Thái, Ngõ Sầm Công, Khâm Thiên sau này). "
        "Dưới góc nhìn của một người ngoại quốc như Bonnafont, vẻ đẹp thanh tao của nghệ thuật ca trù truyền thống (ngón đàn đáy, tiếng phách giòn giã) "
        "đã bị lu mờ bởi không khí ăn chơi hưởng lạc, hút thuốc phiện và mại dâm trá hình vốn đang nở rộ để phục vụ giới công chức, thương nhân thị thành."
    )
    add_chapter_with_plate("Cô Đầu & Đào Hát Ca Trù", "La Chanteuse", "page_027.png", text_chanteuse, comm_chanteuse)

    # ---------------------------------------------------------
    # Chương 8: Người Phụ Nữ Bản Xứ (La Con-gaïe)
    # ---------------------------------------------------------
    text_congai = (
        "Thật xa xôi biết bao cái hình ảnh người phụ nữ phương Tây — bậc nữ chúa ngự trị trong tổ ấm gia đình, người mà chỉ một nụ cười hàm tiếu "
        "cũng đủ làm nở đóa hoa tình yêu thanh tao diễm lệ!\n\n"
        "Người phụ nữ bản xứ (La congaï) nơi đây không được đối đãi như một người bạn đời bình đẳng hay một tri kỷ sẻ chia tâm sự, "
        "mà bị coi như một kẻ tôi đòi hèn mọn của đàn ông. Gánh vác trên vai trăm dâu đổ đầu tằm, lo toan mọi việc trong túp lều tranh lụp xụp, "
        "người đàn bà An Nam làm lụng quần quật nhọc nhằn hơn cả người chồng của thị; thế nhưng gã đàn ông, khi chia sẻ manh chiếu tre với vợ mình, "
        "lại đinh ninh rằng việc ấy đã là ân huệ tột bậc và phần thưởng quá đỗi hào phóng để bù đắp cho những nỗi gian lao của thị.\n\n"
        "Người đàn ông An Nam nhìn thấy ở vợ mình trước hết là chiếc nồi cơm luôn phải đầy ắp, và một kẻ luôn sẵn sàng đáp ứng những đòi hỏi bản năng thể xác thô thiển. "
        "Ở nơi người chồng, tuyệt nhiên vắng bóng chất thơ, không hề có một lý tưởng cao đẹp nào; tất cả chỉ là sự trần tục thô ráp, một sự chiếm hữu động vật.\n\n"
        "Hiếm khi mang nhan sắc kiều diễm, người phụ nữ quanh năm mệt mỏi, tàn tạ trước tuổi vì đòn gánh nặng trĩu trên vai qua năm tháng, với hàm răng đen nhánh "
        "và búng bã trầu liên tục nhổ ra đỏ lòm... khiến ta không khỏi chạnh lòng nhớ tiếc những người phụ nữ phương Tây kiều diễm quê nhà. "
        "Từ bờ môi hồng xinh xắn của nước Pháp hoa lệ cho đến cối xay trầu của xứ Đông Dương, ôi chao, cách biệt muôn trùng xiết bao!"
    )
    comm_congai = (
        "Một bức tranh phác họa đầy xót xa về thân phận người phụ nữ Việt Nam dưới chế độ phong kiến gia trưởng đè nặng. "
        "Dù Bonnafont nhìn họ bằng con mắt so sánh khắt khe của một người Pháp quen với chuẩn mực thẩm mỹ phương Tây, "
        "nhưng đoạn văn đã phản ánh chính xác đức hy sinh cam chịu, gánh nặng gia đình và sự bất công mà người phụ nữ An Nam phải gánh chịu suốt đời."
    )
    add_chapter_with_plate("Người Phụ Nữ Bản Xứ", "La Con-gaïe", "page_034.png", text_congai, comm_congai)

    # ---------------------------------------------------------
    # Chương 9: Kẻ Nhặt Ve Chai / Đồ Phế Thải (Le Biffin)
    # ---------------------------------------------------------
    text_biffin = (
        "Kẻ nhặt ve chai — tay cầm cây gậy sắt có móc nhọn để bới tìm từng mẩu bánh mì khô mốc, từng mảnh phế liệu có thể tái sử dụng — "
        "chẳng phải là hình ảnh xa lạ trên đường phố xứ Bắc Kỳ.\n\n"
        "Mỗi buổi sớm mai, những đứa trẻ gầy guộc rách rưới cùng những bà lão khốn cùng lúi húi sục sạo trong các sọt rác đặt trước cửa nhà dân phố Tây. "
        "Họ nhặt nhạnh từng mẩu giẻ rách, những chiếc vỏ đồ hộp rỉ sét, bó rau dập thối, cọng cỏ rác sân vườn, nút chai cũ, vỏ bao bì... "
        "tất cả mọi thứ mà người đời vứt bỏ, họ đều biết cách biến thành vật có ích.\n\n"
        "Vỏ hộp thiếc được đem bán lại cho các thợ gò thùng người Hoa; thức ăn thừa và rau dập dành để nuôi lợn, nuôi thỏ; những mảnh vải vụn chắp vá "
        "thành chiếc áo cái quần cho đám dân ngụ cư bần hàn. Nhưng hai thứ được săn lùng ráo riết nhất chính là vỏ chai thủy tinh và những chiếc hộp trà "
        "lót giấy thiếc. Mỗi chiếc vỏ chai có thể bán lại được một xu — một đồng xu quý giá đổi lấy bữa cháo lót dạ qua ngày."
    )
    comm_biffin = (
        "Nghề 'đồng nát, ve chai' trên các phố phường Hà Nội xưa. Bức ký họa cho thấy đời sống kinh tế tự phát của tầng lớp dân nghèo đô thị "
        "trong quá trình đô thị hóa dưới thời Pháp thuộc, nơi mọi mảnh phế phẩm của lối sống tiêu dùng phương Tây đều được tận dụng triệt để để sinh tồn."
    )
    add_chapter_with_plate("Kẻ Nhặt Ve Chai & Phế Liệu", "Le Biffin", "plate_12.png", text_biffin, comm_biffin)

    # ---------------------------------------------------------
    # Chương 10: Thầy Chùa & Nhà Sư (Le Bonze)
    # ---------------------------------------------------------
    text_bonze = (
        "Nép mình dưới bóng mát của những cây cổ thụ trăm năm, ngôi chùa Bắc Kỳ là cõi thoát tục thanh tịnh tách biệt hẳn với sự ồn ào bụi bặm của trần gian. "
        "Tại đây, thầy chùa — đầu cạo nhẵn thín, mình vận tấm áo nâu sồng giản dị, cổ đeo chuỗi tràng hạt — dành trọn những tháng ngày êm đềm "
        "bên tiếng mõ tụng kinh và làn khói trầm nghi ngút.\n\n"
        "Đối với dân làng, thầy chùa là cầu nối thiêng liêng giữa thế giới trần tục và cõi Tây phương cực lạc. Thầy chủ trì các buổi lễ cầu siêu cho người đã khuất, "
        "làm lễ cúng sao giải hạn cho kẻ ốm đau, và gieo quẻ xăm định mệnh cho những kẻ băn khoăn về tiền đồ. "
        "Thầy sống đạm bạc nhờ vào phẩm vật cúng dường của thập phương thiện nam tín nữ: vài thúng gạo nếp, nải chuối tiêu, đĩa oản đường.\n\n"
        "Tuy vậy, dưới lăng kính của người Pháp thực dụng, nếp sống tu hành ấy đôi khi bị coi là sự trốn tránh nghĩa vụ lao động và quân dịch; "
        "thế nhưng không ai có thể phủ nhận rằng, chính những ngôi chùa và các vị sư sãi là nơi lưu giữ linh hồn tâm linh, sự bình an và nếp sống thiện lương "
        "của người dân bản xứ trước những biến thiên nghiệt ngã của thời cuộc."
    )
    comm_bonze = (
        "Phật giáo dân gian xứ Bắc Kỳ trong con mắt người phương Tây. Bonnafont nhận ra sức ảnh hưởng to lớn của đạo Phật đối với đời sống tâm lý làng xã: "
        "dù bị chính quyền thực dân đánh thuế và giám sát chặt chẽ, ngôi chùa vẫn là nơi nương tựa tinh thần vững chắc nhất của người nông dân nghèo."
    )
    add_chapter_with_plate("Thầy Chùa & Chốn Cửa Thiền", "Le Bonze", "page_025.png", text_bonze, comm_bonze)

    # ---------------------------------------------------------
    # Chương 11: Tết Nguyên Đán Xứ Bắc Kỳ (Le Têt)
    # ---------------------------------------------------------
    text_tet = (
        "Tết là biến cố trọng đại nhất, thiêng liêng nhất và tưng bừng nhất trong một năm của toàn thể xứ An Nam. "
        "Dường như cả xã hội Bắc Kỳ ngừng thở, trút bỏ mọi nhọc nhằn lo toan thường nhật để bước vào một kỳ lễ hội bất tận kéo dài suốt nhiều ngày đêm.\n\n"
        "Mọi nợ nần trong năm cũ đều phải được thanh toán sòng phẳng trước thời khắc giao thừa; nhà cửa được quét dọn phong quang, trước sân dựng cây nêu "
        "trừ tà, câu đối đỏ dán khắp các cột nhà, và mùi hương trầm quyện với mùi thuốc pháo nổ đì đẹt khắp các ngõ phố. "
        "Từ viên quan lớn uy nghi cho đến người cu li khốn cùng nhất, ai nấy đều cố sắm sửa cho mình một manh áo mới tinh tươm để đi chúc Tết gia tộc, "
        "lạy tạ tổ tiên và viếng cảnh chùa chiền cầu may.\n\n"
        "Trong ba ngày Tết, cờ bạc được tự do công khai: những chiếu tôm điếm, xóc đĩa, bầu cua tôm cá mọc lên khắp các góc đình, bờ ao. "
        "Người An Nam có thể nhịn ăn nhịn mặc cả năm, nhưng ngày Tết thì dứt khoát mâm cỗ phải có bánh chưng xanh, thịt mỡ, dưa hành. "
        "Đó là thời khắc hòa giải, là niềm hy vọng mãnh liệt về một mùa màng tươi tốt và một tương lai bớt đi những đắng cay nhọc nhằn."
    )
    comm_tet = (
        "Bức tranh Tết cổ truyền Việt Nam cách đây hơn một thế kỷ. Bonnafont mô tả Tết không chỉ như một lễ hội văn hóa mà còn là một cơ chế tâm lý xã hội "
        "kỳ diệu giúp giải tỏa mọi căng thẳng, bất công giai cấp tích tụ trong suốt cả năm, đưa mọi người trở về nguồn cội tâm linh và tình làng nghĩa xóm."
    )
    add_chapter_with_plate("Tết Nguyên Đán Xứ Bắc Kỳ", "Le Têt", "page_003.png", text_tet, comm_tet)

    # ---------------------------------------------------------
    # Phụ lục: Từ điển xã hội học thuộc địa
    # ---------------------------------------------------------
    builder.new_page(running_header="PHỤ LỤC TỪ ĐIỂN XÃ HỘI HỌC BẮC KỲ ĐẦU THẾ KỶ XX")
    builder.add_center(builder.y_pos + 10, "PHỤ LỤC: TỪ ĐIỂN THUẬT NGỮ XÃ HỘI THUỘC ĐỊA", builder.font_bold, 13)
    builder.add_center(builder.y_pos + 26, "GIẢI NGHĨA CÁC TỪ LÓNG & DANH TỪ LỊCH SỬ TRONG TÁC PHẨM", builder.font_italic, 9.5)
    builder.y_pos += 38
    builder.curr_page.draw_line(pymupdf.Point(builder.margin_l, builder.y_pos - 6), pymupdf.Point(builder.margin_r, builder.y_pos - 6), color=(0.7, 0.3, 0.2), width=1)
    
    terms = [
        ("Bồi (Boy)", "Từ gốc tiếng Anh chỉ kẻ phục vụ nam giới trong gia đình người Âu kiều ở thuộc địa. Tại Việt Nam, từ 'bồi' đi vào ngôn ngữ hàng ngày (bồi bàn, bồi bếp, bồi phòng, nói tiếng Pháp bồi)."),
        ("Cu li (Coolie)", "Gốc từ tiếng Hindi/Bồ Đào Nha chỉ người lao động chân tay cực nhọc, phu vác, kéo xe tay. Thời Pháp thuộc, cu li là lực lượng lao động đông đảo chịu nhiều áp bức nhất."),
        ("Con gái (Congaï)", "Người Pháp dùng từ này để phiên âm chữ 'con gái' tiếng Việt, nhưng dùng để chỉ chung phụ nữ bản xứ, người tình hoặc vợ bé người Việt của binh lính, kiều dân Pháp."),
        ("Nhà quê (Nhaqué)", "Phiên âm chữ 'nhà quê', được người Pháp dùng để chỉ người nông dân Bắc Kỳ thuần phác, gắn bó với ruộng đồng và phong tục làng xã cổ truyền."),
        ("Lính khố đỏ (Linh)", "Lực lượng lính tập người Việt phục vụ trong quân đội chính quy của Pháp tại Đông Dương, phân biệt với lính khố xanh (bảo an địa phương) và lính cơ (lính lệ phủ huyện)."),
        ("Quạt Panka", "Chiếc quạt vải lớn đóng khung treo ngang trần nhà, kéo bằng dây thừng qua ròng rọc do một phu kéo quạt ngồi ngoài hiên giật nhịp nhàng để làm mát phòng trước khi có quạt điện."),
        ("Tiền trinh, tiền kẽm", "Các đơn vị tiền tệ cổ truyền của triều đình phong kiến bằng đồng hoặc kẽm xâu thành từng chuỗi, lưu hành song song với đồng bạc Đông Dương (Piastre de commerce)."),
        ("Ca trù / Hát ả đào", "Loại hình nghệ thuật diễn xướng bác học truyền thống Bắc Bộ gồm đào nương gõ phách hát, kép đàn gảy đàn đáy và quan viên điểm trống chầu, đầu thế kỷ XX biến tướng thành các nhà chứa trá hình.")
    ]
    
    for term, definition in terms:
        if builder.y_pos + 28 > builder.margin_b:
            builder.new_page(running_header="PHỤ LỤC TỪ ĐIỂN XÃ HỘI HỌC BẮC KỲ ĐẦU THẾ KỶ XX")
        builder.curr_tw.append(pymupdf.Point(builder.margin_l, builder.y_pos), f"★ {term}:", font=builder.font_bold, fontsize=9.5)
        builder.y_pos += 12
        builder.add_text_block(definition, builder.font_reg, 9, line_height=13, indent=12, space_after=6)

    # Save to desktop and library
    out_desktop = r"C:\Users\Admin\Desktop\[Bản Dịch Tiếng Việt] Louis Bonnafont - Muôn Hạng Dân Bắc Kỳ (Types Tonkinois 1903).pdf"
    out_lib = r"C:\Users\Admin\Desktop\Sách\Lịch sử & Biên niên sử\01_Lịch sử Việt Nam\[Bản Dịch Tiếng Việt] Louis Bonnafont - Muôn Hạng Dân Bắc Kỳ (Types Tonkinois 1903).pdf"
    
    pages, sz = builder.save(out_desktop)
    shutil.copy2(out_desktop, out_lib)
    print(f"SUCCESS: Generated {pages} pages, {sz:.2f} MB")
    print(f"Saved to Desktop: {out_desktop}")
    print(f"Saved to Library: {out_lib}")

if __name__ == "__main__":
    build_full_book()
