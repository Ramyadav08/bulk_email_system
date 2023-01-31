from tkinter import *
def ram(event):
    print(f"you clicked button here{event.x},{event.y}")
root=Tk()
root.title("EVENT IN TKINTER")
root.geometry("555x450")
widget=Button(root,text="clickme please")
widget.pack()
widget.bind('<Button-1>',ram)
widget.bind('<Double-1>',quit)
root.mainloop()