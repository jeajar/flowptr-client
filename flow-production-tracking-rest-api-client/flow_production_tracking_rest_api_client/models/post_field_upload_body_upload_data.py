from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_field_upload_body_upload_data_tags_item import PostFieldUploadBodyUploadDataTagsItem


T = TypeVar("T", bound="PostFieldUploadBodyUploadData")


@_attrs_define
class PostFieldUploadBodyUploadData:
    """
    Attributes:
        display_name (Union[Unset, str]): Optional display name for an Attachment.
        tags (Union[Unset, list['PostFieldUploadBodyUploadDataTagsItem']]): Tags to link to an Attachment.
    """

    display_name: Union[Unset, str] = UNSET
    tags: Union[Unset, list["PostFieldUploadBodyUploadDataTagsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_field_upload_body_upload_data_tags_item import PostFieldUploadBodyUploadDataTagsItem

        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = PostFieldUploadBodyUploadDataTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        post_field_upload_body_upload_data = cls(
            display_name=display_name,
            tags=tags,
        )

        post_field_upload_body_upload_data.additional_properties = d
        return post_field_upload_body_upload_data

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
