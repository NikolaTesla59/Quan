import urllib.request

urls = [
    "https://github.com/termux/termux-app/releases/download/v0.118.1/termux-app_v0.118.1+github-debug_arm64-v8a.apk",
    "https://f-droid.org/repo/com.termux_1020.apk"
]

headers = {'User-Agent': 'Mozilla/5.0'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"{u} -> {resp.status}, size: {resp.headers.get('Content-Length')}")
    except Exception as e:
        print(f"{u} -> {e}")
