from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_field_upload_abort_body_upload_info_storage_service import (
    PostFieldUploadAbortBodyUploadInfoStorageService,
)
from ..models.post_field_upload_abort_body_upload_info_upload_type import PostFieldUploadAbortBodyUploadInfoUploadType

T = TypeVar("T", bound="PostFieldUploadAbortBodyUploadInfo")


@_attrs_define
class PostFieldUploadAbortBodyUploadInfo:
    """Response data from the request to get an upload URL and the upload request.

    Attributes:
        timestamp (str): The ISO 8601 timestamp of this request. Used in the complete request to set the created_at
            value of the upload.
        upload_type (PostFieldUploadAbortBodyUploadInfoUploadType): The type of upload that the server has determined
            this request is for.
        upload_id (str): A unique identifier for the upload. This will be set for 's3' uploads but for 'sg' uploads the
            value will be provided after the file is uploaded.
        storage_service (PostFieldUploadAbortBodyUploadInfoStorageService): The location of there the file will be
            uploaded. 'sg' is the Flow Production Tracking Application server. 's3' is Amazon AWS S3.
        original_filename (str): The original filename that was provided in the request.
        multipart_upload (bool): Indicates if the upload was a multi-part upload.
    """

    timestamp: str
    upload_type: PostFieldUploadAbortBodyUploadInfoUploadType
    upload_id: str
    storage_service: PostFieldUploadAbortBodyUploadInfoStorageService
    original_filename: str
    multipart_upload: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        upload_type = self.upload_type.value

        upload_id = self.upload_id

        storage_service = self.storage_service.value

        original_filename = self.original_filename

        multipart_upload = self.multipart_upload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "upload_type": upload_type,
                "upload_id": upload_id,
                "storage_service": storage_service,
                "original_filename": original_filename,
                "multipart_upload": multipart_upload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        upload_type = PostFieldUploadAbortBodyUploadInfoUploadType(d.pop("upload_type"))

        upload_id = d.pop("upload_id")

        storage_service = PostFieldUploadAbortBodyUploadInfoStorageService(d.pop("storage_service"))

        original_filename = d.pop("original_filename")

        multipart_upload = d.pop("multipart_upload")

        post_field_upload_abort_body_upload_info = cls(
            timestamp=timestamp,
            upload_type=upload_type,
            upload_id=upload_id,
            storage_service=storage_service,
            original_filename=original_filename,
            multipart_upload=multipart_upload,
        )

        post_field_upload_abort_body_upload_info.additional_properties = d
        return post_field_upload_abort_body_upload_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
