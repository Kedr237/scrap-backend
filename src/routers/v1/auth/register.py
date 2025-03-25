'''
Provides a function for connecting registration endpoints.
'''

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db_session
from schemas import RegisterInputSchema, RegisterResponseSchema


def setup_router(router: APIRouter) -> None:
    '''
    Connects endpoints to router.

    Routes:
    - POST /: New user registration.
    '''

    @router.post('/')
    async def register_user(
        user: RegisterInputSchema,
        db_session: AsyncSession = Depends(get_db_session),
    ) -> RegisterResponseSchema:
        '''
        Register a new user.

        Returns:
        - RegisterResponseSchema: Response schema for successful registration.
        '''
        ...
