from abc import ABC, abstractmethod
from typing import Any, Optional


class FlowPTRClientInterface(ABC):
    """Interface for Flow Production Tracking REST client."""

    @abstractmethod
    async def get(
        self, endpoint: str, params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """Execute GET request."""
        pass

    @abstractmethod
    async def post(self, endpoint: str, json: dict[str, Any]) -> dict[str, Any]:
        """Execute POST request."""
        pass

    @abstractmethod
    async def put(self, endpoint: str, json: dict[str, Any]) -> dict[str, Any]:
        """Execute PUT request."""
        pass

    @abstractmethod
    async def delete(self, endpoint: str) -> None:
        """Execute DELETE request."""
        pass
