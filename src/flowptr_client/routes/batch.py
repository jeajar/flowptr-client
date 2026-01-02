"""Batch operations route for Flow Production Tracking API.

This module provides batch operations that allow multiple create, update,
and delete operations to be executed atomically in a single API request.
"""

from typing import Any, Optional

from flowptr_client.models.requests import BatchRequest, BatchRequestItem
from flowptr_client.models.responses import BatchedRequestsResponse

from .base import BaseRoute


class BatchRoute(BaseRoute):
    """Route handler for batch operations.

    Batch operations allow multiple create, update, or delete operations
    to be executed atomically in a single request. All operations succeed
    or all fail (transaction rollback).

    Examples:
        >>> # Execute mixed batch operations
        >>> batch_items = [
        ...     BatchRequestItem(
        ...         request_type="create",
        ...         entity="Project",
        ...         data={"code": "new_project", "name": "New Project"}
        ...     ),
        ...     BatchRequestItem(
        ...         request_type="update",
        ...         entity="Project",
        ...         record_id=123,
        ...         data={"name": "Updated Name"}
        ...     ),
        ...     BatchRequestItem(
        ...         request_type="delete",
        ...         entity="Project",
        ...         record_id=456
        ...     )
        ... ]
        >>> response = await client.batch.execute(batch_items)
        >>>
        >>> # Create multiple records
        >>> records = [
        ...     {"code": "proj1", "name": "Project 1"},
        ...     {"code": "proj2", "name": "Project 2"}
        ... ]
        >>> response = await client.batch.create_many(
        ...     "projects", records, return_fields=["id", "code"]
        ... )
    """

    base_route: str = "/entity/_batch"

    async def execute(
        self,
        requests: list[BatchRequestItem],
    ) -> BatchedRequestsResponse:
        """Execute multiple operations in a single atomic batch request.

        All operations in the batch are executed atomically - either all
        succeed or all fail with a transaction rollback.

        Args:
            requests: List of batch request items (create/update/delete)

        Returns:
            BatchedRequestsResponse containing results for each operation

        Raises:
            FlowPTRValidationError: If request validation fails
            FlowPTRError: If the batch operation fails

        Examples:
            >>> from flowptr_client.models.requests import BatchRequestItem
            >>> items = [
            ...     BatchRequestItem(
            ...         request_type="create",
            ...         entity="projects",
            ...         data={"code": "p1"}
            ...     ),
            ...     BatchRequestItem(
            ...         request_type="update",
            ...         entity="projects",
            ...         record_id=123,
            ...         data={"name": "Updated"}
            ...     )
            ... ]
            >>> result = await client.batch.execute(items)
        """
        batch_request = BatchRequest(requests=requests)
        response = await self.client.post(
            self.base_route, json=batch_request.model_dump(exclude_none=True)
        )
        return BatchedRequestsResponse(**response)

    async def create_many(
        self,
        entity: str,
        records: list[dict[str, Any]],
        return_fields: Optional[list[str]] = None,
    ) -> BatchedRequestsResponse:
        """Convenience method to create multiple records in a batch.

        Args:
            entity: Entity type in plural snake_case (e.g., "projects", "shots")
            records: List of data dictionaries, one for each record to create
            return_fields: Optional list of fields to return for each record

        Returns:
            BatchedRequestsResponse with created records

        Raises:
            FlowPTRValidationError: If any record data is invalid
            FlowPTRError: If the batch operation fails

        Examples:
            >>> records = [
            ...     {"code": "proj1", "name": "Project 1"},
            ...     {"code": "proj2", "name": "Project 2"},
            ...     {"code": "proj3", "name": "Project 3"}
            ... ]
            >>> result = await client.batch.create_many(
            ...     "projects",
            ...     records,
            ...     return_fields=["id", "code", "name"]
            ... )
            >>> print(f"Created {len(result.data)} projects")
        """
        requests = [
            BatchRequestItem(
                request_type="create",
                entity=entity,
                data=record,
                options={"fields": return_fields} if return_fields else None,
            )
            for record in records
        ]
        return await self.execute(requests)

    async def update_many(
        self,
        entity: str,
        updates: list[tuple[int, dict[str, Any]]],
        return_fields: Optional[list[str]] = None,
    ) -> BatchedRequestsResponse:
        """Convenience method to update multiple records in a batch.

        Args:
            entity: Entity type in plural snake_case (e.g., "projects", "shots")
            updates: List of (record_id, data) tuples for each update
            return_fields: Optional list of fields to return for each record

        Returns:
            BatchedRequestsResponse with updated records

        Raises:
            FlowPTRValidationError: If any update data is invalid
            FlowPTRNotFoundError: If any record_id doesn't exist
            FlowPTRError: If the batch operation fails

        Examples:
            >>> updates = [
            ...     (123, {"name": "Updated Name 1"}),
            ...     (456, {"name": "Updated Name 2"}),
            ...     (789, {"sg_status": "ip"})
            ... ]
            >>> result = await client.batch.update_many(
            ...     "projects",
            ...     updates,
            ...     return_fields=["id", "name", "sg_status"]
            ... )
        """
        requests = [
            BatchRequestItem(
                request_type="update",
                entity=entity,
                record_id=record_id,
                data=data,
                options={"fields": return_fields} if return_fields else None,
            )
            for record_id, data in updates
        ]
        return await self.execute(requests)

    async def delete_many(
        self,
        entity: str,
        record_ids: list[int],
    ) -> BatchedRequestsResponse:
        """Convenience method to delete multiple records in a batch.

        Args:
            entity: Entity type in plural snake_case (e.g., "projects", "shots")
            record_ids: List of record IDs to delete

        Returns:
            BatchedRequestsResponse with deleted records

        Raises:
            FlowPTRNotFoundError: If any record_id doesn't exist
            FlowPTRError: If the batch operation fails

        Examples:
            >>> record_ids = [123, 456, 789]
            >>> result = await client.batch.delete_many("projects", record_ids)
            >>> print(f"Deleted {len(result.data)} projects")
        """
        requests = [
            BatchRequestItem(
                request_type="delete",
                entity=entity,
                record_id=record_id,
            )
            for record_id in record_ids
        ]
        return await self.execute(requests)
