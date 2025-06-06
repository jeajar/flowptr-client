from dataclasses import dataclass
from typing import Optional


@dataclass
class PageParams:
    """Pagination parameters for Flow PT API."""

    size: int
    number: Optional[int] = None
