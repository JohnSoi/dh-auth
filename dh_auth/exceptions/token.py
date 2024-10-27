"""Исключения токена"""

__author__: str = 'Старков Е.П.'

from fastapi import status
from dh_base.base.exception import BaseAppException


class NotTokenInCookie(BaseAppException):
    """Нет токена в запросе"""
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = 'Нет данных о токене доступа'


class NotValidToken(BaseAppException):
    """Токен не валидный"""
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = 'Невалидный токен доступа'


class TokenExpired(BaseAppException):
    """Токен истек"""
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = 'Токен доступа истек'


class NotUserId(BaseAppException):
    """Нет данных о пользователе в токене"""
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = 'Нет данных о пользователе в токене'


class NoSessionData(BaseAppException):
    """Нет данных о сессии"""
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = 'Нет данных о сессии'


class SessionClose(BaseAppException):
    """Сессия закрыта"""
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = 'Сессия закрыта'
