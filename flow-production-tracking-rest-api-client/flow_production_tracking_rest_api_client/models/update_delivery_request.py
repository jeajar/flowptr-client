from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateDeliveryRequest")


@_attrs_define
class UpdateDeliveryRequest:
    """
    Example:
        {'acknowledgement': 'My acknowledgement string or stringified JSON.'}

    Attributes:
        acknowledgement (str): An updatable value for services to indicate if they have processed the delivery. It has
            to be 4096 bytes long or less.
    """

    acknowledgement: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledgement = self.acknowledgement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acknowledgement": acknowledgement,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acknowledgement = d.pop("acknowledgement")

        update_delivery_request = cls(
            acknowledgement=acknowledgement,
        )

        update_delivery_request.additional_properties = d
        return update_delivery_request

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
