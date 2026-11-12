import numpy as np
import pandas as pd

class PakseFinancialEngine:
    """Mô hình Tài chính Động & Điểm Hòa Vốn Dự án Nha Khoa Quốc Tế Pakse."""
    def __init__(self, capex: float = 3_255_970_000.0, monthly_opex: float = 345_330_000.0, cogs_rate: float = 0.20):
        self.capex = capex
        self.fixed_opex = monthly_opex
        self.cogs_rate = cogs_rate

    def get_breakeven(self, days: int = 26) -> dict:
        rev_month = self.fixed_opex / (1.0 - self.cogs_rate)
        rev_day = rev_month / days
        patients = rev_day / 6_200_000.0
        return {
            'monthly_rev': rev_month,
            'daily_rev': rev_day,
            'patients_day': round(patients, 2)
        }

    def simulate(self, chairs: int, patients_per_chair: float, avg_ticket: float, days: int = 26) -> dict:
        total_patients = chairs * patients_per_chair
        rev_day = total_patients * avg_ticket
        rev_month = rev_day * days
        cogs = rev_month * self.cogs_rate
        ebitda = (rev_month - cogs) - self.fixed_opex
        margin = (ebitda / rev_month) * 100.0 if rev_month > 0 else 0.0
        payback = self.capex / ebitda if ebitda > 0 else 999.0
        return {
            'total_patients': round(total_patients, 1),
            'rev_day': rev_day,
            'rev_month': rev_month,
            'cogs': cogs,
            'ebitda': ebitda,
            'margin': round(margin, 1),
            'payback': round(payback, 1)
        }

    def scenario_table(self, days: int = 26) -> pd.DataFrame:
        scenarios = {
            'Thận Trọng': 80_000_000.0,
            'Cơ Sở (Kỳ vọng)': 140_000_000.0,
            'Đột Phá': 200_000_000.0
        }
        rows = []
        for name, r_day in scenarios.items():
            r_mo = r_day * days
            ebitda = (r_mo * (1.0 - self.cogs_rate)) - self.fixed_opex
            payback = self.capex / ebitda if ebitda > 0 else 999.0
            rows.append({
                'Kịch bản': name,
                'Doanh thu/Ngày (tr)': round(r_day / 1e6, 1),
                'Doanh thu/Tháng (tr)': round(r_mo / 1e6, 1),
                'EBITDA/Tháng (tr)': round(ebitda / 1e6, 1),
                'Biên EBITDA (%)': round((ebitda/r_mo)*100, 1),
                'Hoàn vốn (Tháng)': round(payback, 1)
            })
        return pd.DataFrame(rows)
