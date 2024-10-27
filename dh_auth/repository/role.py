"""Репозиторий ролей"""

__author__: str = 'Старков Е.П.'

from ..models import RoleModel
from dh_base.repositories import BaseRepository
from step_vpn_service.database import Base


class RoleRepository(BaseRepository):
    """Репозиторий ролей"""
    @property
    def model(self) -> Base:
        return RoleModel

    @property
    def ordering_field_name(self) -> str:
        return RoleModel.__table__.c.name
