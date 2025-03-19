from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.options_parameter import OptionsParameter
from ...models.relationships_response import RelationshipsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity: str,
    record_id: int,
    related_field: str,
    *,
    options: Union[Unset, "OptionsParameter"] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_options: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(options, Unset):
        json_options = options.to_dict()
    if not isinstance(json_options, Unset):
        params.update(json_options)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/entity/{entity}/{record_id}/relationships/{related_field}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, RelationshipsResponse]]:
    if response.status_code == 200:
        response_200 = RelationshipsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, RelationshipsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity: str,
    record_id: int,
    related_field: str,
    *,
    client: Union[AuthenticatedClient, Client],
    options: Union[Unset, "OptionsParameter"] = UNSET,
) -> Response[Union[ErrorResponse, RelationshipsResponse]]:
    """Read record relationship

     The endpoint provides access to records related to the current entity record via the a `Entity` or
    `Multi-Entity` field.

    Args:
        entity (str):
        record_id (int):
        related_field (str):
        options (Union[Unset, OptionsParameter]):  Example: {'include_archived_projects': False,
            'return_only': 'active'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RelationshipsResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        related_field=related_field,
        options=options,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: str,
    record_id: int,
    related_field: str,
    *,
    client: Union[AuthenticatedClient, Client],
    options: Union[Unset, "OptionsParameter"] = UNSET,
) -> Optional[Union[ErrorResponse, RelationshipsResponse]]:
    """Read record relationship

     The endpoint provides access to records related to the current entity record via the a `Entity` or
    `Multi-Entity` field.

    Args:
        entity (str):
        record_id (int):
        related_field (str):
        options (Union[Unset, OptionsParameter]):  Example: {'include_archived_projects': False,
            'return_only': 'active'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RelationshipsResponse]
    """

    return sync_detailed(
        entity=entity,
        record_id=record_id,
        related_field=related_field,
        client=client,
        options=options,
    ).parsed


async def asyncio_detailed(
    entity: str,
    record_id: int,
    related_field: str,
    *,
    client: Union[AuthenticatedClient, Client],
    options: Union[Unset, "OptionsParameter"] = UNSET,
) -> Response[Union[ErrorResponse, RelationshipsResponse]]:
    """Read record relationship

     The endpoint provides access to records related to the current entity record via the a `Entity` or
    `Multi-Entity` field.

    Args:
        entity (str):
        record_id (int):
        related_field (str):
        options (Union[Unset, OptionsParameter]):  Example: {'include_archived_projects': False,
            'return_only': 'active'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RelationshipsResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        related_field=related_field,
        options=options,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    record_id: int,
    related_field: str,
    *,
    client: Union[AuthenticatedClient, Client],
    options: Union[Unset, "OptionsParameter"] = UNSET,
) -> Optional[Union[ErrorResponse, RelationshipsResponse]]:
    """Read record relationship

     The endpoint provides access to records related to the current entity record via the a `Entity` or
    `Multi-Entity` field.

    Args:
        entity (str):
        record_id (int):
        related_field (str):
        options (Union[Unset, OptionsParameter]):  Example: {'include_archived_projects': False,
            'return_only': 'active'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RelationshipsResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            record_id=record_id,
            related_field=related_field,
            client=client,
            options=options,
        )
    ).parsed
