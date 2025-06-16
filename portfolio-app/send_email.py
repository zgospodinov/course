import smtplib, ssl
from dotenv import load_dotenv
import os
from email.message import EmailMessage

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Load environment variables from .env in the same directory as the script
load_dotenv(os.path.join(SCRIPT_DIR, '.env'))



host = "smtp.gmail.com"
port = 465  # For SSL

user_name = os.getenv("EMAIL_USERNAME")
password = os.getenv("EMAIL_PASSWORD")  # Now safely stored in .env file

if not user_name or not password:
    raise ValueError("Email credentials not found in .env file. Please check your .env file configuration.")

receiver = "zdravko.gospodinov@gmail.com"
context = ssl.create_default_context()

message = """
Hi!
How are you?

By!
"""

msg = EmailMessage()
msg.set_content(message)
msg['Subject'] = 'Contact me from Portfolio App'
msg['From'] = user_name
msg['To'] = receiver

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user_name, password)
    server.send_message(msg)