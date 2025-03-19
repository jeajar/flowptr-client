from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateOrUpdateRequest")


@_attrs_define
class CreateOrUpdateRequest:
    """This object should contain the key value pairs for the fields you want to set.

    Example:
        {'name': 'Red Sun', 'users': [{'id': 19, 'name': 'Artist 1', 'type': 'HumanUser'}, {'id': 18, 'name': 'Artist
            2', 'type': 'HumanUser'}]}

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_or_update_request = cls()

        create_or_update_request.additional_properties = d
        return create_or_update_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
