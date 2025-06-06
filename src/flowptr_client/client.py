from collections.abc import Mapping
from typing import Any, Optional, Union

import httpx
from authlib.integrations.httpx_client import AsyncOAuth2Client
from authlib.oauth2.rfc6749 import OAuth2Token

from flowptr_client.config import FlowPTRSettings


class FlowPTClient:
    def __init__(self, config: FlowPTRSettings = FlowPTRSettings()) -> None:
        self.config = config
        self.token: Union[None, OAuth2Token] = None
        self.client = AsyncOAuth2Client(
            client_id=config.CLIENT_ID,
            client_secret=config.CLIENT_SECRET,
            token_endpoint=str(config.auth_endpoint),
            grant_type="client_credentials",
            update_token=self._update_token,
        )

    async def _ensure_token(self) -> None:
        """Ensure we have a valid token"""
        if not self.token:
            self.token = await self.client.fetch_token(  # type: ignore
                url=str(self.config.auth_endpoint),
                grant_type="client_credentials",
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "application/json",
                },
            )

    def _update_token(self, token: Union[None, OAuth2Token]) -> None:
        """Callback for token updates"""
        if token:
            self.token = token

    async def _request(
        self, method: str, endpoint: str, **kwargs: Mapping[str, Any]
    ) -> httpx.Response:
        """Make authenticated request to Shotgrid API"""
        await self._ensure_token()

        # Ensure headers are set
        kwargs.setdefault("headers", {})
        if not kwargs["headers"]:
            kwargs["headers"].update(
                {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                }
            )

        url = f"{self.config.base_url}{endpoint}"
        response = await self.client.request(method, url, **kwargs)  # type: ignore
        response.raise_for_status()
        return response

    async def get(
        self, endpoint: str, params: Optional[Mapping[str, Any]] = None
    ) -> dict[str, Any]:
        """Make GET request"""
        response = await self._request("GET", endpoint, params=params)
        return response.json()

    async def post(
        self,
        endpoint: str,
        json: dict[str, Any],
        params: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> dict[str, Any]:
        """Make POST request"""
        response = await self._request(
            "POST", endpoint, params=params, json=json, headers=headers
        )
        return response.json()

    async def put(self, endpoint: str, json: dict[str, Any]) -> dict[str, Any]:
        """Make PUT request"""
        response = await self._request("PUT", endpoint, json=json)
        return response.json()

    async def delete(self, endpoint: str) -> None:
        """Make DELETE request"""
        await self._request("DELETE", endpoint)
