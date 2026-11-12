"""
rebuild_toc_hegel_v3.py
========================
Tái thiết Mục lục Từ điển Triết học Hegel đạt chuẩn xuất bản cao cấp.

Các cải tiến:
1. Chuẩn hóa 19 phân mục vần A – Y theo đúng cấu trúc sách:
   - A: Ánh tượng và Ánh hiện
   - D: Dân tộc và Quốc gia, Duy tâm (thuyết, chủ nghĩa)
   - Đ: Đại cương Bách khoa thư..., Đẹp..., Định mệnh..., Định nghĩa..., Đối lập..., Đời sống..., Đối tượng..., Đồng nhất...
   - Y: Ý chí..., Ý niệm..., Ý thể..., Ý thức...
2. Băng tiêu đề vần (Letter divider): Hợp nhất 2 cột (gridSpan=2), nền xanh navy #1A3A5C, chữ trắng in hoa đậm, gắn hyperlink đến đúng phần vần trong chính văn.
3. Bố cục bảng 2 cột không viền (borderless table):
   - Cột 1 (rộng 7100 twips ~ 12.5 cm):
       + Dòng 1: Thuật ngữ tiếng Việt (In đậm 10.5pt, màu xanh #1A3A5C, gắn Hyperlink)
       + Dòng 2: Thuật ngữ Đức / Anh / Xem thêm (Nghiêng 9pt, màu xám #555555)
   - Cột 2 (rộng 1206 twips ~ 2.1 cm):
       + Số trang canh phải (In đậm 10.5pt, màu đỏ sẫm #8B2020, gắn Hyperlink)
4. Phần đầu sách & Phần cuối sách phân tầng rõ rệt, mục con thụt đầu dòng (indent).
5. Xóa triệt để các đoạn văn rác / stub cũ.
"""

import docx
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import shutil, re, unicodedata, os

# ─── File Paths ────────────────────────────────────────────────────────────────
BACKUP = r"C:\Users\Admin\Desktop\NGU\book\Hegel\13003-tu-dien-triet-hoc-hegel-thuviensach.vn_backup.docx"
OUT_1  = r"C:\Users\Admin\Desktop\NGU\book\Hegel\13003-tu-dien-triet-hoc-hegel-thuviensach.vn.docx"
OUT_2  = r"C:\Users\Admin\Desktop\NGU\book\Hegel\TU_DIEN_TRIET_HOC_HEGEL_CO_MUC_LUC.docx"
OUT_3  = r"C:\Users\Admin\.gemini\antigravity\brain\67523c2b-9f56-4a83-b1bc-4eb7a3f380fc\.user_uploaded\media_1793604932812_8ce6ce96.docx"

# ─── Dimensions ────────────────────────────────────────────────────────────────
TOTAL_W   = 8306   # twips (~14.65 cm, text area width on A4 with 2.5cm margins)
COL_TITLE = 7100   # twips (~12.52 cm)
COL_PAGE  = 1206   # twips (~2.13 cm)

# ─── Helpers ───────────────────────────────────────────────────────────────────
def clean_txt(t):
    if not t: return ""
    t = unicodedata.normalize('NFC', t).lower()
    t = re.sub(r'[^\w\s]', ' ', t)
    return " ".join(t.split())

def _rpr(font="Times New Roman", sz_pt=11, bold=False, italic=False, color=None, underline=False):
    rPr = OxmlElement('w:rPr')
    if font:
        rFonts = OxmlElement('w:rFonts')
        rFonts.set(qn('w:ascii'), font)
        rFonts.set(qn('w:hAnsi'), font)
        rFonts.set(qn('w:cs'), font)
        rPr.append(rFonts)
    if sz_pt:
        sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(int(sz_pt * 2))); rPr.append(sz)
        szCs = OxmlElement('w:szCs'); szCs.set(qn('w:val'), str(int(sz_pt * 2))); rPr.append(szCs)
    if bold:
        rPr.append(OxmlElement('w:b'))
    if italic:
        rPr.append(OxmlElement('w:i'))
    if color:
        c = OxmlElement('w:color'); c.set(qn('w:val'), color); rPr.append(c)
    if underline:
        u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rPr.append(u)
    return rPr

