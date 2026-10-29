# BẢN ĐÁNH GIÁ & PHẢN BIỆN HỌC THUẬT CHUYÊN SÂU
## (ACADEMIC PEER-REVIEW REPORT FOR MASTER / PH.D. LEVEL)

**Đề tài**: *So sánh mô hình và thực trạng quản trị rủi ro tín dụng giữa Ngân hàng Nông nghiệp và Phát triển Nông thôn Việt Nam (Agribank) và Ngân hàng TMCP Quân đội (MB) giai đoạn 2020–2025.*  
**Đối tượng thẩm định**:
1. Báo cáo nghiên cứu Word: `Tieu_luan_Agribank_MB_2020-2025_hoan_thien_v2.docx` (180 đoạn văn, 10 bảng tổng hợp, 14 trang).
2. Mô hình định lượng Excel: `Phan_tich_RRTD_Agribank_MB_2020-2025_v2.xlsx` (6 sheet, 261 công thức động).
3. Danh mục hồ sơ đối chiếu: `Danh_muc_tai_lieu_can_lay_Agribank_MB.xlsx` (18 file BCTC/BCTN gốc, 11 thuyết minh).

---

### TỔNG QUAN XẾP HẠNG VÀ KẾT LUẬN THẨM ĐỊNH (BLUF)

> **Xếp hạng hiện tại**: **XUẤT SẮC Ở CẤP ĐỘ CỬ NHÂN / ĐẠT YÊU CẦU CẤP ĐỘ THẠC SĨ ỨNG DỤNG (EXECUTIVE MASTER / MBA).**  
> **Khoảng cách so với chuẩn Thạc sĩ Nghiên cứu (M.Sc) & Nghiên cứu sinh Tiến sĩ (Ph.D.)**: **CÒN THIẾU 3 TRỤ CỘT HỌC THUẬT NỀN TẢNG:**
> 1. *Khung lý thuyết nền tảng (Theoretical Foundations)*: Bài viết chưa neo vào các lý thuyết kinh tế tài chính kinh điển (Information Asymmetry, Agency Theory, Basel IRB Framework, IFRS 9 ECL Model).
> 2. *Phương pháp luận định lượng & Kiểm định nhân quả (Quantitative / Econometric Rigor)*: Dữ liệu hiện tại thuần túy là thống kê mô tả (Descriptive Statistics) và phân tích tỷ số tài chính (Financial Ratios), chưa có mô hình hồi quy kinh tế lượng, kiểm định căng thẳng vĩ mô (Stress Testing) hay mô phỏng rủi ro vỡ nợ (Default Risk Simulation).
> 3. *Đào sâu thể chế và phân tích pháp y kế toán (Institutional Governance & Forensic Accounting)*: Dù đã bóc tách được các hiện tượng bề mặt (nợ nhóm 2, xóa nợ, TPDN), nhưng chưa khái quát hóa thành các cơ chế "Khoan dung pháp lý" (Regulatory Forbearance), "Quản trị lợi nhuận qua dự phòng" (Earnings Management via Cookie Jar Reserves), và "Xung đột hàm mục tiêu giữa NHTM Nhà nước và NHTMCP".

```
+---------------------------------------------------------------------------------------------------+
|                         MA TRẬN ĐÁNH GIÁ MỨC ĐỘ TRƯỞNG THÀNH HỌC THUẬT                            |
+--------------------------+---------------------+-----------------------+--------------------------+
| Tiêu chí thẩm định       | Chuẩn Cử nhân (BA)  | Bản thảo hiện tại     | Chuẩn ThS / TS (NEU)     |
+--------------------------+---------------------+-----------------------+--------------------------+
| 1. Dữ liệu & Đối soát    | Trích dẫn thứ cấp   | Vượt trội (BCTC gốc)  | Đạt chuẩn ThS            |
| 2. Cơ sở lý thuyết       | Khái niệm cơ bản    | Đạt mức cơ bản (Ch.1) | THIẾU (Chưa có mô hình)  |
| 3. Phương pháp nghiên cứu| Thống kê mô tả      | Phân tích chỉ số      | THIẾU (Chưa có Econometric|
| 4. Bóc tách cơ chế số liệu| Nhận xét tăng/giảm  | Rất tốt (Forensic)    | Đạt khá cấp ThS          |
| 5. Phân tích Case Study  | Kể lại vụ án        | Khá (rút ra bài học)  | THIẾU (Chưa gắn COSO/IIA)|
| 6. Đánh giá & Hàm ý CS   | Khuyến nghị chung   | Sắc bén, đa chiều     | Cần cụ thể hóa kỹ thuật  |
+--------------------------+---------------------+-----------------------+--------------------------+
```

