from datetime import datetime
from pydantic import BaseModel, ConfigDict
from fastapi import UploadFile, File




from cosmetic_app.schemas.category import CategorySchema
from cosmetic_app.schemas.brand import BrandSchema


class ProductSchema(BaseModel):
    # id: int
    model_config = ConfigDict(from_attributes=True)
    title: str
    article_number: str
    price: int
    # image: UploadFile = File(...)
    image: str
    # brand: "BrandSchema"
    created_at: datetime
    updated_at: datetime | None = None


class ProductResponseSchema(ProductSchema):
    categories: CategorySchema
    brand: BrandSchema


class ProductCreateSchema(ProductSchema):
    ...


class ProductUpdateSchema(ProductSchema):
    ...


class ProductUpdatePartialSchema(ProductSchema):
    ...