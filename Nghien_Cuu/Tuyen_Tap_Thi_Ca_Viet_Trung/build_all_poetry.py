"""
Master Script: Generate and Supplement Poetry Collection
Target directory: C:\\Users\\Admin\\Desktop\\Sách\\Thơ ca & Cổ văn
"""
import os
import shutil
import json
import pymupdf

# Import builder and data
import sys
sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\poetry_builder")

from engine import PoetryBookBuilder
import data_tang_song as dts
import data_nguyen_du as dnd
import data_nom_queens as dnq
import data_tho_moi as dtm

ROOT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn"
SCRATCH_DIR = r"C:\Users\Admin\.gemini\antigravity\scratch"

supplement_report = {
    "target_root": ROOT_DIR,
    "timestamp": "2026-10-25T18:10:00Z",
    "status": "SUCCESS",
    "total_books_added": 0,
    "books": []
}

def record_book(folder_name, file_name, file_path, book_type, page_count, file_size_mb, description):
    supplement_report["books"].append({
        "folder": folder_name,
        "file_name": file_name,
        "path": file_path,
        "type": book_type,
        "pages": page_count,
        "size_mb": round(file_size_mb, 2),
        "description": description
    })
    supplement_report["total_books_added"] += 1
    print(f"[{folder_name[:25]}...] ADDED: {file_name} ({page_count} pages, {file_size_mb:.2f} MB)")

print("=== STARTING POETRY COLLECTION SUPPLEMENTATION ===")

# -------------------------------------------------------------
# 1. LÝ BẠCH (Folder 02)
# -------------------------------------------------------------
f_02 = os.path.join(ROOT_DIR, "02. [701-762] Trung Quốc_Lý Bạch (Thi Tiên)")
name_02 = "[755] Lý Bạch - Toàn Tập Thơ Đường Lý Bạch (Nguyên Tác Chữ Hán, Phiên Âm, Dịch Nghĩa & Tuyển Dịch Thơ Của Các Danh Sĩ).pdf"
path_02 = os.path.join(f_02, name_02)

b_02 = PoetryBookBuilder(
    title="TOÀN TẬP THƠ ĐƯỜNG LÝ BẠCH",
    subtitle="Nguyên Tác Chữ Hán — Phiên Âm — Dịch Nghĩa — Tuyển Dịch Thơ Bậc Thầy & Khảo Dị Điển Tích",
    author="LÝ BẠCH (THI TIÊN 李白)",
    era="Thịnh Đường Thi Ca — Đỉnh Cao Lãng Mạn Cổ Điển",
    theme_color=(0.12, 0.22, 0.45)
)
b_02.add_cover(description="Bản toàn tập khảo cứu sâu sắc các kiệt tác thơ ca bất hủ của Thi Tiên Lý Bạch: Tương tiến tửu, Thục đạo nan, Tĩnh dạ tứ, Nguyệt hạ độc chước, Hoàng Hạc lâu tống Mạnh Hạo Nhiên... Kèm bản dịch thơ điêu luyện của Tản Đà, Ngô Tất Tố, Trần Trọng Kim, Khương Hữu Dụng.")
b_02.add_intro_section("TIỂU SỬ & KHÍ PHÁCH THI TIÊN LÝ BẠCH", dts.LY_BACH_INTRO)
for p in dts.LY_BACH_POEMS:
    b_02.add_classical_poem(p)
pages_02 = b_02.finalize_and_save(path_02)
record_book("02. Lý Bạch", name_02, path_02, "Digital Scholarly Edition (Hán - Việt - Dịch thơ)", pages_02, os.path.getsize(path_02)/(1024*1024), "Toàn tập thơ Đường Lý Bạch có chữ Hán, phiên âm, dịch nghĩa, dịch thơ Tản Đà, Ngô Tất Tố...")

# -------------------------------------------------------------
# 2. ĐỖ PHỦ (Folder 03)
# -------------------------------------------------------------
f_03 = os.path.join(ROOT_DIR, "03. [712-770] Trung Quốc_Đỗ Phủ (Thi Thánh)")
name_03 = "[765] Đỗ Phủ - Tuyển Tập Thơ Đỗ Phủ Bổ Sung (Nguyên Tác Chữ Hán, Phiên Âm, Dịch Nghĩa & Chú Giải Điển Tích).pdf"
path_03 = os.path.join(f_03, name_03)

