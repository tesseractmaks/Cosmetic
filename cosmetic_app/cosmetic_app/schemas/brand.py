from pydantic import BaseModel, ConfigDict


class BrandSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
