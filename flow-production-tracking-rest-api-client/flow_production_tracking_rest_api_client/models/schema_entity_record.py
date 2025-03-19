from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_response_value import SchemaResponseValue


T = TypeVar("T", bound="SchemaEntityRecord")


@_attrs_define
class SchemaEntityRecord:
    """The name of the entity and if the entity is visible.

    Attributes:
        name (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and indicates if it
            is editable.
        visible (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and indicates if
            it is editable.
    """

    name: Union[Unset, "SchemaResponseValue"] = UNSET
    visible: Union[Unset, "SchemaResponseValue"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        visible: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.visible, Unset):
            visible = self.visible.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_response_value import SchemaResponseValue

        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, SchemaResponseValue]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = SchemaResponseValue.from_dict(_name)

        _visible = d.pop("visible", UNSET)
        visible: Union[Unset, SchemaResponseValue]
        if isinstance(_visible, Unset):
            visible = UNSET
        else:
            visible = SchemaResponseValue.from_dict(_visible)

        schema_entity_record = cls(
            name=name,
            visible=visible,
        )

        schema_entity_record.additional_properties = d
        return schema_entity_record

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
