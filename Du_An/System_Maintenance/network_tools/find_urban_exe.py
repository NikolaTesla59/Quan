import urllib.request
import re

url = "https://www.urban-vpn.com/free-products/free-windows-vpn/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        exe_links = re.findall(r'href=[\'"]([^\'"]+\.exe[^\'"]*)[\'"]', html, re.IGNORECASE)
        print("Found exe links:", exe_links)
except Exception as e:
    print("Error:", e)
