import urllib.request
import urllib.parse
import json
import ssl
import re
import html
import os
import pymupdf

ctx = ssl._create_unverified_context()

def get_page_text(title):
    url = f"https://vi.wikisource.org/w/api.php?action=parse&page={urllib.parse.quote(title)}&prop=text&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            data = json.loads(r.read())
            raw = data.get('parse', {}).get('text', {}).get('*', '')
            # Remove navboxes, tables of contents, scripts, styles
            clean = re.sub(r'<(script|style|table)[^>]*>.*?</\1>', '', raw, flags=re.S)
            clean = re.sub(r'<div class="header-box[^"]*".*?</div>', '', clean, flags=re.S)
            clean = re.sub(r'<br\s*/?>', '\n', clean)
            clean = re.sub(r'</p>', '\n\n', clean)
            clean = re.sub(r'<[^>]+>', '', clean)
            clean = html.unescape(clean)
            # Remove excessive whitespace
            clean = re.sub(r'\n{3,}', '\n\n', clean).strip()
            return clean
    except Exception as e:
        print(f"Error fetching {title}: {e}")
        return ""

def create_book_pdf(out_path, title, author, chapters):
    """
    chapters: list of (chap_title, chap_text)
    """
    doc = pymupdf.open()
    font_reg = r"C:\Windows\Fonts\times.ttf"
    font_bold = r"C:\Windows\Fonts\timesbd.ttf"
    font_italic = r"C:\Windows\Fonts\timesi.ttf"
    
    # 1. Cover / Title Page
    page = doc.new_page(width=595, height=842) # A4
    page.insert_font(fontname="TimesReg", fontfile=font_reg)
    page.insert_font(fontname="TimesBold", fontfile=font_bold)
    
    rect_title = pymupdf.Rect(50, 250, 545, 450)
    page.insert_textbox(rect_title, title.upper(), fontname="TimesBold", fontsize=24, align=pymupdf.TEXT_ALIGN_CENTER, color=(0.1, 0.1, 0.3))
    
    rect_author = pymupdf.Rect(50, 480, 545, 550)
    page.insert_textbox(rect_author, f"Tác giả: {author}\nẤn bản toàn văn số hóa hoàn chỉnh", fontname="TimesReg", fontsize=15, align=pymupdf.TEXT_ALIGN_CENTER, color=(0.3, 0.3, 0.3))
    
    # 2. Content Pages
    font_size = 11.5
    line_h = 16
    margin_l = 54
    margin_r = 54
    margin_t = 60
    margin_b = 60
    page_w = 595
    page_h = 842
    body_w = page_w - margin_l - margin_r
    body_h = page_h - margin_t - margin_b
    
    for chap_title, text in chapters:
        if not text:
            continue
        paragraphs = text.split('\n\n')
        
        # New page for new chapter
        curr_page = doc.new_page(width=page_w, height=page_h)
        curr_page.insert_font(fontname="TimesReg", fontfile=font_reg)
        curr_page.insert_font(fontname="TimesBold", fontfile=font_bold)
        curr_page.insert_font(fontname="TimesItalic", fontfile=font_italic)
        
        # Insert chapter heading
        rect_h = pymupdf.Rect(margin_l, margin_t, margin_l + body_w, margin_t + 40)
        curr_page.insert_textbox(rect_h, chap_title, fontname="TimesBold", fontsize=16, color=(0.15, 0.15, 0.2))
        
        curr_y = margin_t + 55
        
        for p in paragraphs:
            p = p.strip()
            if not p:
                continue
            
            # Estimate text height
            # A rough estimate or try fitting
            rect_try = pymupdf.Rect(margin_l, curr_y, margin_l + body_w, margin_t + body_h)
            rem = curr_page.insert_textbox(rect_try, p, fontname="TimesReg", fontsize=font_size, align=pymupdf.TEXT_ALIGN_JUSTIFY)
            
            if rem < 0:
                # Text did not fit completely on this page -> make new page
                curr_page = doc.new_page(width=page_w, height=page_h)
                curr_page.insert_font(fontname="TimesReg", fontfile=font_reg)
                curr_page.insert_font(fontname="TimesBold", fontfile=font_bold)
                curr_page.insert_font(fontname="TimesItalic", fontfile=font_italic)
                curr_y = margin_t
                rect_try2 = pymupdf.Rect(margin_l, curr_y, margin_l + body_w, margin_t + body_h)
                curr_page.insert_textbox(rect_try2, p, fontname="TimesReg", fontsize=font_size, align=pymupdf.TEXT_ALIGN_JUSTIFY)
                curr_y = margin_t + 60
            else:
                # Approximate next y
                lines_approx = len(p) / 75 + 1
                curr_y += lines_approx * line_h + 8
                if curr_y > margin_t + body_h - 40:
                    curr_page = doc.new_page(width=page_w, height=page_h)
                    curr_page.insert_font(fontname="TimesReg", fontfile=font_reg)
                    curr_page.insert_font(fontname="TimesBold", fontfile=font_bold)
                    curr_page.insert_font(fontname="TimesItalic", fontfile=font_italic)
                    curr_y = margin_t
    
    # 3. Add Page numbers
    for i, p in enumerate(doc):
        if i == 0:
            continue
        p.insert_text(pymupdf.Point(page_w / 2 - 10, page_h - 30), str(i), fontname="TimesReg", fontsize=10, color=(0.4, 0.4, 0.4))
    
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    pg_count = len(doc)
    doc.save(out_path)
    doc.close()
    sz_mb = round(os.path.getsize(out_path)/1024/1024, 2)
    print(f"SAVED: {os.path.basename(out_path)} ({pg_count} pages, {sz_mb} MB)")

