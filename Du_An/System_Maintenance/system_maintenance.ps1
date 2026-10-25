# Script: System Maintenance & Diagnostics
$ErrorActionPreference = "SilentlyContinue"

function Get-FolderSize([string]$folderPath) {
    if (Test-Path $folderPath) {
        $measure = Get-ChildItem -Path $folderPath -Recurse -Force -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue
        if ($measure -and $measure.Sum) {
            return [math]::Round($measure.Sum / 1MB, 2)
        }
    }
    return 0.0
}

# 1. Measure Temp sizes before cleanup
$userTempPath = $env:TEMP
$winTempPath = "C:\Windows\Temp"

$userTempBefore = Get-FolderSize $userTempPath
$winTempBefore = Get-FolderSize $winTempPath

# 2. Cleanup Temp Files
# Delete files and folders inside $env:TEMP
Get-ChildItem -Path $userTempPath -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
# Delete files and folders inside C:\Windows\Temp
Get-ChildItem -Path $winTempPath -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

$userTempAfter = Get-FolderSize $userTempPath
$winTempAfter = Get-FolderSize $winTempPath

$freedUser = [math]::Max(0, [math]::Round($userTempBefore - $userTempAfter, 2))
$freedWin = [math]::Max(0, [math]::Round($winTempBefore - $winTempAfter, 2))
$totalFreed = [math]::Round($freedUser + $freedWin, 2)

# 3. Flush DNS
$dnsFlush = ipconfig /flushdns

# 4. Drive C info
$driveC = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$totalGB = [math]::Round($driveC.Size / 1GB, 2)
$freeGB = [math]::Round($driveC.FreeSpace / 1GB, 2)
$usedGB = [math]::Round(($driveC.Size - $driveC.FreeSpace) / 1GB, 2)
$freePct = [math]::Round(($driveC.FreeSpace / $driveC.Size) * 100, 2)

# 5. OS and RAM info
$os = Get-CimInstance Win32_OperatingSystem
$totalRamGB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeRamGB = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedRamGB = [math]::Round(($os.TotalVisibleMemorySize - $os.FreePhysicalMemory) / 1MB, 2)
$ramPct = [math]::Round(($usedRamGB / $totalRamGB) * 100, 2)

# 6. Top 10 RAM Processes
$topRam = Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Id, ProcessName, @{Name="RAM_MB";Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}}, @{Name="CPU_Sec";Expression={[math]::Round($_.CPU, 2)}}, @{Name="Path";Expression={$_.Path}}

# 7. Top 10 CPU Processes
$topCpu = Get-Process | Where-Object {$_.CPU -gt 0} | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName, @{Name="CPU_Sec";Expression={[math]::Round($_.CPU, 2)}}, @{Name="RAM_MB";Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}}, @{Name="Path";Expression={$_.Path}}

# Output results in structured format
Write-Output "---SUMMARY_START---"
[PSCustomObject]@{
    UserTemp_Path = $userTempPath
    UserTemp_MB_Before = $userTempBefore
    UserTemp_MB_After = $userTempAfter
    UserTemp_Freed_MB = $freedUser
    WinTemp_Path = $winTempPath
    WinTemp_MB_Before = $winTempBefore
    WinTemp_MB_After = $winTempAfter
    WinTemp_Freed_MB = $freedWin
    Total_Freed_MB = $totalFreed
    Drive_C_Total_GB = $totalGB
    Drive_C_Used_GB = $usedGB
    Drive_C_Free_GB = $freeGB
    Drive_C_Free_Percent = $freePct
    RAM_Total_GB = $totalRamGB
    RAM_Used_GB = $usedRamGB
    RAM_Free_GB = $freeRamGB
    RAM_Used_Percent = $ramPct
    DNS_Flush_Result = ($dnsFlush | Out-String).Trim()
} | ConvertTo-Json -Depth 3
Write-Output "---SUMMARY_END---"

Write-Output "---TOP_RAM_START---"
$topRam | ConvertTo-Json -Depth 3
Write-Output "---TOP_RAM_END---"

Write-Output "---TOP_CPU_START---"
$topCpu | ConvertTo-Json -Depth 3
Write-Output "---TOP_CPU_END---"
