'''
Endpoint for all models.
'''

from .v1.base import BaseModel
from .v1.users import User

__all__ = [
    'BaseModel',
    'User',
]
