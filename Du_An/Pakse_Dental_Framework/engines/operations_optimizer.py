import pandas as pd
import numpy as np

class ClinicOperationsOptimizer:
    """
    Bộ Công Cụ Quản Trị Vận Hành Nha Khoa:
    - Quản lý định mức vật tư tiêu hao (Labo sứ, Trụ Implant, Thuốc tê, Composite)
    - Tối ưu hóa chu kỳ nhập hàng xuyên biên giới Việt Nam - Lào (EOQ Model)
    - Lịch trình khấu hao thiết bị y tế (Máy CT ConeBeam 3D, 03 Ghế nha Ajax)
    - Dự báo đệm an toàn vốn lưu động (Safety Cash Buffer)
    """
    def __init__(self):
        # Danh mục thiết bị chính đầu tư ban đầu
        self.assets = [
            {"name": "Máy CT ConeBeam 3D Panorama toàn cảnh", "cost_vnd": 1_250_000_000, "lifespan_years": 5, "salvage_vnd": 100_000_000},
            {"name": "03 Hệ thống ghế điều trị nha khoa Ajax", "cost_vnd": 390_000_000, "lifespan_years": 5, "salvage_vnd": 30_000_000},
            {"name": "Hệ thống trạm vô trùng Châu Âu Class B", "cost_vnd": 180_000_000, "lifespan_years": 5, "salvage_vnd": 10_000_000},
            {"name": "Thi công chì 2mm, phòng khám, điện nước ngầm", "cost_vnd": 450_000_000, "lifespan_years": 3, "salvage_vnd": 0},
            {"name": "Bộ dụng cụ phẫu thuật & tiểu phẫu Implant", "cost_vnd": 220_000_000, "lifespan_years": 3, "salvage_vnd": 0}
        ]

    def calculate_depreciation_schedule(self) -> pd.DataFrame:
        """Tính toán bảng khấu hao đường thẳng hàng năm và hàng tháng."""
        records = []
        for a in self.assets:
            annual_dep = (a["cost_vnd"] - a["salvage_vnd"]) / a["lifespan_years"]
            monthly_dep = annual_dep / 12.0
            records.append({
                "Hạng mục thiết bị": a["name"],
                "Nguyên giá (VNĐ)": f"{a['cost_vnd']:,.0f}",
                "Thời gian KH (Năm)": a["lifespan_years"],
                "Khấu hao Năm (VNĐ)": f"{annual_dep:,.0f}",
                "Khấu hao Tháng (VNĐ)": f"{monthly_dep:,.0f}"
            })
        return pd.DataFrame(records)

    def optimize_inventory_eoq(self, annual_demand_units: int = 600, order_cost_vnd: float = 3_000_000, holding_cost_rate: float = 0.15, unit_cost_vnd: float = 2_500_000) -> dict:
        """
        Tính lượng đặt hàng kinh tế (EOQ) cho trụ Implant & Phôi sứ nhập từ Việt Nam sang Pakse:
        - Giảm thiểu chi phí vận chuyển cửa khẩu và tồn đọng vốn.
        """
        holding_cost_unit = unit_cost_vnd * holding_cost_rate
        # EOQ = sqrt( (2 * D * S) / H )
        eoq = np.sqrt((2 * annual_demand_units * order_cost_vnd) / holding_cost_unit)
        orders_per_year = annual_demand_units / eoq
        cycle_days = 365.0 / orders_per_year
        
        return {
            "Lượng đặt hàng tối ưu (EOQ)": f"{int(round(eoq))} đơn vị/đợt",
            "Số lần nhập hàng/năm": f"{orders_per_year:.1f} đợt/năm",
            "Chu kỳ nhập hàng lý tưởng": f"Cứ sau ~{int(round(cycle_days))} ngày",
            "Chi phí lưu kho tối thiểu/năm": f"{holding_cost_unit * (eoq / 2):,.0f} VNĐ"
        }

    def working_capital_analysis(self, monthly_revenue_vnd: float, cogs_rate: float = 0.20, fixed_opex_vnd: float = 345_330_000) -> dict:
        """Phân tích dòng tiền lưu động: Lợi thế đặt cọc 50-70% tự nuôi biến phí."""
        cogs = monthly_revenue_vnd * cogs_rate
        cash_in_advance = monthly_revenue_vnd * 0.60  # Trung bình cọc 60%
        working_capital_gap = (cogs + fixed_opex_vnd) - cash_in_advance
        status = "DƯ THỪA TIỀN MẶT LƯU ĐỘNG (Dòng tiền dương mạnh)" if working_capital_gap < 0 else "CẦN TÀI TRỢ LƯU ĐỘNG"

        return {
            "Doanh thu thuần": f"{monthly_revenue_vnd:,.0f} VNĐ",
            "Tiền cọc nhận trước (60%)": f"{cash_in_advance:,.0f} VNĐ",
            "Tổng chi phí trong tháng (COGS + OPEX)": f"{(cogs + fixed_opex_vnd):,.0f} VNĐ",
            "Độ lệch dòng tiền lưu động": f"{abs(working_capital_gap):,.0f} VNĐ",
            "Trạng thái thanh khoản": status
        }
