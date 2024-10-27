"""Репозиторий сессий"""

__author__: str = "Старков Е.П."

from dh_base.database import Base
from dh_base.repositories import BaseRepository

from ..models import SessionModel


class SessionRepository(BaseRepository):
    """Репозиторий сессий"""

    @property
    def model(self) -> Base:
        return SessionModel

    @property
    def ordering_field_name(self) -> str:
        return SessionModel.__table__.c.token
