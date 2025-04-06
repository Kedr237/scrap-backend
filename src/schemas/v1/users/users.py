from datetime import datetime
from enum import Enum

from pydantic import EmailStr

from ..base import BaseModelSchema


class UserRole(str, Enum):

    ADMIN = 'admin'
    USER = 'user'


class UserSchema(BaseModelSchema):

    username: str
    email: EmailStr
    role: UserRole
    avatar: str | None = None
    last_seen: datetime
