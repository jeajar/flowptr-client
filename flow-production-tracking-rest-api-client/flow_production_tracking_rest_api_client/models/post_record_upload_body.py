from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_record_upload_body_upload_data import PostRecordUploadBodyUploadData
    from ..models.post_record_upload_body_upload_info import PostRecordUploadBodyUploadInfo


T = TypeVar("T", bound="PostRecordUploadBody")


@_attrs_define
class PostRecordUploadBody:
    """
    Attributes:
        upload_info (PostRecordUploadBodyUploadInfo): Response data from the request to get an upload URL and the upload
            request.
        upload_data (PostRecordUploadBodyUploadData):
    """

    upload_info: "PostRecordUploadBodyUploadInfo"
    upload_data: "PostRecordUploadBodyUploadData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_info = self.upload_info.to_dict()

        upload_data = self.upload_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_info": upload_info,
                "upload_data": upload_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_record_upload_body_upload_data import PostRecordUploadBodyUploadData
        from ..models.post_record_upload_body_upload_info import PostRecordUploadBodyUploadInfo

        d = dict(src_dict)
        upload_info = PostRecordUploadBodyUploadInfo.from_dict(d.pop("upload_info"))

        upload_data = PostRecordUploadBodyUploadData.from_dict(d.pop("upload_data"))

        post_record_upload_body = cls(
            upload_info=upload_info,
            upload_data=upload_data,
        )

        post_record_upload_body.additional_properties = d
        return post_record_upload_body

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
