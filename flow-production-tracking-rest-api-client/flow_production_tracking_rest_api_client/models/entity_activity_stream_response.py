from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_activity_stream_response_data import EntityActivityStreamResponseData
    from ..models.self_link import SelfLink


T = TypeVar("T", bound="EntityActivityStreamResponse")


@_attrs_define
class EntityActivityStreamResponse:
    """
    Example:
        {'data': {'entity_type': 'Shot', 'entity_id': 5, 'latest_update_id': 9, 'earliest_update_id': 0, 'updates':
            [{'id': 9, 'update_type': 'update', 'meta': {'type': 'attribute_change', 'attribute_name': 'sg_status_list',
            'entity_type': 'Shot', 'entity_id': 5, 'field_data_type': 'status_list', 'old_value': None, 'new_value': 'act'},
            'created_at': '2018-05-30T04:57:24Z', 'read': False, 'primary_entity': {'type': 'Shot', 'id': 5, 'name': 'shot
            5', 'status': 'act'}, 'created_by': {'type': 'ApiUser', 'id': 10, 'name': 'A api user', 'status': 'act',
            'image': None}}]}, 'links': {'self': '/api/v1.1/entity/shots/5/activity_stream'}}

    Attributes:
        data (Union[Unset, EntityActivityStreamResponseData]): The name of the entity and if the entity is visible.
        links (Union[Unset, SelfLink]):
    """

    data: Union[Unset, "EntityActivityStreamResponseData"] = UNSET
    links: Union[Unset, "SelfLink"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_activity_stream_response_data import EntityActivityStreamResponseData
        from ..models.self_link import SelfLink

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityActivityStreamResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = EntityActivityStreamResponseData.from_dict(_data)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfLink]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfLink.from_dict(_links)

        entity_activity_stream_response = cls(
            data=data,
            links=links,
        )

        entity_activity_stream_response.additional_properties = d
        return entity_activity_stream_response

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
