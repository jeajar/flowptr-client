"""Request models for Flow Production Tracking REST API.

These models define the structure of request bodies sent to the API.
"""

from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from flowptr_client.models.common import RequestType


class BatchRequestItem(BaseModel):
    """A single operation in a batch request.

    Batch requests allow multiple create, update, or delete operations
    to be executed atomically in a single API call.

    Attributes:
        request_type: Type of operation (create, update, delete)
        entity: Entity type name in plural snake_case (e.g., "projects", "shots")
        record_id: Record ID (required for update and delete)
        data: Field values to set (required for create and update)
        options: Additional options like fields to return
    """

    request_type: RequestType = Field(..., description="Type of batch operation")
    entity: str = Field(..., description="Entity type in plural snake_case")
    record_id: Optional[int] = Field(
        default=None, description="Record ID for update/delete operations"
    )
    data: Optional[dict[str, Any]] = Field(
        default=None, description="Field values for create/update"
    )
    options: Optional[dict[str, Any]] = Field(
        default=None, description="Additional options"
    )

    model_config = ConfigDict(extra="forbid")


class BatchRequest(BaseModel):
    """Request body for batch operations endpoint.

    POST /entity/_batch

    All operations in the batch are executed atomically - either all
    succeed or all fail (transaction rollback).

    Attributes:
        requests: List of operations to execute
    """

    requests: list[BatchRequestItem] = Field(
        ..., min_length=1, description="Operations to execute in batch"
    )

    model_config = ConfigDict(extra="forbid")


class SearchRequestArray(BaseModel):
    """Search request using array-style filters.

    Content-Type: application/vnd+shotgun.api3_array+json

    Array filters are specified as:
    [
        ["field_name", "operator", value],
        ["another_field", "operator", value]
    ]

    Attributes:
        filters: List of filter conditions (each is [field, operator, value])
        fields: Comma-separated list of fields to return (or "*" for all)
        sort: Comma-separated list of fields to sort by (prefix with "-" for descending)
        page: Pagination parameters
    """

    filters: list[list[Any]] = Field(
        default_factory=list, description="Array-style filter conditions"
    )
    fields: Optional[str] = Field(default=None, description="Fields to return")
    sort: Optional[str] = Field(default=None, description="Sort order")
    page: Optional[dict[str, Any]] = Field(
        default=None, description="Pagination params"
    )

    model_config = ConfigDict(extra="forbid")


class SearchRequestHash(BaseModel):
    """Search request using hash-style (complex) filters.

    Content-Type: application/vnd+shotgun.api3_hash+json

    Hash filters support logical operators and nesting:
    {
        "logical_operator": "and",
        "conditions": [
            ["field", "operator", value],
            {
                "logical_operator": "or",
                "conditions": [...]
            }
        ]
    }

    Attributes:
        filters: Complex filter object with logical operators
        fields: Comma-separated list of fields to return (or "*" for all)
        sort: Comma-separated list of fields to sort by (prefix with "-" for descending)
        page: Pagination parameters
    """

    filters: dict[str, Any] = Field(
        default_factory=dict, description="Hash-style complex filters"
    )
    fields: Optional[str] = Field(default=None, description="Fields to return")
    sort: Optional[str] = Field(default=None, description="Sort order")
    page: Optional[dict[str, Any]] = Field(
        default=None, description="Pagination params"
    )

    model_config = ConfigDict(extra="forbid")


class TextSearchRequest(BaseModel):
    """Request body for text search endpoint.

    POST /entity/_text_search

    Performs full-text search across entity fields.

    Attributes:
        text: Search query text
        entity_types: Dict mapping entity types to field restrictions
        sort: Sort order
        page: Pagination parameters
    """

    text: str = Field(..., min_length=1, description="Search query text")
    entity_types: Optional[dict[str, Any]] = Field(
        default=None, description="Entity type restrictions"
    )
    sort: Optional[str] = Field(default=None, description="Sort order")
    page: Optional[dict[str, Any]] = Field(
        default=None, description="Pagination params"
    )

    model_config = ConfigDict(extra="forbid")


class SummarizeRequest(BaseModel):
    """Request body for summarize endpoint.

    POST /entity/{entity}/_summarize

    Performs aggregations on entity data.

    Attributes:
        summary_fields: List of field aggregations to compute
        filters: Optional filters to apply
        grouping: Optional grouping specifications
    """

    summary_fields: list[dict[str, Any]] = Field(
        ..., min_length=1, description="Aggregation specifications"
    )
    filters: Optional[Union[list[list[Any]], dict[str, Any]]] = Field(
        default=None, description="Filter conditions"
    )
    grouping: Optional[list[dict[str, Any]]] = Field(
        default=None, description="Grouping specifications"
    )

    model_config = ConfigDict(extra="forbid")
