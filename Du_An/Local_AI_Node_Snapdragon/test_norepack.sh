#!/data/data/com.termux/files/usr/bin/bash
BIN="$HOME/ai-node/llama.cpp/build/bin/llama-server"
MODEL="$HOME/ai-node/models/qwen2.5-coder-7b-instruct-q4_k_m.gguf"
LOG="/sdcard/Download/norepack.log"

echo "=== STARTING WITH --no-repack ===" > "$LOG"
$BIN \
    -m "$MODEL" \
    --no-repack \
    -c 2048 \
    -t 4 \
    --host 0.0.0.0 \
    --port 8080 \
    >> "$LOG" 2>&1 &

PID=$!
echo "LAUNCHED WITH PID: $PID" >> "$LOG"
