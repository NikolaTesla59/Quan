import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import shutil
import re
import unicodedata
import os

def clean_txt(t):
    if not t: return ""
    t = unicodedata.normalize('NFC', t).lower()
    t = re.sub(r'[^\w\s]', ' ', t)
    return " ".join(t.split())

def add_bookmark(paragraph, bookmark_id, bookmark_name):
    bm_start = OxmlElement('w:bookmarkStart')
    bm_start.set(qn('w:id'), str(bookmark_id))
    bm_start.set(qn('w:name'), bookmark_name)
    
    bm_end = OxmlElement('w:bookmarkEnd')
    bm_end.set(qn('w:id'), str(bookmark_id))
    
    paragraph._p.insert(0, bm_start)
    paragraph._p.append(bm_end)

def create_hyperlink_run(target_bookmark, text, font_name="Times New Roman", font_size_pt=10.5, bold=False, italic=False, color="003366"):
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('w:anchor'), target_bookmark)
    hyperlink.set(qn('w:history'), '1')
    
    r = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    
    if font_name:
        rFonts = OxmlElement('w:rFonts')
        rFonts.set(qn('w:ascii'), font_name)
        rFonts.set(qn('w:hAnsi'), font_name)
        rFonts.set(qn('w:cs'), font_name)
        rPr.append(rFonts)
        
    if font_size_pt:
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), str(int(font_size_pt * 2)))
        rPr.append(sz)
        
    if bold:
        b = OxmlElement('w:b')
        rPr.append(b)
        
    if italic:
        i = OxmlElement('w:i')
        rPr.append(i)
        
    if color:
        c = OxmlElement('w:color')
        c.set(qn('w:val'), color)
        rPr.append(c)
        
    r.append(rPr)
    
    t = OxmlElement('w:t')
    t.text = text
    t.set(qn('xml:space'), 'preserve')
    r.append(t)
    
    hyperlink.append(r)
    return hyperlink

def add_run(paragraph, text, font_name="Times New Roman", font_size_pt=10.5, bold=False, italic=False, color="333333"):
    run = paragraph.add_run(text)
    run.font.name = font_name
    run.font.size = Pt(font_size_pt)
    run.bold = bold
    run.italic = italic
    if color:
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        run.font.color.rgb = RGBColor(r, g, b)
    return run

# Paths
src_path = r"C:\Users\Admin\Desktop\NGU\book\Hegel\13003-tu-dien-triet-hoc-hegel-thuviensach.vn.docx"
backup_path = r"C:\Users\Admin\Desktop\NGU\book\Hegel\13003-tu-dien-triet-hoc-hegel-thuviensach.vn_backup.docx"

if not os.path.exists(backup_path):
    shutil.copy2(src_path, backup_path)
    print("Backup created at:", backup_path)

doc = docx.Document(src_path)
print(f"Loaded document. Total paragraphs: {len(doc.paragraphs)}")

# 1. Parse BẢNG CHỈ MỤC NỘI DUNG VIỆT - ĐỨC - ANH (paragraphs 3770-4185)
raw_index = []
in_vn = False
for i in range(3770, 4185):
    t = doc.paragraphs[i].text.strip()
    if "BẢNG CHỈ MỤC NỘI DUNG VIỆT - ĐỨC - ANH" in t:
        in_vn = True
        continue
    if "BẢNG CHỈ MỤC NỘI DUNG ĐỨC - ANH - VIỆT" in t:
        in_vn = False
        break
    if in_vn and t:
        raw_index.append(t)

# Fix jammed lines
cleaned_lines = []
for line in raw_index:
    if "(Nguyễn Văn Sướng dịch) Tập tục" in line:
        cleaned_lines.append("(Nguyễn Văn Sướng dịch)")
        cleaned_lines.append("Tập tục / Sitte / custom → Xem: Đời sống Đạo đức và Tập tục (tr.389)")
        cleaned_lines.append("Tất yếu (tính, sự), Khả năng, Khả thể và Bất tất (tính, sự) /")
    else:
        cleaned_lines.append(line)

