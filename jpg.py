from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("jpg immage")
root.geometry("500x450")
image=Image.open("email.jpg")
photo=ImageTk.PhotoImage(image)
Label(image=photo).pack()

root.mainloop()