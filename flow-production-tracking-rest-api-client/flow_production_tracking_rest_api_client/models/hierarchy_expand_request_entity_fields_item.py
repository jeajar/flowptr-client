from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HierarchyExpandRequestEntityFieldsItem")


@_attrs_define
class HierarchyExpandRequestEntityFieldsItem:
    """
    Attributes:
        entity (Union[Unset, str]): The entity to be returned.
        fields (Union[Unset, list[str]]): An array of fields to be returned.
    """

    entity: Union[Unset, str] = UNSET
    fields: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity = self.entity

        fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity is not UNSET:
            field_dict["entity"] = entity
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity = d.pop("entity", UNSET)

        fields = cast(list[str], d.pop("fields", UNSET))

        hierarchy_expand_request_entity_fields_item = cls(
            entity=entity,
            fields=fields,
        )

        hierarchy_expand_request_entity_fields_item.additional_properties = d
        return hierarchy_expand_request_entity_fields_item

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
