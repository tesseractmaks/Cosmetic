import datetime


from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
# from passlib.context import CryptContext

from cosmetic_app.crud.user import read_user_db, update_user_db, create_user_db, delete_user_db
from cosmetic_app.db.db_helper import db_helper
from cosmetic_app.schemas import (
    UserSchema,
    UserCreateSchema,
    UserUpdateSchema,
    UserUpdatePartialSchema,
    UserResponseSchema
)
from .depends_endps import user_by_id

# from cosmetic_app.auth import get_current_active_user


import redis

from kafka import KafkaProducer, KafkaConsumer
import pickle
router = APIRouter(tags=["User"])


def redis_cache(res_raw=None):
    red = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True, encoding="utf-8")
    # red.flushall()
    # red.lpush("users", *[res_raw])

    x = red.lrange('users', 0, -1)
    return x


async def get_consumer():
    consumer = KafkaConsumer(
        "users",
        auto_offset_reset="earliest",
        bootstrap_servers=["127.0.0.1:9092"],
        api_version=(0, 10),
        max_poll_records=1000,
        # consumer_timeout_ms=100,


    )

    for records in consumer:
        record = pickle.loads(records.value)
        if consumer is not None:
            consumer.close()
        return record


async def send_producer(value_raw, topic_name='users'):
    kafka_producer = KafkaProducer(bootstrap_servers=["127.0.0.1:9092"], api_version=(0,10))
    value = pickle.dumps(value_raw)
    try:
        # key_bytes = bytes(key, encoding="utf-8")
        # value_bytes = bytes(value, encoding="utf-8")

        # key_bytes = pickle.dumps(key)
        # value_bytes = pickle.dumps(value)
        kafka_producer.send(topic_name, value=value)

        kafka_producer.flush()

        print("Send Success!")
    except Exception as exc:
        print("--")
        print(str(exc))
    if kafka_producer is not None:
        kafka_producer.close()


# def get_consumer():
#     consumer = KafkaConsumer(
#         "users",
#         auto_offset_reset="earliest",
#         bootstrap_servers=["127.0.0.1:9092"],
#         api_version=(0, 10),
#         consumer_timeout_ms=1000
#     )
    # records = pickle.loads(consumer.value)
    # print(records)
    # for record in records:
    #     print(record["users"])


def parse_response(response_raw):
    e = []

    for i in response_raw:
        # r = i.__dict__
        # print(i.profile.__dict__)

        # a = json.dumps(list(r))
        a = i.__dict__.copy()
        x = i.profile.__dict__.copy()
        a.__delitem__("_sa_instance_state")
        x.__delitem__("_sa_instance_state")
        a.__delitem__("profile")

        # print()
        # z = json.dumps(list(a))
        # y = json.loads(z)
        # print(y)
        # print(type(y))
        a["updated_at"] = str(a["updated_at"])
        a["created_at"] = str(a["created_at"])
        a["id"] = str(a["id"])

        x["updated_at"] = str(x["updated_at"])
        x["created_at"] = str(x["created_at"])
        x["id"] = str(x["id"])
        x["user_id"] = str(x["user_id"])

        data = {
            "user": a,
            "profile": x
        }
        # z = pickle.dumps(data)
        # d = json.loads(z)
        # g = json
        e.append(data)
        # print(e)
        # e.append(pickle.dumps(data))
    # print(e)
    # return e
    return json.dumps(e)
    # return pickle.dumps(e)
        # print(type(z))


@router.get(
    "/",
    # response_model=list[UserResponseSchema]
)
# @cache(expire=300)
async def read_users(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    response = await read_user_db(session=session)

    # kafka
    # send_producer(value, topic_name='users')
    # await send_producer(response, topic_name='users')
    # res = await get_consumer()
    # return res

    # redis
    # value = parse_response(response)
    # redis_cache(value)
    # res = redis_cache()
    # return json.loads(*res)

    return response


@router.get(
    "/{user_id}/",
    # response_model=UserResponseSchema
)
async def read_user_by_id(
        # current_user=Depends(get_current_active_user),
        user: UserSchema = Depends(user_by_id)
):
    return user


@router.post(
    "/",
response_model=UserResponseSchema,
status_code=status.HTTP_201_CREATED
)
async def create_user(
        user_in: UserCreateSchema,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    print(user_in)
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # user_in.password = pwd_context.hash(user_in.password)
    return await create_user_db(session=session, user_in=user_in)


@router.put(
    "/{user_id}",
    # response_model=UserResponseSchema
)
async def update_user(
        user_update: UserUpdateSchema,
        user: UserSchema = Depends(user_by_id),
        # current_user = Depends(get_current_active_user),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_user_db(
        session=session,
        user=user,
        user_update=user_update,
    )

@router.patch(
    "/{user_id}",
    # response_model=UserResponseSchema
)
async def update_user_partial(
        user_update: UserUpdatePartialSchema,
        user: UserSchema = Depends(user_by_id),
# current_user=Depends(get_current_active_user),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):

    return await update_user_db(
        session=session,
        user=user,
        user_update=user_update,
        partial=True
    )


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
        user: UserSchema = Depends(user_by_id),
# current_user=Depends(get_current_active_user),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await delete_user_db(user=user, session=session)



