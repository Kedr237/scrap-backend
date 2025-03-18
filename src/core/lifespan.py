'''
Application lifespan.

Initializes and closes database connections.
'''

from contextlib import asynccontextmanager

from fastapi import FastAPI

from core import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    '''
    Is called at application startup and shutdown.

    Args:
    - app: FastAPI application instance
    '''

    await database.init_models()
    yield
    await database.drop_models()
