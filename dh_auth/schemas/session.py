"""Данные о сессии"""

__author__: str = 'Старков Е.П.'


from pydantic import BaseModel


class SessionCloseIn(BaseModel):
    """Данные для закрытия сессии"""


class SessionData(BaseModel):
    """Данные о сессии"""
    city: str
    country: str
    country_code: str
    ip: str
    lat: float
    lon: float
    os: str
    region_name: str
    type: str
    user_agent: str


class SessionPublicData(SessionData):
    """Публичные данные о сессии"""
    is_active: bool
