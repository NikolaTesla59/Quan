import urllib.request
from bs4 import BeautifulSoup
import json
import time

urls = [
    'https://handbook.bhtcnpm.com/docs/nmlt/lythuyet/chuong1',
    'https://handbook.bhtcnpm.com/docs/nmlt/lythuyet/chuong2',
    'https://handbook.bhtcnpm.com/docs/nmlt/lythuyet/chuong3',
    'https://handbook.bhtcnpm.com/docs/nmlt/lythuyet/chuong4',
    'https://handbook.bhtcnpm.com/docs/nmlt/lythuyet/chuong5',
    'https://handbook.bhtcnpm.com/docs/nmlt/lythuyet/chuong6',
    'https://handbook.bhtcnpm.com/docs/nmlt/lythuyet/chuong7',
    'https://handbook.bhtcnpm.com/docs/oop/lythuyet/chuong1',
    'https://handbook.bhtcnpm.com/docs/oop/lythuyet/chuong2',
    'https://handbook.bhtcnpm.com/docs/oop/lythuyet/chuong3',
    'https://handbook.bhtcnpm.com/docs/oop/lythuyet/chuong4',
    'https://handbook.bhtcnpm.com/docs/dsa/phan1/chuong1',
    'https://handbook.bhtcnpm.com/docs/dsa/phan1/chuong2',
    'https://handbook.bhtcnpm.com/docs/dsa/phan1/chuong3',
    'https://handbook.bhtcnpm.com/docs/dsa/phan2/chuong4',
    'https://handbook.bhtcnpm.com/docs/dsa/phan2/chuong5',
    'https://handbook.bhtcnpm.com/docs/dsa/phan2/chuong6',
    'https://handbook.bhtcnpm.com/docs/dsa/phan2/chuong7',
    'https://handbook.bhtcnpm.com/docs/dsa/phan2/chuong8',
    'https://handbook.bhtcnpm.com/docs/dsa/phan2/chuong9',
    'https://handbook.bhtcnpm.com/docs/csdl/lythuyet/chuong1',
    'https://handbook.bhtcnpm.com/docs/csdl/lythuyet/chuong2',
    'https://handbook.bhtcnpm.com/docs/csdl/lythuyet/chuong3',
    'https://handbook.bhtcnpm.com/docs/csdl/lythuyet/chuong4',
    'https://handbook.bhtcnpm.com/docs/csdl/lythuyet/chuong5',
    'https://handbook.bhtcnpm.com/docs/csdl/lythuyet/chuong6'
]

results = []

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            soup = BeautifulSoup(resp.read().decode('utf-8'), 'html.parser')
            h1 = soup.find('h1')
            h1_text = h1.get_text(strip=True) if h1 else 'No H1'
            h2s = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
            h3s = [h3.get_text(strip=True) for h3 in soup.find_all('h3')]
            article = soup.find('article') or soup.find('main')
            body_text = article.get_text('\n', strip=True) if article else ''
            
            slug = u.replace('https://handbook.bhtcnpm.com/docs/', '')
            results.append({
                'url': u,
                'slug': slug,
                'title': h1_text,
                'h2s': h2s,
                'h3s': h3s,
                'length': len(body_text),
                'summary': body_text[:400]
            })
            print(f"OK: {slug} -> {h1_text}")
    except Exception as e:
        print(f"ERR: {u} -> {e}")

with open('C:/Users/Admin/.gemini/antigravity/scratch/bhtcnpm_handbook/chapters.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Finished saving chapters.json")
