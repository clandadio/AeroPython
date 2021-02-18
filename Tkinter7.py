from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('this is a title')

def open():
    global my_img
    top = Toplevel()
    top.title('top window')
    my_img = ImageTk.PhotoImage(Image.open('dan.jpg'))
    label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='close window', command = top.destroy).pack()


btn = Button(root, text='open second window', command = open).pack()

root.mainloop()