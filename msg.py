import pandas as pd
import smtplib
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
msg="Hello I am ram this message is only for email sending don't mind"
subject= "hello world"
body= "Subject:{}\n\n{}".format(subject, msg)
for Email in emails:
    server.sendmail("ramrekhayadav412@gmail.com", Email, body)
print("successfully sent")
server.quit()
