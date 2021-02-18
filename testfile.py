from pynput import keyboard

x = True

def function_1():
    global x
    if x:
        print('x is true')
        x = False
    else:
        print('x is false')
        x = True

with keyboard.GlobalHotKeys({
        'c': function_1}) as h:
    h.join()