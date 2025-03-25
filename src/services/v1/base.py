'''
Provides base services.
Base services are used as templates for other services.
'''

from typing import Generic, Type, TypeVar

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import Executable

from models import BaseModel
from schemas import BaseSchema

TModel = TypeVar('TModel', bound=BaseModel)
TSchema = TypeVar('TSchema', bound=BaseSchema)


class SessionMixin:
    '''
    Mixin provides a database session instance.

    Attributes:
    - session (AsyncSession): Asynchronous database session.

    Args:
    - session (AsyncSession): Asynchronous database session.
    '''

    def __init__(self, session: AsyncSession):
        self.session = session


class BaseService(SessionMixin):
    '''
    Base class of service.
    It is a parent class for other services.
    '''

    ...


class BaseDataManager(SessionMixin, Generic[TModel, TSchema]):
    '''
    Base class of data manager.
    Supports generic types.

    Attributes:
    - session (AsyncSession): Asynchronous database session.
    - model (Type[TModel]): Data model.
    - schema (Type[TSchema]): Data schema.

    Args:
    - session (AsyncSession): Asynchronous database session.
    - model (Type[TModel]): Data model type.
    - schema (Type[TSchema]): Data schema type.
    '''

    def __init__(self, session: AsyncSession, model: Type[TModel], schema: Type[TSchema]):
        super().__init__(session)
        self.model = model
        self.schema = schema

    async def add_one(self, model: TModel) -> TSchema | None:
        '''
        Adds one entry to the database.

        Args:
        - model (TModel): Data model instance.

        Returns:
        - TSchema | None: Schema of the added entry or None.

        Exceptions:
        - SQLAlchemyError: An error occurred while adding the entry.
        '''

        try:
            self.session.add(model)
            await self.session.commit()
            await self.session.refresh(model)
            return self.schema(**model.to_dict())
        except SQLAlchemyError as error:
            await self.session.rollback()
            print(f'[Error] Error while adding an entry: {error}') # Change to a logger.
            raise

    async def get_one(self, select_statement: Executable) -> TModel | None:
        '''
        Receives one entry from a database.

        Args:
        - select_statement (Executable): SQL-query for selection.

        Returns:
        - TModel | None: Received entry as a model or None.

        Exceptions:
        - SQLAlchemyError: An error occurred while getting the entry.
        '''

        try:
            entry = await self.session.execute(select_statement)
            return entry.scalar()
        except SQLAlchemyError as error:
            print(f'[Error] Error while getting an entry: {error}') # Change to a logger.
            raise
