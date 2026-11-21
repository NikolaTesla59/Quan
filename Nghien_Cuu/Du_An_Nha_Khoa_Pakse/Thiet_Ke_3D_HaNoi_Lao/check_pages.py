import fitz
import os

pdf_path = r"C:\Users\Admin\Desktop\hstk 3D nk HA NOI LAO 18-11.pdf"
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    txt = page.get_text().strip()
    first_line = txt.split('\n')[0] if txt else "(No text - pure image)"
    print(f"Page {i+1:02d}: {first_line[:80]} (length: {len(txt)})")
