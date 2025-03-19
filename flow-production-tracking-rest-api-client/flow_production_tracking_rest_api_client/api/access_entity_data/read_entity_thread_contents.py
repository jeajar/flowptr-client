from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_fields_parameter import EntityFieldsParameter
from ...models.entity_thread_contents_response import EntityThreadContentsResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    record_id: int,
    *,
    entity_fields: Union[Unset, "EntityFieldsParameter"] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_entity_fields: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(entity_fields, Unset):
        json_entity_fields = entity_fields.to_dict()
    if not isinstance(json_entity_fields, Unset):
        params.update(json_entity_fields)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/entity/notes/{record_id}/thread_contents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EntityThreadContentsResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = EntityThreadContentsResponse.from_dict(response.json())

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
) -> Response[Union[EntityThreadContentsResponse, ErrorResponse]]:
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
    entity_fields: Union[Unset, "EntityFieldsParameter"] = UNSET,
) -> Response[Union[EntityThreadContentsResponse, ErrorResponse]]:
    """Read the thread contents for a Note

     The endpoint provides access to the thread content of an entity.  Currently only Note is supported

    Args:
        record_id (int):
        entity_fields (Union[Unset, EntityFieldsParameter]): Indicates which fields to be returned
            when an entity is returned in the payload. Example: {'entity_fields[Asset]': 'fields1,
            fields2', 'entity_fields[Shot]': 'fields1, fields2'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityThreadContentsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        entity_fields=entity_fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    entity_fields: Union[Unset, "EntityFieldsParameter"] = UNSET,
) -> Optional[Union[EntityThreadContentsResponse, ErrorResponse]]:
    """Read the thread contents for a Note

     The endpoint provides access to the thread content of an entity.  Currently only Note is supported

    Args:
        record_id (int):
        entity_fields (Union[Unset, EntityFieldsParameter]): Indicates which fields to be returned
            when an entity is returned in the payload. Example: {'entity_fields[Asset]': 'fields1,
            fields2', 'entity_fields[Shot]': 'fields1, fields2'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityThreadContentsResponse, ErrorResponse]
    """

    return sync_detailed(
        record_id=record_id,
        client=client,
        entity_fields=entity_fields,
    ).parsed


async def asyncio_detailed(
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    entity_fields: Union[Unset, "EntityFieldsParameter"] = UNSET,
) -> Response[Union[EntityThreadContentsResponse, ErrorResponse]]:
    """Read the thread contents for a Note

     The endpoint provides access to the thread content of an entity.  Currently only Note is supported

    Args:
        record_id (int):
        entity_fields (Union[Unset, EntityFieldsParameter]): Indicates which fields to be returned
            when an entity is returned in the payload. Example: {'entity_fields[Asset]': 'fields1,
            fields2', 'entity_fields[Shot]': 'fields1, fields2'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityThreadContentsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        entity_fields=entity_fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    entity_fields: Union[Unset, "EntityFieldsParameter"] = UNSET,
) -> Optional[Union[EntityThreadContentsResponse, ErrorResponse]]:
    """Read the thread contents for a Note

     The endpoint provides access to the thread content of an entity.  Currently only Note is supported

    Args:
        record_id (int):
        entity_fields (Union[Unset, EntityFieldsParameter]): Indicates which fields to be returned
            when an entity is returned in the payload. Example: {'entity_fields[Asset]': 'fields1,
            fields2', 'entity_fields[Shot]': 'fields1, fields2'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityThreadContentsResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            record_id=record_id,
            client=client,
            entity_fields=entity_fields,
        )
    ).parsed
