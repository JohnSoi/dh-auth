"""Репозиторий восстановления доступа"""

__author__: str = 'Старков Е.П.'

from ..models import ForgotPasswordModel
from dh_base.repositories import BaseRepository
from step_vpn_service.database import Base


class ForgotPasswordRepository(BaseRepository):
    """Репозиторий восстановления доступа"""
    @property
    def model(self) -> Base:
        return ForgotPasswordModel

    @property
    def ordering_field_name(self) -> str:
        return ForgotPasswordModel.__table__.c.token
