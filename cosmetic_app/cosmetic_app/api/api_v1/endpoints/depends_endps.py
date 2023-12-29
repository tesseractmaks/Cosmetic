import uuid
from typing import Annotated
from fastapi import HTTPException, status, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from cosmetic_app.crud import (
    read_user_by_id_db,
    read_profile_by_id_db,
    read_tag_by_id_db,
    read_category_by_id_db,
    read_product_by_id_db
)
from cosmetic_app.db.db_helper import db_helper
from cosmetic_app.schemas import (
    UserSchema,
    ProductSchema,
    ProfileSchema,
    TagSchema,
    CategorySchema
)


async def user_by_id(
        user_id: Annotated[uuid.uuid4, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> UserSchema:
    user = await read_user_by_id_db(session=session, user_id=user_id)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="not found..."
    )


async def profile_by_id(
        profile_id: Annotated[uuid.uuid4, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> ProfileSchema:
    profile = await read_profile_by_id_db(session=session, profile_id=profile_id)
    if profile is not None:
        return profile
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="not found..."
    )


async def product_by_id(
        product_id: Annotated[uuid.uuid4, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> ProductSchema:
    product = await read_product_by_id_db(session=session, product_id=product_id)
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="not found..."
    )


async def category_by_id(
        category_id: Annotated[uuid.uuid4, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CategorySchema:
    category = await read_category_by_id_db(session=session, category_id=category_id)
    if category is not None:
        return category
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="not found..."
    )


async def tag_by_id(
        tag_id: Annotated[uuid.uuid4, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> TagSchema:
    tag = await read_tag_by_id_db(session=session, tag_id=tag_id)
    if tag is not None:
        return tag
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="not found..."
    )
