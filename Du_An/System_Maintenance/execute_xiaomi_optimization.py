import subprocess
import time
import sys

def run_adb(cmd, timeout=30):
    full_cmd = f"adb {cmd}"
    try:
        res = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return res.returncode, res.stdout.strip(), res.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, "", "Timeout"
    except Exception as e:
        return -1, "", str(e)

print("===============================================================================")
print("TIẾN TRÌNH TỐI ƯU HÓA & CÀI TIẾNG VIỆT CHO XIAOMI 12S PRO (SNAPDRAGON 8+ GEN 1)")
print("===============================================================================")

# 1. Kiểm tra trạng thái thiết bị
code, out, err = run_adb("devices")
print("Trạng thái ADB hiện tại:\n", out)

if "unauthorized" in out:
    print("\n[CHÚ Ý] Thiết bị đang ở trạng thái 'UNAUTHORIZED'!")
    print("Màn hình điện thoại đang hiện pop-up: 'Allow USB debugging?'")
    print("Vui lòng tích vào ô 'Always allow from this computer' và bấm 'OK' trên màn hình điện thoại!")
    # Chờ tối đa 25 giây cho người dùng bấm OK
    for i in range(25):
        time.sleep(1)
        code, out, err = run_adb("devices")
        if "device\n" in out or out.endswith("device"):
            print("\n[XÁC NHẬN] Đã cấp quyền thành công!")
            break
    else:
        print("\n[DỪNG] Chưa nhận được thao tác bấm OK trên màn hình điện thoại.")
        sys.exit(2)

code, out, err = run_adb("devices")
if "device" not in out:
    print("[LỖI] Không tìm thấy thiết bị ở trạng thái 'device'.")
    sys.exit(1)

# 2. Đọc thông tin thiết bị
_, model, _ = run_adb("shell getprop ro.product.model")
_, android_ver, _ = run_adb("shell getprop ro.build.version.release")
_, miui_ver, _ = run_adb("shell getprop ro.build.version.incremental")
_, codename, _ = run_adb("shell getprop ro.product.device")

print(f"\n[THÔNG TIN THIẾT BỊ]")
print(f"  + Model: {model} (Codename: {codename})")
print(f"  + Android Version: {android_ver}")
print(f"  + ROM Version: {miui_ver}")

# 3. Cài đặt Locale Tiếng Việt
print("\n[BƯỚC 1/5] Cài đặt Locale Tiếng Việt (vi-VN)...")
run_adb("shell setprop persist.sys.locale vi-VN")
run_adb("shell setprop persist.sys.language vi")
run_adb("shell setprop persist.sys.country VN")
run_adb("shell settings put system system_locales vi-VN")
run_adb("shell settings put global system_locales vi-VN")
print("  -> Đã ép cấu hình ngôn ngữ Tiếng Việt (vi-VN) cho toàn bộ ứng dụng!")

# 4. Vô hiệu hóa Joyose (Gỡ bóp xung Snapdragon 8+ Gen 1)
print("\n[BƯỚC 2/5] Vô hiệu hóa daemon 'Joyose' (Chống bóp xung & hạ FPS khi chơi game)...")
code, out, err = run_adb("shell pm disable-user --user 0 com.xiaomi.joyose")
print(f"  -> Kết quả Joyose: {out or err}")

# 5. Debloat quảng cáo ngầm & Telemetry
print("\n[BƯỚC 3/5] Vô hiệu hóa quảng cáo & dịch vụ theo dõi ngầm...")
bloatware = [
    "com.miui.msa.global",
    "com.miui.analytics",
    "com.miui.daemon",
    "com.miui.bugreport",
    "com.miui.hybrid"
]
for pkg in bloatware:
    code, out, err = run_adb(f"shell pm disable-user --user 0 {pkg}")
    print(f"  -> Tắt {pkg}: {out or err}")

# 6. Tối ưu Animation 0.5x & Refresh Rate 120Hz
print("\n[BƯỚC 4/5] Tối ưu tốc độ giao diện 0.5x & Tần số quét 120Hz...")
run_adb("shell settings put global window_animation_scale 0.5")
run_adb("shell settings put global transition_animation_scale 0.5")
run_adb("shell settings put global animator_duration_scale 0.5")
run_adb("shell settings put system min_refresh_rate 120.0")
print("  -> Đã thiết lập Animation 0.5x và khóa tần số quét mượt mà 120Hz!")

# 7. Dọn dẹp cache
print("\n[BƯỚC 5/5] Dọn dẹp bộ nhớ đệm cache hệ thống...")
code, out, err = run_adb("shell pm trim-caches 1000G")
print(f"  -> Dọn dẹp cache: {out or 'Hoàn tất'}")

print("\n===============================================================================")
print("HOÀN TẤT 100% TIẾN TRÌNH TỐI ƯU HÓA VÀ CÀI TIẾNG VIỆT CHO XIAOMI 12S PRO!")
print("===============================================================================")
