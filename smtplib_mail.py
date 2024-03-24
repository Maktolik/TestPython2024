from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path


my_email = EmailMessage()

html_template = Template(Path("templates/index.html").read_text())
html_content = html_template.substitute({'name': 'Tolik', 'date': 'tomorrow'})

my_email['from'] = 'Tolik <makarenko@gmail.com>'
my_email['to'] = 'Test@mail.com'
my_email['subject'] = 'Take me with you!'
my_email.set_content(html_content, 'html')

with open('images/dancing.gif', 'rb') as image_file:
    image_data = image_file.read()
    my_email.add_attachment(image_data, 'image', 'gif', filename='dancing.gif')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    smtp_server.send_message(my_email)
    print('Email sent!')