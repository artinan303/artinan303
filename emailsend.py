import smtplib, ssl
from email.message import EmailMessage


with open("<INSERT PATH>") as file: #email list
    lines = [line.strip() for line in file]

port = 465  # for SSL
sEmail = input("Type your email here and press enter: ")
pasw = input("Type your password and press enter: ")

msg = EmailMessage()
msg['Subject'] = #ENTER SUBJECT
msg['From'] = sEmail
msg['To'] = lines

context = ssl.create_default_context()


with open("<INSERT PATH>") as msgfile: #message
    msg.set_content(msgfile.read())

with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
    server.login(sEmail, pasw)
    server.send_message(msg)
