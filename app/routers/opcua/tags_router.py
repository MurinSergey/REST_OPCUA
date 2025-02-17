from fastapi import APIRouter
from ...schemas.db.opcua_tags_schema import SOpcuaTagResponse

router = APIRouter(
    prefix="/opcua/tags",
    tags=["OPCUA - запросы к тегам на которые подписан сервер"]
)

@router.get(
        path="/",
        summary="Получить список подписанных тегов"
)
async def get_tags():
    return "Список тегов на которые подписан opc клиент"

@router.get(
        path="/read/{tag_name}",
        summary="Получить текущее и историческое значение тега",
)
async def get_tag(tag_name: str, start_date: int = None, end_date: int = None):
    if (start_date is not None):
        if (end_date is not None):
            return f"История: {tag_name=} от {start_date=} до {end_date=}"
        else:
            return f"История: {tag_name=} от {start_date=} до текущей даты"
    else:
        return f"Актуальное значение тега: {tag_name=}"    

@router.get(
        path="/stat/{tag_name}",
        summary="Получить почасовую статистику тега"
)
async def get_stat_by_tag(tag_name: str, start_date: int = None, end_date: int = None, only_one_day: bool = True):
    if (only_one_day):
        if (start_date is None):
            return f"Статистика: {tag_name=} текущего дня"
        else:
            return f"Статистика: {tag_name=} указанного дня {start_date=}"
    else:
        if (start_date is None):
            return f"Ошибка - укажите начальную дату"
        else:
            if (end_date is None):
                return f"Статистика: {tag_name=} от указанного дня {start_date=} до текущего дня"
            else:
                return f"Статистика: {tag_name=} от указанного дня {start_date=} до {end_date=}"