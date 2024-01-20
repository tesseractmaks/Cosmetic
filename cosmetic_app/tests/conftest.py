from typing import AsyncGenerator, Any
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.pool import NullPool
import pytest_asyncio
from jose import jwt
from datetime import datetime, timedelta

from cosmetic_app.core import settings
from cosmetic_app.db import Base
from cosmetic_app.main import app
from cosmetic_app.db import db_helper
from cosmetic_app.models import UserModel


SECRET_KEY = "$2b$12$cZmHQ5w9KXng0Q/XWCn4ReMfPh5JqwzpI6oaEY/XS1ERCHSbJceC."
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
REFRESH_TOKEN_EXPIRE_MINUTES = 20
engine_test = create_async_engine(settings.db_url, poolclass=NullPool)
async_session_maker = async_sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[db_helper.scoped_session_dependency] = override_get_async_session


@pytest_asyncio.fixture(autouse=True, scope="session")
async def init_test_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/api/v1/", follow_redirects=True) as ac:
        yield ac


@pytest.fixture
def anyio_backend():
    return 'asyncio'


@pytest_asyncio.fixture()
async def create_user(
        client: AsyncClient
):
    async with async_session_maker() as session:
        values_data = {
            "email": "email@mail.com",
            "password": "qwerty",
            "is_active": True,
            "created_at": str(datetime.utcnow()),
        }
        user = UserModel(**values_data)
        session.add(user)
        await session.commit()


@pytest_asyncio.fixture
async def create_token(
        client: AsyncClient,
        data={"sub": "one@mail.ru1"},
):
    tokens = {
        "access_expires": timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        "refresh_expires": timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    }

    access_to_encode = data.copy()
    refresh_to_encode = data.copy()

    expire_access = datetime.utcnow() + tokens["access_expires"]
    expire_refresh = datetime.utcnow() + tokens["refresh_expires"]

    access_to_encode.update({"exp": expire_access})
    jwt_access = jwt.encode(access_to_encode, SECRET_KEY, algorithm=ALGORITHM)

    refresh_to_encode.update({"exp": expire_refresh})
    jwt_refresh = jwt.encode(refresh_to_encode, SECRET_KEY, algorithm=ALGORITHM)
    values_data = {
        "access_token": "string",
        "token_type": "string"
    }
    # response: Response = await client.post("http://127.0.0.1:8000/token", json=values_data)
    # response.delete_cookie(key="refresh_token", httponly=True)
    # response.set_cookie(key="refresh_token", value=f"Bearer {jwt_refresh}", httponly=True)
    return jwt_refresh

# from pytest_httpx import HTTPXMock
# import httpx
# @pytest_asyncio.fixture
# async def set_cookie(httpx_mock: HTTPXMock) -> None:
#     """
#     Send a request including a cookie, using a `Cookies` instance.
#     """
#
#     url = "http://127.0.0.1:8000/api/v1/"
#     cookies = httpx.Cookies()
#     cookies["test_refresh_token"] = "refresh_token"
#     httpx_mock.add_response(headers={"set-cookie": "test_refresh_token=refresh_token"})
#
#     # client = httpx.Client(transport=httpx.MockTransport(get_and_set_cookies))
#     client.cookies = cookies
#     response = await client.get(url)
#
#     # assert response.status_code == 200
#     # assert response.json() == {"cookies": "test_refresh_token=refresh_token"}
#     return response.json()




# @pytest_asyncio.fixture
# async def get_cookie(httpx_mock: HTTPXMock):
#     httpx_mock.add_response(headers={"set-cookie": "test_refresh_token=Bearer refresh_token"})
#     async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/api/v1/", follow_redirects=True) as client:
#         response = await client.get("http://127.0.0.1:8000/api/v1/")
#         assert dict(response.cookies) == {"test_refresh_token": "Bearer refresh_token"}
#         return dict(response.cookies)




# @pytest_asyncio.fixture(scope="session")
# async def set_cookie(
#         client: AsyncClient,
# ):
#     values_data = {
#         "access_token": "string",
#         "token_type": "string"
#     }
#     await client.post("http://127.0.0.1:8000/token", json=values_data)
#     # response.delete_cookie(key="refresh_token", httponly=True)
#     # response.set_cookie(key="test_refresh_token", value="Bearer refresh_token", httponly=True)
#
#     client.cookies.set(name="test_refresh_token", value="Bearer refresh_token", domain="http://127.0.0.1:8000",path="/token")





