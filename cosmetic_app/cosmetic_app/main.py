from redis import asyncio as aioredis
import asyncio
from hypercorn.asyncio import serve
from hypercorn.config import Config


from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from contextlib import asynccontextmanager
from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from cosmetic_app.api import router as router_v1
# from api import router_token
from cosmetic_app.core import settings
from cosmetic_app.db import connect_create_if_exist, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = await aioredis.from_url("redis://127.0.0.1:6379", encoding="utf-8")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    await connect_create_if_exist(settings.db_username, settings.db_password, settings.db_name)
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


# app.mount("/img", StaticFiles(directory="frontend", html=True), name="img")
app.include_router(
    router=router_v1,
    prefix=settings.api_v1_prefix
)

# app.include_router(
#     router=router_token
# )

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5050",
    "http://127.0.0.1:5055",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config = Config()
config.bind = ["127.0.0.1:8000"]
sockets = config.create_sockets()
sock = sockets.insecure_sockets[0]

asyncio.run(serve(app, config))







