from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_webhook_index_response_data_item import GetWebhookIndexResponseDataItem
    from ..models.pagination_links import PaginationLinks


T = TypeVar("T", bound="GetWebhookIndexResponse")


@_attrs_define
class GetWebhookIndexResponse:
    """
    Example:
        {'data': [{'id': '04684d89-1ff6-4775-9685-f6771f5d3658', 'num_deliveries': 0, 'url': 'https://test_server',
            'entity_types': {'Asset': {'create': []}}, 'status': 'stable', 'name': 'Asset Create Webhook', 'description':
            'Webhook for Asset creation', 'validate_ssl_cert': True, 'batch_deliveries': False}, {'id':
            '1c7122f3-9fc3-433c-8a34-fad96483532a', 'num_deliveries': 0, 'url': 'https://test_server', 'entity_types':
            {'Asset': {'update': ['code', 'description']}}, 'status': 'stable', 'name': 'Asset Update Webhook',
            'description': "Webhook for Asset updates of 'code' and 'description'", 'validate_ssl_cert': True,
            'batch_deliveries': False}], 'links': {'self': '/api/v1.1/webhook/hooks?page%5Bnumber%5D=2&page%5Bsize%5D=2',
            'next': '/api/v1.1/webhook/hooks?page%5Bnumber%5D=3&page%5Bsize%5D=2', 'prev':
            '/api/v1.1/webhook/hooks?page%5Bnumber%5D=1&page%5Bsize%5D=2'}}

    Attributes:
        data (Union[Unset, list['GetWebhookIndexResponseDataItem']]): An array of found webhooks.
        links (Union[Unset, PaginationLinks]):
    """

    data: Union[Unset, list["GetWebhookIndexResponseDataItem"]] = UNSET
    links: Union[Unset, "PaginationLinks"] = UNSET
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
        from ..models.get_webhook_index_response_data_item import GetWebhookIndexResponseDataItem
        from ..models.pagination_links import PaginationLinks

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = GetWebhookIndexResponseDataItem.from_dict(data_item_data)

            data.append(data_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, PaginationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PaginationLinks.from_dict(_links)

        get_webhook_index_response = cls(
            data=data,
            links=links,
        )

        get_webhook_index_response.additional_properties = d
        return get_webhook_index_response

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
