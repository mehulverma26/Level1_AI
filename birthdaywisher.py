def birthdays():
    import datetime
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from bolna import speak

    dencryptedE = "mehulverma04@gmail.com"
    dencryptedP = "mehul@2605"

    def emailscript1(email, subject, message):
        fromaddr = dencryptedE
        toaddr = email
        msg = MIMEMultipart()
        msg["From"] = fromaddr
        msg["To"] = toaddr
        msg["Subject"] = subject
        body = message
        msg.attach(MIMEText(body, "plain"))
        filename = "birthday.jpg"
        attachment = open("H:\FRIDAY\FRIDAY\\birthday.jpg", "rb")
        p = MIMEBase("application", "octet-stream")
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header("Content-Disposition", "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(fromaddr, dencryptedP)
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

    friends = []
    f = open("friends.txt", "r")
    for line in f:
        entityList = line.split(",")
        k = entityList[0]
        v = entityList[1]
        friends.append(v)
        friends.append(k)
    f.close

    now = datetime.datetime.now()
    date = now.strftime("%d-%m")
    for x in range(len(friends)):
        if date == friends[x]:
            email = friends[x + 1]
            subject = "Hapy Birthday"
            message = "Happy Birthday to the best person on the planet"
            emailscript1(email, subject, message)
            if email == "lghtnngfast@gmail.com":
                print("email sent to dummy")
                speak("email sent to dummy")
            elif email == "makkarjaivardhan8f@gmail.com":
                print("Today is Jai's birthday. Birthday email sent to Jai.")
                speak("Today is Jai's birthday. Birthday email sent to Jai.")
            elif email == "varunsharma20004@gmail.com":
                print("Today is varun's birthday. Birthday email sent to Varun.")
                speak("Today is varun's birthday. Birthday email sent to Varun.")
            else:
                print("today is", email, "'s birthday. Birthday email sent to them.")
                speak("today is " + email + "'s birthday. Birthday email sent to them.")
