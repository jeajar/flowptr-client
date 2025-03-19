from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_credentials_request import ClientCredentialsRequest
from ...models.error_response import ErrorResponse
from ...models.get_access_token_response_200 import GetAccessTokenResponse200
from ...models.password_request import PasswordRequest
from ...models.refresh_request import RefreshRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union["ClientCredentialsRequest", "PasswordRequest", "RefreshRequest"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/access_token",
    }

    _body = body.to_dict()

    _kwargs["data"] = _body
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetAccessTokenResponse200]]:
    if response.status_code == 200:
        response_200 = GetAccessTokenResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetAccessTokenResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["ClientCredentialsRequest", "PasswordRequest", "RefreshRequest"],
) -> Response[Union[ErrorResponse, GetAccessTokenResponse200]]:
    """Request access token

     Get an access token to use in the Authorization header for all other requests. See the
    [Authentication](#authentication) section for more information.

    Args:
        body (Union['ClientCredentialsRequest', 'PasswordRequest', 'RefreshRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetAccessTokenResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["ClientCredentialsRequest", "PasswordRequest", "RefreshRequest"],
) -> Optional[Union[ErrorResponse, GetAccessTokenResponse200]]:
    """Request access token

     Get an access token to use in the Authorization header for all other requests. See the
    [Authentication](#authentication) section for more information.

    Args:
        body (Union['ClientCredentialsRequest', 'PasswordRequest', 'RefreshRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetAccessTokenResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["ClientCredentialsRequest", "PasswordRequest", "RefreshRequest"],
) -> Response[Union[ErrorResponse, GetAccessTokenResponse200]]:
    """Request access token

     Get an access token to use in the Authorization header for all other requests. See the
    [Authentication](#authentication) section for more information.

    Args:
        body (Union['ClientCredentialsRequest', 'PasswordRequest', 'RefreshRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetAccessTokenResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["ClientCredentialsRequest", "PasswordRequest", "RefreshRequest"],
) -> Optional[Union[ErrorResponse, GetAccessTokenResponse200]]:
    """Request access token

     Get an access token to use in the Authorization header for all other requests. See the
    [Authentication](#authentication) section for more information.

    Args:
        body (Union['ClientCredentialsRequest', 'PasswordRequest', 'RefreshRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetAccessTokenResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
