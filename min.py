import argparse
import time

import pyautogui

parser = argparse.ArgumentParser(
    prog="Minimal autoclicker",
    description="Click in one place at an interval",
)
parser.add_argument("x", help="X coordinate to click at")
parser.add_argument("y", help="Y coordinate to click at")
parser.add_argument("time", help="Interval to click at (ms)")

args = parser.parse_args()


while True:
    try:
        pyautogui.click(x=args.x, y=args.y)
        time.sleep(args.time / 100)
    except KeyboardInterrupt:
        print("bye")
        break
