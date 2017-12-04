from Tkinter import *

def printer():
    print "cos"

def aa():
    print value.get()
    button.configure(bg="red")

root = Tk()

value = StringVar()
value.set('red')

Radiobutton(root, text='red', variable=value, value='red', command=aa).pack(anchor=W)
Radiobutton(root, text='green', variable=value, value='green', command=aa).pack(anchor=W)
Radiobutton(root, text='blue', variable=value, value='blue', command=aa).pack(anchor=W)


button = Button(root, text="BUTTON", command=printer).pack(side=LEFT)

root.mainloop()

