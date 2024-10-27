"""Хелперы для работы с токенами"""

__author__: str = 'Старков Е.П.'

from datetime import datetime, timedelta, UTC
from jose import jwt, JWTError
from fastapi import Request

from ..exceptions import NotTokenInCookie, \
    NotValidToken, TokenExpired, NotUserId, NoSessionData, SessionClose
from ..models import SessionModel
from ..repository import SessionRepository
from step_vpn_service.settings import settings


def create_access_token(data: dict) -> str:
    """
    Создание токена доступа

    @param data: данные для токена
    @return: токен доступа
    """
    to_encode: dict = data.copy()
    to_encode.update({
        'exp': datetime.now(UTC) + timedelta(days=settings.TOKEN_EXPIRE_DAY)
    })

    return jwt.encode(to_encode, settings.SECRET_KEY, settings.ENCODE_ALGORITHM)


def get_token(request: Request) -> str | None:
    """
    Получение токена из запроса

    @param request: экземпляр запроса
    @return: токен доступа
    """
    token = request.cookies.get(settings.TOKEN_COOKIE_NAME)

    if not token:
        raise NotTokenInCookie()

    return token


async def get_user_id_from_token(access_token: str) -> int:
    """
    Получение идентификатора пользователя из токена

    @param access_token: токен доступа
    @return: идентификатор пользователя
    """
    try:
        decode_data = jwt.decode(access_token, settings.SECRET_KEY, settings.ENCODE_ALGORITHM)
    except JWTError as exc:
        raise NotValidToken() from exc

    expire: str = decode_data.get('exp')

    if not expire and int(expire) < datetime.now(UTC).timestamp():
        raise TokenExpired()

    user_id: str = decode_data.get('sub')

    if not user_id:
        raise NotUserId()

    session_data: SessionModel = await SessionRepository().find_one_or_none(token=access_token)

    if not session_data:
        raise NoSessionData()

    if not session_data.is_active:
        raise SessionClose()

    return int(user_id)
