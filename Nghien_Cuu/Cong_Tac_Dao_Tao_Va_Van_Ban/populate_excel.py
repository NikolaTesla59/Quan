import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
import shutil
import os

# 1. Load data from docx
import docx
doc_path = r"C:\Users\Admin\.gemini\antigravity\scratch\student_transfer\student_list.docx"
doc = docx.Document(doc_path)
table = doc.tables[0]

students = []
for i in range(1, len(table.rows)):
    row = table.rows[i]
    stt = int(row.cells[0].text.strip())
    name = row.cells[1].text.strip()
    dob = row.cells[2].text.strip()
    students.append((stt, name, dob))

print(f"Loaded {len(students)} students.")

# 2. Paths
src_excel = r"C:\Users\Admin\.gemini\antigravity\brain\67523c2b-9f56-4a83-b1bc-4eb7a3f380fc\.user_uploaded\media_1793517294330_5035755c.xlsx"
backup_excel = r"C:\Users\Admin\.gemini\antigravity\scratch\student_transfer\original_backup.xlsx"
shutil.copy2(src_excel, backup_excel)

wb = openpyxl.load_workbook(src_excel)

# Fonts & Alignments
font_data = Font(name="Times New Roman", size=11, bold=False)
font_bold = Font(name="Times New Roman", size=11, bold=True)
font_title = Font(name="Times New Roman", size=12, bold=True)

align_center = Alignment(horizontal="center", vertical="center", wrap_text=False)
align_left = Alignment(horizontal="left", vertical="center", wrap_text=False)

thin_border_side = Side(border_style="thin", color="000000")
thin_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

# Process Sheet: MÔN HỌC
ws_monhoc = wb["MÔN HỌC"]

# Update title row 4
ws_monhoc.cell(4, 1).value = "BẢNG TỔNG HỢP CAM KẾT ĐẢM BẢO CHẤT LƯỢNG, NĂM HỌC 2026 - 2027\nKHỐI 4      - LỚP     4A\n(Cam kết chất lượng từng lớp với từng em trên từng môn)"

# Fill students in rows 8 to 46 (STT 1 to 39)
start_row = 8
for idx, (stt, name, dob) in enumerate(students):
    r = start_row + idx
    # STT
    c_stt = ws_monhoc.cell(r, 1)
    c_stt.value = stt
    c_stt.font = font_data
    c_stt.alignment = align_center
    c_stt.border = thin_border
    
    # Họ tên
    c_name = ws_monhoc.cell(r, 2)
    c_name.value = name
    c_name.font = font_data
    c_name.alignment = align_left
    c_name.border = thin_border
    c_name.number_format = "@"
    
    # Ngày sinh (FIXED dd/mm/yyyy as text)
    c_dob = ws_monhoc.cell(r, 3)
    c_dob.value = str(dob)
    c_dob.data_type = 's'  # Explicit string type
    c_dob.font = font_data
    c_dob.alignment = align_center
    c_dob.border = thin_border
    c_dob.number_format = "@"

# For rows 47 to 53 (the unused rows 40 to 46)
for r in range(start_row + len(students), 54):
    c_stt = ws_monhoc.cell(r, 1)
    c_stt.value = None  # Clear unused STT number so it doesn't display empty student numbers
    c_stt.border = thin_border
    
    c_name = ws_monhoc.cell(r, 2)
    c_name.value = None
    c_name.border = thin_border
    
    c_dob = ws_monhoc.cell(r, 3)
    c_dob.value = None
    c_dob.border = thin_border

# Process Sheet: HĐGD
ws_hdgd = wb["HĐGD"]

# Update title row 4
ws_hdgd.cell(4, 1).value = "BẢNG TỔNG HỢP CAM KẾT ĐẢM BẢO CHẤT LƯỢNG, NĂM HỌC 2026 - 2027\nKHỐI 4      - LỚP     4A\n(Cam kết chất lượng từng lớp với từng em trên từng môn)"

# Fill students in rows 8 to 46 (STT 1 to 39)
for idx, (stt, name, dob) in enumerate(students):
    r = start_row + idx
    # STT
    c_stt = ws_hdgd.cell(r, 1)
    c_stt.value = stt
    c_stt.font = font_data
    c_stt.alignment = align_center
    c_stt.border = thin_border
    
    # Họ tên
    c_name = ws_hdgd.cell(r, 2)
    c_name.value = name
    c_name.font = font_data
    c_name.alignment = align_left
    c_name.border = thin_border
    c_name.number_format = "@"
    
    # Ngày sinh (FIXED dd/mm/yyyy as text)
    c_dob = ws_hdgd.cell(r, 3)
    c_dob.value = str(dob)
    c_dob.data_type = 's'  # Explicit string type
    c_dob.font = font_data
    c_dob.alignment = align_center
    c_dob.border = thin_border
    c_dob.number_format = "@"

# For rows 47 to 53 in HĐGD, ensure borders and empty cells to match MÔN HỌC
for r in range(start_row + len(students), 54):
    for c in range(1, 22):
        cell = ws_hdgd.cell(r, c)
        cell.border = thin_border
        cell.font = font_data

# In HĐGD, let's also add the "Tổng " row and signatures to match MÔN HỌC!
# Row 54: Tổng
ws_hdgd.cell(54, 2).value = "Tổng "
ws_hdgd.cell(54, 2).font = font_bold
ws_hdgd.cell(54, 2).alignment = align_left
for c in range(1, 22):
    ws_hdgd.cell(54, c).border = thin_border

# Row 55: Signatures
ws_hdgd.merge_cells("B55:C55")
c_gv = ws_hdgd.cell(55, 2)
c_gv.value = "Giáo viên chủ nhiệm"
c_gv.font = font_bold
c_gv.alignment = align_center

ws_hdgd.merge_cells("H55:N55")
c_cmhs = ws_hdgd.cell(55, 8)
c_cmhs.value = "Trưởng ban đại diện CMHS lớp"
c_cmhs.font = font_bold
c_cmhs.alignment = align_center

ws_hdgd.merge_cells("Q55:U55")
c_ht = ws_hdgd.cell(55, 17)
c_ht.value = "Hiệu trưởng"
c_ht.font = font_bold
c_ht.alignment = align_center

# Save output to multiple locations for maximum convenience
out_paths = [
    r"C:\Users\Admin\.gemini\antigravity\scratch\student_transfer\BANG_TONG_HOP_CAM_KET_CHAT_LUONG_LOP_4A.xlsx",
    r"C:\Users\Admin\Desktop\BANG_TONG_HOP_CAM_KET_CHAT_LUONG_LOP_4A.xlsx",
    r"C:\Users\Admin\Downloads\BANG_TONG_HOP_CAM_KET_CHAT_LUONG_LOP_4A.xlsx",
    src_excel  # Update original uploaded file
]

for p in out_paths:
    wb.save(p)
    print(f"Saved: {p} (size={os.path.getsize(p)} bytes)")

print("\n--- Verification of Written Data ---")
check_wb = openpyxl.load_workbook(out_paths[0])
for sname in check_wb.sheetnames:
    ws = check_wb[sname]
    print(f"\nSheet {sname}:")
    for r in [8, 9, 10, 45, 46, 47, 54, 55]:
        stt_val = ws.cell(r, 1).value
        name_val = ws.cell(r, 2).value
        dob_val = ws.cell(r, 3).value
        dob_type = ws.cell(r, 3).data_type
        dob_fmt = ws.cell(r, 3).number_format
        print(f"Row {r:2d} | STT: {stt_val} | Name: {name_val} | DOB: {dob_val} (type={dob_type}, fmt={dob_fmt})")
