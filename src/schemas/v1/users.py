'''
User schemas.
'''

from enum import Enum


class UserRole(str, Enum):
    '''
    System user roles.

    Attributes:
    - ADMIN (str): Administrator role.
    - USER (str): User role.
    '''

    ADMIN = 'admin'
    USER = 'user'
