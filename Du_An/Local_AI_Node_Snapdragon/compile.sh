#!/data/data/com.termux/files/usr/bin/bash
set -e
echo "======================================================"
echo "    DANG GIAI NEN MA NGUON LLAMA.CPP...               "
echo "======================================================"
mkdir -p ~/ai-node
cd ~/ai-node
rm -rf llama.cpp
tar -xzf /sdcard/Download/llama_src.tar.gz
cd llama.cpp

echo "======================================================"
echo "    DANG BIEN DICH LLAMA-SERVER (SNAPDRAGON 8+ GEN 1)..."
echo "======================================================"
cmake -B build -DGGML_OPENMP=OFF -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release -j8 --target llama-server

echo "======================================================"
echo "    BIEN DICH THANH CONG!                              "
echo "======================================================"
ls -lh build/bin/llama-server
