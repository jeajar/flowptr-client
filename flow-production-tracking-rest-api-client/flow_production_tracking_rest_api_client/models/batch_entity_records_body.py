from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_entity_records_body_requests_item import BatchEntityRecordsBodyRequestsItem


T = TypeVar("T", bound="BatchEntityRecordsBody")


@_attrs_define
class BatchEntityRecordsBody:
    """
    Example:
        {'requests': [{'request_type': 'create', 'entity': 'Project', 'data': {'code': 'new project'}, 'options':
            {'fields': ['code']}}]}

    Attributes:
        requests (Union[Unset, list['BatchEntityRecordsBodyRequestsItem']]):
    """

    requests: Union[Unset, list["BatchEntityRecordsBodyRequestsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requests: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.requests, Unset):
            requests = []
            for requests_item_data in self.requests:
                requests_item = requests_item_data.to_dict()
                requests.append(requests_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requests is not UNSET:
            field_dict["requests"] = requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_entity_records_body_requests_item import BatchEntityRecordsBodyRequestsItem

        d = dict(src_dict)
        requests = []
        _requests = d.pop("requests", UNSET)
        for requests_item_data in _requests or []:
            requests_item = BatchEntityRecordsBodyRequestsItem.from_dict(requests_item_data)

            requests.append(requests_item)

        batch_entity_records_body = cls(
            requests=requests,
        )

        batch_entity_records_body.additional_properties = d
        return batch_entity_records_body

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
