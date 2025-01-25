import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.config import settings
from src.config.db.db_helper import setup_database
from src.routers import routers

#Функция жизни приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
        await setup_database()
        print(">>>>>БАЗА ДАННЫХ ГОТОВА")
        yield
        print(">>>>>ВЫКЛЮЧЕНИЕ")

#Функция которая собирает FastAPI
def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.project.name,
        version=settings.project.version,
        lifespan=lifespan
    )
    application.include_router(routers) #Подключаем все "ручки/роуты"
    return application

app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.fastapi.host, port=settings.fastapi.port, reload=True)