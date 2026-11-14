import urllib.request
import ssl
from pathlib import Path

dest = Path(r"C:\Users\Admin\Downloads\UrbanVPN_Setup.exe")
url = "https://cdn.urban-vpn.com/UrbanVPN_Setup.exe"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    print(f"Downloading from {url}...")
    with urllib.request.urlopen(req, context=ctx, timeout=15) as resp, open(dest, "wb") as f:
        f.write(resp.read())
    print(f"Success! Downloaded UrbanVPN_Setup.exe. Size: {dest.stat().st_size} bytes")
except Exception as e:
    print(f"Failed to download from {url}: {e}")
