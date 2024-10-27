"""Задачи по отправке писем"""

__author__: str = 'Старков Е.П.'


import smtplib

from pydantic import EmailStr

from dh_base.consts import TimeInSeconds
from .celery import celery
from .email_templates import create_confirmation_template, \
    create_restore_template, create_forgot_password_template
from dh_base.config import base_config


@celery.task(bind=True, max_retries=3, default_retry_delay=TimeInSeconds.hour)
def send_confirm_email(link: str, email_to: EmailStr) -> None:
    """
    Отправка письма подтверждения

    @param link: ссылка на подтверждение
    @param email_to: почта
    """
    content = create_confirmation_template(link, email_to)

    with smtplib.SMTP_SSL(base_config.SMTP_HOST, base_config.SMTP_PORT) as server:
        server.login(base_config.SMTP_USER, base_config.SMTP_PASSWORD)
        server.send_message(content)


@celery.task(bind=True, max_retries=3, default_retry_delay=TimeInSeconds.hour)
def send_restore_email(link: str, email_to: EmailStr) -> None:
    """
    Отправка письма восстановления
base_config
    @param link: ссылка на подтверждение
    @param email_to: почта
    """
    content = create_restore_template(link, email_to)

    with smtplib.SMTP_SSL(base_config.SMTP_HOST, base_config.SMTP_PORT) as server:
        server.login(base_config.SMTP_USER, base_config.SMTP_PASSWORD)
        server.send_message(content)


@celery.task(bind=True, max_retries=3, default_retry_delay=TimeInSeconds.hour)
def send_forgot_password_email(email_to: EmailStr) -> None:
    """
    Отправка письма об изменении пароля

    @param email_to: почта
    """
    content = create_forgot_password_template(email_to)

    with smtplib.SMTP_SSL(base_config.SMTP_HOST, base_config.SMTP_PORT) as server:
        server.login(base_config.SMTP_USER, base_config.SMTP_PASSWORD)
        server.send_message(content)
