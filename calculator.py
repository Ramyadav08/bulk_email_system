from tkinter import *
def btnclick(number):
    global val
    val=val + str(number)
    abd.set(val)
def btnclear():
    global  val
    val=""
    abd.set(val)
def btnequal():
    global  val
    result=str(eval(val))
    abd.set(result)

root=Tk()
root.title("CALCULATOR")
root.geometry("550x411+500+200")
val=""
abd=StringVar()
ram=Entry(root,textvariable=abd,bd=29,bg="powder blue",font=("arial",20,"bold"),justify="right")
ram.grid(row=0,columnspan=4)
btn7=Button(root,text="7",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("7"))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("8"))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("9"))
btn9.grid(row=1,column=2)
btn_add=Button(root,text="+",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("+"))
btn_add.grid(row=1,column=3)

btn4=Button(root,text="4",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("4"))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("5"))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("6"))
btn6.grid(row=2,column=2)
btn_minus=Button(root,text="-",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("-"))
btn_minus.grid(row=2,column=3)

btn1=Button(root,text="1",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("1"))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("2"))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("3"))
btn3.grid(row=3,column=2)
btn_mul=Button(root,text="*",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("*"))
btn_mul.grid(row=3,column=3)

btn_clear=Button(root,text="C",font=("arial",20,"bold"),bd=12,width=6,command=btnclear)
btn_clear.grid(row=4,column=0)
btn_div=Button(root,text="/",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("/"))
btn_div.grid(row=4,column=1)
btn0=Button(root,text="0",font=("arial",20,"bold"),bd=12,width=6,command=lambda:btnclick("0"))
btn0.grid(row=4,column=2)
btn_equi=Button(root,text="=",font=("arial",20,"bold"),bd=12,width=6,command=btnequal)
btn_equi.grid(row=4,column=3)
root.mainloop()