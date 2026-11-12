import streamlit as st
import numpy as np
import pandas as pd
from engines.portfolio_optimizer import PortfolioOptimizer
from engines.backtester import VectorizedBacktester
from engines.time_series_ai import train_mini_ai_model

st.set_page_config(page_title="Quant Finance & AI Investment Hub", layout="wide", page_icon="📈")

st.title("📈 Quantitative Finance & Deep Learning Investment Framework")
st.markdown("Hệ thống Phân tích Định lượng & AI Đầu tư chuẩn Senior Quant: Tối ưu danh mục Markowitz, Backtesting thực chiến và Mạng nơ-ron Bi-LSTM Attention.")

tab1, tab2, tab3 = st.tabs(["🎯 Tối Ưu Hóa Danh Mục (Portfolio Optimization)", "🧪 Kiểm Thử Chiến Lược (Backtesting Engine)", "🤖 AI Chuỗi Thời Gian (Deep Learning Forecasting)"])

# ----------------- TAB 1: PORTFOLIO OPTIMIZATION -----------------
with tab1:
    st.header("Tối Ưu Hóa Danh Mục Đa Tài Sản (Markowitz & Risk Parity)")
    st.write("Mô phỏng đường biên hiệu quả (Efficient Frontier) và tìm tỷ trọng tối ưu cho danh mục cổ phiếu.")
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.subheader("Cấu hình tài sản & Giả định")
        assets = st.multiselect("Chọn rổ cổ phiếu quan sát:", ["HPG", "VHM", "VIC", "MSB", "TCB", "FPT", "SSI"], default=["HPG", "MSB", "TCB", "FPT"])
        rf = st.slider("Lãi suất phi rủi ro (Risk-free Rate - %):", min_value=2.0, max_value=8.0, value=4.5, step=0.1) / 100.0
        
        # Simulated return vector & covariance matrix based on asset choices
        np.random.seed(len(assets) * 7)
        mu = [round(float(0.12 + 0.05 * np.random.randn()), 4) for _ in assets]
        cov = np.eye(len(assets)) * 0.04
        for i in range(len(assets)):
            for j in range(len(assets)):
                if i != j:
                    cov[i, j] = 0.015 * np.sin(i + j)
        
        df_assets = pd.DataFrame({'Cổ phiếu': assets, 'Lợi suất kỳ vọng năm (%)': [round(m*100, 2) for m in mu]})
        st.dataframe(df_assets, use_container_width=True)

    with col_b:
        if len(assets) >= 2:
            opt_engine = PortfolioOptimizer(mu, cov, assets, risk_free_rate=rf)
            max_sharpe = opt_engine.max_sharpe_portfolio()
            min_var = opt_engine.min_variance_portfolio()
            risk_parity = opt_engine.risk_parity_portfolio()

            st.subheader("Kết Quả So Sánh 3 Chiến Lược Tối Ưu")
            m1, m2, m3 = st.columns(3)
            m1.metric("Max Sharpe Ratio", f"{max_sharpe['sharpe_ratio']:.2f}", f"Ret: {max_sharpe['expected_return']*100:.1f}% | Vol: {max_sharpe['volatility']*100:.1f}%")
            m2.metric("Min Volatility (GMV)", f"{min_var['volatility']*100:.1f}%", f"Ret: {min_var['expected_return']*100:.1f}% | Sharpe: {min_var['sharpe_ratio']:.2f}")
            m3.metric("Risk Parity (ERC)", f"{risk_parity['sharpe_ratio']:.2f}", f"Ret: {risk_parity['expected_return']*100:.1f}% | Vol: {risk_parity['volatility']*100:.1f}%")

            st.write("### Phân Bổ Tỷ Trọng Danh Mục:")
            df_weights = pd.DataFrame({
                'Tài sản': assets,
                'Max Sharpe (%)': [round(max_sharpe['weights'][a]*100, 1) for a in assets],
                'Min Volatility (%)': [round(min_var['weights'][a]*100, 1) for a in assets],
                'Risk Parity (%)': [round(risk_parity['weights'][a]*100, 1) for a in assets]
            })
            st.dataframe(df_weights, use_container_width=True)
            
            # Efficient Frontier curve
            frontier_df = opt_engine.generate_efficient_frontier(30)
            st.line_chart(frontier_df.set_index('Volatility')['Return'])
        else:
            st.warning("Vui lòng chọn ít nhất 2 cổ phiếu để tối ưu hóa danh mục.")

