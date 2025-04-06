from datetime import datetime
from typing import Any, Dict

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump()


class BaseModelSchema(BaseSchema):

    id: int | None = None
    is_available: bool | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class BaseInputSchema(BaseSchema):
    ...


class BaseResponseSchema(BaseSchema):

    success: bool
    message: str | None = None
