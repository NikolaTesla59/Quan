class PakseMarketingEngine:
    """Bộ tạo Nội dung Tiếp thị AI & Tri thức Thẩm định Đầu tư."""
    def __init__(self):
        self.due_diligence = {
            "Pháp lý tại Lào": "Vận hành song song mô hình liên doanh/bảo trợ chuyên môn bác sĩ Lào trong 1-2 tuần đầu để mở cửa thần tốc Tháng 11. Giấy phép doanh nghiệp WFOE 100% vốn nước ngoài được thẩm định nghiệm thu song song trong quá trình phòng khám vận hành ổn định.",
            "Lợi thế cạnh tranh với Thái Lan": "Tiết kiệm 120km vượt biên sang Ubon Ratchathani. Đưa máy CT ConeBeam 3D và Bác sĩ chuyên khoa sâu Việt Nam về phục vụ ngay trung tâm Pakse, giá rẻ hơn Thái Lan 20%-30%, chăm sóc và bảo hành tại chỗ.",
            "Cơ cấu cổ phần": "65% Cổ đông Tài chính (góp tiền mặt, nắm quyền duyệt kép chi tiêu >1.000 USD), 20% Nhóm Vận hành, 15% Bác sĩ Trưởng Chuyên môn (áp dụng cơ chế Vesting 3 năm: 5%/năm cam kết gắn bó)."
        }

    def generate_ad(self, service: str) -> dict:
        data = {
            "Trồng răng Implant CT 3D": {
                "headline": "TRỒNG RĂNG IMPLANT CHUẨN QUỐC TẾ TẠI PAKSE — KHÔNG CẦN SANG THÁI LAN!",
                "hook": "Tại sao phải tốn kém ăn ở, vượt 120km sang Ubon Ratchathani khi công nghệ CT ConeBeam 3D hàng đầu đã có mặt tại Pakse?",
                "body": (
                    "🦷 Phòng khám Nha khoa Quốc tế Pakse (Chợ Đào Hương):\n"
                    "• Chụp phim khảo sát xương hàm 3D tại chỗ, định vị trụ chuẩn xác 100%.\n"
                    "• Bác sĩ chuyên khoa sâu trực tiếp phẫu thuật nhẹ nhàng, không đau.\n"
                    "• Trụ Implant chính hãng Châu Âu, bảo hành trọn đời.\n"
                    "• Tiết kiệm hơn 30% chi phí so với các bệnh viện tại Thái Lan!"
                ),
                "cta": "👉 ĐẶT LỊCH NGAY: Tặng suất chụp CT ConeBeam 3D miễn phí cho 50 khách hàng đầu tiên!"
            },
            "Răng sứ Thẩm mỹ Zirconia": {
                "headline": "NỤ CƯỜI ĐẲNG CẤP DOANH NHÂN — PHỤC HÌNH RĂNG SỨ NGUYÊN KHỐI TRONG 48H",
                "hook": "Nụ cười rạng rỡ mang lại may mắn và thành công trong kinh doanh. Đã đến lúc tạm biệt hàm răng xỉn màu!",
                "body": (
                    "💎 Thiết kế dáng cười phong thủy theo tỉ lệ vàng khuôn mặt.\n"
                    "💎 Phôi sứ Zirconia/Cercon chính hãng không mài nhỏ, không đen viền nướu.\n"
                    "💎 Độ trong tự nhiên và chịu lực gấp 5 lần răng thật."
                ),
                "cta": "Nhắn tin ngay để nhận voucher ưu đãi khai trương giảm 25% trọn gói nụ cười!"
            },
            "Nha khoa Tổng quát Gia đình": {
                "headline": "TRẠM VÔ TRÙNG CHÂU ÂU CLASS B — CHĂM SÓC RĂNG MIỆNG AN TOÀN TUYỆT ĐỐI",
                "hook": "Bảo vệ nụ cười khỏe mạnh cho cả gia đình bạn với quy trình kiểm soát nhiễm khuẩn nghiêm ngặt nhất.",
                "body": (
                    "👨‍👩‍👧‍👦 Dịch vụ nha khoa chuẩn mực ngay tại trung tâm Pakse:\n"
                    "• Nhổ răng khôn không đau bằng công nghệ sóng siêu âm Piezotome.\n"
                    "• Lấy cao răng êm ái, điều trị tủy và trám răng thẩm mỹ công nghệ cao.\n"
                    "• Đội ngũ y bác sĩ tận tâm, thấu hiểu bệnh nhân."
                ),
                "cta": "Liên hệ đặt lịch khám và tư vấn răng miệng hoàn toàn miễn phí ngay hôm nay!"
            }
        }
        return data.get(service, data["Trồng răng Implant CT 3D"])
