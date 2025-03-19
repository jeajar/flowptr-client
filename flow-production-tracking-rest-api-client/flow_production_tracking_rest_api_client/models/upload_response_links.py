from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadResponseLinks")


@_attrs_define
class UploadResponseLinks:
    """
    Attributes:
        complete_upload (Union[Unset, str]): The URL that should be used to complete the upload after the file has been
            uploaded. This is a 'POST' and the body should contain the data returned by this request and the GET upload url
            request.
    """

    complete_upload: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        complete_upload = self.complete_upload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if complete_upload is not UNSET:
            field_dict["complete_upload"] = complete_upload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        complete_upload = d.pop("complete_upload", UNSET)

        upload_response_links = cls(
            complete_upload=complete_upload,
        )

        upload_response_links.additional_properties = d
        return upload_response_links

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
