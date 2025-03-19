from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_record_upload_multipart_upload_type import GetRecordUploadMultipartUploadType
from ...models.next_upload_part_response import NextUploadPartResponse
from ...types import UNSET, Response


def _get_kwargs(
    entity: str,
    record_id: int,
    *,
    filename: str,
    upload_type: GetRecordUploadMultipartUploadType,
    timestamp: str,
    upload_id: str,
    part_number: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filename"] = filename

    json_upload_type = upload_type.value
    params["upload_type"] = json_upload_type

    params["timestamp"] = timestamp

    params["upload_id"] = upload_id

    params["part_number"] = part_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/entity/{entity}/{record_id}/_upload/multipart",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, NextUploadPartResponse]]:
    if response.status_code == 200:
        response_200 = NextUploadPartResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, NextUploadPartResponse]]:
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
    filename: str,
    upload_type: GetRecordUploadMultipartUploadType,
    timestamp: str,
    upload_id: str,
    part_number: int,
) -> Response[Union[ErrorResponse, NextUploadPartResponse]]:
    """Get the URL for the next part to upload in a multi-part upload for a record

     This endpoint indicates a multi-part upload has been aborted. This is the 'get_next_part' link
    received from the 'Get upload URL' request, when a multi-part upload is specified.

    Args:
        entity (str):
        record_id (int):
        filename (str):
        upload_type (GetRecordUploadMultipartUploadType): The type of upload that the server has
            determined this request is for.
        timestamp (str): The ISO 8601 timestamp of this request.
        upload_id (str): A unique identifier for the upload.
        part_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NextUploadPartResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        filename=filename,
        upload_type=upload_type,
        timestamp=timestamp,
        upload_id=upload_id,
        part_number=part_number,
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
    filename: str,
    upload_type: GetRecordUploadMultipartUploadType,
    timestamp: str,
    upload_id: str,
    part_number: int,
) -> Optional[Union[ErrorResponse, NextUploadPartResponse]]:
    """Get the URL for the next part to upload in a multi-part upload for a record

     This endpoint indicates a multi-part upload has been aborted. This is the 'get_next_part' link
    received from the 'Get upload URL' request, when a multi-part upload is specified.

    Args:
        entity (str):
        record_id (int):
        filename (str):
        upload_type (GetRecordUploadMultipartUploadType): The type of upload that the server has
            determined this request is for.
        timestamp (str): The ISO 8601 timestamp of this request.
        upload_id (str): A unique identifier for the upload.
        part_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NextUploadPartResponse]
    """

    return sync_detailed(
        entity=entity,
        record_id=record_id,
        client=client,
        filename=filename,
        upload_type=upload_type,
        timestamp=timestamp,
        upload_id=upload_id,
        part_number=part_number,
    ).parsed


async def asyncio_detailed(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    filename: str,
    upload_type: GetRecordUploadMultipartUploadType,
    timestamp: str,
    upload_id: str,
    part_number: int,
) -> Response[Union[ErrorResponse, NextUploadPartResponse]]:
    """Get the URL for the next part to upload in a multi-part upload for a record

     This endpoint indicates a multi-part upload has been aborted. This is the 'get_next_part' link
    received from the 'Get upload URL' request, when a multi-part upload is specified.

    Args:
        entity (str):
        record_id (int):
        filename (str):
        upload_type (GetRecordUploadMultipartUploadType): The type of upload that the server has
            determined this request is for.
        timestamp (str): The ISO 8601 timestamp of this request.
        upload_id (str): A unique identifier for the upload.
        part_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, NextUploadPartResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        filename=filename,
        upload_type=upload_type,
        timestamp=timestamp,
        upload_id=upload_id,
        part_number=part_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    filename: str,
    upload_type: GetRecordUploadMultipartUploadType,
    timestamp: str,
    upload_id: str,
    part_number: int,
) -> Optional[Union[ErrorResponse, NextUploadPartResponse]]:
    """Get the URL for the next part to upload in a multi-part upload for a record

     This endpoint indicates a multi-part upload has been aborted. This is the 'get_next_part' link
    received from the 'Get upload URL' request, when a multi-part upload is specified.

    Args:
        entity (str):
        record_id (int):
        filename (str):
        upload_type (GetRecordUploadMultipartUploadType): The type of upload that the server has
            determined this request is for.
        timestamp (str): The ISO 8601 timestamp of this request.
        upload_id (str): A unique identifier for the upload.
        part_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, NextUploadPartResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            record_id=record_id,
            client=client,
            filename=filename,
            upload_type=upload_type,
            timestamp=timestamp,
            upload_id=upload_id,
            part_number=part_number,
        )
    ).parsed
