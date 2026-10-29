$procs = Get-Process | Sort-Object CPU -Descending | Select-Object -First 8
Write-Output "=== TOP CPU PROCESSES ==="
foreach ($p in $procs) {
    Write-Output ("{0,-25} PID:{1,-6} CPU:{2,8:N1}s RAM:{3,7:N1}MB" -f $p.ProcessName, $p.Id, $p.CPU, ($p.WorkingSet64 / 1MB))
}

Write-Output ""
Write-Output "=== THERMAL & CLOCK STATUS ==="
$curSpeed = (Get-CimInstance Win32_Processor).CurrentClockSpeed
$maxSpeed = (Get-CimInstance Win32_Processor).MaxClockSpeed
Write-Output "Current CPU Clock: $curSpeed MHz / Max: $maxSpeed MHz"

# Try reading MSAcpi_ThermalZoneTemperature if available
$thermal = Get-CimInstance -Namespace "root/wmi" -ClassName "MSAcpi_ThermalZoneTemperature" -ErrorAction SilentlyContinue
if ($thermal) {
    foreach ($t in $thermal) {
        $celsius = ($t.CurrentTemperature - 2732) / 10.0
        Write-Output "Thermal Zone $($t.InstanceName): $celsius °C"
    }
} else {
    Write-Output "Thermal Zone sensor query via WMI: Not exposed by Dell Insyde BIOS."
}
