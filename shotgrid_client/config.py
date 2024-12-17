from pydantic import Field, HttpUrl, computed_field
from pydantic_settings import BaseSettings


class ShotgridSettings(BaseSettings):
    """Shotgrid API configuration settings"""

    client_id: str = Field(..., description="Script Name")
    client_secret: str = Field(..., description="Script Key")
    domain: HttpUrl = Field(
        default="https://example.shotgrid.autodesk.com",
        description="Shotgrid domain URL",
    )
    api_version: str = Field(default="api/v1.1", description="API version")

    @computed_field
    @property
    def base_url(self) -> HttpUrl:
        return HttpUrl.build(
            scheme=self.domain.scheme,
            host=self.domain.host,
            path=self.api_version,
        )

    @computed_field
    @property
    def auth_endpoint(self) -> HttpUrl:
        return HttpUrl.build(
            scheme=self.domain.scheme,
            host=self.domain.host,
            path=f"{self.api_version}/auth/access_token",
        )

    class Config:
        env_prefix = "FPT_"  # Flow Production Tracking I guess...
        case_sensitive = False


if __name__ == "__main__":
    from rich import print

    config = ShotgridSettings()
    print(config)
    pass
