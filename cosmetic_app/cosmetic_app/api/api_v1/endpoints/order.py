import json
from typing import Any

import jsonpickle
from fastapi import APIRouter, status, Depends, Request, Response
from fastapi.websockets import WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
# from passlib.context import CryptContext
import socket
import aiohttp
from cosmetic_app.api.api_v1.endpoints import get_consumer, create_producer
from cosmetic_app.crud import (
    read_order_db,
    # update_order_db,
    create_order_db,
    # delete_order_db,
)
from cosmetic_app.db import db_helper
from cosmetic_app.schemas import (
    OrderSchema,
    OrderResponseSchema,
    OrderCreateSchema,
    OrderUpdateSchema,
    OrderUpdatePartialSchema,
)

from cosmetic_app.schemas import (
    ProductSchema,
    ProductCreateSchema,
    ProductUpdateSchema,
    ProductUpdatePartialSchema,
    ProductResponseSchema,
    TagResponseSchema, CategoryResponseSchema
)
from .depends_endps import product_by_id

# from cosmetic_app.auth import get_current_active_product

router = APIRouter(tags=["Order"])


async def get_links(client: aiohttp.ClientSession, link):
    try:
        async with client.get(url=link) as response:
            return {"data": "12332312"}
    except Exception:
        pass


@router.get(
    "/",
    # response_model=list[ProductResponseSchema]
)
async def create_producers_order(
        topics: str,
        request: Request,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    for topic in topics.split(","):
        value = {
            'topic': str(topic),
            'host': str(request.client.host),
        }
        create_producer(value)


class ConnectionManager:
    def __init__(self):
        self.active_connection: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connection.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.active_connection.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connection:
            await connection.send_text(message)


manager = ConnectionManager()


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(
        websocket: WebSocket,
        client_id: str,
        # topic: str = None,
):
    # kafka
    # record = get_consumer(topic)

    # sockets
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # print(websocket)
            # await manager.send_personal_message(f"some text{data}", websocket)
            await manager.broadcast(f"Topic #{client_id} -- {data}")
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


@router.get(
    "/topic/{topic}/",
    # response_model=list[ProductResponseSchema]
)
async def get_consumer_order(
        response: Response,

        topic: str = None,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    record = get_consumer(topic)


@router.get(
    "/topic/event",
    # response_model=list[ProductResponseSchema]
)
async def get_consumer_order(
        response: Response,
        topic: str = None,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    print("response")

    response.headers["Content-Type"] = "text/event-stream"
    return {"data": "response"}


    # order_article = await read_order_db(session=session)
    # print(topics.split(","))

    # topics_obj = topics.model_dump()
    # print(topics_obj)
    # for topic in topics.split(","):
    #     create_producer(value=f"value-{topic}", topic_name=str(topic))
    # return order_article


# @router.get(
#     "/",
#     # response_model=list[ProductResponseSchema]
# )
# async def read_orders(
#         # topics: File(...),
#         topics: str,
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#
#     order_article = await read_order_db(session=session)
#     print(topics.split(","))
#     print(type(topics))
#     # topics_obj = topics.model_dump()
#     # print(topics_obj)
#     for topic in topics.split(","):
#         create_producer(value=f"value-{topic}", topic_name=str(topic))
#     return order_article

# @router.get(
#     "/{order_id}/",
#     response_model=ProductResponseSchema
# )
# async def read_order_by_id(
#         # current_order=Depends(get_current_active_order),
#         order: ProductSchema = Depends(order_by_id)
# ):
#     return order


# http://127.0.0.1:8000/api/v1/orders/tag/lush/


@router.post(
    "/",
    response_model=OrderResponseSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_order(
        order_in: ProductCreateSchema,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # order_in.password = pwd_context.hash(order_in.password)
    return await create_order_db(session=session, order_in=order_in)

#
# @router.put(
#     "/{order_id}",
#     # response_model=OrderResponseSchema
# )
# async def update_order(
#         order_update: ProductUpdateSchema,
#         order: ProductSchema = Depends(order_by_id),
#         # current_order = Depends(get_current_active_order),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ):
#     return await update_order_db(
#         session=session,
#         order=order,
#         order_update=order_update,
#     )
#
#
# @router.patch(
#     "/{order_id}",
#     response_model=ProductResponseSchema
# )
# async def update_order_partial(
#         order_update: ProductUpdatePartialSchema,
#         order: ProductSchema = Depends(order_by_id),
#         # current_order=Depends(get_current_active_order),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ):
#     return await update_order_db(
#         session=session,
#         order=order,
#         order_update=order_update,
#         partial=True
#     )
#
#
# @router.delete("/{order_id}/", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_order(
#         order: ProductSchema = Depends(order_by_id),
#         # current_order=Depends(get_current_active_order),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ) -> None:
#     await delete_order_db(order=order, session=session)
