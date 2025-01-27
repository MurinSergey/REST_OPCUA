from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from ...service.db_opcua_tags_service import db_opcua_tags_service
from ...schemas.db.opcua_tags_schema import SOpcuaTagCreate, SOpcuaTagResponse, SOpcuaTagUpdate

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
        res = await db_opcua_tags_service.get_all()
        return res
    except Exception:
        raise HTTPException(status_code=418, detail="ОШИБКА: получения списка тегов")
####################################################################################
@router.get(
        path="/getone/{tag_name_get}",
        summary="Получить указанный тег из базы данных",
)
async def get_tag(tag_name_get: str) -> list[SOpcuaTagResponse]:
    try:
        res = await db_opcua_tags_service.get_single(tag_name_get)
        return res
    except Exception:
        raise HTTPException(status_code=418, detail=f"ОШИБКА: неверный {tag_name_get=}")
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
    except Exception:
        raise HTTPException(status_code=418, detail=f"ОШИБКА: неверный {tag.tag_name=}")
####################################################################################
@router.post(
        path="/update/{tag_name_update}",
        summary="Изменить выбранный тег"
)
async def update_tag(
    tag_name_update: str,
    data: Annotated[SOpcuaTagUpdate, Depends()]
) -> SOpcuaTagResponse:
    try:
        res = await db_opcua_tags_service.update(data, tag_name_update)
        return res
    except Exception:
        raise HTTPException(status_code=418, detail=f"ОШИБКА: неверный {tag_name_update=}")
####################################################################################
@router.post(
        path="/delete/{tag_name_delete}",
        summary="Удалить тег из базы данных"
)
async def delete_tag(tag_name_delete: str) -> SOpcuaTagResponse:
    try:
        res = await db_opcua_tags_service.delete(tag_name_delete)
        return res
    except Exception:
        raise HTTPException(status_code=418, detail=f"ОШИБКА: неверный {tag_name_delete=}")