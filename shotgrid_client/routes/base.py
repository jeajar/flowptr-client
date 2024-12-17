from typing import Protocol

from ..client import ShotgridClient


class BaseRoute(Protocol):
    """Base protocol for all API routes"""

    client: ShotgridClient
    base_route: str

    def __init__(self, client: ShotgridClient) -> None:
        self.client = client
