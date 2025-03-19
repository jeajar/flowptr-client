from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReadSubscriptionsResponse200")


@_attrs_define
class ReadSubscriptionsResponse200:
    """
    Attributes:
        user_id_subscription (str): The key is the user's id, the value is the subscription type
    """

    user_id_subscription: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id_subscription = self.user_id_subscription

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "[user_id]: subscription": user_id_subscription,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id_subscription = d.pop("[user_id]: subscription")

        read_subscriptions_response_200 = cls(
            user_id_subscription=user_id_subscription,
        )

        read_subscriptions_response_200.additional_properties = d
        return read_subscriptions_response_200

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
