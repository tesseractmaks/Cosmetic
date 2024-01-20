import datetime
import random

import pytest
from httpx import AsyncClient
from jsonpickle import json
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy import insert, select
from datetime import datetime

from ..conftest import client
from cosmetic_app.models import UserModel, Category, Tag
from sqlalchemy.orm import selectinload, joinedload, strategy_options
from ..conftest import async_session_maker
from faker import Faker
from pytest_schema import schema
from typing import Type, Any, Annotated

fake = Faker("ru_RU")
from pydantic import BaseModel, ConfigDict


class TagSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str


def assert_schema(response, model: Type[BaseModel]):
    body = response.json()
    if isinstance(body, list):
        for item in body:
            model.model_validate(item, strict=True)
    else:
        model.model_validate(body, strict=True)
    return True


@pytest.mark.anyio
async def test_create_tag(
        client: AsyncClient,
):
    values_data = {
        "title": "Для губ"
    }
    response = await client.post("tags/", json=values_data)
    assert assert_schema(response, TagSchema)
    assert response.status_code == 201


@pytest.mark.anyio
@pytest.mark.parametrize("route", ["tags/"])
async def test_tags(client: AsyncClient, route):
    response = await client.get(route)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_read_tag_by_id(client: AsyncClient):
    async with async_session_maker() as session:
        query = select(Tag.id).limit(1)
        result = await session.execute(query)
        tag_id = result.scalar()
        response = await client.get(f"tags/{str(tag_id)}/")
        assert response.status_code == 200


@pytest.mark.anyio
async def test_update_tag_partial(client: AsyncClient):
    async with async_session_maker() as session:
        values_data = {
            "title": "Для face"
        }
        query = select(Tag.id).limit(1)
        result = await session.execute(query)
        tag_id = result.scalar()
        response = await client.patch(f"tags/{str(tag_id)}", json=values_data)
        assert response.status_code == 200


@pytest.mark.anyio
async def test_delete_tag(client: AsyncClient):
    async with async_session_maker() as session:
        query = select(Tag.id).limit(1)
        result = await session.execute(query)
        tag_id = result.scalar()
        # await client.delete(f'http://127.0.0.1:8000/api/v1/users/{str(user_id)}/')
        response = await client.delete(f"tags/{str(tag_id)}/")
        assert response.status_code == 204
