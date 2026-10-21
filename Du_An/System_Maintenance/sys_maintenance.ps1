$ErrorActionPreference = 'SilentlyContinue'

function Get-DirMetrics($path) {
    if (Test-Path $path) {
        $files = Get-ChildItem -Path $path -Recurse -File -Force -ErrorAction SilentlyContinue
        $measure = $files | Measure-Object -Property Length -Sum
        $sizeMB = if ($measure.Sum) { [math]::Round(($measure.Sum / 1MB), 2) } else { 0 }
        $count = if ($files) { $files.Count } else { 0 }
        return @{ SizeMB = $sizeMB; Count = $count }
    }
    return @{ SizeMB = 0; Count = 0 }
}

# 1. Đo lường ban đầu
$userBefore = Get-DirMetrics $env:TEMP
$winBefore = Get-DirMetrics 'C:\Windows\Temp'

# 2. Xóa Temp User
$userRemoved = 0
$userLocked = 0
Get-ChildItem -Path $env:TEMP -Force -ErrorAction SilentlyContinue | ForEach-Object {
    try {
        Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction Stop
        $userRemoved++
    } catch {
        $userLocked++
    }
}

# Xóa Temp Windows
$winRemoved = 0
$winLocked = 0
Get-ChildItem -Path 'C:\Windows\Temp' -Force -ErrorAction SilentlyContinue | ForEach-Object {
    try {
        Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction Stop
        $winRemoved++
    } catch {
        $winLocked++
    }
}

# Đo lường sau khi xóa
$userAfter = Get-DirMetrics $env:TEMP
$winAfter = Get-DirMetrics 'C:\Windows\Temp'

# 3. Flush DNS
$dnsRaw = ipconfig /flushdns | Out-String

# 4. Kiểm tra ổ C
$disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$totalGB = [math]::Round($disk.Size / 1GB, 2)
$freeGB = [math]::Round($disk.FreeSpace / 1GB, 2)
$usedGB = [math]::Round(($disk.Size - $disk.FreeSpace) / 1GB, 2)
$pctFree = [math]::Round(($disk.FreeSpace / $disk.Size) * 100, 2)

# 5. Kiểm tra tài nguyên RAM tổng thể
$os = Get-CimInstance Win32_OperatingSystem
$totalRAM_MB = [math]::Round($os.TotalVisibleMemorySize / 1KB, 2)
$freeRAM_MB = [math]::Round($os.FreePhysicalMemory / 1KB, 2)
$usedRAM_MB = [math]::Round($totalRAM_MB - $freeRAM_MB, 2)
$pctRAM = [math]::Round(($usedRAM_MB / $totalRAM_MB) * 100, 2)

# 6. Top tiến trình ngốn RAM
$topRam = Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10 Id, ProcessName, @{N='RAM_MB';E={[math]::Round($_.WorkingSet/1MB, 2)}}, @{N='CPU_s';E={if ($_.CPU) { [math]::Round($_.CPU, 2) } else { 0 }}}, Path

# 7. Top tiến trình ngốn CPU (thời gian CPU tích lũy cao nhất)
$topCpu = Get-Process | Where-Object { $_.CPU -gt 0 } | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName, @{N='CPU_s';E={[math]::Round($_.CPU, 2)}}, @{N='RAM_MB';E={[math]::Round($_.WorkingSet/1MB, 2)}}, Path

$report = [PSCustomObject]@{
    UserTemp = @{
        Path = $env:TEMP
        SizeBeforeMB = $userBefore.SizeMB
        SizeAfterMB = $userAfter.SizeMB
        FreedMB = [math]::Round(($userBefore.SizeMB - $userAfter.SizeMB), 2)
        DeletedItems = $userRemoved
        LockedItems = $userLocked
    }
    WinTemp = @{
        Path = 'C:\Windows\Temp'
        SizeBeforeMB = $winBefore.SizeMB
        SizeAfterMB = $winAfter.SizeMB
        FreedMB = [math]::Round(($winBefore.SizeMB - $winAfter.SizeMB), 2)
        DeletedItems = $winRemoved
        LockedItems = $winLocked
    }
    DNS = $dnsRaw.Trim()
    DiskC = @{
        TotalGB = $totalGB
        UsedGB = $usedGB
        FreeGB = $freeGB
        PercentFree = $pctFree
    }
    RAM = @{
        TotalMB = $totalRAM_MB
        UsedMB = $usedRAM_MB
        FreeMB = $freeRAM_MB
        PercentUsed = $pctRAM
    }
    TopRAM = $topRam
    TopCPU = $topCpu
}

$report | ConvertTo-Json -Depth 5
