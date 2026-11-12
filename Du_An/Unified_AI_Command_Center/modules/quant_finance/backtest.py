import numpy as np
import pandas as pd

class BacktestEngine:
    """Động cơ Kiểm thử Chiến lược Giao dịch Vectorized (Zero Look-ahead Bias)."""
    def __init__(self, initial_capital: float = 100_000_000.0, fee: float = 0.0015, tax: float = 0.001, slippage: float = 0.0005):
        self.initial_capital = initial_capital
        self.cost_per_trade = fee + slippage + (tax / 2.0)

    def evaluate(self, prices: pd.Series, signals: pd.Series) -> tuple[dict, pd.DataFrame]:
        df = pd.DataFrame({'price': prices, 'signal': signals}).dropna()
        df['asset_ret'] = df['price'].pct_change().fillna(0)
        df['position'] = df['signal'].shift(1).fillna(0)
        df['trades'] = df['position'].diff().abs().fillna(0)
        df['costs'] = df['trades'] * self.cost_per_trade
        df['net_ret'] = (df['position'] * df['asset_ret']) - df['costs']

        df['strategy_equity'] = self.initial_capital * (1.0 + df['net_ret']).cumprod()
        df['benchmark_equity'] = self.initial_capital * (1.0 + df['asset_ret']).cumprod()
        df['peak'] = df['strategy_equity'].cummax()
        df['drawdown_pct'] = ((df['strategy_equity'] - df['peak']) / df['peak']) * 100.0

        total_ret = ((df['strategy_equity'].iloc[-1] / self.initial_capital) - 1.0) * 100.0
        n_days = len(df)
        cagr = (((1.0 + total_ret/100.0) ** (252.0 / max(n_days, 1))) - 1.0) * 100.0
        max_dd = float(df['drawdown_pct'].min())
        
        ann_mean = float(df['net_ret'].mean()) * 252.0
        ann_vol = float(df['net_ret'].std()) * np.sqrt(252.0)
        sharpe = (ann_mean - 0.045) / ann_vol if ann_vol > 1e-7 else 0.0
        
        downside = df['net_ret'][df['net_ret'] < 0]
        downside_vol = float(downside.std()) * np.sqrt(252.0) if len(downside) > 0 else 1e-7
        sortino = (ann_mean - 0.045) / downside_vol if downside_vol > 1e-7 else 0.0
        calmar = cagr / abs(max_dd) if abs(max_dd) > 1e-7 else 0.0

        metrics = {
            'Lợi nhuận ròng (%)': round(total_ret, 2),
            'CAGR (%)': round(cagr, 2),
            'Sharpe Ratio': round(sharpe, 2),
            'Sortino Ratio': round(sortino, 2),
            'Max Drawdown (%)': round(max_dd, 2),
            'Calmar Ratio': round(calmar, 2),
            'Vốn cuối (VNĐ)': f"{df['strategy_equity'].iloc[-1]:,.0f}"
        }
        return metrics, df
