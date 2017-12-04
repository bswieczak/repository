from Tkinter import *

counter = 30

def counter_label():
    def count():
        global counter
        counter = counter - 1
        label.config(text=str(counter))
        label.after(1000, count)
        if (counter == 0):
            root.destroy()
    count()


root = Tk()

label = Label(root, text="30", fg="dark green")
label.pack()

button = Button(root, text='START', width=25, command=counter_label)
button.pack()
root.mainloop()