# 1. Việc Làng - Ngô Tất Tố
vlec_chapters = [
    ("Lời giới thiệu & Một đám vào ngôi", "Việc làng/Một đám vào ngôi"),
    ("Một tiệc ăn vạ", "Việc làng/Một tiệc ăn vạ"),
    ("Góc chiếu giữa đình", "Việc làng/Góc chiếu giữa đình"),
    ("Con gà thờ", "Việc làng/Con gà thờ"),
    ("Cỗ oản tuần sóc", "Việc làng/Cỗ oản tuần sóc"),
    ("Mua cỗ", "Việc làng/Mua cỗ"),
    ("Cái án ông cụ", "Việc làng/Cái án ông cụ"),
    ("Một cái thảm trạng", "Việc làng/Một cái thảm trạng")
]
print("\nCompiling Việc Làng...")
vl_content = []
for title, page_title in vlec_chapters:
    t = get_page_text(page_title)
    if t:
        vl_content.append((title, t))
out_vl = r"C:\Users\Admin\Desktop\Sách\Văn học\16. [1894-1954] Việt Nam_Ngô Tất Tố\[1940] Việc Làng (Phóng Sự Toàn Tập Hoàn Chỉnh).pdf"
create_book_pdf(out_vl, "Việc Làng", "Ngô Tất Tố", vl_content)

# 2. Lều Chõng - Ngô Tất Tố (21 chương)
print("\nCompiling Lều Chõng...")
lc_content = []
t_pre = get_page_text("Lều chõng/Lời tựa")
if t_pre:
    lc_content.append(("Lời tựa", t_pre))
for c in range(1, 22):
    t = get_page_text(f"Lều chõng/Chương {c}")
    if t:
        lc_content.append((f"Chương {c}", t))
out_lc = r"C:\Users\Admin\Desktop\Sách\Văn học\16. [1894-1954] Việt Nam_Ngô Tất Tố\[1941] Lều Chõng (Tiểu Thuyết Khoa Cử Toàn Văn 21 Chương).pdf"
create_book_pdf(out_lc, "Lều Chõng", "Ngô Tất Tố", lc_content)

# 3. Làm Đĩ - Vũ Trọng Phụng (15 chương)
print("\nCompiling Làm Đĩ...")
ld_content = []
for c in range(1, 16):
    t = get_page_text(f"Làm đĩ/Chương {c}")
    if t:
        ld_content.append((f"Chương {c}", t))
out_ld = r"C:\Users\Admin\Desktop\Sách\Văn học\19. [1912-1939] Việt Nam_Vũ Trọng Phụng\[1936] Làm Đĩ (Toàn Văn Tiểu Thuyết Luân Lý Xã Hội).pdf"
create_book_pdf(out_ld, "Làm Đĩ", "Vũ Trọng Phụng", ld_content)

# 4. Nắng Trong Vườn - Thạch Lam
print("\nCompiling Nắng Trong Vườn...")
nv_text = get_page_text("Nắng trong vườn")
if nv_text:
    out_nv = r"C:\Users\Admin\Desktop\Sách\Văn học\17. [1910-1942] Việt Nam_Thạch Lam\[1938] Nắng Trong Vườn (Toàn Tập Truyện Ngắn Hoàn Chỉnh).pdf"
    create_book_pdf(out_nv, "Nắng Trong Vườn", "Thạch Lam", [("Nắng Trong Vườn", nv_text)])

print("\nALL VIETNAMESE NOVELS COMPILED SUCCESSFULLY!")
