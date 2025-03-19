from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_entity_last_accessed_body import UpdateEntityLastAccessedBody
from ...models.update_entity_last_accessed_response_200 import UpdateEntityLastAccessedResponse200
from ...types import Response


def _get_kwargs(
    record_id: int,
    *,
    body: UpdateEntityLastAccessedBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/entity/projects/{record_id}/_update_last_accessed",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateEntityLastAccessedResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateEntityLastAccessedResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, UpdateEntityLastAccessedResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntityLastAccessedBody,
) -> Response[Union[ErrorResponse, UpdateEntityLastAccessedResponse200]]:
    """Update the last accessed time

     The endpoint updates the last access time of a project by a user

    Args:
        record_id (int):
        body (UpdateEntityLastAccessedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateEntityLastAccessedResponse200]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntityLastAccessedBody,
) -> Optional[Union[ErrorResponse, UpdateEntityLastAccessedResponse200]]:
    """Update the last accessed time

     The endpoint updates the last access time of a project by a user

    Args:
        record_id (int):
        body (UpdateEntityLastAccessedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateEntityLastAccessedResponse200]
    """

    return sync_detailed(
        record_id=record_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntityLastAccessedBody,
) -> Response[Union[ErrorResponse, UpdateEntityLastAccessedResponse200]]:
    """Update the last accessed time

     The endpoint updates the last access time of a project by a user

    Args:
        record_id (int):
        body (UpdateEntityLastAccessedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateEntityLastAccessedResponse200]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntityLastAccessedBody,
) -> Optional[Union[ErrorResponse, UpdateEntityLastAccessedResponse200]]:
    """Update the last accessed time

     The endpoint updates the last access time of a project by a user

    Args:
        record_id (int):
        body (UpdateEntityLastAccessedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateEntityLastAccessedResponse200]
    """

    return (
        await asyncio_detailed(
            record_id=record_id,
            client=client,
            body=body,
        )
    ).parsed
