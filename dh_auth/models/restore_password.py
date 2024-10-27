# pylint: disable=too-few-public-methods
"""Модуль работы с моделью восстановления пароля"""

__author__: str = 'Старков Е.П.'

from uuid import UUID

from sqlalchemy import Uuid, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from dh_base.column import IdColumns, DateEditColumns
from step_vpn_service.database import Base


class ForgotPasswordModel(IdColumns, Base, DateEditColumns):
    """Модель восстановления доступа"""
    __tablename__: str = 'forgot_password'

    token: Mapped[UUID] = mapped_column(Uuid, index=True)
    is_used: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
