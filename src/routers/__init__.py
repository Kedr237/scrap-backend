from fastapi import APIRouter

from routers import v1

ROUTER_VERSIONS = [
    v1,
]


def get_all_routers() -> APIRouter:
    router = APIRouter(prefix='/api')

    for version in ROUTER_VERSIONS:
        version_router = version.get_router()
        router.include_router(version_router)

    return router
