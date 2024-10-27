"""Хелперы для работы с паролем"""

__author__: str = 'Старков Е.П.'

from passlib.context import CryptContext

from step_vpn_service.settings import settings

pwd_conntext = CryptContext(schemes=[settings.CRYPTO_CONTEXT_SCHEME], deprecated='auto')


def get_password_hash(password: str) -> str:
    """
    Хеширование пароля

    @param password: пароль
    @return: хеш пароля
    """
    return pwd_conntext.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Проверка пароля

    @param plain_password: проверяемый пароль
    @param hashed_password: хеш пароля
    @return: совпадают ли пароли?
    """
    return pwd_conntext.verify(plain_password, hashed_password)