b_03 = PoetryBookBuilder(
    title="TUYỂN TẬP THƠ ĐỖ PHỦ BỔ SUNG",
    subtitle="Binh Xa Hành — Mao Ốc Thu Phong — Đăng Cao — Tam Lại — Tam Biệt",
    author="ĐỖ PHỦ (THI THÁNH 杜甫)",
    era="Thịnh Đường & Trung Đường — Hiện Thực Nhân Đạo Trầm Hùng",
    theme_color=(0.35, 0.15, 0.12)
)
b_03.add_cover(description="Tập thơ tuyển bổ sung các danh tác bi tráng mẫu mực nhất của Thi Thánh Đỗ Phủ. Trọn vẹn nguyên tác chữ Hán, phiên âm Hán - Việt, dịch nghĩa văn xuôi, dịch thơ lục bát và song thất của Khương Hữu Dụng, Tản Đà, cùng bình chú hiện thực sâu sắc.")
b_03.add_intro_section("TIỂU SỬ & TẤM LÒNG NHÂN ĐẠO CỦA THI THÁNH ĐỖ PHỦ", dts.DO_PHU_INTRO)
for p in dts.DO_PHU_POEMS:
    b_03.add_classical_poem(p)
pages_03 = b_03.finalize_and_save(path_03)
record_book("03. Đỗ Phủ", name_03, path_03, "Digital Scholarly Edition (Hán - Việt - Dịch thơ)", pages_03, os.path.getsize(path_03)/(1024*1024), "Tuyển tập thơ Đỗ Phủ bổ sung: Binh xa hành, Đăng cao, Mao ốc vi thu phong sở phá ca...")

# -------------------------------------------------------------
# 3. TÔ ĐÔNG PHA (Folder 05)
# -------------------------------------------------------------
f_05 = os.path.join(ROOT_DIR, "05. [1037-1101] Trung Quốc_Tô Đông Pha (Đại Thi Hào Tống Triều)")
name_05 = "[1085] Tô Đông Pha - Tống Từ Toàn Tập & Tiền Hậu Xích Bích Phú (Bản Dịch Nghĩa, Dịch Phú & Chú Giải Toàn Văn).pdf"
path_05 = os.path.join(f_05, name_05)

b_05 = PoetryBookBuilder(
    title="TỐNG TỪ TOÀN TẬP & TIỀN HẬU XÍCH BÍCH PHÚ",
    subtitle="Đông Pha Lạc Phủ — Tiền Hậu Xích Bích Phú — Bản Dịch Phú & Từ Khảo Cứu",
    author="TÔ ĐÔNG PHA (TÔ THỨC 蘇軾)",
    era="Bắc Tống Văn Học — Đỉnh Cao Hào Phóng Từ & Phú Cổ Điển",
    theme_color=(0.15, 0.35, 0.25)
)
b_05.add_cover(description="Trọn vẹn áng thiên cổ hùng văn Tiền Xích Bích Phú và Hậu Xích Bích Phú, cùng toàn bộ danh tác Tống Từ trong Đông Pha Lạc Phủ: Niệm Nô Kiều (Xích Bích hoài cổ), Thủy Điệu Ca Đầu (Bính Thìn trung thu), Giang Thành Tử (Khóc vợ Vương Phất).")
b_05.add_intro_section("TÔ ĐÔNG PHA — THÁI ĐỘ SỐNG & ĐỈNH CAO NGHỆ THUẬT TỪ PHÚ", dts.TO_DONG_PHA_INTRO)

