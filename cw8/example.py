from Tkinter import *

def printer():
    print "hehe"


root = Tk()

e1 = Entry(root).grid(row=0, column=1)
button = Button(root,text="Fajny batonik", command=printer()).grid(row=0,column=2)



root.mainloop()

