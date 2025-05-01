import pytest

from pydantic import ValidationError

from src.foundation.schemas import MetaDataResponse

TEST_VERSION = "v1.2.3"
TEST_NAME = "Test App"
TEST_DESCRIPTION = "Some description"
TEST_URL = "https://test.app/"


@pytest.mark.unit
def test_meta_data_response_validation_error_on_invalid_data():
    with pytest.raises(ValidationError) as ve:
        MetaDataResponse(
            version="",
            name=TEST_NAME,
            url=TEST_URL,
            description=TEST_DESCRIPTION,
        )
    assert "1 validation error for MetaDataResponse" in str(ve.value)
    assert "version" in str(ve.value)
    with pytest.raises(ValidationError) as ne:
        MetaDataResponse(
            version=TEST_VERSION,
            name="",
            url=TEST_URL,
            description=TEST_DESCRIPTION,
        )
    assert "1 validation error for MetaDataResponse" in str(ne.value)
    assert "name" in str(ne.value)
    with pytest.raises(ValidationError) as ue:
        MetaDataResponse(
            version=TEST_VERSION,
            name=TEST_NAME,
            url="some.url",
            description=TEST_DESCRIPTION,
        )
    assert "1 validation error for MetaDataResponse" in str(ue.value)
    assert "url" in str(ue.value)


@pytest.mark.unit
def test_meta_data_response_works_with_valid_data():
    min_response = MetaDataResponse(version=TEST_VERSION, name=TEST_NAME)
    assert min_response.version == TEST_VERSION
    assert min_response.name == TEST_NAME
    max_response = MetaDataResponse(
        version=TEST_VERSION,
        name=TEST_NAME,
        url=TEST_URL,
        description=TEST_DESCRIPTION,
    )
    assert max_response.version == TEST_VERSION
    assert max_response.name == TEST_NAME
    assert str(max_response.url) == TEST_URL
    assert max_response.description == TEST_DESCRIPTION
