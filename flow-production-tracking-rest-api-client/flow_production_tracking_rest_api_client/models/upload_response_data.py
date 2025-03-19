from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadResponseData")


@_attrs_define
class UploadResponseData:
    """
    Attributes:
        upload_id (Union[Unset, str]): A unique identifier for the upload.
        original_filename (Union[Unset, str]): The original filename that was provided in the request.
    """

    upload_id: Union[Unset, str] = UNSET
    original_filename: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        original_filename = self.original_filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload_id is not UNSET:
            field_dict["upload_id"] = upload_id
        if original_filename is not UNSET:
            field_dict["original_filename"] = original_filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_id = d.pop("upload_id", UNSET)

        original_filename = d.pop("original_filename", UNSET)

        upload_response_data = cls(
            upload_id=upload_id,
            original_filename=original_filename,
        )

        upload_response_data.additional_properties = d
        return upload_response_data

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
