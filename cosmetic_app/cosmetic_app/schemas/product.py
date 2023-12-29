from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TagSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str


class CategorySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str


class ProductSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    link_detail: str
    price: int
    image: str
    label: str
    num_goods: str
    data_goods: str
    created_at: datetime
    updated_at: datetime | None = None


class ProductResponseSchema(ProductSchema):
    model_config = ConfigDict(from_attributes=True)
    category_assoc: list[CategorySchema]
    tags_assoc: list[TagSchema]


class ProductCreateSchema(ProductSchema):
    ...


class ProductUpdateSchema(ProductSchema):
    ...


class ProductUpdatePartialSchema(ProductSchema):
    ...
