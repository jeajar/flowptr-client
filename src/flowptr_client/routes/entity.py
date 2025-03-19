from collections.abc import Sequence
from typing import Any, Generic, Optional, TypeVar, Union

from flowptr_client.application.interfaces import FlowPTRClientInterface

from ..domain.value_objects.filter import ComplexFilter, FilterCondition
from ..domain.value_objects.pagination import PageParams

T = TypeVar("T")


class EntityRoute(Generic[T]):
    """Base entity route implementation for Flow PT REST API."""

    base_route: str = "/entity/"

    def __init__(self, client: FlowPTRClientInterface):
        self.client = client

    async def get(
        self,
        entity: str,
        filters: Optional[Sequence[FilterCondition]] = None,
        fields: Optional[Sequence[str]] = None,
        sort: Optional[Sequence[str]] = None,
        page: Optional[PageParams] = None,
    ) -> dict[str, Any]:
        """Get entities matching criteria using array-style filters."""
        params = self._build_params(filters, fields, sort, page)
        return await self.client.get(f"{self.base_route}{entity}", params=params)

    async def search(
        self,
        entity: str,
        filters: Union[Sequence[FilterCondition], ComplexFilter],
        fields: Optional[Sequence[str]] = None,
        sort: Optional[Sequence[str]] = None,
        page: Optional[PageParams] = None,
    ) -> dict[str, Any]:
        """Search entities with complex filters."""
        params = self._build_params(fields=fields, sort=sort, page=page)

        # Convert filters to Flow PT format
        if isinstance(filters, ComplexFilter):
            # Hash style format
            filter_data = {
                "filters": {
                    "logical_operator": filters.logical_operator,
                    "conditions": [
                        self._convert_filter_condition(c)
                        if isinstance(c, FilterCondition)
                        else self._convert_complex_filter(c)
                        for c in filters.conditions
                    ],
                }
            }
            headers = {"Content-Type": "application/vnd+shotgun.api3_hash+json"}
        else:
            # Array style format
            filter_data = {
                "filters": [self._convert_filter_condition(f) for f in filters]
            }
            headers = {"Content-Type": "application/vnd+shotgun.api3_array+json"}

        return await self.client.post(
            f"{self.base_route}{entity}/_search",
            json=filter_data,
            params=params,
            headers=headers,
        )

    def _convert_filter_condition(self, condition: FilterCondition) -> list:
        """Convert FilterCondition to Flow PT format."""
        return [condition.field, condition.relation, condition.value]

    def _convert_complex_filter(self, filter_: ComplexFilter) -> dict:
        """Convert ComplexFilter to Flow PT format."""
        return {
            "logical_operator": filter_.logical_operator,
            "conditions": [
                self._convert_filter_condition(c)
                if isinstance(c, FilterCondition)
                else self._convert_complex_filter(c)
                for c in filter_.conditions
            ],
        }

    def _build_params(
        self,
        filters: Optional[Sequence[FilterCondition]] = None,
        fields: Optional[Sequence[str]] = None,
        sort: Optional[Sequence[str]] = None,
        page: Optional[PageParams] = None,
    ) -> dict[str, Any]:
        """Build query parameters according to Flow PT specs."""
        params: dict[str, Any] = {}

        if filters:
            # Convert simple filters to query params format
            for condition in filters:
                params[f"filter[{condition.field}]"] = condition.value

        if fields:
            params["fields"] = ",".join(fields)

        if sort:
            params["sort"] = ",".join(sort)

        if page:
            params["page[size]"] = page.size
            if page.number is not None:
                params["page[number]"] = page.number

        return params
