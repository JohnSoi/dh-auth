"""Репозиторий восстановления доступа"""

__author__: str = "Старков Е.П."

from dh_base.database import Base
from dh_base.repositories import BaseRepository

from ..models import ForgotPasswordModel


class ForgotPasswordRepository(BaseRepository):
    """Репозиторий восстановления доступа"""

    @property
    def model(self) -> Base:
        return ForgotPasswordModel

    @property
    def ordering_field_name(self) -> str:
        return ForgotPasswordModel.__table__.c.token
