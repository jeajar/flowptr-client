from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RefreshRequest")


@_attrs_define
class RefreshRequest:
    """
    Example:
        {'grant_type': 'client_credentials', 'refresh_token': '<long token string>'}

    Attributes:
        grant_type (Union[Unset, str]): OAuth 2.0 grant type. Should be set to `refresh_token`.
        refresh_token (Union[Unset, str]): Refresh token provided when an access_token was granted.
    """

    grant_type: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type

        refresh_token = self.refresh_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = d.pop("grant_type", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        refresh_request = cls(
            grant_type=grant_type,
            refresh_token=refresh_token,
        )

        refresh_request.additional_properties = d
        return refresh_request

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
