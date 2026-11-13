# Windows Maintenance & Diagnostics Script
$ErrorActionPreference = 'SilentlyContinue'

Write-Output "=========================================="
Write-Output "   WINDOWS SYSTEM MAINTENANCE REPORT"
Write-Output "=========================================="

# 1. Pre-cleanup Disk C
Write-Output "`n[1/5] KIEM TRA DUNG LUONG O C: TRUOC DON DEP"
$diskBefore = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$totalGB = [math]::Round($diskBefore.Size / 1GB, 2)
$freeGBBefore = [math]::Round($diskBefore.FreeSpace / 1GB, 2)
$pctFreeBefore = [math]::Round(($diskBefore.FreeSpace / $diskBefore.Size) * 100, 2)
Write-Output "Tong dung luong: $totalGB GB"
Write-Output "Trong truoc do:  $freeGBBefore GB ($pctFreeBefore%)"

# 2. Temp measurement & cleanup
Write-Output "`n[2/5] XOA FILE RAC TRONG TEMP DIRECTORIES"
$userTemp = $env:TEMP
$winTemp = "C:\Windows\Temp"

$userFiles = Get-ChildItem -Path $userTemp -Recurse -Force -File -ErrorAction SilentlyContinue
$userSizeMB = [math]::Round(($userFiles | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
$userCount = $userFiles.Count

$winFiles = Get-ChildItem -Path $winTemp -Recurse -Force -File -ErrorAction SilentlyContinue
$winSizeMB = [math]::Round(($winFiles | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
$winCount = $winFiles.Count

Write-Output "User Temp ($userTemp): $userSizeMB MB ($userCount files)"
Write-Output "Windows Temp ($winTemp): $winSizeMB MB ($winCount files)"

# Execute cleanup
Remove-Item -Path "$userTemp\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$winTemp\*" -Recurse -Force -ErrorAction SilentlyContinue

# Check remaining (locked files)
$remUserFiles = Get-ChildItem -Path $userTemp -Recurse -Force -File -ErrorAction SilentlyContinue
$remUserSizeMB = [math]::Round(($remUserFiles | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
$remWinFiles = Get-ChildItem -Path $winTemp -Recurse -Force -File -ErrorAction SilentlyContinue
$remWinSizeMB = [math]::Round(($remWinFiles | Measure-Object -Property Length -Sum).Sum / 1MB, 2)

$cleanedUserMB = [math]::Max(0, [math]::Round($userSizeMB - $remUserSizeMB, 2))
$cleanedWinMB = [math]::Max(0, [math]::Round($winSizeMB - $remWinSizeMB, 2))
$totalCleanedMB = [math]::Round($cleanedUserMB + $cleanedWinMB, 2)

Write-Output "Ket qua don dep:"
Write-Output " - Da don tai User Temp: $cleanedUserMB MB (con lai $remUserSizeMB MB dang bi khoa boi cac tien trinh dang chay)"
Write-Output " - Da don tai Windows Temp: $cleanedWinMB MB (con lai $remWinSizeMB MB dang bi khoa)"
Write-Output " -> Tong dung luong rac da giai phong: $totalCleanedMB MB"

# 3. DNS Cache Flush
Write-Output "`n[3/5] XOA CACHE DNS (ipconfig /flushdns)"
$dnsOutput = ipconfig /flushdns
$dnsOutput | ForEach-Object { Write-Output "  $_" }

# 4. Post-cleanup Disk C
Write-Output "`n[4/5] KIEM TRA DUNG LUONG O C: SAU DON DEP"
$diskAfter = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$freeGBAfter = [math]::Round($diskAfter.FreeSpace / 1GB, 2)
$pctFreeAfter = [math]::Round(($diskAfter.FreeSpace / $diskAfter.Size) * 100, 2)
$diffGB = [math]::Round($freeGBAfter - $freeGBBefore, 3)
Write-Output "Trong hien tai: $freeGBAfter GB / $totalGB GB ($pctFreeAfter% trong)"
Write-Output "Chenh lech trong them: $diffGB GB"

# 5. Process & System Health
Write-Output "`n[5/5] RANG BUOC TAI NGUYEN & TIEN TRINH HE THONG"
$os = Get-CimInstance Win32_OperatingSystem
$totalRamGB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeRamGB = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedRamGB = [math]::Round($totalRamGB - $freeRamGB, 2)
$ramPct = [math]::Round(($usedRamGB / $totalRamGB) * 100, 2)
Write-Output "RAM: $usedRamGB GB / $totalRamGB GB ($ramPct% su dung) | Con trong: $freeRamGB GB"

Write-Output "`n--- TOP 10 TIEN TRINH CHIEM DUNG RAM NHIEU NHAT ---"
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Id, ProcessName, @{Name='RAM_MB';Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}}, @{Name='CPU_Sec';Expression={[math]::Round($_.CPU, 2)}} | Format-Table -AutoSize | Out-String | Write-Output

Write-Output "--- TOP 10 TIEN TRINH CHIEM CPU TIME CAO NHAT ---"
Get-Process | Where-Object { $_.CPU -gt 0 } | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName, @{Name='CPU_Sec';Expression={[math]::Round($_.CPU, 2)}}, @{Name='RAM_MB';Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}} | Format-Table -AutoSize | Out-String | Write-Output

Write-Output "=========================================="
Write-Output "           HOAN TAT BAO TRI"
Write-Output "=========================================="
