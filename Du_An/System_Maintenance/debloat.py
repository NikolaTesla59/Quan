import subprocess

pkgs = [
    'com.miui.msa.global',
    'com.miui.analytics',
    'com.miui.daemon',
    'com.miui.bugreport',
    'com.miui.hybrid'
]

for p in pkgs:
    res = subprocess.run(f"adb shell pm uninstall -k --user 0 {p}", shell=True, capture_output=True, text=True)
    print(f"Uninstall {p}: {res.stdout.strip()} {res.stderr.strip()}")
