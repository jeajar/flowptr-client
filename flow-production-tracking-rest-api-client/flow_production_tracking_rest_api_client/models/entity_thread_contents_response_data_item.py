from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityThreadContentsResponseDataItem")


@_attrs_define
class EntityThreadContentsResponseDataItem:
    """
    Attributes:
        id (Union[Unset, int]): Id of Entity Example: 82.
        type_ (Union[Unset, str]): Entity Type Example: Note.
        content (Union[Unset, str]): Content. Example: Some content.
        created_at (Union[Unset, str]): The ISO 8601 timestamp of the creation of the entity. Example:
            2018-05-30T04:57:24Z.
    """

    id: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        content = self.content

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        content = d.pop("content", UNSET)

        created_at = d.pop("created_at", UNSET)

        entity_thread_contents_response_data_item = cls(
            id=id,
            type_=type_,
            content=content,
            created_at=created_at,
        )

        entity_thread_contents_response_data_item.additional_properties = d
        return entity_thread_contents_response_data_item

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
