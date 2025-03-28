'''
Provides a manager for User model.

Managers facilitate low-level communication with the database.

Classes:
    UserManager
'''

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import UserModel
from schemas import UserSchema

from ..base import BaseManager


class UserManager(BaseManager[UserModel, UserSchema]):
    '''
    A manager for working with users through a database.

    Attributes:
        session (AsyncSession): Asynchronous database session.
        model (Type[UserModel]): User model class.
        schema (Type[UserSchema]): User schema class.
    '''

    def __init__(self, session: AsyncSession):
        '''
        Initializes the UserManager.

        Args:
            session (AsyncSession): An asynchronous database session.
        '''
        super().__init__(session=session, model=UserModel, schema=UserSchema)

    async def add_user(self, user: UserModel) -> UserSchema | None:
        '''
        Add a new user to a database.

        Args:
            user (UserModel): User model instance to add.

        Returns:
            UserSchema|None: Schema describing a new user or None.

        Raises:
            IntegrityError: Error when adding a new user.
        '''
        try:
            new_user = await self.add_one(user)
            return new_user
        except IntegrityError as e:
            if 'users_email_key' in str(e):
                print(f'[Error] A user with email [{user.email}] already exists.\n{e}')  # Change to a logger.
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'A user with email [{user.email}] already exists.',
                )
            else:
                print(f'[Error] Error when adding a new user: {e}')  # Change to a logger.
                raise

    async def get_by_email(self, email: str) -> UserSchema | None:
        '''
        Receives a user by email.

        Args:
            email (str): A user email.

        Returns:
            UserSchema|None: A User schema or None.
        '''
        statement = select(self.model).where(self.model.email == email)
        user = await self.get_one(statement)
        return user