# ----------------- TAB 2: BACKTESTING ENGINE -----------------
with tab2:
    st.header("Kiểm Thử Chiến Lược Giao Dịch Thuật Toán (Backtesting)")
    st.write("Mô phỏng chiến lược Momentum Breakout có tính toán đầy đủ thuế (0.1%), phí (0.15%) và trượt giá (0.05%).")
    
    col_bt1, col_bt2 = st.columns([1, 3])
    with col_bt1:
        fast_ma = st.slider("MA Ngắn hạn (Phiên):", 5, 30, 10)
        slow_ma = st.slider("MA Dài hạn (Phiên):", 20, 100, 30)
        initial_cap = st.number_input("Vốn khởi điểm (VNĐ):", value=100_000_000, step=10_000_000)

    # Generate synthetic price series
    np.random.seed(101)
    n_days = 300
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n_days, freq='B')
    returns = np.random.normal(0.0008, 0.018, n_days)
    prices = 25000.0 * np.exp(np.cumsum(returns))
    price_series = pd.Series(prices, index=dates)

    # Generate signals
    ma_fast_series = price_series.rolling(fast_ma).mean()
    ma_slow_series = price_series.rolling(slow_ma).mean()
    signals = (ma_fast_series > ma_slow_series).astype(int)

    backtester = VectorizedBacktester(initial_capital=float(initial_cap))
    res = backtester.run_backtest(price_series, signals)
    metrics = res['metrics']
    df_res = res['dataframe']

    with col_bt2:
        st.subheader("Bảng Chỉ Số Đánh Giá Rủi Ro & Lợi Nhuận Thực Tế")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Tổng Lợi Nhuận", f"{metrics['Total Return (%)']}%", f"CAGR: {metrics['CAGR (%)']}%")
        c2.metric("Sharpe Ratio", f"{metrics['Sharpe Ratio']}", f"Sortino: {metrics['Sortino Ratio']}")
        c3.metric("Max Drawdown", f"{metrics['Max Drawdown (%)']}%", f"Calmar: {metrics['Calmar Ratio']}")
        c4.metric("Tỷ Lệ Thắng (Win Rate)", f"{metrics['Win Rate (%)']}%", f"Vốn cuối: {metrics['Final Capital (VND)']}")

        st.write("### Biểu Đồ Tăng Trưởng Tài Khoản (Strategy vs Benchmark Buy & Hold):")
        st.line_chart(df_res[['strategy_equity', 'benchmark_equity']])
        
        st.write("### Vùng Sụt Giảm Tài Khoản (Underwater Drawdown %):")
        st.area_chart(df_res['drawdown'] * 100)

# ----------------- TAB 3: AI TIME SERIES FORECASTING -----------------
with tab3:
    st.header("Mô Hình Học Sâu PyTorch: Bidirectional LSTM + Temporal Attention")
    st.write("Dự báo xu hướng lợi suất và phân tích cơ chế chú ý theo thời gian trên máy tính cục bộ.")
    
    if st.button("🚀 Chạy Huấn Luyện Mô Hình AI Mẫu (PyTorch)"):
        with st.spinner("Đang chạy mô hình PyTorch trên CPU..."):
            ai_res = train_mini_ai_model(epochs=10)
            st.success(f"Huấn luyện thành công! Độ chính xác chiều dự báo (Directional Accuracy): {ai_res['directional_accuracy']}%")
            
            c_loss, c_pred = st.columns(2)
            with c_loss:
                st.subheader("Hàm Mất Mát Theo Từng Epoch (Loss Curve)")
                loss_df = pd.DataFrame({'Epoch': ai_res['epochs'], 'MSE Loss': ai_res['losses']})
                st.line_chart(loss_df.set_index('Epoch'))
            
            with c_pred:
                st.subheader("So Sánh Giá Trị Thực Tế vs Dự Báo Của AI")
                pred_df = pd.DataFrame({
                    'Mẫu': [f"Mẫu {i+1}" for i in range(len(ai_res['sample_actual']))],
                    'Lợi suất thực tế': ai_res['sample_actual'],
                    'AI Dự báo': ai_res['sample_pred']
                })
                st.dataframe(pred_df, use_container_width=True)
