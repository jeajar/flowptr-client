from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_webhook_request import CreateWebhookRequest
from ...models.error_response import ErrorResponse
from ...models.webhook_record_response import WebhookRecordResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateWebhookRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhook/hooks",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, WebhookRecordResponse]]:
    if response.status_code == 200:
        response_200 = WebhookRecordResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, WebhookRecordResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookRequest,
) -> Response[Union[ErrorResponse, WebhookRecordResponse]]:
    """Create Webhook

     Creates a webhook to receive delivery from the Flow Production Tracking site when entities are
    modified.

    Args:
        body (CreateWebhookRequest):  Example: {'url': 'http://sometargeturl.com', 'entity_types':
            {'Asset': {'create': [], 'update': ['code', 'description']}}, 'token':
            'some_token_to_sign_payload', 'projects': [1, 2], 'name': 'Asset Webhook', 'description':
            "Webhook for Asset creation and updates of 'code' and 'description'", 'validate_ssl_cert':
            True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, WebhookRecordResponse]]
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
    body: CreateWebhookRequest,
) -> Optional[Union[ErrorResponse, WebhookRecordResponse]]:
    """Create Webhook

     Creates a webhook to receive delivery from the Flow Production Tracking site when entities are
    modified.

    Args:
        body (CreateWebhookRequest):  Example: {'url': 'http://sometargeturl.com', 'entity_types':
            {'Asset': {'create': [], 'update': ['code', 'description']}}, 'token':
            'some_token_to_sign_payload', 'projects': [1, 2], 'name': 'Asset Webhook', 'description':
            "Webhook for Asset creation and updates of 'code' and 'description'", 'validate_ssl_cert':
            True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, WebhookRecordResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookRequest,
) -> Response[Union[ErrorResponse, WebhookRecordResponse]]:
    """Create Webhook

     Creates a webhook to receive delivery from the Flow Production Tracking site when entities are
    modified.

    Args:
        body (CreateWebhookRequest):  Example: {'url': 'http://sometargeturl.com', 'entity_types':
            {'Asset': {'create': [], 'update': ['code', 'description']}}, 'token':
            'some_token_to_sign_payload', 'projects': [1, 2], 'name': 'Asset Webhook', 'description':
            "Webhook for Asset creation and updates of 'code' and 'description'", 'validate_ssl_cert':
            True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, WebhookRecordResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookRequest,
) -> Optional[Union[ErrorResponse, WebhookRecordResponse]]:
    """Create Webhook

     Creates a webhook to receive delivery from the Flow Production Tracking site when entities are
    modified.

    Args:
        body (CreateWebhookRequest):  Example: {'url': 'http://sometargeturl.com', 'entity_types':
            {'Asset': {'create': [], 'update': ['code', 'description']}}, 'token':
            'some_token_to_sign_payload', 'projects': [1, 2], 'name': 'Asset Webhook', 'description':
            "Webhook for Asset creation and updates of 'code' and 'description'", 'validate_ssl_cert':
            True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, WebhookRecordResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