# Group into structured entry objects
items = []
i = 0
while i < len(cleaned_lines):
    line = cleaned_lines[i]
    if i + 1 < len(cleaned_lines) and cleaned_lines[i+1].startswith("→"):
        line = line + " " + cleaned_lines[i+1]
        i += 1
    elif i + 1 < len(cleaned_lines) and re.match(r'^\d+\)', cleaned_lines[i+1]):
        line = line + cleaned_lines[i+1]
        i += 1
    elif i + 1 < len(cleaned_lines) and cleaned_lines[i+1].startswith("Notwendigkeit"):
        line = line + " " + cleaned_lines[i+1]
        i += 1
        
    trans = None
    if i + 1 < len(cleaned_lines) and cleaned_lines[i+1].startswith("(") and cleaned_lines[i+1].endswith("dịch)"):
        trans = cleaned_lines[i+1]
        i += 1
        
    items.append({'raw': line, 'trans': trans})
    i += 1

print(f"Total structured index items: {len(items)}")

# 2. Extract parsed fields
parsed_items = []
for it in items:
    raw = it['raw']
    m_page = re.search(r'\(tr\.?\s*(\d+)\)', raw)
    page_num = m_page.group(1) if m_page else ""
    
    see_also = ""
    m_see = re.search(r'→\s*Xem:\s*([^()]+)', raw)
    if m_see:
        see_also = m_see.group(1).strip()
        
    parts = [p.strip() for p in raw.split('/')]
    title_vn = parts[0]
    title_de = parts[1] if len(parts) > 1 else ""
    title_en = parts[2] if len(parts) > 2 else ""
    title_en = re.sub(r'\(tr\.?\s*\d+\)', '', title_en).strip()
    title_en = re.sub(r'→.*', '', title_en).strip()
    
    parsed_items.append({
        'raw': raw,
        'title_vn': title_vn,
        'title_de': title_de,
        'title_en': title_en,
        'page': page_num,
        'see_also': see_also,
        'trans': it['trans']
    })

# 3. Locate target body paragraphs
body_headings = []
for idx in range(20, 3550):
    p = doc.paragraphs[idx]
    t = p.text.strip()
    if not t: continue
    if "[Đức:" in t or "(Đức:" in t:
        title_part = re.split(r'\[Đức:|\(Đức:', t)[0].strip()
        body_headings.append((idx, p, t, clean_txt(title_part)))
    elif p.style.name == "Heading 3" and len(t) <= 3 and t.isupper():
        body_headings.append((idx, p, t, clean_txt(t)))

# Match each parsed item
bm_counter = 100
for it in parsed_items:
    clean_vn = clean_txt(it['title_vn'])
    # Specific overrides for OCR misspellings in body
    if "lịch sử" in clean_vn and "sử học" in clean_vn:
        clean_vn = "lịch sữ sữ học"
    elif "nhìn nhận" in clean_vn and "thừa nhận" in clean_vn:
        clean_vn = "nhìn nhận thữa nhận công nhận sự"
        
    best_match = None
    for bh in body_headings:
        vn_words = clean_vn.split()[:2]
        if vn_words and " ".join(vn_words) in bh[3]:
            best_match = bh
            break
            
    if best_match:
        it['target_p'] = best_match[1]
        it['target_idx'] = best_match[0]
        it['bm_name'] = f"bm_entry_{bm_counter}"
        add_bookmark(best_match[1], bm_counter, it['bm_name'])
        bm_counter += 1
    else:
        it['target_p'] = None
        it['target_idx'] = None
        it['bm_name'] = None

print(f"Bookmarked {bm_counter - 100} dictionary entries!")

# Front matter bookmarks
front_matter_defs = [
    (23, "bm_front_tu_dien_de_hoc", "TỪ ĐIỂN ĐỂ... HỌC! (Lời người dịch – Bùi Văn Nam Sơn)"),
    (48, "bm_front_viet_tat", "Viết tắt tên các tác phẩm được trích dẫn"),
    (77, "bm_front_ngon_ngu_hegel", "Ngôn ngữ Hegel (Michael Inwood)"),
    (88, "bm_front_ngon_ngu_duc", "— Ngôn ngữ Đức"),
    (112, "bm_front_tieng_duc_triet_hoc", "— Sự phát triển của tiếng Đức Triết học"),
    (145, "bm_front_ngon_ngu_cua_hegel", "— Ngôn ngữ của Hegel"),
    (192, "bm_front_ket_luan", "— Kết luận"),
    (220, "bm_front_doi_net_ve_hegel", "Đôi nét về Hegel (Tiểu sử & Bối cảnh thời đại)"),
]

