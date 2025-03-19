from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_update_field_property import CreateUpdateFieldProperty


T = TypeVar("T", bound="UpdateFieldRequest")


@_attrs_define
class UpdateFieldRequest:
    """
    Attributes:
        properties (list['CreateUpdateFieldProperty']): The properties to set for the field.
        project_id (Union[Unset, int]): Optional project id specifying which project to modify the ``visible`` property
            for.
    """

    properties: list["CreateUpdateFieldProperty"]
    project_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        properties = []
        for properties_item_data in self.properties:
            properties_item = properties_item_data.to_dict()
            properties.append(properties_item)

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "properties": properties,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_update_field_property import CreateUpdateFieldProperty

        d = dict(src_dict)
        properties = []
        _properties = d.pop("properties")
        for properties_item_data in _properties:
            properties_item = CreateUpdateFieldProperty.from_dict(properties_item_data)

            properties.append(properties_item)

        project_id = d.pop("project_id", UNSET)

        update_field_request = cls(
            properties=properties,
            project_id=project_id,
        )

        update_field_request.additional_properties = d
        return update_field_request

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
