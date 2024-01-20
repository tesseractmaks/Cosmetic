import datetime
import json
import random
import uuid

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy import insert, select

from cosmetic_app.schemas import UserSchema, UserUpdatePartialSchema
from ..conftest import client
from cosmetic_app.models import UserModel
from sqlalchemy.orm import selectinload, joinedload, strategy_options
from ..conftest import async_session_maker


async def create_user(
        client: AsyncClient
):
    async with async_session_maker() as session:
        values_data = {
            "email": "email@mail.com",
            "password": "qwerty",
            "is_active": True,
            "created_at": str(datetime.datetime.utcnow()),
        }
        user = UserModel(**values_data)
        session.add(user)
        await session.commit()


@pytest.mark.anyio
async def test_read_users_db():
    async with async_session_maker() as session:
        stmt = select(UserModel).order_by(UserModel.id)
        result: AsyncResult = await session.execute(stmt)
        users = result.unique().scalars().all()
        assert len(list(users)) > 1


@pytest.mark.anyio
async def test_read_user_by_id_db():
    async with async_session_maker() as session:
        stmt = select(UserModel.id)
        result: AsyncResult = await session.execute(stmt)
        user_id = result.unique().scalar()
        user = await session.get(UserModel, user_id)
        assert user.__dict__["id"] == user_id


@pytest.mark.anyio
async def test_create_user_db():
    async with async_session_maker() as session:
        user_in = {
            "email": "email@mail.com",
            "password": "qwerty",
            "is_active": True
            }
        user = UserModel(**user_in)
        session.add(user)
        await session.commit()
        assert user.email == "email@mail.com"


@pytest.mark.anyio
async def test_read_user_by_username_db():
    async with async_session_maker() as session:
        stmt = select(UserModel).where(UserModel.email == "one@mail.ru1")
        result: AsyncResult = await session.execute(stmt)
        user = result.scalar()
        assert user.__dict__["email"] == "one@mail.ru1"


@pytest.mark.anyio
async def test_update_user_db():
    user_update = {
        "email": "one6@mail.ru"
        }
    user = {
        "email": "one5@mail.ru",
        "password": "qwerty",
        "is_active": True,
        "created_at": str(datetime.datetime.utcnow())
    }
    user_update = UserUpdatePartialSchema(**user_update)
    user = UserSchema(**user)
    for name, value in user_update.model_dump(exclude_unset=True).items():
        setattr(user, name, value)
    assert user.email == "one6@mail.ru"


@pytest.mark.anyio
async def test_delete_user():
    async with async_session_maker() as session:
        stmt = select(UserModel.id)
        result: AsyncResult = await session.execute(stmt)
        user_id = result.unique().scalar()
        user_get = await session.get(UserModel, user_id)
        await session.delete(user_get)
        await session.commit()
        user_empty = await session.get(UserModel, user_id)
        assert not user_empty

