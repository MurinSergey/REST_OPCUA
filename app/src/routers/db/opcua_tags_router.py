from typing import Annotated
from fastapi import APIRouter, Depends

from ...repositories.db import opcua_tags_repository
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
    tags = await opcua_tags_repository.get_all()
    return tags
####################################################################################
@router.get(
        path="/getone/{tag_name_get}",
        summary="Получить указанный тег из базы данных",
)
async def get_tag(tag_name_get: str) -> list[SOpcuaTagResponse]:
    tags = await opcua_tags_repository.get_single(tag_name=tag_name_get)
    return tags
####################################################################################
@router.post(
        path="/addone",
        summary="Добавить новый тег в базу данных"
)
async def add_tag(
    tag: Annotated[SOpcuaTagCreate, Depends()],
) -> SOpcuaTagResponse:
    tag_dict = tag.model_dump()
    tag = await opcua_tags_repository.create(tag_dict)
    return tag
####################################################################################
@router.post(
        path="/update/{tag_name_update}",
        summary="Изменить выбранный тег"
)
async def update_tag(
    tag_name_update: str,
    data: Annotated[SOpcuaTagUpdate, Depends()]
) -> SOpcuaTagResponse:
    data_dict = data.model_dump()
    tag = await opcua_tags_repository.update(data_dict, tag_name=tag_name_update)
    return tag
####################################################################################
@router.post(
        path="/delete/{tag_name_delete}",
        summary="Удалить тег из базы данных"
)
async def delete_tag(tag_name_delete: str) -> SOpcuaTagResponse:
    tag = await opcua_tags_repository.delete(tag_name=tag_name_delete)
    return tag