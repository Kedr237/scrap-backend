'''
User schemas.
'''

from datetime import datetime
from enum import Enum

from pydantic import EmailStr

from ..base import BaseModelSchema


class UserRole(str, Enum):
    '''
    System user roles.

    Attributes:
        ADMIN (str): Administrator role.
        USER (str): User role.
    '''

    ADMIN = 'admin'
    USER = 'user'


class UserSchema(BaseModelSchema):
    '''
    User schema.

    Attributes:
        username (str): Username.
        email (EmailStr): User email.
        role (UserRole): System user role.
        avatar (str | None): User avatar link.
        last_seen (datetime): Date and time of the last user visit.
    '''

    username: str
    email: EmailStr
    role: UserRole
    avatar: str | None = None
    last_seen: datetime
