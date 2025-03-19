from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assign_subscriptions_body import AssignSubscriptionsBody
from ...models.assign_subscriptions_response_200 import AssignSubscriptionsResponse200
from ...models.assign_subscriptions_response_207 import AssignSubscriptionsResponse207
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AssignSubscriptionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subscription_seat/user_subscriptions",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AssignSubscriptionsResponse200, AssignSubscriptionsResponse207, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AssignSubscriptionsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 207:
        response_207 = AssignSubscriptionsResponse207.from_dict(response.json())

        return response_207
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
) -> Response[Union[AssignSubscriptionsResponse200, AssignSubscriptionsResponse207, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignSubscriptionsBody,
) -> Response[Union[AssignSubscriptionsResponse200, AssignSubscriptionsResponse207, ErrorResponse]]:
    """Assign subscriptions to users

     Assign subscriptions to users using their ID and the subscription string

    Args:
        body (AssignSubscriptionsBody):  Example: {'1554': 'standard', '1588': 'trial'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignSubscriptionsResponse200, AssignSubscriptionsResponse207, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignSubscriptionsBody,
) -> Optional[Union[AssignSubscriptionsResponse200, AssignSubscriptionsResponse207, ErrorResponse]]:
    """Assign subscriptions to users

     Assign subscriptions to users using their ID and the subscription string

    Args:
        body (AssignSubscriptionsBody):  Example: {'1554': 'standard', '1588': 'trial'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignSubscriptionsResponse200, AssignSubscriptionsResponse207, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignSubscriptionsBody,
) -> Response[Union[AssignSubscriptionsResponse200, AssignSubscriptionsResponse207, ErrorResponse]]:
    """Assign subscriptions to users

     Assign subscriptions to users using their ID and the subscription string

    Args:
        body (AssignSubscriptionsBody):  Example: {'1554': 'standard', '1588': 'trial'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignSubscriptionsResponse200, AssignSubscriptionsResponse207, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignSubscriptionsBody,
) -> Optional[Union[AssignSubscriptionsResponse200, AssignSubscriptionsResponse207, ErrorResponse]]:
    """Assign subscriptions to users

     Assign subscriptions to users using their ID and the subscription string

    Args:
        body (AssignSubscriptionsBody):  Example: {'1554': 'standard', '1588': 'trial'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignSubscriptionsResponse200, AssignSubscriptionsResponse207, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
