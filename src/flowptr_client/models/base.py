from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class ShotgridEntity(BaseModel):
    """Base class for Shotgrid entities"""

    id: int
    type: str
    attributes: dict[str, Any]
    created_at: datetime
    updated_at: datetime


class PaginationParams(BaseModel):
    """Pagination parameters"""

    size: Optional[int] = None
    number: Optional[int] = None


class FilterParams(BaseModel):
    """Filter parameters"""

    filters: dict[str, Any] = Field(default_factory=dict)
    fields: list[str] = Field(default_factory=list)
    sort: list[str] = Field(default_factory=list)
    page: Optional[PaginationParams] = None
