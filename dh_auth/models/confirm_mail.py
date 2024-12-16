# pylint: disable=too-few-public-methods
"""Модуль работы с моделью подтверждения"""

__author__: str = "Старков Е.П."

from uuid import UUID

from sqlalchemy import Uuid, Boolean, ForeignKey
from dh_base.mixins import ConvertToDictMixin
from sqlalchemy.orm import Mapped, mapped_column
from dh_base.columns import IdColumns, DateEditColumns
from dh_base.database import Base


class ConfirmEmail(IdColumns, Base, DateEditColumns, ConvertToDictMixin):
    """Модель подтверждение почты"""

    __tablename__: str = "confirm_email"

    token: Mapped[UUID] = mapped_column(Uuid, index=True)
    is_used: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    contact_id: Mapped[int] = mapped_column(ForeignKey("contacts.id", ondelete="CASCADE"))
