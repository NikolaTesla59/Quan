#!/data/data/com.termux/files/usr/bin/bash
BIN="$HOME/ai-node/llama.cpp/build/bin/llama-server"
MODEL="$HOME/ai-node/models/qwen2.5-coder-7b-instruct-q4_k_m.gguf"
LOG="/sdcard/Download/debug.log"

echo "=== START DEBUG RUN ===" > "$LOG"
$BIN -m "$MODEL" -lv 5 -c 512 -t 2 --host 0.0.0.0 --port 8080 > "$LOG" 2>&1
echo "TERMINATED: $?" >> "$LOG"
