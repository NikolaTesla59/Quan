# -*- coding: utf-8 -*-
"""
NEU Master Textbook Builder Engine (Version 2 - TextWriter TrueType UTF-8)
Designed for National Economics University (NEU) Full Scholarly Textbooks
Undergraduate, Master (ThS) and Doctoral (Tiến sĩ) Levels.
Using PyMuPDF TextWriter with Times New Roman system fonts.
"""
import os
import pymupdf

FONT_REG_PATH = r"C:\Windows\Fonts\times.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\timesbd.ttf"
FONT_ITALIC_PATH = r"C:\Windows\Fonts\timesi.ttf"
FONT_BOLD_ITALIC_PATH = r"C:\Windows\Fonts\timesbi.ttf"

class NEUTextbookBuilder:
    def __init__(self, title, subject_code, faculty, authors, level_text="HỆ ĐẠI HỌC CHÍNH QUY & SAU ĐẠI HỌC (THẠC SĨ - TIẾN SĨ)", edition="TÁI BẢN & BỔ SUNG CHUYÊN SÂU LÝ THUYẾT & THỰC NGHIỆM"):
        self.title = title
        self.subject_code = subject_code
        self.faculty = faculty
        self.authors = authors
        self.level_text = level_text
        self.edition = edition
        
        self.doc = pymupdf.open()
        self.page_w, self.page_h = 595, 842 # A4
        self.margin_l, self.margin_r = 54, 541 # width = 487
        self.margin_t, self.margin_b = 60, 782 # height = 722
        self.content_w = self.margin_r - self.margin_l
        
        self.font_reg = pymupdf.Font(fontfile=FONT_REG_PATH)
        self.font_bold = pymupdf.Font(fontfile=FONT_BOLD_PATH)
        self.font_italic = pymupdf.Font(fontfile=FONT_ITALIC_PATH)
        
        self.curr_page = None
        self.curr_tw = None
        self.y_pos = self.margin_t
        self.page_num = 1
        
    def _add_center(self, tw, y, text, font_obj, fontsize):
        w = font_obj.text_length(text, fontsize=fontsize)
        x = max(self.margin_l, (self.page_w - w) / 2)
        tw.append(pymupdf.Point(x, y), text, font=font_obj, fontsize=fontsize)

    def _wrap_line(self, text, max_w, font_obj, fontsize):
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

    def _flush_page(self):
        if self.curr_page is not None and self.curr_tw is not None:
            self.curr_tw.write_text(self.curr_page, color=(0.12, 0.12, 0.12))
            self.curr_tw = None

    def _new_content_page(self, running_header=None):
        self._flush_page()
        
        self.curr_page = self.doc.new_page(width=self.page_w, height=self.page_h)
        self.curr_tw = pymupdf.TextWriter(pymupdf.Rect(0, 0, self.page_w, self.page_h))
        
        # Header text & line
        h_text = running_header or f"TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN  •  {self.title.upper()}"
        if len(h_text) > 80:
            h_text = h_text[:77] + "..."
        self.curr_tw.append(pymupdf.Point(self.margin_l, 44), h_text, font=self.font_bold, fontsize=7.5)
        self.curr_page.draw_line(pymupdf.Point(self.margin_l, 48), pymupdf.Point(self.margin_r, 48), color=(0.7, 0.2, 0.2), width=0.6)
        
        # Footer
        p_text = f"- {self.page_num} -"
        w = self.font_reg.text_length(p_text, fontsize=9)
        self.curr_tw.append(pymupdf.Point((self.page_w - w)/2, self.page_h - 36), p_text, font=self.font_reg, fontsize=9)
        self.curr_page.draw_line(pymupdf.Point(self.margin_l, self.page_h - 48), pymupdf.Point(self.margin_r, self.page_h - 48), color=(0.85, 0.85, 0.85), width=0.5)
        
        self.y_pos = self.margin_t + 10
        self.page_num += 1
        return self.curr_page

    def build_cover(self):
        cover = self.doc.new_page(width=self.page_w, height=self.page_h)
        tw_cover = pymupdf.TextWriter(pymupdf.Rect(0, 0, self.page_w, self.page_h))
        
        # Decorative frames (NEU Navy & Gold-Crimson)
        rect_outer = pymupdf.Rect(32, 32, self.page_w - 32, self.page_h - 32)
        cover.draw_rect(rect_outer, color=(0.08, 0.25, 0.5), width=2.5) # NEU Blue
        rect_inner = pymupdf.Rect(36, 36, self.page_w - 36, self.page_h - 36)
        cover.draw_rect(rect_inner, color=(0.8, 0.6, 0.2), width=0.8) # Gold
        
        # NEU Heading
        self._add_center(tw_cover, 110, "BỘ GIÁO DỤC VÀ ĐÀO TẠO", self.font_bold, 11.5)
        self._add_center(tw_cover, 130, "TRƯỜNG ĐẠI HỌC KINH TẾ QUỐC DÂN", self.font_bold, 14)
        self._add_center(tw_cover, 150, f"KHOA / VIỆN: {self.faculty.upper()}", self.font_bold, 10.5)
        cover.draw_line(pymupdf.Point(self.page_w/2 - 50, 162), pymupdf.Point(self.page_w/2 + 50, 162), color=(0.8, 0.6, 0.2), width=1.2)
        
        # Textbook Title
        self._add_center(tw_cover, 260, "GIÁO TRÌNH", self.font_bold, 16)
        
        title_lines = self._wrap_line(self.title.upper(), self.content_w - 20, self.font_bold, 22)
        y_curr = 300
        for tl in title_lines:
            self._add_center(tw_cover, y_curr, tl, self.font_bold, 22)
            y_curr += 28
            
        cover.draw_line(pymupdf.Point(self.page_w/2 - 70, y_curr + 5), pymupdf.Point(self.page_w/2 + 70, y_curr + 5), color=(0.6, 0.1, 0.1), width=1.5)
        
        # Subject code & Level
        self._add_center(tw_cover, y_curr + 35, f"MÃ HỌC PHẦN: {self.subject_code}  •  QUY MÔ: 3 TÍN CHỈ", self.font_bold, 11)
        self._add_center(tw_cover, y_curr + 60, self.level_text, self.font_bold, 10.5)
        self._add_center(tw_cover, y_curr + 82, f"({self.edition})", self.font_italic, 9.5)
        
        # Authors
        self._add_center(tw_cover, 570, "CHỦ BIÊN & TẬP THỂ TÁC GIẢ:", self.font_bold, 10.5)
        author_lines = self._wrap_line(self.authors, self.content_w - 40, self.font_bold, 12)
        y_a = 590
        for al in author_lines:
            self._add_center(tw_cover, y_a, al, self.font_bold, 12)
            y_a += 17
            
        # Publisher
        self._add_center(tw_cover, 740, "NHÀ XUẤT BẢN ĐẠI HỌC KINH TẾ QUỐC DÂN", self.font_bold, 11.5)
        self._add_center(tw_cover, 760, "HÀ NỘI — 2026", self.font_bold, 10)
        
        tw_cover.write_text(cover, color=(0.08, 0.15, 0.35))

    def add_table_of_contents(self, toc_data):
        self._new_content_page(running_header="MỤC LỤC TỔNG THỂ GIÁO TRÌNH")
        self._add_center(self.curr_tw, self.y_pos + 12, "MỤC LỤC NỘI DUNG TOÀN VĂN", self.font_bold, 15)
        self.y_pos += 40
        self.curr_page.draw_line(pymupdf.Point(self.margin_l, self.y_pos - 10), pymupdf.Point(self.margin_r, self.y_pos - 10), color=(0.8, 0.6, 0.2), width=1)
        
        for item in toc_data:
            num = item.get("chapter_num", "")
            title = item.get("chapter_title", "")
            topics = item.get("topics", [])
            
            c_header = f"CHƯƠNG {num}: {title.upper()}"
            lines = self._wrap_line(c_header, self.content_w - 20, self.font_bold, 10.5)
            if self.y_pos + len(lines) * 15 + len(topics) * 12 > self.margin_b:
                self._new_content_page(running_header="MỤC LỤC TỔNG THỂ GIÁO TRÌNH")
            
            for l in lines:
                self.curr_tw.append(pymupdf.Point(self.margin_l + 5, self.y_pos), l, font=self.font_bold, fontsize=10.5)
                self.y_pos += 15
                
            for top in topics:
                t_lines = self._wrap_line(f"• {top}", self.content_w - 30, self.font_reg, 9)
                for tl in t_lines:
                    if self.y_pos + 12 > self.margin_b:
                        self._new_content_page(running_header="MỤC LỤC TỔNG THỂ GIÁO TRÌNH")
                    self.curr_tw.append(pymupdf.Point(self.margin_l + 20, self.y_pos), tl, font=self.font_reg, fontsize=9)
                    self.y_pos += 12
            self.y_pos += 6

    def add_chapter(self, chap_num, chap_title, introduction, sections, advanced_phd_seminar, review_questions):
        self._new_content_page()
        
        # Chapter Banner
        banner_rect = pymupdf.Rect(self.margin_l, self.y_pos, self.margin_r, self.y_pos + 48)
        self.curr_page.draw_rect(banner_rect, color=(0.08, 0.25, 0.5), fill=(0.95, 0.97, 1.0), width=1)
        
        c_title_num = f"CHƯƠNG {chap_num}"
        self._add_center(self.curr_tw, self.y_pos + 18, c_title_num, self.font_bold, 11)
        
        title_lines = self._wrap_line(chap_title.upper(), self.content_w - 30, self.font_bold, 12.5)
        y_t = self.y_pos + 35
        for tl in title_lines:
            self._add_center(self.curr_tw, y_t, tl, self.font_bold, 12.5)
            y_t += 16
            
        self.y_pos = max(banner_rect.y1 + 18, y_t + 6)
        
        # Introduction
        intro_lines = self._wrap_line(introduction, self.content_w, self.font_italic, 9.5)
        for il in intro_lines:
            if self.y_pos + 13 > self.margin_b:
                self._new_content_page()
            self.curr_tw.append(pymupdf.Point(self.margin_l, self.y_pos), il, font=self.font_italic, fontsize=9.5)
            self.y_pos += 13
        self.y_pos += 10
        self.curr_page.draw_line(pymupdf.Point(self.margin_l, self.y_pos - 4), pymupdf.Point(self.margin_r, self.y_pos - 4), color=(0.85, 0.85, 0.85), width=0.5)
        
        # Sections
        for sec in sections:
            sec_num = sec.get("sec_num", "")
            sec_title = sec.get("sec_title", "")
            sec_text = sec.get("content", "")
            formulas = sec.get("formulas", [])
            case_studies = sec.get("case_studies", [])
            
            # Section Header
            s_head = f"{chap_num}.{sec_num}. {sec_title}"
            s_head_lines = self._wrap_line(s_head, self.content_w, self.font_bold, 11)
            if self.y_pos + len(s_head_lines)*16 + 40 > self.margin_b:
                self._new_content_page()
                
            self.y_pos += 8
            for sh in s_head_lines:
                self.curr_tw.append(pymupdf.Point(self.margin_l, self.y_pos), sh, font=self.font_bold, fontsize=11)
                self.y_pos += 16
            self.y_pos += 4
            
            # Content paragraphs
            if isinstance(sec_text, str):
                paras = sec_text.split("\n\n")
            else:
                paras = sec_text
                
            for p in paras:
                p = p.strip()
                if not p:
                    continue
                wrapped = self._wrap_line(p, self.content_w - 12, self.font_reg, 9.5)
                first = True
                for wl in wrapped:
                    if self.y_pos + 13.5 > self.margin_b:
                        self._new_content_page()
                    x = self.margin_l + 16 if first else self.margin_l
                    self.curr_tw.append(pymupdf.Point(x, self.y_pos), wl, font=self.font_reg, fontsize=9.5)
                    self.y_pos += 13.5
                    first = False
                self.y_pos += 5
                
            # Key formulas / Models Box
            if formulas:
                if self.y_pos + len(formulas)*16 + 25 > self.margin_b:
                    self._new_content_page()
                box_h = len(formulas)*16 + 18
                box_rect = pymupdf.Rect(self.margin_l + 10, self.y_pos, self.margin_r - 10, self.y_pos + box_h)
                self.curr_page.draw_rect(box_rect, color=(0.6, 0.1, 0.1), fill=(0.99, 0.96, 0.96), width=0.8)
                self.curr_tw.append(pymupdf.Point(box_rect.x0 + 8, self.y_pos + 12), "[MÔ HÌNH TOÁN KINH TẾ & CÔNG THỨC ĐỊNH LƯỢNG CHUẨN]:", font=self.font_bold, fontsize=8.5)
                fy = self.y_pos + 26
                for f_item in formulas:
                    self.curr_tw.append(pymupdf.Point(box_rect.x0 + 15, fy), f"• {f_item}", font=self.font_bold, fontsize=9)
                    fy += 15
                self.y_pos = box_rect.y1 + 10
                
            # Case studies
            if case_studies:
                for c in case_studies:
                    c_title = c.get("title", "Tình huống thực tiễn")
                    c_desc = c.get("detail", "")
                    cd_lines = self._wrap_line(f"▶ {c_title}: {c_desc}", self.content_w - 24, self.font_reg, 9)
                    if self.y_pos + len(cd_lines)*13 + 15 > self.margin_b:
                        self._new_content_page()
                    self.y_pos += 4
                    for cl in cd_lines:
                        self.curr_tw.append(pymupdf.Point(self.margin_l + 10, self.y_pos), cl, font=self.font_reg, fontsize=9)
                        self.y_pos += 13
                    self.y_pos += 4

        # Advanced PhD / Master Seminar Module ("Cả tiến sĩ nữa")
        if advanced_phd_seminar:
            if self.y_pos + 100 > self.margin_b:
                self._new_content_page()
            self.y_pos += 12
            self.curr_page.draw_line(pymupdf.Point(self.margin_l, self.y_pos), pymupdf.Point(self.margin_r, self.y_pos), color=(0.08, 0.25, 0.5), width=1.2)
            self.y_pos += 16
            self.curr_tw.append(pymupdf.Point(self.margin_l, self.y_pos), "◆ CHUYÊN ĐỀ NGHIÊN CỨU SAU ĐẠI HỌC & TIẾN SĨ (DOCTORAL RESEARCH SEMINAR):", font=self.font_bold, fontsize=10.5)
            self.y_pos += 16
            
            phd_paras = advanced_phd_seminar.get("topics", [])
            for pt in phd_paras:
                pt_lines = self._wrap_line(f"★ {pt}", self.content_w - 15, self.font_italic, 9)
                for ptl in pt_lines:
                    if self.y_pos + 13 > self.margin_b:
                        self._new_content_page()
                    self.curr_tw.append(pymupdf.Point(self.margin_l + 10, self.y_pos), ptl, font=self.font_italic, fontsize=9)
                    self.y_pos += 13
                self.y_pos += 3
            self.y_pos += 8

        # Review Questions
        if review_questions:
            if self.y_pos + 80 > self.margin_b:
                self._new_content_page()
            self.y_pos += 10
            self.curr_tw.append(pymupdf.Point(self.margin_l, self.y_pos), f"CÂU HỎI ÔN TẬP & THẢO LUẬN HỌC PHẦN (CHƯƠNG {chap_num}):", font=self.font_bold, fontsize=10)
            self.y_pos += 15
            for q_idx, q in enumerate(review_questions, 1):
                q_lines = self._wrap_line(f"{q_idx}. {q}", self.content_w - 15, self.font_reg, 9)
                for ql in q_lines:
                    if self.y_pos + 12 > self.margin_b:
                        self._new_content_page()
                    self.curr_tw.append(pymupdf.Point(self.margin_l + 10, self.y_pos), ql, font=self.font_reg, fontsize=9)
                    self.y_pos += 12
                self.y_pos += 2
            self.y_pos += 12

    def save(self, output_pdf_path):
        self._flush_page()
        abs_path = os.path.abspath(output_pdf_path)
        if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
            abs_path = '\\\\?\\' + abs_path
        dirname = os.path.dirname(abs_path)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        self.doc.save(abs_path)
        self.doc.close()
        size_mb = os.path.getsize(abs_path) / (1024 * 1024)
        doc_c = pymupdf.open(abs_path)
        pages = len(doc_c)
        doc_c.close()
        return pages, size_mb
