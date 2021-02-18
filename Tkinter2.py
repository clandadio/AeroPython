from tkinter import *

root = Tk()

# Creating a label widget
myLabel1 = Label(root, text='hello world')
myLabel2 = Label(root, text='hello people', font=('comic sans ms', 25, 'italic'))

# Shoving it onto the screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)


root.mainloop()