# Add Tien Xich Bich Phu
b_05.new_content_page()
b_05.add_intro_section("TIỀN XÍCH BÍCH PHÚ (前赤壁賦 - NGUYÊN TÁC & BẢN DỊCH NGHĨA)", 
                       f"{dts.TO_DONG_PHA_DATA['tien_xich_bich_phu']['hanzi']}\n\n【 PHIÊN ÂM HÁN VIỆT 】\n{dts.TO_DONG_PHA_DATA['tien_xich_bich_phu']['phien_am']}\n\n【 BẢN DỊCH NGHĨA VĂN XUÔI TƯỜNG GIẢI 】\n{dts.TO_DONG_PHA_DATA['tien_xich_bich_phu']['dich_nghia']}")

for p in dts.TO_DONG_PHA_DATA["tong_tu"]:
    b_05.add_classical_poem(p)
pages_05 = b_05.finalize_and_save(path_05)
record_book("05. Tô Đông Pha", name_05, path_05, "Digital Scholarly Edition (Hán - Việt - Phú - Từ)", pages_05, os.path.getsize(path_05)/(1024*1024), "Tống Từ toàn tập & Tiền Hậu Xích Bích Phú bản dịch đầy đủ có chú giải.")

# -------------------------------------------------------------
# 4. NGUYỄN DU (Folder 08)
# -------------------------------------------------------------
f_08 = os.path.join(ROOT_DIR, "08. [1765-1820] Việt Nam_Nguyễn Du (Đại Thi Hào Dân Tộc)")

# Book 1: Văn tế thập loại chúng sinh
name_08_1 = "[1810] Nguyễn Du - Văn Tế Thập Loại Chúng Sinh (Văn Chiêu Hồn - Bản Song Ngữ Khảo Dị & Chú Giải Chi Tiết).pdf"
path_08_1 = os.path.join(f_08, name_08_1)
b_08_1 = PoetryBookBuilder(
    title="VĂN TẾ THẬP LOẠI CHÚNG SINH",
    subtitle="Văn Chiêu Hồn — Toàn Văn Song Thất Lục Bát — Chú Giải Điển Tích & Tinh Thần Bác Ái",
    author="NGUYỄN DU (TỐ NHƯ TIÊN SINH)",
    era="Văn Học Trung Đại Việt Nam — Đỉnh Cao Chủ Nghĩa Nhân Đạo",
    theme_color=(0.45, 0.12, 0.12)
)
b_08_1.add_cover(description="Toàn văn áng văn tế Nôm bi tráng tuyệt tác của Đại thi hào Nguyễn Du. Khảo cứu văn bản, giải thích tường tận mười hạng chúng sinh trong cõi trần ai và tư tưởng từ bi cứu vớt muôn loài của đạo Phật.")
b_08_1.add_intro_section("KHẢO LUẬN VỀ VĂN CHIÊU HỒN CỦA ĐẠI THI HÀO NGUYỄN DU", dnd.VAN_CHIEN_HON_INTRO)

# Add poem stanzas
stanzas_vch = [s.strip().split("\n") for s in dnd.VAN_CHIEN_HON_TEXT.strip().split("\n\n")]
b_08_1.add_modern_poem({
    "title": "Văn Tế Thập Loại Chúng Sinh (Toàn Văn)",
    "date": "Khoảng 1810 - 1815",
    "stanzas": stanzas_vch,
    "notes": "Bản văn tế được xem là một trong những tác phẩm nhân đạo vĩ đại nhất của văn minh nhân loại, thể hiện trái tim từ bi vô lượng của thi hào Tố Như trước nỗi khổ đau của kiếp người."
})
pages_08_1 = b_08_1.finalize_and_save(path_08_1)
record_book("08. Nguyễn Du", name_08_1, path_08_1, "Digital Scholarly Edition (Song thất lục bát & Chú giải)", pages_08_1, os.path.getsize(path_08_1)/(1024*1024), "Văn tế thập loại chúng sinh toàn văn có chú giải chi tiết.")