def _run(text, font="Times New Roman", sz_pt=11, bold=False, italic=False, color=None):
    r = OxmlElement('w:r')
    r.append(_rpr(font, sz_pt, bold, italic, color))
    t = OxmlElement('w:t')
    t.text = text
    t.set(qn('xml:space'), 'preserve')
    r.append(t)
    return r

def _hyperlink(anchor, text, font="Times New Roman", sz_pt=11, bold=False, italic=False, color=None):
    hl = OxmlElement('w:hyperlink')
    hl.set(qn('w:anchor'), anchor)
    hl.set(qn('w:history'), '1')
    r = OxmlElement('w:r')
    r.append(_rpr(font, sz_pt, bold, italic, color, underline=False))
    t = OxmlElement('w:t')
    t.text = text
    t.set(qn('xml:space'), 'preserve')
    r.append(t)
    hl.append(r)
    return hl

def add_bookmark(paragraph, bm_id, bm_name):
    p = paragraph._p
    bm_s = OxmlElement('w:bookmarkStart')
    bm_s.set(qn('w:id'), str(bm_id))
    bm_s.set(qn('w:name'), bm_name)
    bm_e = OxmlElement('w:bookmarkEnd')
    bm_e.set(qn('w:id'), str(bm_id))
    p.insert(0, bm_s)
    p.append(bm_e)

def _set_col_width(cell, width_twips):
    tc = cell._tc
    tcPr = tc.find(qn('w:tcPr'))
    if tcPr is None:
        tcPr = OxmlElement('w:tcPr'); tc.insert(0, tcPr)
    tcW = tcPr.find(qn('w:tcW'))
    if tcW is None:
        tcW = OxmlElement('w:tcW'); tcPr.append(tcW)
    tcW.set(qn('w:w'), str(width_twips))
    tcW.set(qn('w:type'), 'dxa')

def _set_cell_color(cell, fill_hex):
    tc = cell._tc
    tcPr = tc.find(qn('w:tcPr'))
    if tcPr is None:
        tcPr = OxmlElement('w:tcPr'); tc.insert(0, tcPr)
    shd = tcPr.find(qn('w:shd'))
    if shd is None:
        shd = OxmlElement('w:shd'); tcPr.append(shd)
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)

def _no_borders(table):
    tbl = table._tbl
    tblPr = tbl.find(qn('w:tblPr'))
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr'); tbl.insert(0, tblPr)
    tblBorders = OxmlElement('w:tblBorders')
    for side in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'), 'none')
        el.set(qn('w:sz'), '0')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), 'auto')
        tblBorders.append(el)
    existing = tblPr.find(qn('w:tblBorders'))
    if existing is not None:
        tblPr.remove(existing)
    tblPr.append(tblBorders)

def _set_table_width(table, total_twips):
    tbl = table._tbl
    tblPr = tbl.find(qn('w:tblPr'))
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr'); tbl.insert(0, tblPr)
    tblW = tblPr.find(qn('w:tblW'))
    if tblW is None:
        tblW = OxmlElement('w:tblW'); tblPr.append(tblW)
    tblW.set(qn('w:w'), str(total_twips))
    tblW.set(qn('w:type'), 'dxa')

def make_heading_para(text, sz_pt=18, color="1A3A5C", space_before=240, space_after=60):
    p = OxmlElement('w:p')
    pPr = OxmlElement('w:pPr')
    jc = OxmlElement('w:jc'); jc.set(qn('w:val'), 'center'); pPr.append(jc)
    sp = OxmlElement('w:spacing')
    sp.set(qn('w:before'), str(space_before))
    sp.set(qn('w:after'), str(space_after))
    pPr.append(sp)
    p.append(pPr)
    p.append(_run(text, sz_pt=sz_pt, bold=True, color=color))
    return p

