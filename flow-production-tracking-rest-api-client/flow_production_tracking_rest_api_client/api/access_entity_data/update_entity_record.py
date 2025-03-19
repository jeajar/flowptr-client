from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_or_update_request import CreateOrUpdateRequest
from ...models.error_response import ErrorResponse
from ...models.return_fields_options_parameter import ReturnFieldsOptionsParameter
from ...models.single_record_response import SingleRecordResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity: str,
    record_id: int,
    *,
    body: CreateOrUpdateRequest,
    options: Union[Unset, "ReturnFieldsOptionsParameter"] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_options: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(options, Unset):
        json_options = options.to_dict()
    if not isinstance(json_options, Unset):
        params.update(json_options)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/entity/{entity}/{record_id}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SingleRecordResponse]]:
    if response.status_code == 200:
        response_200 = SingleRecordResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SingleRecordResponse]]:
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
    body: CreateOrUpdateRequest,
    options: Union[Unset, "ReturnFieldsOptionsParameter"] = UNSET,
) -> Response[Union[ErrorResponse, SingleRecordResponse]]:
    """Update an existing record

     The endpoint updates a single entity record. For more information on updating a multi-entity field
    with this endpoint, see the [multi-enity update](#updating-a-multi-entity-field) section.

    Args:
        entity (str):
        record_id (int):
        options (Union[Unset, ReturnFieldsOptionsParameter]):  Example: {'options[fields]':
            'field_1,field_2'}.
        body (CreateOrUpdateRequest): This object should contain the key value pairs for the
            fields you want to set. Example: {'name': 'Red Sun', 'users': [{'id': 19, 'name': 'Artist
            1', 'type': 'HumanUser'}, {'id': 18, 'name': 'Artist 2', 'type': 'HumanUser'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SingleRecordResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        body=body,
        options=options,
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
    body: CreateOrUpdateRequest,
    options: Union[Unset, "ReturnFieldsOptionsParameter"] = UNSET,
) -> Optional[Union[ErrorResponse, SingleRecordResponse]]:
    """Update an existing record

     The endpoint updates a single entity record. For more information on updating a multi-entity field
    with this endpoint, see the [multi-enity update](#updating-a-multi-entity-field) section.

    Args:
        entity (str):
        record_id (int):
        options (Union[Unset, ReturnFieldsOptionsParameter]):  Example: {'options[fields]':
            'field_1,field_2'}.
        body (CreateOrUpdateRequest): This object should contain the key value pairs for the
            fields you want to set. Example: {'name': 'Red Sun', 'users': [{'id': 19, 'name': 'Artist
            1', 'type': 'HumanUser'}, {'id': 18, 'name': 'Artist 2', 'type': 'HumanUser'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SingleRecordResponse]
    """

    return sync_detailed(
        entity=entity,
        record_id=record_id,
        client=client,
        body=body,
        options=options,
    ).parsed


async def asyncio_detailed(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateOrUpdateRequest,
    options: Union[Unset, "ReturnFieldsOptionsParameter"] = UNSET,
) -> Response[Union[ErrorResponse, SingleRecordResponse]]:
    """Update an existing record

     The endpoint updates a single entity record. For more information on updating a multi-entity field
    with this endpoint, see the [multi-enity update](#updating-a-multi-entity-field) section.

    Args:
        entity (str):
        record_id (int):
        options (Union[Unset, ReturnFieldsOptionsParameter]):  Example: {'options[fields]':
            'field_1,field_2'}.
        body (CreateOrUpdateRequest): This object should contain the key value pairs for the
            fields you want to set. Example: {'name': 'Red Sun', 'users': [{'id': 19, 'name': 'Artist
            1', 'type': 'HumanUser'}, {'id': 18, 'name': 'Artist 2', 'type': 'HumanUser'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SingleRecordResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        record_id=record_id,
        body=body,
        options=options,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateOrUpdateRequest,
    options: Union[Unset, "ReturnFieldsOptionsParameter"] = UNSET,
) -> Optional[Union[ErrorResponse, SingleRecordResponse]]:
    """Update an existing record

     The endpoint updates a single entity record. For more information on updating a multi-entity field
    with this endpoint, see the [multi-enity update](#updating-a-multi-entity-field) section.

    Args:
        entity (str):
        record_id (int):
        options (Union[Unset, ReturnFieldsOptionsParameter]):  Example: {'options[fields]':
            'field_1,field_2'}.
        body (CreateOrUpdateRequest): This object should contain the key value pairs for the
            fields you want to set. Example: {'name': 'Red Sun', 'users': [{'id': 19, 'name': 'Artist
            1', 'type': 'HumanUser'}, {'id': 18, 'name': 'Artist 2', 'type': 'HumanUser'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SingleRecordResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            record_id=record_id,
            client=client,
            body=body,
            options=options,
        )
    ).parsed
