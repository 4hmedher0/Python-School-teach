import smtplib
from email.message import EmailMessage
#from email.mime.multipart import MIMEultipart
from email import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
#from smtplib import SMTPAuthenticationError
from smtplib import *
text=open("ddd.txt",'r')
Email=smtplib.SMTP("smtp.gmail.com",587)
Email.ehlo()
Email.starttls()
#for i in text:
try :
    Email.login("ad5044hk@gmail.com","hds09vuqa")
    print("#### Loged in ")
    #my_msg=MIMEultipart("alternative")
    my_msg= MIMEMultipart() #container
    #my_msg=EmailMessage() # to make as var to send 
    #my_msg.set_content(text.read())
    my_msg["Subject"]="Hello World!"
    my_msg["From"]="ad5044hk@gmail.com"
    my_msg["To"]="ad5044hk@gmail.com"
    html_txt="""<html>
<head>
<title>zero</title>
welcome of googel links 
</head>
<body>
 <a href="http://google.com.eg/">googel </a>
<a href="http://google.com.eg/"target="_blank">googel </a> <br>
<a href="http://google.com.eg/"target="_self">googel </a>

</body>
</html>
"""
    #part1=MIMEText(plain_txt,"plain")
    part2=MIMEText(html_txt,"html") #verfiy kind of file 
    #my_msg.attach(part1)
    my_msg.attach(part2) #attachment
    #my_msg.set_content(text.read())
    print(my_msg.as_string())
    Email.send_message(my_msg) #sending
    #Email.sendmail("ad5044hk@gmail.com","ad5044hk@gmail.com",my_msg)

       #break
except SMTPAuthenticationError :
       print("wrong password or email")
#email.sendmail()
#Email.login("ad5044hk@gmail.com","hds09vuqa")
