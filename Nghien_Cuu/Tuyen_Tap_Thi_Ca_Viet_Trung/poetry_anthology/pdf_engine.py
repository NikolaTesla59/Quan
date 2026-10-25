# -*- coding: utf-8 -*-
"""
High-End Classical Poetry & Literature PDF Engine
Utilizes Playwright Chromium to render publication-grade books with ornate typography,
running headers/footers, Han/Nom font support, and elegant page layout.
"""

import asyncio
import os
from playwright.async_api import async_playwright

BASE_CSS = """
@page {
    size: A4;
    margin: 22mm 18mm 22mm 18mm;
    @top-center {
        content: "";
    }
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    font-family: 'Times New Roman', 'Palatino Linotype', 'Georgia', 'KaiTi', 'SimSun', serif;
    font-size: 11.5pt;
    line-height: 1.65;
    color: #1a1a1a;
    background-color: #ffffff;
}

/* Page breaks */
.page-break {
    page-break-before: always;
}

.avoid-break {
    page-break-inside: avoid;
}

/* Ornaments & Rules */
.ornament {
    text-align: center;
    color: #8B1E1E;
    font-size: 14pt;
    margin: 15px 0;
    letter-spacing: 5px;
}

.gold-line {
    height: 1.5px;
    background: linear-gradient(90deg, transparent, #b8860b, #8B1E1E, #b8860b, transparent);
    margin: 20px auto;
    width: 80%;
}

.thin-line {
    border: none;
    border-top: 0.5px solid #d3c4a5;
    margin: 15px 0;
}

/* Book Cover */
.cover-page {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    text-align: center;
    padding: 40px 20px;
    page-break-after: always;
    border: 3px double #8B1E1E;
    box-shadow: inset 0 0 0 8px #fbf8f2, inset 0 0 0 10px #c59b27;
    background: radial-gradient(circle at center, #ffffff 0%, #faf6ee 100%);
}

.cover-header {
    margin-top: 30px;
}

.cover-collection {
    font-size: 12pt;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #8B1E1E;
    font-weight: bold;
    margin-bottom: 8px;
}

.cover-era {
    font-size: 11pt;
    letter-spacing: 2px;
    color: #555555;
    font-style: italic;
}

.cover-body {
    margin: auto 0;
}

.cover-title {
    font-size: 26pt;
    font-weight: bold;
    color: #6a1010;
    line-height: 1.3;
    margin: 15px 0;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.cover-subtitle {
    font-size: 14pt;
    color: #2c3e50;
    line-height: 1.5;
    margin-bottom: 20px;
    max-width: 650px;
    font-style: italic;
}

.cover-author {
    font-size: 16pt;
    font-weight: bold;
    color: #1a1a1a;
    letter-spacing: 2px;
    margin-top: 25px;
}

.cover-author-sub {
    font-size: 11pt;
    color: #666;
    margin-top: 5px;
}

.cover-footer {
    margin-bottom: 25px;
    font-size: 10.5pt;
    color: #666666;
    line-height: 1.6;
}

.seal-box {
    display: inline-block;
    border: 2px solid #8B1E1E;
    color: #8B1E1E;
    padding: 4px 14px;
    font-weight: bold;
    letter-spacing: 2px;
    font-size: 10.5pt;
    margin-top: 15px;
    text-transform: uppercase;
}

/* Headings */
h1.chapter-title {
    color: #721616;
    font-size: 18pt;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 20px;
    margin-bottom: 10px;
    border-bottom: 1px solid #721616;
    padding-bottom: 8px;
}

h2.section-title {
    color: #1a365d;
    font-size: 14pt;
    margin-top: 20px;
    margin-bottom: 10px;
    border-left: 4px solid #8B1E1E;
    padding-left: 10px;
}

h3.poem-title {
    color: #721616;
    font-size: 13pt;
    margin-top: 25px;
    margin-bottom: 6px;
    text-align: center;
}

.poem-chinese-title {
    font-family: 'KaiTi', 'SimSun', 'STKaiti', serif;
    font-size: 14pt;
    color: #555;
    text-align: center;
    margin-bottom: 12px;
    letter-spacing: 2px;
}

/* Introduction Essay */
.intro-box {
    background-color: #faf7f2;
    border: 1px solid #e2d7c5;
    border-left: 4px solid #8B1E1E;
    padding: 18px 22px;
    margin: 20px 0;
    border-radius: 2px;
    font-size: 11pt;
    text-align: justify;
}

.intro-box p {
    margin-top: 0;
    margin-bottom: 10px;
    text-indent: 20px;
}

/* Poetry Stanzas */
.poem-container {
    margin: 20px 0 30px 0;
    padding: 15px 20px;
    background: #fffdf9;
    border: 1px solid #efe8da;
    border-radius: 4px;
}

.poem-stanza {
    margin: 12px 0;
    text-align: center;
    line-height: 1.8;
}

.poem-parallel {
    display: flex;
    justify-content: space-between;
    gap: 15px;
    margin: 15px 0;
}

.poem-col {
    flex: 1;
    padding: 10px;
    border: 1px solid #eee;
    background: #fafafa;
    border-radius: 3px;
}

.col-header {
    font-weight: bold;
    color: #721616;
    text-align: center;
    border-bottom: 1px solid #ddd;
    padding-bottom: 4px;
    margin-bottom: 8px;
    font-size: 10.5pt;
    text-transform: uppercase;
}

.han-script {
    font-family: 'KaiTi', 'SimSun', 'STKaiti', serif;
    font-size: 12.5pt;
    line-height: 1.8;
    color: #222;
}

.phien-am {
    font-style: italic;
    color: #2d3748;
    line-height: 1.7;
    font-size: 11pt;
}

.dich-nghia {
    font-size: 10.5pt;
    color: #4a5568;
    line-height: 1.6;
    text-align: justify;
}

.dich-tho {
    color: #1a365d;
    font-weight: 500;
    line-height: 1.75;
    font-size: 11.5pt;
}

.author-credit {
    font-size: 9.5pt;
    color: #718096;
    text-align: right;
    font-style: italic;
    margin-top: 6px;
}

/* Annotation & Analysis */
.commentary-box {
    margin-top: 12px;
    padding: 10px 14px;
    background: #f7f9fa;
    border-left: 3px solid #2b6cb0;
    font-size: 10pt;
    color: #333;
    line-height: 1.55;
    border-radius: 2px;
}

.commentary-title {
    font-weight: bold;
    color: #2b6cb0;
    margin-bottom: 4px;
    text-transform: uppercase;
    font-size: 9pt;
    letter-spacing: 1px;
}

/* Table of Contents */
.toc-list {
    list-style-type: none;
    padding-left: 0;
    margin: 20px 0;
}

.toc-item {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 5px 0;
    border-bottom: 1px dotted #ccc;
    font-size: 11pt;
}

.toc-title {
    font-weight: 500;
}

.toc-page {
    font-style: italic;
    color: #666;
}
"""

