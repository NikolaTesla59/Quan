"""
Core PDF Reader & Audiobook Text Chunker
Extracts verbatim text page-by-page, cleans artifacts, and structures into natural speech scenes.
"""

import os
import re
from typing import List, Dict, Any
import pypdf

class PDFReader:
    def __init__(self, pdf_path: str):
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Không tìm thấy file PDF: {pdf_path}")
        self.pdf_path = os.path.abspath(pdf_path)
        self.reader = pypdf.PdfReader(self.pdf_path)
        self.total_pages = len(self.reader.pages)

    def extract_text_range(self, start_page: int = 1, end_page: int = None) -> List[Dict[str, Any]]:
        """Extracts verbatim text for the specified page range (1-indexed)."""
        if end_page is None or end_page > self.total_pages:
            end_page = self.total_pages
        
        pages_content = []
        for p in range(start_page - 1, end_page):
            raw_text = self.reader.pages[p].extract_text() or ""
            cleaned = self._clean_verbatim_text(raw_text)
            if cleaned:
                pages_content.append({
                    "page_num": p + 1,
                    "text": cleaned
                })
        return pages_content

    @staticmethod
    def _clean_verbatim_text(text: str) -> str:
        """Cleans noise while strictly preserving verbatim literature content."""
        lines = [line.strip() for line in text.splitlines()]
        filtered = []
        for line in lines:
            if not line:
                continue
            # Remove isolated page numbering digits
            if re.fullmatch(r"\d+", line):
                continue
            filtered.append(line)
        joined = " ".join(filtered)
        # Collapse excessive whitespace
        joined = re.sub(r"\s+", " ", joined).strip()
        return joined

    def chunk_into_audiobook_scenes(
        self,
        pages_content: List[Dict[str, Any]],
        book_title: str,
        chapter_title: str,
        words_per_scene: int = 35
    ) -> List[Dict[str, Any]]:
        """
        Chunks verbatim text into speaking cards/scenes of 30-40 words each.
        Preserves natural sentence boundaries for ideal pacing.
        """
        full_text = " ".join([p["text"] for p in pages_content])
        
        # Split by sentence endings (. ! ? …)
        sentences = re.split(r"(?<=[.!?…])\s+", full_text)
        
        scenes = []
        current_chunk = []
        current_wc = 0
        scene_idx = 1
        
        for s in sentences:
            s = s.strip()
            if not s:
                continue
            words = s.split()
            if current_wc + len(words) > words_per_scene and current_chunk:
                scene_text = " ".join(current_chunk)
                scenes.append({
                    "scene_index": scene_idx,
                    "book_title": book_title,
                    "chapter_title": chapter_title,
                    "text": scene_text,
                    "word_count": current_wc
                })
                scene_idx += 1
                current_chunk = [s]
                current_wc = len(words)
            else:
                current_chunk.append(s)
                current_wc += len(words)
                
        if current_chunk:
            scene_text = " ".join(current_chunk)
            scenes.append({
                "scene_index": scene_idx,
                "book_title": book_title,
                "chapter_title": chapter_title,
                "text": scene_text,
                "word_count": current_wc
            })
            
        return scenes