---

### PHẦN I. THẨM ĐỊNH BỘ DỮ LIỆU & MÔ HÌNH ĐỊNH LƯỢNG EXCEL

#### 1. Ưu điểm nổi bật (Đã đạt chuẩn chuyên viên phân tích tài chính cao cấp - Senior Banking Analyst)
* **Tính đồng bộ và toàn vẹn dữ liệu**: Mô hình Excel đã xử lý trọn vẹn chuỗi thời gian 6 năm (2020–2025) cho cả hai ngân hàng, liên kết chéo giữa `Du_lieu` và `Chi_tieu` qua 261 công thức tự động, triệt tiêu hoàn toàn lỗi kỹ thuật `#REF!`, `#N/A`, `#VALUE!`.
* **Kỹ thuật bóc tách pháp y kế toán (Forensic Accounting)**:
  - Nhận diện và giải quyết chính xác sự khác biệt giữa các chuỗi số liệu NPL của Agribank (chuỗi BCTC hợp nhất ban đầu vs. BCTC riêng lẻ điều chỉnh theo khuyến nghị Kiểm toán Nhà nước).
  - Phân tách bản chất số dư Trái phiếu doanh nghiệp của MB (66.279 tỷ đồng tổng chứng khoán nợ TCKT vs 47.100 tỷ đồng TPDN lĩnh vực Bất động sản và Năng lượng tái tạo).
  - Bóc tách chi phí tín dụng gộp ($Gross\ Credit\ Cost$) của MB năm 2023 đạt 2,03% sau khi cộng ngược 4.800 tỷ đồng hoàn nhập dự phòng nợ cơ cấu Covid-19, thay vì chỉ nhìn con số chi phí ròng 1,24% trên bề mặt báo cáo kết quả kinh doanh.
  - Phân tích độ lệch NPL do hợp nhất công ty tài chính tiêu dùng MCredit (đóng góp 0,16 – 0,22 điểm % vào NPL toàn tập đoàn MB).

#### 2. Các khoảng trống định lượng cần nâng cấp để đạt chuẩn Thạc sĩ Nghiên cứu / Tiến sĩ
* **Khoảng trống 1: Thiếu Mô hình Kiểm tra Căng thẳng Vĩ mô (Macroeconomic Stress Testing)**:
  - Ở cấp độ ThS/TS ngành Tài chính - Ngân hàng tại NEU, hội đồng luôn yêu cầu: *Nếu năm 2026 tăng trưởng GDP suy giảm về mức 5,0%, lãi suất liên ngân hàng tăng 200 điểm cơ bản (bps), hoặc thị trường bất động sản đóng băng thêm 1 chu kỳ, thì tỷ lệ nợ xấu, nợ nhóm 2, chi phí dự phòng bổ sung và CAR của Agribank và MB sẽ biến động như thế nào?*
  - Hiện tại, file Excel mới chỉ có phân tích độ nhạy đơn biến (1D Sensitivity) đối với việc lựa chọn chuỗi số liệu NPL của Agribank, hoàn toàn thiếu vắng **Mô phỏng kịch bản đa biến (Baseline, Adverse, Severe Scenarios)** theo hướng dẫn của Basel II/III (Pillar 2 - ICAAP).
* **Khoảng trống 2: Thiếu Mô hình Định lượng Đo lường Rủi ro Tín dụng Hiện đại (Credit Risk Modeling)**:
  - Bài viết sử dụng thuần túy các chỉ tiêu hồi tố (Lagging Indicators: NPL, nợ nhóm 2, nợ đã xóa). 
  - Chuẩn mực học thuật cao học yêu cầu tiếp cận chỉ tiêu dự báo tương lai (Forward-looking Indicators) hoặc ước lượng các tham số rủi ro:
    $$\text{Expected Loss (EL)} = \text{PD} \times \text{LGD} \times \text{EAD}$$
  - Đánh giá chênh lệch giữa chuẩn mực kế toán Việt Nam (VAS / Thông tư 11 - mô hình tổn thất đã phát sinh *Incurred Loss*) với Chuẩn mực Báo cáo Tài chính Quốc tế IFRS 9 (mô hình tổn thất tín dụng kỳ vọng *Expected Credit Loss - ECL* qua 3 giai đoạn: Stage 1, Stage 2, Stage 3).
