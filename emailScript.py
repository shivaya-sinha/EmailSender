import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "vagishanidhi64@gmail.com"
toaddr = "vagisha.nda@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "CHECK SCRIPT WORKING"
 
body = "Hello! Sup?"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "Screenshot from 2016-10-07 23-32-23.png"
attachment = open("/home/vagisha/Pictures/screenshot/Screenshot from 2016-10-07 23-32-23.png", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())

part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "****")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()