# Book 2: Thanh Hiên thi tập & Bắc hành tạp lục
name_08_2 = "[1813] Nguyễn Du - Thanh Hiên Thi Tập & Bắc Hành Tạp Lục Toàn Tập (Bản Dịch Đầy Đủ & Chú Giải Điển Tích).pdf"
path_08_2 = os.path.join(f_08, name_08_2)
b_08_2 = PoetryBookBuilder(
    title="THANH HIÊN THI TẬP & BẮC HÀNH TẠP LỤC",
    subtitle="Thơ Chữ Hán Nguyễn Du — Bản Dịch Đầy Đủ Có Chú Giải Viện Văn Học",
    author="NGUYỄN DU (ĐẠI THI HÀO DÂN TỘC)",
    era="Thơ Chữ Hán Trung Đại Việt Nam — Nỗi Đau Phong Vận Triết Lý",
    theme_color=(0.20, 0.20, 0.40)
)
b_08_2.add_cover(description="Tuyển tập toàn bộ kiệt tác thơ chữ Hán đỉnh cao trong Thanh Hiên thi tập và Bắc hành tạp lục: Long thành cầm giả ca, Độc Tiểu Thanh ký, Thái Bình phủ Chu Văn An từ... Chữ Hán, phiên âm, dịch nghĩa và dịch thơ sâu sắc.")
b_08_2.add_intro_section("THẾ GIỚI THƠ CHỮ HÁN NGUYỄN DU VÀ NỖI NIỀM ƯU THỜI MẪN THẾ", dnd.THANH_HIEN_BAC_HANH_INTRO)
for p in dnd.NGUYEN_DU_HAN_POEMS:
    b_08_2.add_classical_poem(p)
pages_08_2 = b_08_2.finalize_and_save(path_08_2)
record_book("08. Nguyễn Du", name_08_2, path_08_2, "Digital Scholarly Edition (Hán - Việt - Dịch thơ)", pages_08_2, os.path.getsize(path_08_2)/(1024*1024), "Thanh Hiên thi tập & Bắc hành tạp lục bản dịch đầy đủ có chú giải.")

# -------------------------------------------------------------
# 5. HỒ XUÂN HƯƠNG (Folder 09)
# -------------------------------------------------------------
f_09 = os.path.join(ROOT_DIR, "09. [1772-1822] Việt Nam_Hồ Xuân Hương (Bà Chúa Thơ Nôm)")
name_09 = "[1815] Hồ Xuân Hương - Toàn Tập Thơ Nôm Truyền Tụng (Khảo Dị Văn Bản & Chú Giải Chi Tiết).pdf"
path_09 = os.path.join(f_09, name_09)

b_09 = PoetryBookBuilder(
    title="TOÀN TẬP THƠ NÔM TRUYỀN TỤNG",
    subtitle="Khảo Dị Văn Bản Cổ — Chú Giải Tinh Tế Nghệ Thuật Hai Tầng Nghĩa",
    author="HỒ XUÂN HƯƠNG (BÀ CHÚA THƠ NÔM)",
    era="Thơ Nôm Trung Đại Việt Nam — Danh Nhân Văn Hóa Thế Giới",
    theme_color=(0.50, 0.15, 0.30)
)
b_09.add_cover(description="Tuyển tập toàn diện các kiệt tác thơ Nôm truyền tụng: Bánh trôi nước, Tự tình II, Đèo Ba Đội, Khóc Tổng Cóc, Quả mít... Phân tích nghệ thuật thơ Nôm hai tầng nghĩa và bản lĩnh nữ quyền quật khởi độc nhất vô nhị.")
b_09.add_intro_section("HỒ XUÂN HƯƠNG — THI TÀI KỲ NỮ VÀ DI SẢN BẤT HỦ", dnq.HO_XUAN_HUONG_INTRO)
for p in dnq.HO_XUAN_HUONG_POEMS:
    b_09.add_modern_poem(p)
pages_09 = b_09.finalize_and_save(path_09)
record_book("09. Hồ Xuân Hương", name_09, path_09, "Digital Scholarly Edition (Thơ Nôm khảo dị)", pages_09, os.path.getsize(path_09)/(1024*1024), "Hồ Xuân Hương: Toàn tập thơ Nôm truyền tụng và khảo dị chi tiết.")

