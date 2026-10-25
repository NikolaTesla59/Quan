# -*- coding: utf-8 -*-
"""
Script to render missing masterpieces for Vietnamese Literature:
- Ngô Tất Tố: Việc Làng, Lều Chõng
- Vũ Trọng Phụng: Kỹ Nghệ Lấy Tây, Cơm Thầy Cơm Cô, Làm Đĩ
- Thạch Lam: Nắng Trong Vườn, Theo Dòng, Sợi Tóc
- Nguyễn Tuân: Tùy Bút Sông Đà (Toàn Tập Ký & Tùy Bút)
"""
import os
import sys
import ssl
import asyncio
import urllib.request
from markdown_it import MarkdownIt
from playwright.async_api import async_playwright
import pymupdf

ctx = ssl._create_unverified_context()
md_parser = MarkdownIt()

BASE_VH = r"C:\Users\Admin\Desktop\Sách\Văn học"

BOOKS_TO_RENDER = [
    # 1. Ngô Tất Tố - Việc Làng
    {
        "repo": "ngo-tat-to_viec-lang",
        "folder": "16. [1894-1954] Việt Nam_Ngô Tất Tố",
        "filename": "Việc Làng (Toàn Văn Tập Phóng Sự Hủ Tục Nông Thôn) (1940).pdf",
        "title": "VIỆC LÀNG",
        "subtitle": "Tập Phóng Sự Điều Tra Hủ Tục & Sách Nhiễu Nông Thôn (Toàn Văn)",
        "author": "NGÔ TẤT TỐ",
        "meta": "Xuất bản: 1940 • NXB Mai Lĩnh • Toàn văn tác phẩm số hóa chuẩn thư viện",
        "type": "khudocmo"
    },
    # 2. Ngô Tất Tố - Lều Chõng
    {
        "repo": "ngo-tat-to_leu-chong",
        "folder": "16. [1894-1954] Việt Nam_Ngô Tất Tố",
        "filename": "Lều Chõng (Toàn Văn Tiểu Thuyết Khoa Cử Phong Kiến) (1952).pdf",
        "title": "LỀU CHÕNG",
        "subtitle": "Bức Tranh Toàn Cảnh Chế Độ Thi Cử Khoa Bảng Phong Kiến (Toàn Văn Hoàn Chỉnh)",
        "author": "NGÔ TẤT TỐ",
        "meta": "Hoàn thành: 1939 • NXB Mai Lĩnh • Toàn văn tác phẩm số hóa chuẩn thư viện",
        "type": "khudocmo"
    },
    # 3. Vũ Trọng Phụng - Kỹ Nghệ Lấy Tây
    {
        "repo": "vu-trong-phung_ky-nghe-lay-tay",
        "folder": "19. [1912-1939] Việt Nam_Vũ Trọng Phụng",
        "filename": "Kỹ Nghệ Lấy Tây (Toàn Văn Phóng Sự Hiện Thực) (1934).pdf",
        "title": "KỸ NGHỆ LẤY TÂY",
        "subtitle": "Phóng Sự Hiện Thực Xã Hội Đô Thị Nửa Thực Dân (Toàn Văn)",
        "author": "VŨ TRỌNG PHỤNG",
        "meta": "Xuất bản: 1934 • Báo Nhật Tân • Toàn văn tác phẩm số hóa chuẩn thư viện",
        "type": "khudocmo"
    },
    # 4. Vũ Trọng Phụng - Cơm Thầy Cơm Cô
    {
        "repo": "vu-trong-phung_com-thay-com-co",
        "folder": "19. [1912-1939] Việt Nam_Vũ Trọng Phụng",
        "filename": "Cơm Thầy Cơm Cô (Toàn Văn Phóng Sự Điều Tra) (1936).pdf",
        "title": "CƠM THẦY CƠM CÔ",
        "subtitle": "Bức Tranh Phơi Bày Nỗi Nhục Nhằn Cay Đắng Của Giới Con Sen Kẻ Nhớn (Toàn Văn)",
        "author": "VŨ TRỌNG PHỤNG",
        "meta": "Xuất bản: 1936 • Báo Hà Nội Báo • Toàn văn tác phẩm số hóa chuẩn thư viện",
        "type": "khudocmo"
    },
    # 5. Vũ Trọng Phụng - Làm Đĩ
    {
        "repo": "vu-trong-phung_lam-di",
        "folder": "19. [1912-1939] Việt Nam_Vũ Trọng Phụng",
        "filename": "Làm Đĩ (Toàn Văn Tiểu Thuyết Xã Hội) (1936).pdf",
        "title": "LÀM ĐĨ",
        "subtitle": "Tiểu Thuyết Xã Hội & Luận Đề Giáo Dục Giới Tính Đầy Trắc Ẩn (Toàn Văn)",
        "author": "VŨ TRỌNG PHỤNG",
        "meta": "Xuất bản: 1936 • NXB Mai Lĩnh • Toàn văn tác phẩm số hóa chuẩn thư viện",
        "type": "khudocmo"
    },
    # 6. Thạch Lam - Nắng Trong Vườn
    {
        "repo": "thach-lam_nang-trong-vuon",
        "folder": "17. [1910-1942] Việt Nam_Thạch Lam",
        "filename": "Nắng Trong Vườn (Toàn Tập Truyện Ngắn) (1938).pdf",
        "title": "NẮNG TRONG VƯỜN",
        "subtitle": "Tập Truyện Ngắn Tinh Tế Về Những Mảnh Đời Lặng Lẽ & Nhân Hậu (Toàn Văn)",
        "author": "THẠCH LAM",
        "meta": "Xuất bản: 1938 • NXB Đời Nay • Toàn văn tác phẩm số hóa chuẩn thư viện",
        "type": "khudocmo"
    },
    # 7. Thạch Lam - Theo Dòng
    {
        "repo": "thach-lam_theo-giong",
        "folder": "17. [1910-1942] Việt Nam_Thạch Lam",
        "filename": "Theo Dòng (Toàn Tập Tiểu Luận & Tùy Bút Văn Học) (1941).pdf",
        "title": "THEO DÒNG",
        "subtitle": "Tập Tiểu Luận, Tùy Bút & Quan Điểm Nghệ Thuật Thanh Nhã Của Bậc Thầy Văn Xuôi (Toàn Văn)",
        "author": "THẠCH LAM",
        "meta": "Xuất bản: 1941 • NXB Đời Nay • Toàn văn tác phẩm số hóa chuẩn thư viện",
        "type": "khudocmo"
    },
    # 8. Thạch Lam - Sợi Tóc
    {
        "repo": "thach-lam_soi-toc",
        "folder": "17. [1910-1942] Việt Nam_Thạch Lam",
        "filename": "Sợi Tóc (Toàn Tập Truyện Ngắn Tinh Tuyển) (1942).pdf",
        "title": "SỢI TÓC",
        "subtitle": "Tập Truyện Ngắn Cuối Cùng & Chiêm Nghiệm Vi Diệu Về Thiện - Ác Trong Tâm Hồn (Toàn Văn)",
        "author": "THẠCH LAM",
        "meta": "Xuất bản: 1942 • NXB Đời Nay • Toàn văn tác phẩm số hóa chuẩn thư viện",
        "type": "khudocmo"
    }
]

