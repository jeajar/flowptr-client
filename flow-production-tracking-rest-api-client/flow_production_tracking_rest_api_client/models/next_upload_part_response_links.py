from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NextUploadPartResponseLinks")


@_attrs_define
class NextUploadPartResponseLinks:
    """
    Attributes:
        upload (Union[Unset, str]): The URL that should be used to upload that part of the file. A 'PUT' request should
            be made to this URL will the body of the request being the next chunck of file data.
        get_next_part (Union[Unset, str]): The URL that should be used to get the next part URL. This is a 'GET' with
            parameters that specify the next part of the upload.
    """

    upload: Union[Unset, str] = UNSET
    get_next_part: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload = self.upload

        get_next_part = self.get_next_part

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload is not UNSET:
            field_dict["upload"] = upload
        if get_next_part is not UNSET:
            field_dict["get_next_part"] = get_next_part

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload = d.pop("upload", UNSET)

        get_next_part = d.pop("get_next_part", UNSET)

        next_upload_part_response_links = cls(
            upload=upload,
            get_next_part=get_next_part,
        )

        next_upload_part_response_links.additional_properties = d
        return next_upload_part_response_links

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
