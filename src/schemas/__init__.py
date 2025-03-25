'''
Endpoint for all schemas.
'''

from .v1.auth.register import RegisterInputSchema, RegisterResponseSchema
from .v1.base import BaseSchema
from .v1.users.users import UserRole

__all__ = [
    'BaseSchema',
    'RegisterInputSchema',
    'RegisterResponseSchema',
    'UserRole',
]
