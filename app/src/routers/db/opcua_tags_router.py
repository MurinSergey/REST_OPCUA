from fastapi import APIRouter
from ...schemas.db.opcua_tags_schema import SOpcuaTagResponse

router = APIRouter(
    prefix="/db/tags",
    tags=["DB - запросы к таблице тегов OPCUA клиента"]
)

@router.get(
        path="/",
        summary="Получить список всех узлов"
)
async def get_tags():
    return "Список тегов OPCUA клиента"

@router.get(
        path="/{tag_name}",
        summary="Получить указанный тег из базы данных",
        response_model=SOpcuaTagResponse
)
async def get_tag(tag_name: str) -> SOpcuaTagResponse:
    return f"Узел {tag_name}"

@router.post(
        path="/add",
        summary="Добавить новый тег в базу данных"
)
async def add_tag():
    return "Тег добавлен"

@router.post(
        path="/update",
        summary="Изменить тег"
)
async def update_tag():
    return "Тег изменен"

@router.post(
        path="/delete",
        summary="Удалить тег из базы данных"
)
async def delete_tag():
    return "Тег удален"

