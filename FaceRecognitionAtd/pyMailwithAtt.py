# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:24:24 2020

@author: Chaitanya
"""

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from datetime import date


today = date.today()
# dd-mm-YY
currentDate = today.strftime("%d-%m-%Y")

fromaddr = "gamerchaitanya@gmail.com"
toaddr = "chaitanyaj14@gmail.com"

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject 
msg['Subject'] = "Attendance Till: " + currentDate

# string to store the body of the mail 
body = "ESG 624 PRML Attendace (as on): "+ currentDate

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 
filename = "attendance.xlsx"
attachment = open("attendance.xlsx", "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, "uylnvehzlevsquyk") 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 

# Confirmation
print("Mail Sent Succesfully to: ",toaddr)