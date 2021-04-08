# Chris Landadio 2/23/21

# Use this to program the locations for the other scripts
# Run the script and follow the prompts and it should work fine
# press ESC anytime after the initial y/n/r option to kill the script and not adjust anything

import configparser, sys, time
from pynput import keyboard
from pynput.mouse import Controller

cf = configparser.ConfigParser()
mouse = Controller()
filepath = r'C:\Users\kitty\Desktop\2021 Team\Python\Movement_Coordinates.ini'
data = cf                                   # copy of existing config file in case of no changes
data.read(filepath)                         # defining copy
hotkey = 'S'                                # triggering hotkey for adjusting parameters
iteration = 0                               # iteration count for adjusting settings list

change_pc_settings = input('Would you like to adjust/reset the Screen Resolution or Bounding Box Size? (Y/N/Reset): ').lower()

if change_pc_settings == 'y':
    cf['Bounding Box Size'] = input('Input the desired Bounding Box dimensions "(W, H)": ')
    cf['Screen Resolution'] = input('Input the desired Screen Resolution "W, H": ')
    print('Settings Changed')
elif change_pc_settings == 'n':
    cf['Bounding Box Size'] = data['Bounding Box Size']
    cf['Screen Resolution'] = data['Screen Resolution']
    print('Settings Not Changed')
else:                                                       # any key other than y/n will trigger a reset
    cf['Coordinates'] = {}
    cf['Bounding Box Size'] = {'size' : '(200, 100)'}       # works well for 2x2 setup in Mission Planner    
    cf['Screen Resolution'] = {'res' : '(1366, 768)'}       # default screen resolution of the aero laptop
    print('Settings Reset')

def setting():                                  # it isn't pretty, but it works.
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

# the following list is the given parameters that can be edited in the ['Coordinates'] heading
# you can add/remove items to this list and the script should adjust for the increase automatically

poslist = ['relay_high_pos','relay_low_pos','quicktab_pos','servotab_pos','glider_pos','payload_pos','door_high','door_low','ULBBCorner']

print(f'Move mouse to {poslist[0]} (Relay 0 High Position) and click {hotkey} when ready')

def hi():               # debugging, give it a try lol
    print('hi')

def killscript():       # ability to kill script after y/n/r options after the beginning
    sys.exit()

# The following hotkeys can be changed to whatever

with keyboard.GlobalHotKeys({
        '<esc>' : killscript,
        hotkey : setting,
        'd' : hi}) as h:
    h.join()
