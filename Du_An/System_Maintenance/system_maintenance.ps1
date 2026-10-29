$ErrorActionPreference = 'SilentlyContinue'

Write-Host "====================================================="
Write-Host "         BAO CAO BAO TRI HE THONG WINDOWS           "
Write-Host "====================================================="

# 1. Baseline Disk C
Write-Host "`n>>> [1/4] KIEM TRA DUNG LUONG O DIA C TRUOC KHI DON"
$diskBefore = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$freeBeforeGB = [math]::Round($diskBefore.FreeSpace / 1GB, 2)
$totalGB = [math]::Round($diskBefore.Size / 1GB, 2)
$usedBeforeGB = [math]::Round(($diskBefore.Size - $diskBefore.FreeSpace) / 1GB, 2)
$usedBeforePct = [math]::Round(($usedBeforeGB / $totalGB) * 100, 1)

Write-Host "Tong dung luong C: : $totalGB GB"
Write-Host "Da su dung         : $usedBeforeGB GB ($usedBeforePct %)"
Write-Host "Con trong          : $freeBeforeGB GB"

# 2. Cleanup Temp Files
Write-Host "`n>>> [2/4] DON DEP FILE RAC TRONG THU MUC TEMP"
function Get-FolderStats($path) {
    if (Test-Path $path) {
        $items = Get-ChildItem -Path $path -Recurse -Force -ErrorAction SilentlyContinue
        $measure = $items | Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue
        $sizeMB = if ($measure.Sum) { [math]::Round(($measure.Sum / 1MB), 2) } else { 0 }
        $count = ($items | Measure-Object).Count
        return @{ SizeMB = $sizeMB; Count = $count }
    }
    return @{ SizeMB = 0; Count = 0 }
}

$userTempStatsBefore = Get-FolderStats $env:TEMP
$winTempStatsBefore = Get-FolderStats "C:\Windows\Temp"
Write-Host "User Temp ($env:TEMP): $($userTempStatsBefore.SizeMB) MB ($($userTempStatsBefore.Count) files/folders)"
Write-Host "Windows Temp (C:\Windows\Temp): $($winTempStatsBefore.SizeMB) MB ($($winTempStatsBefore.Count) files/folders)"

# Perform deletion
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue

$userTempStatsAfter = Get-FolderStats $env:TEMP
$winTempStatsAfter = Get-FolderStats "C:\Windows\Temp"

Write-Host "Ket qua sau don:"
Write-Host " - User Temp: Con lai $($userTempStatsAfter.SizeMB) MB (cac file dang duoc ung dung/he thong mo khoa)"
Write-Host " - Windows Temp: Con lai $($winTempStatsAfter.SizeMB) MB (file he thong dang khoa)"

# 3. DNS Flush
Write-Host "`n>>> [3/4] XOA CACHE DNS (ipconfig /flushdns)"
$flushOutput = ipconfig /flushdns
$flushOutput | Out-String | Write-Host

# 4. Measure Post-Cleanup Disk C
$diskAfter = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$freeAfterGB = [math]::Round($diskAfter.FreeSpace / 1GB, 2)
$usedAfterGB = [math]::Round(($diskAfter.Size - $diskAfter.FreeSpace) / 1GB, 2)
$freedMB = [math]::Round(($diskAfter.FreeSpace - $diskBefore.FreeSpace) / 1MB, 2)

Write-Host "Dung luong O C sau khi don:"
Write-Host " - Con trong : $freeAfterGB GB"
Write-Host " - Giai phong: $freedMB MB"

# 5. System Health Overview: CPU, RAM
Write-Host "`n>>> [4/4] SUC KHOE HE THONG VA TIEN TRINH (CPU / RAM)"
$os = Get-CimInstance Win32_OperatingSystem
$totalRAM_GB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeRAM_GB = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedRAM_GB = [math]::Round($totalRAM_GB - $freeRAM_GB, 2)
$ramPct = [math]::Round(($usedRAM_GB / $totalRAM_GB) * 100, 1)

$cpuLoad = (Get-CimInstance Win32_Processor | Measure-Object -Property LoadPercentage -Average).Average

Write-Host "Tong RAM          : $totalRAM_GB GB"
Write-Host "RAM dang dung     : $usedRAM_GB GB ($ramPct %)"
Write-Host "RAM con trong     : $freeRAM_GB GB"
Write-Host "Tai CPU tong the  : $cpuLoad %"

# Top 10 RAM Consumers
Write-Host "`n--- TOP 10 TIEN TRINH CHIEM NHIEU RAM NHAT ---"
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Id, ProcessName, @{Name="RAM_MB";Expression={[math]::Round($_.WorkingSet64 / 1MB, 1)}}, @{Name="CPU_Sec";Expression={[math]::Round($_.CPU, 1)}}, @{Name="Path";Expression={$_.Path}} | Format-Table -AutoSize

# Top 10 CPU Consumers
Write-Host "`n--- TOP 10 TIEN TRINH CO THOI GIAN XU LY CPU NHIEU NHAT ---"
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName, @{Name="CPU_Sec";Expression={[math]::Round($_.CPU, 1)}}, @{Name="RAM_MB";Expression={[math]::Round($_.WorkingSet64 / 1MB, 1)}}, @{Name="Path";Expression={$_.Path}} | Format-Table -AutoSize

# Potential Suspicious / Anomalous Processes Check
Write-Host "`n--- RANSOMWARE / SUSPICIOUS PROCESS SCAN (Chay tu thu muc la / bat thuong) ---"
$suspicious = Get-Process | Where-Object { 
    $_.Path -and (
        $_.Path -like "*\Temp\*" -or 
        ($_.Path -like "*\AppData\Local\Temp\*") -or
        ($_.Path -like "*\Users\Public\*")
    )
}

if ($suspicious) {
    $suspicious | Select-Object Id, ProcessName, Path | Format-Table -AutoSize
} else {
    Write-Host "Khong phat hien tien trinh nao chay tu Temp hoac Users\Public (He thong an toan)."
}
