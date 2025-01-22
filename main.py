import uvicorn
from fastapi import FastAPI
from src.routers import routers
from src.config import settings

def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.project.name,
        version=settings.project.version
    )
    application.include_router(routers)
    return application

app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.fastapi.host, port=settings.fastapi.port, reload=True)