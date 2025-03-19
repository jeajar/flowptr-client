from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWorkDayRulesResponseDataItem")


@_attrs_define
class GetWorkDayRulesResponseDataItem:
    """
    Attributes:
        date (Union[Unset, str]): Date of teh work day rule.
        working (Union[Unset, bool]): If it's a working day or not.
        description (Union[Unset, str]): Description of the work day rule.
        reason (Union[Unset, str]): The reason code of the work day rule. (`STUDIO_WORK_WEEK, STUDIO_EXCEPTION,
            PROJECT_WORK_WEEK, PROJECT_EXCEPTION, USER_WORK_WEEK, USER_EXCEPTION`)
    """

    date: Union[Unset, str] = UNSET
    working: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        working = self.working

        description = self.description

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if working is not UNSET:
            field_dict["working"] = working
        if description is not UNSET:
            field_dict["description"] = description
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        working = d.pop("working", UNSET)

        description = d.pop("description", UNSET)

        reason = d.pop("reason", UNSET)

        get_work_day_rules_response_data_item = cls(
            date=date,
            working=working,
            description=description,
            reason=reason,
        )

        get_work_day_rules_response_data_item.additional_properties = d
        return get_work_day_rules_response_data_item

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
