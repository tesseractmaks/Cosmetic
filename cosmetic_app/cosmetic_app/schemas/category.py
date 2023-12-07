from pydantic import BaseModel, ConfigDict


class CategorySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str

class CategoryResponseSchema(CategorySchema):
    ...


class CategoryCreateSchema(CategorySchema):
    ...


class CategoryUpdateSchema(CategorySchema):
    ...


class CategoryUpdatePartialSchema(CategorySchema):
    ...
