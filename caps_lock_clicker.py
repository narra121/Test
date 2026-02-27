import pyautogui
import time

print("Starting Caps Lock double-press every minute. Press Ctrl+C to stop.")

try:
    while True:
        pyautogui.press('capslock')
        time.sleep(0.1)
        pyautogui.press('capslock')
        print(f"Caps Lock pressed twice at {time.strftime('%H:%M:%S')}")
        time.sleep(60)
except KeyboardInterrupt:
    print("Stopped servie.")


def main():
    pass