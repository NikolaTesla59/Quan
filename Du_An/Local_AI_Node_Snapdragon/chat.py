import urllib.request
import json
import sys
import os
import time

def find_working_endpoint():
    """Kiem tra va tim endpoint hoat dong: USB (127.0.0.1) hoac Wi-Fi (192.168.1.104)"""
    # 1. Thu kich hoat adb forward cho USB
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

def chat():
    print("=" * 65)
    print("  LOCAL AI NODE - SNAPDRAGON 8+ GEN 1 (QWEN 2.5 CODER 7B)")
    print("  Kiem tra ket noi toi Xiaomi 12S Pro...")
    print("=" * 65)
    
    mode_name, base_url = find_working_endpoint()
    
    if not base_url:
        print("[!] Khong the ket noi toi dien thoai qua USB lan Wi-Fi!")
        print("    - Neu cam cap USB: Hay kiem tra xem day cap co tiep xuc tot khong.")
        print("    - Neu qua Wi-Fi: Dam bao dien thoai va PC cung bat chung mang Wi-Fi.")
        print("    - Kiem tra ung dung Termux tren dien thoai co dang chay khong.")
        input("\nNhan Enter de thoat...")
        return

    print(f"[+] Ket noi THANH CONG qua: {mode_name} -> {base_url}")
    print("[+] Model: Qwen2.5-Coder-7B-Instruct (Snapdragon 8+ Gen 1 NPU/CPU)")
    print("[+] Go 'exit' hoac 'quit' de thoat.\n" + "-" * 65)

    url = f"{base_url}/v1/chat/completions"
    history = [
        {"role": "system", "content": "Ban la tro ly AI thong minh chay truc tiep tren chip Qualcomm Snapdragon 8+ Gen 1 cua dien thoai Xiaomi 12S Pro. Hay tra loi chinh xac, co dong va huu ich bang tieng Viet."}
    ]
    
    while True:
        try:
            user_input = input("\n[Ban]: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit", "q"):
                print("\nTam biet!")
                break
                
            history.append({"role": "user", "content": user_input})
            payload = {
                "messages": history,
                "temperature": 0.7,
                "max_tokens": 512,
                "stream": True
            }
            
            headers = {"Content-Type": "application/json"}
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
            
            print("[Snapdragon 8+ Gen 1]: ", end="", flush=True)
            bot_reply = ""
            start_t = time.time()
            first_token = True
            
            with urllib.request.urlopen(req, timeout=180) as resp:
                for line in resp:
                    line = line.decode('utf-8').strip()
                    if not line or not line.startswith("data: "):
                        continue
                    data_str = line[6:]
                    if data_str == "[DONE]":
                        break
                    try:
                        data = json.loads(data_str)
                        content = data["choices"][0].get("delta", {}).get("content", "")
                        if content:
                            if first_token:
                                ttft = time.time() - start_t
                                first_token = False
                            print(content, end="", flush=True)
                            bot_reply += content
                    except Exception:
                        pass
            print()
            history.append({"role": "assistant", "content": bot_reply})
            
        except KeyboardInterrupt:
            print("\nDa huy.")
            break
        except Exception as e:
            print(f"\n[!] Loi ket noi: {e}")
            mode_name, base_url = find_working_endpoint()
            if base_url:
                url = f"{base_url}/v1/chat/completions"
                print(f"[*] Da khoi phuc ket noi qua: {mode_name} ({base_url})")

if __name__ == "__main__":
    chat()
