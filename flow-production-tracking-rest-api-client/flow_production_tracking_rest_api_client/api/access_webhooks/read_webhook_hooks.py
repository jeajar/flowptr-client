from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_webhook_index_response import GetWebhookIndexResponse
from ...models.pagination_parameter import PaginationParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    page: Union[Unset, "PaginationParameter"] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["status"] = status

    params["url"] = url_query

    json_page: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(page, Unset):
        json_page = page.to_dict()
    if not isinstance(json_page, Unset):
        params.update(json_page)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhook/hooks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWebhookIndexResponse]]:
    if response.status_code == 200:
        response_200 = GetWebhookIndexResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWebhookIndexResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    page: Union[Unset, "PaginationParameter"] = UNSET,
) -> Response[Union[ErrorResponse, GetWebhookIndexResponse]]:
    """List Webhooks

     Lists all webhooks that satisfy the given filter.

    Args:
        status (Union[Unset, str]):
        url_query (Union[Unset, str]):
        page (Union[Unset, PaginationParameter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWebhookIndexResponse]]
    """

    kwargs = _get_kwargs(
        status=status,
        url_query=url_query,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    page: Union[Unset, "PaginationParameter"] = UNSET,
) -> Optional[Union[ErrorResponse, GetWebhookIndexResponse]]:
    """List Webhooks

     Lists all webhooks that satisfy the given filter.

    Args:
        status (Union[Unset, str]):
        url_query (Union[Unset, str]):
        page (Union[Unset, PaginationParameter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWebhookIndexResponse]
    """

    return sync_detailed(
        client=client,
        status=status,
        url_query=url_query,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    page: Union[Unset, "PaginationParameter"] = UNSET,
) -> Response[Union[ErrorResponse, GetWebhookIndexResponse]]:
    """List Webhooks

     Lists all webhooks that satisfy the given filter.

    Args:
        status (Union[Unset, str]):
        url_query (Union[Unset, str]):
        page (Union[Unset, PaginationParameter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWebhookIndexResponse]]
    """

    kwargs = _get_kwargs(
        status=status,
        url_query=url_query,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    page: Union[Unset, "PaginationParameter"] = UNSET,
) -> Optional[Union[ErrorResponse, GetWebhookIndexResponse]]:
    """List Webhooks

     Lists all webhooks that satisfy the given filter.

    Args:
        status (Union[Unset, str]):
        url_query (Union[Unset, str]):
        page (Union[Unset, PaginationParameter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWebhookIndexResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            url_query=url_query,
            page=page,
        )
    ).parsed
