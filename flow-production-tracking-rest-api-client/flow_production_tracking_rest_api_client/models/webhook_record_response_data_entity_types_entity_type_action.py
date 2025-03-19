from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookRecordResponseDataEntityTypesEntityTypeAction")


@_attrs_define
class WebhookRecordResponseDataEntityTypesEntityTypeAction:
    """Each key of the hash is an entity type. Each value is an hash where the key is the action the key the webhook is
    interested in. Allowed values are: 'create, update, delete'

        Attributes:
            field_name (Union[Unset, list[str]]): Field name to be returned by webhook.
    """

    field_name: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name: Union[Unset, list[str]] = UNSET
        if not isinstance(self.field_name, Unset):
            field_name = self.field_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_name is not UNSET:
            field_dict["field_name"] = field_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = cast(list[str], d.pop("field_name", UNSET))

        webhook_record_response_data_entity_types_entity_type_action = cls(
            field_name=field_name,
        )

        webhook_record_response_data_entity_types_entity_type_action.additional_properties = d
        return webhook_record_response_data_entity_types_entity_type_action

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
