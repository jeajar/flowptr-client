from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_activity_stream_response import EntityActivityStreamResponse
from ...models.entity_fields_parameter import EntityFieldsParameter
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity: str,
    record_id: int,
    *,
    min_id: Union[Unset, int] = UNSET,
    max_id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    entity_fields: Union[Unset, "EntityFieldsParameter"] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["min_id"] = min_id

    params["max_id"] = max_id

    params["limit"] = limit

    json_entity_fields: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(entity_fields, Unset):
        json_entity_fields = entity_fields.to_dict()
    if not isinstance(json_entity_fields, Unset):
        params.update(json_entity_fields)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/entity/{entity}/{record_id}/activity_stream",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EntityActivityStreamResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = EntityActivityStreamResponse.from_dict(response.json())

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
) -> Response[Union[EntityActivityStreamResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    min_id: Union[Unset, int] = UNSET,
    max_id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    entity_fields: Union[Unset, "EntityFieldsParameter"] = UNSET,
) -> Response[Union[EntityActivityStreamResponse, ErrorResponse]]:
    """Read entity activity stream

     The endpoint provides access to the activity stream of an entity.

    Args:
        entity (str):
        record_id (int):
        min_id (Union[Unset, int]):
        max_id (Union[Unset, int]):
        limit (Union[Unset, int]):
        entity_fields (Union[Unset, EntityFieldsParameter]): Indicates which fields to be returned
            when an entity is returned in the payload. Example: {'entity_fields[Asset]': 'fields1,
            fields2', 'entity_fields[Shot]': 'fields1, fields2'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityActivityStreamResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        min_id=min_id,
        max_id=max_id,
        limit=limit,
        entity_fields=entity_fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    min_id: Union[Unset, int] = UNSET,
    max_id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    entity_fields: Union[Unset, "EntityFieldsParameter"] = UNSET,
) -> Optional[Union[EntityActivityStreamResponse, ErrorResponse]]:
    """Read entity activity stream

     The endpoint provides access to the activity stream of an entity.

    Args:
        entity (str):
        record_id (int):
        min_id (Union[Unset, int]):
        max_id (Union[Unset, int]):
        limit (Union[Unset, int]):
        entity_fields (Union[Unset, EntityFieldsParameter]): Indicates which fields to be returned
            when an entity is returned in the payload. Example: {'entity_fields[Asset]': 'fields1,
            fields2', 'entity_fields[Shot]': 'fields1, fields2'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityActivityStreamResponse, ErrorResponse]
    """

    return sync_detailed(
        entity=entity,
        record_id=record_id,
        client=client,
        min_id=min_id,
        max_id=max_id,
        limit=limit,
        entity_fields=entity_fields,
    ).parsed


async def asyncio_detailed(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    min_id: Union[Unset, int] = UNSET,
    max_id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    entity_fields: Union[Unset, "EntityFieldsParameter"] = UNSET,
) -> Response[Union[EntityActivityStreamResponse, ErrorResponse]]:
    """Read entity activity stream

     The endpoint provides access to the activity stream of an entity.

    Args:
        entity (str):
        record_id (int):
        min_id (Union[Unset, int]):
        max_id (Union[Unset, int]):
        limit (Union[Unset, int]):
        entity_fields (Union[Unset, EntityFieldsParameter]): Indicates which fields to be returned
            when an entity is returned in the payload. Example: {'entity_fields[Asset]': 'fields1,
            fields2', 'entity_fields[Shot]': 'fields1, fields2'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityActivityStreamResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        min_id=min_id,
        max_id=max_id,
        limit=limit,
        entity_fields=entity_fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    min_id: Union[Unset, int] = UNSET,
    max_id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    entity_fields: Union[Unset, "EntityFieldsParameter"] = UNSET,
) -> Optional[Union[EntityActivityStreamResponse, ErrorResponse]]:
    """Read entity activity stream

     The endpoint provides access to the activity stream of an entity.

    Args:
        entity (str):
        record_id (int):
        min_id (Union[Unset, int]):
        max_id (Union[Unset, int]):
        limit (Union[Unset, int]):
        entity_fields (Union[Unset, EntityFieldsParameter]): Indicates which fields to be returned
            when an entity is returned in the payload. Example: {'entity_fields[Asset]': 'fields1,
            fields2', 'entity_fields[Shot]': 'fields1, fields2'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityActivityStreamResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            record_id=record_id,
            client=client,
            min_id=min_id,
            max_id=max_id,
            limit=limit,
            entity_fields=entity_fields,
        )
    ).parsed
