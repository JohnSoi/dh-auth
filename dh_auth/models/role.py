# pylint: disable=too-few-public-methods
"""Модуль работы с моделью роли"""

__author__: str = 'Старков Е.П.'

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dh_base.columns import IdColumns
from dh_base.database import Base


class RoleModel(IdColumns, Base):
    """Модель роли"""
    __tablename__: str = 'roles'

    name: Mapped[str] = mapped_column(String(40), index=True)
    key: Mapped[str] = mapped_column(String(20), index=True)

    access_data: Mapped['AccessDataModel'] = relationship(back_populates='role', lazy=False)
