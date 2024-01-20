import asyncio
import datetime
import json
import random
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, Result, update
from faker import Faker
from fastapi import Depends
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncResult

from cosmetic_app.models.gist import values_data
from cosmetic_app.models.user import UserModel
from cosmetic_app.models.category import Category
from cosmetic_app.models.product import Product

from cosmetic_app.models.associate_tag_product import AssociateTagProduct

from cosmetic_app.db.db_helper import db_helper
from cosmetic_app.schemas import ProductSchema

fake = Faker("ru_RU")


async def add_test_user(session):

    for i in range(1, 20):
        #     user = UserModel(
        #         email=fake.email(),
        #         password=fake.nic_handle(),
        #         is_active=True
        #     )
        #
        #     session.add(user)
        #
        # #
        #     #
        # await session.commit()

        values_data = {
            "email": "one@mail.ru1",
            "password": fake.nic_handle(),
            "is_active": True,
        }
        await session.execute(insert(UserModel).values(values_data))
    await session.commit()


# async def add_test_profile(session):
#     query = select(UserModel.id)
#     users = await session.execute(query)
#
#     for i in users.scalars().all():
#         values_data = {
#             "nickname": fake.user_name(),
#             "phone": fake.phone_number(),
#             "photo": fake.image_url(),
#             "first_name": fake.first_name_female(),
#             "last_name": fake.last_name_female(),
#             "user_id": i,
#             "created_at": datetime.datetime.utcnow(),
#             "updated_at": datetime.datetime.utcnow()
#         }
#         await session.execute(insert(Profile).values(values_data))
#     await session.commit()


async def add_test_category(session):
    for i in ["Для губ", "Макияж", "Туалетная вода", "Уход за кожей", "Для ногтей", "Уход за волосами", "Новые"]:
        values_cat = {
            "title": i,
        }
        new_cat = Category(**values_cat)
        session.add(new_cat)
    await session.commit()


async def add_test_tag(session):
    from cosmetic_app.models.tags import Tag
    for i in ["Для губ", "Для лица", "Для ресниц", "Макияж"]:
        values_tag = {
            "title": i,
        }

        new_tag = Tag(**values_tag)

        session.add(new_tag)
    await session.commit()


async def add_test_product(session):
    for value in values_data:
        new_product = Product(**value)
        session.add(new_product)
    await session.commit()


async def add_test_tag_category(session):

    from cosmetic_app.models.tags import Tag

    query_tag = select(Tag)
    res: AsyncResult = await session.execute(query_tag)
    tag_raw = res.unique().scalars().all()

    query_cat = select(Category)
    res: AsyncResult = await session.execute(query_cat)
    category_raw = res.unique().scalars().all()

    query = select(Product)
    result = await session.execute(query)
    products_raw = result.unique().scalars().all()

    for product in list(products_raw):
        product = await session.scalar(select(Product).where(Product.id == product.id).options(selectinload(Product.tags_assoc)) #.joinedload(AssociateTagProduct.tag)
            )

        product.tags_assoc.append(random.choice(list(tag_raw)))
        # product.tags_assoc.extend(list(tag_raw))

    for product in list(products_raw):
        product = await session.scalar(
            select(Product).where(Product.id == product.id).options(selectinload(Product.category_assoc))
            )
        product.category_assoc.append(random.choice(list(category_raw)))
        # product.category_assoc.extend(list(category_raw))

    await session.commit()


async def add_test_order(session):
    from cosmetic_app.models.order import Order
    values_data = {
        "title": "one",
    }
    # for value in values_data:
    new_order = Order(**values_data)
    session.add(new_order)
    await session.commit()


async def add_test_order_products(session):
    from cosmetic_app.models.order import Order
    from cosmetic_app.models.associate_order_product import AssociateOrderProduct

    query = select(Order)
    result = await session.execute(query)
    order = result.unique().scalar()

    query = select(Product)
    result = await session.execute(query)
    product = result.unique().scalar()
    # Order.products_assoc.unit_price = product.price

    order = await session.scalar(select(Order).where(Order.id == order.id).options(selectinload(Order.products_assoc)) #.joinedload(AssociateTagProduct.tag)
            )
    order.products_assoc.append(product)
    await session.commit()

    query = select(AssociateOrderProduct).where(AssociateOrderProduct.order_id == Order.id)
    result = await session.execute(query)
    ass_order = result.unique().scalar()

    ass_order.order_assoc.title = "two"

    ass_order.image = product.image
    ass_order.unit_price = product.price
    ass_order.quantity = 3
    ass_order.total_price = product.price * 3

    print(ass_order.order_assoc.id, ass_order.order_id, "-------------")


    # for i in order.products_assoc:
    #     i.unit_price = product.price
    #     i.quantity = 2
    #     i.image = product.image
    #     i.total_price = product.price * 2
    # order.products_assoc.append(product)

    await session.commit()


    # new_order.unit_price = product.price
    # session.add(new_order)

    # for i in order.products_assoc:
    #     i.unit_price = product.price
    #     i.quantity = 2
    #     i.image = product.image
    #     i.total_price = product.price * 2
    # order.products_assoc.append(product)


async def add_test_data():
    async with db_helper.session_factory() as session:
        await add_test_user(session)
        await add_test_product(session)
        await add_test_category(session)
        await add_test_tag(session)
        await add_test_tag_category(session)
        await add_test_order(session)
        await add_test_order_products(session)


