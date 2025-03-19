from enum import Enum


class ReadEntityRecordFileFieldAlt(str, Enum):
    ORIGINAL = "original"
    THUMBNAIL = "thumbnail"

    def __str__(self) -> str:
        return str(self.value)
