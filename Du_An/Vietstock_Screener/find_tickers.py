import openpyxl

wb = openpyxl.load_workbook('Bo_Loc_Co_Phieu_Vietstock_Khung_Tieu_Chi_PRO.xlsx', data_only=True)
print("Sheets:", wb.sheetnames)

for sname in wb.sheetnames:
    s = wb[sname]
    print(f"\n--- Sheet: {sname} (rows: {s.max_row}, cols: {s.max_column}) ---")
    headers = [s.cell(5, c).value for c in range(1, min(s.max_column+1, 30))]
    print("Row 5 headers:", headers[:10])
    
    # search for HSG and VCG in any cell of column 1 to 5
    for r in range(1, min(s.max_row+1, 700)):
        v1 = str(s.cell(r, 2).value).strip() if s.cell(r, 2).value else ""
        v2 = str(s.cell(r, 1).value).strip() if s.cell(r, 1).value else ""
        v3 = str(s.cell(r, 3).value).strip() if s.cell(r, 3).value else ""
        if 'HSG' in [v1, v2, v3] or 'VCG' in [v1, v2, v3]:
            row_vals = [s.cell(r, c).value for c in range(1, min(s.max_column+1, 25))]
            print(f"Found at row {r} in {sname}: {row_vals}")
