from fastapi import APIRouter

from .support.controllers import start_controller, opcua_controller

def get_apps_router():
    router = APIRouter()
    router.include_router(start_controller.router)
    router.include_router(opcua_controller.router)
    return router