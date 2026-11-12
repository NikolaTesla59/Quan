import numpy as np
import pandas as pd

class PakseFinancialModel:
    """
    Mô Hình Tài Chính Động Cho Dự Án Phòng Khám Nha Khoa Quốc Tế Pakse (Champasak, Lào).
    Đồng bộ 100% với Mô hình Master & Báo cáo Khả thi $125.798 USD.
    """
    def __init__(
        self,
        capex_vnd: float = 3_255_970_000.0,      # ~$125,798 USD (Đã bao gồm 1 năm tiền nhà trả trước $6,000)
        fixed_opex_vnd: float = 345_330_000.0,    # Định phí hàng tháng: lương 8 nhân sự, điện nước, mkt $5,000
        cogs_rate: float = 0.20,                  # Biến phí (COGS: vật tư tiêu hao, labo sứ, implant) = 20%
        discount_rate: float = 0.12               # WACC / Lãi suất chiết khấu kỳ vọng = 12%
    ):
        self.capex = capex_vnd
        self.fixed_opex = fixed_opex_vnd
        self.cogs_rate = cogs_rate
        self.discount_rate = discount_rate

    def calculate_breakeven(self, working_days: int = 26) -> dict:
        """Tính toán điểm hòa vốn vận hành."""
        # Tại điểm hòa vốn: Doanh thu * (1 - COGS) = Định phí
        # => Doanh thu hòa vốn = Định phí / (1 - COGS)
        be_monthly = self.fixed_opex / (1.0 - self.cogs_rate)
        be_daily = be_monthly / working_days
        # Giả định giá trị trung bình 1 ca khám tổng hợp ~ 6.2 triệu VNĐ
        be_patients = be_daily / 6_200_000.0
        return {
            'monthly_revenue_vnd': round(be_monthly, 0),
            'daily_revenue_vnd': round(be_daily, 0),
            'patients_per_day': round(be_patients, 2)
        }

    def simulate_scenarios(self, working_days: int = 26) -> pd.DataFrame:
        """Mô phỏng 3 kịch bản doanh thu chuẩn: Thận trọng (80tr/ngày), Cơ sở (140tr/ngày), Kỳ vọng (200tr/ngày)."""
        scenarios = {
            'Kịch Bản 1: Thận Trọng': 80_000_000.0,
            'Kịch Bản 2: Cơ Sở (Kỳ vọng)': 140_000_000.0,
            'Kịch Bản 3: Đột Phá': 200_000_000.0
        }
        records = []
        for name, rev_day in scenarios.items():
            rev_month = rev_day * working_days
            cogs = rev_month * self.cogs_rate
            gross_profit = rev_month - cogs
            ebitda = gross_profit - self.fixed_opex
            ebitda_margin = (ebitda / rev_month) * 100.0
            
            # Thời gian hoàn vốn (Tháng) = CAPEX / EBITDA hàng tháng
            payback_months = self.capex / ebitda if ebitda > 0 else 999.0
            
            # Ước tính dòng tiền 3 năm (36 tháng) tính NPV & IRR
            cash_flows = [-self.capex] + [ebitda] * 36
            # NPV tính theo tháng
            monthly_r = (1.0 + self.discount_rate) ** (1.0 / 12.0) - 1.0
            npv = np.sum([cf / ((1.0 + monthly_r) ** t) for t, cf in enumerate(cash_flows)])

            records.append({
                'Kịch Bản': name,
                'Doanh thu Ngày (tr)': round(rev_day / 1e6, 1),
                'Doanh thu Tháng (tr)': round(rev_month / 1e6, 1),
                'Biến phí COGS (tr)': round(cogs / 1e6, 1),
                'Định phí OPEX (tr)': round(self.fixed_opex / 1e6, 1),
                'EBITDA Tháng (tr)': round(ebitda / 1e6, 1),
                'Biên EBITDA (%)': round(ebitda_margin, 1),
                'Thời gian hoàn vốn (Tháng)': round(payback_months, 1),
                'NPV 3 Năm (Tỷ VNĐ)': round(npv / 1e9, 2)
            })
        return pd.DataFrame(records)

    def custom_simulation(self, n_chairs: int, patients_per_chair: float, avg_ticket_vnd: float, working_days: int = 26) -> dict:
        """Mô phỏng tùy biến theo số ghế nha khoa và công suất khám."""
        total_patients_day = n_chairs * patients_per_chair
        rev_day = total_patients_day * avg_ticket_vnd
        rev_month = rev_day * working_days
        cogs = rev_month * self.cogs_rate
        gross_profit = rev_month - cogs
        ebitda = gross_profit - self.fixed_opex
        ebitda_margin = (ebitda / rev_month) * 100.0 if rev_month > 0 else 0.0
        payback = self.capex / ebitda if ebitda > 0 else 999.0

        return {
            'total_patients_day': round(total_patients_day, 1),
            'revenue_day_vnd': rev_day,
            'revenue_month_vnd': rev_month,
            'cogs_vnd': cogs,
            'ebitda_vnd': ebitda,
            'ebitda_margin': round(ebitda_margin, 2),
            'payback_months': round(payback, 2)
        }
