from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_entity_records_body import BatchEntityRecordsBody
from ...models.batched_requests_response import BatchedRequestsResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: BatchEntityRecordsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/entity/_batch",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BatchedRequestsResponse, ErrorResponse]]:
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 200:
        response_200 = BatchedRequestsResponse.from_dict(response.json())

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
) -> Response[Union[BatchedRequestsResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BatchEntityRecordsBody,
) -> Response[Union[BatchedRequestsResponse, ErrorResponse]]:
    """Batch execute requests

     The endpoint batches the execution of multiple create, update, and delete requests together. For
    more information see the [Batching](#batching) section.

    Args:
        body (BatchEntityRecordsBody):  Example: {'requests': [{'request_type': 'create',
            'entity': 'Project', 'data': {'code': 'new project'}, 'options': {'fields': ['code']}}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BatchedRequestsResponse, ErrorResponse]]
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
    body: BatchEntityRecordsBody,
) -> Optional[Union[BatchedRequestsResponse, ErrorResponse]]:
    """Batch execute requests

     The endpoint batches the execution of multiple create, update, and delete requests together. For
    more information see the [Batching](#batching) section.

    Args:
        body (BatchEntityRecordsBody):  Example: {'requests': [{'request_type': 'create',
            'entity': 'Project', 'data': {'code': 'new project'}, 'options': {'fields': ['code']}}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BatchedRequestsResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BatchEntityRecordsBody,
) -> Response[Union[BatchedRequestsResponse, ErrorResponse]]:
    """Batch execute requests

     The endpoint batches the execution of multiple create, update, and delete requests together. For
    more information see the [Batching](#batching) section.

    Args:
        body (BatchEntityRecordsBody):  Example: {'requests': [{'request_type': 'create',
            'entity': 'Project', 'data': {'code': 'new project'}, 'options': {'fields': ['code']}}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BatchedRequestsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BatchEntityRecordsBody,
) -> Optional[Union[BatchedRequestsResponse, ErrorResponse]]:
    """Batch execute requests

     The endpoint batches the execution of multiple create, update, and delete requests together. For
    more information see the [Batching](#batching) section.

    Args:
        body (BatchEntityRecordsBody):  Example: {'requests': [{'request_type': 'create',
            'entity': 'Project', 'data': {'code': 'new project'}, 'options': {'fields': ['code']}}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BatchedRequestsResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
