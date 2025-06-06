from pydantic import Field, HttpUrl, computed_field
from pydantic_settings import BaseSettings


class FlowPTRSettings(BaseSettings):
    """FlowPTR API configuration settings"""

    CLIENT_ID: str = Field(..., description="Script Name")
    CLIENT_SECRET: str = Field(..., description="Script Key")
    DOMAIN: HttpUrl = Field(
        default="https://example.shotgrid.autodesk.com",
        description="FlowPTR domain URL",
    )
    API_VERSION: str = Field(default="api/v1.1", description="API version")

    @computed_field
    @property
    def base_url(self) -> HttpUrl:
        return HttpUrl.build(
            scheme=self.DOMAIN.scheme,
            host=self.DOMAIN.host,
            path=self.API_VERSION,
        )

    @computed_field
    @property
    def auth_endpoint(self) -> HttpUrl:
        return HttpUrl.build(
            scheme=self.DOMAIN.scheme,
            host=self.DOMAIN.host,
            path=f"{self.API_VERSION}/auth/access_token",
        )

    class Config:
        env_prefix = "FPTR_"  # Flow Production Tracking I guess...
        case_sensitive = False


if __name__ == "__main__":
    from rich import print

    config = FlowPTRSettings()
    print(config)
    pass
