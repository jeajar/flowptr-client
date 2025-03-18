from typing import Any

from flowptr_client.client import FlowPTRClient
from flowptr_client.routes import EntityRoute, InfoRoute


class FlowPTRAPI:
    """Main interface for interacting with the Flow Production Tracking API"""

    def __init__(self):
        self._client = FlowPTRClient()
        self._info = InfoRoute(self._client)

    async def get_server_info(self) -> dict[str, Any]:
        """Get Shotgrid server information"""
        return await self._info.get_info()

    async def get_api_spec(self) -> dict[str, Any]:
        """Get OpenAPI specification"""
        return await self._info.get_spec()

    def entity(self, entity_type: str) -> EntityRoute:
        """Get route handler for specific entity type

        Args:
            entity_type: The type of entity to handle (e.g. "projects", "shots", etc.)

        Returns:
            EntityRoute handler for the specified entity type
        """
        return EntityRoute(self._client, entity_type)

    async def close(self) -> None:
        """Close client connections"""
        await self._client.client.aclose()


async def main():
    api = FlowPTRAPI()
    info = await api.get_server_info()
    print(info)

    spec = await api.get_api_spec()
    print(spec)

    projects = await api.entity("projects").get()
    print(projects)

    await api.close()


if __name__ == "__main__":
    import asyncio

    from rich import print

    asyncio.run(main())
