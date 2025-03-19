from enum import Enum


class PostRecordUploadBodyUploadInfoUploadType(str, Enum):
    ATTACHMENT = "Attachment"
    THUMBNAIL = "Thumbnail"

    def __str__(self) -> str:
        return str(self.value)
