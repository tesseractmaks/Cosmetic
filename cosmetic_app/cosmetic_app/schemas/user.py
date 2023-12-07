from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr
from fastapi import UploadFile, File

from .profile import ProfileSchema


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="allow")
    email: EmailStr
    password: str
    is_active: bool
    profile: ProfileSchema = None
    created_at: datetime
    updated_at: datetime | None = None
