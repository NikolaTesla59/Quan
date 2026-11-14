import subprocess

# Check adb devices if adb is present
try:
    adb_res = subprocess.run(["adb", "devices"], capture_output=True, text=True, timeout=3)
    print("ADB Output:\n", adb_res.stdout)
except Exception as e:
    print("ADB not available or error:", e)

# Check WMI / PnP devices via PowerShell without variable expansion issues
ps_cmd = 'Get-CimInstance Win32_PnPEntity | Where-Object { $_.PNPClass -in "WPD","AndroidUsbDeviceClass","USB" -or $_.Name -match "Phone|Android|Apple|Galaxy|Xiaomi|Oppo|Vivo|Realme" } | Select-Object Name, PNPClass, Status | Format-Table -AutoSize'

try:
    res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True, text=True, timeout=10)
    print("PnP Devices:\n", res.stdout)
except Exception as e:
    print("PnP Error:", e)
