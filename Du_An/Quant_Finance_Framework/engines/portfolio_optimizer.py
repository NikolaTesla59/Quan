import numpy as np
import pandas as pd
from scipy.optimize import minimize

class PortfolioOptimizer:
    """
    Quantitative Portfolio Optimization Engine:
    - Markowitz Mean-Variance Efficient Frontier
    - Maximum Sharpe Ratio
    - Minimum Volatility (Global Minimum Variance - GMV)
    - Equal Risk Parity (Inverse Volatility / Risk Budgeting)
    """
    def __init__(self, expected_returns: np.ndarray, cov_matrix: np.ndarray, asset_names: list[str], risk_free_rate: float = 0.045):
        self.mu = np.array(expected_returns)
        self.cov = np.array(cov_matrix)
        self.assets = asset_names
        self.rf = risk_free_rate
        self.n = len(asset_names)

    def portfolio_performance(self, weights: np.ndarray) -> tuple[float, float, float]:
        """Calculates expected return, volatility, and Sharpe ratio."""
        weights = np.array(weights)
        p_ret = float(np.sum(self.mu * weights))
        p_vol = float(np.sqrt(np.dot(weights.T, np.dot(self.cov, weights))))
        sharpe = (p_ret - self.rf) / p_vol if p_vol > 1e-7 else 0.0
        return p_ret, p_vol, sharpe

    def max_sharpe_portfolio(self) -> dict:
        """Finds portfolio weights that maximize the Sharpe ratio."""
        def neg_sharpe(w):
            r, v, s = self.portfolio_performance(w)
            return -s

        constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0})
        bounds = tuple((0.0, 1.0) for _ in range(self.n))
        init_guess = np.ones(self.n) / self.n

        opt = minimize(neg_sharpe, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        weights = np.round(opt.x, 4)
        r, v, s = self.portfolio_performance(weights)
        return {
            'weights': dict(zip(self.assets, weights.tolist())),
            'expected_return': round(r, 4),
            'volatility': round(v, 4),
            'sharpe_ratio': round(s, 4)
        }

    def min_variance_portfolio(self) -> dict:
        """Finds portfolio weights that minimize portfolio volatility."""
        def port_vol(w):
            return self.portfolio_performance(w)[1]

        constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0})
        bounds = tuple((0.0, 1.0) for _ in range(self.n))
        init_guess = np.ones(self.n) / self.n

        opt = minimize(port_vol, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        weights = np.round(opt.x, 4)
        r, v, s = self.portfolio_performance(weights)
        return {
            'weights': dict(zip(self.assets, weights.tolist())),
            'expected_return': round(r, 4),
            'volatility': round(v, 4),
            'sharpe_ratio': round(s, 4)
        }

    def risk_parity_portfolio(self) -> dict:
        """Equal Risk Contribution (Risk Parity)."""
        def risk_budget_obj(w):
            w = np.array(w)
            sig = np.sqrt(np.dot(w.T, np.dot(self.cov, w)))
            if sig < 1e-8:
                return 0.0
            # Marginal Risk Contribution
            mrc = np.dot(self.cov, w) / sig
            # Risk Contribution per asset
            rc = w * mrc
            target_rc = sig / self.n
            return np.sum((rc - target_rc) ** 2)

        constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0})
        bounds = tuple((0.01, 1.0) for _ in range(self.n))
        init_guess = np.ones(self.n) / self.n

        opt = minimize(risk_budget_obj, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        weights = np.round(opt.x / np.sum(opt.x), 4)
        r, v, s = self.portfolio_performance(weights)
        return {
            'weights': dict(zip(self.assets, weights.tolist())),
            'expected_return': round(r, 4),
            'volatility': round(v, 4),
            'sharpe_ratio': round(s, 4)
        }

    def generate_efficient_frontier(self, n_points: int = 50) -> pd.DataFrame:
        """Computes points along the Efficient Frontier curve."""
        min_v = self.min_variance_portfolio()['expected_return']
        max_r = float(np.max(self.mu))
        target_returns = np.linspace(min_v, max_r, n_points)

        frontier = []
        for tr in target_returns:
            def port_vol(w):
                return self.portfolio_performance(w)[1]

            constraints = (
                {'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0},
                {'type': 'eq', 'fun': lambda w: self.portfolio_performance(w)[0] - tr}
            )
            bounds = tuple((0.0, 1.0) for _ in range(self.n))
            init_guess = np.ones(self.n) / self.n
            opt = minimize(port_vol, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
            if opt.success:
                vol = self.portfolio_performance(opt.x)[1]
                frontier.append({'Return': tr, 'Volatility': vol, 'Sharpe': (tr - self.rf) / vol})

        return pd.DataFrame(frontier)
