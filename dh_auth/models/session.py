# pylint: disable=invalid-name
"""Модель сессии"""

__author__: str = 'Старков Е.П.'

from dataclasses import dataclass

from sqlalchemy import Integer, ForeignKey, String, Text, Boolean, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dh_base.column import DateEditColumns
from step_vpn_service.database import Base


@dataclass
class LocationInfo:
    """Данные о положении"""
    city: Mapped[str] = mapped_column(Text)
    country: Mapped[str] = mapped_column(Text)
    country_code: Mapped[str] = mapped_column(Text)
    region_name: Mapped[str] = mapped_column(Text)
    lat: Mapped[float] = mapped_column(Float)
    lon: Mapped[float] = mapped_column(Float)


@dataclass
class OsInfo:
    """Данные о клиенте"""
    os: Mapped[str] = mapped_column(String(40))
    type: Mapped[str] = mapped_column(String(40))
    user_agent: Mapped[str] = mapped_column(Text)


@dataclass
class SessionModel(LocationInfo, OsInfo, DateEditColumns, Base):
    """Модель сессии"""
    __tablename__: str = 'sessions'

    id: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    token: Mapped[str] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    ip: Mapped[str] = mapped_column(Text)

    user: Mapped['UserModel'] = relationship(back_populates='session', lazy=False)
