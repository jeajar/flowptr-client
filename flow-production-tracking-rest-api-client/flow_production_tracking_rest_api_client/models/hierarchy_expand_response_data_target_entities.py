from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hierarchy_expand_response_data_target_entities_additional_filter_presets_item import (
        HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItem,
    )


T = TypeVar("T", bound="HierarchyExpandResponseDataTargetEntities")


@_attrs_define
class HierarchyExpandResponseDataTargetEntities:
    """Seed for a CRUD query to get the target entities associated to the tree node.

    Attributes:
        type_ (Union[Unset, str]): Type of entity for the CRUD query.
        additional_filter_presets (Union[Unset,
            list['HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItem']]): Should be used as is in the CRUD
            query.
    """

    type_: Union[Unset, str] = UNSET
    additional_filter_presets: Union[
        Unset, list["HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        additional_filter_presets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.additional_filter_presets, Unset):
            additional_filter_presets = []
            for additional_filter_presets_item_data in self.additional_filter_presets:
                additional_filter_presets_item = additional_filter_presets_item_data.to_dict()
                additional_filter_presets.append(additional_filter_presets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if additional_filter_presets is not UNSET:
            field_dict["additional_filter_presets"] = additional_filter_presets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hierarchy_expand_response_data_target_entities_additional_filter_presets_item import (
            HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItem,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        additional_filter_presets = []
        _additional_filter_presets = d.pop("additional_filter_presets", UNSET)
        for additional_filter_presets_item_data in _additional_filter_presets or []:
            additional_filter_presets_item = (
                HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItem.from_dict(
                    additional_filter_presets_item_data
                )
            )

            additional_filter_presets.append(additional_filter_presets_item)

        hierarchy_expand_response_data_target_entities = cls(
            type_=type_,
            additional_filter_presets=additional_filter_presets,
        )

        hierarchy_expand_response_data_target_entities.additional_properties = d
        return hierarchy_expand_response_data_target_entities

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
