# Optimization script for Dell Inspiron 5547 (Intel i7-4510U)

Write-Output "=========================================================="
Write-Output "BAT DAU QUY TRINH TOI UU HOA HE THONG DELL INSPIRON 5547"
Write-Output "=========================================================="

# 1. BƯỚC 1: XỬ LÝ DỊCH VỤ SQL SERVER
Write-Output "`n[1/4] Chuyen doi dich vu SQL Server sang che do Thu cong (Manual)..."
$sqlServices = @("MSSQL`$SQLEXPRESS", "SQLTELEMETRY`$SQLEXPRESS", "SQLWriter")

foreach ($s in $sqlServices) {
    try {
        $svc = Get-Service -Name $s -ErrorAction SilentlyContinue
        if ($svc) {
            Write-Output "  -> Dang dung dich vu: $($svc.DisplayName)..."
            Stop-Service -Name $s -Force -ErrorAction SilentlyContinue
            if ($s -like "*TELEMETRY*") {
                Set-Service -Name $s -StartupType Disabled
                Write-Output "  -> Da chuyen $s sang: Disabled"
            } else {
                Set-Service -Name $s -StartupType Manual
                Write-Output "  -> Da chuyen $s sang: Manual"
            }
        }
    } catch {
        Write-Output "  ! Loi xu ly $s : $_"
    }
}

# 2. BƯỚC 2: TẠO SCRIPT BẬT/TẮT SQL SERVER TRÊN DESKTOP
Write-Output "`n[2/4] Tao script 1-click Bat/Tat SQL Server tren Desktop..."
$desktopPath = [Environment]::GetFolderPath("Desktop")

$startLines = @(
    "@echo off",
    "title Khoi dong SQL Server",
    "echo Dang bat SQL Server (SQLEXPRESS)...",
    "net start `"MSSQL`$SQLEXPRESS`"",
    "net start `"SQLWriter`"",
    "echo.",
    "echo Da bat SQL Server thanh cong!",
    "pause"
)
$startSqlContent = $startLines -join "`r`n"

$stopLines = @(
    "@echo off",
    "title Dung SQL Server",
    "echo Dang tat SQL Server de giai phong RAM va CPU...",
    "net stop `"MSSQL`$SQLEXPRESS`" /y",
    "net stop `"SQLWriter`" /y",
    "echo.",
    "echo Da tat SQL Server thanh cong!",
    "pause"
)
$stopSqlContent = $stopLines -join "`r`n"

$startScriptPath = Join-Path $desktopPath "Bat_SQL_Server.bat"
$stopScriptPath = Join-Path $desktopPath "Tat_SQL_Server.bat"

[System.IO.File]::WriteAllText($startScriptPath, $startSqlContent, [System.Text.Encoding]::UTF8)
[System.IO.File]::WriteAllText($stopScriptPath, $stopSqlContent, [System.Text.Encoding]::UTF8)
Write-Output "  -> Da tao: $startScriptPath"
Write-Output "  -> Da tao: $stopScriptPath"

# 3. BƯỚC 3: DỌN DẸP FILE RÁC AN TOÀN (SAFE CLEANUP)
Write-Output "`n[3/4] Don dep bo nho dem va file rac he thong..."
$diskBefore = (Get-CimInstance Win32_LogicalDisk | Where-Object { $_.DeviceID -eq 'C:' }).FreeSpace

# Dọn Temp của User
$userTemp = $env:TEMP
if (Test-Path $userTemp) {
    Write-Output "  -> Dang don User Temp ($userTemp)..."
    Get-ChildItem -Path $userTemp -Recurse -Force -ErrorAction SilentlyContinue |
        Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
}

# Dọn Windows Temp
$winTemp = "C:\Windows\Temp"
if (Test-Path $winTemp) {
    Write-Output "  -> Dang don Windows Temp ($winTemp)..."
    Get-ChildItem -Path $winTemp -Recurse -Force -ErrorAction SilentlyContinue |
        Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
}

# Flush DNS
Write-Output "  -> Xoa bo nho dem DNS..."
ipconfig /flushdns | Out-Null

$diskAfter = (Get-CimInstance Win32_LogicalDisk | Where-Object { $_.DeviceID -eq 'C:' }).FreeSpace
$freedMB = [math]::Round(($diskAfter - $diskBefore) / 1MB, 2)
Write-Output "  -> Da giai phong: $freedMB MB tren o C: (Hien con trong: $([math]::Round($diskAfter / 1GB, 2)) GB)"

# 4. BƯỚC 4: TÌM KIẾM CÔNG CỤ THROTTLESTOP TRÊN MÁY
Write-Output "`n[4/4] Khao sat cong cu ThrottleStop tren he thong..."
$folders = @("C:\Program Files", "C:\Program Files (x86)", "C:\Users\Admin\Downloads", "C:\Tools", "C:\")
$tsFound = $false
foreach ($f in $folders) {
    if (Test-Path $f) {
        $found = Get-ChildItem -Path $f -Filter "*ThrottleStop*.exe" -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($found) {
            Write-Output "  -> Da tim thay ThrottleStop tai: $($found.FullName)"
            $tsFound = $true
            break
        }
    }
}
if (-not $tsFound) {
    Write-Output "  -> Chua co ThrottleStop tren may. Se chuan bi goi huong dan & file thiet lap toi uu."
}

Write-Output "`n=========================================================="
Write-Output "HOAN TAT CAC BUOC TINH CHINH TRUC TIEP TREN HE THONG!"
Write-Output "=========================================================="
