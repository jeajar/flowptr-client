from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_field_upload_body import PostFieldUploadBody
from ...types import UNSET, Response


def _get_kwargs(
    entity: str,
    record_id: int,
    field_name: str,
    *,
    body: PostFieldUploadBody,
    filename: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["filename"] = filename

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/entity/{entity}/{record_id}/{field_name}/_upload",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
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
    entity: str,
    record_id: int,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostFieldUploadBody,
    filename: str,
) -> Response[Union[Any, ErrorResponse]]:
    """Complete upload for field

     This endpoint links an upload to a field on a record. The information sent to it is the response
    data from the request to get an upload URL and the upload request.

    Args:
        entity (str):
        record_id (int):
        field_name (str):
        filename (str):
        body (PostFieldUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        field_name=field_name,
        body=body,
        filename=filename,
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
    body: PostFieldUploadBody,
    filename: str,
) -> Optional[Union[Any, ErrorResponse]]:
    """Complete upload for field

     This endpoint links an upload to a field on a record. The information sent to it is the response
    data from the request to get an upload URL and the upload request.

    Args:
        entity (str):
        record_id (int):
        field_name (str):
        filename (str):
        body (PostFieldUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        entity=entity,
        record_id=record_id,
        field_name=field_name,
        client=client,
        body=body,
        filename=filename,
    ).parsed


async def asyncio_detailed(
    entity: str,
    record_id: int,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostFieldUploadBody,
    filename: str,
) -> Response[Union[Any, ErrorResponse]]:
    """Complete upload for field

     This endpoint links an upload to a field on a record. The information sent to it is the response
    data from the request to get an upload URL and the upload request.

    Args:
        entity (str):
        record_id (int):
        field_name (str):
        filename (str):
        body (PostFieldUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        field_name=field_name,
        body=body,
        filename=filename,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    record_id: int,
    field_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostFieldUploadBody,
    filename: str,
) -> Optional[Union[Any, ErrorResponse]]:
    """Complete upload for field

     This endpoint links an upload to a field on a record. The information sent to it is the response
    data from the request to get an upload URL and the upload request.

    Args:
        entity (str):
        record_id (int):
        field_name (str):
        filename (str):
        body (PostFieldUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            record_id=record_id,
            field_name=field_name,
            client=client,
            body=body,
            filename=filename,
        )
    ).parsed
