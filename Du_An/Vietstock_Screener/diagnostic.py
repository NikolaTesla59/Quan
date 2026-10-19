import sqlite3
import os

print("=== 1. KIỂM TRA CƠ SỞ DỮ LIỆU STOCKS.DB ===")
db_path = r'C:\Users\Admin\.gemini\antigravity\scratch\vietstock-screener\stocks.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print("Tables:", [t[0] for t in tables])
    for t in tables:
        cur.execute(f"SELECT count(*) FROM {t[0]};")
        print(f"  - {t[0]}: {cur.fetchone()[0]:,} dòng")
else:
    print("stocks.db không tồn tại!")

print("\n=== 2. KIỂM TRA THƯ VIỆN ĐỒ THỊ & ĐỊNH LƯỢNG ===")
libs = ['matplotlib', 'seaborn', 'vectorbt', 'mplfinance', 'scikit-learn']
for lib in libs:
    try:
        mod = __import__(lib)
        ver = getattr(mod, '__version__', 'installed')
        print(f"  [OK]      {lib:<15} ({ver})")
    except ImportError:
        print(f"  [MISSING] {lib:<15}")

print("\n=== 3. KIỂM TRA CÔNG CỤ XUẤT BÁO CÁO (PDF/LATEX/OFFICE) ===")
tools = ['pandoc', 'xelatex', 'msedge']
import shutil
for t in tools:
    path = shutil.which(t)
    print(f"  {'[OK]' if path else '[MISSING]'} {t:<15} -> {path}")
