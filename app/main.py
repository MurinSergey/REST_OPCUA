import uvicorn, asyncio
from fastapi import FastAPI
from src.config import settings
from src.models.db import setup_database
from src.routers import routers

def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.project.name,
        version=settings.project.version
    )
    application.include_router(routers)
    return application

app = get_application()

if __name__ == "__main__":
    asyncio.run(setup_database())
    uvicorn.run("main:app", host=settings.fastapi.host, port=settings.fastapi.port, reload=True)