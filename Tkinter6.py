from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('this is a title')

my_img = ImageTk.PhotoImage(Image.open('dan.jpg'))
my_label = Label(image = my_img)
my_label.pack()

button_quit = Button(root, text='exit program', command=root.quit)
button_quit.pack()

root.mainloop()