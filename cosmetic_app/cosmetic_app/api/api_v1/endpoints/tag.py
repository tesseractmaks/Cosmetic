from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
# from passlib.context import CryptContext
from cosmetic_app.core import logger

from cosmetic_app.crud import (
    read_tag_db,
    update_tag_db,
    create_tag_db,
    delete_tag_db
)
from cosmetic_app.db import db_helper
from cosmetic_app.schemas import (
    TagSchema,
    TagCreateSchema,
    TagUpdateSchema,
    TagUpdatePartialSchema,
    TagResponseSchema
)
from .depends_endps import tag_by_id

# from cosmetic_app.auth import get_current_active_tag

router = APIRouter(tags=["Tag"])


@logger.catch
@router.get(
    "/",
    response_model=list[TagResponseSchema]
)
async def read_tags(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    tags = await read_tag_db(session=session)
    if tags is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            headers={"X-Error": "Url format wrong"},
        )
    return tags


@logger.catch
@router.get(
    "/{tag_id}/",
    response_model=TagResponseSchema
)
async def read_tag_by_id(
        # current_tag=Depends(get_current_active_tag),
        tag: TagSchema = Depends(tag_by_id)
):
    if tag is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            headers={"X-Error": "Url format wrong"},
        )
    return tag


@logger.catch
@router.post(
    "/",
    response_model=TagResponseSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_tag(
        tag_in: TagCreateSchema,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    if tag_in is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            headers={"X-Error": "Empty data"},
        )
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # tag_in.password = pwd_context.hash(tag_in.password)
    return await create_tag_db(session=session, tag_in=tag_in)


@logger.catch
@router.put(
    "/{tag_id}",
    response_model=TagResponseSchema
)
async def update_tag(
        tag_update: TagUpdateSchema,
        tag: TagSchema = Depends(tag_by_id),
        # current_tag = Depends(get_current_active_tag),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    if tag_update is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            headers={"X-Error": "Empty data"},
        )
    return await update_tag_db(
        session=session,
        tag=tag,
        tag_update=tag_update,
    )


@logger.catch
@router.patch(
    "/{tag_id}",
    response_model=TagResponseSchema
)
async def update_tag_partial(
        tag_update: TagUpdatePartialSchema,
        tag: TagSchema = Depends(tag_by_id),
        # current_tag=Depends(get_current_active_tag),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    if tag_update is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            headers={"X-Error": "Empty data"},
        )
    return await update_tag_db(
        session=session,
        tag=tag,
        tag_update=tag_update,
        partial=True
    )


@logger.catch
@router.delete("/{tag_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tag(
        tag: TagSchema = Depends(tag_by_id),
        # current_tag=Depends(get_current_active_tag),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    if tag is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            headers={"X-Error": "Url format wrong"},
        )
    await delete_tag_db(tag=tag, session=session)
