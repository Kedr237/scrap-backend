'''
Contains only the base sqlalchemy model.
'''

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    '''
    Base sqlalchemy model.

    Attributes:
    - id (int): Model id.
    - is_available (bool): Whether the model is available.
    - created_at (datetime): Creation date.
    - updated_at (datetime): Modification date.
    '''

    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    is_available: Mapped[bool] = mapped_column(default=True)

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
    )
