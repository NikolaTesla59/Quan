$cs = Get-CimInstance Win32_ComputerSystem
$bb = Get-CimInstance Win32_BaseBoard
$cpu = Get-CimInstance Win32_Processor
$gpu = Get-CimInstance Win32_VideoController
$ram = Get-CimInstance Win32_PhysicalMemory
$battery = Get-CimInstance Win32_Battery -ErrorAction SilentlyContinue
$os = Get-CimInstance Win32_OperatingSystem
$disks = Get-CimInstance Win32_LogicalDisk | Where-Object { $_.DriveType -eq 3 }
$power = powercfg /getactivescheme

Write-Output "=== SYSTEM SPECIFICATIONS ==="
Write-Output "Manufacturer: $($cs.Manufacturer)"
Write-Output "Model: $($cs.Model)"
Write-Output "System Type: $($cs.SystemType)"
Write-Output "Baseboard: $($bb.Manufacturer) - $($bb.Product)"
Write-Output "Is Laptop: $(if ($battery) { 'Yes (Battery detected)' } else { 'No / Desktop' })"
Write-Output ""
Write-Output "=== CPU ==="
Write-Output "CPU Name: $($cpu.Name)"
Write-Output "Cores: $($cpu.NumberOfCores), Threads: $($cpu.NumberOfLogicalProcessors)"
Write-Output "Max Clock Speed: $($cpu.MaxClockSpeed) MHz"
Write-Output ""
Write-Output "=== GPU ==="
foreach ($g in $gpu) {
    Write-Output "GPU: $($g.Name), Driver: $($g.DriverVersion), VRAM: $([math]::Round($g.AdapterRAM / 1GB, 2)) GB"
}
Write-Output ""
Write-Output "=== MEMORY (RAM) ==="
$totalRam = ($ram | Measure-Object Capacity -Sum).Sum / 1GB
Write-Output "Total RAM: $([math]::Round($totalRam, 2)) GB"
foreach ($r in $ram) {
    Write-Output "Stick: $($r.DeviceLocator), Capacity: $([math]::Round($r.Capacity / 1GB, 2)) GB, Speed: $($r.Speed) MHz, Configured: $($r.ConfiguredClockSpeed) MHz, Part: $($r.PartNumber.Trim())"
}
Write-Output ""
Write-Output "=== STORAGE ==="
foreach ($d in $disks) {
    Write-Output "Drive $($d.DeviceID): Free $([math]::Round($d.FreeSpace / 1GB, 2)) GB / Total $([math]::Round($d.Size / 1GB, 2)) GB"
}
Write-Output ""
Write-Output "=== POWER SCHEME ==="
Write-Output "$power"
