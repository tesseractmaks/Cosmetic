from datetime import datetime
from pydantic import BaseModel, ConfigDict
from fastapi import UploadFile, File

from .brand import BrandSchema
from .category import CategorySchema


class ProductSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="allow")
    title: str
    article_number: str
    price: int
    image: UploadFile = File(...)
    brand: BrandSchema
    category: CategorySchema
    created_at: datetime
    updated_at: datetime | None = None

