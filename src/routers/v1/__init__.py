'''
Connecting all API v1 routers.
'''

from fastapi import APIRouter

from . import tests

MODULES = [
    tests,
]


def get_version_routers() -> APIRouter:
    '''
    Returns the version router.
    '''

    router = APIRouter(prefix='/v1', tags=['v1'])

    # Connecting routers.
    for module in MODULES:
        router.include_router(module.router)

    return router
