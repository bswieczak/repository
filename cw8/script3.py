# -*-coding: utf-8-*-
from Tkinter import *
import sys, logging, pdb
sys.path.append('cw9/script1.py')

logging.basicConfig(filename='logs.txt', level=logging.INFO)
logger = logging.getLogger(__name__)


class calc:

    def getandreplace(self):
        self.expression = self.inputArea.get()
        self.newtext = self.expression.replace(self.newdiv, '/')
        self.newtext = self.newtext.replace('x', '*')

    def equals(self):
        self.getandreplace()
        try:
            logging.info('Equals has been pressed')
            self.value = eval(self.newtext)
        except SyntaxError or NameErrror:
            self.inputArea.delete(0, END)
            self.inputArea.insert(0, 'Invalid Input!')
        else:
            self.inputArea.delete(0, END)
            self.inputArea.insert(0, self.value)

    def clearall(self):
        logging.info('Clear All..')

        self.inputArea.delete(0, END)

    def clear1(self):
        logging.info('Clear area..')

        self.txt = self.inputArea.get()[:-1]
        self.inputArea.delete(0, END)
        self.inputArea.insert(0, self.txt)


    def action(self, argi):
        logging.info('Action, send "'+ str(argi) + '" to input')

        self.inputArea.insert(END, argi)

    def __init__(self, master):
        master.title('Calulator')
        master.geometry()
        self.inputArea = Entry(master)
        self.inputArea.grid(row=0, column=0, columnspan=6, pady=3)
        self.inputArea.focus_set()

        logging.info('start')

        self.div = '÷'
        self.newdiv = self.div.decode('utf-8')
        Button(master, text="=", width=10, command=lambda: self.equals()).grid(row=4, column=4, columnspan=2)
        Button(master, text='AC', width=3, command=lambda: self.clearall()).grid(row=1, column=4)
        Button(master, text='C', width=3, command=lambda: self.clear1()).grid(row=1, column=5)
        Button(master, text="+", width=3, command=lambda: self.action('+')).grid(row=4, column=3)
        Button(master, text="x", width=3, command=lambda: self.action('x')).grid(row=2, column=3)
        Button(master, text="-", width=3, command=lambda: self.action('-')).grid(row=3, column=3)
        Button(master, text="÷", width=3, command=lambda: self.action(self.newdiv)).grid(row=1, column=3)
        Button(master, text="7", width=3, command=lambda: self.action(7)).grid(row=1, column=0)
        Button(master, text="8", width=3, command=lambda: self.action(8)).grid(row=1, column=1)
        Button(master, text="9", width=3, command=lambda: self.action(9)).grid(row=1, column=2)
        Button(master, text="4", width=3, command=lambda: self.action(4)).grid(row=2, column=0)
        Button(master, text="5", width=3, command=lambda: self.action(5)).grid(row=2, column=1)
        Button(master, text="6", width=3, command=lambda: self.action(6)).grid(row=2, column=2)
        Button(master, text="1", width=3, command=lambda: self.action(1)).grid(row=3, column=0)
        Button(master, text="2", width=3, command=lambda: self.action(2)).grid(row=3, column=1)
        Button(master, text="3", width=3, command=lambda: self.action(3)).grid(row=3, column=2)
        Button(master, text="0", width=3, command=lambda: self.action(0)).grid(row=4, column=0)
        Button(master, text=".", width=3, command=lambda: self.action('.')).grid(row=4, column=1)

root = Tk()
obj = calc(root)
root.mainloop()


