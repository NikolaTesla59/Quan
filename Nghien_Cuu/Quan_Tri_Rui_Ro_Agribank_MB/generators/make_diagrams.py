import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs(r'C:\Users\Admin\.gemini\antigravity\scratch\diagrams', exist_ok=True)

# ------------------------------------------------------------------------------
# DIAGRAM 1: 3-TIER PROVISIONING FRAMEWORK
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6.2), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title Box
title_box = patches.FancyBboxPatch((5, 87), 90, 10, boxstyle="round,pad=1.5", 
                                   fc="#002060", ec="#001845", lw=1.5)
ax.add_patch(title_box)
ax.text(50, 92, "MÔ HÌNH 3 TẦNG KHOẢN MỤC DỰ PHÒNG HẤP THỤ RỦI RO QUY HOẠCH ĐỘT XUẤT", 
        color="white", fontsize=11, fontweight="bold", ha="center", va="center")

# Central Risk Box
risk_box = patches.FancyBboxPatch((15, 68), 70, 12, boxstyle="round,pad=1", 
                                  fc="#FFF1F0", ec="#CF1322", lw=2, linestyle="--")
ax.add_patch(risk_box)
ax.text(50, 75.5, "RỦI RO QUY HOẠCH / GIẢI TỎA THẦN TỐC (UNFORESEEN EVENT RISK)", 
        color="#CF1322", fontsize=10.5, fontweight="bold", ha="center", va="center")
ax.text(50, 71, "Không có dữ liệu quy hoạch trước - Bất động sản thế chấp đột ngột bị thu hồi đất khẩn cấp", 
        color="#595959", fontsize=8.5, fontstyle="italic", ha="center", va="center")

# Arrow downwards
ax.annotate('', xy=(50, 63), xytext=(50, 68),
            arrowprops=dict(facecolor='#002060', edgecolor='#002060', width=2, headwidth=8))

# 3 Tier Boxes
tier_data = [
    (5, "TẦNG 1: DỰ PHÒNG CHUNG (0,75%)", 
     "Khoản mục Chi phí Hoạt động (P&L) - Thông tư 11/2021/TT-NHNN",
     "• Bản chất: Dự phòng cho các tổn thất 'chưa xác định được'.\n• Quy mô: 0,75% dư nợ Nhóm 1-4 (Agribank/MB đạt 10.000–15.000 tỷ).\n• Chức năng: Túi đệm luật định bảo hiểm cho các cú sốc bất khả kháng.",
     "#E6F7FF", "#1890FF", "#0050B3"),
     
    (36, "TẦNG 2: MANAGEMENT OVERLAY (IFRS 9)", 
     "Khoản mục Dự phòng Bổ sung sau Mô hình (PMA) - IFRS 9 ECL",
     "• Bản chất: Bù đắp điểm mù của mô hình thống kê trước quyết sách chính trị.\n• Cơ chế: Ban Điều hành chủ động trích lập khoản mục bổ sung vào P&L.\n• Kích hoạt: Đẩy khoản vay vào Stage 2 (SICR) với LGD thực tế tăng vọt.",
     "#F6FFED", "#52C41A", "#237804"),
     
    (67, "TẦNG 3: QUỸ DỰ PHÒNG TÀI CHÍNH & VỐN CAR", 
     "Khoản mục Vốn Chủ Sở Hữu (Equity Buffer) - Luật TCTD & Basel II",
     "• Bản chất: Đệm hấp thụ tổn thất vượt quá khả năng của chi phí dự phòng.\n• Quỹ dự phòng tài chính: Trích 10% LNST hàng năm (Nghị định 93/2017).\n• Đệm Vốn kinh tế (CAR 10-11%): Đảm bảo ngân hàng không sụp đổ khi lỗ lớn.",
     "#FFF7E6", "#FA8C16", "#AD4E00")
]

for y_pos, title, sub, desc, bg, border, title_c in tier_data:
    box = patches.FancyBboxPatch((6, 58 - y_pos), 88, 16, boxstyle="round,pad=1", 
                                 fc=bg, ec=border, lw=1.8)
    ax.add_patch(box)
    ax.text(8, 71 - y_pos, title, color=title_c, fontsize=10, fontweight="bold", va="center")
    ax.text(8, 67 - y_pos, sub, color="#595959", fontsize=8, fontstyle="italic", va="center")
    ax.text(8, 61 - y_pos, desc, color="#262626", fontsize=8, va="center", linespacing=1.35)

