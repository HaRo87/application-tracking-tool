import pytest

from pydantic import ValidationError

from src.foundation.schemas import CountryResponse, CountriesResponse

TEST_COUNTRY_NAME = "Canada"
TEST_COUNTRY_CODE = "CA"


@pytest.mark.unit
def test_country_response_validation_error_on_invalid_data():
    with pytest.raises(ValidationError) as ve:
        CountryResponse(name="", code=TEST_COUNTRY_CODE)
    assert "1 validation error for CountryResponse" in str(ve.value)
    assert "name" in str(ve.value)
    with pytest.raises(ValidationError) as ve:
        CountryResponse(name=TEST_COUNTRY_NAME, code="")
    assert "1 validation error for CountryResponse" in str(ve.value)
    assert "code" in str(ve.value)
    with pytest.raises(ValidationError) as ve:
        CountryResponse(name=TEST_COUNTRY_NAME, code="ABC")
    assert "1 validation error for CountryResponse" in str(ve.value)
    assert "code" in str(ve.value)
    with pytest.raises(ValidationError) as ve:
        CountryResponse(name=TEST_COUNTRY_NAME, code="A")
    assert "1 validation error for CountryResponse" in str(ve.value)
    assert "code" in str(ve.value)


@pytest.mark.unit
def test_country_response_works_with_valid_data():
    response = CountryResponse(name=TEST_COUNTRY_NAME, code=TEST_COUNTRY_CODE)
    assert response.name == TEST_COUNTRY_NAME
    assert response.code == TEST_COUNTRY_CODE


@pytest.mark.unit
def test_countries_response_validation_error_on_invalid_data():
    with pytest.raises(ValidationError) as ve:
        CountriesResponse(count=-1, values=[])
    assert "1 validation error for CountriesResponse" in str(ve.value)
    assert "count" in str(ve.value)
    with pytest.raises(ValidationError) as ve:
        CountriesResponse(count=0)
    assert "1 validation error for CountriesResponse" in str(ve.value)
    assert "values" in str(ve.value)


@pytest.mark.unit
def test_countries_response_works_with_valid_data():
    country_response = CountryResponse(
        name=TEST_COUNTRY_NAME, code=TEST_COUNTRY_CODE
    )
    empty_response = CountriesResponse(count=0, values=[])
    assert empty_response.count == 0
    assert len(empty_response.values) == 0
    small_response = CountriesResponse(count=1, values=[country_response])
    assert small_response.count == 1
    assert len(small_response.values) == 1
    assert small_response.values[0].name == TEST_COUNTRY_NAME
    assert small_response.values[0].code == TEST_COUNTRY_CODE
    large_response = CountriesResponse(
        count=3, values=[country_response, country_response, country_response]
    )
    assert large_response.count == 3
    assert len(large_response.values) == 3
    assert large_response.values[2].name == TEST_COUNTRY_NAME
    assert large_response.values[2].code == TEST_COUNTRY_CODE
