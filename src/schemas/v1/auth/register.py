'''
Schemas for a registration system.

Classes:
    RegistrationSchema
    RegistrationResponseSchema
'''

from pydantic import EmailStr, Field

from ..base import BaseInputSchema, BaseResponseSchema


class RegistrationSchema(BaseInputSchema):
    '''
    User registration schema.

    Attributes:
        username (str): Username (no more than 50 characters).
        email (EmailStr): User email.
        password (str): Password (at least 8 characters).
    '''

    username: str = Field(min_length=0, max_length=50, description='Username')
    email: EmailStr = Field(description='User email')
    password: str = Field(min_length=8, description='Password (at least 8 characters)')


class RegistrationResponseSchema(BaseResponseSchema):
    '''
    Response schema for successful registration.

    Attributes:
        user_id (int): User ID.
        message (str): Message on successful registration.
    '''

    user_id: int
    success: bool = True
    message: str = 'Registration was successful'
