from fastapi import APIRouter

from .support.controllers import start_controller
from .support.controllers.opcua import server_controller as opcua_server
from .support.controllers.opcua import tags_conroller as opcua_tags

def get_apps_router():
    router = APIRouter()
    router.include_router(start_controller.router)
    router.include_router(opcua_server.router)
    router.include_router(opcua_tags.router)
    return router