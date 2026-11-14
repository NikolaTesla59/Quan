import subprocess
import time
import sys

def run(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8', errors='ignore')

print("1. Launching Termux...")
run("adb shell am start -n com.termux/.app.TermuxActivity")
time.sleep(1.5)

focus = run("adb shell \"dumpsys window | grep mCurrentFocus\"")
print("Focus:", focus.strip())

if "com.termux" in focus:
    print("2. Sending command to Termux...")
    run("adb shell input text 'bash'")
    run("adb shell input keyevent 62")
    run("adb shell input text 'start_ai.sh'")
    run("adb shell input keyevent 66")
    time.sleep(2)
    print("3. Checking processes...")
    ps = run("adb shell \"ps -A | grep llama-server\"")
    print("llama-server ps output:\n", ps)
else:
    print("Error: Termux is not focused!")
