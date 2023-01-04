from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class SendEmail:

    def __init__(self, msg_to, server, email, password):
        self.msg_to = msg_to
        self.server = server
        self.email = email
        self.password = password

    def send_message_answer_yes(self):
        msg = MIMEMultipart()

        with open('New message.html') as f:
            read = f.read()

        html = read

        message = 'Приветик'

        msg['From'] = self.email
        msg['To'] = self.msg_to
        msg['Subject'] = 'Заголовок'
        password = self.password

        msg.attach(MIMEText(message, 'plain'))
        msg.attach(MIMEText(html, 'html'))

        server = smtplib.SMTP(f'smtp.{self.server}', 587)

        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(msg['From'], password)

        # Отправляем сообщение
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        print('Сообщение пользователю {0} было успешно отправлено!'.format(msg['To']))

    def send_message_answer_no(self):
        msg = MIMEMultipart()

        with open('New message.html') as f:
            read = f.read()

        html2 = read

        message = 'Приветик'

        msg['From'] = self.email
        msg['To'] = self.msg_to
        msg['Subject'] = 'Заголовок'
        password = self.password

        msg.attach(MIMEText(message, 'plain'))
        msg.attach(MIMEText(html2, 'html'))


        server = smtplib.SMTP(f'smtp.{self.server}', 587)

        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(msg['From'], password)

        # Отправляем сообщение
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        print('Сообщение пользователю {0} было успешно отправлено!'.format(msg['To']))
