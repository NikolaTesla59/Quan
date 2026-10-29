import sqlite3
import pandas as pd

conn = sqlite3.connect('stocks.db')

for table in ['Top_Co_Phieu_Chon_Loc', 'Danh_Gia_Toan_Bo_CP', 'Ban_Do_Chu_Ky_Nganh']:
    try:
        df = pd.read_sql(f"SELECT * FROM `{table}`", conn)
        # find column with 'Mã' or 'ma'
        col = [c for c in df.columns if 'Mã' in c or 'ma' in c.lower()][0]
        sub = df[df[col].isin(['HSG', 'VCG'])]
        print(f"=== {table} ===")
        print(sub.T.to_string())
        print("\n" + "="*50 + "\n")
    except Exception as e:
        print(f"Error in {table}: {e}")
