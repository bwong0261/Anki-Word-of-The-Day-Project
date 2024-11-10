import random
import smtplib
import time
import schedule


schedule
smtplib
time

sender_email = 'bwong@student.dalat.org'
sender_password = 'uhqe nvef qoij wekp'
recipient_email = 'benjamin02615@gmail.com'

def send_email():
    subject = 'Work On Coding!'
    body = 'Come on lets finish this project!'

    message = f'Subject: {subject}\n\n{body}'

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

schedule.every().day.at('22:52').do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)
