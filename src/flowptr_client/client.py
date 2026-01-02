"""Main client for Flow Production Tracking REST API."""

from collections.abc import Mapping
from typing import Any, Optional, Union

import httpx
from authlib.integrations.httpx_client import AsyncOAuth2Client
from authlib.oauth2.rfc6749 import OAuth2Token

from flowptr_client.config import FlowPTRSettings
from flowptr_client.exceptions import (
    STATUS_CODE_EXCEPTIONS,
    FlowPTRConnectionError,
    FlowPTRError,
    FlowPTRHTTPError,
    FlowPTRTimeoutError,
)
from flowptr_client.interfaces import FlowPTRRestAPIClientInterface
from flowptr_client.models.responses import ErrorResponse


class FlowPTRClient(FlowPTRRestAPIClientInterface):
    """Async HTTP client for Flow Production Tracking REST API.

    This is a low-level HTTP client that handles OAuth2 authentication and
    request/response management. For a higher-level API with route handlers,
    use FlowPTRAPI instead.

    Examples:
        >>> # Initialize with environment variables
        >>> client = FlowPTRClient()
        >>>
        >>> # Or pass config directly
        >>> config = FlowPTRSettings(
        ...     CLIENT_ID="your_script_name",
        ...     CLIENT_SECRET="your_script_key",
        ...     DOMAIN="https://your-site.shotgrid.autodesk.com"
        ... )
        >>> client = FlowPTRClient(config)
        >>>
        >>> # Make raw HTTP requests
        >>> projects = await client.get("/entity/projects")
        >>> await client.post("/entity/projects", json={"data": {...}})

    Attributes:
        config: Client configuration settings
        token: Current OAuth2 access token
        client: Underlying async OAuth2 HTTP client
    """

    def __init__(self, config: FlowPTRSettings = FlowPTRSettings()) -> None:
        """Initialize the FlowPTR client.

        Args:
            config: Client configuration (loads from environment if not provided)
        """
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
        """Ensure we have a valid OAuth2 access token.

        Fetches a new token if one doesn't exist. Token refresh is handled
        automatically by the OAuth2 client.

        Raises:
            FlowPTRAuthenticationError: If token fetch fails
        """
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
        """Callback for OAuth2 client to update stored token.

        Args:
            token: New OAuth2 token from refresh
        """
        if token:
            self.token = token

    def _handle_http_error(self, error: httpx.HTTPStatusError) -> FlowPTRError:
        """Convert httpx HTTP errors to FlowPTR exceptions.

        Attempts to parse the error response as a FlowPTR error object
        and raise the appropriate exception type based on the status code.

        Args:
            error: The httpx HTTP status error

        Returns:
            Appropriate FlowPTRError subclass instance
        """
        try:
            # Try to parse as FlowPTR error response
            error_data = error.response.json()
            error_response = ErrorResponse(**error_data)

            # Get first error for exception details
            first_error = error_response.errors[0]

            # Map to appropriate exception class
            exception_class = STATUS_CODE_EXCEPTIONS.get(
                first_error.status, FlowPTRHTTPError
            )

            return exception_class(
                message=f"{first_error.title}: {first_error.detail or ''}".strip(),
                status_code=first_error.status,
                error_code=first_error.code,
                details={
                    "source": first_error.source,
                    "meta": first_error.meta,
                    "error_id": first_error.id,
                },
            )
        except Exception:
            # Fallback if response isn't valid FlowPTR error format
            exception_class = STATUS_CODE_EXCEPTIONS.get(
                error.response.status_code, FlowPTRHTTPError
            )
            return exception_class(
                message=f"HTTP {error.response.status_code}: {error.response.text}",
                status_code=error.response.status_code,
            )

    async def _request(
        self, method: str, endpoint: str, **kwargs: Mapping[str, Any]
    ) -> httpx.Response:
        """Make authenticated request to Flow Production Tracking API.

        Handles token management, sets appropriate headers, and converts
        HTTP errors to FlowPTR exceptions.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path (e.g., "/entity/projects")
            **kwargs: Additional arguments passed to httpx request

        Returns:
            HTTP response object

        Raises:
            FlowPTRAuthenticationError: Authentication failed
            FlowPTRValidationError: Request validation failed
            FlowPTRNotFoundError: Resource not found
            FlowPTRServerError: Server-side error
            FlowPTRConnectionError: Network connection error
            FlowPTRTimeoutError: Request timeout
        """
        try:
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

        except httpx.HTTPStatusError as e:
            raise self._handle_http_error(e) from e
        except httpx.TimeoutException as e:
            raise FlowPTRTimeoutError(f"Request timed out: {e}") from e
        except httpx.RequestError as e:
            raise FlowPTRConnectionError(f"Connection failed: {e}") from e

    async def get(
        self, endpoint: str, params: Optional[Mapping[str, Any]] = None
    ) -> dict[str, Any]:
        """Make GET request to the API.

        Args:
            endpoint: API endpoint path
            params: Query parameters

        Returns:
            Parsed JSON response as dictionary

        Raises:
            FlowPTRError: If request fails
        """
        response = await self._request("GET", endpoint, params=params)
        return response.json()

    async def post(
        self,
        endpoint: str,
        json: dict[str, Any],
        params: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> dict[str, Any]:
        """Make POST request to the API.

        Args:
            endpoint: API endpoint path
            json: Request body as dictionary
            params: Query parameters
            headers: Additional headers to send

        Returns:
            Parsed JSON response as dictionary

        Raises:
            FlowPTRError: If request fails
        """
        response = await self._request(
            "POST", endpoint, params=params, json=json, headers=headers
        )
        return response.json()

    async def put(self, endpoint: str, json: dict[str, Any]) -> dict[str, Any]:
        """Make PUT request to the API.

        Args:
            endpoint: API endpoint path
            json: Request body as dictionary

        Returns:
            Parsed JSON response as dictionary

        Raises:
            FlowPTRError: If request fails
        """
        response = await self._request("PUT", endpoint, json=json)
        return response.json()

    async def delete(self, endpoint: str) -> None:
        """Make DELETE request to the API.

        Args:
            endpoint: API endpoint path

        Raises:
            FlowPTRError: If request fails
        """
        await self._request("DELETE", endpoint)
