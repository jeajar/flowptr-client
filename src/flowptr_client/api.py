"""High-level API for Flow Production Tracking REST API.

This module provides the FlowPTRAPI class which composes the HTTP client
with route handlers following Clean Architecture principles.
"""

from typing import TYPE_CHECKING

from flowptr_client.client import FlowPTRClient
from flowptr_client.config import FlowPTRSettings

if TYPE_CHECKING:
    from flowptr_client.routes.batch import BatchRoute
    from flowptr_client.routes.entity import EntityRoute
    from flowptr_client.routes.info import InfoRoute
    from flowptr_client.routes.schema import SchemaRoute


class FlowPTRAPI:
    """High-level API for Flow Production Tracking REST API.

    This class composes the HTTP client with specialized route handlers,
    providing a clean interface for interacting with the API. It follows
    Clean Architecture principles by separating concerns between the HTTP
    client and business logic in route handlers.

    Examples:
        >>> # Initialize with environment variables
        >>> api = FlowPTRAPI()
        >>>
        >>> # Or pass config directly
        >>> config = FlowPTRSettings(
        ...     CLIENT_ID="your_script_name",
        ...     CLIENT_SECRET="your_script_key",
        ...     DOMAIN="https://your-site.shotgrid.autodesk.com"
        ... )
        >>> api = FlowPTRAPI(config)
        >>>
        >>> # Use route handlers
        >>> projects = await api.entity.get("projects", fields=["code", "name"])
        >>> project = await api.entity.get_one("projects", 123)
        >>> schema = await api.schema.get_entity("projects")
        >>> batch_result = await api.batch.create_many("projects", records)

    Attributes:
        client: The underlying HTTP client
        entity: Entity operations route handler
        batch: Batch operations route handler
        schema: Schema introspection route handler
        info: Server info route handler
    """

    def __init__(
        self,
        config: FlowPTRSettings = FlowPTRSettings(),
        client: FlowPTRClient | None = None,
    ) -> None:
        """Initialize the FlowPTR API.

        Args:
            config: Client configuration (loads from environment if not provided)
            client: Optional pre-configured client instance. If not provided,
                   a new client will be created with the given config.
        """
        self.client = client or FlowPTRClient(config)

    @property
    def entity(self) -> "EntityRoute":
        """Access entity operations (CRUD, search, etc.).

        Returns:
            EntityRoute instance for entity operations
        """
        if not hasattr(self, "_entity"):
            from flowptr_client.routes.entity import EntityRoute

            self._entity = EntityRoute(self.client)
        return self._entity

    @property
    def batch(self) -> "BatchRoute":
        """Access batch operations for atomic multi-record operations.

        Returns:
            BatchRoute instance for batch operations
        """
        if not hasattr(self, "_batch"):
            from flowptr_client.routes.batch import BatchRoute

            self._batch = BatchRoute(self.client)
        return self._batch

    @property
    def schema(self) -> "SchemaRoute":
        """Access schema introspection operations.

        Returns:
            SchemaRoute instance for schema operations
        """
        if not hasattr(self, "_schema"):
            from flowptr_client.routes.schema import SchemaRoute

            self._schema = SchemaRoute(self.client)
        return self._schema

    @property
    def info(self) -> "InfoRoute":
        """Access server info and OpenAPI spec.

        Returns:
            InfoRoute instance for info operations
        """
        if not hasattr(self, "_info"):
            from flowptr_client.routes.info import InfoRoute

            self._info = InfoRoute(self.client)
        return self._info
