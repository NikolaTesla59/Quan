import urllib.request
import json

# Check if termux packages have llama.cpp
url = "https://raw.githubusercontent.com/termux/termux-packages/master/packages/llama.cpp/build.sh"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=5) as resp:
        print("llama.cpp in termux-packages:", resp.status)
except Exception as e:
    print("llama.cpp check error:", e)
