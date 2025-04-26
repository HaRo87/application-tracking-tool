from fastapi import APIRouter

from src.foundation import META_DATA
from src.foundation.schemas import MetaDataResponse

router = APIRouter()


@router.get(
    "/meta",
    response_model=MetaDataResponse,
    summary="Get meta data",
    description="Get meta data about this service",
)
def get_meta():
    return META_DATA
