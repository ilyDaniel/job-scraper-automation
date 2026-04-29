import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()




def send_email(new_jobs):
    if not new_jobs:
        return



    sender_email = os.getenv("EMAIL_SENDER")
    receiver_email = os.getenv("EMAIL_RECEIVER")
    app_password = os.getenv("EMAIL_PASSWORD")

    subject = "New Job Listings Found!"

    body = "New jobs found:\n\n"
    body += f"\nChecked at: {datetime.now()}"

    for job in new_jobs:
        body += f"{job['title']} ({job['location']})\n{job['link']}\n\n"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print("Email failed:", e)