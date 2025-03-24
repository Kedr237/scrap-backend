'''
Schemas for a registration system.

Schemas:
- RegistrationSchema
'''

from pydantic import EmailStr, Field

from ..base import BaseInputSchema, BaseResponseSchema


class RegisterInputSchema(BaseInputSchema):
    '''
    User creation schema.

    Attributes:
    - username (str): Username (no more than 50 characters).
    - email (EmailStr): User email.
    - password (str): Password (at least 8 characters).
    '''

    username: str = Field(min_length=0, max_length=50, description='Username')
    email: EmailStr = Field(description='User email')
    password: str = Field(min_length=8, description='Password (at least 8 characters)')


class RegisterResponseSchema(BaseResponseSchema):
    '''
    Response schema for successful registration.

    Attributes:
    - user_id (int): User ID.
    - message (str): Message on successful registration.
    '''

    user_id: int
    success: bool = True
    message: str = 'Registration was successful'
