from email.message import EmailMessage
import ssl, smtplib

email_sender = ""
email_password = ""
email_receiver = ""

subject = "Email From Python"
body = """
Hello there. This is an email from Python.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

print("Sending Email...")
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, em.as_string())
print("E-mail sent.")
