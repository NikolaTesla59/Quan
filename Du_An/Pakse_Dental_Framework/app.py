import streamlit as st
import pandas as pd
from engines.financial_model import PakseFinancialModel
from engines.operations_optimizer import ClinicOperationsOptimizer
from engines.copilot_and_marketing import PakseCopilotAndMarketing

st.set_page_config(page_title="Pakse Dental Venture AI & Ops Framework", layout="wide", page_icon="🏥")

st.title("🏥 Pakse International Dental Clinic Venture & AI Operations Framework")
st.markdown("**Dự án Phòng Khám Nha Khoa Quốc Tế Pakse (Champasak, Lào)** — Hệ thống Mô Phỏng Tài Chính Động, Tối Ưu Hóa Vận Hành Y Tế & Trợ Lý Tiếp Thị AI.")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Mô Hình Tài Chính Động (Financial Engine)",
    "⚙️ Tối Ưu Vận Hành & Khấu Hao (Ops & Inventory)",
    "🤝 Thẩm Định Gọi Vốn (Investor Pitch & Due Diligence)",
    "📢 AI Lên Bài Quảng Cáo & Marketing (Ad Campaign Generator)"
])

model = PakseFinancialModel()
ops = ClinicOperationsOptimizer()
copilot = PakseCopilotAndMarketing()

# ----------------- TAB 1: FINANCIAL ENGINE -----------------
with tab1:
    st.header("Mô Phỏng Tài Chính Động & Điểm Hòa Vốn")
    st.write("Dự toán dòng tiền, EBITDA, thời gian hoàn vốn (Payback) dựa trên dữ liệu thực tế $125.798 USD.")

    be = model.calculate_breakeven()
    st.subheader("1. Chỉ Số Hòa Vốn Vận Hành (Break-even Point)")
    m1, m2, m3 = st.columns(3)
    m1.metric("Doanh thu hòa vốn / Tháng", f"{be['monthly_revenue_vnd']:,.0f} VNĐ", "345,33 tr định phí / 0.8")
    m2.metric("Doanh thu hòa vốn / Ngày", f"{be['daily_revenue_vnd']:,.0f} VNĐ", "Chuẩn 26 ngày/tháng")
    m3.metric("Số ca khám hòa vốn / Ngày", f"{be['patients_per_day']} ca/ngày", "Giá trị trung bình 6,2 tr/ca")

    st.subheader("2. So Sánh 3 Kịch Bản Doanh Thu Master")
    df_scenarios = model.simulate_scenarios()
    st.dataframe(df_scenarios, use_container_width=True)

    st.subheader("3. Bộ Giả Lập Độ Nhạy Tùy Biến (Interactive Sensitivity Simulator)")
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        chairs = st.slider("Số ghế điều trị hoạt động:", min_value=1, max_value=6, value=3)
    with col_s2:
        pts_per_chair = st.slider("Số ca khám trung bình / ghế / ngày:", min_value=0.5, max_value=5.0, value=2.0, step=0.1)
    with col_s3:
        avg_ticket = st.number_input("Giá trị trung bình mỗi ca khám (VNĐ):", value=6_200_000, step=500_000)

    sim = model.custom_simulation(chairs, pts_per_chair, avg_ticket)
    c_res1, c_res2, c_res3, c_res4 = st.columns(4)
    c_res1.metric("Tổng ca khám / ngày", f"{sim['total_patients_day']} ca")
    c_res2.metric("Doanh thu / ngày", f"{sim['revenue_day_vnd']:,.0f} VNĐ")
    c_res3.metric("EBITDA / tháng", f"{sim['ebitda_vnd']:,.0f} VNĐ", f"Biên: {sim['ebitda_margin']}%")
    c_res4.metric("Thời gian hoàn vốn", f"{sim['payback_months']} tháng", "CAPEX 3,26 tỷ")

