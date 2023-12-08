from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
# from passlib.context import CryptContext

from cosmetic_app.crud import (
    read_brand_db,
    update_brand_db,
    create_brand_db,
    delete_brand_db
)
from cosmetic_app.db import db_helper
from cosmetic_app.schemas import (
    BrandSchema,
    BrandCreateSchema,
    BrandUpdateSchema,
    BrandUpdatePartialSchema,
    BrandResponseSchema
)
from .depends_endps import brand_by_id

# from cosmetic_app.auth import get_current_active_brand

router = APIRouter(tags=["Brand"])


@router.get(
    "/",
    response_model=list[BrandResponseSchema]
)
async def read_brands(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await read_brand_db(session=session)


@router.get(
    "/{brand_id}/",
    response_model=BrandResponseSchema
)
async def read_brand_by_id(
        # current_brand=Depends(get_current_active_brand),
        brand: BrandSchema = Depends(brand_by_id)
):
    return brand


@router.post(
    "/",
response_model=BrandResponseSchema,
status_code=status.HTTP_201_CREATED
)
async def create_brand(
        brand_in: BrandCreateSchema,
        session: AsyncSession= Depends(db_helper.scoped_session_dependency)
):
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # brand_in.password = pwd_context.hash(brand_in.password)
    return await create_brand_db(session=session, brand_in=brand_in)


@router.put(
    "/{brand_id}",
    response_model=BrandResponseSchema
)
async def update_brand(
        brand_update: BrandUpdateSchema,
        brand: BrandSchema = Depends(brand_by_id),
        # current_brand = Depends(get_current_active_brand),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_brand_db(
        session=session,
        brand=brand,
        brand_update=brand_update,
    )

@router.patch(
    "/{brand_id}",
    response_model=BrandResponseSchema
)
async def update_brand_partial(
        brand_update: BrandUpdatePartialSchema,
        brand: BrandSchema = Depends(brand_by_id),
# current_brand=Depends(get_current_active_brand),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_brand_db(
        session=session,
        brand=brand,
        brand_update=brand_update,
        partial=True
    )


@router.delete("/{brand_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_brand(
        brand: BrandSchema = Depends(brand_by_id),
# current_brand=Depends(get_current_active_brand),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await delete_brand_db(brand=brand, session=session)



