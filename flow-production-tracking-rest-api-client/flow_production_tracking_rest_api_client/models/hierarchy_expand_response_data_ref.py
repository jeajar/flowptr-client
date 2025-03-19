from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hierarchy_expand_response_data_ref_value import HierarchyExpandResponseDataRefValue


T = TypeVar("T", bound="HierarchyExpandResponseDataRef")


@_attrs_define
class HierarchyExpandResponseDataRef:
    """Reference to the object the tree node is representing.

    Attributes:
        kind (Union[Unset, str]): This can be of type 'root', 'entity', 'entity_type' or 'list'.
        value (Union[Unset, HierarchyExpandResponseDataRefValue]): Reference to the corresponding object.
    """

    kind: Union[Unset, str] = UNSET
    value: Union[Unset, "HierarchyExpandResponseDataRefValue"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hierarchy_expand_response_data_ref_value import HierarchyExpandResponseDataRefValue

        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, HierarchyExpandResponseDataRefValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = HierarchyExpandResponseDataRefValue.from_dict(_value)

        hierarchy_expand_response_data_ref = cls(
            kind=kind,
            value=value,
        )

        hierarchy_expand_response_data_ref.additional_properties = d
        return hierarchy_expand_response_data_ref

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
