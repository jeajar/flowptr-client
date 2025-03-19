from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePreferencesBody")


@_attrs_define
class UpdatePreferencesBody:
    """
    Attributes:
        preference (str): The type of operation to be executed, currently, we only support the following:
            `enable_entity` Example: enable_entity.
        entity_type (str): The name of the custom entity type to interact with. Custom entity name should be passed in
            its singular CamelCase form. Ex: `CustomNonProjectEntity01` Example: CustomNonProjectEntity01.
        display_name (Union[Unset, str]): The display name of the custom entity Example: Cut.
    """

    preference: str
    entity_type: str
    display_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preference = self.preference

        entity_type = self.entity_type

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preference": preference,
                "entity_type": entity_type,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        preference = d.pop("preference")

        entity_type = d.pop("entity_type")

        display_name = d.pop("display_name", UNSET)

        update_preferences_body = cls(
            preference=preference,
            entity_type=entity_type,
            display_name=display_name,
        )

        update_preferences_body.additional_properties = d
        return update_preferences_body

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
