"""Модуль конфигов приложения"""

from pydantic_settings import BaseSettings

__author__: str = "Старков Е.П."


class Settings(BaseSettings):
    """Класс конфигов"""

    class Config:
        """Конфигурация"""

        env_file: str = ".env"

    # Схема криптошифрования
    CRYPTO_CONTEXT_SCHEME: str
    # Алгоритм шифрования
    ENCODE_ALGORITHM: str
    # Секретный ключ приложения
    SECRET_KEY: str
    # Срок действия токена
    TOKEN_EXPIRE_DAY: int
    # Имя куки для токена
    TOKEN_COOKIE_NAME: str

    # Название задач Celery
    CELERY_AUTH_NAME: str


auth_config: Settings = Settings()
