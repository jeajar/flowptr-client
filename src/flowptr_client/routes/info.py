from typing import Any

from .base import BaseRoute


class InfoRoute(BaseRoute):
    """Info route for Shotgrid API server.

    Get Spec should probably be moved to a separate route.
    """

    base_route = "/"  # Root route for info.

    def __init__(self, client):
        self.client = client

    async def get_spec(self) -> dict[str, Any]:
        """Get Shotgrid API spec"""
        return await self.client.get(f"{self.base_route}spec.json")

    async def get_info(self) -> dict[str, Any]:
        """Get Shotgrid server info"""
        return await self.client.get(self.base_route)
