from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_entities_response_data import SchemaEntitiesResponseData
    from ..models.self_link import SelfLink


T = TypeVar("T", bound="SchemaEntitiesResponse")


@_attrs_define
class SchemaEntitiesResponse:
    """
    Example:
        {'data': {'ActionMenuItem': {'name': {'value': 'Action Menu Item', 'editable': False}, 'visible': {'value':
            True, 'editable': False}}, 'ApiUser': {'name': {'value': 'Script', 'editable': False}, 'visible': {'value':
            True, 'editable': False}}, 'ApiUserProjectConnection': {'name': {'value': 'Api User Project Connection',
            'editable': False}, 'visible': {'value': True, 'editable': False}}, 'AppWelcomeUserConnection': {'name':
            {'value': 'App Welcome User Connection', 'editable': False}, 'visible': {'value': True, 'editable': False}},
            'Asset': {'name': {'value': 'Asset', 'editable': False}, 'visible': {'value': True, 'editable': False}}},
            'links': {'self': '/api/v1.1/schema'}}

    Attributes:
        data (Union[Unset, SchemaEntitiesResponseData]):
        links (Union[Unset, SelfLink]):
    """

    data: Union[Unset, "SchemaEntitiesResponseData"] = UNSET
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
        from ..models.schema_entities_response_data import SchemaEntitiesResponseData
        from ..models.self_link import SelfLink

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, SchemaEntitiesResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SchemaEntitiesResponseData.from_dict(_data)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfLink]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfLink.from_dict(_links)

        schema_entities_response = cls(
            data=data,
            links=links,
        )

        schema_entities_response.additional_properties = d
        return schema_entities_response

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
