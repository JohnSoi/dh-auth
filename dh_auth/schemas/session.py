"""Данные о сессии"""

__author__: str = "Старков Е.П."


from pydantic import BaseModel


class SessionCloseIn(BaseModel):
    """Данные для закрытия сессии"""


class SessionBaseData(BaseModel):
    city: str
    country: str
    ip: str
    lat: float
    lon: float
    os: str
    type: str


class SessionDataOut(SessionBaseData):
    country_code: str
    region_name: str
    user_agent: str


class SessionData(SessionBaseData):
    """Данные о сессии"""
    countryCode: str
    regionName: str
    userAgent: str


class SessionPublicData(SessionDataOut):
    """Публичные данные о сессии"""

    is_active: bool
