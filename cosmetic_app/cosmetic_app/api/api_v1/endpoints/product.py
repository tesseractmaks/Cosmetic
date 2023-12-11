from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
# from passlib.context import CryptContext

from cosmetic_app.crud import (
    read_product_db,
    update_product_db,
    create_product_db,
    delete_product_db
)
from cosmetic_app.db import db_helper
from cosmetic_app.schemas import (
    ProductSchema,
    ProductCreateSchema,
    ProductUpdateSchema,
    ProductUpdatePartialSchema,
    ProductResponseSchema
)
from .depends_endps import product_by_id

# from cosmetic_app.auth import get_current_active_product

router = APIRouter(tags=["Product"])


@router.get(
    "/",
    response_model=list[ProductResponseSchema]
)
async def read_products(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await read_product_db(session=session)


@router.get(
    "/{product_id}/",
    response_model=ProductResponseSchema
)
async def read_product_by_id(
        # current_product=Depends(get_current_active_product),
        product: ProductSchema = Depends(product_by_id)
):
    return product


@router.post(
    "/",
response_model=ProductResponseSchema,
status_code=status.HTTP_201_CREATED
)
async def create_product(
        product_in: ProductCreateSchema,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # product_in.password = pwd_context.hash(product_in.password)
    return await create_product_db(session=session, product_in=product_in)


@router.put(
    "/{product_id}",
    response_model=ProductResponseSchema
)
async def update_product(
        product_update: ProductUpdateSchema,
        product: ProductSchema = Depends(product_by_id),
        # current_product = Depends(get_current_active_product),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_product_db(
        session=session,
        product=product,
        product_update=product_update,
    )

@router.patch(
    "/{product_id}",
    response_model=ProductResponseSchema
)
async def update_product_partial(
        product_update: ProductUpdatePartialSchema,
        product: ProductSchema = Depends(product_by_id),
# current_product=Depends(get_current_active_product),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_product_db(
        session=session,
        product=product,
        product_update=product_update,
        partial=True
    )


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product: ProductSchema = Depends(product_by_id),
# current_product=Depends(get_current_active_product),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await delete_product_db(product=product, session=session)