for p_idx, bm_name, title in front_matter_defs:
    bm_counter += 1
    add_bookmark(doc.paragraphs[p_idx], bm_counter, bm_name)

# End matter bookmarks
end_matter_defs = [
    (3423, "bm_end_thu_muc", "Thư mục tham khảo (Tác phẩm & Chuyên khảo)"),
    (3777, "bm_end_chi_muc_vda", "Bảng chỉ mục nội dung Việt – Đức – Anh"),
    (4181, "bm_end_chi_muc_dav", "Bảng chỉ mục nội dung Đức – Anh – Việt"),
    (4385, "bm_end_chi_muc_adv", "Bảng chỉ mục nội dung Anh – Đức – Việt"),
]

for p_idx, bm_name, title in end_matter_defs:
    bm_counter += 1
    add_bookmark(doc.paragraphs[p_idx], bm_counter, bm_name)

# Letter headings A-Y in body
letter_headers = {}
for idx in range(300, 3450):
    p = doc.paragraphs[idx]
    t = p.text.strip()
    if p.style.name == "Heading 3" and len(t) <= 2 and t.isupper():
        bm_counter += 1
        bm_name = f"bm_letter_{t}"
        add_bookmark(p, bm_counter, bm_name)
        letter_headers[t] = bm_name

print(f"Bookmarked {len(letter_headers)} letter sections.")

# 4. Build Table of Contents paragraphs
toc_paragraphs = []

# Title
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(18)
p_title.paragraph_format.space_after = Pt(4)
r_title = add_run(p_title, "MỤC LỤC CHI TIẾT CÁC MỤC TỪ", font_size_pt=18, bold=True, color="003366")

# Subtitle
p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(4)
add_run(p_sub, "TỪ ĐIỂN TRIẾT HỌC HEGEL (MICHAEL INWOOD)", font_size_pt=12, bold=True, color="444444")

p_sub2 = doc.add_paragraph()
p_sub2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub2.paragraph_format.space_after = Pt(16)
add_run(p_sub2, "(Bản dịch tiếng Việt – Bùi Văn Nam Sơn chủ trương & hiệu đính)", font_size_pt=10.5, italic=True, color="666666")

p_sub3 = doc.add_paragraph()
p_sub3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub3.paragraph_format.space_after = Pt(20)
add_run(p_sub3, "Tra cứu nhanh theo vần A – Y • Số trang nguyên bản • Bấm vào từ để đến trực tiếp mục từ", font_size_pt=10, italic=True, color="880000")

toc_paragraphs.extend([p_title, p_sub, p_sub2, p_sub3])

