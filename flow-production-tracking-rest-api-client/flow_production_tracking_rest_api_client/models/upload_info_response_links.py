from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadInfoResponseLinks")


@_attrs_define
class UploadInfoResponseLinks:
    """
    Attributes:
        upload (Union[Unset, str]): The URL that should be used to upload the file. A 'PUT' request should be made to
            this URL will the body of the request being the file data.
        complete_upload (Union[Unset, str]): The URL that should be used to complete the upload after the file has been
            uploaded. This is a 'POST' and the body should contain the data returned by this request.
        get_next_part (Union[Unset, str]): This URL is used for getting the next upload URL when working with multi-part
            uploads. The key will only exist if 'multipart_upload' is true.
    """

    upload: Union[Unset, str] = UNSET
    complete_upload: Union[Unset, str] = UNSET
    get_next_part: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload = self.upload

        complete_upload = self.complete_upload

        get_next_part = self.get_next_part

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload is not UNSET:
            field_dict["upload"] = upload
        if complete_upload is not UNSET:
            field_dict["complete_upload"] = complete_upload
        if get_next_part is not UNSET:
            field_dict["get_next_part"] = get_next_part

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload = d.pop("upload", UNSET)

        complete_upload = d.pop("complete_upload", UNSET)

        get_next_part = d.pop("get_next_part", UNSET)

        upload_info_response_links = cls(
            upload=upload,
            complete_upload=complete_upload,
            get_next_part=get_next_part,
        )

        upload_info_response_links.additional_properties = d
        return upload_info_response_links

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
