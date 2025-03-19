from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_update_update_type import ActivityUpdateUpdateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_update_created_by import ActivityUpdateCreatedBy
    from ..models.activity_update_meta import ActivityUpdateMeta
    from ..models.activity_update_primary_entity import ActivityUpdatePrimaryEntity


T = TypeVar("T", bound="ActivityUpdate")


@_attrs_define
class ActivityUpdate:
    """
    Attributes:
        id (Union[Unset, int]): The record id associated with the activity update. Example: 86.
        update_type (Union[Unset, ActivityUpdateUpdateType]): Describes what type of activity update occured. Default:
            ActivityUpdateUpdateType.UPDATE.
        meta (Union[Unset, ActivityUpdateMeta]): Detailed view of the update.
        created_at (Union[Unset, str]): The ISO 8601 timestamp of the creation of the entity. Example:
            2018-05-30T04:57:24Z.
        read (Union[Unset, bool]):
        primary_entity (Union[Unset, ActivityUpdatePrimaryEntity]):
        created_by (Union[Unset, ActivityUpdateCreatedBy]):
    """

    id: Union[Unset, int] = UNSET
    update_type: Union[Unset, ActivityUpdateUpdateType] = ActivityUpdateUpdateType.UPDATE
    meta: Union[Unset, "ActivityUpdateMeta"] = UNSET
    created_at: Union[Unset, str] = UNSET
    read: Union[Unset, bool] = UNSET
    primary_entity: Union[Unset, "ActivityUpdatePrimaryEntity"] = UNSET
    created_by: Union[Unset, "ActivityUpdateCreatedBy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        update_type: Union[Unset, str] = UNSET
        if not isinstance(self.update_type, Unset):
            update_type = self.update_type.value

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        created_at = self.created_at

        read = self.read

        primary_entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_entity, Unset):
            primary_entity = self.primary_entity.to_dict()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if update_type is not UNSET:
            field_dict["update_type"] = update_type
        if meta is not UNSET:
            field_dict["meta"] = meta
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if read is not UNSET:
            field_dict["read"] = read
        if primary_entity is not UNSET:
            field_dict["primary_entity"] = primary_entity
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_update_created_by import ActivityUpdateCreatedBy
        from ..models.activity_update_meta import ActivityUpdateMeta
        from ..models.activity_update_primary_entity import ActivityUpdatePrimaryEntity

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _update_type = d.pop("update_type", UNSET)
        update_type: Union[Unset, ActivityUpdateUpdateType]
        if isinstance(_update_type, Unset):
            update_type = UNSET
        else:
            update_type = ActivityUpdateUpdateType(_update_type)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ActivityUpdateMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ActivityUpdateMeta.from_dict(_meta)

        created_at = d.pop("created_at", UNSET)

        read = d.pop("read", UNSET)

        _primary_entity = d.pop("primary_entity", UNSET)
        primary_entity: Union[Unset, ActivityUpdatePrimaryEntity]
        if isinstance(_primary_entity, Unset):
            primary_entity = UNSET
        else:
            primary_entity = ActivityUpdatePrimaryEntity.from_dict(_primary_entity)

        _created_by = d.pop("created_by", UNSET)
        created_by: Union[Unset, ActivityUpdateCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ActivityUpdateCreatedBy.from_dict(_created_by)

        activity_update = cls(
            id=id,
            update_type=update_type,
            meta=meta,
            created_at=created_at,
            read=read,
            primary_entity=primary_entity,
            created_by=created_by,
        )

        activity_update.additional_properties = d
        return activity_update

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
