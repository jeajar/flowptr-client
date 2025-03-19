from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWorkDayRulesRequest")


@_attrs_define
class UpdateWorkDayRulesRequest:
    """
    Attributes:
        date (str): The date of the work day rule you want to set `YYYY-MM-DD`.
        working (bool): If it a working day.
        user_id (Union[Unset, int]): The id of the user you want to set the work day rule.
        project_id (Union[Unset, int]): The id of the project you want to set the work day rule.
        recalculate_field (Union[Unset, str]): The field from the task you want recalculation `duration` or `due_date`
            only.
        description (Union[Unset, str]): The description you want to set for that work day rule.
    """

    date: str
    working: bool
    user_id: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    recalculate_field: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        working = self.working

        user_id = self.user_id

        project_id = self.project_id

        recalculate_field = self.recalculate_field

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "working": working,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if recalculate_field is not UNSET:
            field_dict["recalculate_field"] = recalculate_field
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        working = d.pop("working")

        user_id = d.pop("user_id", UNSET)

        project_id = d.pop("project_id", UNSET)

        recalculate_field = d.pop("recalculate_field", UNSET)

        description = d.pop("description", UNSET)

        update_work_day_rules_request = cls(
            date=date,
            working=working,
            user_id=user_id,
            project_id=project_id,
            recalculate_field=recalculate_field,
            description=description,
        )

        update_work_day_rules_request.additional_properties = d
        return update_work_day_rules_request

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
