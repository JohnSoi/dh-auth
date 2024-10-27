# pylint: disable=unnecessary-ellipsis
"""Схемы данных авторизации"""

__author__: str = 'Старков Е.П.'


from pydantic import BaseModel, EmailStr

from ..schemas.role import RolePublicData
from ..schemas.session import SessionData


class AuthData(BaseModel):
    """Данные авторизации"""
    login: str
    password: str


class LoginData(AuthData, SessionData):
    """Данные для входа"""
    ...


class AccessDataPublic(BaseModel):
    """Публичные данные о доступе"""
    is_active: bool
    login: str
    role: RolePublicData


class ForgotPassword(BaseModel):
    """Данные для запроса восстановления"""
    email: EmailStr


class RestorePassword(BaseModel):
    """Данные для восстановления"""
    password: str
