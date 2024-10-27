"""Репозиторий подтверждения почты"""

__author__: str = 'Старков Е.П.'

from ..models import ConfirmEmail
from dh_base.repositories import BaseRepository
from step_vpn_service.database import Base


class ConfirmEmailRepository(BaseRepository):
    """Репозиторий подтверждения почты"""
    @property
    def model(self) -> Base:
        return ConfirmEmail

    @property
    def ordering_field_name(self) -> str:
        return ConfirmEmail.__table__.c.token
