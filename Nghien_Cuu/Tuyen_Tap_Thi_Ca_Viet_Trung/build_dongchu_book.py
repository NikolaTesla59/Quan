import subprocess
import re
import html
import os
import time
import json
import textwrap
from concurrent.futures import ThreadPoolExecutor, as_completed
import bs4
import pymupdf

dest_dir = r'C:\Users\Admin\Desktop\Sách\Lịch sử & Biên niên sử\02_Lịch sử Trung Quốc'
os.makedirs(dest_dir, exist_ok=True)
out_pdf = os.path.join(dest_dir, '[Dã sử & Khảo luận] Phùng Mộng Long - Đông Chu Liệt Quốc (Toàn Dịch 108 Hồi Kinh Điển).pdf')
cache_json = r'C:\Users\Admin\.gemini\antigravity\scratch\dongchu_chapters.json'

font_regular_path = r'C:\Windows\Fonts\times.ttf'
font_bold_path = r'C:\Windows\Fonts\timesbd.ttf'

font_reg = pymupdf.Font(fontfile=font_regular_path)
font_bold = pymupdf.Font(fontfile=font_bold_path)

def fetch_url_curl(url):
    for attempt in range(3):
        try:
            res = subprocess.run(
                ['curl.exe', '-k', '-s', '-A', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', url],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=25
            )
            if res.returncode == 0 and res.stdout:
                return res.stdout.decode('utf-8', errors='ignore')
        except Exception:
            time.sleep(1)
    return ''

def get_chapter_links():
    index_file = r'C:\Users\Admin\.gemini\antigravity\scratch\dongchu_index.html'
    if os.path.exists(index_file):
        with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
            page_html = f.read()
    else:
        page_html = fetch_url_curl('https://www.sachhayonline.com/tua-sach/dong-chu-liet-quoc')
    
    raw_links = re.findall(r'href=[\"\'](https://www\.sachhayonline\.com/doc-online/[^\"]+)[\"\'][^>]*>([^<]+)</a>', page_html)
    chapters = []
    seen = set()
    for link, raw_title in raw_links:
        t_clean = raw_title.strip()
        if not t_clean.startswith('Chương '):
            continue
        num_m = re.match(r'Chương\s+(\d+)', t_clean, re.IGNORECASE)
        if not num_m:
            continue
        num = int(num_m.group(1))
        if num in seen:
            continue
        seen.add(num)
        chapters.append((num, link, t_clean))
    
    chapters.sort(key=lambda x: x[0])
    return chapters

def fetch_single_chapter(chap_info):
    num, link, title = chap_info
    raw_html = fetch_url_curl(link)
    if not raw_html:
        return {'num': num, 'title': title, 'lines': []}
    
    soup = bs4.BeautifulSoup(raw_html, 'html.parser')
    div = soup.find('div', class_='chapter-content')
    if not div:
        for c in ['content', 'doc-content', 'entry-content']:
            div = soup.find('div', class_=c)
            if div: break
    
    if not div:
        return {'num': num, 'title': title, 'lines': []}
    
    for tag in div(['script', 'style', 'nav']):
        tag.decompose()
        
    lines = []
    for l in div.get_text('\n').splitlines():
        line_clean = l.strip()
        if line_clean and not line_clean.startswith('http') and not line_clean.startswith('Nguồn:') and not line_clean.startswith('Chia sẻ:'):
            lines.append(line_clean)
            
    return {'num': num, 'title': title, 'lines': lines}

def draw_center(page, y, text, fontname, font_obj, fontsize, color, page_w):
    w = font_obj.text_length(text, fontsize=fontsize)
    x = max(30, (page_w - w) / 2)
    page.insert_text(pymupdf.Point(x, y), text, fontname=fontname, fontsize=fontsize, color=color)

def main():
    all_chapters = []
    if os.path.exists(cache_json):
        print(f'Loading cached chapters from {cache_json}...')
        with open(cache_json, 'r', encoding='utf-8') as f:
            all_chapters = json.load(f)
    
    if len(all_chapters) < 108:
        print('1. Getting list of chapters...')
        chapters_info = get_chapter_links()
        print(f'Found {len(chapters_info)} chapters. Downloading concurrently with 10 workers...')
        
        all_chapters = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(fetch_single_chapter, c) for c in chapters_info]
            for f in as_completed(futures):
                res = f.result()
                all_chapters.append(res)
                if len(all_chapters) % 25 == 0 or len(all_chapters) == len(chapters_info):
                    print(f'  Downloaded {len(all_chapters)}/{len(chapters_info)} chapters...', flush=True)
        
        all_chapters.sort(key=lambda x: x['num'])
        
        # Save cache
        with open(cache_json, 'w', encoding='utf-8') as f:
            json.dump(all_chapters, f, ensure_ascii=False, indent=2)
        print('Saved chapters cache to JSON.')
    
    print('3. Generating Book PDF with PyMuPDF...')
    doc = pymupdf.open()
    
    page_w, page_h = 595, 842 # A4
    margin_l, margin_r = 54, 541 # width = 487
    margin_t, margin_b = 60, 782 # height = 722
    content_w = margin_r - margin_l
    
    # --- COVER PAGE ---
    cover = doc.new_page(width=page_w, height=page_h)
    cover.insert_font(fontname='Times-Bold', fontfile=font_bold_path)
    cover.insert_font(fontname='Times', fontfile=font_regular_path)
    
    rect_outer = pymupdf.Rect(36, 36, page_w - 36, page_h - 36)
    cover.draw_rect(rect_outer, color=(0.55, 0.1, 0.1), width=2)
    rect_inner = pymupdf.Rect(40, 40, page_w - 40, page_h - 40)
    cover.draw_rect(rect_inner, color=(0.7, 0.5, 0.2), width=0.75)
    
    draw_center(cover, 180, "TỦ SÁCH LỊCH SỬ & BIÊN NIÊN SỬ KINH ĐIỂN", 'Times-Bold', font_bold, 13, (0.55, 0.1, 0.1), page_w)
    draw_center(cover, 280, "ĐÔNG CHU LIỆT QUỐC", 'Times-Bold', font_bold, 26, (0.1, 0.1, 0.1), page_w)
    draw_center(cover, 320, "東 周 列 國 志", 'Times-Bold', font_bold, 18, (0.4, 0.4, 0.4), page_w)
    draw_center(cover, 360, "TRỌN BỘ TOÀN DỊCH 108 HỒI KINH ĐIỂN", 'Times-Bold', font_bold, 13, (0.55, 0.1, 0.1), page_w)
    
    draw_center(cover, 480, "Nguyên tác: Phùng Mộng Long (1574 - 1646)", 'Times', font_reg, 12, (0.2, 0.2, 0.2), page_w)
    draw_center(cover, 510, "Hiệu đính: Sái Nguyên Phóng (thời Thanh)", 'Times', font_reg, 12, (0.2, 0.2, 0.2), page_w)
    draw_center(cover, 540, "Dịch giả: Cụ Nguyễn Đỗ Mục", 'Times-Bold', font_bold, 12, (0.1, 0.1, 0.1), page_w)
    draw_center(cover, 600, "Phân loại: Dã sử & Khảo luận - Biên niên sử Xuân Thu & Chiến Quốc", 'Times', font_reg, 11, (0.3, 0.3, 0.3), page_w)
    draw_center(cover, 740, "XUẤT BẢN TOÀN TẬP ĐẦY ĐỦ", 'Times-Bold', font_bold, 11, (0.4, 0.4, 0.4), page_w)
    
    curr_page = None
    y_pos = margin_t
    page_num = 1
    
    def new_content_page():
        nonlocal curr_page, y_pos, page_num
        curr_page = doc.new_page(width=page_w, height=page_h)
        curr_page.insert_font(fontname='Times-Bold', fontfile=font_bold_path)
        curr_page.insert_font(fontname='Times', fontfile=font_regular_path)
        # Header
        curr_page.insert_text(pymupdf.Point(margin_l, 45), "ĐÔNG CHU LIỆT QUỐC  •  PHÙNG MỘNG LONG", fontname='Times-Bold', fontsize=8, color=(0.4, 0.4, 0.4))
        curr_page.draw_line(pymupdf.Point(margin_l, 50), pymupdf.Point(margin_r, 50), color=(0.7, 0.7, 0.7), width=0.5)
        # Footer
        p_text = f"- {page_num} -"
        draw_center(curr_page, page_h - 35, p_text, 'Times', font_reg, 9, (0.4, 0.4, 0.4), page_w)
        curr_page.draw_line(pymupdf.Point(margin_l, page_h - 48), pymupdf.Point(margin_r, page_h - 48), color=(0.85, 0.85, 0.85), width=0.5)
        y_pos = margin_t + 10
        page_num += 1
        return curr_page
    
    # --- TABLE OF CONTENTS ---
    print('  Formatting Table of Contents...')
    new_content_page()
    draw_center(curr_page, y_pos + 10, "MỤC LỤC TRỌN BỘ 108 HỒI", 'Times-Bold', font_bold, 16, (0.55, 0.1, 0.1), page_w)
    y_pos += 40
    
    for c in all_chapters:
        num = c['num']
        clean_t = c['title'].replace(f'Chương {num}:', '').strip()
        tline = f"Hồi {num}: {clean_t}"
        wrapped = textwrap.wrap(tline, width=88)
        if y_pos + len(wrapped) * 13 > margin_b:
            new_content_page()
        for wl in wrapped:
            curr_page.insert_text(pymupdf.Point(margin_l + 10, y_pos), wl, fontname='Times', fontsize=9, color=(0.15, 0.15, 0.15))
            y_pos += 13
        y_pos += 2
    
    # --- CHAPTER CONTENTS ---
    print('  Paginating 108 Chapters...')
    fontsize = 10
    line_h = 14
    
    for c in all_chapters:
        num = c['num']
        title = c['title']
        lines = c['lines']
        
        new_content_page()
        
        chap_title = title.replace('Chương ', 'HỒI ').upper()
        header_wrapped = textwrap.wrap(chap_title, width=65)
        y_pos += 8
        for hw in header_wrapped:
            draw_center(curr_page, y_pos, hw, 'Times-Bold', font_bold, 12.5, (0.55, 0.1, 0.1), page_w)
            y_pos += 17
        
        y_pos += 4
        curr_page.draw_line(pymupdf.Point(page_w/2 - 60, y_pos), pymupdf.Point(page_w/2 + 60, y_pos), color=(0.55, 0.1, 0.1), width=1)
        y_pos += 18
        
        for p in lines:
            is_poem = len(p) < 60 and ('/' in p or p.count(',') >= 2)
            indent = 25 if is_poem else 16
            wrap_w = 78 if is_poem else 92
            w_lines = textwrap.wrap(p, width=wrap_w)
            
            if y_pos + len(w_lines) * line_h > margin_b:
                new_content_page()
            
            first = True
            for wl in w_lines:
                curr_x = margin_l + indent if first else margin_l
                curr_page.insert_text(pymupdf.Point(curr_x, y_pos), wl, fontname='Times', fontsize=fontsize, color=(0.1, 0.1, 0.1))
                y_pos += line_h
                first = False
            y_pos += 4
    
    print(f'4. Saving master book PDF to {out_pdf}...')
    doc.save(out_pdf)
    doc.close()
    
    size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
    doc_check = pymupdf.open(out_pdf)
    final_pages = len(doc_check)
    doc_check.close()
    
    print(f'SUCCESS! Created Đông Chu Liệt Quốc PDF:')
    print(f'  Path: {out_pdf}')
    print(f'  Size: {size_mb:.2f} MB')
    print(f'  Total Pages: {final_pages}')

if __name__ == '__main__':
    main()