def make_subtitle_para(text, sz_pt=11, color="444444", italic=False, bold=False, space_before=0, space_after=60):
    p = OxmlElement('w:p')
    pPr = OxmlElement('w:pPr')
    jc = OxmlElement('w:jc'); jc.set(qn('w:val'), 'center'); pPr.append(jc)
    sp = OxmlElement('w:spacing')
    sp.set(qn('w:before'), str(space_before))
    sp.set(qn('w:after'), str(space_after))
    pPr.append(sp)
    p.append(pPr)
    p.append(_run(text, sz_pt=sz_pt, bold=bold, italic=italic, color=color))
    return p

def make_divider_para(color="1A3A5C"):
    p = OxmlElement('w:p')
    pPr = OxmlElement('w:pPr')
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), color)
    pBdr.append(bottom)
    pPr.append(pBdr)
    sp = OxmlElement('w:spacing'); sp.set(qn('w:before'), '40'); sp.set(qn('w:after'), '80')
    pPr.append(sp)
    p.append(pPr)
    return p

def make_section_label_para(text, sz_pt=10.5, color="1A3A5C", space_before=180, space_after=60):
    p = OxmlElement('w:p')
    pPr = OxmlElement('w:pPr')
    sp = OxmlElement('w:spacing'); sp.set(qn('w:before'), str(space_before)); sp.set(qn('w:after'), str(space_after))
    pPr.append(sp)
    p.append(pPr)
    p.append(_run(text, sz_pt=sz_pt, bold=True, color=color))
    return p

def make_page_break_para():
    p = OxmlElement('w:p')
    r = OxmlElement('w:r')
    br = OxmlElement('w:br'); br.set(qn('w:type'), 'page')
    r.append(br)
    p.append(r)
    return p

# ─── Load Document from Backup ─────────────────────────────────────────────────
print("1. Đang nạp tài liệu từ file backup...")
doc = Document(BACKUP)
print(f"   Đã nạp {len(doc.paragraphs)} đoạn văn.")

# ─── Parse Index ───────────────────────────────────────────────────────────────
print("2. Đang phân tích Bảng chỉ mục nội dung...")
raw_index = []
in_vn = False
for i in range(3770, 4185):
    t = doc.paragraphs[i].text.strip()
    if "BẢNG CHỈ MỤC NỘI DUNG VIỆT - ĐỨC - ANH" in t:
        in_vn = True; continue
    if "BẢNG CHỈ MỤC NỘI DUNG ĐỨC - ANH - VIỆT" in t:
        in_vn = False; break
    if in_vn and t:
        raw_index.append(t)

cleaned_lines = []
for line in raw_index:
    if "(Nguyễn Văn Sướng dịch) Tập tục" in line:
        cleaned_lines.append("(Nguyễn Văn Sướng dịch)")
        cleaned_lines.append("Tập tục / Sitte / custom → Xem: Đời sống Đạo đức và Tập tục (tr.389)")
        cleaned_lines.append("Tất yếu (tính, sự), Khả năng, Khả thể và Bất tất (tính, sự) /")
    else:
        cleaned_lines.append(line)

items = []
i = 0
while i < len(cleaned_lines):
    line = cleaned_lines[i]
    if i + 1 < len(cleaned_lines) and cleaned_lines[i+1].startswith("→"):
        line = line + " " + cleaned_lines[i+1]; i += 1
    elif i + 1 < len(cleaned_lines) and re.match(r'^\d+\)', cleaned_lines[i+1]):
        line = line + cleaned_lines[i+1]; i += 1
    elif i + 1 < len(cleaned_lines) and cleaned_lines[i+1].startswith("Notwendigkeit"):
        line = line + " " + cleaned_lines[i+1]; i += 1
    trans = None
    if i + 1 < len(cleaned_lines) and cleaned_lines[i+1].startswith("(") and cleaned_lines[i+1].endswith("dịch)"):
        trans = cleaned_lines[i+1]; i += 1
    items.append({'raw': line, 'trans': trans})
    i += 1

