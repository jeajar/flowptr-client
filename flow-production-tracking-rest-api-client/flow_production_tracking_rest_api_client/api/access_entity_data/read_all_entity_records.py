from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.options_parameter import OptionsParameter
from ...models.paginated_record_response import PaginatedRecordResponse
from ...models.pagination_parameter import PaginationParameter
from ...models.read_all_entity_records_filter import ReadAllEntityRecordsFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity: str,
    *,
    filter_: Union[Unset, "ReadAllEntityRecordsFilter"] = UNSET,
    fields: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    page: Union[Unset, "PaginationParameter"] = UNSET,
    options: Union[Unset, "OptionsParameter"] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_filter_: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.to_dict()
    if not isinstance(json_filter_, Unset):
        params.update(json_filter_)

    params["fields"] = fields

    params["sort"] = sort

    json_page: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(page, Unset):
        json_page = page.to_dict()
    if not isinstance(json_page, Unset):
        params.update(json_page)

    json_options: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(options, Unset):
        json_options = options.to_dict()
    if not isinstance(json_options, Unset):
        params.update(json_options)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/entity/{entity}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedRecordResponse]]:
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 200:
        response_200 = PaginatedRecordResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, PaginatedRecordResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, "ReadAllEntityRecordsFilter"] = UNSET,
    fields: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    page: Union[Unset, "PaginationParameter"] = UNSET,
    options: Union[Unset, "OptionsParameter"] = UNSET,
) -> Response[Union[ErrorResponse, PaginatedRecordResponse]]:
    """Read all records

     The endpoints retrieves records for a given entity. It allows the use simple filtering op. For more
    information see the [Filtering](#filtering) section.

    Args:
        entity (str):
        filter_ (Union[Unset, ReadAllEntityRecordsFilter]):
        fields (Union[Unset, str]):
        sort (Union[Unset, str]):
        page (Union[Unset, PaginationParameter]):
        options (Union[Unset, OptionsParameter]):  Example: {'include_archived_projects': False,
            'return_only': 'active'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedRecordResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        filter_=filter_,
        fields=fields,
        sort=sort,
        page=page,
        options=options,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, "ReadAllEntityRecordsFilter"] = UNSET,
    fields: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    page: Union[Unset, "PaginationParameter"] = UNSET,
    options: Union[Unset, "OptionsParameter"] = UNSET,
) -> Optional[Union[ErrorResponse, PaginatedRecordResponse]]:
    """Read all records

     The endpoints retrieves records for a given entity. It allows the use simple filtering op. For more
    information see the [Filtering](#filtering) section.

    Args:
        entity (str):
        filter_ (Union[Unset, ReadAllEntityRecordsFilter]):
        fields (Union[Unset, str]):
        sort (Union[Unset, str]):
        page (Union[Unset, PaginationParameter]):
        options (Union[Unset, OptionsParameter]):  Example: {'include_archived_projects': False,
            'return_only': 'active'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedRecordResponse]
    """

    return sync_detailed(
        entity=entity,
        client=client,
        filter_=filter_,
        fields=fields,
        sort=sort,
        page=page,
        options=options,
    ).parsed


async def asyncio_detailed(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, "ReadAllEntityRecordsFilter"] = UNSET,
    fields: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    page: Union[Unset, "PaginationParameter"] = UNSET,
    options: Union[Unset, "OptionsParameter"] = UNSET,
) -> Response[Union[ErrorResponse, PaginatedRecordResponse]]:
    """Read all records

     The endpoints retrieves records for a given entity. It allows the use simple filtering op. For more
    information see the [Filtering](#filtering) section.

    Args:
        entity (str):
        filter_ (Union[Unset, ReadAllEntityRecordsFilter]):
        fields (Union[Unset, str]):
        sort (Union[Unset, str]):
        page (Union[Unset, PaginationParameter]):
        options (Union[Unset, OptionsParameter]):  Example: {'include_archived_projects': False,
            'return_only': 'active'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedRecordResponse]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        filter_=filter_,
        fields=fields,
        sort=sort,
        page=page,
        options=options,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, "ReadAllEntityRecordsFilter"] = UNSET,
    fields: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    page: Union[Unset, "PaginationParameter"] = UNSET,
    options: Union[Unset, "OptionsParameter"] = UNSET,
) -> Optional[Union[ErrorResponse, PaginatedRecordResponse]]:
    """Read all records

     The endpoints retrieves records for a given entity. It allows the use simple filtering op. For more
    information see the [Filtering](#filtering) section.

    Args:
        entity (str):
        filter_ (Union[Unset, ReadAllEntityRecordsFilter]):
        fields (Union[Unset, str]):
        sort (Union[Unset, str]):
        page (Union[Unset, PaginationParameter]):
        options (Union[Unset, OptionsParameter]):  Example: {'include_archived_projects': False,
            'return_only': 'active'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedRecordResponse]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            client=client,
            filter_=filter_,
            fields=fields,
            sort=sort,
            page=page,
            options=options,
        )
    ).parsed
