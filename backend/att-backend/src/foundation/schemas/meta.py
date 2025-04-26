from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class MetaDataResponse(BaseModel):
    version: str = Field(min_length=3, pattern=r"^v[0-9]+\.[0-9]+\.{0,1}[0-9]*")
    name: str = Field(min_length=1)
    url: HttpUrl
    description: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "version": "v0.2.1",
                "name": "Application Tracking Tool Backend",
                "url": "https://github.com/HaRo87/application-tracking-tool",
                "description": "A tool which helps in tracking job applications.",
            }
        }