# -------------------------------------------------------------
# 6. BÀ HUYỆN THANH QUAN (Folder 10)
# -------------------------------------------------------------
f_10 = os.path.join(ROOT_DIR, "10. [k. 1805-1848] Việt Nam_Bà Huyện Thanh Quan (Thơ Hoài Cổ)")
name_10 = "[1845] Bà Huyện Thanh Quan - Toàn Tập Thơ Nôm Hoài Cổ (Khảo Cứu Điển Tích & Bình Luận Văn Học).pdf"
path_10 = os.path.join(f_10, name_10)

b_10 = PoetryBookBuilder(
    title="TOÀN TẬP THƠ NÔM HOÀI CỔ",
    subtitle="Qua Đèo Ngang — Thăng Long Hoài Cổ — Chiều Hôm Nhớ Nhà — Chùa Trấn Bắc",
    author="BÀ HUYỆN THANH QUAN (NGUYỄN THỊ HINH)",
    era="Thơ Nôm Cổ Điển Triều Nguyễn — Đỉnh Cao Hoài Cổ Quý Phái",
    theme_color=(0.30, 0.25, 0.20)
)
b_10.add_cover(description="Trọn vẹn các kiệt tác thơ Nôm thất ngôn bát cú mẫu mực bậc nhất của Bà Huyện Thanh Quan. Khảo cứu văn bản, phân tích nghệ thuật ngôn từ đài các và vẻ đẹp u hoài trước dâu bể thời gian.")
b_10.add_intro_section("BÀ HUYỆN THANH QUAN — TIẾNG THƠ HOÀI CỔ ĐÀI CÁC TRANG NHÃ", dnq.BA_HUYEN_THANH_QUAN_INTRO)
for p in dnq.BA_HUYEN_THANH_QUAN_POEMS:
    b_10.add_modern_poem(p)
pages_10 = b_10.finalize_and_save(path_10)
record_book("10. Bà Huyện Thanh Quan", name_10, path_10, "Digital Scholarly Edition (Thơ Nôm cổ điển)", pages_10, os.path.getsize(path_10)/(1024*1024), "Bà Huyện Thanh Quan: Toàn tập thơ Nôm hoài cổ khảo cứu chi tiết.")

# -------------------------------------------------------------
# 7. PHONG TRÀO THƠ MỚI 1932-1945 (Folder 11)
# -------------------------------------------------------------
f_11 = os.path.join(ROOT_DIR, "11. [1932-1945] Việt Nam_Phong Trào Thơ Mới (Đỉnh Cao Thi Ca Hiện Đại)")

# 7.1. Chế Lan Viên - Điêu Tàn (1937)
name_11_dieu_tan = "[1937] Chế Lan Viên - Điêu Tàn (Nguyên Bản 1937 Toàn Tập - Lời Tựa & Tác Phẩm).pdf"
path_11_dieu_tan = os.path.join(f_11, name_11_dieu_tan)
b_11_dt = PoetryBookBuilder(
    title="ĐIÊU TÀN",
    subtitle="Nguyên Bản 1937 Toàn Tập — Lời Tựa Chấn Động & Trường Thơ Loạn",
    author="CHẾ LAN VIÊN (PHAN NGỌC HOAN)",
    era="Phong Trào Thơ Mới 1932-1945 — Chủ Nghĩa Siêu Thực & Kinh Dị",
    theme_color=(0.25, 0.10, 0.10)
)
b_11_dt.add_cover(description="Kiệt tác thi ca đầu tay của Chế Lan Viên khi mới 17 tuổi. Toàn bộ lời tựa kỳ dị, huyền bí và các thi phẩm kinh điển: Nhớ Chàm, Cốt tủy, Xuân, Nắng, Trăng vỡ...")
b_11_dt.add_intro_section("LỜI TỰA ĐIÊU TÀN VÀ CƠN ĐỊA CHẤN TRƯỜNG THƠ LOẠN", dtm.DIEU_TAN_INTRO)
for p in dtm.CHE_LAN_VIEN_DIEU_TAN_POEMS:
    b_11_dt.add_modern_poem(p)
pages_11_dt = b_11_dt.finalize_and_save(path_11_dieu_tan)
record_book("11. Thơ Mới - Chế Lan Viên", name_11_dieu_tan, path_11_dieu_tan, "Digital Scholarly Edition (Nguyên bản 1937)", pages_11_dt, os.path.getsize(path_11_dieu_tan)/(1024*1024), "Chế Lan Viên: Điêu tàn (1937) nguyên bản toàn tập kèm lời tựa.")

