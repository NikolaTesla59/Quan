# Windows System Maintenance Script
Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

function Get-DirSizeMB ($dirPath) {
    if (Test-Path $dirPath) {
        $files = Get-ChildItem -Path $dirPath -Recurse -Force -File -ErrorAction SilentlyContinue
        if ($files) {
            $totalBytes = ($files | Measure-Object -Property Length -Sum).Sum
            if ($totalBytes) {
                return [math]::Round($totalBytes / 1MB, 2)
            }
        }
    }
    return 0.0
}

Write-Output "[1/5] Thu thap thong so he thong truoc don dep..."
$diskC = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$cTotalGB = [math]::Round($diskC.Size / 1GB, 2)
$cFreeBeforeGB = [math]::Round($diskC.FreeSpace / 1GB, 2)
$cUsedBeforeGB = [math]::Round(($diskC.Size - $diskC.FreeSpace) / 1GB, 2)

$userTempPath = $env:TEMP
$winTempPath = "C:\Windows\Temp"

$userTempBeforeMB = Get-DirSizeMB $userTempPath
$winTempBeforeMB = Get-DirSizeMB $winTempPath

Write-Output "Dung luong o C truoc don: Total = $cTotalGB GB, Used = $cUsedBeforeGB GB, Free = $cFreeBeforeGB GB"
Write-Output "User Temp truoc don: $userTempBeforeMB MB"
Write-Output "Windows Temp truoc don: $winTempBeforeMB MB"

Write-Output "`n[2/5] Don dep file rac trong $userTempPath va $winTempPath..."

# Count files before
$userTempFilesBefore = @(Get-ChildItem -Path $userTempPath -Recurse -Force -ErrorAction SilentlyContinue).Count
$winTempFilesBefore = @(Get-ChildItem -Path $winTempPath -Recurse -Force -ErrorAction SilentlyContinue).Count

# Delete user temp
$deletedUserCount = 0
Get-ChildItem -Path $userTempPath -Force -ErrorAction SilentlyContinue | ForEach-Object {
    try {
        Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction Stop
        $deletedUserCount++
    } catch {
        # File/folder is in use by a running process
    }
}

# Delete windows temp
$deletedWinCount = 0
Get-ChildItem -Path $winTempPath -Force -ErrorAction SilentlyContinue | ForEach-Object {
    try {
        Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction Stop
        $deletedWinCount++
    } catch {
        # File/folder is in use or requires elevation
    }
}

$userTempAfterMB = Get-DirSizeMB $userTempPath
$winTempAfterMB = Get-DirSizeMB $winTempPath

Write-Output "Don dep User Temp hoan tat. Con lai: $userTempAfterMB MB (cac tep dang duoc tien trinh su dung)."
Write-Output "Don dep Windows Temp hoan tat. Con lai: $winTempAfterMB MB (cac tep he thong dang su dung)."

Write-Output "`n[3/5] Xoa cache DNS (ipconfig /flushdns)..."
$dnsOutput = & ipconfig /flushdns
Write-Output ($dnsOutput -join "`n")

Write-Output "`n[4/5] Kiem tra lai dung luong o dia C..."
$diskCAfter = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$cFreeAfterGB = [math]::Round($diskCAfter.FreeSpace / 1GB, 2)
$cUsedAfterGB = [math]::Round(($diskCAfter.Size - $diskCAfter.FreeSpace) / 1GB, 2)
$freedGB = [math]::Round($cFreeAfterGB - $cFreeBeforeGB, 3)

Write-Output "Dung luong o C sau don: Total = $cTotalGB GB, Used = $cUsedAfterGB GB, Free = $cFreeAfterGB GB"
Write-Output "Dung luong giai phong tren o C: $freedGB GB"

Write-Output "`n[5/5] Quet danh sach tien trinh nguyen RAM / CPU..."
Write-Output "--- TOP 10 TIEN TRINH SU DUNG RAM NHIEU NHAT ---"
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Id, ProcessName, @{Name="RAM_MB"; Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}}, @{Name="CPU_Sec"; Expression={[math]::Round($_.CPU, 2)}}, Path | Format-Table -AutoSize

Write-Output "--- TOP 10 TIEN TRINH SU DUNG CPU NHIEU NHAT (Tich luy) ---"
Get-Process | Where-Object { $_.CPU -ne $null } | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName, @{Name="CPU_Sec"; Expression={[math]::Round($_.CPU, 2)}}, @{Name="RAM_MB"; Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}}, Path | Format-Table -AutoSize

Write-Output "`n=== KET THUC BAO TRI HE THONG ==="
