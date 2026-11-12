import numpy as np
import pandas as pd
from scipy.optimize import minimize

class PortfolioEngine:
    """Động cơ Tối ưu hóa Danh mục Đầu tư: Markowitz & Risk Parity."""
    def __init__(self, expected_returns: np.ndarray, cov_matrix: np.ndarray, asset_names: list[str], risk_free_rate: float = 0.045):
        self.mu = np.array(expected_returns)
        self.cov = np.array(cov_matrix)
        self.assets = asset_names
        self.rf = risk_free_rate
        self.n = len(asset_names)

    def performance(self, weights: np.ndarray) -> tuple[float, float, float]:
        w = np.array(weights)
        r = float(np.sum(self.mu * w))
        v = float(np.sqrt(np.dot(w.T, np.dot(self.cov, w))))
        s = (r - self.rf) / v if v > 1e-7 else 0.0
        return r, v, s

    def optimize_max_sharpe(self) -> dict:
        opt = minimize(lambda w: -self.performance(w)[2], np.ones(self.n)/self.n, method='SLSQP',
                       bounds=tuple((0.0, 1.0) for _ in range(self.n)),
                       constraints=({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0}))
        w = np.round(opt.x, 4)
        r, v, s = self.performance(w)
        return {'weights': dict(zip(self.assets, w.tolist())), 'return': r, 'vol': v, 'sharpe': s}

    def optimize_min_vol(self) -> dict:
        opt = minimize(lambda w: self.performance(w)[1], np.ones(self.n)/self.n, method='SLSQP',
                       bounds=tuple((0.0, 1.0) for _ in range(self.n)),
                       constraints=({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0}))
        w = np.round(opt.x, 4)
        r, v, s = self.performance(w)
        return {'weights': dict(zip(self.assets, w.tolist())), 'return': r, 'vol': v, 'sharpe': s}

    def optimize_risk_parity(self) -> dict:
        def obj(w):
            sig = np.sqrt(np.dot(w.T, np.dot(self.cov, w)))
            if sig < 1e-8: return 0.0
            mrc = np.dot(self.cov, w) / sig
            rc = w * mrc
            return np.sum((rc - (sig / self.n)) ** 2)
        opt = minimize(obj, np.ones(self.n)/self.n, method='SLSQP',
                       bounds=tuple((0.01, 1.0) for _ in range(self.n)),
                       constraints=({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0}))
        w = np.round(opt.x / np.sum(opt.x), 4)
        r, v, s = self.performance(w)
        return {'weights': dict(zip(self.assets, w.tolist())), 'return': r, 'vol': v, 'sharpe': s}

    def efficient_frontier(self, n_points: int = 30) -> pd.DataFrame:
        min_v = self.optimize_min_vol()['return']
        max_r = float(np.max(self.mu))
        target_returns = np.linspace(min_v, max_r, n_points)
        rows = []
        for tr in target_returns:
            opt = minimize(lambda w: self.performance(w)[1], np.ones(self.n)/self.n, method='SLSQP',
                           bounds=tuple((0.0, 1.0) for _ in range(self.n)),
                           constraints=({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0},
                                        {'type': 'eq', 'fun': lambda w: self.performance(w)[0] - tr}))
            if opt.success:
                vol = self.performance(opt.x)[1]
                rows.append({'Return (%)': tr * 100, 'Volatility (%)': vol * 100, 'Sharpe': (tr - self.rf) / vol})
        return pd.DataFrame(rows)
