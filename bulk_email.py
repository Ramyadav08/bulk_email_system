from tkinter import *
from tkinter import messagebox,filedialog
import os
import pandas as pd
import email_fun
import time
class Bulk_mail:
    def __init__(self,root):
        self.root=root
        self.root.title("BULK EMAIL APP")
        self.root.geometry("1000x600+200+50")
        self.root.resizable(False,False)
        #tittle.................
        title=Label(self.root,font=("arial",40,"bold"),text="Bulk email send ",bg="#222A35").place(x=0,y=0,relwidth=1)
        btn_setting=Button(self.root,text="LOGIN",font=("arial",22,"bold"),bg="green",fg="yellow",bd=0,command=self._login_win).place(x=800,y=4)
        #radio button................
        self.var_choice=StringVar()
        single=Radiobutton(self.root,text="single",value="single",variable=self.var_choice, font=("times new roman",25,"bold")
                           ,fg="black",command=self.check_single_or_bulk).place(x=50,y=90)
        bulk= Radiobutton(self.root, text="Bulk",value="bulk",variable=self.var_choice, font=("times new roman", 25, "bold"),
                          fg="black",command=self.check_single_or_bulk).place(x=250,y=90)
        self.var_choice.set("single")
        #input label.......and input box...............
        To=Label(self.root,font=("arial",22),text="To (Email Address)",fg="black").place(x=15,y=170)
        subject=Label(self.root, font=("arial", 22), text="SUBJECT", fg="black").place(x=15, y=220)
        msg = Label(self.root, font=("arial", 22), text="MESSAGE", fg="black").place(x=15, y=370)
        self.txt_to=Entry(self.root,font=("arial",16),fg="black",bg="lightyellow")
        self.txt_to.place(x=300,y=170,width=350,height=30)
        self.subject = Entry(self.root, font=("arial", 15), fg="black", bg="lightyellow")
        self.subject.place(x=300, y=220, width=400, height=30)
        self.message = Text(self.root, font=("arial", 16), fg="black", bg="lightyellow")
        self.message.place(x=300, y=270, width=600, height=200)

        btn_send=Button(self.root,text="SEND",font=('arial',12,"bold"),bg="green",fg="black",activebackground="green",cursor="hand2",
                        command=self.send_mail).place(x=800,y=480)
        btn_clear= Button(self.root, text="CLEAR",command=self.clear1, font=('arial', 12, "bold"), bg="red"
                          , fg="black",activebackground="red",cursor="hand2").place(x=700,y=480)
        self.btn_browse = Button(self.root, text="BROWSE", font=('arial', 10, "bold"), bg="green",
                                 fg="black",activebackground="green", cursor="hand2",command=self.browse_file)
        self.btn_browse.place(x=700, y=170)
        self.check_file_exist()


        #statues>>>>>>>>>////////..........
        self.Total = Label(self.root, font=("arial", 15),bg='white', fg="black")
        self.Total.place(x=15, y=480)
        self.sent= Label(self.root, font=("arial", 15), bg='white',fg="green")
        self.sent.place(x=300, y=480)
        self.left = Label(self.root, font=("arial", 15),bg='white', fg="orange")
        self.left.place(x=420, y=480)
        self.failed = Label(self.root, font=("arial", 15), bg='white', fg="red")
        self.failed.place(x=550, y=480)

    def browse_file(self):
        op=filedialog.askopenfile(initialdir="/",title="select excel file for the emails",
                                  filetype=(("all file","*.*"),("Excel file",".xlsx")))
        if op!=None:
            data = pd.read_excel(op.name)

            if "email" in data.columns:
                self.emails = list(data["email"])
                l = []
                for i in self.emails:
                    if pd.isnull(i) == False:
                        l.append(i)
                self.emails = l
                if len(self.emails)>0:
                    self.txt_to.config(state=NORMAL)
                    self.txt_to.delete(0,END)
                    self.txt_to.insert(0,str(op.name.split("/")[-1]))
                    self.txt_to.config(state="readonly")
                    self.Total.config(text="TOTAL: "+str(len(self.emails)))
                    self.sent.config(text="SENT: ")
                    self.left.config(text="LEFT: ")
                    self.failed.config(text="FAILED: ")
                else:
                    messagebox.showerror("Error","this file hasnot any email",parent=self.root)
            else:
                messagebox.showerror("Error","please select the file which have email column",parent=self.root)



    def send_mail(self):
        x=self.message.get("1.0",END)
        if self.txt_to.get()=="" or self.subject.get()=="" or x==1:
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            if self.var_choice.get()=="single":
                status=email_fun.email_fun(self.txt_to.get(),self.subject.get(),self.message.get("1.0",END),self.user_,self.pass_)
                if status=="s":
                    messagebox.showinfo("Success", "Email has been sent", parent=self.root)
                if status=="f":
                    messagebox.showerror("Failed","try again",parent=self.root)
            if self.var_choice.get()=="bulk":
                for x in self.emails:
                    self.failed_=[]
                    self.s_count=0
                    self.f_count=0
                    status=email_fun.email_fun(x, self.subject.get(), self.message.get("1.0", END), self.user_,
                                        self.pass_)
                    if status=='s':
                        self.s_count+=1
                    if status=="f":
                        self.f_count+=1
                    self.status_bar()
                messagebox.showinfo("Success", "Email has been sent", parent=self.root)

    def status_bar(self):
        self.Total.config(text="TOTAL: " + str(len(self.emails))+"=>>")
        self.sent.config(text="SENT: "+ str(self.s_count))
        self.left.config(text="LEFT: "+str(len(self.emails)-(self.s_count + self.f_count)))
        self.failed.config(text="FAILED: "+str(self.f_count))
        self.Total.update()
        self.sent.update()
        self.left.update()
        self.failed.update()


    def check_single_or_bulk(self):
        if self.var_choice.get()=="single":
            self.btn_browse.config(state=DISABLED)
            self.txt_to.config(state=NORMAL)
            self.txt_to.delete(0,END)
            self.clear1()
        if self.var_choice.get()=="bulk":
            self.btn_browse.config(state=NORMAL)
            self.txt_to.delete(0, END)
            self.txt_to.config(state="readonly")

    def clear1(self):
        self.txt_to.config(state=NORMAL)
        self.txt_to.delete(0,END)
        self.subject.delete(0,END)
        self.message.delete("1.0",END)
        self.var_choice.set("single")
        self.btn_browse.config(state=DISABLED)
        self.Total.config(text="")
        self.sent.config(text="")
        self.left.config(text="")
        self.failed.config(text="")


    def _login_win(self):
        self.check_file_exist()
        self.root2=Toplevel()
        self.root2.title("LOGIN")
        self.root2.geometry("700x400+300+200")
        self.root2.focus_force()
        self.root2.config(bg="white")
        title =Label(self.root2, font=("arial", 40, "bold"), text="LOGIN", bg="#222A35").place(x=0, y=0,relwidth=1)
        des=Label(self.root2,text="Enter the email address and password from which to send all emails ",bg="yellow",fg="#222A35",
                  font=("times new roman",15,"bold")).place(x=0,y=77,relwidth=1)
        self.root2.grab_set()
        user_= Label(self.root2,font=("arial", 22), text="Email Address",bg="white", fg="black").place(x=15, y=170)
        pass_= Label(self.root2,font=("arial", 22), text="Password",bg="white" ,fg="black").place(x=15, y=220)
        #entery box........
        self.txt_user = Entry(self.root2, font=("arial", 10, "bold"), fg="black", bg="lightyellow")
        self.txt_user.place(x=250, y=170, width=380, height=30)
        self.pass_ = Entry(self.root2, font=("arial", 10, "bold"), fg="black", bg="lightyellow",show="*")
        self.pass_.place(x=250, y=220, width=380, height=30)
        #button ......................
        btn_save2 = Button(self.root2, text="SAVE", font=('arial', 12, "bold"),command=self.save_login, bg="green", fg="black",
                          activebackground="green", cursor="hand2").place(x=430, y=280)
        btn_clear2= Button(self.root2, text="CLEAR",command=self.clear2, font=('arial', 12, "bold"), bg="red", fg="black",
                          activebackground="red", cursor="hand2").place(x=350, y=280)
        self.txt_user.insert(0,self.user_)
        self.pass_.insert(0,self.pass_)
    def clear2(self):
        self.txt_user.delete(0,END)
        self.pass_.delete(0,END)
    def check_file_exist(self):
        if os.path.exists("login.txt")==False:
            f=open("login.txt","w")
            f.write(",")
            f.close()
        f2=open("login.txt","r")
        self.userpass_=[]
        for i in f2:
            self.userpass_.append([i.split(",")[0],i.split(",")[1]])
        self.user_=self.userpass_[0][0]
        self.pass_=self.userpass_[0][1]

    def save_login(self):
        if self.txt_user.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","all field are required",parent=self.root2)
        else:
            f=open("login.txt","w")
            f.write(self.txt_user.get()+","+self.pass_.get())
            f.close()
            messagebox.showinfo("Success", "saved", parent=self.root2)
            self.check_file_exist()
root=Tk()
obj=Bulk_mail(root)
root.mainloop()