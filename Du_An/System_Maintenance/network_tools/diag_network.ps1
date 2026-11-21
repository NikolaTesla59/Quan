Write-Host "=== 1. NETWORK ADAPTERS ===" -ForegroundColor Cyan
Get-NetAdapter | Where-Object Status -eq 'Up' | Format-Table Name, InterfaceDescription, Status, LinkSpeed

Write-Host "=== 2. IP CONFIGURATION ===" -ForegroundColor Cyan
Get-NetIPConfiguration | Format-List InterfaceAlias, IPv4Address, IPv4DefaultGateway, DNSServer

Write-Host "=== 3. WI-FI SIGNAL & STATS ===" -ForegroundColor Cyan
netsh wlan show interfaces

Write-Host "=== 4. PING ROUTER & INTERNET & PHONE ===" -ForegroundColor Cyan
$targets = @('192.168.1.1', '8.8.8.8', '1.1.1.1', '192.168.1.104')
foreach ($t in $targets) {
    $p = Test-Connection -ComputerName $t -Count 3 -ErrorAction SilentlyContinue
    if ($p) {
        $avg = ($p | Measure-Object -Property ResponseTime -Average).Average
        Write-Host ("Ping to {0}: OK (Avg: {1:N1} ms)" -f $t, $avg) -ForegroundColor Green
    } else {
        Write-Host ("Ping to {0}: FAILED / TIMEOUT" -f $t) -ForegroundColor Red
    }
}

Write-Host "=== 5. ADB DEVICES & LOCAL PORTS ===" -ForegroundColor Cyan
adb devices
Get-NetTCPConnection -State Listen | Where-Object LocalPort -in 8080, 5000, 8022 | Format-Table LocalAddress, LocalPort, State, OwningProcess

Write-Host "=== 6. TOP NETWORK PROCESSES ===" -ForegroundColor Cyan
Get-NetTCPConnection -State Established | Group-Object OwningProcess | Sort-Object Count -Descending | Select-Object -First 5 Count, @{N="Process";E={(Get-Process -Id $_.Name -ErrorAction SilentlyContinue).ProcessName}}, @{N="PID";E={$_.Name}} | Format-Table
