import os
import shutil

def get_folder_size(path):
    total = 0
    if not os.path.exists(path):
        return 0
    try:
        for root, dirs, files in os.walk(path):
            for f in files:
                try:
                    fp = os.path.join(root, f)
                    if not os.path.islink(fp):
                        total += os.path.getsize(fp)
                except Exception:
                    pass
    except Exception:
        pass
    return total

print("=== 1. SYSTEM ROOT FILES (C:\\) ===")
for fname in ['pagefile.sys', 'hiberfil.sys', 'swapfile.sys', 'dumpstack.log']:
    p = os.path.join('C:\\', fname)
    if os.path.exists(p):
        try:
            sz = os.path.getsize(p) / (1024**3)
            print(f"File {fname:20}: {sz:.2f} GB")
        except Exception as e:
            print(f"File {fname:20}: {e}")

print("\n=== 2. COMMON JUNK & CACHE FOLDERS ===")
user_temp = os.environ.get('TEMP', r'C:\Users\Admin\AppData\Local\Temp')
targets = [
    ("User Temp", user_temp),
    ("Windows Temp", r"C:\Windows\Temp"),
    ("Windows Update Download", r"C:\Windows\SoftwareDistribution\Download"),
    ("Recycle Bin (C:\\$Recycle.Bin)", r"C:\$Recycle.Bin"),
    ("User Downloads", r"C:\Users\Admin\Downloads"),
    ("Pip Cache", os.path.expanduser(r"~\AppData\Local\pip\cache")),
    ("Npm Cache", os.path.expanduser(r"~\AppData\Local\npm-cache")),
    ("Gradle Cache", os.path.expanduser(r"~/.gradle/caches")),
    ("CrashDumps", os.path.expanduser(r"~\AppData\Local\CrashDumps")),
    ("Delivery Optimization Cache", r"C:\Windows\SoftwareDistribution\DeliveryOptimization")
]

for label, p in targets:
    sz = get_folder_size(p) / (1024**2) # in MB
    if sz > 1024:
        print(f"{label:30}: {sz/1024:.2f} GB ({p})")
    else:
        print(f"{label:30}: {sz:.1f} MB ({p})")

print("\n=== 3. USER APPDATA TOP SUBFOLDERS ===")
appdata_local = os.path.expanduser(r"~\AppData\Local")
if os.path.exists(appdata_local):
    subdirs = []
    for d in os.listdir(appdata_local):
        dp = os.path.join(appdata_local, d)
        if os.path.isdir(dp):
            s = get_folder_size(dp) / (1024**2)
            subdirs.append((d, s))
    subdirs.sort(key=lambda x: x[1], reverse=True)
    for d, s in subdirs[:10]:
        if s > 100:
            print(f"Local AppData: {d:25} -> {s/1024:.2f} GB" if s > 1024 else f"Local AppData: {d:25} -> {s:.1f} MB")
