"""
PDF Layout and Rendering Engine for Classical Poetry & Literature
Designed for PyMuPDF (fitz)
"""
import os
import pymupdf

FONT_VN_REG = r"C:\Windows\Fonts\times.ttf"
FONT_VN_BOLD = r"C:\Windows\Fonts\timesbd.ttf"
FONT_VN_ITALIC = r"C:\Windows\Fonts\timesi.ttf"
FONT_VN_BI = r"C:\Windows\Fonts\timesbi.ttf"
FONT_ZH = r"C:\Windows\Fonts\msyh.ttc"  # Microsoft YaHei supports full CJK

PAGE_W = 595.3
PAGE_H = 841.9
MARGIN_L = 50.0
MARGIN_R = 50.0
MARGIN_T = 55.0
MARGIN_B = 55.0
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

class PoetryBookBuilder:
    def __init__(self, title, subtitle, author, era, theme_color=(0.15, 0.25, 0.45)):
        self.doc = pymupdf.open()
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.era = era
        self.theme_color = theme_color  # RGB tuple (0..1)
        self.secondary_color = (0.5, 0.4, 0.25)
        self.bg_light = (0.97, 0.97, 0.95)
        
        self.current_page = None
        self.current_y = MARGIN_T
        self.pages = []
        
    def _register_fonts(self, page):
        page.insert_font(fontname="VN", fontfile=FONT_VN_REG)
        page.insert_font(fontname="VNBold", fontfile=FONT_VN_BOLD)
        page.insert_font(fontname="VNItalic", fontfile=FONT_VN_ITALIC)
        page.insert_font(fontname="VNBI", fontfile=FONT_VN_BI)
        page.insert_font(fontname="ZH", fontfile=FONT_ZH)

    def new_content_page(self):
        page = self.doc.new_page(width=PAGE_W, height=PAGE_H)
        self._register_fonts(page)
        self.current_page = page
        self.current_y = MARGIN_T + 15
        
        # Draw header
        header_text = f"{self.author} — {self.title}"
        page.insert_text((MARGIN_L, MARGIN_T - 10), header_text, fontname="VNItalic", fontsize=9, color=(0.4, 0.4, 0.4))
        page.draw_line((MARGIN_L, MARGIN_T - 5), (PAGE_W - MARGIN_R, MARGIN_T - 5), color=(0.75, 0.75, 0.75), width=0.5)
        
        # Track pages for footer update later
        self.pages.append(page)
        return page

    def check_space(self, needed_height):
        if self.current_page is None or (self.current_y + needed_height > PAGE_H - MARGIN_B):
            self.new_content_page()

    def add_cover(self, description=None):
        page = self.doc.new_page(width=PAGE_W, height=PAGE_H)
        self._register_fonts(page)
        
        # Outer border
        outer_rect = pymupdf.Rect(28, 28, PAGE_W - 28, PAGE_H - 28)
        page.draw_rect(outer_rect, color=self.theme_color, width=2.0)
        
        # Inner decorative border
        inner_rect = pymupdf.Rect(34, 34, PAGE_W - 34, PAGE_H - 34)
        page.draw_rect(inner_rect, color=self.secondary_color, width=0.8)
        
        # Corner marks
        for x, y, dx, dy in [(38, 38, 15, 15), (PAGE_W - 38, 38, -15, 15),
                            (38, PAGE_H - 38, 15, -15), (PAGE_W - 38, PAGE_H - 38, -15, -15)]:
            page.draw_line((x, y), (x + dx, y), color=self.theme_color, width=1.2)
            page.draw_line((x, y), (x, y + dy), color=self.theme_color, width=1.2)
        
        # Badge Era
        badge_y = 110
        page.draw_rect(pymupdf.Rect(MARGIN_L + 40, badge_y - 18, PAGE_W - MARGIN_L - 40, badge_y + 10),
                       fill=self.theme_color, color=self.theme_color)
        page.insert_text((MARGIN_L + 60, badge_y - 2), self.era.upper(),
                         fontname="VNBold", fontsize=11, color=(1, 1, 1))
        
        # Book Title
        title_y = 200
        # Title can wrap
        title_rect = pymupdf.Rect(MARGIN_L + 15, title_y, PAGE_W - MARGIN_R - 15, title_y + 120)
        page.insert_textbox(title_rect, self.title, fontname="VNBold", fontsize=23, 
                            color=self.theme_color, align=pymupdf.TEXT_ALIGN_CENTER)
        
        # Decorative separator
        sep_y = title_y + 110
        page.draw_line((MARGIN_L + 80, sep_y), (PAGE_W - MARGIN_R - 80, sep_y), color=self.secondary_color, width=1.2)
        page.draw_circle((PAGE_W / 2, sep_y), 3.5, fill=self.secondary_color, color=self.secondary_color)
        
        # Subtitle
        if self.subtitle:
            sub_rect = pymupdf.Rect(MARGIN_L + 20, sep_y + 20, PAGE_W - MARGIN_R - 20, sep_y + 90)
            page.insert_textbox(sub_rect, self.subtitle, fontname="VNItalic", fontsize=13,
                                color=(0.25, 0.25, 0.25), align=pymupdf.TEXT_ALIGN_CENTER)
            
        # Author Name
        author_y = 480
        page.insert_textbox(pymupdf.Rect(MARGIN_L, author_y, PAGE_W - MARGIN_R, author_y + 25), "TÁC GIẢ",
                            fontname="VNBold", fontsize=11, color=self.secondary_color, align=pymupdf.TEXT_ALIGN_CENTER)
        page.insert_textbox(pymupdf.Rect(MARGIN_L, author_y + 25, PAGE_W - MARGIN_R, author_y + 70), self.author,
                            fontname="VNBold", fontsize=21, color=self.theme_color, align=pymupdf.TEXT_ALIGN_CENTER)
        
        # Description box
        if description:
            desc_rect = pymupdf.Rect(MARGIN_L + 30, 560, PAGE_W - MARGIN_R - 30, 710)
            page.draw_rect(desc_rect, fill=self.bg_light, color=(0.85, 0.85, 0.80), width=0.5)
            inner_desc = pymupdf.Rect(MARGIN_L + 40, 572, PAGE_W - MARGIN_R - 40, 700)
            page.insert_textbox(inner_desc, description, fontname="VN", fontsize=10.5,
                                color=(0.2, 0.2, 0.2), align=pymupdf.TEXT_ALIGN_LEFT)
        
        # Bottom Imprint
        imprint_y = 750
        page.insert_textbox(pymupdf.Rect(MARGIN_L, imprint_y, PAGE_W - MARGIN_R, imprint_y + 20),
                            "TỦ SÁCH TINH HOA THƠ CA & CỔ VĂN KINH ĐIỂN",
                            fontname="VNBold", fontsize=10, color=(0.35, 0.35, 0.35), align=pymupdf.TEXT_ALIGN_CENTER)
        page.insert_textbox(pymupdf.Rect(MARGIN_L, imprint_y + 20, PAGE_W - MARGIN_R, imprint_y + 40),
                            "Bản Số Hóa Chuẩn Xác — Thư Viện Lưu Trữ Quốc Gia",
                            fontname="VNItalic", fontsize=9, color=(0.5, 0.5, 0.5), align=pymupdf.TEXT_ALIGN_CENTER)

    def add_intro_section(self, section_title, content_text):
        self.new_content_page()
        
        # Section title
        self.current_page.draw_rect(pymupdf.Rect(MARGIN_L, self.current_y, PAGE_W - MARGIN_R, self.current_y + 30),
                                    fill=self.theme_color, color=self.theme_color)
        self.current_page.insert_text((MARGIN_L + 15, self.current_y + 20), section_title.upper(),
                                      fontname="VNBold", fontsize=13, color=(1, 1, 1))
        self.current_y += 45
        
        # Multi-paragraph body text
        paragraphs = content_text.strip().split("\n\n")
        for para in paragraphs:
            para = para.strip().replace("\n", " ")
            if not para:
                continue
            # Calculate height needed
            # Approx 75 chars per line at 11pt
            lines_est = max(1, len(para) // 70 + 1)
            para_h = lines_est * 16 + 12
            self.check_space(para_h)
            
            rect = pymupdf.Rect(MARGIN_L, self.current_y, PAGE_W - MARGIN_R, self.current_y + para_h)
            self.current_page.insert_textbox(rect, para, fontname="VN", fontsize=11,
                                            color=(0.15, 0.15, 0.15), align=pymupdf.TEXT_ALIGN_JUSTIFY)
            self.current_y += para_h + 4

    def add_classical_poem(self, poem_data):
        """
        poem_data: dict with:
          - title_vn: str
          - title_zh: str (optional)
          - category: str (e.g. 'Thất ngôn bát cú', 'Cổ thi', 'Tống Từ', etc.)
          - hanzi: list of str or multiline str
          - phien_am: list of str or multiline str
          - dich_nghia: list of str or multiline str
          - dich_tho: list of dict(translator, meter, text)
          - chu_giai: str (optional)
        """
        self.check_space(140)
        
        # Poem Header Box
        header_h = 32
        h_rect = pymupdf.Rect(MARGIN_L, self.current_y, PAGE_W - MARGIN_R, self.current_y + header_h)
        self.current_page.draw_rect(h_rect, fill=self.bg_light, color=self.secondary_color, width=0.8)
        
        title_str = poem_data.get('title_vn', '')
        if poem_data.get('title_zh'):
            title_str += f" ({poem_data.get('title_zh')})"
            
        self.current_page.insert_text((MARGIN_L + 12, self.current_y + 20), title_str,
                                      fontname="VNBold", fontsize=12.5, color=self.theme_color)
        
        cat_str = poem_data.get('category', '')
        if cat_str:
            self.current_page.insert_text((PAGE_W - MARGIN_R - 150, self.current_y + 20),
                                          cat_str, fontname="VNItalic", fontsize=9.5, color=(0.4, 0.4, 0.4))
        self.current_y += header_h + 12
        
        # 1. Hán tự & Phiên âm
        hanzi_lines = [l.strip() for l in poem_data.get('hanzi', '').strip().split('\n') if l.strip()]
        phien_am_lines = [l.strip() for l in poem_data.get('phien_am', '').strip().split('\n') if l.strip()]
        
        if hanzi_lines or phien_am_lines:
            # We can print side by side or sequential
            # Printing sequential gives maximum readability and room for full stanzas
            if hanzi_lines:
                self.check_space(len(hanzi_lines) * 19 + 25)
                self.current_page.insert_text((MARGIN_L + 10, self.current_y + 12), "【 NGUYÊN TÁC CHỮ HÁN 】",
                                              fontname="VNBold", fontsize=9, color=self.secondary_color)
                self.current_y += 20
                for hl in hanzi_lines:
                    self.check_space(20)
                    self.current_page.insert_text((MARGIN_L + 25, self.current_y + 12), hl,
                                                  fontname="ZH", fontsize=11.5, color=(0.1, 0.1, 0.1))
                    self.current_y += 18
                self.current_y += 8
                
            if phien_am_lines:
                self.check_space(len(phien_am_lines) * 17 + 25)
                self.current_page.insert_text((MARGIN_L + 10, self.current_y + 12), "【 PHIÊN ÂM HÁN - VIỆT 】",
                                              fontname="VNBold", fontsize=9, color=self.secondary_color)
                self.current_y += 20
                for pal in phien_am_lines:
                    self.check_space(18)
                    self.current_page.insert_text((MARGIN_L + 25, self.current_y + 12), pal,
                                                  fontname="VNBI", fontsize=10.5, color=(0.15, 0.15, 0.35))
                    self.current_y += 17
                self.current_y += 8
                
        # 2. Dịch nghĩa
        dich_nghia = poem_data.get('dich_nghia', '').strip()
        if dich_nghia:
            lines_est = max(1, len(dich_nghia) // 65 + 1)
            dn_h = lines_est * 15 + 28
            self.check_space(dn_h)
            self.current_page.insert_text((MARGIN_L + 10, self.current_y + 12), "【 DỊCH NGHĨA VĂN XUÔI 】",
                                          fontname="VNBold", fontsize=9, color=self.secondary_color)
            self.current_y += 20
            dn_rect = pymupdf.Rect(MARGIN_L + 20, self.current_y, PAGE_W - MARGIN_R - 20, self.current_y + dn_h)
            self.current_page.insert_textbox(dn_rect, dich_nghia, fontname="VN", fontsize=10,
                                            color=(0.25, 0.25, 0.25), align=pymupdf.TEXT_ALIGN_JUSTIFY)
            self.current_y += dn_h + 4
            
        # 3. Dịch thơ (các bản dịch của danh sĩ)
        dich_tho_list = poem_data.get('dich_tho', [])
        for dt in dich_tho_list:
            translator = dt.get('translator', 'Khuyết danh')
            meter = dt.get('meter', '')
            verses = [v.strip() for v in dt.get('text', '').strip().split('\n') if v.strip()]
            
            dt_h = len(verses) * 17 + 35
            self.check_space(dt_h)
            
            tag_text = f"【 BẢN DỊCH THƠ: {translator.upper()} ({meter}) 】" if meter else f"【 BẢN DỊCH THƠ: {translator.upper()} 】"
            self.current_page.insert_text((MARGIN_L + 10, self.current_y + 12), tag_text,
                                          fontname="VNBold", fontsize=9, color=self.theme_color)
            self.current_y += 20
            
            # Draw decorative quote bar
            bar_top = self.current_y
            for v in verses:
                self.check_space(18)
                self.current_page.insert_text((MARGIN_L + 30, self.current_y + 12), v,
                                              fontname="VNItalic", fontsize=10.5, color=(0.1, 0.1, 0.1))
                self.current_y += 17
            bar_bot = self.current_y
            self.current_page.draw_line((MARGIN_L + 18, bar_top), (MARGIN_L + 18, bar_bot),
                                        color=self.secondary_color, width=1.5)
            self.current_y += 8
            
        # 4. Chú giải điển tích & Lời bình
        chu_giai = poem_data.get('chu_giai', '').strip()
        if chu_giai:
            cg_lines = max(1, len(chu_giai) // 70 + 1)
            cg_h = cg_lines * 14 + 26
            self.check_space(cg_h)
            
            # Background box for commentary
            cg_box = pymupdf.Rect(MARGIN_L + 10, self.current_y, PAGE_W - MARGIN_R - 10, self.current_y + cg_h)
            self.current_page.draw_rect(cg_box, fill=(0.95, 0.96, 0.97), color=(0.8, 0.85, 0.9), width=0.5)
            
            self.current_page.insert_text((MARGIN_L + 18, self.current_y + 14), "CHÚ GIẢI & BỐI CẢNH:",
                                          fontname="VNBold", fontsize=8.5, color=self.theme_color)
            cg_rect = pymupdf.Rect(MARGIN_L + 18, self.current_y + 18, PAGE_W - MARGIN_R - 18, self.current_y + cg_h - 4)
            self.current_page.insert_textbox(cg_rect, chu_giai, fontname="VN", fontsize=9,
                                            color=(0.3, 0.3, 0.35), align=pymupdf.TEXT_ALIGN_JUSTIFY)
            self.current_y += cg_h + 12
            
        # Separator line between poems
        self.check_space(20)
        self.current_page.draw_line((MARGIN_L + 100, self.current_y + 6), (PAGE_W - MARGIN_R - 100, self.current_y + 6),
                                    color=(0.85, 0.85, 0.85), width=0.8)
        self.current_y += 18

    def add_modern_poem(self, poem_data):
        """
        poem_data: dict with:
          - title: str
          - subtitle / date: str
          - epigraph: str (optional)
          - stanzas: list of list of str (or list of stanzas)
          - notes / commentary: str (optional)
        """
        self.check_space(120)
        
        # Poem Title
        self.current_page.draw_rect(pymupdf.Rect(MARGIN_L, self.current_y, PAGE_W - MARGIN_R, self.current_y + 26),
                                    fill=self.bg_light, color=self.theme_color, width=0.8)
        self.current_page.insert_text((MARGIN_L + 12, self.current_y + 17), poem_data.get('title', '').upper(),
                                      fontname="VNBold", fontsize=11.5, color=self.theme_color)
        
        date_str = poem_data.get('date', '')
        if date_str:
            self.current_page.insert_text((PAGE_W - MARGIN_R - 120, self.current_y + 17),
                                          date_str, fontname="VNItalic", fontsize=9.5, color=(0.4, 0.4, 0.4))
        self.current_y += 36
        
        # Epigraph / Đề từ
        epigraph = poem_data.get('epigraph', '').strip()
        if epigraph:
            epi_h = 24
            self.check_space(epi_h)
            self.current_page.insert_text((MARGIN_L + 40, self.current_y + 12), f"« {epigraph} »",
                                          fontname="VNItalic", fontsize=9.5, color=(0.35, 0.35, 0.35))
            self.current_y += epi_h + 6
            
        # Stanzas
        stanzas = poem_data.get('stanzas', [])
        for stanza in stanzas:
            lines = [l.strip() for l in stanza if l.strip()]
            stanza_h = len(lines) * 17 + 10
            self.check_space(stanza_h)
            for line in lines:
                self.current_page.insert_text((MARGIN_L + 35, self.current_y + 12), line,
                                              fontname="VN", fontsize=10.5, color=(0.1, 0.1, 0.1))
                self.current_y += 17
            self.current_y += 8
            
        # Commentary / Notes
        commentary = poem_data.get('notes', '').strip()
        if commentary:
            c_lines = max(1, len(commentary) // 70 + 1)
            c_h = c_lines * 14 + 20
            self.check_space(c_h)
            
            box = pymupdf.Rect(MARGIN_L + 15, self.current_y, PAGE_W - MARGIN_R - 15, self.current_y + c_h)
            self.current_page.draw_rect(box, fill=self.bg_light, color=(0.85, 0.85, 0.85), width=0.5)
            self.current_page.insert_text((MARGIN_L + 25, self.current_y + 12), "BÌNH CHÚ & VĂN BẢN:",
                                          fontname="VNBold", fontsize=8.5, color=self.secondary_color)
            c_rect = pymupdf.Rect(MARGIN_L + 25, self.current_y + 15, PAGE_W - MARGIN_R - 25, self.current_y + c_h - 4)
            self.current_page.insert_textbox(c_rect, commentary, fontname="VNItalic", fontsize=9,
                                            color=(0.3, 0.3, 0.3), align=pymupdf.TEXT_ALIGN_JUSTIFY)
            self.current_y += c_h + 10
            
        # Divider
        self.check_space(18)
        self.current_page.draw_line((MARGIN_L + 120, self.current_y + 4), (PAGE_W - MARGIN_R - 120, self.current_y + 4),
                                    color=(0.88, 0.88, 0.88), width=0.6)
        self.current_y += 15

    def finalize_and_save(self, output_path):
        # Add footers with page numbers to all content pages
        total_pages = len(self.doc)
        for i in range(1, total_pages):  # skip cover (page 0)
            page = self.doc[i]
            page_no_text = f"Trang {i} / {total_pages - 1}"
            footer_text = f"Tủ Sách Thơ Ca & Cổ Văn — {self.author}"
            
            page.draw_line((MARGIN_L, PAGE_H - MARGIN_B + 10), (PAGE_W - MARGIN_R, PAGE_H - MARGIN_B + 10),
                           color=(0.8, 0.8, 0.8), width=0.5)
            page.insert_text((MARGIN_L, PAGE_H - MARGIN_B + 22), footer_text,
                             fontname="VNItalic", fontsize=8.5, color=(0.5, 0.5, 0.5))
            page.insert_text((PAGE_W - MARGIN_R - 60, PAGE_H - MARGIN_B + 22), page_no_text,
                             fontname="VN", fontsize=8.5, color=(0.4, 0.4, 0.4))
            
        # Ensure target dir exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.doc.save(output_path, deflate=True)
        self.doc.close()
        return total_pages
