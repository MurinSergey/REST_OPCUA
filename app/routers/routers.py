from fastapi import APIRouter

from .pages import start_page_router as home_page
from .db import opcua_tags_router as db_tags
from .opcua import server_router as opcua_server
from .opcua import tags_router as opcua_tags

#Функция собирает все роуты в одно место
def get_apps_router():
    router = APIRouter()
    router.include_router(home_page.router)
    router.include_router(db_tags.router)
    router.include_router(opcua_server.router)
    router.include_router(opcua_tags.router)

    return router

routers = get_apps_router()