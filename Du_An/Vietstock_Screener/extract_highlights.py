import openpyxl
import pandas as pd

wb = openpyxl.load_workbook('Bo_Loc_Co_Phieu_Vietstock_Khung_Tieu_Chi_PRO.xlsx', data_only=True)

s = wb['Danh_Gia_Toan_Bo_CP']
headers = [s.cell(1, c).value for c in range(1, s.max_column+1)]

rows = []
for r in range(2, s.max_row+1):
    vals = [s.cell(r, c).value for c in range(1, s.max_column+1)]
    if vals[1]: # Mã CK
        rows.append(vals)

df = pd.DataFrame(rows, columns=headers)

def to_float(val):
    try:
        if val is None or val == '' or val == '-':
            return None
        return float(val)
    except:
        return None

df['PE'] = df['P/E Thực Tế (x)'].apply(to_float)
df['Fwd_PE'] = df['Forward P/E (x)'].apply(to_float)
df['ROE_raw'] = df['ROE (%)'].apply(to_float)
df['ROE'] = df['ROE_raw'].apply(lambda x: x*100 if x is not None and abs(x) <= 1.0 else x)
df['Upside_raw'] = df['Biên An Toàn Upside (%)'].apply(to_float)
df['Upside'] = df['Upside_raw'].apply(lambda x: x*100 if x is not None and abs(x) <= 10.0 else x)
df['Gia'] = df['Thị Giá (VNĐ)'].apply(to_float)
df['Target'] = df['Giá Mục Tiêu CTCK (VNĐ)'].apply(to_float)
df['Score'] = df['TỔNG ĐIỂM (100)'].apply(to_float)
df['Liquidity'] = df['Thanh Khoản 20D (Tỷ/P)'].apply(to_float)

print(f"Tổng số mã phân tích: {len(df)}")
passed_gates = df[df['KẾT LUẬN CỔNG'] == 'VƯỢT QUA CỔNG CỨNG']
print(f"Số mã vượt qua cổng cứng: {len(passed_gates)}")

# 1. TOP CỔ PHIẾU P/E THẤP + ROE CAO (Chất lượng tài chính tốt, định giá rẻ)
print("\n" + "="*120)
print("1. TOP CỔ PHIẾU ĐỊNH GIÁ RẺ NHẤT (P/E THẤP + ROE CAO + THANH KHOẢN TỐT)")
print("="*120)
# Lọc P/E từ 1.0 đến 10.0, ROE >= 15%, Thanh khoản >= 1 tỷ/phiên hoặc trong nhóm Vượt Cổng
low_pe = df[(df['PE'] > 1.0) & (df['PE'] <= 9.0) & (df['ROE'] >= 15.0) & (df['KẾT LUẬN CỔNG'] == 'VƯỢT QUA CỔNG CỨNG')].sort_values(by='PE')
for _, r in low_pe.head(10).iterrows():
    print(f"[{r['Mã CK']:<4}] {r['Tên Doanh Nghiệp']:<32} | P/E: {r['PE']:>5.2f} | Fwd P/E: {r['Fwd_PE']:>4.1f} | ROE: {r['ROE']:>5.1f}% | Upside: {r['Upside']:>+6.1f}% | Giá: {r['Gia']:>8,.0f} | Target: {r['Target']:>8,.0f} | Điểm: {r['Score']}")

# 2. TOP CỔ PHIẾU CÓ HIỆU QUẢ SINH LỜI ROE CAO NHẤT
print("\n" + "="*120)
print("2. TOP CỔ PHIẾU HIỆU QUẢ SINH LỜI CAO NHẤT (ROE CAO + VƯỢT QUA CỔNG BẢO VỆ)")
print("="*120)
high_roe = df[(df['KẾT LUẬN CỔNG'] == 'VƯỢT QUA CỔNG CỨNG') & (df['ROE'] >= 20.0)].sort_values(by='ROE', ascending=False)
for _, r in high_roe.head(10).iterrows():
    print(f"[{r['Mã CK']:<4}] {r['Tên Doanh Nghiệp']:<32} | ROE: {r['ROE']:>5.1f}% | P/E: {r['PE']:>5.2f} | Upside: {r['Upside']:>+6.1f}% | Giá: {r['Gia']:>8,.0f} | Target: {r['Target']:>8,.0f} | Điểm: {r['Score']} | Khuyến nghị: {r['KHUYẾN NGHỊ ĐỊNH CHẾ']}")

# 3. TOP CỔ PHIẾU UPSIDE ĐỊNH GIÁ KỲ VỌNG CAO NHẤT
print("\n" + "="*120)
print("3. TOP CỔ PHIẾU CÓ UPSIDE ĐỊNH GIÁ LỚN NHẤT (Biên an toàn định chế >= 30%)")
print("="*120)
high_upside = df[(df['KẾT LUẬN CỔNG'] == 'VƯỢT QUA CỔNG CỨNG') & (df['Upside'] >= 30.0)].sort_values(by='Upside', ascending=False)
for _, r in high_upside.head(10).iterrows():
    print(f"[{r['Mã CK']:<4}] {r['Tên Doanh Nghiệp']:<32} | Upside: {r['Upside']:>+6.1f}% | Giá: {r['Gia']:>8,.0f} -> Target: {r['Target']:>8,.0f} | P/E: {r['PE']:>5.2f} | ROE: {r['ROE']:>5.1f}% | Điểm: {r['Score']} | Xúc tác: {str(r['Xúc Tác Trọng Yếu'])[:35]}")

# 4. TOP 10 TOÀN DIỆN (BẢNG TOP_CO_PHIEU_CHON_LOC)
s_top = wb['Top_Co_Phieu_Chon_Loc']
h_top = [s_top.cell(5, c).value for c in range(1, s_top.max_column+1)]
r_top = []
for r in range(6, s_top.max_row+1):
    vals = [s_top.cell(r, c).value for c in range(1, s_top.max_column+1)]
    if vals[1]:
        r_top.append(vals)
df_top = pd.DataFrame(r_top, columns=h_top)
print("\n" + "="*120)
print("4. TOP 10 CỔ PHIẾU TINH TUYỂN DẪN ĐẦU THEO MÔ HÌNH CHẤM ĐIỂM PRO")
print("="*120)
for _, r in df_top.head(10).iterrows():
    print(f"Hạng {r['Hạng']:<2} [{r['Mã CK']:<4}] {r['Tên Doanh Nghiệp']:<30} | Điểm: {r['Tổng Điểm']}/100 | Giá: {float(r['Thị Giá (VNĐ)']):>8,.0f} | Target: {float(r['Giá Mục Tiêu (VNĐ)']):>8,.0f} | Upside: {float(r['Upside Kỳ Vọng (%)'])*100:>+5.1f}% | P/E: {float(r['P/E Hiện Tại']):>4.1f} | ROE: {float(r['ROE (%)'])*100:>4.1f}% | Chiến lược: {r['Chiến Lược']}")
