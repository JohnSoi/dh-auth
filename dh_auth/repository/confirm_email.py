"""Репозиторий подтверждения почты"""

__author__: str = "Старков Е.П."

from dh_base.database import Base
from dh_base.repositories import BaseRepository

from ..models import ConfirmEmail


class ConfirmEmailRepository(BaseRepository):
    """Репозиторий подтверждения почты"""

    @property
    def model(self) -> Base:
        return ConfirmEmail

    @property
    def ordering_field_name(self) -> str:
        return ConfirmEmail.__table__.c.token
