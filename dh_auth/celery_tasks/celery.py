"""Конфиг Celery"""

__author__: str = "Старков Е.П."

from celery import Celery
from dh_base.config import base_config
from celery.schedules import crontab

from dh_auth.config import auth_config

celery: Celery = Celery(
    auth_config.CELERY_AUTH_NAME,
    broker=base_config.REDIS_URL,
    include=[f"{base_config.APP_NAME}.celery_tasks.email_sender"],
    broker_connection_retry_on_startup=True,
)

celery.conf.update(timezone="UTC", enable_utc=True)

celery_beat: Celery = Celery(
    f"{auth_config.CELERY_AUTH_NAME}_beat",
    broker=base_config.REDIS_URL,
    include=[f"{base_config.APP_NAME}.celery_tasks.service"],
    broker_connection_retry_on_startup=True,
)

celery_beat.conf.update(timezone="UTC", enable_utc=True)

celery.conf.beat_schedule = {
    "delete_old_item_in_bd": {
        "task": f"{base_config.APP_NAME}.celery_tasks.service.delete_old_item",
        "schedule": crontab(hour="22", minute="0"),
    }
}
