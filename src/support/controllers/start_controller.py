from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=["Стартовая страница"]
)

@router.get(
        path="/",
        summary="Стартовая страница сервиса"
)
async def home():
    return "Для изучния API перейдите на /docs"