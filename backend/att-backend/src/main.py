from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.foundation import META_DATA
from src.foundation.models import Base, get_engine
from src.routing.v1 import router as v1_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    try:
        Base.metadata.create_all(get_engine())
        yield
    finally:
        Base.metadata.drop_all(get_engine())


app = FastAPI(
    title="Application Tracking Tool",
    version=META_DATA.version,
    description=str(META_DATA.description),
    lifespan=lifespan,
)

app.include_router(v1_router, prefix="/v1")

add_pagination(app)
