# -*- coding: utf-8 -*-
"""
Chinh Phụ Ngâm Khúc - Bản Toàn Văn Diễn Nôm Song Thất Lục Bát 412 Câu
Đoàn Thị Điểm diễn Nôm - Đặng Trần Côn nguyên tác chữ Hán
"""

import sys
import os
import asyncio

sys.path.append(r'C:\Users\Admin\.gemini\antigravity\scratch\poetry_anthology')
from pdf_engine import render_html_to_pdf

OUTPUT_DIR = r"C:\Users\Admin\Desktop\Sách\Thơ ca & Cổ văn\07. [1705-1773] Việt Nam_Đoàn Thị Điểm & Đặng Trần Côn (Chinh Phụ Ngâm)"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "[1741] Chinh Phụ Ngâm Khúc (Bản Toàn Văn Diễn Nôm Song Thất Lục Bát 412 Câu).pdf")
OLD_FILE = os.path.join(OUTPUT_DIR, "[1741] Chinh Phụ Ngâm Khúc (Bản Diễn Nôm Song Thất Lục Bát).pdf")

# We will compile the complete 412 lines (103 stanzas of 7-7-6-8) with Han text, Sino-Vietnamese, annotations and scholarly commentary.
# Let's define the content builder.
