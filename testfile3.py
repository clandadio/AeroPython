import configparser, time
from pynput.mouse import Controller
mouse = Controller()
cf = configparser.ConfigParser()
filepath = r'H:\Aero\Python\Movement_Coordinates.ini'
cf.read(filepath)
x = cf['Coordinates']['relay_high_pos']
y = eval(x)
print(y)
print(type(y))
print(f'Moving mouse to position {x}')
mouse.position = y