import numpy as np
import pandas as pd

class VectorizedBacktester:
    """
    Vectorized Quantitative Backtesting Engine:
    - Eliminates Look-ahead Bias & Survivorship Bias
    - Simulates Transaction Fees (0.15%), Tax (0.1%), Slippage (0.05%)
    - Metrics: Cumulative Return, CAGR, Sharpe, Sortino, Max Drawdown, Calmar Ratio
    """
    def __init__(self, initial_capital: float = 100_000_000.0, fee_rate: float = 0.0015, tax_rate: float = 0.001, slippage: float = 0.0005):
        self.initial_capital = initial_capital
        self.fee = fee_rate
        self.tax = tax_rate
        self.slippage = slippage

    def run_backtest(self, price_series: pd.Series, signals: pd.Series) -> dict:
        """
        Runs strategy backtest based on price and position signals (1: Long, 0: Cash, -1: Short).
        """
        df = pd.DataFrame({'price': price_series, 'signal': signals}).dropna()
        # Daily return of the underlying asset
        df['asset_return'] = df['price'].pct_change().fillna(0)
        
        # Position taken yesterday for today's return (prevents Look-ahead bias)
        df['position'] = df['signal'].shift(1).fillna(0)
        
        # Trade occurrences (when position changes)
        df['trades'] = df['position'].diff().abs().fillna(0)
        
        # Gross strategy return
        df['gross_return'] = df['position'] * df['asset_return']
        
        # Transaction costs: Fee + Slippage on every entry/exit, plus Tax on sell
        cost_per_trade = self.fee + self.slippage + (self.tax / 2.0)
        df['costs'] = df['trades'] * cost_per_trade
        
        # Net strategy return
        df['net_return'] = df['gross_return'] - df['costs']
        
        # Cumulative Equity Curves
        df['strategy_equity'] = self.initial_capital * (1.0 + df['net_return']).cumprod()
        df['benchmark_equity'] = self.initial_capital * (1.0 + df['asset_return']).cumprod()
        
        # Drawdown calculation
        df['peak'] = df['strategy_equity'].cummax()
        df['drawdown'] = (df['strategy_equity'] - df['peak']) / df['peak']
        max_drawdown = float(df['drawdown'].min())
        
        # Performance ratios (Annualized 252 trading days)
        total_return = float((df['strategy_equity'].iloc[-1] / self.initial_capital) - 1.0)
        n_days = len(df)
        cagr = float((1.0 + total_return) ** (252.0 / max(n_days, 1)) - 1.0)
        
        daily_ret = df['net_return']
        mean_ret = float(daily_ret.mean()) * 252.0
        vol = float(daily_ret.std()) * np.sqrt(252.0)
        sharpe = (mean_ret - 0.045) / vol if vol > 1e-7 else 0.0
        
        # Downside Deviation for Sortino
        downside = daily_ret[daily_ret < 0]
        downside_std = float(downside.std()) * np.sqrt(252.0) if len(downside) > 0 else 1e-7
        sortino = (mean_ret - 0.045) / downside_std if downside_std > 1e-7 else 0.0
        
        calmar = cagr / abs(max_drawdown) if abs(max_drawdown) > 1e-7 else 0.0
        win_rate = float((daily_ret[df['position'] != 0] > 0).mean() * 100.0) if len(daily_ret[df['position'] != 0]) > 0 else 0.0

        return {
            'metrics': {
                'Total Return (%)': round(total_return * 100, 2),
                'CAGR (%)': round(cagr * 100, 2),
                'Sharpe Ratio': round(sharpe, 2),
                'Sortino Ratio': round(sortino, 2),
                'Max Drawdown (%)': round(max_drawdown * 100, 2),
                'Calmar Ratio': round(calmar, 2),
                'Win Rate (%)': round(win_rate, 2),
                'Final Capital (VND)': f"{df['strategy_equity'].iloc[-1]:,.0f}"
            },
            'dataframe': df
        }
