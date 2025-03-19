from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_entity_records_body_requests_item_request_type import BatchEntityRecordsBodyRequestsItemRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_entity_records_body_requests_item_data import BatchEntityRecordsBodyRequestsItemData
    from ..models.batch_return_fields_options_parameter import BatchReturnFieldsOptionsParameter


T = TypeVar("T", bound="BatchEntityRecordsBodyRequestsItem")


@_attrs_define
class BatchEntityRecordsBodyRequestsItem:
    """
    Attributes:
        request_type (Union[Unset, BatchEntityRecordsBodyRequestsItemRequestType]):
        entity (Union[Unset, str]): The entity type associated with the request. Example: Project.
        record_id (Union[Unset, int]): The record id associated with the request. Example: 86.
        options (Union[Unset, BatchReturnFieldsOptionsParameter]): Optional parameters for the `create` request type.
            Example: {'options': {'fields': ['field_1', 'field_2']}}.
        data (Union[Unset, BatchEntityRecordsBodyRequestsItemData]): The entity fields, as keys, and their associated
            values. Example: {'code': 'new project', 'name': 'My New Project'}.
    """

    request_type: Union[Unset, BatchEntityRecordsBodyRequestsItemRequestType] = UNSET
    entity: Union[Unset, str] = UNSET
    record_id: Union[Unset, int] = UNSET
    options: Union[Unset, "BatchReturnFieldsOptionsParameter"] = UNSET
    data: Union[Unset, "BatchEntityRecordsBodyRequestsItemData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_type: Union[Unset, str] = UNSET
        if not isinstance(self.request_type, Unset):
            request_type = self.request_type.value

        entity = self.entity

        record_id = self.record_id

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_type is not UNSET:
            field_dict["request_type"] = request_type
        if entity is not UNSET:
            field_dict["entity"] = entity
        if record_id is not UNSET:
            field_dict["record_id"] = record_id
        if options is not UNSET:
            field_dict["options"] = options
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_entity_records_body_requests_item_data import BatchEntityRecordsBodyRequestsItemData
        from ..models.batch_return_fields_options_parameter import BatchReturnFieldsOptionsParameter

        d = dict(src_dict)
        _request_type = d.pop("request_type", UNSET)
        request_type: Union[Unset, BatchEntityRecordsBodyRequestsItemRequestType]
        if isinstance(_request_type, Unset):
            request_type = UNSET
        else:
            request_type = BatchEntityRecordsBodyRequestsItemRequestType(_request_type)

        entity = d.pop("entity", UNSET)

        record_id = d.pop("record_id", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, BatchReturnFieldsOptionsParameter]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = BatchReturnFieldsOptionsParameter.from_dict(_options)

        _data = d.pop("data", UNSET)
        data: Union[Unset, BatchEntityRecordsBodyRequestsItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = BatchEntityRecordsBodyRequestsItemData.from_dict(_data)

        batch_entity_records_body_requests_item = cls(
            request_type=request_type,
            entity=entity,
            record_id=record_id,
            options=options,
            data=data,
        )

        batch_entity_records_body_requests_item.additional_properties = d
        return batch_entity_records_body_requests_item

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
