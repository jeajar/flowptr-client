from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_field_request import CreateFieldRequest
from ...models.error_response import ErrorResponse
from ...models.schema_field_response import SchemaFieldResponse
from ...types import Response


def _get_kwargs(
    entity: str,
    *,
    body: CreateFieldRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/schema/{entity}/fields",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SchemaFieldResponse]]:
    if response.status_code == 201:
        response_201 = SchemaFieldResponse.from_dict(response.json())

        return response_201
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, SchemaFieldResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFieldRequest,
) -> Response[Union[ErrorResponse, SchemaFieldResponse]]:
    """Create new field on entity

     Creates a new field on the given entity

    Args:
        entity (str):
        body (CreateFieldRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SchemaFieldResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFieldRequest,
) -> Optional[Union[ErrorResponse, SchemaFieldResponse]]:
    """Create new field on entity

     Creates a new field on the given entity

    Args:
        entity (str):
        body (CreateFieldRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SchemaFieldResponse]
    """

    return sync_detailed(
        entity=entity,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFieldRequest,
) -> Response[Union[ErrorResponse, SchemaFieldResponse]]:
    """Create new field on entity

     Creates a new field on the given entity

    Args:
        entity (str):
        body (CreateFieldRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SchemaFieldResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFieldRequest,
) -> Optional[Union[ErrorResponse, SchemaFieldResponse]]:
    """Create new field on entity

     Creates a new field on the given entity

    Args:
        entity (str):
        body (CreateFieldRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SchemaFieldResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            client=client,
            body=body,
        )
    ).parsed
