# Script to disable unnecessary background startup apps and services

Write-Host "=== 1. DISABLING CHROME AUTOLAUNCH ===" -ForegroundColor Cyan
$chromeRunPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$props = Get-ItemProperty $chromeRunPath
foreach ($p in $props.PSObject.Properties) {
    if ($p.Name -like "GoogleChromeAutoLaunch*") {
        Remove-ItemProperty -Path $chromeRunPath -Name $p.Name -Force -ErrorAction SilentlyContinue
        Write-Host "Removed Chrome auto-launch key: $($p.Name)" -ForegroundColor Green
    }
}

# Ensure Chrome doesn't keep running in background when closed
$chromePolicyPath = "HKLM:\SOFTWARE\Policies\Google\Chrome"
if (-not (Test-Path $chromePolicyPath)) {
    New-Item -Path $chromePolicyPath -Force | Out-Null
}
Set-ItemProperty -Path $chromePolicyPath -Name "BackgroundModeEnabled" -Value 0 -Type DWord -Force
Write-Host "Configured Chrome BackgroundModeEnabled = 0." -ForegroundColor Green


Write-Host "`n=== 2. DISABLING CLOUDFLARE WARP AUTOSTART ===" -ForegroundColor Cyan
$warpRunPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"
$warpProp = (Get-ItemProperty $warpRunPath -Name "CloudflareWARP" -ErrorAction SilentlyContinue)
if ($warpProp) {
    Remove-ItemProperty -Path $warpRunPath -Name "CloudflareWARP" -Force -ErrorAction SilentlyContinue
    Write-Host "Removed Cloudflare WARP from Windows Startup." -ForegroundColor Green
}

# Stop WARP GUI tray process to immediately free RAM
$warpProc = Get-Process -Name "Cloudflare WARP" -ErrorAction SilentlyContinue
if ($warpProc) {
    Stop-Process -Id $warpProc.Id -Force -ErrorAction SilentlyContinue
    Write-Host "Stopped running Cloudflare WARP tray process." -ForegroundColor Green
}


Write-Host "`n=== 3. CONFIGURING ULTRAVIEWER SERVICE ===" -ForegroundColor Cyan
$uvSvc = Get-Service -Name "UltraViewService" -ErrorAction SilentlyContinue
if ($uvSvc) {
    Set-Service -Name "UltraViewService" -StartupType Manual -ErrorAction SilentlyContinue
    if ($uvSvc.Status -eq "Running") {
        Stop-Service -Name "UltraViewService" -Force -ErrorAction SilentlyContinue
        Write-Host "Set UltraViewer Service to MANUAL and stopped background running." -ForegroundColor Green
    } else {
        Write-Host "Set UltraViewer Service to MANUAL." -ForegroundColor Green
    }
}


Write-Host "`n=== 4. CONFIGURING FOXIT READER UPDATE SERVICE ===" -ForegroundColor Cyan
$foxitSvc = Get-Service -Name "FoxitReaderUpdateService" -ErrorAction SilentlyContinue
if ($foxitSvc) {
    Set-Service -Name "FoxitReaderUpdateService" -StartupType Disabled -ErrorAction SilentlyContinue
    if ($foxitSvc.Status -eq "Running") {
        Stop-Service -Name "FoxitReaderUpdateService" -Force -ErrorAction SilentlyContinue
        Write-Host "Set Foxit Update Service to DISABLED and stopped." -ForegroundColor Green
    } else {
        Write-Host "Set Foxit Update Service to DISABLED." -ForegroundColor Green
    }
}


Write-Host "`n=== 5. VERIFICATION ===" -ForegroundColor Cyan
Write-Host "Services status:"
Get-Service -Name "UltraViewService", "FoxitReaderUpdateService" -ErrorAction SilentlyContinue | Select-Object Name, DisplayName, Status, StartType | Format-Table -AutoSize
