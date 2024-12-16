"""Конечные точки сессий"""

__author__: str = "Старков Е.П."

from fastapi import Depends, APIRouter
from dh_user.model import UserModel
from dh_user.helpers import get_current_user

from ..schemas import SessionCloseIn
from ..services import SessionService

router: APIRouter = APIRouter(prefix="/session", tags=["Session"])


@router.post("/close", description="Закрытие сессии")
async def session_close(session_data: SessionCloseIn, user: UserModel = Depends(get_current_user)):
    """Закрытие сессии"""
    await SessionService.close(session_data.id, user)
    return {"success": True}


@router.post("/closeAll", description="Закрытие всех сессий текущего пользователя")
async def close_all(user: UserModel = Depends(get_current_user)):
    """Закрытие всех сессий"""
    await SessionService.close_all(user)
    return {"success": True}
