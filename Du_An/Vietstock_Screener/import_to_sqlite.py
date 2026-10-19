import pandas as pd
import sqlite3
import os

xlsx = r'C:\Users\Admin\.gemini\antigravity\scratch\vietstock-screener\Bo_Loc_Co_Phieu_Vietstock_Khung_Tieu_Chi.xlsx'
db_path = r'C:\Users\Admin\.gemini\antigravity\scratch\vietstock-screener\stocks.db'

xl = pd.ExcelFile(xlsx)
print('Sheets in Excel:', xl.sheet_names)

conn = sqlite3.connect(db_path)
for sheet in xl.sheet_names:
    df = pd.read_excel(xlsx, sheet_name=sheet)
    # clean table name
    tname = sheet.strip().replace(' ', '_').replace('-', '_')
    df.to_sql(tname, conn, if_exists='replace', index=False)
    print(f'Imported sheet "{sheet}" -> table "{tname}" ({len(df)} rows)')

conn.close()
print('stocks.db populated successfully!')
