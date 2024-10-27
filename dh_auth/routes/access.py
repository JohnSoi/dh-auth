"""Конечные точки для доступа"""

__author__: str = "Старков Е.П."


from uuid import UUID

from fastapi import Depends, Response, APIRouter

from ..helpers import get_token
from ..schemas import LoginData, ForgotPassword, RestorePassword
from ..services import AccessService

router: APIRouter = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", description="Вход в систему")
async def login(response: Response, payload: LoginData):
    """Вход"""
    return await AccessService.login_user(response, payload)


@router.post("/logout", description="Выход из системы")
async def logout(response: Response, access_token: str = Depends(get_token)):
    """Выход"""
    return await AccessService.logout(response, access_token)


@router.post("/forgot_password", description="Обработка отправки письма для восстановления пароля")
async def forgot_password(payload: ForgotPassword):
    """Запрос восстановления gпароля"""
    return await AccessService.forgot_password(payload.email)


@router.post("/restore_password/{restore_uuid}", description="Восстановление пароля")
async def restore_password(restore_uuid: UUID, payload: RestorePassword):
    """Восстановление пароля"""
    return await AccessService.restore_password(restore_uuid, payload.password)


@router.post("/confirm_email/{confirm_uuid}", description="Подтверждение почты")
async def confirm_email(confirm_uuid: UUID):
    """Подтверждение почты"""
    return await AccessService.confirm_email(confirm_uuid)
