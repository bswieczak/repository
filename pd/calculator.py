from Tkinter import *


class Calculator:

    entryInput = None

    def __init__(self, rootWindow):
        self.loadContext(rootWindow)

    def equals(self):
        expression = self.entryInput.get()
        try:
            value = eval(expression)
        except SyntaxError:
            self.entryInput.delete(0, END)
            self.entryInput.insert(0, 'ERROR')
        else:
            self.entryInput.delete(0, END)
            self.entryInput.insert(0, value)

    def deleteAllVariables(self):
        self.entryInput.delete(0, END)

    def deleteLastVariable(self):
        txt = self.entryInput.get()[:-1]
        self.entryInput.delete(0, END)
        self.entryInput.insert(0, txt)

    def onClick(self, variable):
        self.entryInput.insert(END, variable)

    def loadContext(self, window):
        window.title('Kalkulator prosty')
        self.entryInput = Entry(window)
        self.entryInput.grid(row=0, column=0, columnspan=4, pady=5)

        Button(window, text='CE', width=3, command=lambda: self.deleteAllVariables()).grid(row=1, column=0)
        Button(window, text='C', width=3, command=lambda: self.deleteLastVariable()).grid(row=1, column=1)
        Button(window, text="(", width=3, command=lambda: self.onClick('(')).grid(row=1, column=2)
        Button(window, text=")", width=3, command=lambda: self.onClick(')')).grid(row=1, column=3)

        Button(window, text="7", width=3, command=lambda: self.onClick(7)).grid(row=2, column=0)
        Button(window, text="8", width=3, command=lambda: self.onClick(8)).grid(row=2, column=1)
        Button(window, text="9", width=3, command=lambda: self.onClick(9)).grid(row=2, column=2)
        Button(window, text="*", width=3, command=lambda: self.onClick('*')).grid(row=2, column=3)

        Button(window, text="4", width=3, command=lambda: self.onClick(4)).grid(row=3, column=0)
        Button(window, text="5", width=3, command=lambda: self.onClick(5)).grid(row=3, column=1)
        Button(window, text="6", width=3, command=lambda: self.onClick(6)).grid(row=3, column=2)
        Button(window, text="/", width=3, command=lambda: self.onClick('/')).grid(row=3, column=3)

        Button(window, text="1", width=3, command=lambda: self.onClick(1)).grid(row=4, column=0)
        Button(window, text="2", width=3, command=lambda: self.onClick(2)).grid(row=4, column=1)
        Button(window, text="3", width=3, command=lambda: self.onClick(3)).grid(row=4, column=2)
        Button(window, text="+", width=3, command=lambda: self.onClick('+')).grid(row=4, column=3)

        Button(window, text=".", width=3, command=lambda: self.onClick('.')).grid(row=5, column=0)
        Button(window, text="0", width=3, command=lambda: self.onClick(0)).grid(row=5, column=1)
        Button(window, text="=", width=3, command=lambda: self.equals()).grid(row=5, column=2)
        Button(window, text="-", width=3, command=lambda: self.onClick('-')).grid(row=5, column=3)


rootWindow = Tk()
obj = Calculator(rootWindow)
rootWindow.mainloop()
