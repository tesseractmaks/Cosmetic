from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
# from passlib.context import CryptContext
from cosmetic_app.core import logger

from cosmetic_app.crud import (
    read_product_db,
    update_product_db,
    create_product_db,
    delete_product_db,
    read_tag_by_title_db,
    read_category_by_title_db
)
from cosmetic_app.db import db_helper
from cosmetic_app.schemas import (
    ProductSchema,
    ProductCreateSchema,
    ProductUpdateSchema,
    ProductUpdatePartialSchema,
    ProductResponseSchema,
    TagResponseSchema, CategoryResponseSchema
)
from .depends_endps import product_by_id

# from cosmetic_app.auth import get_current_active_product

router = APIRouter(tags=["Product"])


@logger.catch
@router.get(
    "/",
    response_model=list[ProductResponseSchema]
)
async def read_products(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    products = await read_product_db(session=session)
    if products is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            headers={"X-Error": "Url format wrong"},
        )
    return products


@logger.catch
@router.get(
    "/{product_id}/",
    response_model=ProductResponseSchema
)
async def read_product_by_id(
        # current_product=Depends(get_current_active_product),
        product: ProductSchema = Depends(product_by_id)
):
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            headers={"X-Error": "Url format wrong"},
        )
    return product


# http://127.0.0.1:8000/api/v1/products/tag/lush/

@logger.catch
@router.get(
    "/tag/{tag_title}/",
    # response_model=TagResponseSchema
)
async def read_products_by_tag(
        tag_title: str,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    products = await read_tag_by_title_db(session=session, tag_title=tag_title)
    if products is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            headers={"X-Error": "Url format wrong"},
        )

    for product in products.products_assoc:
        print(product.title)

    return products.products_assoc


@logger.catch
@router.get(
    "/category/{category_title}/",
    # response_model=CategoryResponseSchema
)
async def read_products_by_tag(
        category_title: str,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),

):
    products = await read_category_by_title_db(session=session, category_title=category_title)
    if products is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            headers={"X-Error": "Url format wrong"},
        )
    # for product in products.products_assoc:
    #     print(product.title)
    return products.products_assoc


@logger.catch
@router.post(
    "/",
    response_model=ProductUpdatePartialSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_product(
        product_in: ProductCreateSchema,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # product_in.password = pwd_context.hash(product_in.password)
    return await create_product_db(session=session, product_in=product_in)


@logger.catch
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
    if product_update is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            headers={"X-Error": "Empty data"},
        )
    return await update_product_db(
        session=session,
        product=product,
        product_update=product_update,
    )


@logger.catch
@router.patch(
    "/{product_id}",
    response_model=ProductUpdatePartialSchema
)
async def update_product_partial(
        product_update: ProductUpdatePartialSchema,
        product: ProductSchema = Depends(product_by_id),
        # current_product=Depends(get_current_active_product),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    if product_update is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            headers={"X-Error": "Empty data"},
        )
    return await update_product_db(
        session=session,
        product=product,
        product_update=product_update,
        partial=True
    )


@logger.catch
@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product: ProductSchema = Depends(product_by_id),
        # current_product=Depends(get_current_active_product),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            headers={"X-Error": "Url format wrong"},
        )
    await delete_product_db(product=product, session=session)
