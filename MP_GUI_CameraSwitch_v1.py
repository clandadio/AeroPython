# Chris Landadio 2/17/21

# Make sure the Relay is set to LOW to begin with so the toggling can work correctly

from pynput.mouse import Button, Controller
from pynput import keyboard
import time, datetime, csv

mouse = Controller()    # the mouse is the given controller

camerahigh = False      # camera starts on low
gliderhigh = False      
payloadhigh = False

logfilename = str(datetime.datetime.now())[0:-10].replace(':','-')
logfilename_txt = r'H:\Aero\Python\Logs\\' + logfilename + '.txt'
logfilename_csv = r'H:\Aero\Python\Logs\\' + logfilename + '.csv'

logstatus = input('Would you like to log the Camera and Drop system info for this flight? (Yes/No): ').lower()

if logstatus == 'yes':
    print('The flight will be logged in txt and csv formats')
    with open(logfilename_txt, mode='w', encoding='utf-8') as logfile_txt:
        logfile_txt.write(logfilename)
        logfile_txt.write('\nLOG FILE FOR DROP SYSTEMS AND CAMERA SWITCHES\n\n')
    with open(logfilename_csv, mode='w', newline='') as logfile_csv:
        writer = csv.writer(logfile_csv, delimiter=',')
        writer.writerow([logfilename])
        writer.writerow(['LOG FILE FOR DROP SYSTEMS AND CAMERA SWITCHES'])
        writer.writerow(['Date','Timestamp','Droptype'])

    logstatus = True
else:
    print('The flight will NOT be logged')
    logstatus = False

# relay button mouse position - (High on Relay0) - camera switch
relay_high_pos = (76, 694)
# relay button mouse position - (Low on Relay0) - camera switch
relay_low_pos = (32, 696)
# quick button mouse position - For stats and screenshot
quicktab_pos = (23,499)
# servo/relay button mouse position - For servos and relay manual triggering
servotab_pos = (169, 500)

# initially triggered with shift+j in AHK, then use defined hotkeys

def writedata(filename_txt, filename_csv, droptype):                          # function to write timestamps and relay status
    if logstatus:
            with open(logfilename_txt, mode='a', encoding='utf-8') as logfile:
                logfile.write(
                    str(datetime.datetime.now())+'\n'+
                    str(datetime.datetime.now().timestamp())+'\n'+
                    str(droptype)+'\n\n'
                )

            with open(logfilename_csv, mode='a', newline='') as logfile:
                writer = csv.writer(logfile, delimiter=',')
                writer.writerow([
                    datetime.datetime.now(),
                    datetime.datetime.now().timestamp(),
                    droptype
                ])

def camera_toggle():
    global camerahigh
    print(camerahigh)

    # mouse.position = servotab_pos         # movement to servo/relay tab button
    # mouse.click(Button.left, 1)           # trigger servo/relay tab

    if not camerahigh:
        # mouse.position = relay_high_pos   # movement to servo button
        # mouse.click(Button.left, 1)       # trigger servo button

        writedata(logfilename_txt, logfilename_csv, 'Camera wide to narrow')
            
        # time.sleep(0.3)                   # delay for program and transmission
        camerahigh = True

    else:
        # mouse.position = relay_low_pos    # movement to servo button
        # mouse.click(Button.left, 1)       # trigger servo button

        writedata(logfilename_txt, logfilename_csv, 'Camera narrow to wide')

        # time.sleep(0.3)                   # delay for program and transmission
        camerahigh = False

    # mouse.position = quicktab_pos        # movement to quick tab button
    # mouse.click(Button.left, 1)          # trigger switch to quick tab

    print(camerahigh)

def hi():
    print('hi')                         # debugging

def glider_drop():
    global gliderhigh
    if gliderhigh:
        writedata(logfilename_txt, logfilename_csv, 'Glider high to low')
        gliderhigh = False

    else:
        writedata(logfilename_txt, logfilename_csv, 'Glider low to high')
        gliderhigh = True

def payload_drop():
    global payloadhigh
    if gliderhigh:
        writedata(logfilename_txt, logfilename_csv, 'Payload high to low')
        payloadhigh = False

    else:
        writedata(logfilename_txt, logfilename_csv, 'Payload low to high')
        payloadhigh = True     

with keyboard.GlobalHotKeys({
        'c' : camera_toggle,
        '<shift>+g' : glider_drop,
        '<shift>+h' : payload_drop,
        'd' : hi}) as h:
    h.join()

# delays may have to be adjusted based on system lag, mostly MP being slow af
# the current delays haven't been tuned, but seem to work well ~90% of the time