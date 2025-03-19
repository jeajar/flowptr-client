from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.revive_entity_record_response_200 import ReviveEntityRecordResponse200
from ...types import UNSET, Response


def _get_kwargs(
    entity: str,
    record_id: int,
    *,
    revive: bool = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["revive"] = revive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/entity/{entity}/{record_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ReviveEntityRecordResponse200]]:
    if response.status_code == 200:
        response_200 = ReviveEntityRecordResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ReviveEntityRecordResponse200]]:
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
    revive: bool = True,
) -> Response[Union[ErrorResponse, ReviveEntityRecordResponse200]]:
    """Revive a record

     The endpoint revives a single entity record.

    Args:
        entity (str):
        record_id (int):
        revive (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ReviveEntityRecordResponse200]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        revive=revive,
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
    revive: bool = True,
) -> Optional[Union[ErrorResponse, ReviveEntityRecordResponse200]]:
    """Revive a record

     The endpoint revives a single entity record.

    Args:
        entity (str):
        record_id (int):
        revive (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ReviveEntityRecordResponse200]
    """

    return sync_detailed(
        entity=entity,
        record_id=record_id,
        client=client,
        revive=revive,
    ).parsed


async def asyncio_detailed(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    revive: bool = True,
) -> Response[Union[ErrorResponse, ReviveEntityRecordResponse200]]:
    """Revive a record

     The endpoint revives a single entity record.

    Args:
        entity (str):
        record_id (int):
        revive (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ReviveEntityRecordResponse200]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        revive=revive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    revive: bool = True,
) -> Optional[Union[ErrorResponse, ReviveEntityRecordResponse200]]:
    """Revive a record

     The endpoint revives a single entity record.

    Args:
        entity (str):
        record_id (int):
        revive (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ReviveEntityRecordResponse200]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            record_id=record_id,
            client=client,
            revive=revive,
        )
    ).parsed
