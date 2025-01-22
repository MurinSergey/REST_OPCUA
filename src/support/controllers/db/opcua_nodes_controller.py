from fastapi import APIRouter

router = APIRouter(
    prefix="/db/opcua/nodes",
    tags=["DB - запросы к таблице узлов для OPCUA сервера"]
)

@router.get(
        path="/",
        summary="Получить список всех узлов"
)
async def get_nodes():
    return "Список узлов для OPCUA сервера"

@router.get(
        path="/{nodeID}",
        summary="Получить указанный узел из базы данных"
)
async def get_node(nodeID: str):
    return f"Узел {nodeID}"

@router.post(
        path="/add",
        summary="Добавить новый узел в базу данных"
)
async def add_node():
    return "Узел добавлен"

@router.post(
        path="/remove",
        summary="Удалить узел из базы данных"
)
async def remove_node():
    return "Узел удален"

