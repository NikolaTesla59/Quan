"""
Standalone YouTube Video Studio Application
Run independently via: streamlit run app.py
Or click: YOUTUBE_VIDEO_STUDIO.bat on Desktop
"""

import os
import sys
import glob
import streamlit as st

# Setup paths
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

from core.video_composer import VideoComposer
from core.pdf_reader import PDFReader

st.set_page_config(
    page_title="Studio Sản Xuất Video YouTube Từ Sách PDF",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Dark Studio Styling
st.markdown("""
<style>
    .studio-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.5px;
        margin-bottom: 4px;
    }
    .studio-sub {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 24px;
    }
    .status-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="studio-header">🎬 XƯỞNG SẢN XUẤT VIDEO YOUTUBE & TIKTOK TỰ ĐỘNG</div>', unsafe_allow_html=True)
st.markdown('<div class="studio-sub">Chuyển thể sách PDF nguyên tác thành Video 16:9 Full HD và 9:16 Shorts chất lượng cao với giọng đọc AI Studio.</div>', unsafe_allow_html=True)

# Scan user's Desktop Sách folder for quick selection
sach_dir = r"C:\Users\Admin\Desktop\Sách"
scanned_books = {}
if os.path.exists(sach_dir):
    pdf_files = glob.glob(os.path.join(sach_dir, "**", "*.pdf"), recursive=True)
    for p in pdf_files[:30]:
        base_name = os.path.splitext(os.path.basename(p))[0]
        scanned_books[base_name] = p

col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.subheader("⚙️ 1. Cấu Hình Sách & Phân Đoạn")
    
    source_type = st.radio("Nguồn sách PDF:", ["Chọn từ thư viện Desktop/Sách", "Tự nhập đường dẫn file PDF"], horizontal=True)
    
    if source_type == "Chọn từ thư viện Desktop/Sách" and scanned_books:
        selected_name = st.selectbox("Chọn tác phẩm:", list(scanned_books.keys()))
        selected_pdf = scanned_books[selected_name]
        default_book_title = selected_name.split("]")[-1].strip() if "]" in selected_name else selected_name
    else:
        selected_pdf = st.text_input("Đường dẫn file PDF:", value=r"C:\Users\Admin\Desktop\Sách\Địa chính trị - Quan hệ quốc tế\01. [k. 544-496 TCN] Trung Quốc_Tôn Tử\[k. 500 TCN] Tôn Tử - Binh Pháp Tôn Tử (13 Thiên Toàn Thư).pdf")
        default_book_title = "Binh Pháp Tôn Tử"

    # Inspect total pages
    total_pages = 1
    if os.path.exists(selected_pdf):
        try:
            reader = PDFReader(selected_pdf)
            total_pages = reader.total_pages
            st.caption(f"📁 Tệp hợp lệ: `{os.path.basename(selected_pdf)}` (Tổng cộng: **{total_pages}** trang)")
        except Exception:
            st.caption(f"📁 Tệp: `{selected_pdf}`")
    else:
        st.warning("⚠️ File PDF chưa tồn tại hoặc đường dẫn không hợp lệ.")

    c_b1, c_b2 = st.columns(2)
    with c_b1:
        book_title = st.text_input("Tên tác phẩm hiển thị:", value=default_book_title)
    with c_b2:
        chapter_title = st.text_input("Tên chương / Phân đoạn:", value="Kế Hoạch & Tác Chiến Cốt Yếu")

    st.markdown("**Khoảng trang cần chuyển thành Video:**")
    c_p1, c_p2 = st.columns(2)
    with c_p1:
        start_page = st.number_input("Trang bắt đầu:", min_value=1, max_value=max(1, total_pages), value=min(4, total_pages), step=1)
    with c_p2:
        end_page = st.number_input("Trang kết thúc:", min_value=1, max_value=max(1, total_pages), value=min(5, total_pages), step=1)

    st.subheader("🎙️ 2. Giọng Đọc AI & Định Dạng Video")
    c_v1, c_v2 = st.columns(2)
    with c_v1:
        voice_sel = st.selectbox("Giọng đọc AI:", ["Nam (Trầm ấm, hào hùng - NamMinh)", "Nữ (Truyền cảm, nhẹ nhàng - HoaiMy)"])
        voice_gender = "male" if "Nam" in voice_sel else "female"
    with c_v2:
        speed_sel = st.selectbox("Tốc độ giọng đọc:", ["Chuẩn (Normal)", "Nhanh (+10%)", "Trầm chậm (-10%)"])
        speed_map = {"Chuẩn (Normal)": "+0%", "Nhanh (+10%)": "+10%", "Trầm chậm (-10%)": "-10%"}
        voice_speed = speed_map[speed_sel]

    c_f1, c_f2 = st.columns(2)
    with c_f1:
        render_16_9 = st.checkbox("📺 YouTube Chuẩn (16:9 Ngang - 1080p)", value=True)
    with c_f2:
        render_9_16 = st.checkbox("📱 Shorts / TikTok (9:16 Dọc - 1080x1920)", value=True)

    btn_start = st.button("🚀 BẮT ĐẦU XUẤT BẢN VIDEO", type="primary", use_container_width=True)

with col_right:
    st.subheader("📺 3. Trình Phát Xem Trước & Thành Phẩm")
    
    composer = VideoComposer(workspace_dir=CURRENT_DIR)
    
    if btn_start:
        if not os.path.exists(selected_pdf):
            st.error("❌ Vui lòng chọn hoặc kiểm tra lại đường dẫn file PDF!")
        elif start_page > end_page:
            st.error("❌ Trang bắt đầu không thể lớn hơn trang kết thúc!")
        else:
            prog_bar = st.progress(0, text="Khởi động pipeline...")
            status_text = st.empty()

            def on_progress(pct: int, msg: str):
                prog_bar.progress(pct, text=msg)
                status_text.info(f"⏳ {msg}")

            try:
                result = composer.process_audiobook(
                    pdf_path=selected_pdf,
                    book_title=book_title,
                    chapter_title=chapter_title,
                    start_page=int(start_page),
                    end_page=int(end_page),
                    voice_gender=voice_gender,
                    voice_speed=voice_speed,
                    render_16_9=render_16_9,
                    render_9_16=render_9_16,
                    progress_callback=on_progress
                )
                prog_bar.progress(100, text="Hoàn tất!")
                status_text.success("🎉 Xuất bản video thành công 100%!")
            except Exception as e:
                st.error(f"Lỗi: {e}")

    # Display existing outputs
    output_files = glob.glob(os.path.join(composer.output_dir, "*.mp4"))
    meta_files = glob.glob(os.path.join(composer.output_dir, "*.txt"))

    if output_files:
        st.markdown(f"**Đã tìm thấy {len(output_files)} video trong thư mục xuất bản:**")
        
        tab_v1, tab_v2, tab_v3 = st.tabs(["📺 Bản 16:9 Dài", "📱 Bản 9:16 Shorts", "📝 Gói SEO YouTube"])
        
        with tab_v1:
            land_files = [f for f in output_files if "16x9" in f or "YouTube" in f]
            if land_files:
                target_16 = land_files[0]
                st.video(target_16)
                st.caption(f"📁 Tệp: `{target_16}` | Dung lượng: {os.path.getsize(target_16)/(1024*1024):.2f} MB")
            else:
                st.info("Chưa có bản 16:9 nào.")

        with tab_v2:
            port_files = [f for f in output_files if "9x16" in f or "Shorts" in f]
            if port_files:
                target_9 = port_files[0]
                st.video(target_9)
                st.caption(f"📁 Tệp: `{target_9}` | Dung lượng: {os.path.getsize(target_9)/(1024*1024):.2f} MB")
            else:
                st.info("Chưa có bản Shorts nào.")

        with tab_v3:
            if meta_files:
                with open(meta_files[0], "r", encoding="utf-8") as f:
                    st.code(f.read(), language="markdown")
            else:
                st.info("Chưa có gói SEO.")

        st.markdown("---")
        if st.button("📂 Mở Thư Mục Chứa Video Trên Máy Tính", use_container_width=True):
            os.startfile(composer.output_dir)
    else:
        st.info("💡 Bấm nút 'BẮT ĐẦU XUẤT BẢN VIDEO' để hệ thống tự động bóc tách PDF, lồng tiếng và render video hoàn chỉnh.")
