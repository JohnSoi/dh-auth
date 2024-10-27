"""Исключения доступа"""

__author__: str = 'Старков Е.П.'

from fastapi import status
from dh_base.exception import BaseAppException


class LoginExist(BaseAppException):
    """Логин уже существует"""
    STATUS_CODE: int = status.HTTP_409_CONFLICT
    DETAIL: str = 'Данный логин уже используется в системе'


class NoActiveAccessData(BaseAppException):
    """Нет данных о доступе"""
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = 'Не найдены активные данные о доступе'


class NotFoundConfirmToken(BaseAppException):
    """Нет токена доступа"""
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = 'Не найден токен доступа'


class ConfirmTokenExpire(BaseAppException):
    """Токен доступа истек"""
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = 'Токен подтверждения истек. Запросите новый'


class ConfirmTokenUsed(BaseAppException):
    """Токен подтверждения использован"""
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = 'Токен подтверждения уже использован'


class NotFoundRestoreToken(BaseAppException):
    """Токен восстановления не найден"""
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = 'Не найден токен восстановления'


class RestoreTokenExpire(BaseAppException):
    """Токен восстановления истек"""
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = 'Токен восстановления истек. Запросите новый'


class RestoreTokenUsed(BaseAppException):
    """Токен восстановления использован"""
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = 'Токен восстановления уже использован'


class NotAccessOperation(BaseAppException):
    """Нет доступа к операции"""
    STATUS_CODE: int = status.HTTP_406_NOT_ACCEPTABLE
    DETAIL: int = 'У вас нет доступа к данной операцией над пользователем'
