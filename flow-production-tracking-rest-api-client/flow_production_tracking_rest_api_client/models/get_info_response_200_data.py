from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInfoResponse200Data")


@_attrs_define
class GetInfoResponse200Data:
    """
    Attributes:
        shotgun_version (Union[Unset, str]): The Flow Production Tracking server version number.
        api_version (Union[Unset, str]): The REST API version number.
    """

    shotgun_version: Union[Unset, str] = UNSET
    api_version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shotgun_version = self.shotgun_version

        api_version = self.api_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shotgun_version is not UNSET:
            field_dict["shotgun_version"] = shotgun_version
        if api_version is not UNSET:
            field_dict["api_version"] = api_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shotgun_version = d.pop("shotgun_version", UNSET)

        api_version = d.pop("api_version", UNSET)

        get_info_response_200_data = cls(
            shotgun_version=shotgun_version,
            api_version=api_version,
        )

        get_info_response_200_data.additional_properties = d
        return get_info_response_200_data

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
