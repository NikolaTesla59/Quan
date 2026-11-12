import subprocess
import sys

def run(cmd):
    print(f"RUN: {cmd}", flush=True)
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
    out = res.stdout.strip()
    err = res.stderr.strip()
    if out:
        print(f"  OUT: {out}", flush=True)
    if err:
        print(f"  ERR: {err}", flush=True)
    return res.returncode, out, err

print("=== BẮT ĐẦU TỐI ƯU HÓA & CÀI TIẾNG VIỆT CHO XIAOMI 12S PRO ===", flush=True)

# 1. Thông tin máy
run("adb shell getprop ro.product.model")
run("adb shell getprop ro.build.version.release")
run("adb shell getprop ro.build.version.incremental")

# 2. Cài Tiếng Việt cho hệ thống và ứng dụng
print("\n--- 1. CÀI TIẾNG VIỆT CHO HỆ THỐNG VÀ TOÀN BỘ ỨNG DỤNG ---", flush=True)
run("adb shell setprop persist.sys.locale vi-VN")
run("adb shell setprop persist.sys.language vi")
run("adb shell setprop persist.sys.country VN")
run("adb shell settings put system system_locales vi-VN")
run("adb shell settings put global system_locales vi-VN")

# 3. Vô hiệu hóa Joyose (Gỡ bóp xung Snapdragon 8+ Gen 1)
print("\n--- 2. VÔ HIỆU HÓA JOYOSE (CHỐNG BÓP XUNG & CHỐNG TỤT FPS) ---", flush=True)
run("adb shell pm disable-user --user 0 com.xiaomi.joyose")

# 4. Debloat quảng cáo & theo dõi ngầm
print("\n--- 3. DEBLOAT QUẢNG CÁO & DỊCH VỤ NGẦM ---", flush=True)
for pkg in ["com.miui.msa.global", "com.miui.analytics", "com.miui.daemon", "com.miui.bugreport", "com.miui.hybrid"]:
    run(f"adb shell pm disable-user --user 0 {pkg}")

# 5. Tối ưu Animation 0.5x và Refresh Rate 120Hz
print("\n--- 4. TỐI ƯU ANIMATION 0.5X VÀ KHÓA 120HZ ---", flush=True)
run("adb shell settings put global window_animation_scale 0.5")
run("adb shell settings put global transition_animation_scale 0.5")
run("adb shell settings put global animator_duration_scale 0.5")
run("adb shell settings put system min_refresh_rate 120.0")

# 6. Dọn dẹp cache rác
print("\n--- 5. DỌN DẸP BỘ NHỚ ĐỆM CACHE ---", flush=True)
run("adb shell pm trim-caches 1000G")

print("\n=== HOÀN TẤT TOÀN BỘ 100% ===", flush=True)