def make_toc_section_header(title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    add_run(p, title, font_size_pt=12, bold=True, color="003366")
    return p

def make_toc_line(title, page_str, bm_name=None, sub_text="", italic_sub=True, bullet="• "):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    
    add_run(p, bullet, font_size_pt=10, bold=True, color="003366")
    
    if bm_name:
        h = create_hyperlink_run(bm_name, title, font_size_pt=10.5, bold=True, color="004B87")
        p._p.append(h)
    else:
        add_run(p, title, font_size_pt=10.5, bold=True, color="222222")
        
    if sub_text:
        add_run(p, "  " + sub_text, font_size_pt=9.5, italic=italic_sub, color="555555")
        
    if page_str:
        dots = " " + "." * 10 + " "
        add_run(p, dots, font_size_pt=9, color="AAAAAA")
        if bm_name:
            h_page = create_hyperlink_run(bm_name, f"tr. {page_str}", font_size_pt=10, bold=True, color="880000")
            p._p.append(h_page)
        else:
            add_run(p, f"tr. {page_str}", font_size_pt=10, bold=True, color="880000")
            
    return p

# I. Front matter in TOC
toc_paragraphs.append(make_toc_section_header("I. PHẦN ĐẦU SÁCH: DẪN LUẬN & QUY CÁCH"))
for p_idx, bm_name, title in front_matter_defs:
    p_line = make_toc_line(title, "", bm_name=bm_name, bullet="▪ " if not title.startswith("—") else "    ▫ ")
    toc_paragraphs.append(p_line)

# II. Dictionary Entries grouped by letter
toc_paragraphs.append(make_toc_section_header("II. PHẦN CHÍNH VĂN: CÁC MỤC TỪ THEO VẦN A – Y"))

current_letter = None
for it in parsed_items:
    first_char = it['title_vn'].strip()[:1].upper()
    if it['title_vn'].strip().startswith("Đ"):
        first_char = "Đ"
    elif it['title_vn'].strip().startswith("D"):
        first_char = "D"
        
    if first_char != current_letter:
        current_letter = first_char
        p_letter = doc.add_paragraph()
        p_letter.paragraph_format.space_before = Pt(10)
        p_letter.paragraph_format.space_after = Pt(4)
        bm_let = letter_headers.get(current_letter, None)
        if bm_let:
            h_let = create_hyperlink_run(bm_let, f"— MỤC TỪ VẦN {current_letter} —", font_size_pt=11, bold=True, color="880000")
            p_letter._p.append(h_let)
        else:
            add_run(p_letter, f"— MỤC TỪ VẦN {current_letter} —", font_size_pt=11, bold=True, color="880000")
        toc_paragraphs.append(p_letter)
        
    sub_parts = []
    if it['title_de'] and it['title_en']:
        sub_parts.append(f"[{it['title_de']} / {it['title_en']}]")
    elif it['title_de']:
        sub_parts.append(f"[{it['title_de']}]")
    if it['see_also']:
        sub_parts.append(f"→ Xem: {it['see_also']}")
    if it['trans']:
        sub_parts.append(f"({it['trans'].replace('(', '').replace(')', '')})")
    sub_text = " ".join(sub_parts)
    
    p_entry = make_toc_line(it['title_vn'], it['page'], bm_name=it['bm_name'], sub_text=sub_text)
    toc_paragraphs.append(p_entry)

# III. End matter in TOC
toc_paragraphs.append(make_toc_section_header("III. PHẦN CUỐI SÁCH: TÀI LIỆU THAM KHẢO & CÁC BẢNG CHỈ MỤC"))
for p_idx, bm_name, title in end_matter_defs:
    p_end = make_toc_line(title, "", bm_name=bm_name, bullet="▪ ")
    toc_paragraphs.append(p_end)

# Add page break paragraph after TOC
p_break = doc.add_paragraph()
r_break = p_break.add_run()
r_break.add_break(docx.enum.text.WD_BREAK.PAGE)
toc_paragraphs.append(p_break)

print(f"Generated {len(toc_paragraphs)} TOC paragraphs.")

# 5. Insert TOC paragraphs before paragraph 23 (TỪ ĐIỂN ĐỂ... HỌC!)
target_start_p = doc.paragraphs[22]
for toc_p in toc_paragraphs:
    target_start_p._p.addprevious(toc_p._p)

print("Inserted TOC before paragraph 23.")

# 6. Remove the broken trailing stub paragraphs at the end (paragraphs with "Table of Contents")
for p in list(doc.paragraphs):
    if p.text.strip() == "Table of Contents":
        curr = p._p
        while curr is not None:
            nxt = curr.getnext()
            parent = curr.getparent()
            parent.remove(curr)
            curr = nxt
        print("Removed trailing Table of Contents stub.")
        break

# 7. Save document to target paths
out_desktop_hegel = src_path
out_desktop_clean = r"C:\Users\Admin\Desktop\TU_DIEN_TRIET_HOC_HEGEL_CO_MUC_LUC.docx"
out_user_uploaded = r"C:\Users\Admin\.gemini\antigravity\brain\67523c2b-9f56-4a83-b1bc-4eb7a3f380fc\.user_uploaded\media_1793604932812_8ce6ce96.docx"

doc.save(out_desktop_hegel)
print("Saved:", out_desktop_hegel, f"({os.path.getsize(out_desktop_hegel)} bytes)")

doc.save(out_desktop_clean)
print("Saved:", out_desktop_clean, f"({os.path.getsize(out_desktop_clean)} bytes)")

doc.save(out_user_uploaded)
print("Saved:", out_user_uploaded, f"({os.path.getsize(out_user_uploaded)} bytes)")

print("\n--- ALL COMPLETED PERFECTLY! ---")
