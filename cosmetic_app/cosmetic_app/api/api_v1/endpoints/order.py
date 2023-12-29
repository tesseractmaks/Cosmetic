from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
# from passlib.context import CryptContext

from cosmetic_app.crud import (
    read_order_db,
    # update_order_db,
    create_order_db,
    # delete_order_db,
)
from cosmetic_app.db import db_helper
from cosmetic_app.schemas import (
    OrderSchema,
    OrderResponseSchema,
    OrderCreateSchema,
    OrderUpdateSchema,
    OrderUpdatePartialSchema,
)

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

router = APIRouter(tags=["Order"])


@router.get(
    "/",
    # response_model=list[ProductResponseSchema]
)
async def read_orders(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await read_order_db(session=session)


# @router.get(
#     "/{order_id}/",
#     response_model=ProductResponseSchema
# )
# async def read_order_by_id(
#         # current_order=Depends(get_current_active_order),
#         order: ProductSchema = Depends(order_by_id)
# ):
#     return order


# http://127.0.0.1:8000/api/v1/orders/tag/lush/


@router.post(
    "/",
    response_model=OrderResponseSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_order(
        order_in: ProductCreateSchema,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # order_in.password = pwd_context.hash(order_in.password)
    return await create_order_db(session=session, order_in=order_in)

#
# @router.put(
#     "/{order_id}",
#     # response_model=OrderResponseSchema
# )
# async def update_order(
#         order_update: ProductUpdateSchema,
#         order: ProductSchema = Depends(order_by_id),
#         # current_order = Depends(get_current_active_order),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ):
#     return await update_order_db(
#         session=session,
#         order=order,
#         order_update=order_update,
#     )
#
#
# @router.patch(
#     "/{order_id}",
#     response_model=ProductResponseSchema
# )
# async def update_order_partial(
#         order_update: ProductUpdatePartialSchema,
#         order: ProductSchema = Depends(order_by_id),
#         # current_order=Depends(get_current_active_order),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ):
#     return await update_order_db(
#         session=session,
#         order=order,
#         order_update=order_update,
#         partial=True
#     )
#
#
# @router.delete("/{order_id}/", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_order(
#         order: ProductSchema = Depends(order_by_id),
#         # current_order=Depends(get_current_active_order),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ) -> None:
#     await delete_order_db(order=order, session=session)