* **Khoảng trống 3: Thiếu Đo lường Hiệu quả Tài chính có Điều chỉnh Rủi ro (RAROC)**:
  - Cả hai ngân hàng đều tăng trưởng tín dụng mạnh trong giai đoạn 2020–2025 (Agribank tăng bình quân 10–14%/năm, MB tăng bùng nổ 25–39%/năm). Tuy nhiên, bài viết chưa tính toán chỉ số **RAROC (Risk-Adjusted Return on Capital)**:
    $$\text{RAROC} = \frac{\text{Lợi nhuận ròng} - \text{Tổn thất dự kiến (EL)}}{\text{Vốn kinh tế (Economic Capital)}}$$
  - Thiếu RAROC khiến bài so sánh chưa trả lời được câu hỏi mang tính bản chất: *Liệu lợi nhuận kỷ lục của MB giai đoạn 2021–2022 có thực sự tạo ra giá trị kinh tế thặng dư sau khi đã trừ đi chi phí vốn rủi ro, hay chỉ là sự vay mượn lợi nhuận tương lai thông qua việc chấp nhận rủi ro danh mục quá mức?*

---

### PHẦN II. PHẢN BIỆN CHUYÊN SÂU BẢN BÁO CÁO WORD THEO TỪNG CHƯƠNG

#### CHƯƠNG 1. CƠ SỞ LÝ THUYẾT, PHÁP LÝ VÀ THỰC TRẠNG CHUNG
* **Nhận xét hiện trạng**: Tác giả đã tổng hợp rất tốt khung pháp lý điều chỉnh (Bảng 1 đối chiếu Thông tư 02, Thông tư 11, Thông tư 41, Nghị quyết 42). Tuy nhiên, **Chương 1 hiện tại mang tính chất "tài liệu ôn tập pháp luật" hơn là "khung lý thuyết học thuật"**.
* **Lỗ hổng học thuật cấp ThS/TS**:
  - *Hoàn toàn vắng bóng các lý thuyết tài chính kinh điển*: Cần đưa vào:
    1. **Lý thuyết Bất cân xứng thông tin (Information Asymmetry Theory - Stiglitz & Weiss, 1981)**: Giải thích hiện tượng hạn chế tín dụng (Credit Rationing), nghịch tuyển (Adverse Selection) và rủi ro đạo đức (Moral Hazard) khi ngân hàng nới lỏng điều kiện giải ngân.
    2. **Lý thuyết Người đại diện (Agency Theory - Jensen & Meckling, 1976)**: Giải thích sự phân kỳ trong hành vi quản trị rủi ro giữa Ban điều hành Agribank (đại diện cho chủ sở hữu Nhà nước, ngại rủi ro pháp lý, ưu tiên bảo toàn vốn) so với Ban điều hành MB (đại diện cho cổ đông tư nhân và quỹ đầu tư, chịu áp lực chỉ tiêu ROE, P/B và giá cổ phiếu).
    3. **Khung Hiệp ước Vốn Basel (Basel II & Basel III Core Principles)**: Làm rõ 3 trụ cột (Pillar 1: Yêu cầu vốn tối thiểu với phương pháp chuẩn hóa SA vs phương pháp xếp hạng nội bộ IRB; Pillar 2: Quy trình đánh giá mức đủ vốn nội bộ ICAAP; Pillar 3: Kỷ luật thị trường).
  - *Khái niệm "Khoan dung pháp lý" (Regulatory Forbearance)*: Phải khẳng định Thông tư 01/2020 và Thông tư 02/2023 về cơ cấu lại thời hạn trả nợ giữ nguyên nhóm nợ thực chất là chính sách can thiệp hành chính tạm thời làm "đóng băng" việc ghi nhận rủi ro, tạo ra hiện tượng *Evergreening loans* (đảo nợ kỹ thuật).

