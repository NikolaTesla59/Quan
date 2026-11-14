import urllib.request
import json

urls = {
    "Urban_VPN_Extension": "https://chromewebstore.google.com/detail/urban-vpn-proxy/eppiocemhmnlbhjplcgkfeedignmkgam",
    "Touch_VPN_Extension": "https://chromewebstore.google.com/detail/touch-vpn-secure-and-unl/bihmplhobchoageeokmgbdihknkjbknd",
    "SoftEther_VPN": "https://www.vpngate.net/en/download.aspx",
    "Urban_VPN_PC": "https://www.urban-vpn.com/free-products/free-windows-vpn/"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"{name}: {resp.status} OK")
    except Exception as e:
        print(f"{name}: {e}")
