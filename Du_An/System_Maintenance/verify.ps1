# Verification Script
$chromeHighEff = (Get-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Google\Chrome' -Name 'HighEfficiencyModeEnabled' -ErrorAction SilentlyContinue).HighEfficiencyModeEnabled
$chromeSavings = (Get-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Google\Chrome' -Name 'MemorySaverModeSavings' -ErrorAction SilentlyContinue).MemorySaverModeSavings

$swPath = 'C:\Windows\SoftwareDistribution\Download'
$swFiles = Get-ChildItem -Path $swPath -Recurse -Force -File -ErrorAction SilentlyContinue
$swBytes = ($swFiles | Measure-Object -Property Length -Sum).Sum
if (-not $swBytes) { $swBytes = 0 }
$swMB = [math]::Round(($swBytes / 1MB), 2)

$drive = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$totalGB = [math]::Round($drive.Size / 1GB, 2)
$freeGB = [math]::Round($drive.FreeSpace / 1GB, 2)
$usedGB = [math]::Round(($drive.Size - $drive.FreeSpace) / 1GB, 2)
$pctFree = [math]::Round(($drive.FreeSpace / $drive.Size) * 100, 2)

$os = Get-CimInstance Win32_OperatingSystem
$totalRAM = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeRAM = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedRAM = [math]::Round($totalRAM - $freeRAM, 2)
$pctRAM = [math]::Round(($usedRAM / $totalRAM) * 100, 1)

Write-Output "CHROME_HIGH_EFF: $chromeHighEff"
Write-Output "CHROME_SAVINGS: $chromeSavings"
Write-Output "SW_DOWNLOAD_MB: $swMB"
Write-Output "DRIVE_C_TOTAL_GB: $totalGB"
Write-Output "DRIVE_C_FREE_GB: $freeGB"
Write-Output "DRIVE_C_PCT_FREE: $pctFree"
Write-Output "RAM_TOTAL_GB: $totalRAM"
Write-Output "RAM_FREE_GB: $freeRAM"
Write-Output "RAM_USED_GB: $usedRAM"
Write-Output "RAM_PCT_USED: $pctRAM"
