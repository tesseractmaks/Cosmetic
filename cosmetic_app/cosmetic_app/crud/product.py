import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, update, delete

from cosmetic_app.models import Product
from cosmetic_app.schemas import (
    ProductSchema,
    ProductUpdateSchema,
    ProductCreateSchema,
    ProductUpdatePartialSchema,
)


async def read_product_db(session: AsyncSession) -> list[ProductSchema]:
    query = select(Product).order_by(Product.id)
    result: Result = await session.execute(query)
    products = result.scalars().all()
    return list(products)


async def read_product_by_id_db(session: AsyncSession, product_id: uuid.uuid4) -> ProductSchema | None:
    return await session.get(Product, product_id)


async def create_product_db(
        session: AsyncSession,
        product_in: ProductCreateSchema,
) -> Product:
    product_obj = product_in.model_dump()
    product = Product(**product_obj)
    session.add(product)
    await session.commit()
    return product


async def update_product_db(
    session: AsyncSession,
        product: ProductSchema,
        product_update: ProductUpdateSchema | ProductUpdatePartialSchema,
        partial: bool = False
) -> ProductSchema:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product_db(session: AsyncSession, product: ProductSchema) -> None:
    await session.delete(product)
    await session.commit()