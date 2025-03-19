from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hierarchy_expand_response_data import HierarchyExpandResponseData


T = TypeVar("T", bound="HierarchyExpandResponse")


@_attrs_define
class HierarchyExpandResponse:
    """
    Example:
        {'data': {'label': 'Demo: Animation', 'ref': {'kind': 'entity', 'value': {'type': 'Project', 'id': 70}},
            'parent_path': '/', 'path': '/Project/70', 'target_entities': {'type': 'Version', 'additional_filter_presets':
            [{'preset_name': 'NAV_ENTRIES', 'path': '/Project/70', 'seed': {'type': 'Version', 'field': 'entity'}}]},
            'has_children': True, 'children': [{'label': 'Assets', 'ref': {'kind': 'entity_type', 'value': 'Asset'}, 'path':
            '/Project/70/Asset', 'target_entities': {'type': 'Version', 'additional_filter_presets': [{'preset_name':
            'NAV_ENTRIES', 'path': '/Project/70/Asset', 'seed': {'type': 'Version', 'field': 'entity'}}]}, 'has_children':
            True}, {'label': 'Shots', 'ref': {'kind': 'entity_type', 'value': 'Shot'}, 'path': '/Project/70/Shot',
            'target_entities': {'type': 'Version', 'additional_filter_presets': [{'preset_name': 'NAV_ENTRIES', 'path':
            '/Project/70/Shot', 'seed': {'type': 'Version', 'field': 'entity'}}]}, 'has_children': True}]}}

    Attributes:
        data (Union[Unset, HierarchyExpandResponseData]): The navigation tree at a specific level.
    """

    data: Union[Unset, "HierarchyExpandResponseData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hierarchy_expand_response_data import HierarchyExpandResponseData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, HierarchyExpandResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = HierarchyExpandResponseData.from_dict(_data)

        hierarchy_expand_response = cls(
            data=data,
        )

        hierarchy_expand_response.additional_properties = d
        return hierarchy_expand_response

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
