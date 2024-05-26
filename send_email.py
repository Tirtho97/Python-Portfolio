import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "lucifer.dummy11@gmail.com"
    password = "ztyg wwde iojo iwkv"
    reciever = "lucifer.dummy11@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)