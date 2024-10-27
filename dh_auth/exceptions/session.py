"""Исключения сессий"""

__author__: str = "Старков Е.П."

from fastapi import status
from dh_base.exceptions import BaseAppException


class SessionNotFound(BaseAppException):
    """Сессия не найдена"""

    _CODE = status.HTTP_400_BAD_REQUEST
    _DETAIL = "Сессия не найдена"


class CloseSessionOtherUser(BaseAppException):
    """Закрытие не своей сессии"""

    _CODE = status.HTTP_406_NOT_ACCEPTABLE
    _DETAIL = "Сессию может закрыть только ее пользователь"
