# Advanced Maintenance & Optimization Script
$ErrorActionPreference = 'SilentlyContinue'

Write-Host "=========================================="
Write-Host "TASK 1: ENABLING CHROME MEMORY SAVER"
Write-Host "=========================================="

$chromeRegPath = "HKLM:\SOFTWARE\Policies\Google\Chrome"
if (-not (Test-Path $chromeRegPath)) {
    New-Item -Path $chromeRegPath -Force | Out-Null
}

Set-ItemProperty -Path $chromeRegPath -Name "HighEfficiencyModeEnabled" -Value 1 -Type DWord -Force
Set-ItemProperty -Path $chromeRegPath -Name "MemorySaverModeSavings" -Value 1 -Type DWord -Force

$verifyHighEff = (Get-ItemProperty -Path $chromeRegPath -Name "HighEfficiencyModeEnabled" -ErrorAction SilentlyContinue).HighEfficiencyModeEnabled
$verifySavings = (Get-ItemProperty -Path $chromeRegPath -Name "MemorySaverModeSavings" -ErrorAction SilentlyContinue).MemorySaverModeSavings

if ($verifyHighEff -eq 1 -and $verifySavings -eq 1) {
    Write-Host "[SUCCESS] Chrome Memory Saver enabled globally via Enterprise Policy (Mode: Balanced)."
} else {
    Write-Host "[WARNING] Registry verification returned unexpected state."
}

Write-Host ""
Write-Host "=========================================="
Write-Host "TASK 2: ADVANCED DISK & UPDATE CLEANUP"
Write-Host "=========================================="

function Get-FolderSizeMB($path) {
    if (-not (Test-Path $path)) { return 0.0 }
    $files = Get-ChildItem -Path $path -Recurse -Force -File -ErrorAction SilentlyContinue
    $bytes = ($files | Measure-Object -Property Length -Sum).Sum
    if (-not $bytes) { return 0.0 }
    return [math]::Round(($bytes / 1MB), 2)
}

# 1. Measure initial space
$cDriveBefore = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$freeCBeforeGB = [math]::Round($cDriveBefore.FreeSpace / 1GB, 2)

$swPath = "C:\Windows\SoftwareDistribution\Download"
$werPath = "C:\ProgramData\Microsoft\Windows\WER"
$miniPath = "C:\Windows\Minidump"

$swBeforeMB = Get-FolderSizeMB $swPath
$werBeforeMB = Get-FolderSizeMB $werPath
$miniBeforeMB = Get-FolderSizeMB $miniPath

Write-Host ("SoftwareDistribution Download Before: {0} MB" -f $swBeforeMB)
Write-Host ("Windows Error Reporting (WER) Before: {0} MB" -f $werBeforeMB)
Write-Host ("Minidump Crash Files Before: {0} MB" -f $miniBeforeMB)

# 2. Clean Windows Update Cache
Write-Host "Stopping Windows Update & BITS services..."
Stop-Service -Name wuauserv -Force -ErrorAction SilentlyContinue
Stop-Service -Name bits -Force -ErrorAction SilentlyContinue

Write-Host "Purging SoftwareDistribution\Download cache..."
Get-ChildItem -Path $swPath -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "Restarting Windows Update & BITS services..."
Start-Service -Name bits -ErrorAction SilentlyContinue
Start-Service -Name wuauserv -ErrorAction SilentlyContinue

# 3. Clean Error Reports & Dumps
Write-Host "Cleaning crash dumps and error logs..."
Get-ChildItem -Path $werPath -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem -Path $miniPath -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
if (Test-Path "C:\Windows\MEMORY.DMP") {
    Remove-Item -Path "C:\Windows\MEMORY.DMP" -Force -ErrorAction SilentlyContinue
}

# 4. Empty Recycle Bin
Write-Host "Clearing Recycle Bin..."
Clear-RecycleBin -Force -ErrorAction SilentlyContinue

# 5. Measure after
$swAfterMB = Get-FolderSizeMB $swPath
$werAfterMB = Get-FolderSizeMB $werPath
$miniAfterMB = Get-FolderSizeMB $miniPath

$cDriveAfter = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$freeCAfterGB = [math]::Round($cDriveAfter.FreeSpace / 1GB, 2)
$freedTotalGB = [math]::Round(($freeCAfterGB - $freeCBeforeGB), 2)
$freedTotalMB = [math]::Round(($cDriveAfter.FreeSpace - $cDriveBefore.FreeSpace) / 1MB, 2)

Write-Host ""
Write-Host ("SoftwareDistribution Download After: {0} MB" -f $swAfterMB)
Write-Host ("Windows Error Reporting After: {0} MB" -f $werAfterMB)
Write-Host ("Minidump After: {0} MB" -f $miniAfterMB)
Write-Host ("Disk C Free Before: {0} GB | After: {1} GB" -f $freeCBeforeGB, $freeCAfterGB)
Write-Host ("Net Space Gained: {0} MB ({1} GB)" -f $freedTotalMB, $freedTotalGB)

Write-Host ""
Write-Host "=========================================="
Write-Host "CURRENT RAM STATUS"
Write-Host "=========================================="
$os = Get-CimInstance Win32_OperatingSystem
$totalRAMGB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeRAMGB = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedRAMGB = [math]::Round($totalRAMGB - $freeRAMGB, 2)
$pctRAM = [math]::Round(($usedRAMGB / $totalRAMGB) * 100, 1)

Write-Host ("RAM: Total {0} GB | Used {1} GB ({2}%) | Free {3} GB" -f $totalRAMGB, $usedRAMGB, $pctRAM, $freeRAMGB)
