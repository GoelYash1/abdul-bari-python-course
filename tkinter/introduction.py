import tkinter

screen = tkinter.Tk()
screen.title("My First Application")
screen.resizable(False,True)
screen.geometry(newGeometry='600x400+100-10')
screen.attributes('-alpha',0.90)
screen.mainloop()
