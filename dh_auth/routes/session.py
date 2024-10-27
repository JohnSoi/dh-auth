"""Конечные точки сессий"""

__author__: str = 'Старков Е.П.'

from fastapi import APIRouter, Depends

from ..schemas import SessionCloseIn
from ..services import SessionService
from step_vpn_service.users.helpers import get_current_user
from step_vpn_service.users.model import UserModel

router: APIRouter = APIRouter(prefix='/session', tags=['Session'])


@router.post('/close', description='Закрытие сессии')
async def session_close(session_data: SessionCloseIn, user: UserModel = Depends(get_current_user)):
    """Закрытие сессии"""
    await SessionService.close(session_data.id, user)
    return {'success': True}


@router.post('/closeAll', description='Закрытие всех сессий текущего пользователя')
async def close_all(user: UserModel = Depends(get_current_user)):
    """Закрытие всех сессий"""
    await SessionService.close_all(user)
    return {'success': True}
