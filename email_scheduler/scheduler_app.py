import time, schedule
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailScheduler:

    def __init__(self, config):
        self.config = config
        pass
    
    def run(self):
        try:
            while True:
                time.sleep(5)
                schedule.run_pending()
        except KeyboardInterrupt:
            print("EmailScheduler is shutting down, goodbye!")
    
    def add_email_event(self, recipients, subject, message):
        schedule.every().monday.at("10:01").do(self.send_email, recipients, subject, message)

    def send_email(self, recipients, subject, message):
        with SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.config["email"], self.config["password"])
            for recipient in recipients:
                email_msg = MIMEMultipart()
                email_msg["From"] = self.config["email"]
                email_msg["To"] = recipient
                email_msg["Subject"] = subject
                email_body = MIMEText(message)
                email_msg.attach(email_body)
                email_msg = email_msg.as_string()
                try:
                    smtp.sendmail(self.config["email"], recipient, email_msg)
                    print(f"{time.time()} - Sent message to {recipient}")
                except:
                    print(f"{time.time()} - Error sending message to {recipient}")