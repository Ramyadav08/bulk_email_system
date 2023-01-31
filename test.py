import pandas as pd
import smtplib
from tkinter import *

def getvar():
    msg_.set(msg.get())
    subject.set(subj.get())
root=Tk()
root.geometry("660x590+300+90")
root.resizable(False,False)
root.config(bg="white")
msg=StringVar()
subj=StringVar()
title = Label(root, font=("arial", 22,"bold"), text="Bulk email send ", bg="#222A35")
title.place(x=0, y=0, relwidth=1)
subject=Label(root,text="SUBJECT",font=("arial",22),bg="white",fg="black")
subject.place(x=275,y=40)
msg_ = Label(root, font=("arial", 22), text="MESSAGE", fg="black")
msg_.place(x=275, y=140)

subject_entery= Entry(root,textvar=subj, font=("arial", 15), fg="black", bg="lightyellow")
subject_entery.place(x=100, y=100, width=500, height=30)
message = Text(root,textvar=msg, font=("arial", 16), fg="black", bg="lightyellow")
message.place(x=100, y=190, width=500, height=300)

btn_send=Button(root,text="SEND",font=('arial',16,"bold"),bg="green",fg="black",activebackground="green",cursor="hand2",command=getvar)
btn_send.place(x=295,y=500)
root.mainloop()
data=pd.read_excel("Book1.xlsx")
emails=list(data["email"])
if "email" in data.columns:
    print("exist")
    l=[]
    for i in emails:
        #print(i)
        if pd.isnull(i)==False:
            #print(i)
            l.append(i)
    emails = l
    print(emails)
else:
    print("not exists")
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("ramrekhayadav412@gmail.com", "ramrekha81718")
body= "Subject:{}\n\n{}".format(subject, msg)
for Email in emails:
    server.sendmail("ramrekhayadav412@gmail.com", Email, body)
print("successfully sent")
server.quit()
