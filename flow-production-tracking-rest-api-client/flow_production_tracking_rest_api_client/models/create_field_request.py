from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_field_request_data_type import CreateFieldRequestDataType

if TYPE_CHECKING:
    from ..models.create_update_field_property import CreateUpdateFieldProperty


T = TypeVar("T", bound="CreateFieldRequest")


@_attrs_define
class CreateFieldRequest:
    """
    Attributes:
        data_type (CreateFieldRequestDataType): The data type of the field to create.
        properties (list['CreateUpdateFieldProperty']): The properties to set for the field.
    """

    data_type: CreateFieldRequestDataType
    properties: list["CreateUpdateFieldProperty"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_type = self.data_type.value

        properties = []
        for properties_item_data in self.properties:
            properties_item = properties_item_data.to_dict()
            properties.append(properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_type": data_type,
                "properties": properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_update_field_property import CreateUpdateFieldProperty

        d = dict(src_dict)
        data_type = CreateFieldRequestDataType(d.pop("data_type"))

        properties = []
        _properties = d.pop("properties")
        for properties_item_data in _properties:
            properties_item = CreateUpdateFieldProperty.from_dict(properties_item_data)

            properties.append(properties_item)

        create_field_request = cls(
            data_type=data_type,
            properties=properties,
        )

        create_field_request.additional_properties = d
        return create_field_request

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
