"""Сервис для работы с сессиями"""

__author__: str = 'Старков Е.П.'

from datetime import datetime

from sqlalchemy import Update, update

from step_vpn_service.auth.consts import ADMIN_ROLE_KEY
from step_vpn_service.auth.exceptions import SessionNotFound, CloseSessionOtherUser
from step_vpn_service.auth.models import SessionModel
from step_vpn_service.auth.repository import SessionRepository
from step_vpn_service.users.model import UserModel


class SessionService:
    """Сервис для работы с сессиями"""

    @staticmethod
    async def close(session_id: int, user: UserModel) -> None:
        """
        Закрытие сессии по идентификатору

        @param session_id: идентификатор сессии
        @param user: данные пользователя
        """
        session_repository: SessionRepository = SessionRepository()
        session_data: SessionModel = await session_repository.get(session_id)

        if not session_data:
            raise SessionNotFound()

        if session_data.user_id != user.id and user.access_data.role.key != ADMIN_ROLE_KEY:
            raise CloseSessionOtherUser()

        await session_repository.delete(session_data.id)

    @staticmethod
    async def close_all(user: UserModel) -> None:
        """
        Закрытие всех сессий пользователя

        @param user: данные пользователя
        """
        query: Update = update(SessionModel).where(SessionModel.user_id == user.id).values(
            date_delete=datetime.now(),
            date_update=datetime.now(),
            is_active=False
        )
        await SessionRepository().manual_execute(query)