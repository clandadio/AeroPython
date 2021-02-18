from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='look, I clicked a button')
    myLabel.pack()

myButton = Button(root, text = 'click me', command = myClick, fg = 'blue', bg = 'green')
myButton.pack()

root.mainloop()