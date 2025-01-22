from fastapi import APIRouter

router = APIRouter(
    prefix="/opcua",
    tags=["Запросы к серверу OPCUA"]
)

@router.get(
        path="/",
        summary="Получить информацию о OPCUA сервере"
)
async def get_info():
    return "Вы подключены к OPCUA серверу"

