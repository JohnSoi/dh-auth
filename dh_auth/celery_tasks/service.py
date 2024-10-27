"""Сервисные задачи"""

__author__: str = "Старков Е.П."


from datetime import UTC, datetime, timedelta

from sqlalchemy import Delete, Select, delete, select
from dh_user.model import UserModel
from dh_base.config import base_config
from dh_base.database import Base, sync_session_maker

from .celery import celery
from ..models import ConfirmEmail, SessionModel, ForgotPasswordModel

MODELS: list[Base] = [SessionModel, ConfirmEmail, ForgotPasswordModel, UserModel]


@celery.task
def delete_old_item() -> None:
    """Удаление старых записей"""
    with sync_session_maker() as session:
        for model in MODELS:
            query: Select = select(model).where(
                model.date_delete < datetime.now(UTC) + timedelta(days=base_config.DAYS_DELETE_PLD_ITEM)
            )
            temp_result = session.execute(query)

            if not temp_result:
                continue

            ids: list[int] = [item.id for item in list(temp_result.scalars().all())]

            delete_query: Delete = delete(model).where(model.id.in_(ids))

            session.execute(delete_query)
