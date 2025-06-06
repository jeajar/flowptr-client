from abc import ABC, abstractmethod
from typing import Any, Optional


class FlowPTRRestAPIClientInterface(ABC):
    """Interface for Flow Production Tracking REST API client."""

    @abstractmethod
    async def get(
        self, endpoint: str, params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """Execute GET request."""

    @abstractmethod
    async def post(self, endpoint: str, json: dict[str, Any]) -> dict[str, Any]:
        """Execute POST request."""

    @abstractmethod
    async def put(self, endpoint: str, json: dict[str, Any]) -> dict[str, Any]:
        """Execute PUT request."""

    @abstractmethod
    async def delete(self, endpoint: str) -> None:
        """Execute DELETE request."""
