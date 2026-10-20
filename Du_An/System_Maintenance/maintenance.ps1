# Windows Maintenance and Diagnostics Script (ASCII-safe)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

function Get-FolderSizeInMB ($path) {
    if (Test-Path $path) {
        $measure = Get-ChildItem -Path $path -Recurse -Force -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum
        if ($measure.Sum) {
            return [math]::Round(($measure.Sum / 1MB), 2)
        }
    }
    return 0.0
}

Write-Output "=== [1] BEFORE CLEANUP ==="
$userTempBefore = Get-FolderSizeInMB $env:TEMP
$winTempBefore = Get-FolderSizeInMB "C:\Windows\Temp"

$disk = Get-CimInstance Win32_LogicalDisk -Filter 'DeviceID="C:"'
$totalDiskGB = [math]::Round($disk.Size / 1GB, 2)
$freeDiskBeforeGB = [math]::Round($disk.FreeSpace / 1GB, 2)
$usedDiskBeforeGB = [math]::Round(($disk.Size - $disk.FreeSpace) / 1GB, 2)

Write-Output "User Temp ($env:TEMP): $userTempBefore MB"
Write-Output "Windows Temp (C:\Windows\Temp): $winTempBefore MB"
Write-Output "Disk C: Used $usedDiskBeforeGB GB / $totalDiskGB GB (Free: $freeDiskBeforeGB GB)"

Write-Output ""
Write-Output "=== [2] PERFORMING CLEANUP AND FLUSH DNS ==="
# Remove User Temp items
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
# Remove Windows Temp items
Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue

# Flush DNS
ipconfig /flushdns

$userTempAfter = Get-FolderSizeInMB $env:TEMP
$winTempAfter = Get-FolderSizeInMB "C:\Windows\Temp"

$diskAfter = Get-CimInstance Win32_LogicalDisk -Filter 'DeviceID="C:"'
$freeDiskAfterGB = [math]::Round($diskAfter.FreeSpace / 1GB, 2)
$usedDiskAfterGB = [math]::Round(($diskAfter.Size - $diskAfter.FreeSpace) / 1GB, 2)
$percentFree = [math]::Round(($diskAfter.FreeSpace / $diskAfter.Size) * 100, 2)

$freedUserMB = [math]::Round($userTempBefore - $userTempAfter, 2)
$freedWinMB = [math]::Round($winTempBefore - $winTempAfter, 2)
$totalFreedMB = [math]::Round($freedUserMB + $freedWinMB, 2)

Write-Output ""
Write-Output "=== [3] CLEANUP RESULTS ==="
Write-Output "Freed from User Temp: $freedUserMB MB (In-use/Locked remaining: $userTempAfter MB)"
Write-Output "Freed from Windows Temp: $freedWinMB MB (In-use/Locked remaining: $winTempAfter MB)"
Write-Output "Total Space Freed from Temp: $totalFreedMB MB"
Write-Output "Disk C Current: Free $freeDiskAfterGB GB / $totalDiskGB GB ($percentFree % free)"

Write-Output ""
Write-Output "=== [4] TOP 10 PROCESSES BY RAM (WORKING SET) ==="
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Id, ProcessName, @{Name="RAM_MB";Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}}, Path | Format-Table -AutoSize | Out-String | Write-Output

Write-Output ""
Write-Output "=== [5] TOP 10 PROCESSES BY CPU TIME ==="
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName, @{Name="CPU_TotalSec";Expression={[math]::Round($_.CPU, 2)}}, @{Name="RAM_MB";Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}}, Path | Format-Table -AutoSize | Out-String | Write-Output

Write-Output ""
Write-Output "=== [6] SYSTEM HEALTH AND HARDWARE STATUS ==="
$os = Get-CimInstance Win32_OperatingSystem
$totalRAM_GB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeRAM_GB = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedRAM_GB = [math]::Round(($os.TotalVisibleMemorySize - $os.FreePhysicalMemory) / 1MB, 2)
$ramUsagePct = [math]::Round(($usedRAM_GB / $totalRAM_GB) * 100, 2)

Write-Output "Total RAM: $totalRAM_GB GB | Used: $usedRAM_GB GB ($ramUsagePct %) | Free: $freeRAM_GB GB"

$cpuLoad = (Get-CimInstance Win32_Processor | Measure-Object -Property LoadPercentage -Average).Average
Write-Output "Current CPU Load: $cpuLoad %"

$uptime = (Get-Date) - $os.LastBootUpTime
Write-Output "System Uptime: $($uptime.Days) days $($uptime.Hours) hours $($uptime.Minutes) mins"
