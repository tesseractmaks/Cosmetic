import datetime
import random

import pytest
from httpx import AsyncClient
from jsonpickle import json
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy import insert, select
from datetime import datetime

from ..conftest import client
from cosmetic_app.models import Product
from sqlalchemy.orm import selectinload, joinedload, strategy_options
from ..conftest import async_session_maker
from faker import Faker
from pytest_schema import schema
from typing import Type, Any, Annotated

fake = Faker("ru_RU")
from pydantic import BaseModel, ConfigDict


class ProductSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    link_detail: str
    price: int
    image: str
    label: str
    num_goods: str
    data_goods: str
    created_at: str
    updated_at: str | None = None


class TagSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str


class CategorySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str


class ProductResponseSchema(ProductSchema):
    model_config = ConfigDict(from_attributes=True)
    category_assoc: list[CategorySchema]
    tags_assoc: list[TagSchema]


def assert_schema(response, model: Type[BaseModel]):
    body = response.json()
    if isinstance(body, list):
        for item in body:
            model.model_validate(item, strict=True)
    else:
        model.model_validate(body, strict=True)
    return True


@pytest.mark.anyio
async def test_create_product(
        client: AsyncClient,
):
    values_data = {
        "title": "Dolce &amp; Gabbana Light Blue",
        "price": random.randint(600, 2710),
        "image": "../uploads/posts/2021-05/1621438635_product-961805-0-productpagedesktop.jpg",
        "label": random.choice(["new", "", ""]),
        "link_detail": "26-shorty-triplex-red.html",
        "num_goods": "goods_26",
        "created_at": str(datetime.utcnow()),
        "data_goods": "26|Dolce & Gabbana Light Blue|1772,25|-|http://raro.prowebmarket.ru/ptoduct/26-shorty-triplex-red.html|"
    }
    response = await client.post("products/", json=values_data)
    assert assert_schema(response, ProductSchema)
    assert response.status_code == 201


@pytest.mark.anyio
@pytest.mark.parametrize("route", ["products/"])
async def test_products(client: AsyncClient, route):
    response = await client.get(route)
    assert response.status_code == 200


# @pytest.mark.anyio
# async def test_read_product_by_id(client: AsyncClient):
#     async with async_session_maker() as session:
#         query = select(Product.id).limit(1)
#         result = await session.execute(query)
#         product_id = result.scalar()
#         response = await client.get(f"products/{str(product_id)}/")
#         # assert assert_schema(response, ProductResponseSchema)
#         assert response.status_code == 200


@pytest.mark.anyio
async def test_update_product_partial(client: AsyncClient):
    async with async_session_maker() as session:
        values_data = {
            "title": "Для face"
        }
        query = select(Product.id).limit(1)
        result = await session.execute(query)
        product_id = result.scalar()
        response = await client.patch(f"products/{str(product_id)}", json=values_data)
        assert response.status_code == 200


@pytest.mark.anyio
async def test_delete_tag(client: AsyncClient):
    async with async_session_maker() as session:
        query = select(Product.id).limit(1)
        result = await session.execute(query)
        product_id = result.scalar()
        response = await client.delete(f"products/{str(product_id)}/")
        assert response.status_code == 204
