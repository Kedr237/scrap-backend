'''
Provides a function for connecting registration endpoints.
'''

from fastapi import APIRouter


def setup_router(router: APIRouter) -> None:
    '''
    Connects endpoints to router.

    Returns:
    - str: Success message.
    '''

    @router.get('/')
    async def test_connecting() -> str:
        return 'The connection was successful!'
