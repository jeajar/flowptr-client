from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItemSeed")


@_attrs_define
class HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItemSeed:
    """Seed entity field which indicates the schema used by the provided path.

    Attributes:
        type_ (Union[Unset, str]):
        field (Union[Unset, str]):
    """

    type_: Union[Unset, str] = UNSET
    field: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        field = self.field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        field = d.pop("field", UNSET)

        hierarchy_expand_response_data_target_entities_additional_filter_presets_item_seed = cls(
            type_=type_,
            field=field,
        )

        hierarchy_expand_response_data_target_entities_additional_filter_presets_item_seed.additional_properties = d
        return hierarchy_expand_response_data_target_entities_additional_filter_presets_item_seed

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
