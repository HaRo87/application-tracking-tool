from typing import List

from pydantic import BaseModel, Field


class CountryResponse(BaseModel):
    name: str = Field(
        min_length=1,
        description="Name of the country",
        examples=["Canada", "Germany"],
    )
    code: str = Field(
        min_length=2,
        max_length=2,
        pattern=r"^[A-Z]{2,2}$",
        description="The country code following the ISO-3166-1 alpha-2 scheme",
        examples=["CA", "DE"],
    )


class CountriesResponse(BaseModel):
    count: int = Field(
        ge=0, description="Number of countries", examples=[10, 2]
    )
    values: List[CountryResponse] = Field(
        min_length=0,
        description="List of countries",
        examples=[[CountryResponse(name="Canada", code="CA")]],
    )
