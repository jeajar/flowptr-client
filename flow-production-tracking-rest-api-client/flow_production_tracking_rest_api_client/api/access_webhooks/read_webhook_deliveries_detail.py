from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delivery_record_response import DeliveryRecordResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    record_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/webhook/deliveries/{record_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeliveryRecordResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DeliveryRecordResponse.from_dict(response.json())

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
) -> Response[Union[DeliveryRecordResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    record_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DeliveryRecordResponse, ErrorResponse]]:
    """Get Delivery Details

     Return details about the provided delivery.

    Args:
        record_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeliveryRecordResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        record_uuid=record_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    record_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DeliveryRecordResponse, ErrorResponse]]:
    """Get Delivery Details

     Return details about the provided delivery.

    Args:
        record_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeliveryRecordResponse, ErrorResponse]
    """

    return sync_detailed(
        record_uuid=record_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    record_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DeliveryRecordResponse, ErrorResponse]]:
    """Get Delivery Details

     Return details about the provided delivery.

    Args:
        record_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeliveryRecordResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        record_uuid=record_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    record_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DeliveryRecordResponse, ErrorResponse]]:
    """Get Delivery Details

     Return details about the provided delivery.

    Args:
        record_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeliveryRecordResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            record_uuid=record_uuid,
            client=client,
        )
    ).parsed
