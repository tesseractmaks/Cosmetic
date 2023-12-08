from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
# from fastapi import UploadFile, File



from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cosmetic_app.schemas import UserSchema


class ProfileSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    model_config = ConfigDict(from_attributes=True)
    nickname: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    photo: str | None = None #UploadFile = File(default=None)

    user_id: UUID = Field(default_factory=uuid4)
    created_at: datetime | None = None
    updated_at: datetime | None = None


class ProfileResponseSchema(ProfileSchema):
    ...


class ProfileCreateSchema(ProfileSchema):
    ...


class ProfileUpdateSchema(ProfileSchema):
    ...


class ProfileUpdatePartialSchema(ProfileSchema):
    ...