# Windows System Maintenance Script
$ErrorActionPreference = 'SilentlyContinue'

Write-Host "=========================================="
Write-Host "1. MEASURING & CLEANING TEMP DIRECTORIES"
Write-Host "=========================================="

$userTemp = $env:TEMP
$winTemp = 'C:\Windows\Temp'

function Get-FolderStats($path) {
    if (-not (Test-Path -Path $path)) {
        return [PSCustomObject]@{ Count = 0; SizeMB = 0.0 }
    }
    $files = Get-ChildItem -Path $path -Recurse -Force -File -ErrorAction SilentlyContinue
    $count = ($files | Measure-Object).Count
    $sumBytes = ($files | Measure-Object -Property Length -Sum).Sum
    if (-not $sumBytes) { $sumBytes = 0 }
    return [PSCustomObject]@{
        Count = $count
        SizeMB = [math]::Round(($sumBytes / 1MB), 2)
    }
}

$userBefore = Get-FolderStats $userTemp
$winBefore = Get-FolderStats $winTemp

Write-Host ("User Temp Path: {0}" -f $userTemp)
Write-Host ("  Before: {0} files ({1} MB)" -f $userBefore.Count, $userBefore.SizeMB)
Write-Host ("Windows Temp Path: {0}" -f $winTemp)
Write-Host ("  Before: {0} files ({1} MB)" -f $winBefore.Count, $winBefore.SizeMB)

# Perform Deletion
$deletedUserCount = 0
Get-ChildItem -Path $userTemp -Force -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
    try {
        Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction Stop
        $deletedUserCount++
    } catch {
        # File is locked / in use by running process
    }
}

$deletedWinCount = 0
Get-ChildItem -Path $winTemp -Force -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
    try {
        Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction Stop
        $deletedWinCount++
    } catch {
        # File is locked / in use by system service
    }
}

$userAfter = Get-FolderStats $userTemp
$winAfter = Get-FolderStats $winTemp

$userFreed = [math]::Max(0, [math]::Round(($userBefore.SizeMB - $userAfter.SizeMB), 2))
$winFreed = [math]::Max(0, [math]::Round(($winBefore.SizeMB - $winAfter.SizeMB), 2))
$totalFreed = [math]::Round(($userFreed + $winFreed), 2)

Write-Host ""
Write-Host ("User Temp After: {0} files ({1} MB) | Freed: {2} MB" -f $userAfter.Count, $userAfter.SizeMB, $userFreed)
Write-Host ("Windows Temp After: {0} files ({1} MB) | Freed: {2} MB" -f $winAfter.Count, $winAfter.SizeMB, $winFreed)
Write-Host ("Total Temp Space Reclaimed: {0} MB" -f $totalFreed)

Write-Host ""
Write-Host "=========================================="
Write-Host "2. FLUSHING DNS CACHE"
Write-Host "=========================================="
$flushResult = ipconfig /flushdns
$flushResult | ForEach-Object { Write-Host $_ }

Write-Host ""
Write-Host "=========================================="
Write-Host "3. DISK SPACE & SYSTEM RESOURCES"
Write-Host "=========================================="

# Disk C
$driveC = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$totalDiskGB = [math]::Round($driveC.Size / 1GB, 2)
$freeDiskGB = [math]::Round($driveC.FreeSpace / 1GB, 2)
$usedDiskGB = [math]::Round(($driveC.Size - $driveC.FreeSpace) / 1GB, 2)
$percentFree = [math]::Round(($driveC.FreeSpace / $driveC.Size) * 100, 2)
$percentUsed = [math]::Round((($driveC.Size - $driveC.FreeSpace) / $driveC.Size) * 100, 2)

Write-Host ("Drive C: Capacity: {0} GB | Used: {1} GB ({2}%) | Free: {3} GB ({4}%)" -f $totalDiskGB, $usedDiskGB, $percentUsed, $freeDiskGB, $percentFree)

# RAM
$os = Get-CimInstance Win32_OperatingSystem
$totalRAMGB = [math]::Round($os.TotalVisibleMemorySize / 1MB / 1024, 2)
$freeRAMGB = [math]::Round($os.FreePhysicalMemory / 1MB / 1024, 2)
$usedRAMGB = [math]::Round($totalRAMGB - $freeRAMGB, 2)
$ramPercentUsed = [math]::Round(($usedRAMGB / $totalRAMGB) * 100, 2)

Write-Host ("RAM: Total: {0} GB | Used: {1} GB ({2}%) | Free: {3} GB" -f $totalRAMGB, $usedRAMGB, $ramPercentUsed, $freeRAMGB)

Write-Host ""
Write-Host "=========================================="
Write-Host "4. TOP PROCESSES BY MEMORY (RAM)"
Write-Host "=========================================="
Get-Process | Where-Object { $_.WorkingSet64 -gt 50MB } |
    Sort-Object WorkingSet64 -Descending |
    Select-Object -First 10 Id, ProcessName,
        @{Name='RAM (MB)'; Expression={[math]::Round($_.WorkingSet64 / 1MB, 1)}},
        @{Name='CPU (s)'; Expression={[math]::Round($_.CPU, 1)}},
        @{Name='Path'; Expression={try { $_.Path } catch { "N/A" }}} |
    Format-Table -AutoSize

Write-Host "=========================================="
Write-Host "5. TOP PROCESSES BY CPU USAGE"
Write-Host "=========================================="
Get-Process | Where-Object { $_.CPU -gt 5 } |
    Sort-Object CPU -Descending |
    Select-Object -First 10 Id, ProcessName,
        @{Name='CPU (s)'; Expression={[math]::Round($_.CPU, 1)}},
        @{Name='RAM (MB)'; Expression={[math]::Round($_.WorkingSet64 / 1MB, 1)}},
        @{Name='Path'; Expression={try { $_.Path } catch { "N/A" }}} |
    Format-Table -AutoSize

Write-Host "=========================================="
Write-Host "6. ANOMALY / UNUSUAL PROCESS SCAN"
Write-Host "=========================================="
# Scan for processes running from AppData or Temp, or without Company / Description
$suspicious = Get-Process | ForEach-Object {
    $proc = $_
    $path = ""
    try { $path = $proc.Path } catch {}
    if ($path) {
        if ($path -match "\\(Temp|AppData\\Local\\Temp)\\" -or ($path -match "AppData" -and $path -notmatch "(Google|Microsoft|Programs|npm|nvm|JetBrains|Cursor|Anthropic|Gemini|Code)")) {
            [PSCustomObject]@{
                Id = $proc.Id
                Name = $proc.ProcessName
                Path = $path
                RAM_MB = [math]::Round($proc.WorkingSet64 / 1MB, 1)
            }
        }
    }
}

if ($suspicious) {
    Write-Host "Alert: Processes running from unusual temporary locations:"
    $suspicious | Format-Table -AutoSize
} else {
    Write-Host "No anomalous processes detected in temp/untrusted locations."
}
