from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_delivery_index_response import GetDeliveryIndexResponse
from ...models.pagination_parameter import PaginationParameter
from ...models.read_webhook_deliveries_status import ReadWebhookDeliveriesStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hook_id: str,
    *,
    page: Union[Unset, "PaginationParameter"] = UNSET,
    status: Union[Unset, ReadWebhookDeliveriesStatus] = UNSET,
    to: Union[Unset, int] = UNSET,
    from_: Union[Unset, int] = UNSET,
    entity_id: Union[Unset, int] = UNSET,
    entity_type: Union[Unset, str] = UNSET,
    acknowledgement: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_page: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(page, Unset):
        json_page = page.to_dict()
    if not isinstance(json_page, Unset):
        params.update(json_page)

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["to"] = to

    params["from"] = from_

    params["entity_id"] = entity_id

    params["entity_type"] = entity_type

    params["acknowledgement"] = acknowledgement

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/webhook/hooks/{hook_id}/deliveries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetDeliveryIndexResponse]]:
    if response.status_code == 200:
        response_200 = GetDeliveryIndexResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetDeliveryIndexResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, "PaginationParameter"] = UNSET,
    status: Union[Unset, ReadWebhookDeliveriesStatus] = UNSET,
    to: Union[Unset, int] = UNSET,
    from_: Union[Unset, int] = UNSET,
    entity_id: Union[Unset, int] = UNSET,
    entity_type: Union[Unset, str] = UNSET,
    acknowledgement: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetDeliveryIndexResponse]]:
    """List Deliveries

     Lists all deliveries that satisfy the given filter.

    Args:
        hook_id (str):
        page (Union[Unset, PaginationParameter]):
        status (Union[Unset, ReadWebhookDeliveriesStatus]):
        to (Union[Unset, int]):
        from_ (Union[Unset, int]):
        entity_id (Union[Unset, int]):
        entity_type (Union[Unset, str]):
        acknowledgement (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetDeliveryIndexResponse]]
    """

    kwargs = _get_kwargs(
        hook_id=hook_id,
        page=page,
        status=status,
        to=to,
        from_=from_,
        entity_id=entity_id,
        entity_type=entity_type,
        acknowledgement=acknowledgement,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, "PaginationParameter"] = UNSET,
    status: Union[Unset, ReadWebhookDeliveriesStatus] = UNSET,
    to: Union[Unset, int] = UNSET,
    from_: Union[Unset, int] = UNSET,
    entity_id: Union[Unset, int] = UNSET,
    entity_type: Union[Unset, str] = UNSET,
    acknowledgement: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetDeliveryIndexResponse]]:
    """List Deliveries

     Lists all deliveries that satisfy the given filter.

    Args:
        hook_id (str):
        page (Union[Unset, PaginationParameter]):
        status (Union[Unset, ReadWebhookDeliveriesStatus]):
        to (Union[Unset, int]):
        from_ (Union[Unset, int]):
        entity_id (Union[Unset, int]):
        entity_type (Union[Unset, str]):
        acknowledgement (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetDeliveryIndexResponse]
    """

    return sync_detailed(
        hook_id=hook_id,
        client=client,
        page=page,
        status=status,
        to=to,
        from_=from_,
        entity_id=entity_id,
        entity_type=entity_type,
        acknowledgement=acknowledgement,
    ).parsed


async def asyncio_detailed(
    hook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, "PaginationParameter"] = UNSET,
    status: Union[Unset, ReadWebhookDeliveriesStatus] = UNSET,
    to: Union[Unset, int] = UNSET,
    from_: Union[Unset, int] = UNSET,
    entity_id: Union[Unset, int] = UNSET,
    entity_type: Union[Unset, str] = UNSET,
    acknowledgement: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetDeliveryIndexResponse]]:
    """List Deliveries

     Lists all deliveries that satisfy the given filter.

    Args:
        hook_id (str):
        page (Union[Unset, PaginationParameter]):
        status (Union[Unset, ReadWebhookDeliveriesStatus]):
        to (Union[Unset, int]):
        from_ (Union[Unset, int]):
        entity_id (Union[Unset, int]):
        entity_type (Union[Unset, str]):
        acknowledgement (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetDeliveryIndexResponse]]
    """

    kwargs = _get_kwargs(
        hook_id=hook_id,
        page=page,
        status=status,
        to=to,
        from_=from_,
        entity_id=entity_id,
        entity_type=entity_type,
        acknowledgement=acknowledgement,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, "PaginationParameter"] = UNSET,
    status: Union[Unset, ReadWebhookDeliveriesStatus] = UNSET,
    to: Union[Unset, int] = UNSET,
    from_: Union[Unset, int] = UNSET,
    entity_id: Union[Unset, int] = UNSET,
    entity_type: Union[Unset, str] = UNSET,
    acknowledgement: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetDeliveryIndexResponse]]:
    """List Deliveries

     Lists all deliveries that satisfy the given filter.

    Args:
        hook_id (str):
        page (Union[Unset, PaginationParameter]):
        status (Union[Unset, ReadWebhookDeliveriesStatus]):
        to (Union[Unset, int]):
        from_ (Union[Unset, int]):
        entity_id (Union[Unset, int]):
        entity_type (Union[Unset, str]):
        acknowledgement (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetDeliveryIndexResponse]
    """

    return (
        await asyncio_detailed(
            hook_id=hook_id,
            client=client,
            page=page,
            status=status,
            to=to,
            from_=from_,
            entity_id=entity_id,
            entity_type=entity_type,
            acknowledgement=acknowledgement,
        )
    ).parsed
