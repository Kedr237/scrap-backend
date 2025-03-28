'''
User models.

Classes:
    UserModel
'''

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from schemas import UserRole

from ..base import BaseModel


class UserModel(BaseModel):
    '''
    Base user model.

    Attributes:
    - username (str): Username.
    - email (str): User email.
    - hashed_password (str): Hashed password.
    - role (UserRole): System user role.
    - avatar (str): User avatar link.
    - last_seen (datetime): Date and time of the last user visit.
    '''

    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(nullable=False, default='User')
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(nullable=False, default=UserRole.USER)
    avatar: Mapped[str] = mapped_column(nullable=True)
    last_seen: Mapped[datetime] = mapped_column(
        nullable=False,
        server_default=func.now(),
    )
