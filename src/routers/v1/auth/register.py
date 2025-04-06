from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db_session
from schemas import RegistrationResponseSchema, RegistrationSchema
from services import UserService


def setup_router(router: APIRouter) -> None:
    @router.post('/')
    async def register_user(
        user: RegistrationSchema,
        db_session: AsyncSession = Depends(get_db_session),
    ) -> RegistrationResponseSchema:
        return await UserService(db_session).create(user)
