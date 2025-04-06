from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from core.config import config


def setup_router(router: APIRouter) -> None:
    @router.get('/')
    async def root() -> RedirectResponse:
        return RedirectResponse(url=config.DOCS_URL)
