from tkinter import *
root =Tk()
def getvar():
    print("successfully submitted!!!")
    print(f"{name.get()}")
    result.set(name.get())
    with open("lab.txt", "a") as f:
        f.write(f"{name.get()}\n")
root.title("Ramyadav")
root.geometry("500x550")
Label(root,text="Enter your name",font="arial 14 bold",bg="gray",fg="green").pack()
name=StringVar()
Entry(root,textvar=name,width=80).pack()
Button(text="submit", command=getvar).pack()
result=StringVar()
Label(root,textvariable=result,font="arial 17 bold").pack()
root.mainloop()