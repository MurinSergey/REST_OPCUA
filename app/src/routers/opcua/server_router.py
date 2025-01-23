from fastapi import APIRouter

router = APIRouter(
    prefix="/opcua",
    tags=["OPCUA - запросы к серверу"]
)

@router.get(
        path="/info",
        summary="Получить информацию о OPCUA сервере"
)
async def get_info():
    return "Вы подключены к OPCUA серверу"

@router.post(
        path="/subscribe",
        summary="Обновить подписку на теги"
)
async def subscribe_tags():
    return "Подписки обновлены"

@router.post(
        path="/connect",
        summary="Подключиться к OPCUA серверу"
)
async def connect():
    return "OPC подключен"

@router.post(
        path="/disconnect",
        summary="Отключится от OPCUA сервера"
)
async def disconnect():
    return "OPC отключен"