from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAccessTokenResponse200")


@_attrs_define
class GetAccessTokenResponse200:
    """
    Attributes:
        token_type (Union[Unset, str]): The type of token being returned. This should prefix your access_token in the
            Authorization header sent with requests. Default: 'Bearer'.
        access_token (Union[Unset, str]): The token to be used in the Authorization header to makes requests.
        expires_in (Union[Unset, int]): The number of seconds the access_token is valid for. Default: 3600.
        refresh_token (Union[Unset, str]): The token to be used with they `refresh_token` grant type to generate a new
            access token.
    """

    token_type: Union[Unset, str] = "Bearer"
    access_token: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = 3600
    refresh_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_type = self.token_type

        access_token = self.access_token

        expires_in = self.expires_in

        refresh_token = self.refresh_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token_type = d.pop("token_type", UNSET)

        access_token = d.pop("access_token", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        get_access_token_response_200 = cls(
            token_type=token_type,
            access_token=access_token,
            expires_in=expires_in,
            refresh_token=refresh_token,
        )

        get_access_token_response_200.additional_properties = d
        return get_access_token_response_200

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
