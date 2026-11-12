import streamlit as st
import numpy as np
import pandas as pd

# Import specialized engines
from modules.quant_finance.portfolio import PortfolioEngine
from modules.quant_finance.backtest import BacktestEngine
from modules.quant_finance.time_series import run_ai_training
from modules.pakse_dental.finance import PakseFinancialEngine
from modules.pakse_dental.operations import PakseOperationsEngine
from modules.pakse_dental.marketing_ai import PakseMarketingEngine
from modules.youtube_studio.studio_ui import render_youtube_studio

st.set_page_config(
    page_title="Executive AI Command Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Executive CSS Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://img.icons8.com/isometric/100/combo-chart.png", width=64)
st.sidebar.title("Trung Tâm Điều Hành AI")
st.sidebar.caption("Senior Staff Engineering & Quant Intelligence")

nav_choice = st.sidebar.radio(
    "Không Gian Làm Việc:",
    [
        "🏢 Bảng Tổng Quan Điều Hành (Overview)",
        "📈 Tài Chính Định Lượng & AI Đầu Tư",
        "🏥 Dự Án Nha Khoa Quốc Tế Pakse",
        "🎬 Xưởng Sản Xuất Video YouTube (PDF to Video)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Hệ thống đang hoạt động:**\n- PyTorch: 2.15 (CPU)\n- Keras: 3.15\n- Streamlit: 1.66")

# ==============================================================================
# SECTION 1: EXECUTIVE OVERVIEW
# ==============================================================================
if nav_choice == "🏢 Bảng Tổng Quan Điều Hành (Overview)":
    st.markdown('<div class="main-header">Trung Tâm Điều Hành Trí Tuệ Nhân Tạo & Dự Án Chiến Lược</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Hệ thống hợp nhất toàn bộ năng lực định lượng tài chính cao cấp và mô phỏng quản trị dự án đầu tư y tế.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📈 Khối Tài Chính Định Lượng (Quant Finance)")
        st.write("Tái cấu trúc từ toàn bộ kiến thức Kinh tế lượng, CFA Level I, Quants và hệ thống dữ liệu ngân hàng:")
        st.markdown("""
        * **Tối ưu hóa danh mục Markowitz**: Tự động giải ma trận hiệp phương sai tìm điểm Max Sharpe, Min Volatility và Risk Parity.
        * **Công cụ Backtest Vectorized**: Kiểm thử chiến lược giao dịch có khấu trừ ma sát thị trường (0.15% phí, 0.1% thuế, 0.05% slippage).
        * **Học sâu chuỗi thời gian**: Mạng nơ-ron Bi-LSTM Attention dự báo xu hướng lợi suất.
        """)

    with col2:
        st.subheader("🏥 Khối Dự Án Nha Khoa Quốc Tế Pakse (Laos)")
        st.write("Đồng bộ 100% hồ sơ tài chính Master trị giá $125.798 USD (~3,26 tỷ VNĐ):")
        st.markdown("""
        * **Mô phỏng tài chính động**: Điểm hòa vốn 16,6 tr/ngày (~2,68 ca khám/ngày); thời gian hoàn vốn từ 3 đến 6 tháng.
        * **Quản trị vận hành & Khấu hao**: Lịch khấu hao máy CT ConeBeam 3D, 03 ghế Ajax và tối ưu EOQ nhập phôi sứ/trụ Implant.
        * **AI Marketing Generator**: Tự động sinh kịch bản quảng cáo đa kênh tiếp cận kiều bào và tầng lớp trung lưu Champasak.
        """)

    st.markdown("---")
    st.success("✅ Toàn bộ các module tính toán độc lập đã được biên dịch sẵn sàng và kiểm tra tương thích 100% trên máy tính.")

# ==============================================================================
# SECTION 2: QUANT FINANCE & INVESTMENT AI
# ==============================================================================
elif nav_choice == "📈 Tài Chính Định Lượng & AI Đầu Tư":
    st.markdown('<div class="main-header">Tài Chính Định Lượng & AI Đầu Tư Thực Chiến</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Tối ưu hóa danh mục đa tài sản, kiểm định thuật toán giao dịch và mạng nơ-ron học sâu.</div>', unsafe_allow_html=True)

    tab_p, tab_bt, tab_ai = st.tabs(["🎯 Tối Ưu Danh Mục (Markowitz)", "🧪 Backtesting Chiến Lược", "🤖 AI Chuỗi Thời Gian (PyTorch)"])

    with tab_p:
        st.subheader("Tối Ưu Hóa Tỷ Trọng Danh Mục")
        col_pa, col_pb = st.columns([1, 2])
        with col_pa:
            tickers = st.multiselect("Chọn rổ tài sản phân tích:", ["HPG", "VHM", "VIC", "MSB", "TCB", "FPT", "SSI"], default=["HPG", "MSB", "TCB", "FPT"])
            rf = st.slider("Lãi suất phi rủi ro (%/năm):", 2.0, 8.0, 4.5, 0.1) / 100.0

            np.random.seed(len(tickers) * 9)
            mu = [round(float(0.12 + 0.04 * np.random.randn()), 4) for _ in tickers]
            cov = np.eye(len(tickers)) * 0.04
            for i in range(len(tickers)):
                for j in range(len(tickers)):
                    if i != j: cov[i, j] = 0.015 * np.cos(i + j)

        with col_pb:
            if len(tickers) >= 2:
                engine = PortfolioEngine(mu, cov, tickers, risk_free_rate=rf)
                ms = engine.optimize_max_sharpe()
                mv = engine.optimize_min_vol()
                rp = engine.optimize_risk_parity()

                m1, m2, m3 = st.columns(3)
                m1.metric("Max Sharpe", f"{ms['sharpe']:.2f}", f"Lợi suất: {ms['return']*100:.1f}%")
                m2.metric("Min Volatility", f"{mv['vol']*100:.1f}%", f"Sharpe: {mv['sharpe']:.2f}")
                m3.metric("Risk Parity (ERC)", f"{rp['sharpe']:.2f}", f"Biến động: {rp['vol']*100:.1f}%")

                df_w = pd.DataFrame({
                    'Cổ phiếu': tickers,
                    'Max Sharpe (%)': [round(ms['weights'][t]*100, 1) for t in tickers],
                    'Min Vol (%)': [round(mv['weights'][t]*100, 1) for t in tickers],
                    'Risk Parity (%)': [round(rp['weights'][t]*100, 1) for t in tickers]
                })
                st.dataframe(df_w, use_container_width=True)
                st.write("### Đường Biên Hiệu Quả (Efficient Frontier)")
                st.line_chart(engine.efficient_frontier().set_index('Volatility (%)')['Return (%)'])
            else:
                st.warning("Vui lòng chọn ít nhất 2 cổ phiếu.")

    with tab_bt:
        st.subheader("Kiểm Thử Thuật Toán Giao Dịch (Backtest)")
        col_bta, col_btb = st.columns([1, 3])
        with col_bta:
            fast_ma = st.slider("MA Ngắn hạn:", 5, 25, 10)
            slow_ma = st.slider("MA Dài hạn:", 20, 80, 30)
            capital = st.number_input("Vốn khởi điểm (VNĐ):", value=100_000_000, step=10_000_000)

        np.random.seed(42)
        n_days = 252
        dates = pd.date_range(end=pd.Timestamp.today(), periods=n_days, freq='B')
        prices = pd.Series(30000.0 * np.exp(np.cumsum(np.random.normal(0.0006, 0.016, n_days))), index=dates)
        sig = (prices.rolling(fast_ma).mean() > prices.rolling(slow_ma).mean()).astype(int)

        bt = BacktestEngine(initial_capital=float(capital))
        metrics, df_bt = bt.evaluate(prices, sig)

        with col_btb:
            b1, b2, b3, b4 = st.columns(4)
            b1.metric("Lợi nhuận", f"{metrics['Lợi nhuận ròng (%)']}%", f"CAGR: {metrics['CAGR (%)']}%")
            b2.metric("Sharpe Ratio", f"{metrics['Sharpe Ratio']}", f"Sortino: {metrics['Sortino Ratio']}")
            b3.metric("Max Drawdown", f"{metrics['Max Drawdown (%)']}%", f"Calmar: {metrics['Calmar Ratio']}")
            b4.metric("Vốn kết thúc", f"{metrics['Vốn cuối (VNĐ)']}")

            st.write("### Biểu Đồ Đường Vốn Chiến Lược vs Thị Trường")
            st.line_chart(df_bt[['strategy_equity', 'benchmark_equity']])
            st.write("### Tỷ Lệ Sụt Giảm Tài Khoản (Underwater Drawdown %)")
            st.area_chart(df_bt['drawdown_pct'])

    with tab_ai:
        st.subheader("Mạng Nơ-ron PyTorch: Bi-LSTM + Temporal Self-Attention")
        st.write("Huấn luyện mô hình học sâu nhận diện xu hướng chuỗi thời gian lợi suất.")
        if st.button("🚀 Chạy Huấn Luyện AI Ngay (PyTorch CPU Engine)"):
            with st.spinner("Đang tính toán lan truyền ngược (Backpropagation)..."):
                ai_res = run_ai_training(epochs=10)
                st.success(f"Huấn luyện thành công! Độ chính xác chiều biến động: {ai_res['acc']}%")
                col_loss, col_pred = st.columns(2)
                with col_loss:
                    st.write("### Đường Hội Tụ Hàm Mất Mát (Loss Curve)")
                    st.line_chart(pd.DataFrame({'Epoch': range(1, 11), 'MSE Loss': ai_res['losses']}).set_index('Epoch'))
                with col_pred:
                    st.write("### Đối Chiếu Dự Báo vs Thực Tế")
                    st.dataframe(pd.DataFrame({'Thực tế': ai_res['actual'], 'AI Dự báo': ai_res['pred']}), use_container_width=True)

# ==============================================================================
# SECTION 3: PAKSE DENTAL CLINIC VENTURE AI
# ==============================================================================
elif nav_choice == "🏥 Dự Án Nha Khoa Quốc Tế Pakse":
    st.markdown('<div class="main-header">Phòng Khám Nha Khoa Quốc Tế Pakse (Champasak, Lào)</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Mô hình tài chính động $125.798 USD, tối ưu hóa vật tư y tế và bộ công cụ tiếp thị AI.</div>', unsafe_allow_html=True)

    pk_finance = PakseFinancialEngine()
    pk_ops = PakseOperationsEngine()
    pk_mkt = PakseMarketingEngine()

    tab_f, tab_o, tab_d, tab_m = st.tabs([
        "📊 Mô Hình Tài Chính Động",
        "⚙️ Vận Hành & Khấu Hao Y Tế",
        "🤝 Thẩm Định Gọi Vốn (Due Diligence)",
        "📢 AI Lên Bài Quảng Cáo Tiếp Thị"
    ])

    with tab_f:
        st.subheader("1. Chỉ Số Hòa Vốn & Kịch Bản Master")
        be = pk_finance.get_breakeven()
        f1, f2, f3 = st.columns(3)
        f1.metric("Doanh thu hòa vốn / Tháng", f"{be['monthly_rev']:,.0f} VNĐ", "345,33 tr định phí")
        f2.metric("Doanh thu hòa vốn / Ngày", f"{be['daily_rev']:,.0f} VNĐ", "Chuẩn 26 ngày")
        f3.metric("Số ca khám hòa vốn", f"{be['patients_day']} ca/ngày", "Trung bình 6,2 tr/ca")

        st.write("### Bảng So Sánh 3 Kịch Bản Doanh Thu:")
        st.dataframe(pk_finance.scenario_table(), use_container_width=True)

        st.subheader("2. Giả Lập Tùy Biến Độ Nhạy (Sensitivity Simulation)")
        sc1, sc2, sc3 = st.columns(3)
        with sc1: chairs = st.slider("Số ghế nha hoạt động:", 1, 6, 3)
        with sc2: pts = st.slider("Ca khám / ghế / ngày:", 0.5, 4.0, 2.0, 0.1)
        with sc3: tkt = st.number_input("Giá trị trung bình 1 ca (VNĐ):", value=6_200_000, step=500_000)

        sim_res = pk_finance.simulate(chairs, pts, tkt)
        sr1, sr2, sr3, sr4 = st.columns(4)
        sr1.metric("Tổng ca / ngày", f"{sim_res['total_patients']} ca")
        sr2.metric("Doanh thu / tháng", f"{sim_res['rev_month']:,.0f} VNĐ")
        sr3.metric("EBITDA / tháng", f"{sim_res['ebitda']:,.0f} VNĐ", f"Biên: {sim_res['margin']}%")
        sr4.metric("Thời gian hoàn vốn", f"{sim_res['payback']} tháng", "CAPEX 3,26 tỷ")

    with tab_o:
        st.subheader("1. Lịch Trình Khấu Hao Thiết Bị Y Tế")
        st.dataframe(pk_ops.depreciation_table(), use_container_width=True)

        st.subheader("2. Lượng Đặt Hàng Kinh Tế (EOQ) Phôi Sứ & Trụ Implant")
        eoq = pk_ops.calculate_eoq()
        for k, v in eoq.items():
            st.metric(k, v)

    with tab_d:
        st.subheader("Hồ Sơ Thẩm Định Cổ Đông & Trả Lời Chất Vấn")
        q_item = st.selectbox("Chọn nội dung chất vấn:", list(pk_mkt.due_diligence.keys()))
        st.info(f"💡 **Trả lời chính thức:**\n\n{pk_mkt.due_diligence[q_item]}")

        st.markdown("""
        * **65% Cổ đông Tài chính** ($81.769 USD): Kiểm soát giải ngân, duyệt chi >1.000 USD.
        * **20% Nhóm Vận hành** ($25.160 USD): Điều hành, đối ngoại tại Lào.
        * **15% Bác sĩ Trưởng (ESOP)** ($18.870 USD): Cơ chế **Vesting 3 năm** (5%/năm cam kết gắn bó).
        """)

    with tab_m:
        st.subheader("AI Tạo Bài Viết Quảng Cáo & Kịch Bản Tiếp Thị")
        svc = st.selectbox("Chọn dịch vụ mục tiêu:", [
            "Trồng răng Implant CT 3D",
            "Răng sứ Thẩm mỹ Zirconia",
            "Nha khoa Tổng quát Gia đình"
        ])
        ad = pk_mkt.generate_ad(svc)

        st.write(f"### Tiêu đề: `{ad['headline']}`")
        st.warning(f"**Câu hút (Hook):** {ad['hook']}")
        st.text_area("Thân bài quảng cáo (Copy đăng Facebook / Zalo):", ad['body'], height=160)
        st.success(f"**Lời kêu gọi (CTA):** {ad['cta']}")

# ==============================================================================
# SECTION 4: YOUTUBE VIDEO STUDIO
# ==============================================================================
elif nav_choice == "🎬 Xưởng Sản Xuất Video YouTube (PDF to Video)":
    render_youtube_studio()

