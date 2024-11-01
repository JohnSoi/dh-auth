"""Репозиторий ролей"""

__author__: str = "Старков Е.П."

from dh_base.database import Base
from dh_base.repositories import BaseRepository

from ..models import RoleModel


class RoleRepository(BaseRepository):
    """Репозиторий ролей"""

    @property
    def model(self) -> Base:
        return RoleModel

    @property
    def ordering_field_name(self) -> str:
        return RoleModel.__table__.c.name
