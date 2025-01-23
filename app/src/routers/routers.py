from fastapi import APIRouter

from .pages import start_page_router as home_page
from .db import opcua_nodes_router as opcua_nodes
from .opcua import server_router as opcua_server
from .opcua import tags_router as opcua_tags


def get_apps_router():
    router = APIRouter()
    router.include_router(home_page.router)
    router.include_router(opcua_nodes.router)
    router.include_router(opcua_server.router)
    router.include_router(opcua_tags.router)

    return router

routers = get_apps_router()