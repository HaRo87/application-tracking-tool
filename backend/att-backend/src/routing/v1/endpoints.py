from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import apaginate
from sqlalchemy import select
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


@router.get(
    path="/countries",
    response_model=Page[CountryResponse],
    summary="Get all countries",
    description="Get a list of all countries",
    status_code=HTTPStatus.OK,
)
async def get_countries(db: Session = Depends(get_db)):
    return await apaginate(
        conn=db, query=select(CountriesOrm).order_by(CountriesOrm.name)
    )


@router.get(
    path="/countries/{id}",
    response_model=CountryResponse,
    summary="Get a specific country",
    description="Get details about a specific country",
    status_code=HTTPStatus.OK,
)
def get_country(id: int, db: Session = Depends(get_db)):
    db_country = db.query(CountriesOrm).filter(CountriesOrm.id == id).first()
    if db_country is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Country does not exist"
        )
    return db_country


@router.post(
    path="/countries/",
    response_model=CountryResponse,
    summary="Create a new country",
    description="Create a new country in the database",
    status_code=HTTPStatus.CREATED,
)
def create_country(country: CountryRequest, db: Session = Depends(get_db)):
    db_country = (
        db.query(CountriesOrm)
        .filter(
            (CountriesOrm.name == country.name)
            & (CountriesOrm.code == country.code)
        )
        .first()
    )
    if db_country is None:
        db_country = CountriesOrm(name=country.name, code=country.code)
        db.add(db_country)
        db.commit()
        db.refresh(db_country)
        return db_country
    else:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail="Country already exists"
        )


@router.delete(
    path="/countries/{id}",
    summary="Delete a country",
    description="Delete the specified country",
    status_code=HTTPStatus.OK,
)
def delete_country(id: int, db: Session = Depends(get_db)):
    if id < 1:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="invalid id, must be > 0"
        )
    db_country = db.query(CountriesOrm).filter(CountriesOrm.id == id).first()
    if db_country is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Country does not exist"
        )
    db.delete(db_country)
    db.commit()
