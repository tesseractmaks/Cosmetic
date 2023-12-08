import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, update, delete

from cosmetic_app.models.brand import Brand
from cosmetic_app.schemas import (
    BrandSchema,
    BrandUpdateSchema,
    BrandCreateSchema,
    BrandUpdatePartialSchema,
)


async def read_brand_db(session: AsyncSession) -> list[BrandSchema]:
    query = select(Brand).order_by(Brand.id)
    result: Result = await session.execute(query)
    brands = result.scalars().all()
    return list(brands)


async def read_brand_by_id_db(session: AsyncSession, brand_id: uuid.uuid4) -> BrandSchema | None:
    return await session.get(Brand, brand_id)


async def create_brand_db(
        session: AsyncSession,
        brand_in: BrandCreateSchema,
) -> Brand:
    brand_obj = brand_in.model_dump()
    brand = Brand(**brand_obj)
    session.add(brand)
    await session.commit()
    return brand


async def update_brand_db(
    session: AsyncSession,
        brand: BrandSchema,
        brand_update: BrandUpdateSchema | BrandUpdatePartialSchema,
        partial: bool = False
) -> BrandSchema:
    for name, value in brand_update.model_dump(exclude_unset=partial).items():
        setattr(brand, name, value)
    await session.commit()
    return brand


async def delete_brand_db(session: AsyncSession, brand: BrandSchema) -> None:
    await session.delete(brand)
    await session.commit()