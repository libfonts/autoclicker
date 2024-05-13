import argparse
import time

from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

parser = argparse.ArgumentParser(
    prog="Not so minimal autoclicker",
    description="Click in multiple specified places at a specified interval",
)
parser.add_argument(
    "time",
    metavar='T',
    nargs="?",
    default=1500,
    type=int,
    help="Interval to click at in miliseconds (default: 1500)"
)

args = parser.parse_args()

mouse = Controller()
locs = []

def press(key):
    if not isinstance(key, Key): return 

    if key == Key.enter:
        locs.append(mouse.position)
        print(f"Added {mouse.position} to selection")
    elif key == Key.esc:
        print("Ending selection")
        print("Selected:", locs)
        return False

print("Enter to select, Esc to exit selection")
with Listener(on_press=press, suppress=True) as l:
    l.join()

listener = Listener(on_press=lambda x: isinstance(x, Key) and x != Key.esc, suppress=True)
listener.start()

print("Press Esc again to exit")
while listener.running:
    prev = mouse.position
    for pos in locs:
        mouse.position = pos
        mouse.click(Button.left)
    mouse.position = prev
    time.sleep(args.time / 1000)
