from tkinter import *

screen = Tk()
screen.title("Pack Geometry")

"""
    # anchor does not work on the size of the window whereas side works on the boundaries of the window
"""
l1 = Label(text="Label 1", bg='red',fg='yellow')
# l1.pack(anchor=NW) # anchor is used for anchoring a label to nw, ne, n, sw, se, s, e, w
# l1.side(side=LEFT) # it also places the label but according to the screen size
# l1.pack(padx=2,pady=2)
l1.pack(side=LEFT,ipadx=2,ipady=2,padx=2,pady=2,fill=Y) # internal padding

l2 = Label(text="Label 2", bg='red',fg='yellow')
l2.pack(side=TOP,ipadx=2,ipady=2,padx=2,pady=2, fill=X)

l3 = Label(text="Label 3", bg='red',fg='yellow')
l3.pack(side=TOP,ipadx=2,ipady=2,padx=2,pady=2)

l4 = Label(text='Label 4',bg='red',fg='yellow')
l4.pack(side=TOP,ipadx=2,ipady=2,padx=2,pady=2)

screen.mainloop()