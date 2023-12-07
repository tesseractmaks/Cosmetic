from datetime import datetime
from pydantic import BaseModel, ConfigDict
from fastapi import UploadFile, File

from .user import UserSchema


class ProfileSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="allow")
    nickname: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    photo: UploadFile = File(default=None)
    user: UserSchema
    created_at: datetime
    updated_at: datetime | None = None

