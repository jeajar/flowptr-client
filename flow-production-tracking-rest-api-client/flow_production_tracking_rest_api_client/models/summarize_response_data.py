from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summarize_response_data_groups_item import SummarizeResponseDataGroupsItem
    from ..models.summarize_response_data_summaries import SummarizeResponseDataSummaries


T = TypeVar("T", bound="SummarizeResponseData")


@_attrs_define
class SummarizeResponseData:
    """
    Attributes:
        summaries (Union[Unset, SummarizeResponseDataSummaries]): The total summary for the query.
        groups (Union[Unset, list['SummarizeResponseDataGroupsItem']]): The summary for each group.
    """

    summaries: Union[Unset, "SummarizeResponseDataSummaries"] = UNSET
    groups: Union[Unset, list["SummarizeResponseDataGroupsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summaries: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summaries, Unset):
            summaries = self.summaries.to_dict()

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summaries is not UNSET:
            field_dict["summaries"] = summaries
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.summarize_response_data_groups_item import SummarizeResponseDataGroupsItem
        from ..models.summarize_response_data_summaries import SummarizeResponseDataSummaries

        d = dict(src_dict)
        _summaries = d.pop("summaries", UNSET)
        summaries: Union[Unset, SummarizeResponseDataSummaries]
        if isinstance(_summaries, Unset):
            summaries = UNSET
        else:
            summaries = SummarizeResponseDataSummaries.from_dict(_summaries)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = SummarizeResponseDataGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        summarize_response_data = cls(
            summaries=summaries,
            groups=groups,
        )

        summarize_response_data.additional_properties = d
        return summarize_response_data

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
