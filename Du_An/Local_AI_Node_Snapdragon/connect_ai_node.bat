@echo off
title Ket noi Local AI Node (Xiaomi 12S Pro -> PC)
echo ==============================================================
echo   DANG THIET LAP CHUYEN TIEP CONG ADB CHO LOCAL AI NODE
echo   Cong: 8080 (Snapdragon 8+ Gen 1 -> PC)
echo ==============================================================
adb reverse tcp:8080 tcp:8080
if %ERRORLEVEL% equ 0 (
    echo.
    echo [OK] DA KET NOI CONG 8080 QUA CAP USB THANH CONG!
    echo PC co the goi AI tai: http://localhost:8080/v1
    echo.
) else (
    echo.
    echo [!] Khong the thiet lap ADB reverse. Hay kiem tra cap USB!
    echo.
)
pause
