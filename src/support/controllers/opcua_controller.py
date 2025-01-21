from fastapi import APIRouter

router = APIRouter(
    prefix="/opcua",
    tags=["Запросы к OPCUA"]
)

@router.get("/")
async def get_info():
    return "Вы подключены к OPCUA серверу"

@router.get("/tags")
async def get_tags():
    return "Список тегов на которые подписан клиент"

@router.get("/tags/{nodeID}")
async def get_tag_value(nodeID: int):
    return f"Актуальное значение тега: {nodeID}"

@router.get("/tags/{nodeID}")
async def get_tag_history(nodeID: int, date: int):
    return f"Актуальное значение тега: {nodeID}"
