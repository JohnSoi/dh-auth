"""Данные по ролям"""

__author__: str = "Старков Е.П."


from uuid import UUID

from pydantic import BaseModel


class RoleAuth(BaseModel):
    """Данные о роли при регистрации"""

    role_id: int


class RolePublicData(BaseModel):
    """Публичные данные о роли"""

    name: str
    key: str
    uuid: UUID
