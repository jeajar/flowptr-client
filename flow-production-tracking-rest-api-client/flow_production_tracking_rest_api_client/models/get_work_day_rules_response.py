from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_work_day_rules_response_data_item import GetWorkDayRulesResponseDataItem
    from ..models.self_link import SelfLink


T = TypeVar("T", bound="GetWorkDayRulesResponse")


@_attrs_define
class GetWorkDayRulesResponse:
    """
    Example:
        {'data': [{'date': '2012-01-01', 'working': False, 'description': None, 'reason': 'STUDIO_WORK_WEEK'}, {'date':
            '2012-01-02', 'working': False, 'description': None, 'reason': 'STUDIO_WORK_WEEK'}], 'links': {'self':
            '/api/v1.1/schedule/work_day_rules?end_date=2012-01-02&project_id=1&start_date=2012-01-01&user_id=1'}}

    Attributes:
        data (Union[Unset, list['GetWorkDayRulesResponseDataItem']]): An array of found work day rules.
        links (Union[Unset, SelfLink]):
    """

    data: Union[Unset, list["GetWorkDayRulesResponseDataItem"]] = UNSET
    links: Union[Unset, "SelfLink"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_work_day_rules_response_data_item import GetWorkDayRulesResponseDataItem
        from ..models.self_link import SelfLink

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = GetWorkDayRulesResponseDataItem.from_dict(data_item_data)

            data.append(data_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfLink]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfLink.from_dict(_links)

        get_work_day_rules_response = cls(
            data=data,
            links=links,
        )

        get_work_day_rules_response.additional_properties = d
        return get_work_day_rules_response

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
