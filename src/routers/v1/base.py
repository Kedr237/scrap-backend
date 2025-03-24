'''
Provides a function for connecting base endpoints.
'''

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from core.config import config


def setup_router(router: APIRouter) -> None:
    '''
    Connects endpoints to router.
    '''

    @router.get('/')
    async def root() -> RedirectResponse:
        '''
        Redirects to documentation.

        Returns:
        - RedirectResponse: Redirect to DOCS_URL.
        '''

        return RedirectResponse(url=config.DOCS_URL)
