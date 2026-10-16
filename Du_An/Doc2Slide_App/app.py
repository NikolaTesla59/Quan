import streamlit as st
import docx
from pptx import Presentation
from pptx.util import Inches, Pt
import io
import re

st.set_page_config(page_title="Doc2Slide AI", layout="centered")

st.title("🚀 Doc2Slide - Word to PowerPoint Automator")
st.write("Công cụ này giúp bạn chuyển đổi nhanh một tài liệu Word dài thành các Slide thuyết trình (Dự kiến 15 phút).")

uploaded_file = st.file_uploader("Tải lên file Word (.docx) của bạn", type=["docx"])

def extract_text_and_headings(doc_file):
    doc = docx.Document(doc_file)
    content = []
    current_heading = "Slide Nội dung"
    current_bullets = []
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
            
        # Nhan dien Heading
        if para.style.name.startswith('Heading'):
            if current_bullets:
                content.append({"title": current_heading, "bullets": current_bullets})
            current_heading = text
            current_bullets = []
        else:
            # Tach thanh cac y chinh
            sentences = re.split(r'(?<=[.!?]) +', text)
            for s in sentences:
                if len(s) > 10:
                    current_bullets.append(s)
                    
            # Neu nhieu bullet qua thi chia slide
            if len(current_bullets) >= 4:
                content.append({"title": current_heading, "bullets": current_bullets})
                current_bullets = []
                
    if current_bullets:
         content.append({"title": current_heading, "bullets": current_bullets})
         
    return content

def create_ppt(content):
    prs = Presentation()
    
    # Slide Tieu de
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "Bài Thuyết Trình"
    subtitle.text = "Được tạo tự động bởi Doc2Slide"
    
    # Cac slide noi dung
    bullet_slide_layout = prs.slide_layouts[1]
    for slide_data in content:
        slide = prs.slides.add_slide(bullet_slide_layout)
        shapes = slide.shapes
        title_shape = shapes.title
        body_shape = shapes.placeholders[1]
        
        title_shape.text = slide_data['title']
        tf = body_shape.text_frame
        
        for i, bullet in enumerate(slide_data['bullets']):
            if i == 0:
                p = tf.paragraphs[0]
                p.text = bullet
            else:
                p = tf.add_paragraph()
                p.text = bullet
                p.level = 1
                
    return prs

if uploaded_file is not None:
    st.success("Đã tải file thành công!")
    
    if st.button("Chuyển đổi sang PowerPoint"):
        with st.spinner("Đang phân tích tài liệu và vẽ Slide..."):
            try:
                # 1. Trich xuat noi dung
                content = extract_text_and_headings(uploaded_file)
                
                # 2. Tao PPTX
                prs = create_ppt(content)
                
                # 3. Luu vao bo nho tam
                pptx_io = io.BytesIO()
                prs.save(pptx_io)
                pptx_io.seek(0)
                
                st.success(f"Hoàn thành! Đã tạo ra {len(content) + 1} slides (tương đương khoảng {max(1, len(content)//2)} phút thuyết trình).")
                
                st.download_button(
                    label="📥 Tải xuống File PowerPoint (.pptx)",
                    data=pptx_io,
                    file_name="Doc2Slide_Presentation.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )
            except Exception as e:
                st.error(f"Đã xảy ra lỗi: {e}")
