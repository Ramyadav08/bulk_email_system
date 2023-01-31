from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("my digital")
from time import strftime
def time():
    string=strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)
label=Label(root,font=("arial",40,"bold"),background="black",foreground="red")
label.pack(anchor="center")
time()
mainloop()