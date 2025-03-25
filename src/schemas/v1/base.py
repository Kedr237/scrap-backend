'''
Contains schemas that define base settings
and can be used in other schemas.

Schemas:
- BaseSchema
- BaseModelSchema
- BaseInputSchema
- BaseResponseSchema
'''

from datetime import datetime
from typing import Optional, Dict, Any

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    '''
    Base schema for other schemas.
    Contains only the general configuration.

    Attributes:
    - model_config (ConfigDict): Allows attributes to be used as fields.

    Methods:
    - to_dict(): Converts the object into a dictionary.
    '''

    model_config = ConfigDict(from_attributes=True)

    def to_dict(self) -> Dict[str, Any]:
        '''
        Converts the schema instance to a dictionary.

        Returns:
        - Dict[str, Any]: A dictionary representing the schema.
        '''
        return self.model_dump()


class BaseModelSchema(BaseSchema):
    '''
    Base schema for data model schemas.
    Contains general configuration and attributes for all model schemas.

    Attributes:
    - id (int): Model id.
    - is_available (bool): Whether the model is available.
    - created_at (datetime): Creation date.
    - updated_at (datetime): Modification date.
    '''

    id: Optional[int] = None
    is_available: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class BaseInputSchema(BaseSchema):
    '''
    Base schema for input data.
    Does not contain id and other fields unnecessary for input data.
    '''

    ...


class BaseResponseSchema(BaseSchema):
    '''
    Base schema for API responses.
    Provides a common configuration for all response schemas.

    Attributes:
    - success (bool): Indicates whether the request was successful.
    - message (Optional[str]): Message associated with the request.
    '''

    success: bool
    message: Optional[str] = None
