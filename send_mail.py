import smtplib
from bolna import speak
from take_command import TC


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    to = input("please enter an email address to send an email to: ")
    speak("please tell me what to send them")
    content = TC()
    server.login("mehulverma04@gmail.com", "mehul@2605")
    server.sendmail("mehulverma04@gmail.com", to, content)
    server.close()
