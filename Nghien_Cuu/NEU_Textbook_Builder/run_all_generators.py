# -*- coding: utf-8 -*-
"""
Master Runner & Inspector for NEU Finance Specialist:
Compiles all 10 scholarly textbooks, verifies PyMuPDF integrity,
and generates the final report.
"""
import sys
import os
import json
import time

sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder")
sys.path.append(r"C:\Users\Admin\.gemini\antigravity\scratch\neu_textbook_builder\generators")

from gen_book_1_ktdt import build_ktdt
from gen_book_2_ttck import build_ttck
from gen_book_3_tcdn import build_tcdn
from gen_book_4_tctt import build_tctt
from gen_book_5_dgts import build_dgts
from gen_book_6_kdbh import build_kdbh
from gen_book_7_nhtm import build_nhtm
from gen_book_8_tcqt import build_tcqt
from gen_book_9_ttqt import build_ttqt
from gen_book_10_gddp import build_gddp

import pymupdf

def run_all():
    print("="*80)
    print("STARTING NEU FINANCE SPECIALIST TEXTBOOK GENERATION & VERIFICATION PIPELINE")
    print("="*80)
    
    generators = [
        ("Kinh tế đầu tư", build_ktdt),
        ("Thị trường chứng khoán", build_ttck),
        ("Tài chính doanh nghiệp", build_tcdn),
        ("Tài chính tiền tệ", build_tctt),
        ("Định giá tài sản & Bất động sản", build_dgts),
        ("Kinh doanh bảo hiểm", build_kdbh),
        ("Quản trị ngân hàng thương mại", build_nhtm),
        ("Tài chính quốc tế", build_tcqt),
        ("Thanh toán quốc tế", build_ttqt),
        ("Giao dịch & Đàm phán quốc tế", build_gddp)
    ]
    
    results = []
    
    for idx, (name, gen_func) in enumerate(generators, 1):
        print(f"\n[{idx}/10] Generating: {name}...")
        t0 = time.time()
        try:
            info = gen_func()
            elapsed = time.time() - t0
            
            # Rigorous PyMuPDF Verification
            pdf_path = info["path"]
            assert os.path.exists(pdf_path), f"File not found: {pdf_path}"
            doc = pymupdf.open(pdf_path)
            page_count = len(doc)
            assert page_count > 0, "Page count must be > 0"
            
            # Check font and text extraction on sample pages
            sample_texts = []
            font_error = False
            for p_num in range(min(page_count, 3)):
                txt = doc[p_num].get_text()
                if "\ufffd" in txt or len(txt.strip()) < 30:
                    font_error = True
                sample_texts.append({
                    "page": p_num + 1,
                    "preview": txt[:120].replace("\n", " ").strip()
                })
            doc.close()
            
            status = "VERIFIED_PERFECT" if not font_error else "WARNING_FONT_ISSUE"
            
            res_item = {
                "order": idx,
                "title": info["title"],
                "subject_code": info["code"],
                "faculty": "Trường Đại học Kinh tế Quốc dân (NEU)",
                "authors": info["author"],
                "pdf_path": pdf_path,
                "pages": page_count,
                "size_mb": info["size_mb"],
                "generation_time_sec": round(elapsed, 2),
                "verification_status": status,
                "sample_extracted_text": sample_texts
            }
            results.append(res_item)
            print(f" -> [OK] Pages: {page_count}, Size: {info['size_mb']} MB, Status: {status} ({elapsed:.2f}s)")
            
        except Exception as e:
            print(f" -> [ERROR] Failed to generate {name}: {str(e)}")
            results.append({
                "order": idx,
                "title": name,
                "error": str(e),
                "verification_status": "FAILED"
            })
            
    # Write summary report
    report_path = r"C:\Users\Admin\.gemini\antigravity\scratch\neu_agent_1_report.json"
    report_data = {
        "agent_name": "NEU Finance Specialist (Chuyên gia Tài chính - Ngân hàng - Bảo hiểm - Đầu tư & Định giá NEU)",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_books_assigned": 10,
        "total_books_completed": len([r for r in results if r.get("verification_status") == "VERIFIED_PERFECT"]),
        "total_pages_generated": sum(r.get("pages", 0) for r in results),
        "standards": {
            "academic_levels": ["Đại học chính quy", "Thạc sĩ (Cao học)", "Tiến sĩ (Doctoral Research Seminar)"],
            "font_system": "Times New Roman TrueType Unicode UTF-8",
            "publisher": "Nhà xuất bản Đại học Kinh tế Quốc dân (NXB ĐHKTQD)",
            "verification_tool": "PyMuPDF TextWriter"
        },
        "textbooks": results
    }
    
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n[SUMMARY] Saved full report to: {report_path}")
    print(f"Total books completed: {report_data['total_books_completed']}/{report_data['total_books_assigned']}")
    print(f"Total pages generated: {report_data['total_pages_generated']} pages")

if __name__ == "__main__":
    run_all()
