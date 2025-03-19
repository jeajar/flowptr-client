from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schema_entity_response import SchemaEntityResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity: str,
    *,
    project_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/schema/{entity}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SchemaEntityResponse]]:
    if response.status_code == 200:
        response_200 = SchemaEntityResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SchemaEntityResponse]]:
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
    project_id: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SchemaEntityResponse]]:
    """Read schema for a single entity

     Returns schema information about the given entity.

    Args:
        entity (str):
        project_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SchemaEntityResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    project_id: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SchemaEntityResponse]]:
    """Read schema for a single entity

     Returns schema information about the given entity.

    Args:
        entity (str):
        project_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SchemaEntityResponse]
    """

    return sync_detailed(
        entity=entity,
        client=client,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    project_id: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, SchemaEntityResponse]]:
    """Read schema for a single entity

     Returns schema information about the given entity.

    Args:
        entity (str):
        project_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SchemaEntityResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    project_id: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, SchemaEntityResponse]]:
    """Read schema for a single entity

     Returns schema information about the given entity.

    Args:
        entity (str):
        project_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SchemaEntityResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            client=client,
            project_id=project_id,
        )
    ).parsed
