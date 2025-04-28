from fastapi import FastAPI

from src.foundation import META_DATA
from src.routing.v1 import router as v1_router

app = FastAPI(
    title="Application Tracking Tool",
    version=META_DATA.version,
    description=str(META_DATA.description),
)

app.include_router(v1_router, prefix="/v1")
