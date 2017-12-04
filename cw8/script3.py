from Tkinter import *

global liczba_1
global liczba_2

def save():


root = Tk()

e1 = Entry(root).grid(row=0, column=1)

Button(root, text="7", command=save).grid(row=1, column=0)
Button(root, text="8").grid(row=1, column=1)
Button(root, text="9").grid(row=1, column=2)
Button(root, text="/").grid(row=1, column=3)


Button(root, text="4").grid(row=2, column=0)
Button(root, text="5").grid(row=2, column=1)
Button(root, text="6").grid(row=2, column=2)
Button(root, text="*").grid(row=2, column=3)


Button(root, text="1").grid(row=3, column=0)
Button(root, text="2").grid(row=3, column=1)
Button(root, text="3").grid(row=3, column=2)
Button(root, text="-").grid(row=3, column=3)

Button(root, text="0").grid(row=4, column=0)
Button(root, text="+").grid(row=4, column=1)
Button(root, text="=").grid(row=4, column=2)




root.mainloop()

