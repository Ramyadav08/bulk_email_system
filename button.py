from tkinter import *
root=Tk()
root.geometry("550x450")
def hello():
    print("hello ramrekha kya hal hai aaj aap ka! sab thik thak hai na?")
f1=Frame(root,borderwidth=8,bg="gray",relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")
b1=Button(f1,text="submit",command=hello)
b1.pack(side=LEFT)
b2=Button(f1,text="submit")
b2.pack(side=LEFT)
b3=Button(f1,text="submit")
b3.pack(side=LEFT)

root.mainloop()