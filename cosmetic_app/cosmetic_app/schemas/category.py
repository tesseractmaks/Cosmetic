from pydantic import BaseModel, ConfigDict


class CategorySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
