from typing import Any, Optional

import httpx
from authlib.integrations.httpx_client import AsyncOAuth2Client

from flowptr_client.application.interfaces import FlowPTRClientInterface
from flowptr_client.config import FlowPTRClientSettings


class FlowPTRClient(FlowPTRClientInterface):
    def __init__(self, config: FlowPTRClientSettings = FlowPTRClientSettings()):
        self.config = config
        self.token = None
        self.client = AsyncOAuth2Client(
            client_id=config.CLIENT_ID,
            client_secret=config.CLIENT_SECRET,
            token_endpoint=str(config.auth_endpoint),
            grant_type="client_credentials",
            update_token=self._update_token,
        )

    async def _ensure_token(self):
        """Ensure we have a valid token"""
        if not self.token:
            self.token = await self.client.fetch_token(
                url=str(self.config.auth_endpoint),
                grant_type="client_credentials",
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "application/json",
                },
            )

    def _update_token(self, token: list[str, Any]):
        """Callback for token updates"""
        if token:
            self.token = token

    async def _request(self, method: str, endpoint: str, **kwargs) -> httpx.Response:
        """Make authenticated request to Shotgrid API"""
        await self._ensure_token()

        # Ensure headers are set
        kwargs.setdefault("headers", {})
        kwargs["headers"].update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

        url = f"{self.config.base_url}{endpoint}"
        response = await self.client.request(method, url, **kwargs)
        response.raise_for_status()
        return response

    async def get(
        self, endpoint: str, params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """Make GET request"""
        response = await self._request("GET", endpoint, params=params)
        return response.json()

    async def post(self, endpoint: str, json: dict[str, Any]) -> dict[str, Any]:
        """Make POST request"""
        response = await self._request("POST", endpoint, json=json)
        return response.json()

    async def put(self, endpoint: str, json: dict[str, Any]) -> dict[str, Any]:
        """Make PUT request"""
        response = await self._request("PUT", endpoint, json=json)
        return response.json()

    async def delete(self, endpoint: str) -> None:
        """Make DELETE request"""
        await self._request("DELETE", endpoint)
