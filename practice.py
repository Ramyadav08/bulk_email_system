from tkinter import *
def getvalue():
    print("username:",uservalue.get())
    print("password:",passvalue.get())
root=Tk()
root.geometry("550x450")
root.title("login form")
#root.title("hello world!")
#ram=Label(text='''hi i am ram rekha yadav from lamtiya kapilvastu nepal where you can find love and thunder
#\nwhich is  most important thing in the world in the whole life.there are a lot of hero in the world but i love
#\najay devgan who is known as mass mararaj made
#\nfool aur kate''',bg="red",fg="yellow",padx=3,pady=5,font=("comicsensms",19,"bold"))
#ram.pack(side=BOTTOM,anchor="se")
#ram.pack(fill=X)'''
user=Label(root,text="username")
password=Label(root,text="password")
user.grid(row=0)
password.grid(row=1)
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="submit",command=getvalue).grid()
root.mainloop()