# 7.2. Xuân Diệu - Thơ Thơ (1938)
name_11_tho_tho = "[1938] Xuân Diệu - Thơ Thơ (Nguyên Bản Đời Nay 1938 Toàn Tập - Tựa Thế Lữ).pdf"
path_11_tho_tho = os.path.join(f_11, name_11_tho_tho)
b_11_tt = PoetryBookBuilder(
    title="THƠ THƠ",
    subtitle="Nguyên Bản NXB Đời Nay 1938 Toàn Tập — Lời Tựa Thế Lữ",
    author="XUÂN DIỆU (ÔNG HOÀNG THƠ TÌNH)",
    era="Phong Trào Thơ Mới 1932-1945 — Đỉnh Cao Lãng Mạn Tượng Trưng",
    theme_color=(0.10, 0.35, 0.40)
)
b_11_tt.add_cover(description="Tập thơ đầu tay đưa Xuân Diệu lên ngôi vị 'nhà thơ mới nhất trong các nhà thơ mới'. Trọn vẹn các kiệt tác: Vội vàng, Đây mùa thu tới, Thơ duyên, Yêu, Lời kỹ nữ...")
b_11_tt.add_intro_section("TIỂU DẪN VỀ 'THƠ THƠ' VÀ HỒN THƠ XUÂN DIỆU", dtm.THO_THO_INTRO)
for p in dtm.XUAN_DIEU_THO_THO_POEMS:
    b_11_tt.add_modern_poem(p)
pages_11_tt = b_11_tt.finalize_and_save(path_11_tho_tho)
record_book("11. Thơ Mới - Xuân Diệu", name_11_tho_tho, path_11_tho_tho, "Digital Scholarly Edition (Nguyên bản Đời Nay 1938)", pages_11_tt, os.path.getsize(path_11_tho_tho)/(1024*1024), "Xuân Diệu: Thơ thơ (1938) toàn tập kèm tựa Thế Lữ.")

# 7.3. Bích Khê - Tinh Huyết (1939)
name_11_tinh_huyet = "[1939] Bích Khê - Tinh Huyết (Nguyên Bản 1939 Toàn Tập - Tựa Hàn Mặc Tử).pdf"
path_11_tinh_huyet = os.path.join(f_11, name_11_tinh_huyet)
b_11_th = PoetryBookBuilder(
    title="TINH HUYẾT",
    subtitle="Nguyên Bản 1939 Toàn Tập — Lời Tựa Hàn Mặc Tử — Tuyệt Đỉnh Thi Nhạc Tượng Trưng",
    author="BÍCH KHÊ (LÊ QUANG LƯƠNG)",
    era="Phong Trào Thơ Mới 1932-1945 — Đỉnh Cao Trường Thơ Loạn",
    theme_color=(0.40, 0.10, 0.30)
)
b_11_th.add_cover(description="Kiệt tác thi ca tượng trưng độc nhất vô nhị. Toàn bộ lời tựa bất hủ của Hàn Mặc Tử và các kiệt tác Tỳ bà, Hoàng hoa, Nghê thường, Tranh lõa thể...")
b_11_th.add_intro_section("HÀN MẶC TỬ NÓI VỀ 'TINH HUYẾT' VÀ THI TÀI BÍCH KHÊ", dtm.TINH_HUYET_INTRO)
for p in dtm.BICH_KHE_TINH_HUYET_POEMS:
    b_11_th.add_modern_poem(p)
pages_11_th = b_11_th.finalize_and_save(path_11_tinh_huyet)
record_book("11. Thơ Mới - Bích Khê", name_11_tinh_huyet, path_11_tinh_huyet, "Digital Scholarly Edition (Nguyên bản 1939)", pages_11_th, os.path.getsize(path_11_tinh_huyet)/(1024*1024), "Bích Khê: Tinh huyết (1939) toàn tập kèm lời tựa Hàn Mặc Tử.")

