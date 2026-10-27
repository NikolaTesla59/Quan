$ErrorActionPreference = 'SilentlyContinue'

$cDriveBefore = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'" | Select-Object DeviceID, Size, FreeSpace

function Get-FolderStats($path) {
    if (Test-Path $path) {
        $files = Get-ChildItem -Path $path -Recurse -Force -ErrorAction SilentlyContinue
        $size = ($files | Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum
        $count = ($files | Measure-Object).Count
        if ($null -eq $size) { $size = 0 }
        return [PSCustomObject]@{ Path = $path; Count = $count; SizeBytes = [int64]$size }
    }
    return [PSCustomObject]@{ Path = $path; Count = 0; SizeBytes = 0 }
}

$userTempStatsBefore = Get-FolderStats $env:TEMP
$winTempStatsBefore = Get-FolderStats 'C:\Windows\Temp'

# 1. Clean User Temp
$userTempDeleted = 0
$userTempLocked = 0
Get-ChildItem -Path $env:TEMP -Force -ErrorAction SilentlyContinue | ForEach-Object {
    try {
        Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction Stop
        $userTempDeleted++
    } catch {
        $userTempLocked++
    }
}

# Clean Windows Temp
$winTempDeleted = 0
$winTempLocked = 0
Get-ChildItem -Path 'C:\Windows\Temp' -Force -ErrorAction SilentlyContinue | ForEach-Object {
    try {
        Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction Stop
        $winTempDeleted++
    } catch {
        $winTempLocked++
    }
}

$userTempStatsAfter = Get-FolderStats $env:TEMP
$winTempStatsAfter = Get-FolderStats 'C:\Windows\Temp'

# 2. Flush DNS
$dnsRaw = ipconfig /flushdns
$dnsResult = ($dnsRaw | Where-Object { $_.Trim() -ne '' }) -join ' | '

# 3. Disk After
$cDriveAfter = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'" | Select-Object DeviceID, Size, FreeSpace

# OS & RAM Info
$os = Get-CimInstance Win32_OperatingSystem
$totalRamMB = [math]::Round($os.TotalVisibleMemorySize / 1024, 2)
$freeRamMB = [math]::Round($os.FreePhysicalMemory / 1024, 2)
$usedRamMB = [math]::Round($totalRamMB - $freeRamMB, 2)
$ramPercentUsed = [math]::Round(($usedRamMB / $totalRamMB) * 100, 2)

# Top RAM Processes
$topRam = Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10 Id, ProcessName, @{Name='RAM_MB';Expression={[math]::Round($_.WorkingSet / 1MB, 2)}}, @{Name='CPU_Sec';Expression={[math]::Round($_.CPU, 2)}}

# Top CPU Processes
$topCpu = Get-Process | Where-Object { $_.CPU -gt 0 } | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName, @{Name='RAM_MB';Expression={[math]::Round($_.WorkingSet / 1MB, 2)}}, @{Name='CPU_Sec';Expression={[math]::Round($_.CPU, 2)}}

# Suspicious / High resource processes check (e.g. processes without file description or running from temp/unusual paths)
$heavyProcs = Get-Process | Where-Object { $_.WorkingSet -gt 500MB -or $_.CPU -gt 100 } | Select-Object -First 15 Id, ProcessName, @{Name='RAM_MB';Expression={[math]::Round($_.WorkingSet / 1MB, 2)}}, @{Name='CPU_Sec';Expression={[math]::Round($_.CPU, 2)}}, Path, Description

$report = [PSCustomObject]@{
    DriveBefore = @{
        TotalGB = [math]::Round($cDriveBefore.Size / 1GB, 2)
        FreeGB = [math]::Round($cDriveBefore.FreeSpace / 1GB, 2)
        UsedGB = [math]::Round(($cDriveBefore.Size - $cDriveBefore.FreeSpace) / 1GB, 2)
        PercentFree = [math]::Round(($cDriveBefore.FreeSpace / $cDriveBefore.Size) * 100, 2)
    }
    DriveAfter = @{
        TotalGB = [math]::Round($cDriveAfter.Size / 1GB, 2)
        FreeGB = [math]::Round($cDriveAfter.FreeSpace / 1GB, 2)
        UsedGB = [math]::Round(($cDriveAfter.Size - $cDriveAfter.FreeSpace) / 1GB, 2)
        PercentFree = [math]::Round(($cDriveAfter.FreeSpace / $cDriveAfter.Size) * 100, 2)
    }
    UserTemp = @{
        BeforeMB = [math]::Round($userTempStatsBefore.SizeBytes / 1MB, 2)
        AfterMB = [math]::Round($userTempStatsAfter.SizeBytes / 1MB, 2)
        CleanedMB = [math]::Round(($userTempStatsBefore.SizeBytes - $userTempStatsAfter.SizeBytes) / 1MB, 2)
        ItemsBefore = $userTempStatsBefore.Count
        ItemsAfter = $userTempStatsAfter.Count
        DeletedTopLevel = $userTempDeleted
        LockedTopLevel = $userTempLocked
    }
    WinTemp = @{
        BeforeMB = [math]::Round($winTempStatsBefore.SizeBytes / 1MB, 2)
        AfterMB = [math]::Round($winTempStatsAfter.SizeBytes / 1MB, 2)
        CleanedMB = [math]::Round(($winTempStatsBefore.SizeBytes - $winTempStatsAfter.SizeBytes) / 1MB, 2)
        ItemsBefore = $winTempStatsBefore.Count
        ItemsAfter = $winTempStatsAfter.Count
        DeletedTopLevel = $winTempDeleted
        LockedTopLevel = $winTempLocked
    }
    DnsResult = $dnsResult
    Memory = @{
        TotalGB = [math]::Round($totalRamMB / 1024, 2)
        UsedGB = [math]::Round($usedRamMB / 1024, 2)
        FreeGB = [math]::Round($freeRamMB / 1024, 2)
        PercentUsed = $ramPercentUsed
    }
    TopRam = $topRam
    TopCpu = $topCpu
    HeavyProcesses = $heavyProcs
}

$report | ConvertTo-Json -Depth 6
