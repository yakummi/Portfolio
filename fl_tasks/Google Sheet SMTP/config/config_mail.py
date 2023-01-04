from task_smtp import SendEmail

yandex_email = '' # Яндекс почта
yandex_password = '' # Пароль от нее

google_email = '' # Гугл почта
google_password = '' # Пароль от нее



def check_mail(mail, answer):
    email = mail.split('@')[1]
    host = email.split('.')[0]
    if email == 'yandex.ru':
        my_mail = yandex_email
        gs = SendEmail(mail, email, my_mail, yandex_password)
        if answer == 'Нет':
            gs.send_message_answer_no()
        if answer == 'Да':
            gs.send_message_answer_yes()

    elif email == 'gmail.com':
        my_mail = google_email
        gs = SendEmail(mail, email, my_mail, google_password)
        if answer == 'Нет':
            gs.send_message_answer_no()
        if answer == 'Да':
            gs.send_message_answer_yes()
