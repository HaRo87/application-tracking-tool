from pydantic import HttpUrl

from src.foundation.schemas import MetaDataResponse

META_DATA = MetaDataResponse(
    version="v0.1",
    name="Application Tracking Tool Backend",
    description="A tool which helps in tracking job applications.",
    url=HttpUrl(url="https://github.com/HaRo87/application-tracking-tool"),
)