#### CHƯƠNG 2. MÔ HÌNH QUẢN TRỊ RỦI RO TÍN DỤNG TẠI AGRIBANK VÀ MB
* **Nhận xét hiện trạng**: Ma trận so sánh mô hình 3 tuyến phòng vệ (Bảng 3) rất rõ ràng, bóc tách được sự khác biệt giữa bộ máy cồng kềnh, phân tán của Agribank và mô hình tập đoàn tập trung hóa của MB.
* **Lỗ hổng học thuật cấp ThS/TS**:
  - Chưa làm rõ **Cấu trúc Thể chế và Khẩu vị Rủi ro (Risk Appetite Framework - RAF)**:
    - Agribank mang bản chất của một *Policy-tilted State-Owned Bank*: Khẩu vị rủi ro gắn liền với Nghị quyết 26-NQ/TW về Nông nghiệp - Nông dân - Nông thôn, danh mục có độ phân tán cao (Granular portfolio) nhưng biên lãi ròng (NIM) mỏng, chi phí vận hành (CIR) cao do mạng lưới chi nhánh rộng nhất hệ thống.
    - MB mang bản chất của một *Aggressive Financial Conglomerate*: Mô hình hệ sinh thái kết hợp ngân hàng thương mại - ngân hàng đầu tư (MBS) - bảo hiểm (MB Ageas) - tài chính tiêu dùng (MCredit). Khẩu vị rủi ro chấp nhận đầu tư lớn vào các phân khúc lợi suất cao (BĐS, TPDN, vay mua nhà dự án).
  - Thiếu phân tích về **Chính sách Tiền lương và Cơ chế Đãi ngộ (Incentive Compensation Alignment)**: Ở MB, KPI gắn chặt với lợi nhuận kinh doanh thúc đẩy cán bộ tín dụng mở rộng dư nợ nhanh; trong khi ở Agribank, nguy cơ trách nhiệm hình sự đối với thất thoát tài sản nhà nước tạo ra sức ì và sự bảo thủ trong thẩm định tín dụng.

#### CHƯƠNG 3 & 4. HỆ CHỈ TIÊU & PHÂN TÍCH THỰC TRẠNG (2020–2025)
* **Nhận xét hiện trạng**: Đây là phần mạnh nhất của báo cáo. Việc đối chiếu các chỉ tiêu nợ xấu, nợ nhóm 2, LLCR, credit cost, và các chuỗi số liệu của Agribank được thực hiện rất công phu và chuẩn xác.
* **Lỗ hổng học thuật cấp ThS/TS**:
  - *Chưa phân rã tốc độ tăng nợ xấu theo Hiệu ứng Quy mô (Denominator Effect) vs. Hiệu ứng Chất lượng thực (Asset Quality Effect)*:
    - Năm 2025, NPL của MB giảm về 1,29%. Bài viết đã nhận định đúng việc MB xóa nợ 11.200 tỷ đồng, nhưng cần dùng phương pháp phân rã toán học (Decomposition Analysis) để chỉ rõ: Trong mức giảm $\Delta NPL$, bao nhiêu phần trăm do **Mẫu số tăng trưởng phi mã** (dư nợ tăng tới 39,6% - hiệu ứng pha loãng nợ xấu), bao nhiêu phần trăm do **Tử số giảm** (nhờ kỹ thuật xóa nợ nội bảng chuyển ra ngoại bảng).
  - *Hiện tượng Quản trị Lợi nhuận qua Quỹ Dự phòng (Cookie Jar Accounting)*:
    - Cần nhấn mạnh luận điểm học thuật: Giai đoạn 2020–2022, MB duy trì LLCR ở mức cao ngất ngưởng (đạt đỉnh 268% năm 2021) không đơn thuần là "quản trị rủi ro tốt", mà là hành vi trích lập vượt mức cần thiết để tích lũy "bộ đệm lợi nhuận bí mật". Đến năm 2023, khi thị trường khó khăn, MB lập tức hoàn nhập 4.800 tỷ đồng để bù đắp vào lợi nhuận kinh doanh. Đây là một điển hình kinh điển về *Earnings Smoothing* (Làm mượt lợi nhuận) trong lý thuyết kế toán ngân hàng mà một luận văn ThS/TS bắt buộc phải mổ xẻ.
  - *Nợ nhóm 5 của Agribank (>75%) - Bẫy Thanh lý Tài sản Bảo đảm*:
    - Cần phân tích sâu hơn về nút thắt thể chế: Tại sao nợ xấu Agribank không thể xử lý nhanh như MB? Vì TSBĐ của Agribank chủ yếu là đất nông nghiệp, đất ở nông thôn tại các địa bàn vùng sâu vùng xa. Khi Nghị quyết 42 hết hiệu lực, quyền thu giữ TSBĐ bị vô hiệu hóa, ngân hàng phải khởi kiện qua tòa án với thời gian tố tụng trung bình 3–5 năm. Đây là rủi ro thanh khoản tài sản bảo đảm (Collateral Liquidity Risk) chứ không chỉ là rủi ro tín dụng đơn thuần.

