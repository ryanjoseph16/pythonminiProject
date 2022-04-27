from cgitb import text
from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("My Digital Clock")

def getTime():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text = timeVar)
    clock.after(200, getTime)

clock = Label(master, font=('Arial', 100), bg = "black" , fg = "green")
clock.pack()

getTime()
master.mainloop()