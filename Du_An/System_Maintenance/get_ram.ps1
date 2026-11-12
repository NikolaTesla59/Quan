$os = Get-CimInstance Win32_OperatingSystem
$totalGB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeGB = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedGB = [math]::Round($totalGB - $freeGB, 2)
$pctUsed = [math]::Round(($usedGB / $totalGB) * 100, 1)

Write-Output "TOTAL_GB: $totalGB"
Write-Output "USED_GB: $usedGB"
Write-Output "FREE_GB: $freeGB"
Write-Output "PCT_USED: $pctUsed"
