from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
# from passlib.context import CryptContext

from cosmetic_app.crud import (
    read_category_db,
    update_category_db,
    create_category_db,
    delete_category_db
)
from cosmetic_app.db import db_helper
from cosmetic_app.schemas import (
    CategorySchema,
    CategoryCreateSchema,
    CategoryUpdateSchema,
    CategoryUpdatePartialSchema,
    CategoryResponseSchema
)
from .depends_endps import category_by_id

# from cosmetic_app.auth import get_current_active_category

router = APIRouter(tags=["Category"])


@router.get(
    "/",
    response_model=list[CategoryResponseSchema]
)
async def read_categorys(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await read_category_db(session=session)


@router.get(
    "/{category_id}/",
    response_model=CategoryResponseSchema
)
async def read_category_by_id(
        # current_category=Depends(get_current_active_category),
        category: CategorySchema = Depends(category_by_id)
):
    return category


@router.post(
    "/",
response_model=CategoryResponseSchema,
status_code=status.HTTP_201_CREATED
)
async def create_category(
        category_in: CategoryCreateSchema,
        session: AsyncSession=Depends(db_helper.scoped_session_dependency)
):
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # category_in.password = pwd_context.hash(category_in.password)
    return await create_category_db(session=session, category_in=category_in)


@router.put(
    "/{category_id}",
    response_model=CategoryResponseSchema
)
async def update_category(
        category_update: CategoryUpdateSchema,
        category: CategorySchema = Depends(category_by_id),
        # current_category = Depends(get_current_active_category),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_category_db(
        session=session,
        category=category,
        category_update=category_update,
    )

@router.patch(
    "/{category_id}",
    response_model=CategoryResponseSchema
)
async def update_category_partial(
        category_update: CategoryUpdatePartialSchema,
        category: CategorySchema = Depends(category_by_id),
# current_category=Depends(get_current_active_category),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_category_db(
        session=session,
        category=category,
        category_update=category_update,
        partial=True
    )


@router.delete("/{category_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
        category: CategorySchema = Depends(category_by_id),
# current_category=Depends(get_current_active_category),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await delete_category_db(category=category, session=session)



