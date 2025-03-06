'''
Provides tests router.
'''

from fastapi import APIRouter

from . import tests

router = APIRouter(prefix='/tests', tags=['tests'])

# Connecting endpoints.
tests.setup_router(router)
