from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReadLicenseInfoResponse200Data")


@_attrs_define
class ReadLicenseInfoResponse200Data:
    """
    Attributes:
        assigned (Union[Unset, float]): The number of assigned seats.
        free (Union[Unset, float]): The number of available seats.
        rule (Union[Unset, str]): The license rule applied.
        total (Union[Unset, float]): The total number of seats.
        type_ (Union[Unset, str]): The allocation license type.
    """

    assigned: Union[Unset, float] = UNSET
    free: Union[Unset, float] = UNSET
    rule: Union[Unset, str] = UNSET
    total: Union[Unset, float] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned = self.assigned

        free = self.free

        rule = self.rule

        total = self.total

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if free is not UNSET:
            field_dict["free"] = free
        if rule is not UNSET:
            field_dict["rule"] = rule
        if total is not UNSET:
            field_dict["total"] = total
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assigned = d.pop("assigned", UNSET)

        free = d.pop("free", UNSET)

        rule = d.pop("rule", UNSET)

        total = d.pop("total", UNSET)

        type_ = d.pop("type", UNSET)

        read_license_info_response_200_data = cls(
            assigned=assigned,
            free=free,
            rule=rule,
            total=total,
            type_=type_,
        )

        read_license_info_response_200_data.additional_properties = d
        return read_license_info_response_200_data

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
