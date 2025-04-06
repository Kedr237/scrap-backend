from fastapi import APIRouter

from . import register

router = APIRouter(prefix='/auth', tags=['auth'])

register_router = APIRouter(prefix='/register', tags=['register'])

register.setup_router(register_router)

router.include_router(register_router)
