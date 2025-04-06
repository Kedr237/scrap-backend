from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from models import UserModel
from schemas import UserSchema

from ..base import BaseManager


class UserManager(BaseManager[UserModel, UserSchema]):

    def __init__(self, session: AsyncSession):
        '''
        Initializes the UserManager.

        Args:
            session (AsyncSession): An asynchronous database session.
        '''
        super().__init__(session=session, model=UserModel, schema=UserSchema)

    async def add_user(self, user: UserModel) -> UserSchema | None:
        try:
            new_user = await self.add_one(user)
            return new_user

        except SQLAlchemyError as e:
            print(f'[Error] Error when adding a new user: {e}')  # Change to a logger.
            raise

    async def get_by_email(self, email: str) -> UserSchema | None:
        statement = select(self.model).where(self.model.email == email)
        user = await self.get_one(statement)
        return user
