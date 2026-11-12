# -*- coding: utf-8 -*-
"""
Builder for: [Bản Dịch Tiếng Việt] Louis Bonnafont - Muôn Hạng Dân Bắc Kỳ (Types Tonkinois 1903)
Extracts original illustrations from BONNAFONT-Louis-Types-tonkinois.pdf
Compiles complete Vietnamese translations, scholarly notes, and 75-character index.
"""
import os
import pymupdf

FONT_REG = r"C:\Windows\Fonts\times.ttf"
FONT_BOLD = r"C:\Windows\Fonts\timesbd.ttf"
FONT_ITALIC = r"C:\Windows\Fonts\timesi.ttf"
FONT_BOLD_ITALIC = r"C:\Windows\Fonts\timesbi.ttf"

class BookBuilder:
    def __init__(self, title, subtitle):
        self.doc = pymupdf.open()
        self.page_w, self.page_h = 595, 842 # A4
        self.margin_l, self.margin_r = 54, 541
        self.margin_t, self.margin_b = 54, 788
        self.content_w = self.margin_r - self.margin_l
        
        self.font_reg = pymupdf.Font(fontfile=FONT_REG)
        self.font_bold = pymupdf.Font(fontfile=FONT_BOLD)
        self.font_italic = pymupdf.Font(fontfile=FONT_ITALIC)
        self.font_bi = pymupdf.Font(fontfile=FONT_BOLD_ITALIC)
        
        self.title = title
        self.subtitle = subtitle
        self.page_num = 1
        self.curr_page = None
        self.curr_tw = None
        self.y_pos = self.margin_t

    def _flush_page(self):
        if self.curr_page is not None and self.curr_tw is not None:
            self.curr_tw.write_text(self.curr_page, color=(0.12, 0.12, 0.12))
            self.curr_tw = None

    def new_page(self, running_header=None):
        self._flush_page()
        self.curr_page = self.doc.new_page(width=self.page_w, height=self.page_h)
        self.curr_tw = pymupdf.TextWriter(pymupdf.Rect(0, 0, self.page_w, self.page_h))
        
        # Border frame (warm colonial vintage)
        self.curr_page.draw_rect(pymupdf.Rect(30, 30, self.page_w - 30, self.page_h - 30), color=(0.55, 0.25, 0.15), width=0.8)
        self.curr_page.draw_rect(pymupdf.Rect(33, 33, self.page_w - 33, self.page_h - 33), color=(0.8, 0.65, 0.35), width=0.4)
        
        # Header
        h_text = running_header or f"LOUIS BONNAFONT  •  {self.title.upper()} (HÀ NỘI 1903)"
        if len(h_text) > 85:
            h_text = h_text[:82] + "..."
        w_h = self.font_italic.text_length(h_text, fontsize=8)
        self.curr_tw.append(pymupdf.Point((self.page_w - w_h)/2, 44), h_text, font=self.font_italic, fontsize=8)
        self.curr_page.draw_line(pymupdf.Point(self.margin_l, 48), pymupdf.Point(self.margin_r, 48), color=(0.7, 0.3, 0.2), width=0.5)
        
        # Footer
        p_text = f"- {self.page_num} -"
        w_p = self.font_reg.text_length(p_text, fontsize=9)
        self.curr_tw.append(pymupdf.Point((self.page_w - w_p)/2, self.page_h - 38), p_text, font=self.font_reg, fontsize=9)
        self.curr_page.draw_line(pymupdf.Point(self.margin_l, self.page_h - 48), pymupdf.Point(self.margin_r, self.page_h - 48), color=(0.85, 0.85, 0.85), width=0.4)
        
        self.y_pos = self.margin_t + 10
        self.page_num += 1
        return self.curr_page

    def _wrap(self, text, max_w, font_obj, fontsize):
        words = text.split()
        lines = []
        curr = []
        for w in words:
            cand = ' '.join(curr + [w])
            if font_obj.text_length(cand, fontsize=fontsize) <= max_w:
                curr.append(w)
            else:
                if curr:
                    lines.append(' '.join(curr))
                curr = [w]
        if curr:
            lines.append(' '.join(curr))
        return lines

    def add_center(self, y, text, font_obj, fontsize, color=(0.1, 0.1, 0.1)):
        w = font_obj.text_length(text, fontsize=fontsize)
        x = max(self.margin_l, (self.page_w - w) / 2)
        self.curr_tw.append(pymupdf.Point(x, y), text, font=font_obj, fontsize=fontsize)

    def add_text_block(self, text, font_obj, fontsize, line_height=14, indent=0, space_after=8, color=None):
        paras = text.split('\n')
        for p in paras:
            p = p.strip()
            if not p:
                self.y_pos += space_after / 2
                continue
            lines = self._wrap(p, self.content_w - indent, font_obj, fontsize)
            for idx, l in enumerate(lines):
                if self.y_pos + line_height > self.margin_b:
                    self.new_page()
                x = self.margin_l + (indent if idx == 0 else indent)
                self.curr_tw.append(pymupdf.Point(x, self.y_pos), l, font=font_obj, fontsize=fontsize)
                self.y_pos += line_height
            self.y_pos += space_after

    def build_cover(self, cover_img_path):
        cover = self.doc.new_page(width=self.page_w, height=self.page_h)
        tw = pymupdf.TextWriter(pymupdf.Rect(0, 0, self.page_w, self.page_h))
        
        # Ornate borders
        cover.draw_rect(pymupdf.Rect(25, 25, self.page_w - 25, self.page_h - 25), color=(0.45, 0.15, 0.1), width=2.5)
        cover.draw_rect(pymupdf.Rect(29, 29, self.page_w - 29, self.page_h - 29), color=(0.85, 0.7, 0.35), width=1.0)
        cover.draw_rect(pymupdf.Rect(33, 33, self.page_w - 33, self.page_h - 33), color=(0.45, 0.15, 0.1), width=0.5)
        
        # Author
        w_a = self.font_bold.text_length("LOUIS BONNAFONT", fontsize=15)
        tw.append(pymupdf.Point((self.page_w - w_a)/2, 85), "LOUIS BONNAFONT", font=self.font_bold, fontsize=15)
        
        # French original title
        w_fr = self.font_italic.text_length("(TYPES TONKINOIS — HANOI 1903)", fontsize=11)
        tw.append(pymupdf.Point((self.page_w - w_fr)/2, 108), "(TYPES TONKINOIS — HANOI 1903)", font=self.font_italic, fontsize=11)
        
        cover.draw_line(pymupdf.Point(self.page_w/2 - 60, 120), pymupdf.Point(self.page_w/2 + 60, 120), color=(0.7, 0.2, 0.1), width=1.2)
        
        # Main Vietnamese Title
        w_t1 = self.font_bold.text_length("MUÔN HẠNG DÂN BẮC KỲ", fontsize=24)
        tw.append(pymupdf.Point((self.page_w - w_t1)/2, 160), "MUÔN HẠNG DÂN BẮC KỲ", font=self.font_bold, fontsize=24)
        
        # Subtitle
        w_sub = self.font_italic.text_length("Bản Dịch Toàn Văn, Khảo Luận Lịch Sử & Toàn Bộ Tranh Minh Họa Gốc", fontsize=11.5)
        tw.append(pymupdf.Point((self.page_w - w_sub)/2, 185), "Bản Dịch Toàn Văn, Khảo Luận Lịch Sử & Toàn Bộ Tranh Minh Họa Gốc", font=self.font_italic, fontsize=11.5)
        
        # Cover illustration image
        if os.path.exists(cover_img_path):
            img_rect = pymupdf.Rect(self.page_w/2 - 130, 210, self.page_w/2 + 130, 590)
            cover.insert_image(img_rect, filename=cover_img_path)
            cover.draw_rect(img_rect, color=(0.6, 0.4, 0.2), width=0.8)
        
        # Publisher & metadata
        w_il = self.font_bold.text_length("TRANH MINH HỌA NGUYÊN BẢN: E. RONJAT & CÉZARD", fontsize=9.5)
        tw.append(pymupdf.Point((self.page_w - w_il)/2, 630), "TRANH MINH HỌA NGUYÊN BẢN: E. RONJAT & CÉZARD", font=self.font_bold, fontsize=9.5)
        
        w_pub1 = self.font_bold.text_length("NHÀ IN F.-H. SCHNEIDER, HÀ NỘI — 1903", fontsize=11)
        tw.append(pymupdf.Point((self.page_w - w_pub1)/2, 740), "NHÀ IN F.-H. SCHNEIDER, HÀ NỘI — 1903", font=self.font_bold, fontsize=11)
        
        w_pub2 = self.font_reg.text_length("ẤN BẢN KHẢO CỨU VIỆT NGỮ ĐẦY ĐỦ — NĂM 2026", fontsize=10)
        tw.append(pymupdf.Point((self.page_w - w_pub2)/2, 760), "ẤN BẢN KHẢO CỨU VIỆT NGỮ ĐẦY ĐỦ — NĂM 2026", font=self.font_reg, fontsize=10)
        
        tw.write_text(cover, color=(0.1, 0.1, 0.1))

    def save(self, output_path):
        self._flush_page()
        abs_p = os.path.abspath(output_path)
        if os.name == 'nt' and not abs_p.startswith('\\\\?\\'):
            abs_p = '\\\\?\\' + abs_p
        os.makedirs(os.path.dirname(abs_p), exist_ok=True)
        self.doc.save(abs_p)
        self.doc.close()
        sz = os.path.getsize(abs_p) / (1024 * 1024)
        c = pymupdf.open(abs_p)
        p = len(c)
        c.close()
        return p, sz

print("BookBuilder class ready.")
