from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_webhook_index_response_data_item_entity_types import GetWebhookIndexResponseDataItemEntityTypes


T = TypeVar("T", bound="GetWebhookIndexResponseDataItem")


@_attrs_define
class GetWebhookIndexResponseDataItem:
    """
    Attributes:
        id (Union[Unset, str]): GUID based id of the webhook.
        num_deliveries (Union[Unset, int]): Numbers of deliveries of the webhook.
        url (Union[Unset, str]): Webhook target url.
        entity_types (Union[Unset, GetWebhookIndexResponseDataItemEntityTypes]): The filters for the webhook base on
            entity types and action. **Note that even though 'entity_types' is plural, only a single entity type is
            currently supported.**
        status (Union[Unset, str]): Status of the webhook we are looking for.
        name (Union[Unset, str]): Name of the webhook
        description (Union[Unset, str]): Description of the webhook
        validate_ssl_cert (Union[Unset, bool]): Indicates if the request to the webhook service should validate the SSL
            certificate.
        batch_deliveries (Union[Unset, bool]): Indicates if the webhook should deliver batches or single deliveries
    """

    id: Union[Unset, str] = UNSET
    num_deliveries: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    entity_types: Union[Unset, "GetWebhookIndexResponseDataItemEntityTypes"] = UNSET
    status: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    validate_ssl_cert: Union[Unset, bool] = UNSET
    batch_deliveries: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        num_deliveries = self.num_deliveries

        url = self.url

        entity_types: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity_types, Unset):
            entity_types = self.entity_types.to_dict()

        status = self.status

        name = self.name

        description = self.description

        validate_ssl_cert = self.validate_ssl_cert

        batch_deliveries = self.batch_deliveries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if num_deliveries is not UNSET:
            field_dict["num_deliveries"] = num_deliveries
        if url is not UNSET:
            field_dict["url"] = url
        if entity_types is not UNSET:
            field_dict["entity_types"] = entity_types
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if validate_ssl_cert is not UNSET:
            field_dict["validate_ssl_cert"] = validate_ssl_cert
        if batch_deliveries is not UNSET:
            field_dict["batch_deliveries"] = batch_deliveries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_webhook_index_response_data_item_entity_types import (
            GetWebhookIndexResponseDataItemEntityTypes,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        num_deliveries = d.pop("num_deliveries", UNSET)

        url = d.pop("url", UNSET)

        _entity_types = d.pop("entity_types", UNSET)
        entity_types: Union[Unset, GetWebhookIndexResponseDataItemEntityTypes]
        if isinstance(_entity_types, Unset):
            entity_types = UNSET
        else:
            entity_types = GetWebhookIndexResponseDataItemEntityTypes.from_dict(_entity_types)

        status = d.pop("status", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        validate_ssl_cert = d.pop("validate_ssl_cert", UNSET)

        batch_deliveries = d.pop("batch_deliveries", UNSET)

        get_webhook_index_response_data_item = cls(
            id=id,
            num_deliveries=num_deliveries,
            url=url,
            entity_types=entity_types,
            status=status,
            name=name,
            description=description,
            validate_ssl_cert=validate_ssl_cert,
            batch_deliveries=batch_deliveries,
        )

        get_webhook_index_response_data_item.additional_properties = d
        return get_webhook_index_response_data_item

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
