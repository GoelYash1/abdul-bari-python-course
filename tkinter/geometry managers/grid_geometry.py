from tkinter import *

win = Tk()
win.title("Grid Manager")

l1 = Label(win, bg='lightblue', text='Label 1')
l2 = Label(win, bg='lightblue', text='Label 2')
l3 = Label(win, bg='lightblue', text='Label 3')
l4 = Label(win, bg='lightblue', text='Label 4')
l5 = Label(win, bg='lightblue', text='Label 5')
l6 = Label(win, bg='lightblue', text='Label 6')
l7 = Label(win, bg='lightblue', text='Label 7')
l8 = Label(win, bg='lightblue', text='Label 8')
l9 = Label(win, bg='lightblue', text='Label 9')

l1.grid(row=0,column=0, padx=5, pady=5)
l2.grid(row=0,column=1, padx=5, pady=5)
l3.grid(row=0,column=2, padx=5, pady=5)

l4.grid(row=1,column=0, padx=5, pady=5)
l5.grid(row=1,column=1, padx=5, pady=5)
l6.grid(row=1,column=2, padx=5, pady=5)

l7.grid(row=2,column=0, padx=5, pady=5)
l8.grid(row=2,column=1, padx=5, pady=5)
l9.grid(row=2,column=2, padx=5, pady=5)

win.mainloop()