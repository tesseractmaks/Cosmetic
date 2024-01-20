import datetime
import json
import random
import uuid

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy import insert, select

from cosmetic_app.schemas import UserSchema, UserUpdatePartialSchema, TagUpdatePartialSchema
from ..conftest import client
from cosmetic_app.models import UserModel, Tag
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
async def test_read_tags_db():
    async with async_session_maker() as session:
        stmt = select(Tag)
        result: AsyncResult = await session.execute(stmt)
        users = result.unique().scalars().all()
        assert len(list(users)) > 1


@pytest.mark.anyio
async def test_read_tag_by_id_db():
    async with async_session_maker() as session:
        stmt = select(Tag.id)
        result: AsyncResult = await session.execute(stmt)
        tag_id = result.unique().scalar()
        tag = await session.get(Tag, tag_id)
        assert tag.__dict__["id"] == tag_id


@pytest.mark.anyio
async def test_create_tag_db():
    async with async_session_maker() as session:
        tag_in = {
            "title": "Для губ"
            }
        tag = Tag(**tag_in)
        session.add(tag)
        await session.commit()
        assert tag.title == "Для губ"


@pytest.mark.anyio
async def test_read_user_by_tag_db():
    async with async_session_maker() as session:
        stmt = select(Tag).where(Tag.title == "Для губ")
        result: AsyncResult = await session.execute(stmt)
        tag = result.scalar()
        assert tag.__dict__["title"] == "Для губ"


@pytest.mark.anyio
async def test_update_tag_db():
    tag_update = {
        "title": "Для лица"
    }
    tag = {
        "title": "Для губ"
    }
    tag_update = TagUpdatePartialSchema(**tag_update)
    tag = Tag(**tag)
    for name, value in tag_update.model_dump(exclude_unset=True).items():
        setattr(tag, name, value)
    assert tag.title == "Для лица"


@pytest.mark.anyio
async def test_delete_tag():
    async with async_session_maker() as session:
        stmt = select(Tag.id)
        result: AsyncResult = await session.execute(stmt)
        tag_id = result.unique().scalar()
        tag_get = await session.get(Tag, tag_id)
        await session.delete(tag_get)
        await session.commit()
        tag_empty = await session.get(Tag, tag_id)
        assert not tag_empty

