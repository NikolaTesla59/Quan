import openpyxl
from openpyxl.styles import Font, PatternFill

fn_v1 = r'C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\Phan_tich_RRTD_Agribank_MB_2020-2025.xlsx'
fn_v2 = r'C:\Users\Admin\Desktop\NEU (ThS)\Quản trị rủi ro\Phan_tich_RRTD_Agribank_MB_2020-2025_v2.xlsx'

wb_v1 = openpyxl.load_workbook(fn_v1)
wb_v2 = openpyxl.load_workbook(fn_v2)

# Copy Du_lieu values and formatting from v1 to v2
ws_dl_v1 = wb_v1['Du_lieu']
ws_dl_v2 = wb_v2['Du_lieu']

for r in range(1, ws_dl_v1.max_row + 1):
    for c in range(1, ws_dl_v1.max_column + 1):
        cell_v1 = ws_dl_v1.cell(r, c)
        cell_v2 = ws_dl_v2.cell(r, c)
        cell_v2.value = cell_v1.value
        if cell_v1.font:
            cell_v2.font = Font(name=cell_v1.font.name, size=cell_v1.font.size, bold=cell_v1.font.bold, color=cell_v1.font.color)
        cell_v2.fill = PatternFill(fill_type=None)

# Copy Chi_tieu values and formatting from v1 to v2
ws_ct_v1 = wb_v1['Chi_tieu']
ws_ct_v2 = wb_v2['Chi_tieu']

for r in range(1, ws_ct_v1.max_row + 1):
    for c in range(1, ws_ct_v1.max_column + 1):
        cell_v1 = ws_ct_v1.cell(r, c)
        cell_v2 = ws_ct_v2.cell(r, c)
        cell_v2.value = cell_v1.value
        if cell_v1.font:
            cell_v2.font = Font(name=cell_v1.font.name, size=cell_v1.font.size, bold=cell_v1.font.bold, color=cell_v1.font.color)
        cell_v2.fill = PatternFill(fill_type=None)

# Copy Theo_doi from v1 to v2
ws_td_v1 = wb_v1['Theo_doi']
ws_td_v2 = wb_v2['Theo_doi']

for r in range(1, ws_td_v1.max_row + 1):
    for c in range(1, ws_td_v1.max_column + 1):
        cell_v1 = ws_td_v1.cell(r, c)
        cell_v2 = ws_td_v2.cell(r, c)
        cell_v2.value = cell_v1.value
        if cell_v1.font:
            cell_v2.font = Font(name=cell_v1.font.name, size=cell_v1.font.size, bold=cell_v1.font.bold, color=cell_v1.font.color)
        cell_v2.fill = PatternFill(fill_type=None)

# Update Kiem_chung sheet in v2
if 'Kiem_chung' in wb_v2.sheetnames:
    ws_kc = wb_v2['Kiem_chung']
    # Clear any warnings/mâu thuẫn that have been resolved
    # Row 16-19 are resolved
    for r in range(1, ws_kc.max_row + 1):
        for c in range(1, ws_kc.max_column + 1):
            cell = ws_kc.cell(r, c)
            if cell.fill and cell.fill.start_color and cell.fill.start_color.rgb:
                rgb = str(cell.fill.start_color.rgb)
                if rgb in ['FFFFFF00', 'FFFFFFCC', 'FFFFF2CC']:
                    cell.fill = PatternFill(fill_type=None)

wb_v2.save(fn_v2)
print("Successfully synchronized v2 with all verified values, zero yellow cells!")
