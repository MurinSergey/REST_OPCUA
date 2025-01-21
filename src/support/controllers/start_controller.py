from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=["Стартовая страница"]
)

@router.get("/")
async def get_hello():
    return "Для изучния API перейдите на /docs"