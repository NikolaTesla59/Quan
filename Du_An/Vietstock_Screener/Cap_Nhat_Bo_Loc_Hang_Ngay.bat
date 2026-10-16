@echo off
chcp 65001 > nul
title HE THONG CAP NHAT BO LOC CO PHIEU TU DONG HANG NGAY
color 0A

echo ==============================================================================
echo       HỆ THỐNG CẬP NHẬT DỮ LIỆU CỔ PHIẾU TỰ ĐỘNG (VIETSTOCK + LIVE MARKET)
echo ==============================================================================
echo.
echo Đang kết nối máy chủ Vietstock và Bảng điện thời gian thực...
echo Quá trình quét và tính toán lại 626 cổ phiếu mất khoảng 15-20 giây. Vui lòng chờ...
echo.

python "C:\Users\Admin\Downloads\auto_update_screener.py"

echo.
echo ==============================================================================
echo ĐÃ CẬP NHẬT XONG! 
echo Mời bạn mở file: Bo_Loc_Co_Phieu_Vietstock_Khung_Tieu_Chi_PRO.xlsx
echo ==============================================================================
echo.
pause
