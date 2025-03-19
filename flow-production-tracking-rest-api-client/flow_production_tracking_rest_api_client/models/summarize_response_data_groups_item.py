from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summarize_response_data_groups_item_summaries import SummarizeResponseDataGroupsItemSummaries


T = TypeVar("T", bound="SummarizeResponseDataGroupsItem")


@_attrs_define
class SummarizeResponseDataGroupsItem:
    """
    Attributes:
        group_name (Union[Unset, str]): The display name for the group.
        group_value (Union[Unset, str]): The actual value of the grouping value. This is often the same as `group_name`
            but in the case when grouping by entity, the `group_name` may be `PuppyA` and the group_value would be
            `{'type':'Asset','id':922,'name':'PuppyA'}`.
        summaries (Union[Unset, SummarizeResponseDataGroupsItemSummaries]): The summary calculation dict for each field
            requested.
    """

    group_name: Union[Unset, str] = UNSET
    group_value: Union[Unset, str] = UNSET
    summaries: Union[Unset, "SummarizeResponseDataGroupsItemSummaries"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_name = self.group_name

        group_value = self.group_value

        summaries: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summaries, Unset):
            summaries = self.summaries.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if group_value is not UNSET:
            field_dict["group_value"] = group_value
        if summaries is not UNSET:
            field_dict["summaries"] = summaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.summarize_response_data_groups_item_summaries import SummarizeResponseDataGroupsItemSummaries

        d = dict(src_dict)
        group_name = d.pop("group_name", UNSET)

        group_value = d.pop("group_value", UNSET)

        _summaries = d.pop("summaries", UNSET)
        summaries: Union[Unset, SummarizeResponseDataGroupsItemSummaries]
        if isinstance(_summaries, Unset):
            summaries = UNSET
        else:
            summaries = SummarizeResponseDataGroupsItemSummaries.from_dict(_summaries)

        summarize_response_data_groups_item = cls(
            group_name=group_name,
            group_value=group_value,
            summaries=summaries,
        )

        summarize_response_data_groups_item.additional_properties = d
        return summarize_response_data_groups_item

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
