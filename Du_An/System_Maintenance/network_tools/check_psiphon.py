import urllib.request

urls = [
    "https://psiphon.ca/psiphon3.exe",
    "https://s3.amazonaws.com/psiphon/web/mjr1-p23r-puwl/psiphon3.exe",
    "https://psiphon.ca/en/download.html"
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            print(f"{u} -> {resp.status}, length: {resp.headers.get('Content-Length')}")
    except Exception as e:
        print(f"{u} -> {e}")
