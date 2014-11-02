import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

class EmailSender:
    def __init__(self, username, password, target):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(username, password)
        self.target = target
        return

    def sendNotification(self, htmlMsg):
        # Setup message headers
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Updated grades! " + str(datetime.datetime.now())
        msg['From'] = self.target
        msg['To'] = self.target

        # Setup plain text part
        part1 = MIMEText("Grades updated!", 'plain')

        # Setup HTML message part
        part2 = MIMEText(htmlMsg, 'html')

        # Send the message
        msg.attach(part1)
        msg.attach(part2)

        self.server.sendmail(self.target, self.target, msg.as_string())
        return
