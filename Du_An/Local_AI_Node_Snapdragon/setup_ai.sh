#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "======================================================"
echo "    KHOI TAO LOCAL AI NODE TREN SNAPDRAGON 8+ GEN 1  "
echo "======================================================"

# 1. Cap nhat va cai dat moi truong bien dich
echo "[1/4] Dang cap nhat goi Termux va cai dat cong cu..."
pkg update -y
pkg install -y git cmake clang make curl wget

# 2. Tao thu muc lam viec
mkdir -p ~/ai-node
cd ~/ai-node

# 3. Tai va bien dich llama.cpp toi uu cho Snapdragon 8+ Gen 1
if [ ! -f ~/ai-node/llama.cpp/build/bin/llama-server ]; then
    echo "[2/4] Dang tai ma nguon llama.cpp..."
    if [ ! -d "llama.cpp" ]; then
        git clone --depth 1 https://github.com/ggerganov/llama.cpp.git
    fi
    cd llama.cpp
    echo "[3/4] Dang bien dich llama-server (tan dung 8 nhan CPU)..."
    cmake -B build -DGGML_OPENMP=OFF -DCMAKE_BUILD_TYPE=Release
    cmake --build build --config Release -j8 --target llama-server
    cd ~/ai-node
else
    echo "[2/4] llama-server da duoc bien dich san!"
fi

# 4. Tao script khoi dong server
cat << 'EOF' > ~/start_ai.sh
#!/data/data/com.termux/files/usr/bin/bash
cd ~/ai-node

# Thu muc chua model
mkdir -p ~/ai-node/models
cd ~/ai-node/models

# Kiem tra va tai model Qwen2.5-Coder neu chua co
MODEL_FILE="qwen2.5-coder-7b-instruct-q4_k_m.gguf"
MODEL_URL="https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF/resolve/main/qwen2.5-coder-7b-instruct-q4_k_m.gguf"

if [ ! -f "$MODEL_FILE" ]; then
    echo "Chua co file model $MODEL_FILE. Dang bat dau tai tu HuggingFace..."
    wget -c "$MODEL_URL" -O "$MODEL_FILE"
fi

echo "======================================================"
echo "  DANG KHOI CHAY LOCAL AI SERVER TREN CONG 8080...    "
echo "  - Model: Qwen2.5-Coder-7B-Instruct                 "
echo "  - Nhan ho tro: 8 luong (Snapdragon 8+ Gen 1)        "
echo "  - Lang nghe: 0.0.0.0:8080 (Ho tro ca USB & Wi-Fi)   "
echo "======================================================"

# Khoi chay llama-server ho tro ca USB va Wi-Fi
~/ai-node/llama.cpp/build/bin/llama-server \
    -m "$MODEL_FILE" \
    --host 0.0.0.0 \
    --port 8080 \
    -t 6 \
    -c 4096 \
    --mlock
EOF

chmod +x ~/start_ai.sh
echo "======================================================"
echo "  DA CAI DAT THANH CONG!                              "
echo "  De khoi dong AI Server, chi can go: bash ~/start_ai.sh "
echo "======================================================"
