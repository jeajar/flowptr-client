from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.self_link import SelfLink
    from ..models.update_entity_last_accessed_response_200_data import UpdateEntityLastAccessedResponse200Data


T = TypeVar("T", bound="UpdateEntityLastAccessedResponse200")


@_attrs_define
class UpdateEntityLastAccessedResponse200:
    """
    Attributes:
        data (Union[Unset, UpdateEntityLastAccessedResponse200Data]):
        links (Union[Unset, SelfLink]):
    """

    data: Union[Unset, "UpdateEntityLastAccessedResponse200Data"] = UNSET
    links: Union[Unset, "SelfLink"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.self_link import SelfLink
        from ..models.update_entity_last_accessed_response_200_data import UpdateEntityLastAccessedResponse200Data

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, UpdateEntityLastAccessedResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = UpdateEntityLastAccessedResponse200Data.from_dict(_data)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfLink]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfLink.from_dict(_links)

        update_entity_last_accessed_response_200 = cls(
            data=data,
            links=links,
        )

        update_entity_last_accessed_response_200.additional_properties = d
        return update_entity_last_accessed_response_200

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
