import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(jobs):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receiver = os.getenv("EMAIL_USER")

    message = MIMEMultipart("alternative")
    message["Subject"] = "🔎 Daily Full Stack Job Updates"
    message["From"] = sender
    message["To"] = receiver

    if not jobs:
        body = "No new jobs found today."
    else:
        body = "<h3>Today's Job Listings</h3><ul>"
        for job in jobs:
            body += f"<li><a href='{job}'>{job}</a></li>"
        body += "</ul>"

    message.attach(MIMEText(body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(message)
