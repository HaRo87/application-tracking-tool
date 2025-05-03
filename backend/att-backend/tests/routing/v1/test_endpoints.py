from http import HTTPStatus

import pytest

from fastapi import HTTPException
from unittest.mock import MagicMock, Mock, patch

from src.foundation.schemas import CountryRequest
from src.routing.v1.endpoints import create_country


@pytest.fixture
def mock_db_session():
    session = MagicMock()
    session.add = MagicMock()
    session.commit = MagicMock()
    session.refresh = MagicMock()
    return session


@pytest.fixture
def mock_v1_countries():
    return [
        Mock(id=1, name="Canada", code="CA"),
        Mock(id=2, name="Germany", code="DE"),
    ]


@pytest.mark.unit
@patch("src.foundation.models.database.get_db", return_value=MagicMock())
def test_create_country_success(mock_db, mock_db_session):
    mock_db.return_value.__enter__.return_value = mock_db_session
    mock_db_session.query.return_value.filter.return_value.first.return_value = (
        None
    )
    mock_db_session.refresh.side_effect = lambda item: setattr(item, "id", 1)

    country_data = CountryRequest(name="Canada", code="CA")
    created_country = create_country(country=country_data, db=mock_db_session)

    assert created_country.id == 1
    assert created_country.name == country_data.name
    assert created_country.code == country_data.code


@pytest.mark.unit
@patch("src.foundation.models.database.get_db", return_value=MagicMock())
def test_create_country_fail(mock_db, mock_db_session, mock_v1_countries):
    mock_db.return_value.__enter__.return_value = mock_db_session
    mock_db_session.query.return_value.filter.return_value.first.return_value = mock_v1_countries[
        0
    ]

    country_data = CountryRequest(name="Canada", code="CA")
    with pytest.raises(HTTPException) as he:
        create_country(country=country_data, db=mock_db_session)
    assert he.value.status_code == HTTPStatus.CONFLICT
    assert he.value.detail == "Country already exists"
