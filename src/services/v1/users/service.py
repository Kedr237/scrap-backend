'''
Provides a service for working with users with business logic.

Classes:
    UserService
'''

import os

from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import UserModel
from schemas import (
    RegistrationResponseSchema,
    RegistrationSchema,
    UserRole,
    UserSchema,
)

from ..base import BaseService
from .manager import UserManager

pwd_context = CryptContext(
    schemes=['argon2'],
    deprecated='auto',
    argon2__time_cost=2,
    argon2__memory_cost=102400,
    argon2__parallelism=os.cpu_count(),
)


class UserService(BaseService):
    '''
    Service for user management.
    Contains high level methods for business logic.

    Args:
        session (AsyncSession): An asynchronous database session.

    Attributes:
        session (AsyncSession): An asynchronous database session.
        _manager (UserManager): A manager for working with user data.
    '''

    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self._manager = UserManager(session)

    async def create(self, user: RegistrationSchema) -> RegistrationResponseSchema:
        '''
        Create a new user.

        Args:
            user (RegistrationSchema): A schema describing a user to create.

        Returns:
            RegistrationResponseSchema: A schema for successful registration.

        Raises:
            Exception: Any exception when creating a new user.
        '''

        user_model = UserModel(
            username=user.username,
            email=user.email,
            hashed_password=self.hash_password(user.password),
            role=UserRole.USER,
        )

        try:
            user_created = await self._manager.add_user(user_model)

            user_response = RegistrationResponseSchema(
                user_id=user_created.id,
            )
            return user_response

        except HTTPException:
            raise

        except Exception as e:
            print(f'[Error] {e}')  # Change to a logger.
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='An error occurred while creating the user.',
            )

    async def get_by_email(self, email: str) -> UserSchema:
        ...

    def hash_password(self, password: str) -> str:
        '''
        Generates a password hash.

        Args:
            password (str): Original password.

        Returns:
            str: Hashed password.
        '''
        return pwd_context.hash(password)

    async def get_all(self):  # delete
        try:
            users = await self.session.execute(select(UserModel))
            return users.scalars().all()
        except Exception as e:
            print(f'[Error] {e}')