parsed_items = []
for it in items:
    raw = it['raw']
    m_page = re.search(r'\(tr\.?\s*(\d+)\s*\)', raw)
    page_num = m_page.group(1) if m_page else ""
    m_see = re.search(r'→\s*Xem:\s*([^()]+)', raw)
    see_also = m_see.group(1).strip() if m_see else ""
    parts = [p.strip() for p in raw.split('/')]
    title_vn = parts[0]
    title_de = parts[1] if len(parts) > 1 else ""
    title_en = parts[2] if len(parts) > 2 else ""
    title_en = re.sub(r'\(tr\.?\s*\d+\s*\)', '', title_en).strip()
    title_en = re.sub(r'→.*', '', title_en).strip()
    parsed_items.append({
        'raw': raw, 'title_vn': title_vn,
        'title_de': title_de, 'title_en': title_en,
        'page': page_num, 'see_also': see_also,
        'trans': it['trans']
    })

print(f"   Đã trích xuất {len(parsed_items)} mục từ.")

# ─── Locate Target Paragraphs & Bookmark ───────────────────────────────────────
print("3. Đang đánh dấu Bookmark cho các mục từ và phân mục trong chính văn...")
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

bm_counter = 100
for it in parsed_items:
    clean_vn = clean_txt(it['title_vn'])
    if "lịch sử" in clean_vn and "sử học" in clean_vn:
        clean_vn = "lịch sữ sữ học"
    elif "nhìn nhận" in clean_vn and "thừa nhận" in clean_vn:
        clean_vn = "nhìn nhận thữa nhận công nhận sự"
    best = None
    for bh in body_headings:
        vn_words = clean_vn.split()[:2]
        if vn_words and " ".join(vn_words) in bh[3]:
            best = bh; break
    if best:
        it['bm_name'] = f"bm_entry_{bm_counter}"
        add_bookmark(best[1], bm_counter, it['bm_name'])
        bm_counter += 1
    else:
        it['bm_name'] = None

print(f"   Đã gắn bookmark cho {bm_counter - 100} mục từ.")

# Front matter bookmarks
front_matter_defs = [
    (23,  "bm_front_tu_dien_de_hoc",       "TỪ ĐIỂN ĐỂ... HỌC! (Lời người dịch – Bùi Văn Nam Sơn)"),
    (48,  "bm_front_viet_tat",             "Viết tắt tên các tác phẩm được trích dẫn"),
    (77,  "bm_front_ngon_ngu_hegel",       "Ngôn ngữ Hegel (Michael Inwood)"),
    (88,  "bm_front_ngon_ngu_duc",         "Ngôn ngữ Đức"),
    (112, "bm_front_tieng_duc_triet_hoc",  "Sự phát triển của tiếng Đức Triết học"),
    (145, "bm_front_ngon_ngu_cua_hegel",   "Ngôn ngữ của Hegel"),
    (192, "bm_front_ket_luan",             "Kết luận"),
    (220, "bm_front_doi_net_ve_hegel",     "Đôi nét về Hegel (Tiểu sử & Bối cảnh thời đại)"),
]

# End matter bookmarks
end_matter_defs = [
    (3423, "bm_end_thu_muc",       "Thư mục tham khảo (Tác phẩm & Chuyên khảo)"),
    (3777, "bm_end_chi_muc_vda",   "Bảng chỉ mục nội dung Việt – Đức – Anh"),
    (4181, "bm_end_chi_muc_dav",   "Bảng chỉ mục nội dung Đức – Anh – Việt"),
    (4385, "bm_end_chi_muc_adv",   "Bảng chỉ mục nội dung Anh – Đức – Việt"),
]

