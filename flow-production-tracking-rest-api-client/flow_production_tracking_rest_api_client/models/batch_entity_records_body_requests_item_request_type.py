from enum import Enum


class BatchEntityRecordsBodyRequestsItemRequestType(str, Enum):
    CREATE = "create"
    DELETE = "delete"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
