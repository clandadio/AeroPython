# Chris Landadio 1/16/21

from pynput.mouse import Button, Controller
from tkinter import Label, Grid, mainloop, Tk
from PIL import ImageTk, Image
import pyscreenshot as ss
import time, configparser

Drop_name = 'payload'            #defines windows placement

mouse = Controller()
boundingbox = (42,520,242,620)  #screenshot bounding box

# glider button mouse position - (High on Servo10) - Release for Glider
glider_pos = (92,532)
# payload button mouse position - (High on Servo11) - Release for Payload
payload_pos = (92,566)
# quick button mouse position - For stats and screenshot
quicktab_pos = (23,499)
# servo/relay button mouse position - For servos and relay manual triggering
servotab_pos = (169, 500)

root = Tk()
root.title('Payload Release Height')         # window title
root.configure(bg = 'white')                 # background color

# Values for windows on the screen
scr_res = (1366, 768)                       # screen resolution
offset = 7                                  # offset from edge of screen (subjective)
x_coord = 960-offset                        # location of top left corner of the window
if Drop_name == 'glider':                   # glider widget will be on the top half rn
    y_coord = 0                             # location of top left corner of the window
else:
    y_coord = int(scr_res[1]/2)             
width = scr_res[0]-x_coord-offset           # size of the window
length = int((scr_res[1]/2)-30)             # size of the window

# Geometry (w, h, x, y)
dimensions = (str(width)+'x'+str(length)+'+'+str(x_coord)+'+'+str(y_coord))
root.geometry(dimensions)

# triggered with shift+h in AHK
mouse.position = quicktab_pos     # movement to quick tab button for moving the cmd window
mouse.click(Button.left, 1)       # trigger click quick tab for cmd window
time.sleep(0.1)                   # delay for program delay

mouse.position = servotab_pos     # movement to servo/relay tab button
mouse.click(Button.left, 1)       # trigger servo/relay tab

mouse.position = payload_pos      # movement to servo button
mouse.click(Button.left, 1)       # trigger servo button
time.sleep(0.3)                   # delay for program and transmission

mouse.position = quicktab_pos     # movement to quick tab button
mouse.click(Button.left, 1)       # trigger switch to quick tab
time.sleep(0.3)                   # delay for program delay

# delays may have to be adjusted based on system lag, mostly MP being slow af
# the current delays haven't been tuned, but seem to work well ~90% of the time

# taking the screenshot and saving it
image = ss.grab(bbox=boundingbox)   
name = 'payloadreleaseheight.png'
image.save(name)
print('drop complete; image saved')

# labels below the displayed screenshot
my_img = ImageTk.PhotoImage(Image.open(name).resize((width,int(width/2)),Image.LANCZOS))
Label(image = my_img).grid(row=0)
Label(root, text = 'Elevation of Payload Release', font = 20).grid(row=1)

root.mainloop()