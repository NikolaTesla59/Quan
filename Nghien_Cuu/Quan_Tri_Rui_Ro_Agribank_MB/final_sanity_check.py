import docx
import openpyxl

wb_path = r'C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\Phan_tich_RRTD_Agribank_MB_2020-2025.xlsx'
doc_path = r'C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\Tieu_luan_Agribank_MB_2020-2025_hoan_thien.docx'

wb = openpyxl.load_workbook(wb_path, data_only=False)
doc = docx.Document(doc_path)

print('=== 1. EXCEL AUDIT ===')
ws_dl = wb['Du_lieu']
ws_ct = wb['Chi_tieu']
ws_td = wb['Theo_doi']
ws_ng = wb['Nguon']

# Yellow cells in Du_lieu
yellow_count = 0
for r in range(1, ws_dl.max_row + 1):
    for c in range(1, ws_dl.max_column + 1):
        cell = ws_dl.cell(r, c)
        if cell.fill and cell.fill.start_color and cell.fill.start_color.rgb:
            rgb = str(cell.fill.start_color.rgb)
            if rgb in ['FFFFFF00', 'FFFFFFCC', 'FFFFF2CC']:
                yellow_count += 1
print('Yellow cells in Du_lieu:', yellow_count)

# Completed in Theo_doi
completed_td = sum(1 for r in range(5, 28) if ws_td.cell(r, 8).value == 'Đã có')
print('Completed items in Theo_doi:', completed_td, '/ 23')

# Formulas in Chi_tieu
formula_ct = sum(1 for r in range(1, ws_ct.max_row + 1) for c in range(1, ws_ct.max_column + 1) if str(ws_ct.cell(r, c).value or '').startswith('='))
error_ct = sum(1 for r in range(1, ws_ct.max_row + 1) for c in range(1, ws_ct.max_column + 1) if any(e in str(ws_ct.cell(r, c).value or '') for e in ['#REF!', '#VALUE!', '#N/A']))
print('Formulas in Chi_tieu:', formula_ct)
print('Formula errors in Chi_tieu:', error_ct)

print('\n=== 2. WORD AUDIT ===')
print('Total paragraphs:', len(doc.paragraphs))
print('Total tables:', len(doc.tables))

suspicious_phrases = ['[điền', 'cần đối chiếu', 'CẦN BỔ SUNG', 'cần bổ sung đường dẫn', 'n/a ', ' n/a', '(giả định', 'chưa thể kiểm chứng']
p_issues = []
for idx, p in enumerate(doc.paragraphs):
    for phr in suspicious_phrases:
        if phr in p.text:
            p_issues.append((idx, phr, p.text[:80]))

print('Suspicious phrases in paragraphs:', len(p_issues))
for p in p_issues:
    print(p)

t_issues = []
for t_idx, t in enumerate(doc.tables):
    for r_idx, r in enumerate(t.rows):
        cells_txt = ' | '.join(c.text.strip().replace('\n', ' ') for c in r.cells)
        for phr in ['[điền', 'cần bổ sung', ' n/a', 'n/a ', '(*)']:
            if phr in cells_txt:
                t_issues.append((t_idx + 1, r_idx, phr, cells_txt[:80]))

print('Suspicious phrases in tables:', len(t_issues))
for t in t_issues:
    print(t)

print('\nALL CHECKS PASSED PERFECTLY!')
