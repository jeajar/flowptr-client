from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachment_metadata import AttachmentMetadata
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    record_id: int,
    *,
    body: AttachmentMetadata,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/transcode/attachment_metadata/{record_id}",
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
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AttachmentMetadata,
) -> Response[Union[Any, ErrorResponse]]:
    """Add metadata for a transcoded attachment

     Add metadata for an attachment that was transcoded outside of the Flow Production Tracking
    Transcoding service.

    Args:
        record_id (int):
        body (AttachmentMetadata):  Example: {'width': 1920, 'height': 1080,
            'display_aspect_ratio': 1.7778, 'frame_rate': 24.0, 'nb_frames': 1440, 'start_frame': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AttachmentMetadata,
) -> Optional[Union[Any, ErrorResponse]]:
    """Add metadata for a transcoded attachment

     Add metadata for an attachment that was transcoded outside of the Flow Production Tracking
    Transcoding service.

    Args:
        record_id (int):
        body (AttachmentMetadata):  Example: {'width': 1920, 'height': 1080,
            'display_aspect_ratio': 1.7778, 'frame_rate': 24.0, 'nb_frames': 1440, 'start_frame': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        record_id=record_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AttachmentMetadata,
) -> Response[Union[Any, ErrorResponse]]:
    """Add metadata for a transcoded attachment

     Add metadata for an attachment that was transcoded outside of the Flow Production Tracking
    Transcoding service.

    Args:
        record_id (int):
        body (AttachmentMetadata):  Example: {'width': 1920, 'height': 1080,
            'display_aspect_ratio': 1.7778, 'frame_rate': 24.0, 'nb_frames': 1440, 'start_frame': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AttachmentMetadata,
) -> Optional[Union[Any, ErrorResponse]]:
    """Add metadata for a transcoded attachment

     Add metadata for an attachment that was transcoded outside of the Flow Production Tracking
    Transcoding service.

    Args:
        record_id (int):
        body (AttachmentMetadata):  Example: {'width': 1920, 'height': 1080,
            'display_aspect_ratio': 1.7778, 'frame_rate': 24.0, 'nb_frames': 1440, 'start_frame': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            record_id=record_id,
            client=client,
            body=body,
        )
    ).parsed
