import asyncpg
from sqlalchemy import inspect, insert
from faker import Faker
import random

from cosmetic_app.models import User, Product, Profile, Category, Brand
from .base_class import Base
from .db_helper import db_helper


async def connect_create_if_exist(user, password, db_name):
    sys_conn = await asyncpg.connect(user=user, password=password, host="127.0.0.1")
    try:
        await asyncpg.connect(user=user, password=password, host="127.0.0.1", database=db_name)
    except asyncpg.InvalidCatalogNameError:
        await sys_conn.execute(
            f"CREATE DATABASE {db_name} OWNER {user}"
        )
    finally:
        await sys_conn.close()


async def init_db():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        tables = await conn.run_sync(
            lambda sys_conn: inspect(sys_conn).get_table_names()
        )
        if not tables:
            await conn.run_sync(Base.metadata.create_all)

    await add_test_user()
    await add_test_profile()
    await add_test_product()
    await add_test_category()
    await add_test_brand()


from faker.providers.person.ru_RU import Provider
fake = Faker("ru_RU")


async def add_test_user():
    async with db_helper.engine.connect() as conn:
        for i in range(1, 10):
            values_data = {
                "email": fake.email(),
                "password": "string",
                "is_active": True,
                "profile": i
            }
            await conn.execute(insert(User).values(values_data))
            await conn.flush()
            await conn.commit()


async def add_test_profile():
    async with db_helper.engine.connect() as conn:
        for i in range(10):
            values_data = {
                "nickname": fake.email(),
                "phone": fake.phone_number(),
                "photo": "string",
                "first_name": Provider.first_name,
                "last_name": Provider.last_name,
                "user_id": i,
                "user": User
            }
            await conn.execute(insert(Profile).values(values_data))


async def add_test_product():
    async with db_helper.engine.connect() as conn:
        for _ in range(20):
            values_data = {
                "title": random.choice(["Eyeliner", "Lipstick", "Blush", "Mascara", "Eyeshadow"]),
                "article_number": f"#{random.randint(200, 300)}",
                "price": random.randint(40, 210),
                "image": "string",
                "brand_id": random.randint(1, 3),
                "brand": Brand,
                "category_id": random.randint(1, 3),
                "categories": Category,
            }
            await conn.execute(insert(Product).values(values_data))

async def add_test_category():
    async with db_helper.engine.connect() as conn:
        for i in ["Green", "Blue", "White"]:
            values_data = {
                "title": i,
            }
            await conn.execute(insert(Category).values(values_data))


async def add_test_brand():
    async with db_helper.engine.connect() as conn:
        for i in ["RevitaYouth", "SereneSilk", "PureHarmony"]:
            values_data = {
                "title": i,
            }
            await conn.execute(insert(Brand).values(values_data))


