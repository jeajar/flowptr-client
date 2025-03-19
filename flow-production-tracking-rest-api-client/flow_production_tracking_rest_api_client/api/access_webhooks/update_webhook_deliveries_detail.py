from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_delivery_request import UpdateDeliveryRequest
from ...types import Response


def _get_kwargs(
    record_uuid: str,
    *,
    body: UpdateDeliveryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/webhook/deliveries/{record_uuid}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Union[Any, ErrorResponse]]:
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
    body: UpdateDeliveryRequest,
) -> Response[Union[Any, ErrorResponse]]:
    """Update a Delivery

     Update a delivery detail.

    Args:
        record_uuid (str):
        body (UpdateDeliveryRequest):  Example: {'acknowledgement': 'My acknowledgement string or
            stringified JSON.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        record_uuid=record_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    record_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDeliveryRequest,
) -> Optional[Union[Any, ErrorResponse]]:
    """Update a Delivery

     Update a delivery detail.

    Args:
        record_uuid (str):
        body (UpdateDeliveryRequest):  Example: {'acknowledgement': 'My acknowledgement string or
            stringified JSON.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        record_uuid=record_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    record_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDeliveryRequest,
) -> Response[Union[Any, ErrorResponse]]:
    """Update a Delivery

     Update a delivery detail.

    Args:
        record_uuid (str):
        body (UpdateDeliveryRequest):  Example: {'acknowledgement': 'My acknowledgement string or
            stringified JSON.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        record_uuid=record_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    record_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDeliveryRequest,
) -> Optional[Union[Any, ErrorResponse]]:
    """Update a Delivery

     Update a delivery detail.

    Args:
        record_uuid (str):
        body (UpdateDeliveryRequest):  Example: {'acknowledgement': 'My acknowledgement string or
            stringified JSON.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            record_uuid=record_uuid,
            client=client,
            body=body,
        )
    ).parsed
