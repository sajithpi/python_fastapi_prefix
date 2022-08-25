from email.message import EmailMessage
import ssl
import smtplib

my_email = 'sajithviolin96@gmail.com'
password = 'kdofppdwydfdnucc'
to_addr = 'radioboxmail@gmail.com'
subject = 'hi hello from python'

em = EmailMessage()
em['From'] = my_email
em['to'] = to_addr
em['subject'] = subject

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(my_email, password)
    smtp.sendmail(my_email, to_addr, em.as_string())