#### CHƯƠNG 5. CÁC TÌNH HUỐNG THỰC TIỄN (CASE STUDIES)
* **Nhận xét hiện trạng**: Việc đưa vào 4 tình huống (Lifepro Agribank, Cán bộ MB Gia Lai, Cú sốc nợ xấu MB 2023, Đợt làm sạch nợ quý IV/2025) giúp bài viết có tính thực tiễn cao.
* **Lỗ hổng học thuật cấp ThS/TS**:
  - **Cách tiếp cận còn nặng tính "phóng sự báo chí"**: Tác giả liệt kê diễn biến vụ án, mức án tù, số tiền thiệt hại. Ở bậc Thạc sĩ / Tiến sĩ, một Case Study nghiên cứu phải được phân tích qua các mô hình chuẩn quốc tế:
    1. **Khung Kiểm soát Nội bộ COSO (COSO 2013 Internal Control Framework)**: Mổ xẻ vụ Lifepro và MB Gia Lai xem vi phạm ở thành tố nào: *Môi trường kiểm soát (Control Environment)*, *Đánh giá rủi ro (Risk Assessment)*, *Hoạt động kiểm soát (Control Activities - nguyên tắc phê duyệt kép, đối chiếu độc lập)*, *Thông tin & Truyền thông*, hay *Hoạt động giám sát*.
    2. **Mô hình Tam giác Gian lận (Fraud Triangle - Cressey, 1953)**: Phân tích 3 yếu tố: *Áp lực (Pressure - chỉ tiêu doanh số/KPI)*, *Cơ hội (Opportunity - phân quyền lỏng lẻo tại chi nhánh)*, và *Thái độ / Hợp lý hóa hành vi (Rationalization)*.
    3. **Lỗ hổng Tuyến phòng vệ thứ hai và thứ ba**: Tại sao Khối Quản trị rủi ro và Kiểm toán nội bộ của Hội sở không phát hiện sớm các dấu hiệu cảnh báo đỏ (Red Flags)?

#### CHƯƠNG 6 & 7. SO SÁNH VÀ KIẾN NGHỊ
* **Nhận xét hiện trạng**: Bảng 9 so sánh nguyên nhân khả dĩ và kiểm định rất sắc sảo. Các kiến nghị đối với NHNN, Agribank, và MB đều đúng hướng.
* **Lỗ hổng học thuật cấp ThS/TS**:
  - *Kiến nghị cần nâng tầm hàm lượng công nghệ và kỹ thuật quản trị tiên tiến*:
    - Thay vì chỉ kiến nghị Agribank "tăng vốn" hay "nâng cao chất lượng cán bộ", cần đề xuất: Xây dựng hệ thống **Cảnh báo sớm (Early Warning System - EWS)** ứng dụng Machine Learning (mô hình Random Forest / XGBoost hoặc Logistic Regression) trên dữ liệu lớn dòng tiền nông nghiệp; xây dựng kịch bản **Rủi ro Khí hậu và Môi trường (Climate & Environmental Risk Stress Testing)** vào quy trình thẩm định cho vay nông nghiệp theo định hướng ESG.
    - Đối với MB: Đề xuất áp dụng **Quy chuẩn Giới hạn Rủi ro Tập trung Đa chiều (Multi-dimensional Concentration Limits)**: Không chỉ giới hạn theo ngành BĐS mà phải giới hạn theo hệ sinh thái doanh nghiệp liên quan (Group of Connected Clients) bao gồm cả danh mục tín dụng, TPDN, bảo lãnh và cam kết ngoại bảng.

---

### PHẦN III. KẾ HOẠCH HÀNH ĐỘNG NÂNG CẤP LÊN CHUẨN THS / TS

Để nâng tầm toàn bộ công trình này đạt điểm xuất sắc tuyệt đối trước Hội đồng chấm luận văn Thạc sĩ / Nghiên cứu sinh Tiến sĩ tại Đại học Kinh tế Quốc dân (NEU), đề xuất 4 nhóm giải pháp điều chỉnh trực tiếp:

