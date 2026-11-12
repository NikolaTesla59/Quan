"""
YouTube Studio AI Module for Unified Command Center
Transforms PDF books into standard 16:9 landscape and 9:16 vertical Shorts videos.
"""

import os
import sys
import streamlit as st

# Add pipeline directory to sys.path
pipeline_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\pdf_to_youtube_pipeline"
if pipeline_dir not in sys.path:
    sys.path.append(pipeline_dir)

from pipeline import PDFToYouTubePipeline

def render_youtube_studio():
    st.markdown('<div class="main-header">🎬 Xưởng Sản Xuất Video YouTube Tự Động (PDF to Video AI)</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Tự động chuyển đổi sách PDF, tác phẩm kinh điển và tóm tắt tri thức thành Video 16:9 & Shorts 9:16 chất lượng cao.</div>', unsafe_allow_html=True)

    # 1. Advisory Banner on Copyright & Monetization
    with st.expander("⚖️ CHÍNH SÁCH BẢN QUYỀN YOUTUBE & CHIẾN LƯỢC BẬT KIẾM TIỀN BỀN VỮNG", expanded=False):
        col_cp1, col_cp2 = st.columns(2)
        with col_cp1:
            st.markdown("""
            ### 🏛️ 1. Sách Phạm Vi Công Cộng (Public Domain)
            - **Đối tượng**: Tác giả đã mất trên 50-70 năm (ví dụ: *Tôn Tử, Adam Smith, Karl Marx, Bà Huyện Thanh Quan, Nikolai Gogol, Lev Tolstoy...*).
            - **Mức độ an toàn**: **100% Hợp pháp & Tuyệt đối an toàn**.
            - **Hình thức**: Được phép diễn đọc toàn bộ nguyên tác (Audiobook), chèn nhạc nền royalty-free và bật kiếm tiền YouTube Adsense mà không lo Content ID.
            """)
        with col_cp2:
            st.markdown("""
            ### 🛡️ 2. Sách Đang Có Bản Quyền (Transformative Fair Use)
            - **Đối tượng**: Sách hiện đại còn hạn bản quyền (*Sapiens, Tư Duy Nhanh Và Chậm, Thiên Nga Đen...*).
            - **Quy tắc YouTube**: **KHÔNG ĐƯỢC** đọc nguyên văn từng câu chữ (sẽ dính Content ID hoặc gậy DMCA của NXB).
            - **Giải pháp chuyển thể**: Bắt buộc chuyển thể sang dạng **Tóm tắt sách, Review, Bình luận triết học & Đúc kết bài học**. Luật SHTT quốc tế và chính sách YouTube bảo hộ nguyên tắc "Transformative Use" này!
            """)

    st.markdown("---")

    col_setup, col_preview = st.columns([1, 1])

    with col_setup:
        st.subheader("⚙️ Cấu Hình Chuyển Thể")

        # Preset books from user's Desktop library
        preset_books = {
            "Binh Pháp Tôn Tử (Tôn Tử - 500 TCN) [Public Domain]": r"C:\Users\Admin\Desktop\Sách\Địa chính trị - Quan hệ quốc tế\01. [k. 544-496 TCN] Trung Quốc_Tôn Tử\[k. 500 TCN] Tôn Tử - Binh Pháp Tôn Tử (13 Thiên Toàn Thư).pdf",
            "Tù Nhân Của Địa Lý (Tim Marshall - 2015) [Cần tóm tắt]": r"C:\Users\Admin\Desktop\Sách\Địa chính trị - Quan hệ quốc tế\12. [1959-] Anh_Tim Marshall (Địa Chính Trị Hiện Đại)\[2015] Tim Marshall - Tù Nhân Của Địa Lý (Prisoners of Geography).pdf",
            "Đường Về Nô Lệ (Friedrich Hayek - 1944) [Kinh tế chính trị]": r"C:\Users\Admin\Desktop\Sách\Lịch sử tư tưởng kinh tế\08. [1899-1992] Áo_Friedrich Hayek\[1944] Friedrich Hayek - Đường Về Nô Lệ.pdf",
            "Tự nhập đường dẫn PDF khác...": ""
        }

        selected_preset = st.selectbox("Chọn Sách Từ Thư Viện:", list(preset_books.keys()))

        if selected_preset == "Tự nhập đường dẫn PDF khác...":
            pdf_path = st.text_input("Đường dẫn file PDF trên máy tính:", "")
        else:
            pdf_path = preset_books[selected_preset]
            st.caption(f"📁 Tệp: `{pdf_path}`")

        c1, c2 = st.columns(2)
        with c1:
            book_title = st.text_input("Tên tác phẩm / Kênh:", value="Binh Pháp Tôn Tử")
        with c2:
            chapter_title = st.text_input("Tên phân đoạn / Chương:", value="Kế Hoạch & Tác Chiến Cốt Yếu")

        c3, c4 = st.columns(2)
        with c3:
            start_p = st.number_input("Trang bắt đầu:", min_value=1, value=4, step=1)
        with c4:
            end_p = st.number_input("Trang kết thúc:", min_value=1, value=5, step=1)

        c5, c6 = st.columns(2)
        with c5:
            voice_choice = st.selectbox("Giọng Đọc AI:", ["Nam (Trầm ấm, hào hùng)", "Nữ (Truyền cảm, nhẹ nhàng)"])
            voice_gender = "male" if "Nam" in voice_choice else "female"
        with c6:
            speed_choice = st.selectbox("Tốc độ đọc:", ["Chuẩn (Normal)", "Nhanh (+10%)", "Trầm chậm (-10%)"])
            speed_map = {"Chuẩn (Normal)": "+0%", "Nhanh (+10%)": "+10%", "Trầm chậm (-10%)": "-10%"}
            voice_speed = speed_map[speed_choice]

        st.markdown("**Định Dạng Xuất Bản:**")
        chk_land = st.checkbox("📺 YouTube Chuẩn (16:9 Ngang - 1080p)", value=True)
        chk_port = st.checkbox("📱 YouTube Shorts / TikTok (9:16 Dọc - 1080x1920)", value=True)

        btn_run = st.button("🚀 Bắt Đầu Tạo Video Tự Động", use_container_width=True, type="primary")

    with col_preview:
        st.subheader("📺 Kết Quả & Trình Phát Video")

        output_land_default = os.path.join(pipeline_dir, "output", "Binh_Phap_Ton_Tu_YouTube_16x9.mp4")
        output_port_default = os.path.join(pipeline_dir, "output", "Binh_Phap_Ton_Tu_Shorts_9x16.mp4")
        meta_default = os.path.join(pipeline_dir, "output", "Binh_Phap_Ton_Tu_YouTube_Metadata.txt")

        if btn_run:
            if not os.path.exists(pdf_path):
                st.error(f"❌ Không tìm thấy file PDF tại: {pdf_path}")
            else:
                progress_bar = st.progress(0, text="Khởi động pipeline...")
                try:
                    pipeline = PDFToYouTubePipeline(
                        voice_gender=voice_gender,
                        voice_speed=voice_speed
                    )
                    progress_bar.progress(30, text="Đang xử lý âm thanh & thiết kế khung hình...")
                    results = pipeline.process_pdf(
                        pdf_path=pdf_path,
                        book_title=book_title,
                        chapter_title=chapter_title,
                        start_page=int(start_p),
                        end_page=int(end_p),
                        max_words_per_scene=30,
                        render_landscape=chk_land,
                        render_portrait=chk_port
                    )
                    progress_bar.progress(100, text="Hoàn tất trọn vẹn!")
                    st.success("🎉 Đã render hoàn tất cả Video 16:9 và Shorts 9:16!")
                except Exception as e:
                    st.error(f"Lỗi thực thi: {e}")

        # Check existing outputs
        if os.path.exists(output_land_default) or os.path.exists(output_port_default):
            tab_land, tab_port, tab_seo = st.tabs(["📺 Bản 16:9 Dài", "📱 Bản 9:16 Shorts", "📝 YouTube SEO"])

            with tab_land:
                if os.path.exists(output_land_default):
                    st.video(output_land_default)
                    st.caption(f"Đường dẫn: `{output_land_default}` | Kích thước: {os.path.getsize(output_land_default)/(1024*1024):.2f} MB")
                else:
                    st.info("Chưa có bản 16:9 được tạo.")

            with tab_port:
                if os.path.exists(output_port_default):
                    st.video(output_port_default)
                    st.caption(f"Đường dẫn: `{output_port_default}` | Kích thước: {os.path.getsize(output_port_default)/(1024*1024):.2f} MB")
                else:
                    st.info("Chưa có bản Shorts 9:16 được tạo.")

            with tab_seo:
                if os.path.exists(meta_default):
                    with open(meta_default, "r", encoding="utf-8") as f:
                        st.code(f.read(), language="markdown")
                else:
                    st.info("Chưa có dữ liệu SEO.")
        else:
            st.info("ℹ️ Nhấn nút 'Bắt Đầu Tạo Video Tự Động' để hệ thống tiến hành trích xuất sách, lồng tiếng và render video hoàn chỉnh.")
