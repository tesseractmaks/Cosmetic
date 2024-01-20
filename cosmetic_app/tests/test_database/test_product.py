import datetime
import json
import random
import uuid

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy import insert, select

from cosmetic_app.schemas import UserSchema, UserUpdatePartialSchema, ProductUpdatePartialSchema
from ..conftest import client
from cosmetic_app.models import UserModel, Product
from sqlalchemy.orm import selectinload, joinedload, strategy_options
from ..conftest import async_session_maker

product_in = {
            "link_detail": "17-kombinezon-bona-fide.html",
            "image": "../uploads/posts/2021-05/1621247418_2.jpg",
            "title": "Ginseng Milk and Tonic Duo",
            "price": random.randint(600, 2710),
            "label": random.choice(["new", ""]),
            "num_goods": "goods_17",
            "data_goods": "17|Ginseng Milk and Tonic Duo|2400|-|http://raro.prowebmarket.ru/ptoduct/17-kombinezon-bona-fide.html|"
        }


@pytest.mark.anyio
async def test_read_products_db():
    async with async_session_maker() as session:
        stmt = select(Product)
        result: AsyncResult = await session.execute(stmt)
        products = result.unique().scalars().all()
        assert len(list(products)) > 1


@pytest.mark.anyio
async def test_read_product_by_id_db():
    async with async_session_maker() as session:
        stmt = select(Product.id)
        result: AsyncResult = await session.execute(stmt)
        product_id = result.unique().scalar()
        product = await session.get(Product, product_id)
        assert product.__dict__["id"] == product_id


@pytest.mark.anyio
async def test_create_product_db():
    async with async_session_maker() as session:
        product = Product(**product_in)
        session.add(product)
        await session.commit()
        assert product.num_goods == "goods_17"


@pytest.mark.anyio
async def test_update_product_db():
    product_update = {
        "num_goods": "goods_177"
    }
    product_update = ProductUpdatePartialSchema(**product_update)
    product = Product(**product_in)
    for name, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, name, value)
    assert product.num_goods == "goods_177"


@pytest.mark.anyio
async def test_delete_product():
    async with async_session_maker() as session:
        stmt = select(Product.id)
        result: AsyncResult = await session.execute(stmt)
        product_id = result.unique().scalar()
        product_get = await session.get(Product, product_id)
        await session.delete(product_get)
        await session.commit()
        product_empty = await session.get(Product, product_id)
        assert not product_empty
