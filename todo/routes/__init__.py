from fastapi import APIRouter

from .auth import router as router_auth
from .user import router as router_user

main_router = APIRouter()

main_router.include_router(router_user, prefix='/user', tags=['user'])

main_router.include_router(router_auth, tags=['authentication'])
