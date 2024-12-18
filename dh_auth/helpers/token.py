"""Хелперы для работы с токенами"""

__author__: str = "Старков Е.П."

from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt
from fastapi import Request

from ..config import auth_config
from ..models import SessionModel
from ..exceptions import NotUserId, SessionClose, TokenExpired, NoSessionData, NotValidToken, NotTokenInCookie
from ..repository import SessionRepository


def create_access_token(data: dict) -> str:
    """
    Создание токена доступа

    @param data: данные для токена
    @return: токен доступа
    """
    to_encode: dict = data.copy()
    to_encode.update({"exp": datetime.now(UTC) + timedelta(days=auth_config.TOKEN_EXPIRE_DAY)})

    return jwt.encode(to_encode, auth_config.SECRET_KEY, auth_config.ENCODE_ALGORITHM)


def get_token(request: Request) -> str | None:
    """
    Получение токена из запроса

    @param request: экземпляр запроса
    @return: токен доступа
    """
    token = request.cookies.get(auth_config.TOKEN_COOKIE_NAME) or request.headers.get("authorization")

    if "Bearer " in token:
        token = token.replace("Bearer ", "")

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
        decode_data = jwt.decode(access_token, auth_config.SECRET_KEY, auth_config.ENCODE_ALGORITHM)
    except JWTError as exc:
        raise NotValidToken() from exc

    expire: str = decode_data.get("exp")

    if not expire and int(expire) < datetime.now(UTC).timestamp():
        raise TokenExpired()

    user_id: str = decode_data.get("sub")

    if not user_id:
        raise NotUserId()

    session_data: SessionModel = await SessionRepository().find_one_or_none(token=access_token)

    if not session_data:
        raise NoSessionData()

    if not session_data.is_active:
        raise SessionClose()

    return int(user_id)
