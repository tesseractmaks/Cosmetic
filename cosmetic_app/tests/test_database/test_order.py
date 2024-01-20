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
from cosmetic_app.models import UserModel, Product, AssociateOrderProduct, Order
from sqlalchemy.orm import selectinload, joinedload, strategy_options
from ..conftest import async_session_maker

order_in = {
            "link_detail": "17-kombinezon-bona-fide.html",
            "image": "../uploads/posts/2021-05/1621247418_2.jpg",
            "title": "Ginseng Milk and Tonic Duo",
            "price": random.randint(600, 2710),
            "label": random.choice(["new", ""]),
            "num_goods": "goods_17",
            "data_goods": "17|Ginseng Milk and Tonic Duo|2400|-|http://raro.prowebmarket.ru/ptoduct/17-kombinezon-bona-fide.html|"
        }


@pytest.mark.anyio
async def test_read_order_db():
    async with async_session_maker() as session:
        query = select(AssociateOrderProduct).options(selectinload(AssociateOrderProduct.order_assoc))
        result: AsyncResult = await session.execute(query)
        order = result.unique().scalar()
        assert order.order_assoc.title == order.title


@pytest.mark.anyio
async def test_create_order_db():
    async with async_session_maker() as session:
        order_obj = order_in.model_dump()
        order = Order(**order_obj)
        session.add(order)
        assert order == ""

