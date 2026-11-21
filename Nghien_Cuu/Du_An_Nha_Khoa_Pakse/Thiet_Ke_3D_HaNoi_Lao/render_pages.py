import fitz
import os

pdf_path = r"C:\Users\Admin\Desktop\hstk 3D nk HA NOI LAO 18-11.pdf"
out_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\hstk_3d_images"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Rendering {len(doc)} pages to {out_dir}...")

# zoom matrix: 1.5x (around 1296 x 810 px, crisp and lightweight)
mat = fitz.Matrix(1.5, 1.5)

for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=mat)
    img_path = os.path.join(out_dir, f"page_{i+1:02d}.jpg")
    pix.save(img_path)
    if (i + 1) % 10 == 0 or i == len(doc) - 1:
        print(f"Rendered {i+1}/{len(doc)} pages")

print("Done rendering all pages!")
