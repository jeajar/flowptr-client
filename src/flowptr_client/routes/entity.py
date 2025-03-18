from dataclasses import dataclass
from typing import Any, Generic, Optional, TypedDict, TypeVar

T = TypeVar("T")


@dataclass
class PageParams:
    size: int
    number: Optional[int] = None


class EntityData(TypedDict):
    id: int
    type: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]


class EntityRoute(Generic[T]):
    """Base entity route implementation for ShotGrid/Flow REST API"""

    base_route: str = "/entity/"

    def __init__(self, client, entity_type: str):
        self.client = client
        self.entity_type = entity_type

    async def get(
        self,
        filters: Optional[dict[str, Any]] = None,
        fields: Optional[list[str]] = None,
        sort: Optional[list[str]] = None,
        page: Optional[PageParams] = None,
    ) -> dict[str, Any]:
        """Get entities matching criteria"""
        params = self._build_params(filters, fields, sort, page)
        return await self.client.get(
            f"{self.base_route}{self.entity_type}", params=params
        )

    async def get_by_id(
        self, entity_id: int, fields: Optional[list[str]] = None
    ) -> EntityData:
        """Get single entity by ID"""
        params = self._build_params(fields=fields)
        return await self.client.get(
            f"{self.base_route}{self.entity_type}/{entity_id}", params=params
        )

    async def search(
        self,
        filters: dict[str, Any],
        fields: Optional[list[str]] = None,
        sort: Optional[list[str]] = None,
        page: Optional[PageParams] = None,
    ) -> dict[str, Any]:
        """Search entities with complex filters"""
        params = self._build_params(fields=fields, sort=sort, page=page)
        return await self.client.post(
            f"{self.base_route}{self.entity_type}/_search",
            json={"filters": filters},
            params=params,
        )

    async def summarize(
        self,
        filters: dict[str, Any],
        summary_fields: list[str],
        grouping: Optional[list[str]] = None,
    ) -> dict[str, Any]:
        """Get summary of entity fields with optional grouping"""
        data = {"filters": filters, "summary_fields": summary_fields}
        if grouping:
            data["grouping"] = grouping
        return await self.client.post(
            f"{self.base_route}{self.entity_type}/_summarize", json=data
        )

    async def create(self, data: dict[str, Any]) -> dict[str, Any]:
        """Create new entity"""
        return await self.client.post(f"{self.base_route}{self.entity_type}", json=data)

    async def update(self, entity_id: int, data: dict[str, Any]) -> dict[str, Any]:
        """Update existing entity"""
        return await self.client.put(
            f"{self.base_route}{self.entity_type}/{entity_id}", json=data
        )

    async def delete(self, entity_id: int) -> None:
        """Delete entity"""
        await self.client.delete(f"{self.base_route}{self.entity_type}/{entity_id}")

    async def revive(self, entity_id: int) -> dict[str, Any]:
        """Revive deleted entity"""
        return await self.client.put(
            f"{self.base_route}{self.entity_type}/{entity_id}/revive"
        )

    async def get_related(
        self, entity_id: int, relation: str, fields: Optional[list[str]] = None
    ) -> dict[str, Any]:
        """Get related entities"""
        params = self._build_params(fields=fields)
        return await self.client.get(
            f"{self.base_route}{self.entity_type}/{entity_id}/{relation}", params=params
        )

    async def activity_stream(
        self, entity_id: int, limit: Optional[int] = None, cursor: Optional[str] = None
    ) -> dict[str, Any]:
        """Get activity stream for an entity"""
        params = {}
        if limit:
            params["limit"] = limit
        if cursor:
            params["cursor"] = cursor
        return await self.client.get(
            f"{self.base_route}{self.entity_type}/{entity_id}/activity_stream",
            params=params,
        )

    def _build_params(
        self,
        filters: Optional[dict[str, Any]] = None,
        fields: Optional[list[str]] = None,
        sort: Optional[list[str]] = None,
        page: Optional[PageParams] = None,
    ) -> dict[str, Any]:
        """Build query parameters"""
        params: dict[str, Any] = {}

        if filters:
            params.update({f"filter[{k}]": v for k, v in filters.items()})

        if fields:
            params["fields"] = ",".join(fields)

        if sort:
            params["sort"] = ",".join(sort)

        if page:
            params["page[size]"] = page.size
            if page.number is not None:
                params["page[number]"] = page.number

        return params