plt.tight_layout()
p1 = r'C:\Users\Admin\.gemini\antigravity\scratch\diagrams\So_do_1_Ba_tang_khoan_muc_du_phong.png'
plt.savefig(p1, bbox_inches='tight', dpi=300)
plt.close()
print("Saved Diagram 1:", p1)

# ------------------------------------------------------------------------------
# DIAGRAM 2: 4-STEP BANK ACTION WORKFLOW
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6.2), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title Box
title_box = patches.FancyBboxPatch((5, 87), 90, 10, boxstyle="round,pad=1.5", 
                                   fc="#002060", ec="#001845", lw=1.5)
ax.add_patch(title_box)
ax.text(50, 92, "QUY TRÌNH 4 BƯỚC ỨNG PHÓ KẾ TOÁN & PHÁP LÝ KHI BỊ 'ĐÁNH ÚP' QUY HOẠCH", 
        color="white", fontsize=11, fontweight="bold", ha="center", va="center")

steps = [
    (15, "BƯỚC 1: CÁCH LY & GIÁM SÁT", 
     "Khảo sát chủ trương / Hướng tuyến",
     "• Đưa ngay khoản vay vào danh sách Watchlist (Giám sát đặc biệt).\n• Đo lường tổng dư nợ và giá trị TSBĐ nằm trong hành lang dự án.",
     "#E6F7FF", "#1890FF", "#0050B3"),
     
    (36, "BƯỚC 2: TÁI ĐỊNH GIÁ & TRÍCH LẬP", 
     "Hạ giá trị khấu trừ C theo TT11 / IFRS 9",
     "• Hạ giá định giá về bằng giá bồi thường GPMB dự kiến (V_GPMB).\n• Ép giá trị khấu trừ C sụt giảm -> Trích đủ Dự phòng cụ thể đón đầu.",
     "#FFF1F0", "#FF4D4F", "#A8071A"),
     
    (57, "BƯỚC 3: RÀNG BUỘC HỢP ĐỒNG", 
     "Kích hoạt Covenants & Event of Default",
     "• Coi việc dính giải tỏa là vi phạm nghĩa vụ hợp đồng thế chấp.\n• Buộc khách hàng nộp TSBĐ bổ sung trong 15-30 ngày hoặc trả bớt gốc.",
     "#FFFBE6", "#FAAD14", "#D48806"),
     
    (78, "BƯỚC 4: THU HỒI & XÓA NỢ NỘI BẢNG", 
     "Phong tỏa bồi thường & Xử lý phần hụt",
     "• Đăng ký quyền ưu tiên thanh toán, nhận tiền bồi thường từ Ban GPMB.\n• Phần nợ thiếu hụt: Dùng Quỹ dự phòng rủi ro xóa nợ nội bảng (Write-off).",
     "#F6FFED", "#52C41A", "#237804")
]

for idx, (x_center, title, sub, desc, bg, border, title_c) in enumerate(steps):
    box = patches.FancyBboxPatch((5, 80 - (idx * 17.5)), 90, 14, boxstyle="round,pad=1", 
                                 fc=bg, ec=border, lw=1.8)
    ax.add_patch(box)
    ax.text(8, 89 - (idx * 17.5), title, color=title_c, fontsize=9.5, fontweight="bold", va="center")
    ax.text(45, 89 - (idx * 17.5), f"[{sub}]", color="#595959", fontsize=8.5, fontstyle="italic", va="center")
    ax.text(8, 82.5 - (idx * 17.5), desc, color="#262626", fontsize=8, va="center", linespacing=1.35)
    
    # Arrow downwards between boxes
    if idx < 3:
        ax.annotate('', xy=(50, 79.5 - (idx * 17.5)), xytext=(50, 80.5 - (idx * 17.5)),
                    arrowprops=dict(facecolor='#002060', edgecolor='#002060', width=1.5, headwidth=5))

plt.tight_layout()
p2 = r'C:\Users\Admin\.gemini\antigravity\scratch\diagrams\So_do_2_Quy_trinh_ung_pho_ngan_hang.png'
plt.savefig(p2, bbox_inches='tight', dpi=300)
plt.close()
print("Saved Diagram 2:", p2)
