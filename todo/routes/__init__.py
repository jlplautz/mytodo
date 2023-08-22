from fastapi import APIRouter

from .user import router as router_user

# from .user import router as router_todo

main_router = APIRouter()

main_router.include_router(router_user, prefix='/user', tags=['user'])

# main_router.include_router(router_todo, prefix='/todo', tags=['todo'])
