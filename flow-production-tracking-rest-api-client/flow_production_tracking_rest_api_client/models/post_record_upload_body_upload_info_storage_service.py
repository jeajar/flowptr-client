from enum import Enum


class PostRecordUploadBodyUploadInfoStorageService(str, Enum):
    S3 = "s3"
    SG = "sg"

    def __str__(self) -> str:
        return str(self.value)
