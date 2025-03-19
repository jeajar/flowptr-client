from enum import Enum


class PostFieldUploadAbortBodyUploadInfoStorageService(str, Enum):
    S3 = "s3"
    SG = "sg"

    def __str__(self) -> str:
        return str(self.value)
