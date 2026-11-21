# Windows Routine Maintenance Script
$ErrorActionPreference = "Continue"

Write-Output "=================================================="
Write-Output "1. CHECKING INITIAL METRICS"
Write-Output "=================================================="

# 1. Disk C status
$cDisk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$cSizeGB = [math]::Round($cDisk.Size / 1GB, 2)
$cFreeGB = [math]::Round($cDisk.FreeSpace / 1GB, 2)
$cUsedGB = [math]::Round(($cDisk.Size - $cDisk.FreeSpace) / 1GB, 2)
$cFreePct = [math]::Round(($cDisk.FreeSpace / $cDisk.Size) * 100, 2)
Write-Output "Disk C: Total: $cSizeGB GB | Used: $cUsedGB GB | Free: $cFreeGB GB ($cFreePct % free)"

# 2. Measure temp before
$userTempPath = $env:TEMP
$winTempPath = "C:\Windows\Temp"

$userTempFilesBefore = Get-ChildItem -Path $userTempPath -Recurse -Force -ErrorAction SilentlyContinue
$userTempSizeBefore = ($userTempFilesBefore | Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum
if (-not $userTempSizeBefore) { $userTempSizeBefore = 0 }
$userTempCountBefore = ($userTempFilesBefore | Measure-Object).Count

$winTempFilesBefore = Get-ChildItem -Path $winTempPath -Recurse -Force -ErrorAction SilentlyContinue
$winTempSizeBefore = ($winTempFilesBefore | Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum
if (-not $winTempSizeBefore) { $winTempSizeBefore = 0 }
$winTempCountBefore = ($winTempFilesBefore | Measure-Object).Count

$uMbBefore = [math]::Round($userTempSizeBefore / 1MB, 2)
$wMbBefore = [math]::Round($winTempSizeBefore / 1MB, 2)
Write-Output "User Temp before: $uMbBefore MB ($userTempCountBefore items)"
Write-Output "Windows Temp before: $wMbBefore MB ($winTempCountBefore items)"

Write-Output ""
Write-Output "=================================================="
Write-Output "2. CLEANING TEMP DIRECTORIES"
Write-Output "=================================================="

# Clean User Temp
Write-Output "[*] Cleaning User Temp: $userTempPath ..."
Get-ChildItem -Path $userTempPath -Force -ErrorAction SilentlyContinue | ForEach-Object {
    Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction SilentlyContinue
}

# Clean Windows Temp
Write-Output "[*] Cleaning Windows Temp: $winTempPath ..."
Get-ChildItem -Path $winTempPath -Force -ErrorAction SilentlyContinue | ForEach-Object {
    Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction SilentlyContinue
}

# Measure temp after
$userTempFilesAfter = Get-ChildItem -Path $userTempPath -Recurse -Force -ErrorAction SilentlyContinue
$userTempSizeAfter = ($userTempFilesAfter | Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum
if (-not $userTempSizeAfter) { $userTempSizeAfter = 0 }
$userTempCountAfter = ($userTempFilesAfter | Measure-Object).Count

$winTempFilesAfter = Get-ChildItem -Path $winTempPath -Recurse -Force -ErrorAction SilentlyContinue
$winTempSizeAfter = ($winTempFilesAfter | Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum
if (-not $winTempSizeAfter) { $winTempSizeAfter = 0 }
$winTempCountAfter = ($winTempFilesAfter | Measure-Object).Count

$uMbAfter = [math]::Round($userTempSizeAfter / 1MB, 2)
$wMbAfter = [math]::Round($winTempSizeAfter / 1MB, 2)

$cleanedUserMB = [math]::Round(($userTempSizeBefore - $userTempSizeAfter) / 1MB, 2)
$cleanedWinMB = [math]::Round(($winTempSizeBefore - $winTempSizeAfter) / 1MB, 2)
$totalCleanedMB = [math]::Round(($cleanedUserMB + $cleanedWinMB), 2)

Write-Output "[OK] Cleaned User Temp: $cleanedUserMB MB (Remaining: $uMbAfter MB in $userTempCountAfter locked/active items)"
Write-Output "[OK] Cleaned Windows Temp: $cleanedWinMB MB (Remaining: $wMbAfter MB in $winTempCountAfter locked/active items)"
Write-Output "[OK] Total Temp Cleaned: $totalCleanedMB MB"

Write-Output ""
Write-Output "=================================================="
Write-Output "3. FLUSHING DNS CACHE"
Write-Output "=================================================="
try {
    Clear-DnsClientCache -ErrorAction Stop
    Write-Output "[OK] Clear-DnsClientCache executed successfully."
}
catch {
    Write-Output "[WARN] Clear-DnsClientCache cmdlet returned error, falling back to ipconfig."
}
$flushResult = ipconfig /flushdns
$flushResult | ForEach-Object { Write-Output "    $_" }

Write-Output ""
Write-Output "=================================================="
Write-Output "4. SYSTEM HEALTH AND PERFORMANCE AUDIT"
Write-Output "=================================================="

# OS & RAM info
$os = Get-CimInstance Win32_OperatingSystem
$totalRAM_GB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeRAM_GB = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedRAM_GB = [math]::Round(($os.TotalVisibleMemorySize - $os.FreePhysicalMemory) / 1MB, 2)
$usedRAM_Pct = [math]::Round(($usedRAM_GB / $totalRAM_GB) * 100, 2)
$lastBoot = $os.LastBootUpTime
$uptime = (Get-Date) - $lastBoot
$uptimeFormatted = "$($uptime.Days)d $($uptime.Hours)h $($uptime.Minutes)m"

Write-Output "OS: $($os.Caption) ($($os.OSArchitecture)) Build $($os.BuildNumber)"
Write-Output "Uptime: $uptimeFormatted (Last Boot: $lastBoot)"
Write-Output "RAM Usage: $usedRAM_GB GB / $totalRAM_GB GB ($usedRAM_Pct % in use, $freeRAM_GB GB free)"

# Updated Disk C status after clean
$cDiskAfter = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$cFreeGBAfter = [math]::Round($cDiskAfter.FreeSpace / 1GB, 2)
$cFreePctAfter = [math]::Round(($cDiskAfter.FreeSpace / $cDiskAfter.Size) * 100, 2)
Write-Output "Disk C (After clean): Free: $cFreeGBAfter GB ($cFreePctAfter % free)"

Write-Output ""
Write-Output "--- TOP 10 PROCESSES BY RAM (WORKING SET) ---"
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10 Id, ProcessName, @{Name="RAM_MB";Expression={[math]::Round($_.WorkingSet / 1MB, 2)}}, @{Name="Path";Expression={try {$_.MainModule.FileName} catch {"N/A (Access/Protected)"}}} | Format-Table -AutoSize | Out-String | Write-Output

Write-Output ""
Write-Output "--- TOP 10 PROCESSES BY CPU (TOTAL SECONDS) ---"
Get-Process | Where-Object { $_.CPU -gt 0 } | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName, @{Name="CPU_Sec";Expression={[math]::Round($_.CPU, 2)}}, @{Name="RAM_MB";Expression={[math]::Round($_.WorkingSet / 1MB, 2)}} | Format-Table -AutoSize | Out-String | Write-Output

Write-Output ""
Write-Output "--- SUSPICIOUS PROCESS SCAN (RUNNING FROM TEMP OR USER PROFILE DIRECTORIES) ---"
$suspicious = Get-Process | ForEach-Object {
    try {
        $p = $_.MainModule.FileName
        if ($p -and (($p -like "*\Temp\*") -or ($p -like "*\AppData\Local\Temp\*"))) {
            $_
        }
    } catch {}
}
if ($suspicious) {
    Write-Output "[WARN] Found processes running from Temp paths:"
    $suspicious | Select-Object Id, ProcessName, Path | Format-Table -AutoSize | Out-String | Write-Output
} else {
    Write-Output "[OK] No processes running from Temp directories found."
}
