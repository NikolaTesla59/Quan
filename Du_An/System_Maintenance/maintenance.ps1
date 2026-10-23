$ErrorActionPreference = 'SilentlyContinue'

Write-Host "=================================================="
Write-Host "1. KIEM TRA VA XOA FILE RAC (TEMP)"
Write-Host "=================================================="

$userTemp = $env:TEMP
$winTemp = "C:\Windows\Temp"

function Get-FolderSizeMB ($folderPath) {
    if (Test-Path -Path $folderPath) {
        $measure = Get-ChildItem -Path $folderPath -Recurse -Force -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue
        if ($measure -and $measure.Sum) {
            return [math]::Round($measure.Sum / 1MB, 2)
        }
    }
    return 0
}

$userTempBefore = Get-FolderSizeMB $userTemp
$winTempBefore = Get-FolderSizeMB $winTemp
Write-Host ("Dung luong User Temp truoc don dep: " + $userTempBefore + " MB (" + $userTemp + ")")
Write-Host ("Dung luong Windows Temp truoc don dep: " + $winTempBefore + " MB (" + $winTemp + ")")

Write-Host "`nDang tien hanh xoa file rac..."
# Xoa User Temp
Get-ChildItem -Path $userTemp -Force -Recurse -ErrorAction SilentlyContinue | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue

# Xoa Windows Temp
Get-ChildItem -Path $winTemp -Force -Recurse -ErrorAction SilentlyContinue | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue

$userTempAfter = Get-FolderSizeMB $userTemp
$winTempAfter = Get-FolderSizeMB $winTemp
$userFreed = [math]::Round([math]::Max(0, $userTempBefore - $userTempAfter), 2)
$winFreed = [math]::Round([math]::Max(0, $winTempBefore - $winTempAfter), 2)
$totalFreed = [math]::Round($userFreed + $winFreed, 2)

Write-Host ("Dung luong User Temp sau don dep: " + $userTempAfter + " MB (Giai phong: " + $userFreed + " MB)")
Write-Host ("Dung luong Windows Temp sau don dep: " + $winTempAfter + " MB (Giai phong: " + $winFreed + " MB)")
Write-Host ("===> TONG DUNG LUONG DA GIAI PHONG: " + $totalFreed + " MB")
Write-Host "(Luu y: Cac file con lai dang duoc su dung boi cac tien trinh dang chay nen duoc he dieu hanh khoa an toan)"

Write-Host "`n=================================================="
Write-Host "2. XOA CACHE DNS (FLUSHDNS)"
Write-Host "=================================================="
$flushResult = ipconfig /flushdns
$flushResult | ForEach-Object { Write-Host $_ }

Write-Host "`n=================================================="
Write-Host "3. KIEM TRA DUNG LUONG O DIA C:"
Write-Host "=================================================="
$diskC = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$totalGB = [math]::Round($diskC.Size / 1GB, 2)
$freeGB = [math]::Round($diskC.FreeSpace / 1GB, 2)
$usedGB = [math]::Round(($diskC.Size - $diskC.FreeSpace) / 1GB, 2)
$pctFree = [math]::Round(($diskC.FreeSpace / $diskC.Size) * 100, 2)
$pctUsed = [math]::Round(100 - $pctFree, 2)

Write-Host ("O dia: " + $diskC.DeviceID + " (" + $diskC.VolumeName + ")")
Write-Host ("Tong dung luong: " + $totalGB + " GB")
Write-Host ("Da su dung:      " + $usedGB + " GB (" + $pctUsed + "%)")
Write-Host ("Con trong:       " + $freeGB + " GB (" + $pctFree + "%)")

Write-Host "`n=================================================="
Write-Host "4. KIEM TRA RAM VA CAC TIEN TRINH HE THONG"
Write-Host "=================================================="
$os = Get-CimInstance Win32_OperatingSystem
$totalRAM_GB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeRAM_GB = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedRAM_GB = [math]::Round($totalRAM_GB - $freeRAM_GB, 2)
$pctRAM = [math]::Round(($usedRAM_GB / $totalRAM_GB) * 100, 2)
Write-Host ("Tong RAM he thong: " + $totalRAM_GB + " GB")
Write-Host ("RAM dang dung:     " + $usedRAM_GB + " GB (" + $pctRAM + "%)")
Write-Host ("RAM kha dung:      " + $freeRAM_GB + " GB")

Write-Host "`n--- TOP 10 TIEN TRINH CHIEM RAM NHIEU NHAT ---"
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Id, ProcessName, @{Name="RAM_MB"; Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}}, Path | Format-Table -AutoSize

Write-Host "`n--- TOP 10 TIEN TRINH SU DUNG CPU NHIEU NHAT ---"
Get-Process | Where-Object { $_.CPU -gt 0 } | Sort-Object CPU -Descending | Select-Object -First 10 Id, ProcessName, @{Name="Total_CPU_Sec"; Expression={[math]::Round($_.CPU, 2)}}, @{Name="RAM_MB"; Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}} | Format-Table -AutoSize

Write-Host "`n--- KIEM TRA CAC TIEN TRINH CHAY TU THU MUC BAT THUONG (Temp/AppData Roaming exe la) ---"
$suspicious = Get-Process | Where-Object { 
    $_.Path -and (
        $_.Path -like "*\Temp\*" -or 
        $_.Path -like "*\AppData\Local\Temp\*"
    )
} | Select-Object Id, ProcessName, Path, @{Name="RAM_MB"; Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}}

if ($suspicious) {
    Write-Host "CANH BAO: Phat hien tien trinh chay tu thu muc Temp:"
    $suspicious | Format-Table -AutoSize
} else {
    Write-Host "Khong phat hien tien trinh nao dang thuc thi truc tiep tu thu muc Temp."
}
