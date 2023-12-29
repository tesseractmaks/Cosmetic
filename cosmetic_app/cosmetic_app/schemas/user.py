from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from fastapi import UploadFile, File
from uuid import UUID, uuid4

from typing import TYPE_CHECKING

# if TYPE_CHECKING:
from cosmetic_app.schemas.profile import ProfileSchema


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: str
    password: str
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None


class UserResponseSchema(UserSchema):
    id: UUID = Field(default_factory=uuid4)
    profile: ProfileSchema


class UserCreateSchema(UserSchema):
    ...


class UserUpdateSchema(UserSchema):
    ...


class UserUpdatePartialSchema(UserSchema):
    ...