CSS_STYLE = """
@page {
    size: A5 portrait;
    margin: 15mm 15mm 18mm 15mm;
    @bottom-center {
        content: counter(page);
        font-family: 'Times New Roman', serif;
        font-size: 9pt;
        color: #666;
    }
}
body {
    font-family: 'Times New Roman', serif;
    font-size: 10.5pt;
    line-height: 1.55;
    color: #1a1a1a;
    text-align: justify;
}
.book-cover {
    page-break-after: always;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    border: 2px solid #8b0000;
    padding: 35px;
    box-sizing: border-box;
}
.book-badge {
    font-size: 9pt;
    letter-spacing: 2px;
    color: #8b0000;
    text-transform: uppercase;
    font-weight: bold;
    margin-bottom: 20px;
}
.book-title {
    font-size: 24pt;
    font-weight: bold;
    color: #8b0000;
    margin-bottom: 10px;
    text-transform: uppercase;
}
.book-subtitle {
    font-size: 11pt;
    font-style: italic;
    color: #555;
    margin-bottom: 25px;
    max-width: 85%;
    line-height: 1.4;
}
.book-author {
    font-size: 16pt;
    font-weight: bold;
    color: #222;
    margin-top: 30px;
}
.book-meta {
    font-size: 9.5pt;
    color: #777;
    margin-top: 15px;
}
h1 {
    font-size: 15pt;
    color: #8b0000;
    border-bottom: 1px solid #8b0000;
    padding-bottom: 5px;
    margin-top: 30px;
    page-break-before: always;
}
h2 {
    font-size: 12.5pt;
    color: #4a0e17;
    margin-top: 20px;
}
h3 {
    font-size: 11.5pt;
    color: #333;
    margin-top: 15px;
}
p {
    margin-bottom: 10px;
    text-indent: 1.5em;
}
blockquote {
    font-style: italic;
    margin: 15px 25px;
    color: #555;
    border-left: 3px solid #8b0000;
    padding-left: 10px;
}
"""

