# Chris Landadio 2/21/21

# Use this to program the locations for the other scripts.
# Once you program the ULBBCorner, close the script, because it will keep overwriting the last given value
# Run the script and follow the prompts and it should work fine

import configparser, sys, time
from pynput import keyboard
from pynput.mouse import Controller

cf = configparser.ConfigParser()
mouse = Controller()
filepath = r'H:\Aero\Python\Movement_Coordinates.ini'
hotkey = 'S'
iteration = 0

cf['Coordinates'] = {}
cf['Bounding Box Size'] = {'size' : '(200, 100)'}
cf['Screen Resolution'] = {'res' : '(1366, 768)'}

def setting():
    global iteration
    try:
        print(f'Move mouse to {poslist[iteration+1]} and click {hotkey} when ready')
        cf['Coordinates'][poslist[iteration]] = str(mouse.position)
        iteration += 1
        print(iteration)
    except:
        print(poslist[iteration])
        cf['Coordinates'][poslist[iteration]] = str(mouse.position)
        with open(filepath, mode='w', encoding='utf-8') as config:
            cf.write(config)
        print('Positions all defined, script will exit in 3 seconds')
        time.sleep(3)
        sys.exit()
       
    with open(filepath, mode='w', encoding='utf-8') as config:
        cf.write(config)

print(f'Move mouse to Relay 0 High Position and click {hotkey} when ready')

poslist = ['relay_high_pos','relay_low_pos','quicktab_pos','servotab_pos','glider_pos','payload_pos', 'ULBBCorner']

def hi():           # debugging
    print('hi')

# The following hotkeys can be changed to whatever

with keyboard.GlobalHotKeys({
        'S' : setting,
        'd' : hi}) as h:
    h.join()