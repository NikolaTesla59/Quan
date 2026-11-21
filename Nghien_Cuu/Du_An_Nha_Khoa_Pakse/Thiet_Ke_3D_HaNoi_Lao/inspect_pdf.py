import sys
print("Python:", sys.executable)

pdf_path = r"C:\Users\Admin\Desktop\hstk 3D nk HA NOI LAO 18-11.pdf"

try:
    import fitz # PyMuPDF
    print("fitz is installed")
    doc = fitz.open(pdf_path)
    print("Total pages:", len(doc))
    for i in range(min(5, len(doc))):
        page = doc[i]
        print(f"Page {i+1} rect:", page.rect)
        text = page.get_text()
        if text.strip():
            print(f"Page {i+1} text snippet:", text.strip()[:200])
except Exception as e:
    print("fitz error or not installed:", e)

try:
    import pypdf
    print("pypdf is installed")
    reader = pypdf.PdfReader(pdf_path)
    print("pypdf pages:", len(reader.pages))
except Exception as e:
    print("pypdf error or not installed:", e)
