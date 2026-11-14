#!/data/data/com.termux/files/usr/bin/bash
BIN="$HOME/ai-node/llama.cpp/build/bin/llama-server"
LOG="/sdcard/Download/version.log"
$BIN --version > "$LOG" 2>&1
echo "EXIT: $?" >> "$LOG"
