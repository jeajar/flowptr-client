from typing import Any, Optional

from .base import BaseRoute


class SchemaRoute(BaseRoute):
    """Route handler for Flow PT schema endpoints."""

    base_route: str = "/schema"

    async def get_entity(
        self, entity_type: str, project_id: Optional[int] = None
    ) -> dict[str, Any]:
        """Get all field schemas for an entity.

        Args:
            entity_type: Name of entity type in snake_case (e.g. "project", "shot")
            project_id: Optional project ID to get project-specific schema

        Returns:
            Dictionary containing field schemas for the entity
        """
        params = {}
        if project_id is not None:
            params["project_id"] = project_id

        return await self.client.get(f"{self.base_route}{entity_type}", params=params)

    async def get_entity_fields(
        self, entity_type: str, project_id: Optional[int] = None
    ) -> dict[str, Any]:
        """Get schema for a specific field on an entity.

        Args:
            entity_type: Name of entity type in snake_case
            field_name: Name of the field to get schema for
            project_id: Optional project ID to get project-specific schema

        Returns:
            Dictionary containing schema for the specified field
        """
        params = {}
        if project_id is not None:
            params["project_id"] = project_id

        return await self.client.get(
            f"{self.base_route}{entity_type}/fields", params=params
        )
