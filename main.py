import smtplib as s
import schedule 
import time
import os
from os import environ

gmailaddress=environ['gmailaddress']
gmailpassword=environ['gmailpassword']
subject1='A'
subject2='B'
subject3='C'
subject4='D'
body1="A"
body2="B"
body3="C"
body4="D"
message1="Subject:{}\n\n{}".format(subject1,body1)
message2="Subject:{}\n\n{}".format(subject2,body2)
message3="Subject:{}\n\n{}".format(subject3,body3)
message4="Subject:{}\n\n{}".format(subject4,body4)
ToSend=environ['ToSend']
Name=environ['Name']
def send_mail_1():
	ob=s.SMTP("smtp.gmail.com",587)
	ob.starttls()
	ob.login(gmailaddress,gmailpassword)
	ob.sendmail(Name,ToSend,message1)
	print("done")
	ob.quit()
def send_mail_2():
	ob=s.SMTP("smtp.gmail.com",587)
	ob.starttls()
	ob.login(gmailaddress,gmailpassword)
	ob.sendmail(Name,ToSend,message2)
	print("done")
	ob.quit()
def send_mail_3():
	ob=s.SMTP("smtp.gmail.com",587)
	ob.starttls()
	ob.login(gmailaddress,gmailpassword)
	ob.sendmail(Name,ToSend,message3)
	print("done")
	ob.quit()
def send_mail_4():
	ob=s.SMTP("smtp.gmail.com",587)
	ob.starttls()
	ob.login(gmailaddress,gmailpassword)
	ob.sendmail(Name,ToSend,message4)
	print("done")
	ob.quit()
schedule.every().day.at("12:35").do(send_mail_1)
schedule.every().day.at("12:36").do(send_mail_2)
schedule.every().day.at("12:37").do(send_mail_3)
schedule.every().day.at("12:38").do(send_mail_4)
while 1:
	schedule.run_pending()
	time.sleep(1)