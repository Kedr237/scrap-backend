'''
Connecting all API v1 routers.
'''

from fastapi import APIRouter

from . import auth, base

router = APIRouter(prefix='/v1', tags=['v1'])

# Setup base endpoints.
base.setup_router(router)

# Modules for connecting to the router.
MODULES = [
    auth,
]


def get_router() -> APIRouter:
    '''
    Connects all version routers from MODULES to one router.

    Returns:
    - APIRouter: Router containing all version routers.
    '''

    # Connecting routers.
    for module in MODULES:
        router.include_router(module.router)

    return router
