from pynput.mouse import Controller
from pynput import keyboard

mouse = Controller()

def function_1():
    print(mouse.position)

with keyboard.GlobalHotKeys({
    '<shift>+f': function_1}) as h:
    h.join()