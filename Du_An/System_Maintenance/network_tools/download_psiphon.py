import urllib.request
import os

dest = r"C:\Users\Admin\Downloads\psiphon3.exe"
url = "https://psiphon.ca/psiphon3.exe"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print(f"Downloading {url} to {dest}...")
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=30) as resp, open(dest, 'wb') as f:
    chunk_size = 1024 * 1024
    total = 0
    while True:
        chunk = resp.read(chunk_size)
        if not chunk:
            break
        f.write(chunk)
        total += len(chunk)
        print(f"Downloaded {total / (1024*1024):.2f} MB")

print("Download complete. File size:", os.path.getsize(dest))
