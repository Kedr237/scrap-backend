'''
Application executable.

- Initializes FastAPI application.
- Includes routers.
- Customizes cors.
'''

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from core.config import config
from routers import get_all_routers

app = FastAPI(
    title=config.TITLE,
    docs_url=config.DOCS_URL,
    openapi_url=config.OPENAPI_URL,
    default_response_class=JSONResponse,
)

app.include_router(get_all_routers())

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
