Get-CimInstance Win32_Process | Where-Object { $_.ProcessId -in 13776, 16916 } | Select-Object ProcessId, Name, ExecutablePath, CommandLine, CreationDate | Format-List
