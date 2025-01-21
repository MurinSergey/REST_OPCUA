from fastapi import APIRouter

from .support.controllers import start_controller

def get_apps_router():
    router = APIRouter()
    router.include_router(start_controller.router)
    return router