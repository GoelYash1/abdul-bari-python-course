from tkinter import *

win = Tk()
win.title("My Application")
win.geometry('600x400+10+10')

# label
l = Label(win, text="Hello World")
l.pack()

# button
b = Button(win, text="Click Me")
b.pack()

nLabel = Label(win, text="Name")
nLabel.pack()
# entry (text box)
e = Entry(win)
e.pack()

# textlines
t = Text(win, width=30, height=10)
t.pack()

# checkbutton
c = Checkbutton(win, text='Yes')
c.pack()

# Radiobutton
v1 = StringVar(value="Option 1")
r1 = Radiobutton(win, text='Option 1', variable=v1, value='Option 1')
r2 = Radiobutton(win, text='Option 2', variable=v1, value='Option 2')
r3 = Radiobutton(win, text='Option 3',variable=v1, value='Option 3')

r1.pack()
r2.pack()
r3.pack()

#Option Menu
v = StringVar(value="Python")
o = OptionMenu(win, v,'Python',*('Java','C++','Python','Javascript'))
o.pack()

# Scale
sc = Scale(win,from_=0, to=100)
sc.pack()
win.mainloop()