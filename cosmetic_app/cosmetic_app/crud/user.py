import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, update, delete

from cosmetic_app.models import User
from cosmetic_app.schemas import (
    UserSchema,
    UserUpdateSchema,
    UserCreateSchema,
    UserUpdatePartialSchema,
)


async def read_user_db(session: AsyncSession) -> list[UserSchema]:
    query = select(User).order_by(User.id)
    result: Result = await session.execute(query)
    users = result.scalars().all()
    return list(users)


async def read_user_by_id_db(session: AsyncSession, user_id: uuid.uuid4) -> UserSchema | None:
    return await session.get(User, user_id)


async def create_user_db(
        session: AsyncSession,
        user_in: UserCreateSchema,
) -> User:
    user_obj = user_in.model_dump()
    user = User(**user_obj)
    session.add(user)
    await session.commit()
    return user


async def update_user_db(
    session: AsyncSession,
        user: UserSchema,
        user_update: UserUpdateSchema | UserUpdatePartialSchema,
        partial: bool = False
) -> UserSchema:
    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()
    return user


async def delete_user_db(session: AsyncSession, user: UserSchema) -> None:
    await session.delete(user)
    await session.commit()