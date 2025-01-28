from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from ...service import db_opcua_tags_service
from ...schemas.db import SOpcuaTagCreate, SOpcuaTagResponse

router = APIRouter(
    prefix="/db/tags",
    tags=["DB - запросы к таблице тегов OPCUA клиента"]
)
####################################################################################
@router.get(
        path="/getall",
        summary="Получить список всех тегов из базы данных"
)
async def get_tags() -> list[SOpcuaTagResponse]:
    try:
        res = await db_opcua_tags_service.get_all(order="tag_name")
        return res
    except Exception as err:
        print(type(err))
        raise HTTPException(status_code=418, detail="ОШИБКА: получения списка тегов")
####################################################################################
@router.get(
        path="/getone/{req_tag_name}",
        summary="Получить указанный тег из базы данных",
)
async def get_tag(req_tag_name: str) -> SOpcuaTagResponse:
    try:
        res = await db_opcua_tags_service.get_single(tag_name=req_tag_name)
        return res
    except Exception as err:
        print(type(err))
        raise HTTPException(status_code=418, detail=f"ОШИБКА: неверный {req_tag_name=}")
####################################################################################
@router.post(
        path="/addone",
        summary="Добавить новый тег в базу данных"
)
async def add_tag(
    tag: Annotated[SOpcuaTagCreate, Depends()],
) -> SOpcuaTagResponse:
    try:
        res = await db_opcua_tags_service.create(tag)
        return res
    except Exception as err:
        print(type(err))
        raise HTTPException(status_code=418, detail=f"ОШИБКА: неверный {tag=}")
####################################################################################
@router.post(
        path="/update/{req_tag_name}",
        summary="Изменить выбранный тег",
)
async def update_tag(
    req_tag_name: str,
    data: Annotated[SOpcuaTagCreate, Depends()]
) -> SOpcuaTagResponse:
    try:
        res = await db_opcua_tags_service.update(data, tag_name=req_tag_name)
        return res
    except Exception as err:
        print(type(err))
        raise HTTPException(status_code=418, detail=f"ОШИБКА: неверный {req_tag_name=}")
####################################################################################
@router.post(
        path="/delete/{req_tag_name}",
        summary="Удалить тег из базы данных"
)
async def delete_tag(req_tag_name: str) -> SOpcuaTagResponse:
    try:
        res = await db_opcua_tags_service.delete(tag_name=req_tag_name)
        return res
    except Exception as err:
        print(type(err))
        raise HTTPException(status_code=418, detail=f"ОШИБКА: неверный {req_tag_name=}")