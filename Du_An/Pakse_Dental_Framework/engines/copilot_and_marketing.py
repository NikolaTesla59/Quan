class PakseCopilotAndMarketing:
    """
    Trợ lý Đầu tư & Bộ Tạo Nội Dung Quảng Cáo Tiếp Thị Nha Khoa Pakse:
    - Hồ sơ thẩm định gọi vốn (Due Diligence & Investor Pitch Q&A)
    - Tự động sinh bài quảng cáo, thông điệp truyền thông số (Facebook, TikTok, Biển bảng)
    """
    def __init__(self):
        self.qa_knowledge = {
            "Pháp lý tại Lào": "Dự án áp dụng mô hình liên doanh hoặc bảo trợ chuyên môn Bác sĩ Lào ngay trong 1-2 tuần đầu để mở cửa đón khách thần tốc trong Tháng 11. Giấy phép doanh nghiệp 100% vốn nước ngoài (WFOE) được nghiệm thu song song khi cơ sở đã vận hành ổn định.",
            "Lợi thế cạnh tranh so với Thái Lan": "Bệnh nhân Nam Lào hiện phải đi 120km sang Ubon Ratchathani (Thái Lan) rất tốn kém ăn ở và tái khám. Phòng khám đưa máy CT ConeBeam 3D và Bác sĩ chuyên khoa sâu Việt Nam về ngay Chợ Đào Hương Pakse, giá rẻ hơn Thái Lan 20% - 30%, bảo hành tại chỗ.",
            "Cơ cấu cổ phần & Quyền kiểm soát": "65% Cổ đông Tài chính (nắm quyền kiểm soát chi tiêu và phê duyệt kép giao dịch >1.000 USD), 20% Nhóm Vận hành & Sáng lập, 15% Bác sĩ Trưởng Chuyên môn (áp dụng cơ chế Vesting 3 năm: 5%/năm cam kết gắn bó).",
            "Thời gian hoàn vốn": "Nhờ tiền nhà 1 năm trả trước đã tính vào CAPEX và biến phí COGS được tự nuôi bằng tiền cọc bệnh nhân (50-70%), thời gian hoàn vốn thực tế chỉ từ 3 đến 6 tháng."
        }

    def get_investor_answer(self, topic: str) -> str:
        """Trả lời chất vấn nhà đầu tư theo chuẩn hồ sơ Master."""
        return self.qa_knowledge.get(topic, "Nội dung đang được cập nhật trong phụ lục hợp đồng.")

    def generate_ad_campaign(self, service_type: str, target_audience: str) -> dict:
        """Tự động sinh kịch bản quảng cáo và thông điệp tiếp thị."""
        campaigns = {
            "Trồng răng Implant (CT ConeBeam 3D)": {
                "headline": "TRỒNG RĂNG IMPLANT CHUẨN QUỐC TẾ NGAY TẠI PAKSE — KHÔNG CẦN VƯỢT BIÊN SANG THÁI LAN!",
                "hook": "Tại sao phải mất cả ngày đi 120km sang Ubon Ratchathani khi công nghệ chụp phim CT ConeBeam 3D hiện đại nhất thế giới đã có mặt tại Pakse?",
                "body": (
                    "🦷 Phòng khám Nha khoa Quốc tế Pakse (Trục No.13 Chợ Đào Hương) chính thức mang đến giải pháp phục hình răng hoàn hảo:\n"
                    "✅ Bác sĩ chuyên khoa sâu đầu ngành trực tiếp phẫu thuật.\n"
                    "✅ Trụ Implant chính hãng nhập khẩu Châu Âu, tương thích sinh học 100%.\n"
                    "✅ Chụp phim khảo sát xương 3 chiều tại chỗ — Chính xác tuyệt đối, không đau.\n"
                    "✅ Tiết kiệm hơn 30% chi phí so với làm tại bệnh viện Thái Lan, bảo hành trọn đời tại Pakse!"
                ),
                "cta": "👉 ĐẶT LỊCH KHÁM NGAY HÔM NAY: Miễn phí chụp phim CT ConeBeam 3D cho 50 khách hàng đầu tiên! Hotline: [Số điện thoại]"
            },
            "Răng sứ thẩm mỹ cao cấp (Zirconia/Cercon)": {
                "headline": "NỤ CƯỜI ĐẲNG CẤP DOANH NHÂN — RĂNG SỨ NGUYÊN KHỐI CHÂU ÂU CHỈ SAU 48H",
                "hook": "Răng xỉn màu, khấp khểnh khiến bạn thiếu tự tin khi giao tiếp kinh doanh? Đã đến lúc nâng tầm nụ cười với công nghệ răng sứ thẩm mỹ không mài nhỏ!",
                "body": (
                    "✨ Thiết kế dáng cười phong thủy theo tỉ lệ vàng khuôn mặt:\n"
                    "💎 Phôi sứ Zirconia/Cercon tinh khiết, độ cứng gấp 5 lần răng thật.\n"
                    "💎 Không đen viền nướu, không ê buốt, màu sắc trong bóng tự nhiên.\n"
                    "💎 Xưởng Labo kỹ thuật số chuẩn xác từng micromet."
                ),
                "cta": "Inbox ngay nhận bảng giá ưu đãi khai trương giảm 25% trọn gói nụ cười!"
            },
            "Nha khoa gia đình & Chăm sóc tổng quát": {
                "headline": "CHĂM SÓC RĂNG MIỆNG TOÀN DIỆN CHO CẢ GIA ĐÌNH TẠI TRUNG TÂM PAKSE",
                "hook": "Hệ thống trạm vô trùng Châu Âu Class B tuyệt đối an toàn — Trải nghiệm nhổ răng khôn không đau và lấy cao răng êm ái.",
                "body": (
                    "👨‍👩‍👧‍👦 Dành trọn sự an tâm cho gia đình bạn:\n"
                    "🛡️ Quy trình vô khuẩn 1 chiều chống lây nhiễm chéo tuyệt đối.\n"
                    "🛡️ Không gian phòng khám sang trọng, máy móc nhập khẩu nguyên chiếc.\n"
                    "🛡️ Đội ngũ y bác sĩ tận tâm, thấu hiểu bệnh nhân."
                ),
                "cta": "Liên hệ ngay để nhận thẻ thành viên Dental VIP chăm sóc răng miệng trọn đời cho cả gia đình!"
            }
        }
        return campaigns.get(service_type, campaigns["Trồng răng Implant (CT ConeBeam 3D)"])
