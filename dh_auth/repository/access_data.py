"""Репозиторий доступа"""

__author__: str = "Старков Е.П."

from typing import Type

from dh_user.model import UserModel
from dh_base.repositories import BaseRepository

from ..consts import ADMIN_ROLE_KEY
from ..models import AccessDataModel
from ..exceptions import NoActiveAccessData, NotAccessOperation


class AccessDataRepository(BaseRepository):
    """Репозиторий доступа"""

    @property
    def model(self) -> Type[AccessDataModel]:
        return AccessDataModel

    @property
    def ordering_field_name(self) -> str:
        return AccessDataModel.__table__.c.login

    async def get_data_with_permission(self, user_id: int, user: UserModel) -> AccessDataModel:
        """
        Получить данные о доступе с проверкой прав

        @param user_id: идентификатор пользователя
        @param user: данные о текущем пользователе
        @return: данные о доступе
        """
        if user_id != user.id and user.access_data.role.key != ADMIN_ROLE_KEY:
            raise NotAccessOperation()

        access_data: AccessDataModel = await self.find_one_or_none(user_id=user_id)

        if not access_data:
            raise NoActiveAccessData()

        return access_data
