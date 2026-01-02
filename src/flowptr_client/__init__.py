"""FlowPTR (Flow Production Tracking REST API) Client.

A modern async Python client for the Autodesk Shotgrid REST API.
"""

from flowptr_client.api import FlowPTRAPI
from flowptr_client.client import FlowPTRClient
from flowptr_client.config import FlowPTRSettings
from flowptr_client.exceptions import (
    FlowPTRAuthenticationError,
    FlowPTRAuthorizationError,
    FlowPTRConnectionError,
    FlowPTRError,
    FlowPTRHTTPError,
    FlowPTRNotFoundError,
    FlowPTRServerError,
    FlowPTRTimeoutError,
    FlowPTRValidationError,
)
from flowptr_client.models.common import GrantType, RequestType, ReturnOnly
from flowptr_client.models.filter import ComplexFilter, FilterCondition
from flowptr_client.models.pagination import PageParams
from flowptr_client.models.requests import (
    BatchRequest,
    BatchRequestItem,
    SearchRequestArray,
    SearchRequestHash,
    SummarizeRequest,
    TextSearchRequest,
)
from flowptr_client.models.responses import (
    BatchedRequestsResponse,
    ErrorObject,
    ErrorResponse,
    PaginatedRecordResponse,
    PaginationLinks,
    Record,
    SelfLink,
    SingleRecordResponse,
)

# Backwards compatibility - deprecated alias
FlowPTClient = FlowPTRAPI

__version__ = "0.2.0"

__all__ = [
    # Main API
    "FlowPTRAPI",
    # Low-level client
    "FlowPTRClient",
    "FlowPTClient",  # Deprecated - points to FlowPTRAPI
    "FlowPTRSettings",
    # Exceptions
    "FlowPTRError",
    "FlowPTRHTTPError",
    "FlowPTRAuthenticationError",
    "FlowPTRAuthorizationError",
    "FlowPTRNotFoundError",
    "FlowPTRValidationError",
    "FlowPTRServerError",
    "FlowPTRConnectionError",
    "FlowPTRTimeoutError",
    # Models - Common
    "RequestType",
    "GrantType",
    "ReturnOnly",
    # Models - Filters
    "FilterCondition",
    "ComplexFilter",
    # Models - Pagination
    "PageParams",
    # Models - Requests
    "BatchRequestItem",
    "BatchRequest",
    "SearchRequestArray",
    "SearchRequestHash",
    "TextSearchRequest",
    "SummarizeRequest",
    # Models - Responses
    "Record",
    "SelfLink",
    "PaginationLinks",
    "SingleRecordResponse",
    "PaginatedRecordResponse",
    "BatchedRequestsResponse",
    "ErrorObject",
    "ErrorResponse",
]
