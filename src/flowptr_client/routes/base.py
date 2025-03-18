from typing import Protocol

from ..client import FlowPTRClient


class BaseRoute(Protocol):
    """Base protocol for all API routes"""

    client: FlowPTRClient
    base_route: str

    def __init__(self, client: FlowPTRClient) -> None:
        self.client = client
