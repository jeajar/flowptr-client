from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.upload_info_response_data_storage_service import UploadInfoResponseDataStorageService
from ..models.upload_info_response_data_upload_type import UploadInfoResponseDataUploadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadInfoResponseData")


@_attrs_define
class UploadInfoResponseData:
    """
    Attributes:
        timestamp (Union[Unset, str]): The ISO 8601 timestamp of this request. Used in the complete request to set the
            created_at value of the upload.
        upload_type (Union[Unset, UploadInfoResponseDataUploadType]): The type of upload that the server has determined
            this request is for.
        upload_id (Union[Unset, str]): A unique identifier for the upload. This will be set for 's3' uploads but for
            'sg' uploads the value will be provided after the file is uploaded.
        storage_service (Union[Unset, UploadInfoResponseDataStorageService]): The location of there the file will be
            uploaded. 'sg' is the Flow Production Tracking Application server. 's3' is Amazon AWS S3.
        original_filename (Union[Unset, str]): The original filename that was provided in the request.
        multipart_upload (Union[Unset, bool]): Indicates if the upload is a multi-part upload. This is only supported
            for 's3' uploads.
    """

    timestamp: Union[Unset, str] = UNSET
    upload_type: Union[Unset, UploadInfoResponseDataUploadType] = UNSET
    upload_id: Union[Unset, str] = UNSET
    storage_service: Union[Unset, UploadInfoResponseDataStorageService] = UNSET
    original_filename: Union[Unset, str] = UNSET
    multipart_upload: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        upload_type: Union[Unset, str] = UNSET
        if not isinstance(self.upload_type, Unset):
            upload_type = self.upload_type.value

        upload_id = self.upload_id

        storage_service: Union[Unset, str] = UNSET
        if not isinstance(self.storage_service, Unset):
            storage_service = self.storage_service.value

        original_filename = self.original_filename

        multipart_upload = self.multipart_upload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if upload_type is not UNSET:
            field_dict["upload_type"] = upload_type
        if upload_id is not UNSET:
            field_dict["upload_id"] = upload_id
        if storage_service is not UNSET:
            field_dict["storage_service"] = storage_service
        if original_filename is not UNSET:
            field_dict["original_filename"] = original_filename
        if multipart_upload is not UNSET:
            field_dict["multipart_upload"] = multipart_upload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        _upload_type = d.pop("upload_type", UNSET)
        upload_type: Union[Unset, UploadInfoResponseDataUploadType]
        if isinstance(_upload_type, Unset):
            upload_type = UNSET
        else:
            upload_type = UploadInfoResponseDataUploadType(_upload_type)

        upload_id = d.pop("upload_id", UNSET)

        _storage_service = d.pop("storage_service", UNSET)
        storage_service: Union[Unset, UploadInfoResponseDataStorageService]
        if isinstance(_storage_service, Unset):
            storage_service = UNSET
        else:
            storage_service = UploadInfoResponseDataStorageService(_storage_service)

        original_filename = d.pop("original_filename", UNSET)

        multipart_upload = d.pop("multipart_upload", UNSET)

        upload_info_response_data = cls(
            timestamp=timestamp,
            upload_type=upload_type,
            upload_id=upload_id,
            storage_service=storage_service,
            original_filename=original_filename,
            multipart_upload=multipart_upload,
        )

        upload_info_response_data.additional_properties = d
        return upload_info_response_data

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
