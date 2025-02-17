import asyncio
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config import settings
from app.config.db.db_helper import setup_database
from app.routers import routers
from app.config.opcua.opcua_helper import main_loop
from app.config.opcua.opcua_helper import opcua_client

#Функция жизни приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
        await setup_database()
        await asyncio.sleep(2)
        print(">>>>>БАЗА ДАННЫХ ГОТОВА")
        task = asyncio.create_task(main_loop())
        await asyncio.sleep(2)
        print(">>>>>ПРОЦЕСС OPC ЗАПУЩЕН ")
        yield
        task.cancel()
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