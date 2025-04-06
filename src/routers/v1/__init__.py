from fastapi import APIRouter

from . import auth, base

router = APIRouter(prefix='/v1', tags=['v1'])

base.setup_router(router)

MODULES = [
    auth,
]


def get_router() -> APIRouter:
    for module in MODULES:
        router.include_router(module.router)

    return router
