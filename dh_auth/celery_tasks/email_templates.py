"""Отправка писем"""

__author__: str = "Старков Е.П."


from email.message import EmailMessage

from pydantic import EmailStr
from dh_base.config import base_config


def create_confirmation_template(link: str, email_to: EmailStr) -> EmailMessage:
    """
    Отправка письма подтверждения почты

    @param link: ссылка на подтверждение
    @param email_to: почта
    @return объект письма
    """
    email: EmailMessage = EmailMessage()

    email["Subject"] = "Подтверждение регистрации"
    email["From"] = base_config.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Вы зарегистрировались в {base_config.APP_NAME}</h1>
            <p>Подтвердите свой email: <a href="{link}">Подтвердить</a></p>
        """,
        subtype="html",
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

    email["Subject"] = "Восстановление доступа"
    email["From"] = base_config.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Вы запросили восстановление пароля в {base_config.APP_NAME}</h1>
            <p>
                Для восстановления пароля перейдите по ссылке: 
                <a href="{link}">Восстановить пароль</a>
            </p>
            <footer>* Токен восстановления доступен в течении 
            {base_config.RESTORE_TOKEN_EXPIRE_HOUR} часов</footer>
        """,
        subtype="html",
    )

    return email


def create_forgot_password_template(email_to: EmailStr) -> EmailMessage:
    """
    Отправка письма об изменении пароля

    @param email_to: почта
    @return объект письма
    """
    email: EmailMessage = EmailMessage()

    email["Subject"] = "Изменение пароля"
    email["From"] = base_config.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Ваш пароль был сброшен в {base_config.APP_NAME}</h1>
            <p>
                Ваш пароль был сброшен в системе. Если это не вы срочно запросите смену пароля
            </p>    
        """,
        subtype="html",
    )

    return email
