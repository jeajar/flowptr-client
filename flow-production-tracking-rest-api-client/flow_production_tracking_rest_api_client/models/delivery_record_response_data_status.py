from enum import Enum


class DeliveryRecordResponseDataStatus(str, Enum):
    DELIVERED = "delivered"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
