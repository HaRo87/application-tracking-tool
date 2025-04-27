from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class MetaDataResponse(BaseModel):
    version: str = Field(
        min_length=3,
        pattern=r"^v[0-9]+\.[0-9]+\.{0,1}[0-9]*",
        description="A valid version following semantic versioning.",
        examples=["v0.1", "v2.2.1"],
    )
    name: str = Field(
        min_length=1,
        description="Name of the service.",
        examples=["My Awesome Service", "Application Tracking Tool"],
    )
    url: Optional[HttpUrl] = Field(
        description="A url pointing to the homepage of the service",
        examples=["https://my-awesome-service.com"],
        default=None,
    )
    description: Optional[str] = Field(
        description="A short description",
        examples=["A service which is awesome"],
        default=None,
    )