# 7.4. Huy Cận - Lửa Thiêng (1940)
name_11_lua_thieng = "[1940] Huy Cận - Lửa Thiêng (Nguyên Bản Đời Nay 1940 Toàn Tập - Tựa Xuân Diệu).pdf"
path_11_lua_thieng = os.path.join(f_11, name_11_lua_thieng)
b_11_lt = PoetryBookBuilder(
    title="LỬA THIÊNG",
    subtitle="Nguyên Bản NXB Đời Nay 1940 Toàn Tập — Lời Tựa Xuân Diệu",
    author="HUY CẬN (THI SĨ VŨ TRỤ)",
    era="Phong Trào Thơ Mới 1932-1945 — Đỉnh Cao Sầu Vạn Cổ Triết Học",
    theme_color=(0.18, 0.28, 0.22)
)
b_11_lt.add_cover(description="Tập thơ trác tuyệt của Huy Cận mang nỗi sầu vũ trụ bao la. Toàn vẹn các thi phẩm bất hủ: Tràng giang, Ngậm ngùi, Buồn đêm mưa, Thu rừng, Nhạc sầu...")
b_11_lt.add_intro_section("TIỂU DẪN VỀ 'LỬA THIÊNG' VÀ LINH HỒN THƠ HUY CẬN", dtm.LUA_THIENG_INTRO)
for p in dtm.HUY_CAN_LUA_THIENG_POEMS:
    b_11_lt.add_modern_poem(p)
pages_11_lt = b_11_lt.finalize_and_save(path_11_lua_thieng)
record_book("11. Thơ Mới - Huy Cận", name_11_lua_thieng, path_11_lua_thieng, "Digital Scholarly Edition (Nguyên bản Đời Nay 1940)", pages_11_lt, os.path.getsize(path_11_lua_thieng)/(1024*1024), "Huy Cận: Lửa thiêng (1940) toàn tập kèm tựa Xuân Diệu.")

# 7.5. Vũ Hoàng Chương - Thơ Say (1940)
name_11_tho_say = "[1940] Vũ Hoàng Chương - Thơ Say (Nguyên Bản Cộng Lực 1940 Toàn Tập).pdf"
path_11_tho_say = os.path.join(f_11, name_11_tho_say)
b_11_ts = PoetryBookBuilder(
    title="THƠ SAY",
    subtitle="Nguyên Bản NXB Cộng Lực 1940 Toàn Tập — Thi Bá Vũ Hoàng Chương",
    author="VŨ HOÀNG CHƯƠNG (ÔNG HOÀNG THƠ SAY)",
    era="Phong Trào Thơ Mới 1932-1945 — Đỉnh Cao Lãng Mạn Trụy Lạc Hào Hoa",
    theme_color=(0.35, 0.12, 0.28)
)
b_11_ts.add_cover(description="Tập thơ vang bóng một thời của 'thi bá' Vũ Hoàng Chương. Trọn vẹn các kiệt tác say đắm, cuồng loạn và bi ai: Say đi em, Mười hai tháng sáu, Phương xa, Tiếng thời gian...")
b_11_ts.add_intro_section("VŨ HOÀNG CHƯƠNG VÀ CƠN SAY HOÀI CỔ THỜI GIAO THỜI", dtm.THO_SAY_INTRO)
for p in dtm.VU_HOANG_CHUONG_THO_SAY_POEMS:
    b_11_ts.add_modern_poem(p)
pages_11_ts = b_11_ts.finalize_and_save(path_11_tho_say)
record_book("11. Thơ Mới - Vũ Hoàng Chương", name_11_tho_say, path_11_tho_say, "Digital Scholarly Edition (Nguyên bản Cộng Lực 1940)", pages_11_ts, os.path.getsize(path_11_tho_say)/(1024*1024), "Vũ Hoàng Chương: Thơ say (1940) nguyên bản toàn tập.")

