#!/data/data/com.termux/files/usr/bin/bash
BIN="$HOME/ai-node/llama.cpp/build/bin/llama-cli"
MODEL="$HOME/ai-node/models/qwen2.5-coder-7b-instruct-q4_k_m.gguf"
LOG="/sdcard/Download/cli_test.log"

echo "=== TESTING LLAMA-CLI ===" > "$LOG"
$BIN -m "$MODEL" -p "Hello" -n 5 -t 4 -c 512 >> "$LOG" 2>&1
echo "EXIT CODE: $?" >> "$LOG"
