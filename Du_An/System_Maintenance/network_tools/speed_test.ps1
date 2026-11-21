$url = "https://speed.cloudflare.com/__down?bytes=25000000"
$t0 = [System.DateTime]::Now
$wc = New-Object System.Net.WebClient
$wc.DownloadData($url) | Out-Null
$dur = ([System.DateTime]::Now - $t0).TotalSeconds
$mbps = (25 * 8) / $dur
Write-Host "Download Speed: $([math]::Round($mbps, 2)) Mbps (Duration: $([math]::Round($dur, 2))s)" -ForegroundColor Green
