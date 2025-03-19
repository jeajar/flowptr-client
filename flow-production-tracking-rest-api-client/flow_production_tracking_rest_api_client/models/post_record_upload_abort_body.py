from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_record_upload_abort_body_upload_info import PostRecordUploadAbortBodyUploadInfo


T = TypeVar("T", bound="PostRecordUploadAbortBody")


@_attrs_define
class PostRecordUploadAbortBody:
    """
    Attributes:
        upload_info (PostRecordUploadAbortBodyUploadInfo): Response data from the request to get an upload URL and the
            upload request.
    """

    upload_info: "PostRecordUploadAbortBodyUploadInfo"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_info = self.upload_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_info": upload_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_record_upload_abort_body_upload_info import PostRecordUploadAbortBodyUploadInfo

        d = dict(src_dict)
        upload_info = PostRecordUploadAbortBodyUploadInfo.from_dict(d.pop("upload_info"))

        post_record_upload_abort_body = cls(
            upload_info=upload_info,
        )

        post_record_upload_abort_body.additional_properties = d
        return post_record_upload_abort_body

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
