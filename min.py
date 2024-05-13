import time

from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

print("LMB at next mouse position when Enter pressed")

mouse = Controller()
coords = None


def press(key):
    if isinstance(key, Key) and key == Key.enter:
        print(f"Clicking at {mouse.position}")
        global coords
        coords = mouse.position
        return False


with Listener(on_press=press, suppress=True) as l:
    l.join()

listener = Listener(on_press=lambda x: isinstance(x, Key) and x != Key.esc, suppress=True)
listener.start()

print("Press Esc again to exit")
while listener.running:
    prev = mouse.position
    mouse.position = coords
    mouse.click(Button.left)
    mouse.position = prev
    time.sleep(1.5)

