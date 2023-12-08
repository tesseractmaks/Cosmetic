import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, update, delete

from cosmetic_app.models.profile import Profile
from cosmetic_app.schemas import (
    ProfileSchema,
    ProfileUpdateSchema,
    ProfileCreateSchema,
    ProfileUpdatePartialSchema,
    ProfileResponseSchema,
    ProductSchema
)


async def read_profile_db(session: AsyncSession) -> list[ProfileSchema]:
    query = select(Profile).order_by(Profile.id)
    result: Result = await session.execute(query)
    profiles = result.scalars().all()
    return list(profiles)


async def read_profile_by_id_db(session: AsyncSession, profile_id: uuid.uuid4) -> ProfileSchema | None:
    return await session.get(Profile, profile_id)


async def create_profile_db(
        session: AsyncSession,
        profile_in: ProfileCreateSchema,
) -> Profile:
    profile_obj = profile_in.model_dump()
    profile = Profile(**profile_obj)
    session.add(profile)
    await session.commit()
    return profile


async def update_profile_db(
    session: AsyncSession,
        profile: ProfileSchema,
        profile_update: ProfileUpdateSchema | ProfileUpdatePartialSchema,
        partial: bool = False
) -> ProfileSchema:
    for name, value in profile_update.model_dump(exclude_unset=partial).items():
        setattr(profile, name, value)
    await session.commit()
    return profile


async def delete_profile_db(session: AsyncSession, profile: ProfileSchema) -> None:
    await session.delete(profile)
    await session.commit()