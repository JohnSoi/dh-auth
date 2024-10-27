"""Сервис доступа"""

__author__: str = 'Старков Е.П.'


from datetime import datetime, timedelta, UTC
from uuid import UUID, uuid4

from fastapi import Response
from pydantic import EmailStr

from ..exceptions import NotFoundConfirmToken, ConfirmTokenExpire, \
    ConfirmTokenUsed, NotFoundRestoreToken, RestoreTokenUsed
from ..helpers.auth import verify_password, get_password_hash
from ..helpers.token import create_access_token
from ..models import SessionModel, ConfirmEmail, ForgotPasswordModel
from ..repository import AccessDataRepository, SessionRepository, \
    ConfirmEmailRepository, ForgotPasswordRepository
from ..schemas import LoginData
from step_vpn_service.contacts.consts import ContactType
from step_vpn_service.contacts.model import ContactModel
from step_vpn_service.contacts.repository import ContactRepository
from step_vpn_service.settings import settings
from dh_user.exceptions import UserNotFound
from dh_user.model import UserModel
from dh_user.repository import UserRepository
from ..celery_tasks.email_sender import send_restore_email, send_forgot_password_email


class AccessService:
    """Сервис доступа"""
    @classmethod
    async def login_user(cls, response: Response, payload: LoginData) -> dict[str, str]:
        """
        Авторизация пользователя

        @param response: экземпляр ответа
        @param payload: данные для авторизации
        @return: данные о токене доступа
        """
        user = await cls._get_user_by_login_and_password(payload.login, payload.password)

        if not user:
            raise UserNotFound()

        access_token = create_access_token({'sub': str(user.id)})
        await SessionRepository().create({
            **payload.dict(),
            'user_id': user.id,
            'token': access_token
        })
        response.set_cookie(settings.TOKEN_COOKIE_NAME, access_token, httponly=True)

        return {'access_token': access_token}

    @classmethod
    async def logout(cls, response: Response, access_token: str) -> None:
        """
        Выход из системы

        @param response: экземпляр ответа
        @param access_token: токен доступа
        """
        session: SessionModel = await SessionRepository().find_one_or_none(token=access_token)

        if session:
            await SessionRepository().delete(session.id)

        response.set_cookie(settings.TOKEN_COOKIE_NAME, '', httponly=True)

    @classmethod
    async def confirm_email(cls, confirm_uuid: UUID) -> dict[str, bool]:
        """
        Подтверждение почты

        @param confirm_uuid: токен подтверждения
        @return: данные о подтверждении
        """
        confirm_data: ConfirmEmail = await ConfirmEmailRepository().find_one_or_none(
            token=confirm_uuid
        )

        if not confirm_data:
            raise NotFoundConfirmToken()

        if (confirm_data.date_create + timedelta(
                hours=settings.CONFIRM_TOKEN_EXPIRE_HOUR)) < (datetime.now(UTC)
        ):
            raise ConfirmTokenExpire()

        if confirm_data.is_used:
            raise ConfirmTokenUsed()

        contact_data: ContactModel = await ContactRepository().find_one_or_none(
            user_id=confirm_data.user_id, type=ContactType.EMAIL
        )

        if contact_data:
            await ContactRepository().update(contact_data.id, {
                'is_confirm': True
            })

        await ConfirmEmailRepository().update(confirm_data.id, {
            'is_used': True
        })

        return {'success': True, 'token': confirm_uuid}

    @classmethod
    async def forgot_password(cls, email: EmailStr) -> dict[str, bool]:
        """
        Запрос восстановления пароля

        @param email: почта
        @return: успешность операции
        """
        contact_exist: ContactModel = await ContactRepository().find_one_or_none(value=email)

        token: UUID = uuid4()
        result: dict[str, bool] = {'success': True}

        if not contact_exist:
            return result

        await ForgotPasswordRepository().create({
            'token': token,
            'user_id': contact_exist.user_id
        })

        send_restore_email.delay(f'/auth/restore_password/{token}', email)

        return result

    @classmethod
    async def restore_password(cls, restore_uuid: UUID, password: str) -> dict[str, bool | UUID]:
        """
        Восстановления пароля

        @param restore_uuid: токен восстановления
        @param password: новый пароль
        @return: данные о восстановлении
        """
        token_exist: ForgotPasswordModel = await ForgotPasswordRepository().find_one_or_none(
            token=restore_uuid
        )

        if not token_exist:
            raise NotFoundRestoreToken()

        if token_exist.is_used:
            raise RestoreTokenUsed()

        if (token_exist.date_create + timedelta(
                hours=settings.CONFIRM_TOKEN_EXPIRE_HOUR)) < (datetime.now(UTC)
        ):
            raise ConfirmTokenExpire()

        await ForgotPasswordRepository().update(token_exist.id, {'is_used': True})

        user_exist: UserModel = await UserRepository().get(token_exist.user_id)

        if not user_exist:
            raise UserNotFound()

        await UserRepository().update(user_exist.id, {'password': get_password_hash(password)})

        send_forgot_password_email.delay(await user_exist.email_value)

        return {
            'success': True,
            'token': restore_uuid
        }

    @classmethod
    async def _get_user_by_login_and_password(cls, login: str, password: str) -> UserModel | None:
        """
        Получение пользователя по логину и паролю

        @param login: логин
        @param password: пароль
        @return: модель пользователя или None - если данные не корректны
        """
        existing_user: UserModel | None = await AccessDataRepository().find_one_or_none(login=login)

        if not existing_user or not verify_password(password, existing_user.password):
            return None

        return existing_user
