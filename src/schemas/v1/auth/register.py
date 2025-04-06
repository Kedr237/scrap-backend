from pydantic import EmailStr, Field

from ..base import BaseInputSchema, BaseResponseSchema


class RegistrationSchema(BaseInputSchema):

    username: str = Field(min_length=0, max_length=50, description='Username')
    email: EmailStr = Field(description='User email')
    password: str = Field(min_length=8, description='Password (at least 8 characters)')


class RegistrationResponseSchema(BaseResponseSchema):

    user_id: int
    success: bool = True
    message: str = 'Registration was successful'
