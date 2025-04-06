from fastapi import FastAPI
from fastapi.responses import JSONResponse

from core.config import config
from core.lifespan import lifespan
from routers import get_all_routers

app = FastAPI(
    title=config.TITLE,
    docs_url=config.DOCS_URL,
    openapi_url=config.OPENAPI_URL,
    default_response_class=JSONResponse,
    lifespan=lifespan,
)

app.include_router(get_all_routers())