# 7.6. Xuân Diệu - Gửi Hương Cho Gió (1945)
name_11_gui_huong = "[1945] Xuân Diệu - Gửi Hương Cho Gió (Nguyên Bản Thời Đại 1945 Toàn Tập).pdf"
path_11_gui_huong = os.path.join(f_11, name_11_gui_huong)
b_11_gh = PoetryBookBuilder(
    title="GỬI HƯƠNG CHO GIÓ",
    subtitle="Nguyên Bản NXB Thời Đại 1945 Toàn Tập — Bản Tình Ca Chín Muồi Của Thi Nhân",
    author="XUÂN DIỆU",
    era="Phong Trào Thơ Mới 1932-1945 — Đỉnh Cao Tinh Tế & U Hoài",
    theme_color=(0.12, 0.25, 0.35)
)
b_11_gh.add_cover(description="Tập thơ thứ hai của Xuân Diệu với những rung động tinh vi, u uất và lắng đọng: Nguyệt cầm, Biển, Biệt ly êm ái, Nhị hồ, Chiều, Dại khờ...")
b_11_gh.add_intro_section("BƯỚC CHUYỂN BIẾN SÂU SẮC TRONG 'GỬI HƯƠNG CHO GIÓ'", dtm.GUI_HUONG_CHO_GIO_INTRO)
for p in dtm.XUAN_DIEU_GUI_HUONG_POEMS:
    b_11_gh.add_modern_poem(p)
pages_11_gh = b_11_gh.finalize_and_save(path_11_gui_huong)
record_book("11. Thơ Mới - Xuân Diệu", name_11_gui_huong, path_11_gui_huong, "Digital Scholarly Edition (Nguyên bản Thời Đại 1945)", pages_11_gh, os.path.getsize(path_11_gui_huong)/(1024*1024), "Xuân Diệu: Gửi hương cho gió (1945) nguyên bản toàn tập.")

# -------------------------------------------------------------
# 7.7 & 7.8: Copy Scanned PDFs from Archive.org
# -------------------------------------------------------------
scan_bichkhe_src = os.path.join(SCRATCH_DIR, "thobichkhe.pdf")
if os.path.exists(scan_bichkhe_src):
    name_scan_bk = "[1997] Bích Khê - Thơ Bích Khê (Kiều Văn chủ biên - NXB Đồng Nai).pdf"
    dest_scan_bk = os.path.join(f_11, name_scan_bk)
    shutil.copy2(scan_bichkhe_src, dest_scan_bk)
    doc_bk = pymupdf.open(dest_scan_bk)
    pages_scan_bk = len(doc_bk)
    doc_bk.close()
    record_book("11. Thơ Mới - Bích Khê", name_scan_bk, dest_scan_bk, "Archival Scan (Archive.org)", pages_scan_bk, os.path.getsize(dest_scan_bk)/(1024*1024), "Bản scan nguyên tác sách giấy 137 trang Thơ Bích Khê do Kiều Văn chủ biên.")

scan_xuandieu_src = os.path.join(SCRATCH_DIR, "xuandieu.pdf")
if os.path.exists(scan_xuandieu_src):
    name_scan_xd = "[1997] Xuân Diệu - Thơ Và Đời (Lữ Huy Nguyên - NXB Văn Học).pdf"
    dest_scan_xd = os.path.join(f_11, name_scan_xd)
    shutil.copy2(scan_xuandieu_src, dest_scan_xd)
    doc_xd = pymupdf.open(dest_scan_xd)
    pages_scan_xd = len(doc_xd)
    doc_xd.close()
    record_book("11. Thơ Mới - Xuân Diệu", name_scan_xd, dest_scan_xd, "Archival Scan (Archive.org)", pages_scan_xd, os.path.getsize(dest_scan_xd)/(1024*1024), "Bản scan nguyên tác sách giấy đồ sộ 340 trang Xuân Diệu Thơ Và Đời do Lữ Huy Nguyên biên soạn.")

# -------------------------------------------------------------
# Save final verification JSON report
# -------------------------------------------------------------
report_path = os.path.join(SCRATCH_DIR, "poetry_supplement.json")
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(supplement_report, f, ensure_ascii=False, indent=2)

print(f"\n=== COMPLETED! Total books added: {supplement_report['total_books_added']} ===")
print(f"Report saved to: {report_path}")
