import os

from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

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

    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self._manager = UserManager(session)

    async def create(self, user: RegistrationSchema) -> RegistrationResponseSchema:
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

        except IntegrityError as e:
            if 'users_email_key' in str(e):
                print(f'[Error] A user with email [{user.email}] already exists.')  # Change to a logger.
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'A user with email [{user.email}] already exists.',
                )

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='An error occurred while creating the user.',
            )

    async def get_by_email(self, email: str) -> UserSchema:
        ...

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