for p_idx, bm_name, title in front_matter_defs + end_matter_defs:
    bm_counter += 1
    add_bookmark(doc.paragraphs[p_idx], bm_counter, bm_name)

letter_headers = {}
for idx in range(300, 3450):
    p = doc.paragraphs[idx]
    t = p.text.strip()
    if p.style.name == "Heading 3" and len(t) <= 2 and t.isupper():
        bm_counter += 1
        bm_name = f"bm_letter_{t}"
        add_bookmark(p, bm_counter, bm_name)
        letter_headers[t] = bm_name

print(f"   Đã gắn bookmark cho {len(letter_headers)} phần phân loại chữ cái A–Y.")

# ─── Group into 19 Canonical Sections ──────────────────────────────────────────
def get_letter_section(title_vn):
    u = title_vn.strip().upper()
    if u.startswith('Á') or u.startswith('A'): return 'A'
    if u.startswith('Đ'): return 'Đ'
    if u.startswith('D'): return 'D'
    if u.startswith('Ý') or u.startswith('Y'): return 'Y'
    return u[0]

sections_dict = {}
for it in parsed_items:
    sec = get_letter_section(it['title_vn'])
    sections_dict.setdefault(sec, []).append(it)

# Special adjustment: In section D, ensure "Dân tộc và Quốc gia" comes first, then "Duy tâm"
if 'D' in sections_dict:
    sections_dict['D'].sort(key=lambda x: 0 if 'Dân tộc' in x['title_vn'] else 1)

