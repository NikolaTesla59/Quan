import openpyxl
import re
from datetime import datetime

audit_path = r"C:\Users\Admin\Desktop\BANG_TONG_HOP_CAM_KET_CHAT_LUONG_LOP_4A.xlsx"
wb = openpyxl.load_workbook(audit_path)

# Ensure no cell in Col C has mm-dd-yy
for sname in wb.sheetnames:
    ws = wb[sname]
    for r in range(8, ws.max_row + 1):
        if ws.cell(r, 3).number_format == 'mm-dd-yy':
            ws.cell(r, 3).number_format = '@'

wb.save(audit_path)
wb.save(r"C:\Users\Admin\Downloads\BANG_TONG_HOP_CAM_KET_CHAT_LUONG_LOP_4A.xlsx")
wb.save(r"C:\Users\Admin\.gemini\antigravity\brain\67523c2b-9f56-4a83-b1bc-4eb7a3f380fc\.user_uploaded\media_1793517294330_5035755c.xlsx")
wb.save(r"C:\Users\Admin\.gemini\antigravity\scratch\student_transfer\BANG_TONG_HOP_CAM_KET_CHAT_LUONG_LOP_4A.xlsx")

# Run full audit
errors = []
date_regex = re.compile(r"^\d{2}/\d{2}/\d{4}$")

for sname in ["MÔN HỌC", "HĐGD"]:
    ws = wb[sname]
    print(f"\n================ AUDITING SHEET: {sname} ================")
    
    # Check title
    title = ws.cell(4, 1).value
    print(f"Title: {repr(title[:60])}...")
    
    for i in range(1, 40):
        r = 7 + i
        stt = ws.cell(r, 1).value
        name = ws.cell(r, 2).value
        dob = ws.cell(r, 3).value
        dob_type = ws.cell(r, 3).data_type
        dob_fmt = ws.cell(r, 3).number_format
        
        if stt != i:
            errors.append(f"[{sname}] Row {r}: STT expected {i}, got {stt}")
        if not name or not isinstance(name, str) or len(name.strip()) < 3:
            errors.append(f"[{sname}] Row {r}: Invalid name {name}")
        if not dob or not isinstance(dob, str):
            errors.append(f"[{sname}] Row {r}: DOB not string {dob}")
        elif not date_regex.match(dob):
            errors.append(f"[{sname}] Row {r}: DOB not dd/mm/yyyy format: {dob}")
        else:
            try:
                datetime.strptime(dob, "%d/%m/%Y")
            except ValueError as ve:
                errors.append(f"[{sname}] Row {r}: Invalid calendar date {dob}: {ve}")
        
        if dob_type != 's':
            errors.append(f"[{sname}] Row {r}: DOB data_type not 's', got {dob_type}")
        if dob_fmt != '@':
            errors.append(f"[{sname}] Row {r}: DOB number_format not '@', got {dob_fmt}")

print(f"\n--- AUDIT RESULTS: {len(errors)} ERRORS FOUND ---")
if errors:
    for e in errors:
        print("ERROR:", e)
else:
    print("ALL 39 STUDENTS AUDITED SUCCESSFULLY ACROSS BOTH SHEETS! 100% PERFECT!")
