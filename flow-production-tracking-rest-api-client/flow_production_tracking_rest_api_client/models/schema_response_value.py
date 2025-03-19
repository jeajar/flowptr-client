from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaResponseValue")


@_attrs_define
class SchemaResponseValue:
    """Simple object that contains the attributes value and indicates if it is editable.

    Attributes:
        value (Union[Unset, bool, str]): The property's value.
        editable (Union[Unset, bool]): Whether or not the property is editable.
    """

    value: Union[Unset, bool, str] = UNSET
    editable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Union[Unset, bool, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        editable = self.editable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if editable is not UNSET:
            field_dict["editable"] = editable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_value(data: object) -> Union[Unset, bool, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, bool, str], data)

        value = _parse_value(d.pop("value", UNSET))

        editable = d.pop("editable", UNSET)

        schema_response_value = cls(
            value=value,
            editable=editable,
        )

        schema_response_value.additional_properties = d
        return schema_response_value

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
