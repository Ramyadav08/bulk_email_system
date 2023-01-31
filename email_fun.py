import smtplib
def email_fun(to_,sub_,msg_,from_,passed_):
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(from_,passed_)
    msg="Subject: {}\n\n{}".format(sub_,msg_)
    s.sendmail(from_,to_,msg)
    x=s.ehlo()
    if x[0]==250:
       return "s"
    else:
       return "f"
    s.close()
