import smtplib, ssl
from dotenv import load_dotenv
import os
from email.message import EmailMessage

def send_email(sent_from, message_content):
    load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

    host = "smtp.gmail.com"
    port = 465  # For SSL

    user_name = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")

    if not user_name or not password:
        raise ValueError("Email credentials not found in .env file. Please check your .env file configuration.")

    context = ssl.create_default_context()

    msg = EmailMessage()
    msg.set_content(message_content + f"\n\n{sent_from}")
    msg['Subject'] = f'Contact me from Portfolio App: {sent_from}'
    msg['From'] = sent_from
    msg['To'] = user_name

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.send_message(msg)


if __name__ == "__main__":
    # Example usage for testing:
    send_email("zdravko.gospodinov@gmail.com", "Hey there, Zdravko!")
    