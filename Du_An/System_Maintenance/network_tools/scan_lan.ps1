$subnet = "192.168.1."
Write-Host "Scanning active devices on $subnet* ..." -ForegroundColor Cyan
100..115 | ForEach-Object {
    $ip = "$subnet$_"
    $res = Test-Connection -ComputerName $ip -Count 1 -Quiet -TimeoutSeconds 1
    if ($res) {
        Write-Host "Device active: $ip" -ForegroundColor Green
    }
}
