"""Данные о сессии"""

__author__: str = "Старков Е.П."


from pydantic import BaseModel


class SessionCloseIn(BaseModel):
    """Данные для закрытия сессии"""


class SessionData(BaseModel):
    """Данные о сессии"""

    city: str
    country: str
    countryCode: str
    ip: str
    lat: float
    lon: float
    os: str
    regionName: str
    type: str
    userAgent: str


class SessionPublicData(SessionData):
    """Публичные данные о сессии"""

    is_active: bool
