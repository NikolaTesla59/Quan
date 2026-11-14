import urllib.request
import json
import sys
import time
import os

def find_working_endpoint():
    try:
        os.system("adb forward tcp:8080 tcp:8080 >nul 2>&1")
    except Exception:
        pass
    
    candidates = [
        ("USB Cable (ADB)", "http://127.0.0.1:8080"),
        ("Wi-Fi Local Network", "http://192.168.1.104:8080")
    ]
    
    for name, base_url in candidates:
        try:
            req = urllib.request.Request(f"{base_url}/v1/models", headers={"User-Agent": "AI-Node-Client"})
            with urllib.request.urlopen(req, timeout=3) as resp:
                if resp.status == 200:
                    return name, base_url
        except Exception:
            continue
            
    return None, None

def test_stream():
    mode_name, base_url = find_working_endpoint()
    if not base_url:
        print("[!] Khong the ket noi toi Xiaomi 12S Pro qua USB lan Wi-Fi!")
        return

    print(f"[*] Ket noi thanh cong qua {mode_name} tai {base_url} (Snapdragon 8+ Gen 1)...")
    url = f"{base_url}/v1/chat/completions"
    payload = {
        "messages": [
            {"role": "system", "content": "Ban la bo xu ly AI cuc bo cho Antigravity tren chip Snapdragon 8+ Gen 1. Hay gioi thieu cuc ky ngan gon trong 1-2 cau."},
            {"role": "user", "content": "Chao ban, hay gioi thieu ve chinh minh!"}
        ],
        "temperature": 0.7,
        "max_tokens": 50,
        "stream": True
    }
    
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    
    print("\n" + "="*60)
    print("[AI NODE - XIAOMI 12S PRO DANG PHAN HOI TRUC TIEP]:")
    
    t0 = time.time()
    first_token_time = None
    token_count = 0
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            for line in resp:
                line = line.decode('utf-8').strip()
                if not line or not line.startswith("data: "):
                    continue
                data_str = line[6:]
                if data_str == "[DONE]":
                    break
                try:
                    data = json.loads(data_str)
                    delta = data["choices"][0].get("delta", {})
                    content = delta.get("content", "")
                    if content:
                        if first_token_time is None:
                            first_token_time = time.time() - t0
                        print(content, end="", flush=True)
                        token_count += 1
                except Exception:
                    pass
        
        t_total = time.time() - t0
        print("\n" + "="*60)
        print(f"\n[+] Thoi gian sinh token dau tien (TTFT): {first_token_time:.2f}s")
        print(f"[+] Tong thoi gian: {t_total:.2f}s")
        print(f"[+] So luong token tao ra: {token_count}")
        if token_count > 0 and t_total > 0:
            print(f"[+] Toc do sinh trung binh: {token_count / t_total:.2f} tokens/s")
    except Exception as e:
        print(f"\n[!] Loi ket noi: {e}")

if __name__ == "__main__":
    test_stream()
