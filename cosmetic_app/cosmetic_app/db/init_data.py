import asyncio
import datetime
import random

from sqlalchemy import insert, select
from faker import Faker

from cosmetic_app.models.user import UserModel
from cosmetic_app.models.profile import Profile
from cosmetic_app.models.category import Category
from cosmetic_app.models.product import Product
from .db_helper import db_helper

fake = Faker("ru_RU")


async def add_test_user():
    async with db_helper.engine.begin() as conn:
        for i in range(1, 20):
            values_data = {
                "email": fake.email(),
                "password": fake.nic_handle(),
                "is_active": True,
            }
            await conn.execute(insert(UserModel).values(values_data))


async def add_test_profile():
    async with db_helper.engine.begin() as conn:
        query = select(UserModel.id)
        users = await conn.execute(query)

        for i in users.scalars().all():
            values_data = {
                "nickname": fake.user_name(),
                "phone": fake.phone_number(),
                "photo":  fake.image_url(),
                "first_name": fake.first_name_female(),
                "last_name": fake.last_name_female(),
                "user_id": i,
                "created_at": datetime.datetime.utcnow(),
                "updated_at": datetime.datetime.utcnow()
            }
            await conn.execute(insert(Profile).values(values_data))
        # await conn.commit()


async def add_test_category():
    async with db_helper.engine.begin() as conn:
        for i in ["Green", "Blue", "White"]:
            values_data = {
                "title": i,
            }
            await conn.execute(insert(Category).values(values_data))
        # await conn.commit()


async def add_test_brand():
    await asyncio.sleep(0.1)
    from cosmetic_app.models.brand import Brand

    async with db_helper.engine.begin() as conn:
        for i in ["RevitaYouth", "SereneSilk", "PureHarmony"]:
            values_data = {
                "title": i,
            }
            await conn.execute(insert(Brand).values(values_data))
        # await conn.commit()


async def add_test_product():
    await asyncio.sleep(0.1)
    from cosmetic_app.models.brand import Brand
    async with db_helper.engine.begin() as conn:
        query = select(Category.id)
        category_obj = await conn.execute(query)
        category = category_obj.scalars().all()

        query = select(Brand.id)
        brand_obj = await conn.execute(query)
        brands = brand_obj.scalars().all()

        for _ in range(3):
            values_data = {
                "title": random.choice(["Eyeliner", "Lipstick", "Blush", "Mascara", "Eyeshadow"]),
                "article_number": f"#{random.randint(200, 300)}",
                "price": random.randint(40, 210),
                "image": fake.image_url(),
                "brand_id": random.choice(brands),
                "category_id": random.choice(category),
                # "categories": Category,
            }
            await conn.execute(insert(Product).values(values_data))
        # await conn.commit()


async def add_test_data():
    await add_test_user()
    await add_test_profile()
    await add_test_category()
    await add_test_brand()
    await add_test_product()