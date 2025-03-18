'''
User models.

Models:
- User
'''

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func


from .base import BaseModel
from .types import str_50
from schemas import UserRole


class User(BaseModel):
    '''
    Base user model.

    Attributes:
    - username (str_50): User name.
    - email (str): User email.
    - password (str): Hashed password.
    - role (UserRole): System user role.
    - avatar (str): User avatar link.
    - last_seen (datetime): Date and time of the last user visit.
    '''

    __tablename__ = 'users'

    username: Mapped[str_50] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(default=UserRole.USER)
    avatar: Mapped[str] = mapped_column(nullable=True)
    last_seen: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
