from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_update import ActivityUpdate


T = TypeVar("T", bound="EntityActivityStreamResponseData")


@_attrs_define
class EntityActivityStreamResponseData:
    """The name of the entity and if the entity is visible.

    Attributes:
        entity_id (Union[Unset, int]): Id of Entity Example: 82.
        entity_type (Union[Unset, str]): Entity Type Example: Project.
        latest_update_id (Union[Unset, int]): Last updated id. Example: {'name': 10}.
        earliest_update_id (Union[Unset, int]): Earliest updated id. Example: {'name': 1}.
        updates (Union[Unset, list['ActivityUpdate']]): Array of activities
    """

    entity_id: Union[Unset, int] = UNSET
    entity_type: Union[Unset, str] = UNSET
    latest_update_id: Union[Unset, int] = UNSET
    earliest_update_id: Union[Unset, int] = UNSET
    updates: Union[Unset, list["ActivityUpdate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        entity_type = self.entity_type

        latest_update_id = self.latest_update_id

        earliest_update_id = self.earliest_update_id

        updates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.updates, Unset):
            updates = []
            for updates_item_data in self.updates:
                updates_item = updates_item_data.to_dict()
                updates.append(updates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if latest_update_id is not UNSET:
            field_dict["latest_update_id"] = latest_update_id
        if earliest_update_id is not UNSET:
            field_dict["earliest_update_id"] = earliest_update_id
        if updates is not UNSET:
            field_dict["updates"] = updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_update import ActivityUpdate

        d = dict(src_dict)
        entity_id = d.pop("entity_id", UNSET)

        entity_type = d.pop("entity_type", UNSET)

        latest_update_id = d.pop("latest_update_id", UNSET)

        earliest_update_id = d.pop("earliest_update_id", UNSET)

        updates = []
        _updates = d.pop("updates", UNSET)
        for updates_item_data in _updates or []:
            updates_item = ActivityUpdate.from_dict(updates_item_data)

            updates.append(updates_item)

        entity_activity_stream_response_data = cls(
            entity_id=entity_id,
            entity_type=entity_type,
            latest_update_id=latest_update_id,
            earliest_update_id=earliest_update_id,
            updates=updates,
        )

        entity_activity_stream_response_data.additional_properties = d
        return entity_activity_stream_response_data

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
