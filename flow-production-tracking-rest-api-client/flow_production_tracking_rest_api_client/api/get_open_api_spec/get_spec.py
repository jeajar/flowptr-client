from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_spec_format import GetSpecFormat
from ...models.get_spec_response_200 import GetSpecResponse200
from ...types import Response


def _get_kwargs(
    format_: GetSpecFormat,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/spec.{format_}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSpecResponse200]:
    if response.status_code == 200:
        response_200 = GetSpecResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSpecResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    format_: GetSpecFormat,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetSpecResponse200]:
    """OpenAPI v3 Spec

     The endpoint provides the [OpenAPI v3](https://github.com/OAI/OpenAPI-
    Specification/blob/master/versions/3.0.0.md) specification for a version of the API.

    Args:
        format_ (GetSpecFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSpecResponse200]
    """

    kwargs = _get_kwargs(
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    format_: GetSpecFormat,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetSpecResponse200]:
    """OpenAPI v3 Spec

     The endpoint provides the [OpenAPI v3](https://github.com/OAI/OpenAPI-
    Specification/blob/master/versions/3.0.0.md) specification for a version of the API.

    Args:
        format_ (GetSpecFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSpecResponse200
    """

    return sync_detailed(
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    format_: GetSpecFormat,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetSpecResponse200]:
    """OpenAPI v3 Spec

     The endpoint provides the [OpenAPI v3](https://github.com/OAI/OpenAPI-
    Specification/blob/master/versions/3.0.0.md) specification for a version of the API.

    Args:
        format_ (GetSpecFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSpecResponse200]
    """

    kwargs = _get_kwargs(
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    format_: GetSpecFormat,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetSpecResponse200]:
    """OpenAPI v3 Spec

     The endpoint provides the [OpenAPI v3](https://github.com/OAI/OpenAPI-
    Specification/blob/master/versions/3.0.0.md) specification for a version of the API.

    Args:
        format_ (GetSpecFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSpecResponse200
    """

    return (
        await asyncio_detailed(
            format_=format_,
            client=client,
        )
    ).parsed