CANONICAL_LETTERS = ['A', 'B', 'C', 'D', 'Đ', 'G', 'H', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y']

# ─── Build Table Elements ──────────────────────────────────────────────────────
print("4. Đang tạo các khối giao diện bảng Mục lục...")

def build_front_end_table(entries):
    tbl = doc.add_table(rows=0, cols=2)
    _no_borders(tbl)
    _set_table_width(tbl, TOTAL_W)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    for en in entries:
        row = tbl.add_row()
        c1, c2 = row.cells[0], row.cells[1]
        _set_col_width(c1, COL_TITLE)
        _set_col_width(c2, COL_PAGE)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(2.5)
        p1.paragraph_format.space_after  = Pt(2.5)
        if en.get('indent', 0) > 0:
            pPr1 = p1._p.find(qn('w:pPr'))
            if pPr1 is None:
                pPr1 = OxmlElement('w:pPr'); p1._p.insert(0, pPr1)
            ind = OxmlElement('w:ind')
            ind.set(qn('w:left'), str(en['indent']))
            pPr1.append(ind)
        
        prefix = "• " if not en.get('is_sub') else "— "
        if en['bm_name']:
            p1._p.append(_hyperlink(en['bm_name'], prefix + en['title'],
                                    sz_pt=10.5, bold=en.get('bold', False), color="1A3A5C"))
        else:
            p1._p.append(_run(prefix + en['title'], sz_pt=10.5,
                              bold=en.get('bold', False), color="333333"))
        p2 = c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p2.paragraph_format.space_before = Pt(2.5)
        p2.paragraph_format.space_after  = Pt(2.5)
    return tbl

def build_dictionary_table():
    tbl = doc.add_table(rows=0, cols=2)
    _no_borders(tbl)
    _set_table_width(tbl, TOTAL_W)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT

    for letter in CANONICAL_LETTERS:
        items_in_sec = sections_dict.get(letter, [])
        if not items_in_sec:
            continue
        
        # ── Letter Section Divider Header (Full span navy band) ───────────────
        row_hdr = tbl.add_row()
        c1, c2 = row_hdr.cells[0], row_hdr.cells[1]
        _set_col_width(c1, TOTAL_W)
        _set_cell_color(c1, "1A3A5C")
        
        # Set gridSpan = 2 on c1 and remove c2 XML
        c1_tc = c1._tc
        tcPr1 = c1_tc.find(qn('w:tcPr'))
        if tcPr1 is None:
            tcPr1 = OxmlElement('w:tcPr'); c1_tc.insert(0, tcPr1)
        gridSpan = OxmlElement('w:gridSpan'); gridSpan.set(qn('w:val'), '2'); tcPr1.append(gridSpan)
        
        # Remove c2 tc element from row
        tr = row_hdr._tr
        tr.remove(c2._tc)
        
        p_hdr = c1.paragraphs[0]
        p_hdr.paragraph_format.space_before = Pt(5)
        p_hdr.paragraph_format.space_after  = Pt(5)
        
        bm_let = letter_headers.get(letter)
        header_text = f"  MỤC TỪ VẦN {letter}  ({len(items_in_sec)} mục từ)"
        if bm_let:
            p_hdr._p.append(_hyperlink(bm_let, header_text, sz_pt=11.5, bold=True, color="FFFFFF"))
        else:
            p_hdr._p.append(_run(header_text, sz_pt=11.5, bold=True, color="FFFFFF"))

        # ── Rows for Entries ──────────────────────────────────────────────────
        for it in items_in_sec:
            row_entry = tbl.add_row()
            cell_title, cell_page = row_entry.cells[0], row_entry.cells[1]
            _set_col_width(cell_title, COL_TITLE)
            _set_col_width(cell_page, COL_PAGE)
            
            # Left cell: Vietnamese term
            pt = cell_title.paragraphs[0]
            pt.paragraph_format.space_before = Pt(2)
            pt.paragraph_format.space_after  = Pt(0)
            
            title_label = it['title_vn']
            if it['bm_name']:
                pt._p.append(_hyperlink(it['bm_name'], title_label, sz_pt=10.5, bold=True, color="1A3A5C"))
            else:
                pt._p.append(_run(title_label, sz_pt=10.5, bold=True, color="222222"))
                
            # Second line: German / English / Cross-ref / Translator
            sub_parts = []
            de_en = []
            if it['title_de']: de_en.append(it['title_de'])
            if it['title_en']: de_en.append(it['title_en'])
            if de_en:
                sub_parts.append(" / ".join(de_en))
            if it['see_also']:
                sub_parts.append(f"→ Xem: {it['see_also']}")
            if it['trans']:
                t_str = it['trans'].strip()
                if not t_str.startswith('('): t_str = f"({t_str})"
                sub_parts.append(t_str)
                
            if sub_parts:
                p_sub = OxmlElement('w:p')
                pPr_sub = OxmlElement('w:pPr')
                sp_sub = OxmlElement('w:spacing')
                sp_sub.set(qn('w:before'), '0')
                sp_sub.set(qn('w:after'), '30')
                pPr_sub.append(sp_sub)
                p_sub.append(pPr_sub)
                p_sub.append(_run(" | ".join(sub_parts), sz_pt=9, italic=True, color="555555"))
                cell_title._tc.append(p_sub)

            # Right cell: Page number (bold, dark red, hyperlink)
            pp = cell_page.paragraphs[0]
            pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            pp.paragraph_format.space_before = Pt(2)
            pp.paragraph_format.space_after  = Pt(0)
            
            if it['page']:
                page_str = f"tr. {it['page']}"
                if it['bm_name']:
                    pp._p.append(_hyperlink(it['bm_name'], page_str, sz_pt=10, bold=True, color="8B2020"))
                else:
                    pp._p.append(_run(page_str, sz_pt=10, bold=True, color="8B2020"))

    return tbl

# ─── Assemble all TOC elements ────────────────────────────────────────────────
toc_elements = []

# Title & Subtitle block
toc_elements.append(make_heading_para("MỤC LỤC CHI TIẾT CÁC MỤC TỪ", sz_pt=20, color="1A3A5C", space_before=240, space_after=60))
toc_elements.append(make_subtitle_para("TỪ ĐIỂN TRIẾT HỌC HEGEL (Michael Inwood)", sz_pt=12, color="333333", bold=True, space_after=30))
toc_elements.append(make_subtitle_para("Bản dịch tiếng Việt — Bùi Văn Nam Sơn chủ trương & hiệu đính", sz_pt=10.5, color="666666", italic=True, space_after=80))
toc_elements.append(make_subtitle_para("Bấm vào tên mục từ hoặc số trang để chuyển trực tiếp đến nội dung mục từ", sz_pt=9.5, color="8B2020", italic=True, space_after=100))
toc_elements.append(make_divider_para("1A3A5C"))

# Section I: Front matter
toc_elements.append(make_section_label_para("I. PHẦN ĐẦU SÁCH — DẪN LUẬN & QUY CÁCH", sz_pt=11, color="1A3A5C", space_before=160, space_after=60))
front_entries = []
for p_idx, bm_name, title in front_matter_defs:
    is_sub = title in ["Ngôn ngữ Đức", "Sự phát triển của tiếng Đức Triết học", "Ngôn ngữ của Hegel", "Kết luận"]
    front_entries.append({
        'title': title, 'bm_name': bm_name,
        'bold': not is_sub, 'is_sub': is_sub,
        'indent': 360 if is_sub else 0
    })
front_tbl = build_front_end_table(front_entries)
toc_elements.append(front_tbl._tbl)

toc_elements.append(make_divider_para("CCCCCC"))

# Section II: Dictionary
toc_elements.append(make_section_label_para("II. PHẦN CHÍNH VĂN — 139 MỤC TỪ THEO VẦN A – Y", sz_pt=11, color="1A3A5C", space_before=160, space_after=60))
dict_tbl = build_dictionary_table()
toc_elements.append(dict_tbl._tbl)

toc_elements.append(make_divider_para("CCCCCC"))

# Section III: End matter
toc_elements.append(make_section_label_para("III. PHẦN CUỐI SÁCH — TÀI LIỆU THAM KHẢO & CÁC BẢNG CHỈ MỤC", sz_pt=11, color="1A3A5C", space_before=160, space_after=60))
end_entries = [{
    'title': title, 'bm_name': bm_name,
    'bold': True, 'is_sub': False, 'indent': 0
} for p_idx, bm_name, title in end_matter_defs]
end_tbl = build_front_end_table(end_entries)
toc_elements.append(end_tbl._tbl)

toc_elements.append(make_divider_para("1A3A5C"))
toc_elements.append(make_page_break_para())

# ─── Insert TOC into document ──────────────────────────────────────────────────
print("5. Đang chèn Mục lục vào tài liệu...")
anchor_p = doc.paragraphs[22]._p
for el in toc_elements:
    anchor_p.addprevious(el)

# ─── Remove trailing stub ──────────────────────────────────────────────────────
for p in list(doc.paragraphs):
    if p.text.strip() == "Table of Contents":
        cur = p._p
        while cur is not None:
            nxt = cur.getnext()
            par = cur.getparent()
            par.remove(cur)
            cur = nxt
        print("   Đã dọn dẹp các đoạn Table of Contents rác ở cuối sách.")
        break

# ─── Save Document ─────────────────────────────────────────────────────────────
print("6. Đang lưu tài liệu hoàn thiện...")
for out_path in [OUT_1, OUT_2, OUT_3]:
    doc.save(out_path)
    sz = os.path.getsize(out_path)
    print(f"   ✓ Đã lưu thành công: {out_path} ({sz:,} bytes)")

print("\n🎉 HOÀN THÀNH XUẤT SẮC! Mục lục đã được làm mới hoàn toàn theo tiêu chuẩn xuất bản cao cấp.")
