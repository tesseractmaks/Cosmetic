import datetime
import json
import random
import uuid

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy import insert, select

from cosmetic_app.schemas import UserSchema, UserUpdatePartialSchema, TagUpdatePartialSchema, \
    CategoryUpdatePartialSchema
from ..conftest import client
from cosmetic_app.models import UserModel, Tag, Category
from sqlalchemy.orm import selectinload, joinedload, strategy_options
from ..conftest import async_session_maker


@pytest.mark.anyio
async def test_read_categories_db():
    async with async_session_maker() as session:
        stmt = select(Category)
        result: AsyncResult = await session.execute(stmt)
        categories = result.unique().scalars().all()
        assert len(list(categories)) > 1


@pytest.mark.anyio
async def test_read_category_by_id_db():
    async with async_session_maker() as session:
        stmt = select(Category.id)
        result: AsyncResult = await session.execute(stmt)
        category_id = result.unique().scalar()
        category = await session.get(Category, category_id)
        assert category.__dict__["id"] == category_id


@pytest.mark.anyio
async def test_create_category_db():
    async with async_session_maker() as session:
        category_in = {
            "title": "Для губ"
            }
        category = Category(**category_in)
        session.add(category)
        await session.commit()
        assert category.title == "Для губ"


@pytest.mark.anyio
async def test_update_category_db():
    category_update = {
        "title": "Для лица"
    }
    category = {
        "title": "Для губ"
    }
    category_update = CategoryUpdatePartialSchema(**category_update)
    category = Category(**category)
    for name, value in category_update.model_dump(exclude_unset=True).items():
        setattr(category, name, value)
    assert category.title == "Для лица"


@pytest.mark.anyio
async def test_delete_category():
    async with async_session_maker() as session:
        stmt = select(Category.id)
        result: AsyncResult = await session.execute(stmt)
        category_id = result.unique().scalar()
        category_get = await session.get(Category, category_id)
        await session.delete(category_get)
        await session.commit()
        category_empty = await session.get(Category, category_id)
        assert not category_empty

