from datetime import *
from tkinter import *
import numpy

def Time():
    dt = datetime.now()
    Real_time = (dt.strftime("%H:%M:%S"))
    clock.config(text=Real_time)
    clock.after(1000, Time)

root = Tk()
root.title("Clock")
icon=PhotoImage(file='clock.png')
root.iconphoto(False, icon)
root.geometry("400x100")
clock = Label(root, bg="black", fg="cyan", font=("calibre", 75, "bold"))
clock.pack()
Time()
root.mainloop()
