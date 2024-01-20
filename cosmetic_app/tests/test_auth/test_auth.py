from typing import AsyncGenerator, Annotated
import time
from fastapi import Depends, HTTPException, status, Cookie, Response
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from cosmetic_app.db.db_helper import db_helper
import pytest_asyncio
from cosmetic_app.models import UserModel
from cosmetic_app.schemas import UserSchema
from ..conftest import async_session_maker, create_token, client


from sqlalchemy.ext.asyncio import AsyncResult
import pytest
from cosmetic_app.main import app
from httpx import AsyncClient
from ..conftest import client
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy import insert, select

SECRET_KEY = "$2b$12$cZmHQ5w9KXng0Q/XWCn4ReMfPh5JqwzpI6oaEY/XS1ERCHSbJceC."
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
REFRESH_TOKEN_EXPIRE_MINUTES = 20

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
test_refresh = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJvbmVAbWFpbC5ydTEiLCJleHAiOjE3MDUyMjgxNjJ9.zFTCi1nlYJEJvHYg5XV7kpK1Nd_Z3dgaOlslxWStpZI"


async def read_user_by_username_db(username):
    async with async_session_maker() as session:
        stmt = select(UserModel).where(UserModel.email == username)
        result: AsyncResult = await session.execute(stmt)
        user = result.scalar()
        return user


@pytest.mark.anyio
async def test_authenticate_user(
) -> UserSchema | bool:
    user = await read_user_by_username_db(username="one@mail.ru1")
    assert user


@pytest.mark.anyio
async def test_get_current_active_user(username: UserSchema = "one@mail.ru1"):
    current_user = await read_user_by_username_db(username=username)
    assert current_user.is_active


@pytest.mark.anyio
async def test_verify_password():
    hashed_password = pwd_context.hash("qwerty")
    assert pwd_context.verify("qwerty", hashed_password)



