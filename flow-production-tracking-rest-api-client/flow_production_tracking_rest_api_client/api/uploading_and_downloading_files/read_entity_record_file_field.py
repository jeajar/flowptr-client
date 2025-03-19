from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.field_hash_response import FieldHashResponse
from ...models.read_entity_record_file_field_alt import ReadEntityRecordFileFieldAlt
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity: str,
    record_id: int,
    field_name: str,
    *,
    alt: Union[Unset, ReadEntityRecordFileFieldAlt] = UNSET,
    range_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(range_, Unset):
        headers["Range"] = range_

    params: dict[str, Any] = {}

    json_alt: Union[Unset, str] = UNSET
    if not isinstance(alt, Unset):
        json_alt = alt.value

    params["alt"] = json_alt

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/entity/{entity}/{record_id}/{field_name}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, FieldHashResponse]]:
    if response.status_code == 200:
        response_200 = FieldHashResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, FieldHashResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity: str,
    record_id: int,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    alt: Union[Unset, ReadEntityRecordFileFieldAlt] = UNSET,
    range_: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, FieldHashResponse]]:
    """Read file field

     The endpoint provides access to information about an image or attachment field. You can optionally
    use the alt query parameter to download the associated image or attachment.

    Args:
        entity (str):
        record_id (int):
        field_name (str):
        alt (Union[Unset, ReadEntityRecordFileFieldAlt]):
        range_ (Union[Unset, str]):  Example: bytes=0-100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FieldHashResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        field_name=field_name,
        alt=alt,
        range_=range_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: str,
    record_id: int,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    alt: Union[Unset, ReadEntityRecordFileFieldAlt] = UNSET,
    range_: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, FieldHashResponse]]:
    """Read file field

     The endpoint provides access to information about an image or attachment field. You can optionally
    use the alt query parameter to download the associated image or attachment.

    Args:
        entity (str):
        record_id (int):
        field_name (str):
        alt (Union[Unset, ReadEntityRecordFileFieldAlt]):
        range_ (Union[Unset, str]):  Example: bytes=0-100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FieldHashResponse]
    """

    return sync_detailed(
        entity=entity,
        record_id=record_id,
        field_name=field_name,
        client=client,
        alt=alt,
        range_=range_,
    ).parsed


async def asyncio_detailed(
    entity: str,
    record_id: int,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    alt: Union[Unset, ReadEntityRecordFileFieldAlt] = UNSET,
    range_: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, FieldHashResponse]]:
    """Read file field

     The endpoint provides access to information about an image or attachment field. You can optionally
    use the alt query parameter to download the associated image or attachment.

    Args:
        entity (str):
        record_id (int):
        field_name (str):
        alt (Union[Unset, ReadEntityRecordFileFieldAlt]):
        range_ (Union[Unset, str]):  Example: bytes=0-100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FieldHashResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        field_name=field_name,
        alt=alt,
        range_=range_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    record_id: int,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    alt: Union[Unset, ReadEntityRecordFileFieldAlt] = UNSET,
    range_: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, FieldHashResponse]]:
    """Read file field

     The endpoint provides access to information about an image or attachment field. You can optionally
    use the alt query parameter to download the associated image or attachment.

    Args:
        entity (str):
        record_id (int):
        field_name (str):
        alt (Union[Unset, ReadEntityRecordFileFieldAlt]):
        range_ (Union[Unset, str]):  Example: bytes=0-100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FieldHashResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            record_id=record_id,
            field_name=field_name,
            client=client,
            alt=alt,
            range_=range_,
        )
    ).parsed
