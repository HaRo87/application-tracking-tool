from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.foundation import META_DATA
from src.foundation.models import get_db, CountriesOrm
from src.foundation.schemas import (
    CountryRequest,
    CountryResponse,
    MetaDataResponse,
)

router = APIRouter()


@router.get(
    "/meta",
    response_model=MetaDataResponse,
    summary="Get meta data",
    description="Get meta data about this service",
)
def get_meta():
    return META_DATA


@router.post(
    "/countries/",
    response_model=CountryResponse,
    summary="Create a new country",
    description="Create a new country in the database",
    status_code=HTTPStatus.CREATED,
)
def create_country(country: CountryRequest, db: Session = Depends(get_db)):
    db_country = CountriesOrm(name=country.name, code=country.code)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country
