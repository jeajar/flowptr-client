from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityFieldsParameter")


@_attrs_define
class EntityFieldsParameter:
    """Indicates which fields to be returned when an entity is returned in the payload.

    Example:
        {'entity_fields[Asset]': 'fields1, fields2', 'entity_fields[Shot]': 'fields1, fields2'}

    Attributes:
        entity (Union[Unset, str]): The entity to be returned.
        fields (Union[Unset, list[str]]): List of comma-separated fields to return. If * is specified, all fields will
            be returned. Default: *
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

        entity_fields_parameter = cls(
            entity=entity,
            fields=fields,
        )

        entity_fields_parameter.additional_properties = d
        return entity_fields_parameter

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
