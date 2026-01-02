"""Pagination models for Flow Production Tracking API.

These models define pagination parameters used when querying lists of records.
"""

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PageParams(BaseModel):
    """Pagination parameters for Flow PT API.

    Controls the page size and page number when retrieving lists of entities.
    The API uses 1-based page numbering.

    Examples:
        >>> # Get first page with 100 records
        >>> PageParams(size=100, number=1)
        >>>
        >>> # Get 500 records (default page size)
        >>> PageParams(size=500)

    Attributes:
        size: Number of records per page (1-5000, default 500)
        number: Page number to retrieve (1-based, None for first page)
    """

    size: int = Field(default=500, ge=1, le=5000, description="Records per page")
    number: Optional[int] = Field(
        default=None, ge=1, description="Page number (1-based)"
    )

    model_config = ConfigDict(frozen=True)
