# pylint: disable=too-few-public-methods
"""Модуль данных для доступа"""

__author__: str = 'Старков Е.П.'

from datetime import date

from sqlalchemy import Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dh_base.database import Base


class AccessDataModel(Base):
    """Модель данных доступа"""
    __tablename__: str = 'access_data'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    login: Mapped[str] = mapped_column(String(50), index=True)
    password: Mapped[str] = mapped_column(String(100))

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    date_last_auth: Mapped[date] = mapped_column(Date, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id', ondelete='CASCADE'))

    user: Mapped['UserModel'] = relationship(back_populates='access_data', lazy=False)
    role: Mapped['RoleModel'] = relationship(back_populates='access_data', lazy=False)
