from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

def quit(*args):  #used inside func definitions to pass non keyworded arguments
    root.destroy() #causes main loop to exit
    
def clock():
    time = datetime.datetime.now()
    time = (time.strftime("%Y-%m-%d %H:%M:%S")) #formats time strftime
    txt.set(time) #displays the time
    
    root.after(1000, clock) #trigger the clock to start after every milisecond

#following are customization for the window 
root = Tk()
root.attributes("-fullscreen", True) #make it true to make it fullscreen
root.configure(background='black') #background color
root.bind("x", quit) #x is a label.The X icon to close the window
root.after(1000, clock)

#following are customizations for the clock
fnt = font.Font(family='Helvetica', size=100, weight='bold')
txt = StringVar() #holds a string value by default
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="orange", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER) #relx and rely gives position relative to window.Anchor centers the widget

root.mainloop()    #keeps clock running until window is closed 
