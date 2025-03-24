'''
Provides a router for registration and authorization.
'''

from fastapi import APIRouter

from . import register

# Import router.
router = APIRouter(prefix='/auth', tags=['auth'])

# Other routers.
register_router = APIRouter(prefix='/register', tags=['register'])

# Connecting endpoints to other routers.
register.setup_router(register_router)

# Connecting other routers to the import router.
router.include_router(register_router)