# ----------------- TAB 2: OPERATIONS & INVENTORY -----------------
with tab2:
    st.header("Tối Ưu Hóa Chi Phí Vận Hành Y Tế & Khấu Hao Máy Móc")
    
    st.subheader("1. Lịch Trình Khấu Hao Thiết Bị Ban Đầu (Depreciation Schedule)")
    st.write("Khấu hao máy CT ConeBeam 3D, ghế nha khoa Ajax và hệ thống vô trùng Class B.")
    st.dataframe(ops.calculate_depreciation_schedule(), use_container_width=True)

    st.subheader("2. Mô Hình Đặt Hàng Kinh Tế (EOQ) Vật Tư Tiêu Hao & Trụ Implant")
    st.write("Tối ưu hóa chi phí vận chuyển qua cửa khẩu Việt - Lào và lưu kho tại Pakse.")
    eoq_res = ops.optimize_inventory_eoq()
    e1, e2, e3, e4 = st.columns(4)
    for col, (k, v) in zip([e1, e2, e3, e4], eoq_res.items()):
        col.metric(k, v)

    st.subheader("3. Kiểm Soát Đệm Dòng Tiền Lưu Động (Working Capital Buffer)")
    test_rev = st.slider("Giả định Doanh thu tháng thử nghiệm (VNĐ):", 500_000_000, 4_000_000_000, 2_080_000_000, step=100_000_000)
    wc_res = ops.working_capital_analysis(test_rev)
    st.write(f"**Đánh giá thanh khoản:** {wc_res['Trạng thái thanh khoản']}")
    st.json(wc_res)

# ----------------- TAB 3: INVESTOR PITCH -----------------
with tab3:
    st.header("Hồ Sơ Thẩm Định & Trả Lời Chất Vấn Nhà Đầu Tư (Due Diligence)")
    st.write("Hệ thống tri thức đối phó chất vấn của Cổ đông Tài chính dựa trên bản Master.")

    topic = st.selectbox("Chọn nội dung chất vấn đầu tư:", [
        "Pháp lý tại Lào",
        "Lợi thế cạnh tranh so với Thái Lan",
        "Cơ cấu cổ phần & Quyền kiểm soát",
        "Thời gian hoàn vốn"
    ])
    st.info(f"💡 **Trả lời chính thức:**\n\n{copilot.get_investor_answer(topic)}")

    st.markdown("""
    ---
    ### Cơ Cấu Cổ Phần Khuyến Nghị:
    * **65% Cổ đông Tài chính** ($81.769 USD): Góp tiền mặt, phê duyệt kép chi tiêu >1.000 USD.
    * **20% Nhóm Sáng lập & Vận hành** ($25.160 USD): Khảo sát thực địa, chuỗi cung ứng, điều hành tại chỗ.
    * **15% Bác sĩ Trưởng Chuyên môn (ESOP)** ($18.870 USD): Cơ chế **Vesting 3 năm** (5%/năm cam kết gắn bó).
    """)

# ----------------- TAB 4: MARKETING & AD GENERATOR -----------------
with tab4:
    st.header("AI Lên Bài Quảng Cáo & Kịch Bản Marketing Đa Kênh")
    st.write("Tự động sinh thông điệp truyền thông định vị dịch vụ nha khoa chất lượng cao tại Champasak.")

    col_m1, col_m2 = st.columns(2)
    with col_m1:
        service = st.selectbox("Chọn dịch vụ nha khoa trọng tâm:", [
            "Trồng răng Implant (CT ConeBeam 3D)",
            "Răng sứ thẩm mỹ cao cấp (Zirconia/Cercon)",
            "Nha khoa gia đình & Chăm sóc tổng quát"
        ])
    with col_m2:
        audience = st.selectbox("Đối tượng mục tiêu:", [
            "Kiều bào & Doanh nhân Việt tại Champasak (>18.000 người)",
            "Tầng lớp trung lưu & quan chức bản địa Lào",
            "Bệnh nhân muốn tiết kiệm chi phí vượt biên sang Ubon (Thái Lan)"
        ])

    ad = copilot.generate_ad_campaign(service, audience)
    st.subheader(f"📌 Tiêu Đề Bài Viết (Headline):")
    st.markdown(f"### `{ad['headline']}`")
    
    st.subheader("🎯 Câu Mở Đầu Thu Hút (Hook):")
    st.warning(ad['hook'])

    st.subheader("📝 Thân Bài Quảng Cáo (Body Copy):")
    st.text_area("Nội dung chi tiết (Copy để đăng Facebook / Zalo):", ad['body'], height=180)

    st.subheader("⚡ Lời Kêu Gọi Hành Động (Call-to-Action):")
    st.success(ad['cta'])
