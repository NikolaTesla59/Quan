#!/data/data/com.termux/files/usr/bin/bash
BIN="$HOME/ai-node/llama.cpp/build/bin/llama-server"
$BIN --help | grep -i -E 'repack|fit|mmap|cache|ram|mem|weight' > /sdcard/Download/flags.txt
