# Optimize Windows Network Stack & Bandwidth

# 1. Congestion Provider -> CUBIC
try {
    netsh int tcp set supplemental template=custom congestionprovider=cubic
    Set-NetTCPSetting -SettingName InternetCustom -CongestionProvider CUBIC -ErrorAction SilentlyContinue
    Set-NetTCPSetting -SettingName DatacenterCustom -CongestionProvider CUBIC -ErrorAction SilentlyContinue
} catch {
    Write-Warning "TCP congestion setting note: $_"
}

# 2. QoS Reserve Bandwidth -> 0% (Release 20% reserved bandwidth)
$pschedPath = 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\Psched'
if (-not (Test-Path $pschedPath)) {
    New-Item -Path $pschedPath -Force | Out-Null
}
Set-ItemProperty -Path $pschedPath -Name 'NonBestEffortLimit' -Value 0 -Type DWord

# 3. Delivery Optimization -> Disable P2P upload/download (Mode 0: HTTP only / no P2P seeding)
$doPath = 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization'
if (-not (Test-Path $doPath)) {
    New-Item -Path $doPath -Force | Out-Null
}
Set-ItemProperty -Path $doPath -Name 'DODownloadMode' -Value 0 -Type DWord

# 4. Set High-Speed Low-Latency DNS (Cloudflare 1.1.1.1 & Google 8.8.8.8) on Wi-Fi
Set-DnsClientServerAddress -InterfaceAlias 'Wi-Fi' -ServerAddresses @('1.1.1.1', '8.8.8.8', '1.0.0.1')
try {
    Set-DnsClientServerAddress -InterfaceAlias 'Wi-Fi' -ServerAddresses @('2606:4700:4700::1111', '2001:4860:4860::8888') -Family IPv6 -ErrorAction SilentlyContinue
} catch {}

# 5. Flush and reset DNS cache
Clear-DnsClientCache
ipconfig /flushdns

# 6. Verification
Write-Host "=== 1. DNS CONFIGURATION ===" -ForegroundColor Green
Get-DnsClientServerAddress -InterfaceAlias 'Wi-Fi' | Select-Object InterfaceAlias, AddressFamily, ServerAddresses

Write-Host "=== 2. QOS & DELIVERY OPTIMIZATION ===" -ForegroundColor Green
Get-ItemProperty -Path $pschedPath -Name 'NonBestEffortLimit' | Select-Object NonBestEffortLimit
Get-ItemProperty -Path $doPath -Name 'DODownloadMode' | Select-Object DODownloadMode

Write-Host "=== 3. TCP GLOBAL SETTINGS ===" -ForegroundColor Green
netsh int tcp show global
