'''
Endpoint for all services.
'''

from services.v1.users.service import UserService

__all__ = [
    'UserService'
]
