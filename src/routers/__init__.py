'''
Connecting all routers.

API versions:
    v1
'''

from fastapi import APIRouter

from routers import v1

ROUTER_VERSIONS = [
    v1,
]


def get_all_routers() -> APIRouter:
    '''
    Returns the main router with all endpoints.
    '''

    router = APIRouter(prefix='/api')

    # Connecting version routers.
    for version in ROUTER_VERSIONS:
        version_router = version.get_router()
        router.include_router(version_router)

    return router
