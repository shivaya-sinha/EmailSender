import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

#From address
fromaddr = "vagishanidhi64@gmail.com"
#To address
toaddr = "vagisha.nda@gmail.com"

#Creating message
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "CHECK SCRIPT WORKING"
body = "Hello! Sup?"
msg.attach(MIMEText(body, 'plain'))

#Attachment
filename = "Screenshot from 2016-10-07 23-32-23.png"
attachment = open("/home/vagisha/Pictures/screenshot/Screenshot from 2016-10-07 23-32-23.png", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

#Contacting the server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "****")
text = msg.as_string()
#Sending mail
server.sendmail(fromaddr, toaddr, text)
server.quit()
