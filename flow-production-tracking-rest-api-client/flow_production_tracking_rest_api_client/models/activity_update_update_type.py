from enum import Enum


class ActivityUpdateUpdateType(str, Enum):
    CREATE = "create"
    CREATE_REPLY = "create_reply"
    DELETE = "delete"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
