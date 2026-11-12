$cpu = Get-CimInstance Win32_Processor
$ram = Get-CimInstance Win32_PhysicalMemory
$disks = Get-CimInstance Win32_DiskDrive
$cache = Get-CimInstance Win32_CacheMemory

Write-Host "=== CPU INFO ==="
$cpu | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed, L2CacheSize, L3CacheSize | Format-List

Write-Host "=== CACHE INFO ==="
$cache | Select-Object Level, InstalledSize, Purpose, DeviceID | Format-Table

Write-Host "=== RAM INFO ==="
$totalRamGB = ($ram | Measure-Object -Property Capacity -Sum).Sum / 1GB
Write-Host "Total RAM: $([math]::Round($totalRamGB, 2)) GB"
$ram | Select-Object Manufacturer, Capacity, Speed, MemoryType, PartNumber | Format-Table

Write-Host "=== DISK INFO ==="
$disks | Select-Object Model, InterfaceType, MediaType, @{Name="SizeGB";Expression={[math]::Round($_.Size / 1GB, 2)}} | Format-Table
