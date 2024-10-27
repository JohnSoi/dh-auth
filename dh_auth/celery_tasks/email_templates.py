"""Отправка писем"""

__author__: str = 'Старков Е.П.'


from email.message import EmailMessage

from pydantic import EmailStr

from step_vpn_service.settings import settings


def create_confirmation_template(link: str, email_to: EmailStr) -> EmailMessage:
    """
    Отправка письма подтверждения почты

    @param link: ссылка на подтверждение
    @param email_to: почта
    @return объект письма
    """
    email: EmailMessage = EmailMessage()

    email['Subject'] = 'Подтверждение регистрации'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f'''
            <h1>Вы зарегистрировались в {settings.APP_NAME}</h1>
            <p>Подтвердите свой email: <a href="{link}">Подтвердить</a></p>
        ''',
        subtype='html'
    )

    return email


def create_restore_template(link: str, email_to: EmailStr) -> EmailMessage:
    """
    Отправка письма восстановления пароля

    @param link: ссылка на восстановление
    @param email_to: почта
    @return объект письма
    """
    email: EmailMessage = EmailMessage()

    email['Subject'] = 'Восстановление доступа'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f'''
            <h1>Вы запросили восстановление пароля в {settings.APP_NAME}</h1>
            <p>
                Для восстановления пароля перейдите по ссылке: 
                <a href="{link}">Восстановить пароль</a>
            </p>
            <footer>* Токен восстановления доступен в течении 
            {settings.RESTORE_TOKEN_EXPIRE_HOUR} часов</footer>
        ''',
        subtype='html'
    )

    return email


def create_forgot_password_template(email_to: EmailStr) -> EmailMessage:
    """
    Отправка письма об изменении пароля

    @param email_to: почта
    @return объект письма
    """
    email: EmailMessage = EmailMessage()

    email['Subject'] = 'Изменение пароля'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f'''
            <h1>Ваш пароль был сброшен в {settings.APP_NAME}</h1>
            <p>
                Ваш пароль был сброшен в системе. Если это не вы срочно запросите смену пароля
            </p>    
        ''',
        subtype='html'
    )

    return email
