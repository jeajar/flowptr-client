from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hierarchy_expand_request_entity_fields_item import HierarchyExpandRequestEntityFieldsItem


T = TypeVar("T", bound="HierarchyExpandRequest")


@_attrs_define
class HierarchyExpandRequest:
    """
    Attributes:
        path (str): It provides the target navigation level and is composed of all information to get there.
        entity_fields (Union[Unset, list['HierarchyExpandRequestEntityFieldsItem']]): Indicates which fields to be
            returned when an entity is returned in the payload.
        seed_entity_field (Union[Unset, str]): Indicates the schema to be used for the provided path. This seed is
            expected to be an 'entity' field.
    """

    path: str
    entity_fields: Union[Unset, list["HierarchyExpandRequestEntityFieldsItem"]] = UNSET
    seed_entity_field: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        entity_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entity_fields, Unset):
            entity_fields = []
            for entity_fields_item_data in self.entity_fields:
                entity_fields_item = entity_fields_item_data.to_dict()
                entity_fields.append(entity_fields_item)

        seed_entity_field = self.seed_entity_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if entity_fields is not UNSET:
            field_dict["entity_fields"] = entity_fields
        if seed_entity_field is not UNSET:
            field_dict["seed_entity_field"] = seed_entity_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hierarchy_expand_request_entity_fields_item import HierarchyExpandRequestEntityFieldsItem

        d = dict(src_dict)
        path = d.pop("path")

        entity_fields = []
        _entity_fields = d.pop("entity_fields", UNSET)
        for entity_fields_item_data in _entity_fields or []:
            entity_fields_item = HierarchyExpandRequestEntityFieldsItem.from_dict(entity_fields_item_data)

            entity_fields.append(entity_fields_item)

        seed_entity_field = d.pop("seed_entity_field", UNSET)

        hierarchy_expand_request = cls(
            path=path,
            entity_fields=entity_fields,
            seed_entity_field=seed_entity_field,
        )

        hierarchy_expand_request.additional_properties = d
        return hierarchy_expand_request

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
