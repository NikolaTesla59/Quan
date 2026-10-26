# -*- coding: utf-8 -*-
import json
import pymupdf

with open(r'C:\Users\Admin\.gemini\antigravity\scratch\neu_agent_1_report.json', 'r', encoding='utf-8') as f:
    rep = json.load(f)

print(f"Total completed: {rep['total_books_completed']} / {rep['total_books_assigned']}")
print(f"Total pages: {rep['total_pages_generated']}")

all_ok = True
for b in rep['textbooks']:
    doc = pymupdf.open(b['pdf_path'])
    full_text = ''
    for p in doc:
        full_text += p.get_text() + '\n'
    doc.close()
    
    # Normalize non-breaking spaces for text matching
    full_text_norm = full_text.replace('\xa0', ' ')
    
    phd_count = full_text_norm.count('DOCTORAL RESEARCH SEMINAR')
    formula_count = full_text_norm.count('MÔ HÌNH TOÁN KINH TẾ & CÔNG THỨC ĐỊNH LƯỢNG CHUẨN')
    
    print(f"{b['order']}. {b['title']}: {b['pages']} trang, {b['size_mb']} MB -- PhD seminars: {phd_count}, Formula boxes: {formula_count} -- Status: {b['verification_status']}")
    if phd_count == 0 or formula_count == 0 or b['verification_status'] != 'VERIFIED_PERFECT':
        all_ok = False

print("Overall Pipeline Verification Result:", "100% PERFECT" if all_ok else "FAILED")
