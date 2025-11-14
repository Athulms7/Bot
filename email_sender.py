import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()

SKILLS = ["react", "node", "flask", "postgres", "tailwind", "typescript", "mongodb"]

def filter_jobs(all_jobs):
    filtered = []
    for job in all_jobs:
        text = (job["title"] + " " + job["company"]).lower()
        if any(skill in text for skill in SKILLS):
            filtered.append(job)
    return filtered

def send_email(jobs):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "🔎 Daily Full-Stack Jobs Update"
    msg["From"] = sender
    msg["To"] = sender

    if not jobs:
        html = "<p>No new matching jobs found today.</p>"
    else:
        html = "<h2>Today's Matching Jobs</h2>"
        for j in jobs:
            html += (f"<b>{j['title']}</b> — {j['company']}<br>"
                     f"📍 {j['location']} | 🌐 {j['source']}<br>"
                     f"<a href='{j['link']}'>Apply here</a><br><br>")
    msg.attach(MIMEText(html, "html"))
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(sender, password)
        s.send_message(msg)
