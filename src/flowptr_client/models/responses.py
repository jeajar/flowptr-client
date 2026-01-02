"""Response models for Flow Production Tracking REST API.

These models follow the JSONAPI specification used by the Shotgrid REST API.
All responses conform to the JSONAPI structure with data, links, and error objects.
"""

from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field


class SelfLink(BaseModel):
    """Self-referential link to the current resource.

    Attributes:
        self_: URL to the current resource
    """

    self_: str = Field(..., alias="self")

    model_config = ConfigDict(populate_by_name=True)


class PaginationLinks(BaseModel):
    """Pagination links for navigating through result pages.

    Attributes:
        self_: URL to the current page
        next: URL to the next page (None if on last page)
        prev: URL to the previous page (None if on first page)
    """

    self_: str = Field(..., alias="self")
    next: Optional[str] = None
    prev: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class Record(BaseModel):
    """A JSONAPI record representing an entity from Flow Production Tracking.

    This is the core data structure returned by the API. Each record contains:
    - Unique identifier and type
    - Non-relational field values in attributes
    - Entity/multi-entity relationships
    - Self-referential link

    Attributes:
        id: Unique record identifier
        type: Entity type (e.g., "Project", "Shot", "Asset")
        attributes: Non-relational field values as key-value pairs
        relationships: Related entities and multi-entity fields
        links: Self-referential link to this record
    """

    id: int
    type: str
    attributes: dict[str, Any] = Field(default_factory=dict)
    relationships: dict[str, Any] = Field(default_factory=dict)
    links: Optional[SelfLink] = None

    model_config = ConfigDict(extra="allow")


class SingleRecordResponse(BaseModel):
    """API response containing a single record.

    Returned by operations that work with a single entity:
    - GET /entity/{entity}/{record_id}
    - POST /entity/{entity} (create)
    - PUT /entity/{entity}/{record_id} (update)

    Attributes:
        data: The record data
        links: Self-referential link to this resource
    """

    data: Record
    links: Optional[SelfLink] = None

    model_config = ConfigDict(extra="allow")


class PaginatedRecordResponse(BaseModel):
    """API response containing multiple records with pagination.

    Returned by operations that return lists:
    - GET /entity/{entity}
    - POST /entity/{entity}/_search
    - POST /entity/_text_search

    Attributes:
        data: List of records
        links: Pagination links for navigating result pages
    """

    data: list[Record]
    links: Optional[PaginationLinks] = None

    model_config = ConfigDict(extra="allow")


class BatchedRequestsResponse(BaseModel):
    """Response from batch operations endpoint.

    Batch operations are atomic - all operations succeed or all fail.
    The response contains the results for each operation in the batch.

    Returned by:
    - POST /entity/_batch

    Attributes:
        data: List of records created/updated by the batch operation
    """

    data: list[Record]

    model_config = ConfigDict(extra="allow")


class ErrorObject(BaseModel):
    """Individual error object following JSONAPI error structure.

    Attributes:
        id: Unique identifier for this error instance
        status: HTTP status code
        code: Shotgrid-specific error code
        title: Short, human-readable summary of the error
        detail: Detailed explanation of the error
        source: Information about the source of the error (e.g., which field)
        meta: Additional metadata about the error
    """

    id: str
    status: int
    code: Optional[int] = None
    title: str
    detail: Optional[str] = None
    source: Optional[dict[str, Any]] = None
    meta: Optional[dict[str, Any]] = None

    model_config = ConfigDict(extra="allow")


class ErrorResponse(BaseModel):
    """API error response containing one or more errors.

    Returned when a request fails validation or encounters an error.
    May contain multiple error objects if multiple issues were detected.

    Attributes:
        errors: List of error objects describing what went wrong
    """

    errors: list[ErrorObject]

    model_config = ConfigDict(extra="allow")


class InfoResponse(BaseModel):
    """Response from server info endpoint.

    Returned by:
    - GET /

    Contains version information and server details.
    """

    data: dict[str, Any]

    model_config = ConfigDict(extra="allow")


class SchemaResponse(BaseModel):
    """Response from schema endpoints.

    Returned by:
    - GET /schema
    - GET /schema/{entity}
    - GET /schema/{entity}/fields
    - GET /schema/{entity}/fields/{field_name}

    Contains entity and field schema definitions.
    """

    data: dict[str, Any]

    model_config = ConfigDict(extra="allow")
