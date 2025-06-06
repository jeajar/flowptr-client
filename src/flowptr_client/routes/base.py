from flowptr_client.interfaces import FlowPTRRestAPIClientInterface


class BaseRoute:
    """Base protocol for all API routes"""

    base_route: str

    def __init__(self, client: FlowPTRRestAPIClientInterface) -> None:
        """Initialize the route with a FlowPTRClient instance."""
        self.client = client
