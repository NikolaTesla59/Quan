import urllib.request
import json

url = "https://api.github.com/repos/ggerganov/llama.cpp/releases/latest"
headers = {'User-Agent': 'Mozilla/5.0'}
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        assets = [a['name'] for a in data.get('assets', [])]
        for a in assets:
            print(a)
except Exception as e:
    print("Error:", e)
