import pytest

from unittest.mock import MagicMock, patch

from src.foundation.schemas import CountryRequest
from src.routing.v1.endpoints import create_country


@pytest.fixture
def mock_db_session():
    session = MagicMock()
    session.add = MagicMock()
    session.commit = MagicMock()
    session.refresh = MagicMock()
    return session


@pytest.mark.unit
@patch("src.foundation.models.database.get_db", return_value=MagicMock())
def test_create_country_success(mock_db, mock_db_session):
    mock_db.return_value.__enter__.return_value = mock_db_session
    mock_db_session.refresh.side_effect = lambda item: setattr(item, "id", 1)

    country_data = CountryRequest(name="Canada", code="CA")
    created_country = create_country(country=country_data, db=mock_db_session)

    assert created_country.id == 1
    assert created_country.name == country_data.name
    assert created_country.code == country_data.code
