from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hierarchy_expand_response_data_target_entities_additional_filter_presets_item_seed import (
        HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItemSeed,
    )


T = TypeVar("T", bound="HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItem")


@_attrs_define
class HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItem:
    """
    Attributes:
        preset_name (Union[Unset, str]): It uses a special 'NAV_ENTRIES' preset to build a request and retrieve the
            proper entities.
        path (Union[Unset, str]): Absolute path that corresponds to this tree node.
        seed (Union[Unset, HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItemSeed]): Seed entity field
            which indicates the schema used by the provided path.
    """

    preset_name: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    seed: Union[Unset, "HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItemSeed"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preset_name = self.preset_name

        path = self.path

        seed: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.seed, Unset):
            seed = self.seed.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preset_name is not UNSET:
            field_dict["preset_name"] = preset_name
        if path is not UNSET:
            field_dict["path"] = path
        if seed is not UNSET:
            field_dict["seed"] = seed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hierarchy_expand_response_data_target_entities_additional_filter_presets_item_seed import (
            HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItemSeed,
        )

        d = dict(src_dict)
        preset_name = d.pop("preset_name", UNSET)

        path = d.pop("path", UNSET)

        _seed = d.pop("seed", UNSET)
        seed: Union[Unset, HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItemSeed]
        if isinstance(_seed, Unset):
            seed = UNSET
        else:
            seed = HierarchyExpandResponseDataTargetEntitiesAdditionalFilterPresetsItemSeed.from_dict(_seed)

        hierarchy_expand_response_data_target_entities_additional_filter_presets_item = cls(
            preset_name=preset_name,
            path=path,
            seed=seed,
        )

        hierarchy_expand_response_data_target_entities_additional_filter_presets_item.additional_properties = d
        return hierarchy_expand_response_data_target_entities_additional_filter_presets_item

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
