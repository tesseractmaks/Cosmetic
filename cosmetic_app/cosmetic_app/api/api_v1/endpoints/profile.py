from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
# from passlib.context import CryptContext

from cosmetic_app.crud import (
    read_profile_db,
    update_profile_db,
    create_profile_db,
    delete_profile_db
)
from cosmetic_app.db import db_helper
from cosmetic_app.schemas import (
    ProfileSchema,
    ProfileCreateSchema,
    ProfileUpdateSchema,
    ProfileUpdatePartialSchema,
    ProfileResponseSchema
)
from .depends_endps import profile_by_id

# from cosmetic_app.auth import get_current_active_profile

router = APIRouter(tags=["Profile"])


@router.get(
    "/",
    response_model=list[ProfileResponseSchema]
)
async def read_profiles(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await read_profile_db(session=session)


@router.get(
    "/{profile_id}/",
    response_model=ProfileResponseSchema
)
async def read_profile_by_id(
        # current_profile=Depends(get_current_active_profile),
        profile: ProfileSchema = Depends(profile_by_id)
):
    return profile


@router.post(
    "/",
response_model=ProfileResponseSchema,
status_code=status.HTTP_201_CREATED
)
async def create_profile(
        profile_in: ProfileCreateSchema,
        session: AsyncSession= Depends(db_helper.scoped_session_dependency)
):
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # profile_in.password = pwd_context.hash(profile_in.password)
    return await create_profile_db(session=session, profile_in=profile_in)


@router.put(
    "/{profile_id}",
    response_model=ProfileResponseSchema
)
async def update_profile(
        profile_update: ProfileUpdateSchema,
        profile: ProfileSchema = Depends(profile_by_id),
        # current_profile = Depends(get_current_active_profile),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_profile_db(
        session=session,
        profile=profile,
        profile_update=profile_update,
    )

@router.patch(
    "/{profile_id}",
    response_model=ProfileResponseSchema
)
async def update_profile_partial(
        profile_update: ProfileUpdatePartialSchema,
        profile: ProfileSchema = Depends(profile_by_id),
# current_profile=Depends(get_current_active_profile),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_profile_db(
        session=session,
        profile=profile,
        profile_update=profile_update,
        partial=True
    )


@router.delete("/{profile_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(
        profile: ProfileSchema = Depends(profile_by_id),
# current_profile=Depends(get_current_active_profile),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await delete_profile_db(profile=profile, session=session)



