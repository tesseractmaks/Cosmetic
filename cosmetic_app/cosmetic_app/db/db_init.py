import asyncpg
from sqlalchemy import inspect, insert

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
        await add_test_data(conn)

async def add_test_data(conn):
    values_data = {
        "username": "one_user",
        "permissions": [1, 2],
        "is_active": True,
        "groups": [2, 3],
    }
    await conn.execute(insert(UserModel).values(values_data))

