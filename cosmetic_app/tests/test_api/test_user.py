import datetime
import random

import pytest
from httpx import AsyncClient
from jsonpickle import json
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy import insert, select
from datetime import datetime

from ..conftest import client
from cosmetic_app.models import UserModel, Category
from sqlalchemy.orm import selectinload, joinedload, strategy_options
from ..conftest import async_session_maker
from faker import Faker
from pytest_schema import schema
from typing import Type, Any, Annotated

fake = Faker("ru_RU")
from pydantic import BaseModel, ConfigDict, Field


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: str
    password: str
    is_active: bool

# UserSchema = {
#     "email": str,
#     "password": str,
#     "is_active": bool,
#     "created_at": datetime,
#     "updated_at": datetime
#               }


def assert_schema(response, model: Type[BaseModel]):
    body = response.json()
    if isinstance(body, list):
        for item in body:
            model.model_validate(item, strict=True)
    else:
        model.model_validate(body, strict=True)
    return True


@pytest.mark.anyio
async def test_create_user(
        client: AsyncClient,
):
    values_data = {
        "email": fake.email(),
        "password": fake.nic_handle(),
        "is_active": True,
        "created_at": str(datetime.utcnow()),
    }
    response = await client.post("users/", json=values_data)
    assert assert_schema(response, UserSchema)
    assert response.status_code == 201


@pytest.mark.anyio
@pytest.mark.parametrize("route", ["users/"])
async def test_read_users(client: AsyncClient, route):
    response = await client.get(route)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_read_user_by_id(client: AsyncClient):
    async with async_session_maker() as session:
        query = select(UserModel.id).limit(1)
        result = await session.execute(query)
        user_id = result.scalar()
        response = await client.get(f"users/{str(user_id)}/")
        assert response.status_code == 200


@pytest.mark.anyio
async def test_update_user_partial(client: AsyncClient):
    async with async_session_maker() as session:
        values_data = {
            "email": "one55@mail.ru"
        }
        query = select(UserModel.id).limit(1)
        result = await session.execute(query)
        user_id = result.scalar()

        response = await client.patch(f"users/{str(user_id)}", json=values_data)
        assert response.status_code == 200


@pytest.mark.anyio
async def test_delete_user(client: AsyncClient):
    async with async_session_maker() as session:
        query = select(UserModel.id).limit(1)
        result = await session.execute(query)
        user_id = result.scalar()
        # await client.delete(f'http://127.0.0.1:8000/api/v1/users/{str(user_id)}/')
        response = await client.delete(f"users/{str(user_id)}/")
        assert response.status_code == 204
