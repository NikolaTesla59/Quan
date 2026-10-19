$ErrorActionPreference = 'SilentlyContinue'

function Get-FolderSize ($path) {
    if (Test-Path $path) {
        $measure = Get-ChildItem -Path $path -Recurse -Force -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum
        if ($measure.Sum) { return [math]::Round(($measure.Sum / 1MB), 2) }
    }
    return 0
}

$userTempPath = $env:TEMP
$winTempPath = "C:\Windows\Temp"

$userTempBefore = Get-FolderSize $userTempPath
$winTempBefore = Get-FolderSize $winTempPath

# Dọn dẹp User Temp
Remove-Item -Path "$userTempPath\*" -Recurse -Force -ErrorAction SilentlyContinue

# Dọn dẹp Windows Temp
Remove-Item -Path "$winTempPath\*" -Recurse -Force -ErrorAction SilentlyContinue

$userTempAfter = Get-FolderSize $userTempPath
$winTempAfter = Get-FolderSize $winTempPath

# Xóa cache DNS
$flushOutput = ipconfig /flushdns
$dnsResult = ($flushOutput -join " `n ").Trim()

# Kiểm tra dung lượng ổ đĩa C
$diskC = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'" | Select-Object DeviceID,
    @{Name="SizeGB";Expression={[math]::Round($_.Size / 1GB, 2)}},
    @{Name="FreeGB";Expression={[math]::Round($_.FreeSpace / 1GB, 2)}},
    @{Name="UsedGB";Expression={[math]::Round(($_.Size - $_.FreeSpace) / 1GB, 2)}},
    @{Name="PercentFree";Expression={[math]::Round(($_.FreeSpace / $_.Size) * 100, 2)}}

# Sức khỏe RAM
$os = Get-CimInstance Win32_OperatingSystem
$totalRAM = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeRAM = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedRAM = [math]::Round($totalRAM - $freeRAM, 2)
$percentRAM = [math]::Round(($usedRAM / $totalRAM) * 100, 2)

# CPU Load trung bình hiện tại
$cpuLoad = (Get-CimInstance Win32_Processor | Measure-Object -Property LoadPercentage -Average).Average

# Top 10 tiến trình tốn RAM
$topRAM = Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Id, ProcessName,
    @{Name="MemoryMB";Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}},
    Path

# Top 10 tiến trình tốn CPU
$topCPU = Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName,
    @{Name="CPU_Seconds";Expression={[math]::Round($_.CPU, 2)}},
    Path

# Tổng hợp kết quả
$summary = [PSCustomObject]@{
    UserTempBeforeMB = $userTempBefore
    UserTempAfterMB = $userTempAfter
    UserTempFreedMB = [math]::Round(($userTempBefore - $userTempAfter), 2)
    WinTempBeforeMB = $winTempBefore
    WinTempAfterMB = $winTempAfter
    WinTempFreedMB = [math]::Round(($winTempBefore - $winTempAfter), 2)
    DNSResult = $dnsResult
    DiskC = $diskC
    RAM_TotalGB = [math]::Round($totalRAM / 1024, 2)
    RAM_UsedGB = [math]::Round($usedRAM / 1024, 2)
    RAM_FreeGB = [math]::Round($freeRAM / 1024, 2)
    RAM_UsagePercent = $percentRAM
    CPULoadPercent = $cpuLoad
    TopRAM = $topRAM
    TopCPU = $topCPU
}

$summary | ConvertTo-Json -Depth 5
