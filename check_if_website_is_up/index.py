import requests
import smtplib
from email.mime.text import MIMEText # Used for sending plain text email
from email.mime.multipart import MIMEMultipart # to attch in the email

def check_website(url):
    try:
        response = requests.get(url) # Send a GET request to the URL
        print(response)
        if response.status_code == 200: # if the status code is 200, the website is up
            return True
        else:
            return False
    except:
        return False

def send_email(sender_email, password, receiver_email, subject, body):
    message = MIMEMultipart() # prpare a message
    message['from'] = sender_email
    message['to'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body,'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls() # Start TLS encryption
        server.login(sender_email,password)
        text = message.as_string()
        server.sendmail(sender_email,receiver_email,text)
        server.quit() # Close the conncection
        print("Email sent Successfully")
    except:
        print("Faild to send the email")


url = "https://fakestoreapi.org/"

if not check_website(url):
    sender_email = "mihirkanojia95@gmail.com"
    subject = "Website is not Working"
    body = "the application is in a terminated state"
    receiver_email = "mihirkanojia95@gmail.com"
    password = "nsfu lrwx xesn uahg"
    send_email(sender_email, password, receiver_email, subject, body)
else:
    print("the website is UP!!")
