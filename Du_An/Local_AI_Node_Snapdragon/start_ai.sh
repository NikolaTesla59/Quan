#!/data/data/com.termux/files/usr/bin/bash

MODEL_FILE="$HOME/ai-node/models/qwen2.5-coder-7b-instruct-q4_k_m.gguf"
SERVER_BIN="$HOME/ai-node/llama.cpp/build/bin/llama-server"
LOG_FILE="/sdcard/Download/llama_server.log"

echo "=== STARTING LLAMA-SERVER ===" > "$LOG_FILE"

$SERVER_BIN \
    -m "$MODEL_FILE" \
    --host 0.0.0.0 \
    --port 8080 \
    -t 4 \
    -c 2048 \
    >> "$LOG_FILE" 2>&1

EXIT_CODE=$?
echo "LLAMA SERVER EXITED WITH CODE: $EXIT_CODE" >> "$LOG_FILE"
