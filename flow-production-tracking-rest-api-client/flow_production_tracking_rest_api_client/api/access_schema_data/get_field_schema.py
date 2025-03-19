from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schema_field_response import SchemaFieldResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity: str,
    field_name: str,
    *,
    project_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/schema/{entity}/fields/{field_name}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SchemaFieldResponse]]:
    if response.status_code == 200:
        response_200 = SchemaFieldResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SchemaFieldResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity: str,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    project_id: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SchemaFieldResponse]]:
    """Read one field schema for an entity

     Returns schema information about a specific field on a given entity.

    Args:
        entity (str):
        field_name (str):
        project_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SchemaFieldResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        field_name=field_name,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: str,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    project_id: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SchemaFieldResponse]]:
    """Read one field schema for an entity

     Returns schema information about a specific field on a given entity.

    Args:
        entity (str):
        field_name (str):
        project_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SchemaFieldResponse]
    """

    return sync_detailed(
        entity=entity,
        field_name=field_name,
        client=client,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    entity: str,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    project_id: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SchemaFieldResponse]]:
    """Read one field schema for an entity

     Returns schema information about a specific field on a given entity.

    Args:
        entity (str):
        field_name (str):
        project_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SchemaFieldResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        field_name=field_name,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    project_id: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SchemaFieldResponse]]:
    """Read one field schema for an entity

     Returns schema information about a specific field on a given entity.

    Args:
        entity (str):
        field_name (str):
        project_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SchemaFieldResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            field_name=field_name,
            client=client,
            project_id=project_id,
        )
    ).parsed
