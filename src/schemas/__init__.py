'''
Endpoint for all schemas.
'''

from .v1.auth.register import RegistrationResponseSchema, RegistrationSchema
from .v1.base import BaseSchema
from .v1.users.users import UserRole, UserSchema

__all__ = [
    'BaseSchema',
    'RegistrationResponseSchema',
    'RegistrationSchema',
    'UserRole',
    'UserSchema',
]
