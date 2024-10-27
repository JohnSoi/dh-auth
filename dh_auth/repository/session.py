"""Репозиторий сессий"""

__author__: str = 'Старков Е.П.'

from ..models import SessionModel
from dh_base.repositories import BaseRepository
from step_vpn_service.database import Base


class SessionRepository(BaseRepository):
    """Репозиторий сессий"""
    @property
    def model(self) -> Base:
        return SessionModel

    @property
    def ordering_field_name(self) -> str:
        return SessionModel.__table__.c.token