def fetch_doc_md(repo):
    url = f"https://raw.githubusercontent.com/khudocmo/{repo}/main/doc.md"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        raw_md = resp.read().decode('utf-8')
    if raw_md.startswith('---'):
        parts = raw_md.split('---', 2)
        if len(parts) >= 3:
            return parts[2]
    return raw_md

async def render_books():
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for b in BOOKS_TO_RENDER:
            folder_path = os.path.join(BASE_VH, b['folder'])
            os.makedirs(folder_path, exist_ok=True)
            out_pdf = os.path.join(folder_path, b['filename'])

            print(f"\n---> Fetching {b['title']} ({b['repo']})...")
            try:
                raw_text = fetch_doc_md(b['repo'])
                body_html = md_parser.render(raw_text)

                full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>{CSS_STYLE}</style>
</head>
<body>
    <div class="book-cover">
        <div class="book-badge">Tủ Sách Văn Học Kinh Điển Việt Nam</div>
        <div class="book-title">{b['title']}</div>
        <div class="book-subtitle">{b['subtitle']}</div>
        <div class="book-author">{b['author']}</div>
        <div class="book-meta">{b['meta']}</div>
    </div>
    {body_html}
</body>
</html>"""

                print(f"Rendering {b['filename']}...")
                await page.set_content(full_html, wait_until="networkidle")
                await page.pdf(
                    path=out_pdf,
                    format="A5",
                    print_background=True,
                    margin={"top": "15mm", "bottom": "18mm", "left": "15mm", "right": "15mm"}
                )

                sz = os.path.getsize(out_pdf)
                sz_mb = round(sz / (1024 * 1024), 2)
                doc = pymupdf.open(out_pdf)
                pgs = len(doc)
                doc.close()

                print(f"  [SUCCESS] {b['filename']} -> {sz_mb} MB, {pgs} pages")
                results.append({
                    "author": b["author"],
                    "title": b["title"],
                    "file": b["filename"],
                    "status": "SUCCESS",
                    "pages": pgs,
                    "size_bytes": sz,
                    "size_mb": sz_mb
                })
            except Exception as e:
                print(f"  [FAILED] {b['filename']}: {e}")
                results.append({
                    "author": b["author"],
                    "title": b["title"],
                    "file": b["filename"],
                    "status": "FAILED",
                    "error": str(e)
                })

        await browser.close()
    return results

if __name__ == "__main__":
    import json
    res = asyncio.run(render_books())
    with open(r"C:\Users\Admin\.gemini\antigravity\scratch\vietnamese_render_results.json", "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
