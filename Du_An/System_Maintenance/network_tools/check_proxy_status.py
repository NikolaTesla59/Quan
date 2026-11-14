import winreg
import urllib.request
import json

# Check registry proxy
try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings")
    proxy_enable, _ = winreg.QueryValueEx(key, "ProxyEnable")
    proxy_server, _ = winreg.QueryValueEx(key, "ProxyServer")
    print(f"ProxyEnable: {proxy_enable}, ProxyServer: {proxy_server}")
except Exception as e:
    print("Registry check error:", e)

# Check direct python request (with default system proxy)
try:
    with urllib.request.urlopen("http://ip-api.com/json", timeout=5) as resp:
        data = json.loads(resp.read().decode())
        print("System IP check:", data.get("query"), data.get("country"))
except Exception as e:
    print("IP check error:", e)
