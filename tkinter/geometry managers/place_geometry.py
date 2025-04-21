from tkinter import *

win = Tk()
win.title("Place Geometry")
win.geometry("600x400")

b1 = Button(win, text="Button 1", bg='lightblue',fg = 'blue')
b2 = Button(win, text="Button 2", bg='lightblue',fg = 'blue')
b3 = Button(win, text="Button 3", bg='lightblue',fg = 'blue')

b1.place(x=10, y=5, width=100, height=50)
b2.place(x=110, y=55, width=100, height=50)
b3.place(relx=0.5, rely=0.5, relwidth=.1, relheight=.2)

win.mainloop()