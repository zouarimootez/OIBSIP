import smtplib
from email.mime.text import MIMEText
from speech.text_to_speech import speak

def send_email(to, subject, body):
    try:
        sender_email = "your email"
        sender_password = "your password"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to, msg.as_string())
        speak("Email sent successfully!")
    except Exception as e:
        speak("Sorry, I couldn't send the email.")