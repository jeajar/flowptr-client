from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.self_link import SelfLink
    from ..models.webhook_record_response_data import WebhookRecordResponseData


T = TypeVar("T", bound="WebhookRecordResponse")


@_attrs_define
class WebhookRecordResponse:
    """
    Example:
        {'data': {'id': '04684d89-1ff6-4775-9685-f6771f5d3658', 'num_deliveries': 0, 'url': 'https://test_server',
            'entity_types': {'Asset': {'create': ['code', 'description']}}, 'status': 'stable', 'name': 'Asset Webhook',
            'description': "Webhook for Asset creation and updates of 'code' and 'description'", 'validate_ssl_cert': True,
            'batch_deliveries': False}, 'links': {'self': '/api/v1.1/webhook/hooks/04684d89-1ff6-4775-9685-f6771f5d3658'}}

    Attributes:
        data (Union[Unset, WebhookRecordResponseData]):
        links (Union[Unset, SelfLink]):
    """

    data: Union[Unset, "WebhookRecordResponseData"] = UNSET
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
        from ..models.self_link import SelfLink
        from ..models.webhook_record_response_data import WebhookRecordResponseData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, WebhookRecordResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WebhookRecordResponseData.from_dict(_data)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfLink]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfLink.from_dict(_links)

        webhook_record_response = cls(
            data=data,
            links=links,
        )

        webhook_record_response.additional_properties = d
        return webhook_record_response

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
