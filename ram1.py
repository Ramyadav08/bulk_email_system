import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("ramrekhayadav412@gmail.com","ramrekha81718")
subject="sending mail"
body="this is the way of the trying to send mail"
message="Subject :{}\n\n{}".format(subject,body)
#print(message)
ob.sendmail("ramrekhayadav412@gmail.com","agupta844@rku.ac.in",message)
print("seccess sent")
ob.quit()