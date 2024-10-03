#smart mail transfer protocol
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
otp = random.randint(1111,9999)

smtp_server = "smtp.gmail.com"
smtp_port = 587
mailusername = "20bec016@iiitdwd.ac.in"
mailpassword = "yxqb amoc velb hnkk"

from_email = "20bec016@iiitdwd.ac.in"
to_email = input("enter email address: ")
subject = "OTP For validation"
body = f"otp for validation is {otp}"

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['subject'] = subject
msg.attach(MIMEText(body,'plain'))

server=smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(mailusername,mailpassword)
server.send_message(msg)
server.quit()


validate = int(input("Enter Otp for verification: "))
if validate == otp:
    print("Login Sucessful")

else:
    print("Login Unsucessful")
