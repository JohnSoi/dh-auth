"""Сервисные задачи"""

__author__: str = 'Старков Е.П.'


from datetime import datetime, UTC, timedelta

from sqlalchemy import Select, select, delete, Delete

from step_vpn_service.celery_tasks.celery import celery
from step_vpn_service.database import sync_session_maker, Base
from step_vpn_service.auth.models import SessionModel, ConfirmEmail, ForgotPasswordModel
from step_vpn_service.settings import settings
from step_vpn_service.users.model import UserModel

MODELS: list[Base] = [SessionModel, ConfirmEmail, ForgotPasswordModel, UserModel]


@celery.task
def delete_old_item() -> None:
    """Удаление старых записей"""
    with sync_session_maker() as session:
        for model in MODELS:
            query: Select = select(model).where(
                model.date_delete < datetime.now(UTC) + timedelta(days=settings.DAYS_DELETE_PLD_ITEM)
            )
            temp_result = session.execute(query)

            if not temp_result:
                continue

            ids: list[int] = [item.id for item in list(temp_result.scalars().all())]

            delete_query: Delete = delete(model).where(model.id.in_(ids))

            session.execute(delete_query)
