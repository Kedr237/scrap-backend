'''
Customizes the endpoints.
'''

from fastapi import APIRouter


def setup_router(router: APIRouter):
    '''
    Connects endpoints to router.
    '''

    @router.get('/')
    async def test_hello() -> str:
        return 'Hello world!'