HEADER_TEMPLATE = """
<div style="width: 100%; font-size: 8.5pt; font-family: 'Times New Roman', serif; color: #777; border-bottom: 0.5px solid #bbb; padding-bottom: 3px; margin: 0 18mm; display: flex; justify-content: space-between;">
    <span style="text-transform: uppercase; letter-spacing: 1px;">{header_left}</span>
    <span style="font-style: italic;">{header_right}</span>
</div>
"""

FOOTER_TEMPLATE = """
<div style="width: 100%; font-size: 8.5pt; font-family: 'Times New Roman', serif; color: #777; border-top: 0.5px solid #bbb; padding-top: 3px; margin: 0 18mm; display: flex; justify-content: space-between;">
    <span style="letter-spacing: 1px;">Tủ Sách Tinh Hoa Thi Ca & Cổ Văn</span>
    <span>Trang <span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>
"""

async def render_html_to_pdf(html_content: str, output_path: str, header_left="TINH HOA THI CA & CỔ VĂN", header_right="Ấn Bản Toàn Thư Khảo Luận"):
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    header = HEADER_TEMPLATE.format(header_left=header_left, header_right=header_right)
    footer = FOOTER_TEMPLATE

    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Ấn Bản Thi Ca Cổ Điển</title>
<style>
{BASE_CSS}
</style>
</head>
<body>
{html_content}
</body>
</html>
"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(full_html, wait_until='networkidle')
        await page.pdf(
            path=output_path,
            format='A4',
            print_background=True,
            display_header_footer=True,
            header_template=header,
            footer_template=footer,
            margin={
                'top': '20mm',
                'bottom': '20mm',
                'left': '18mm',
                'right': '18mm'
            }
        )
        await browser.close()
    
    size = os.path.getsize(output_path)
    print(f"[OK] Generated: {output_path} ({size:,} bytes)")
    return size
