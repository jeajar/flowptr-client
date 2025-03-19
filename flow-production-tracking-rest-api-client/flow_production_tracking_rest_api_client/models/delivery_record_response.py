from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_record_response_data import DeliveryRecordResponseData
    from ..models.self_link import SelfLink


T = TypeVar("T", bound="DeliveryRecordResponse")


@_attrs_define
class DeliveryRecordResponse:
    """
    Example:
        {'data': {'id': '008b4850-d5d2-4c2b-bfb4-8c4331233c4a', 'event_time': 1540909354, 'status': 'delivered',
            'process_time': 936, 'body': '', 'response_code': 204, 'request_body': {'data': {'id': 857, 'meta': {'type':
            'attribute_change', 'entity_id': 0, 'new_value': '**********', 'old_value': '', 'entity_type': 'Asset',
            'attribute_name': 'sg_site_admin_login', 'field_data_type': 'text'}, 'user_id': 1, 'entity_id': 99, 'operation':
            'create', 'user_type': 'HumanUser', 'project_id': 65, 'entity_type': 'Asset'}, 'timestamp':
            '2019-02-28T21:52:57Z'}, 'acknowledgement': '', 'request_headers': {}, 'response_headers': {}}, 'links':
            {'self': '/api/v1.1/webhook/deliveries/008b4850-d5d2-4c2b-bfb4-8c4331233c4a'}}

    Attributes:
        data (Union[Unset, DeliveryRecordResponseData]):
        links (Union[Unset, SelfLink]):
    """

    data: Union[Unset, "DeliveryRecordResponseData"] = UNSET
    links: Union[Unset, "SelfLink"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
        from ..models.delivery_record_response_data import DeliveryRecordResponseData
        from ..models.self_link import SelfLink

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, DeliveryRecordResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DeliveryRecordResponseData.from_dict(_data)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfLink]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfLink.from_dict(_links)

        delivery_record_response = cls(
            data=data,
            links=links,
        )

        delivery_record_response.additional_properties = d
        return delivery_record_response

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
