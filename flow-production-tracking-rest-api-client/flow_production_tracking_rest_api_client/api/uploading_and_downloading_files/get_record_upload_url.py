from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.upload_info_response import UploadInfoResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity: str,
    record_id: int,
    *,
    filename: str,
    multipart_upload: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filename"] = filename

    params["multipart_upload"] = multipart_upload

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/entity/{entity}/{record_id}/_upload",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UploadInfoResponse]]:
    if response.status_code == 200:
        response_200 = UploadInfoResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UploadInfoResponse]]:
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
    multipart_upload: Union[Unset, bool] = UNSET,
) -> Response[Union[ErrorResponse, UploadInfoResponse]]:
    """Get upload URL for record

     This endpoint provides the information for where an upload should be sent and how to connect the
    upload to a record once it has been uploaded.

    Args:
        entity (str):
        record_id (int):
        filename (str):
        multipart_upload (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UploadInfoResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        filename=filename,
        multipart_upload=multipart_upload,
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
    multipart_upload: Union[Unset, bool] = UNSET,
) -> Optional[Union[ErrorResponse, UploadInfoResponse]]:
    """Get upload URL for record

     This endpoint provides the information for where an upload should be sent and how to connect the
    upload to a record once it has been uploaded.

    Args:
        entity (str):
        record_id (int):
        filename (str):
        multipart_upload (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UploadInfoResponse]
    """

    return sync_detailed(
        entity=entity,
        record_id=record_id,
        client=client,
        filename=filename,
        multipart_upload=multipart_upload,
    ).parsed


async def asyncio_detailed(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    filename: str,
    multipart_upload: Union[Unset, bool] = UNSET,
) -> Response[Union[ErrorResponse, UploadInfoResponse]]:
    """Get upload URL for record

     This endpoint provides the information for where an upload should be sent and how to connect the
    upload to a record once it has been uploaded.

    Args:
        entity (str):
        record_id (int):
        filename (str):
        multipart_upload (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UploadInfoResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        filename=filename,
        multipart_upload=multipart_upload,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    filename: str,
    multipart_upload: Union[Unset, bool] = UNSET,
) -> Optional[Union[ErrorResponse, UploadInfoResponse]]:
    """Get upload URL for record

     This endpoint provides the information for where an upload should be sent and how to connect the
    upload to a record once it has been uploaded.

    Args:
        entity (str):
        record_id (int):
        filename (str):
        multipart_upload (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UploadInfoResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            record_id=record_id,
            client=client,
            filename=filename,
            multipart_upload=multipart_upload,
        )
    ).parsed
