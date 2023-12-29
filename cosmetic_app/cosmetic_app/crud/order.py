import uuid
from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from cosmetic_app.models.product import Product
from cosmetic_app.models.order import Order
from cosmetic_app.models.associate_order_product import AssociateOrderProduct
from cosmetic_app.schemas import (
    OrderSchema,
    OrderUpdateSchema,
    OrderCreateSchema,
    OrderResponseSchema,
    OrderUpdatePartialSchema
)
from cosmetic_app.schemas import (
    ProductSchema,
    ProductUpdateSchema,
    ProductCreateSchema,
    ProductUpdatePartialSchema,
)


async def read_order_db(session: AsyncSession):
    query = select(AssociateOrderProduct).options(selectinload(AssociateOrderProduct.order_assoc))
    result: AsyncResult = await session.execute(query)
    order = result.unique().scalar()
    return order.order_assoc.title

# async def read_order_db(session: AsyncSession) -> list[OrderSchema]:
#     query = select(AssociateOrderProduct).options(selectinload(Product.order_assoc))
#     result: AsyncResult = await session.execute(query)
#     orders = result.unique().scalar()
#     return list(orders)


# async def read_order_by_id_db(session: AsyncSession, order_id: uuid.uuid4) -> ProductSchema | None:
#     return await session.get(Product,order_id)


async def create_order_db(
        session: AsyncSession,
        order_in: OrderCreateSchema,
) -> Order:
    order_obj =order_in.model_dump()
    order = Order(**order_obj)
    session.add(order)
    await session.commit()
    return order


# async def update_product_db(
#     session: AsyncSession,
#         product: ProductSchema,
#         product_update: ProductUpdateSchema | ProductUpdatePartialSchema,
#         partial: bool = False
# ) -> ProductSchema:
#     for name, value in product_update.model_dump(exclude_unset=partial).items():
#         setattr(product, name, value)
#     await session.commit()
#     return product
#
#
# async def delete_product_db(session: AsyncSession, product: ProductSchema) -> None:
#     await session.delete(product)
#     await session.commit()