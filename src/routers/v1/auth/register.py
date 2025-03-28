'''
Provides a function for connecting registration endpoints.
'''

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db_session
from schemas import RegistrationResponseSchema, RegistrationSchema
from services import UserService


def setup_router(router: APIRouter) -> None:
    '''
    Connects endpoints to router.

    Routes:
        POST /: New user registration.
    '''

    @router.post('/')
    async def register_user(
        user: RegistrationSchema,
        db_session: AsyncSession = Depends(get_db_session),
    ) -> RegistrationResponseSchema:
        '''
        Register a new user.

        Returns:
            RegistrationResponseSchema: Response schema for successful registration.
        '''
        return await UserService(db_session).create(user)

    @router.get('/')  # delete
    async def get_all(
        db_session: AsyncSession = Depends(get_db_session),
    ):
        return await UserService(db_session).get_all()
