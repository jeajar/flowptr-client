from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_delivery_index_response_included_item_attributes import (
        GetDeliveryIndexResponseIncludedItemAttributes,
    )


T = TypeVar("T", bound="GetDeliveryIndexResponseIncludedItem")


@_attrs_define
class GetDeliveryIndexResponseIncludedItem:
    """
    Attributes:
        type_ (Union[Unset, str]): The entity type.
        id (Union[Unset, int]): The entity id.
        attributes (Union[Unset, GetDeliveryIndexResponseIncludedItemAttributes]): A hash of any record attributes
            requested.
    """

    type_: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    attributes: Union[Unset, "GetDeliveryIndexResponseIncludedItemAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_delivery_index_response_included_item_attributes import (
            GetDeliveryIndexResponseIncludedItemAttributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, GetDeliveryIndexResponseIncludedItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = GetDeliveryIndexResponseIncludedItemAttributes.from_dict(_attributes)

        get_delivery_index_response_included_item = cls(
            type_=type_,
            id=id,
            attributes=attributes,
        )

        get_delivery_index_response_included_item.additional_properties = d
        return get_delivery_index_response_included_item

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
