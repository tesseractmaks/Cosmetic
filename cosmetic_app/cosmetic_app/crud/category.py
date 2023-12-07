import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, update, delete

from cosmetic_app.models import Category
from cosmetic_app.schemas import (
    CategorySchema,
    CategoryUpdateSchema,
    CategoryCreateSchema,
    CategoryUpdatePartialSchema,
)


async def read_category_db(session: AsyncSession) -> list[CategorySchema]:
    query = select(Category).order_by(Category.id)
    result: Result = await session.execute(query)
    categorys = result.scalars().all()
    return list(categorys)


async def read_category_by_id_db(session: AsyncSession, category_id: uuid.uuid4) -> CategorySchema | None:
    return await session.get(Category, category_id)


async def create_category_db(
        session: AsyncSession,
        category_in: CategoryCreateSchema,
) -> Category:
    category_obj = category_in.model_dump()
    category = Category(**category_obj)
    session.add(category)
    await session.commit()
    return category


async def update_category_db(
    session: AsyncSession,
        category: CategorySchema,
        category_update: CategoryUpdateSchema | CategoryUpdatePartialSchema,
        partial: bool = False
) -> CategorySchema:
    for name, value in category_update.model_dump(exclude_unset=partial).items():
        setattr(category, name, value)
    await session.commit()
    return category


async def delete_category_db(session: AsyncSession, category: CategorySchema) -> None:
    await session.delete(category)
    await session.commit()