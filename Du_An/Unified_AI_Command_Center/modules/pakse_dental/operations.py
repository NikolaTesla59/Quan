import numpy as np
import pandas as pd

class PakseOperationsEngine:
    """Quản trị Thiết bị Y tế, Khấu hao & Lượng đặt hàng Kinh tế (EOQ)."""
    def __init__(self):
        self.equipment = [
            {"name": "Máy CT ConeBeam 3D Panorama toàn cảnh", "cost": 1_250_000_000, "years": 5, "salvage": 100_000_000},
            {"name": "03 Hệ thống ghế điều trị nha khoa Ajax", "cost": 390_000_000, "years": 5, "salvage": 30_000_000},
            {"name": "Hệ thống trạm vô trùng Châu Âu Class B", "cost": 180_000_000, "years": 5, "salvage": 10_000_000},
            {"name": "Phòng chì 2mm & Hạ tầng kỹ thuật ngầm", "cost": 450_000_000, "years": 3, "salvage": 0},
            {"name": "Bộ dụng cụ phẫu thuật & cấy ghép Implant", "cost": 220_000_000, "years": 3, "salvage": 0}
        ]

    def depreciation_table(self) -> pd.DataFrame:
        rows = []
        for eq in self.equipment:
            annual = (eq["cost"] - eq["salvage"]) / eq["years"]
            rows.append({
                "Hạng mục thiết bị": eq["name"],
                "Nguyên giá (VNĐ)": f"{eq['cost']:,.0f}",
                "Thời gian (Năm)": eq["years"],
                "Khấu hao Năm (VNĐ)": f"{annual:,.0f}",
                "Khấu hao Tháng (VNĐ)": f"{annual/12:,.0f}"
            })
        return pd.DataFrame(rows)

    def calculate_eoq(self, annual_demand: int = 600, order_cost: float = 3_000_000, unit_price: float = 2_500_000) -> dict:
        holding_cost = unit_price * 0.15
        eoq = np.sqrt((2 * annual_demand * order_cost) / holding_cost)
        orders = annual_demand / eoq
        return {
            "Lượng đặt hàng tối ưu (EOQ)": f"{int(round(eoq))} trụ/đợt",
            "Số lần nhập hàng/năm": f"{orders:.1f} đợt",
            "Chu kỳ nhập hàng": f"Cứ sau ~{int(round(365.0/orders))} ngày",
            "Chi phí lưu kho tối thiểu": f"{holding_cost * (eoq/2):,.0f} VNĐ/năm"
        }
