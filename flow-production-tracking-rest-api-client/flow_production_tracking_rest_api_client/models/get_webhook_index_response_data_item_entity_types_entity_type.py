from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_webhook_index_response_data_item_entity_types_entity_type_action import (
        GetWebhookIndexResponseDataItemEntityTypesEntityTypeAction,
    )


T = TypeVar("T", bound="GetWebhookIndexResponseDataItemEntityTypesEntityType")


@_attrs_define
class GetWebhookIndexResponseDataItemEntityTypesEntityType:
    """Entity type name

    Attributes:
        action (Union[Unset, GetWebhookIndexResponseDataItemEntityTypesEntityTypeAction]): Each key of the hash is an
            entity type. Each value is an hash where the key is the action the key the webhook is interested in. Allowed
            values are: 'create, update, delete'
    """

    action: Union[Unset, "GetWebhookIndexResponseDataItemEntityTypesEntityTypeAction"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_webhook_index_response_data_item_entity_types_entity_type_action import (
            GetWebhookIndexResponseDataItemEntityTypesEntityTypeAction,
        )

        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: Union[Unset, GetWebhookIndexResponseDataItemEntityTypesEntityTypeAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = GetWebhookIndexResponseDataItemEntityTypesEntityTypeAction.from_dict(_action)

        get_webhook_index_response_data_item_entity_types_entity_type = cls(
            action=action,
        )

        get_webhook_index_response_data_item_entity_types_entity_type.additional_properties = d
        return get_webhook_index_response_data_item_entity_types_entity_type

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
