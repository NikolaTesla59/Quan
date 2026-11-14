import urllib.request
import json
import sys
import time

def test_ai(base_url="http://localhost:8080"):
    print(f"Connecting to AI Node at {base_url}...")
    url = f"{base_url}/v1/chat/completions"
    payload = {
        "messages": [
            {"role": "system", "content": "Ban la tro ly AI thong minh tren Snapdragon 8+ Gen 1. Hay tra loi that ngan gon trong 1 cau."},
            {"role": "user", "content": "Ban la ai va dang chay tren thiet bi nao?"}
        ],
        "temperature": 0.7,
        "max_tokens": 60
    }
    
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            elapsed = time.time() - t0
            data = json.loads(resp.read().decode('utf-8'))
            reply = data["choices"][0]["message"]["content"]
            usage = data.get("usage", {})
            comp_tokens = usage.get("completion_tokens", 0)
            tok_per_sec = comp_tokens / elapsed if elapsed > 0 else 0
            
            print("\n" + "="*50)
            print("[AI NODE - XIAOMI 12S PRO PHAN HOI]:")
            print(reply)
            print("="*50)
            print(f"Thoi gian phan hoi: {elapsed:.2f}s | So tokens: {comp_tokens} | Toc do: {tok_per_sec:.2f} tok/s")
            print(">>> KET NOI THANH CONG 100%! LOCAL AI NODE DANG HOAT DONG HOAN HAO!")
    except Exception as e:
        print(f"\n[!] Loi ket noi: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080"
    test_ai(target)
