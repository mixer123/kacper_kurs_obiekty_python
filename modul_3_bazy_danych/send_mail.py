import smtplib, ssl
smtp_server = 'smtp.gmail.com'
port = 465
sender_email = 'cos'
password ='cos'
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:

    server.login(sender_email, password)
    server.sendmail(sender_email, sender_email,'subject', 'tresc maila')
