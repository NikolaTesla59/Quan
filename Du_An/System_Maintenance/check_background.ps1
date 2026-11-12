Write-Output "=== 1. STARTUP COMMANDS ==="
Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location, User | Format-Table -AutoSize

Write-Output "=== 2. RUNNING PROCESSES (TOP 15 RAM) ==="
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 15 ProcessName, Id, @{N='RAM_MB';E={[math]::Round($_.WorkingSet64/1MB,1)}}, Path | Format-Table -AutoSize

Write-Output "=== 3. THIRD-PARTY SERVICES ==="
Get-CimInstance Win32_Service | Where-Object { $_.State -eq 'Running' -and $_.PathName -notmatch 'C:\\Windows\\system32' -and $_.PathName -notmatch 'C:\\Windows\\SysWOW64' } | Select-Object Name, DisplayName, StartMode, PathName | Format-Table -AutoSize
