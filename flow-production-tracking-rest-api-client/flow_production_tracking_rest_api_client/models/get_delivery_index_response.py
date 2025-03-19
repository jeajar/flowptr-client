from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_delivery_index_response_data_item import GetDeliveryIndexResponseDataItem
    from ..models.get_delivery_index_response_included_item import GetDeliveryIndexResponseIncludedItem
    from ..models.pagination_links import PaginationLinks


T = TypeVar("T", bound="GetDeliveryIndexResponse")


@_attrs_define
class GetDeliveryIndexResponse:
    """
    Example:
        {'data': [{'id': '008b4850-d5d2-4c2b-bfb4-8c4331233c4a', 'event_time': 1540909354, 'status': 'delivered',
            'process_time': 936, 'body': '', 'response_code': 204, 'request_body': {'data': {'id': 857, 'meta': {'type':
            'attribute_change', 'entity_id': 0, 'new_value': '**********', 'old_value': '', 'entity_type': 'Asset',
            'attribute_name': 'sg_site_admin_login', 'field_data_type': 'text'}, 'user_id': 1, 'entity_id': 99, 'operation':
            'create', 'user_type': 'HumanUser', 'project_id': 65, 'entity_type': 'Asset'}, 'timestamp':
            '2019-02-28T21:52:57Z'}, 'acknowledgement': '', 'request_headers': {}, 'response_headers': {}}], 'links':
            {'self':
            '/api/v1.1/webhook/hook/4218f8cc-7bc9-44a8-883a-d20d537f6fb5/deliveries?page%5Bnumber%5D=2&page%5Bsize%5D=500',
            'next':
            '/api/v1.1/webhook/hook/4218f8cc-7bc9-44a8-883a-d20d537f6fb5/deliveries?page%5Bnumber%5D=3&page%5Bsize%5D=500',
            'prev':
            '/api/v1.1/webhook/hook/4218f8cc-7bc9-44a8-883a-d20d537f6fb5/deliveries?page%5Bnumber%5D=1&page%5Bsize%5D=500'}}

    Attributes:
        data (Union[Unset, list['GetDeliveryIndexResponseDataItem']]): An array of found deliveries.
        links (Union[Unset, PaginationLinks]):
        included (Union[Unset, list['GetDeliveryIndexResponseIncludedItem']]): An array of objects representing entities
            referenced by the found deliveries.
    """

    data: Union[Unset, list["GetDeliveryIndexResponseDataItem"]] = UNSET
    links: Union[Unset, "PaginationLinks"] = UNSET
    included: Union[Unset, list["GetDeliveryIndexResponseIncludedItem"]] = UNSET
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

        included: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if links is not UNSET:
            field_dict["links"] = links
        if included is not UNSET:
            field_dict["included"] = included

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_delivery_index_response_data_item import GetDeliveryIndexResponseDataItem
        from ..models.get_delivery_index_response_included_item import GetDeliveryIndexResponseIncludedItem
        from ..models.pagination_links import PaginationLinks

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = GetDeliveryIndexResponseDataItem.from_dict(data_item_data)

            data.append(data_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, PaginationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PaginationLinks.from_dict(_links)

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = GetDeliveryIndexResponseIncludedItem.from_dict(included_item_data)

            included.append(included_item)

        get_delivery_index_response = cls(
            data=data,
            links=links,
            included=included,
        )

        get_delivery_index_response.additional_properties = d
        return get_delivery_index_response

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
