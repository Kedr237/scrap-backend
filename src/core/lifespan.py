from contextlib import asynccontextmanager

from fastapi import FastAPI

from core import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.drop_models()
    await database.init_models()
    yield
