from tkinter import *

root = Tk()

e = Entry(root, width = 50, borderwidth = 5)
e.pack()
e.insert(0, 'Enter your name: ')

def myClick():
    hello = 'hello ' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text = 'enter your name', command = myClick, fg = 'blue', bg = 'green')
myButton.pack()

root.mainloop()