import urllib.request
import os

dest = r"C:\Users\Admin\Downloads\termux-arm64.apk"
url = "https://github.com/termux/termux-app/releases/download/v0.118.1/termux-app_v0.118.1+github-debug_arm64-v8a.apk"
headers = {'User-Agent': 'Mozilla/5.0'}

print("Downloading Termux APK...")
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=30) as resp, open(dest, "wb") as f:
    chunk_size = 1024 * 1024
    total = 0
    while True:
        chunk = resp.read(chunk_size)
        if not chunk:
            break
        f.write(chunk)
        total += len(chunk)
        print(f"Downloaded {total / (1024*1024):.2f} MB")

print("Download complete, size:", os.path.getsize(dest))
