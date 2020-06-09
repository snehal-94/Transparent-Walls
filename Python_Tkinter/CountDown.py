from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

global endTime

def quit(*args):
    root.destroy()

def cant_wait():
    timeleft = endtime-datetime.datetime.now()
    timeleft = timeleft-datetime.timedelta(microseconds=timeleft.microseconds)
                #doesn't display the microseconds in time
    txt.set(timeleft)
    root.after(1000,cant_wait)

root=Tk()
root.attributes("-fullscreen",True)
root.configure(background='white')
root.bind("x", quit)
root.after(1000,cant_wait)

endtime = datetime.datetime(2018,7,30,0,0) #specifying the year,mon,day,hr,s for the endtime

fnt= font.Font(family= "Helvetica",size=60, weight='bold')
txt=StringVar()
lbl= ttk.Label(root, textvariable=txt, font=fnt, foreground="black",background="white")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