#### 1. Bổ sung Khung Lý thuyết & Khung Phân tích (Chương 1)
- Bổ sung Tiểu mục *1.1. Khung lý thuyết kinh tế tài chính về rủi ro tín dụng*:
  * Đưa vào Lý thuyết Bất cân xứng thông tin (Stiglitz-Weiss).
  * Đưa vào Lý thuyết Chi phí Đại diện (Jensen-Meckling).
  * Chuẩn mực IFRS 9 ECL vs VAS 02/TT11 Incurred Loss.
- Bổ sung Sơ đồ *Khung Phân tích Quản trị Rủi ro Tín dụng Ngân hàng (Analytical Framework)* liên kết giữa: Thể chế sở hữu $\rightarrow$ Khẩu vị rủi ro $\rightarrow$ Cấu trúc danh mục $\rightarrow$ Các cú sốc chính sách/vĩ mô $\rightarrow$ Biểu hiện nợ xấu và Bộ đệm dự phòng $\rightarrow$ Kỹ thuật xử lý nợ.

#### 2. Nâng cấp Bóc tách Định lượng trong Excel
- Bổ sung **Sheet `Stress_Testing`**: Xây dựng bảng kịch bản giả lập 3 mức độ (Cơ sở, Tiêu cực, Khủng hoảng) cho năm 2026:
  * Biến vĩ mô: Tăng trưởng GDP (6,5% vs 5,0% vs 3,5%); Lãi suất (+0 bps vs +150 bps vs +300 bps).
  * Dự báo tác động đến: $NPL$, Tỷ lệ nợ nhóm 2, Chi phí dự phòng cần trích lập thêm, Lợi nhuận trước thuế và $CAR$ theo Basel II.
- Bổ sung **Sheet `IFRS9_Simulation`**: Ước tính quy mô trích lập dự phòng tổn thất kỳ vọng (ECL) nếu chuyển dịch toàn bộ danh mục nợ nhóm 2 sang Stage 2 (Lifetime ECL) của Agribank và MB.

#### 3. Tái cấu trúc Chương 5 (Case Studies) theo Chuẩn Kiểm soát Nội bộ COSO
- Chuyển các mục 5.1 và 5.2 từ lối viết tường thuật diễn biến sang **Ma trận Đánh giá Lỗ hổng Kiểm soát Nội bộ COSO 2013**:
  * Liệt kê rõ: Cơ chế phân quyền, Rào cản kiểm soát kép (Dual Control), Sự can thiệp của người quản lý (Management Override of Controls), và Thất bại trong giám sát từ xa của Tuyến 2.

#### 4. Chuẩn hóa Ngôn ngữ & Văn phong Học thuật (Academic Classic Prose)
- Rà soát toàn bộ văn bản để loại bỏ các từ ngữ mang phong cách đời thường hoặc báo chí.
- Đảm bảo các thuật ngữ chuyên ngành tài chính quốc tế được đồng bộ: *Risk-Weighted Assets (RWA), Loan Loss Coverage Ratio (LLCR), Capital Adequacy Ratio (CAR), Net Interest Margin (NIM), Non-Performing Loans (NPL), Provision for Credit Losses (PCL), Internal Capital Adequacy Assessment Process (ICAAP)*.

---

### KẾT LUẬN ĐÁNH GIÁ CHUNG

Công trình hiện tại đã sở hữu **phần cốt lõi dữ liệu vững chắc nhất, hiếm có ở các bài tiểu luận thông thường**: sự chi tiết, trung thực và đối soát tỉ mỉ từng con số từ BCTC kiểm toán và BCTN gốc của cả Agribank và MB suốt 6 năm. 

Khoảng cách để đưa công trình này từ **"Tiểu luận môn học xuất sắc"** thành một **"Luận văn Thạc sĩ / Công trình Nghiên cứu cấp Cao học đạt giải thưởng hoặc sẵn sàng xuất bản tạp chí chuyên ngành"** nằm ở **Tầng Lý luận học thuật, Phương pháp luận phân tích định lượng nâng cao (Stress Test/IFRS 9) và Khung kiểm soát nội bộ COSO**. Việc bổ sung các chiều kích này sẽ biến bài nghiên cứu thành một sản phẩm mẫu mực, có sức thuyết phục tuyệt đối trước mọi hội đồng chuyên gia.
