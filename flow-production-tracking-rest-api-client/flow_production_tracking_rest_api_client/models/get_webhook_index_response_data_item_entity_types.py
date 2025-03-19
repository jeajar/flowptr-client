from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_webhook_index_response_data_item_entity_types_entity_type import (
        GetWebhookIndexResponseDataItemEntityTypesEntityType,
    )


T = TypeVar("T", bound="GetWebhookIndexResponseDataItemEntityTypes")


@_attrs_define
class GetWebhookIndexResponseDataItemEntityTypes:
    """The filters for the webhook base on entity types and action. **Note that even though 'entity_types' is plural, only
    a single entity type is currently supported.**

        Attributes:
            entity_type (Union[Unset, GetWebhookIndexResponseDataItemEntityTypesEntityType]): Entity type name
    """

    entity_type: Union[Unset, "GetWebhookIndexResponseDataItemEntityTypesEntityType"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_webhook_index_response_data_item_entity_types_entity_type import (
            GetWebhookIndexResponseDataItemEntityTypesEntityType,
        )

        d = dict(src_dict)
        _entity_type = d.pop("entity_type", UNSET)
        entity_type: Union[Unset, GetWebhookIndexResponseDataItemEntityTypesEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = GetWebhookIndexResponseDataItemEntityTypesEntityType.from_dict(_entity_type)

        get_webhook_index_response_data_item_entity_types = cls(
            entity_type=entity_type,
        )

        get_webhook_index_response_data_item_entity_types.additional_properties = d
        return get_webhook_index_response_data_item_entity_types

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
