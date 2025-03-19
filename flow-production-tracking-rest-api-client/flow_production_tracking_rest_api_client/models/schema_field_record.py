from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_field_record_properties import SchemaFieldRecordProperties
    from ..models.schema_response_value import SchemaResponseValue


T = TypeVar("T", bound="SchemaFieldRecord")


@_attrs_define
class SchemaFieldRecord:
    """The properties of a field.

    Attributes:
        name (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and indicates if it
            is editable.
        description (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and indicates
            if it is editable.
        entity_type (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and indicates
            if it is editable.
        data_type (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and indicates if
            it is editable.
        editable (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and indicates if
            it is editable.
        mandatory (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and indicates if
            it is editable.
        unique (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and indicates if it
            is editable.
        visible (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and indicates if
            it is editable.
        ui_value_displayable (Union[Unset, SchemaResponseValue]): Simple object that contains the attributes value and
            indicates if it is editable.
        properties (Union[Unset, SchemaFieldRecordProperties]): Additional field specific properties.
    """

    name: Union[Unset, "SchemaResponseValue"] = UNSET
    description: Union[Unset, "SchemaResponseValue"] = UNSET
    entity_type: Union[Unset, "SchemaResponseValue"] = UNSET
    data_type: Union[Unset, "SchemaResponseValue"] = UNSET
    editable: Union[Unset, "SchemaResponseValue"] = UNSET
    mandatory: Union[Unset, "SchemaResponseValue"] = UNSET
    unique: Union[Unset, "SchemaResponseValue"] = UNSET
    visible: Union[Unset, "SchemaResponseValue"] = UNSET
    ui_value_displayable: Union[Unset, "SchemaResponseValue"] = UNSET
    properties: Union[Unset, "SchemaFieldRecordProperties"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        entity_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.to_dict()

        data_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.to_dict()

        editable: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.editable, Unset):
            editable = self.editable.to_dict()

        mandatory: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mandatory, Unset):
            mandatory = self.mandatory.to_dict()

        unique: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.unique, Unset):
            unique = self.unique.to_dict()

        visible: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.visible, Unset):
            visible = self.visible.to_dict()

        ui_value_displayable: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ui_value_displayable, Unset):
            ui_value_displayable = self.ui_value_displayable.to_dict()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if editable is not UNSET:
            field_dict["editable"] = editable
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if unique is not UNSET:
            field_dict["unique"] = unique
        if visible is not UNSET:
            field_dict["visible"] = visible
        if ui_value_displayable is not UNSET:
            field_dict["ui_value_displayable"] = ui_value_displayable
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_field_record_properties import SchemaFieldRecordProperties
        from ..models.schema_response_value import SchemaResponseValue

        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, SchemaResponseValue]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = SchemaResponseValue.from_dict(_name)

        _description = d.pop("description", UNSET)
        description: Union[Unset, SchemaResponseValue]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = SchemaResponseValue.from_dict(_description)

        _entity_type = d.pop("entity_type", UNSET)
        entity_type: Union[Unset, SchemaResponseValue]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = SchemaResponseValue.from_dict(_entity_type)

        _data_type = d.pop("data_type", UNSET)
        data_type: Union[Unset, SchemaResponseValue]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = SchemaResponseValue.from_dict(_data_type)

        _editable = d.pop("editable", UNSET)
        editable: Union[Unset, SchemaResponseValue]
        if isinstance(_editable, Unset):
            editable = UNSET
        else:
            editable = SchemaResponseValue.from_dict(_editable)

        _mandatory = d.pop("mandatory", UNSET)
        mandatory: Union[Unset, SchemaResponseValue]
        if isinstance(_mandatory, Unset):
            mandatory = UNSET
        else:
            mandatory = SchemaResponseValue.from_dict(_mandatory)

        _unique = d.pop("unique", UNSET)
        unique: Union[Unset, SchemaResponseValue]
        if isinstance(_unique, Unset):
            unique = UNSET
        else:
            unique = SchemaResponseValue.from_dict(_unique)

        _visible = d.pop("visible", UNSET)
        visible: Union[Unset, SchemaResponseValue]
        if isinstance(_visible, Unset):
            visible = UNSET
        else:
            visible = SchemaResponseValue.from_dict(_visible)

        _ui_value_displayable = d.pop("ui_value_displayable", UNSET)
        ui_value_displayable: Union[Unset, SchemaResponseValue]
        if isinstance(_ui_value_displayable, Unset):
            ui_value_displayable = UNSET
        else:
            ui_value_displayable = SchemaResponseValue.from_dict(_ui_value_displayable)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, SchemaFieldRecordProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = SchemaFieldRecordProperties.from_dict(_properties)

        schema_field_record = cls(
            name=name,
            description=description,
            entity_type=entity_type,
            data_type=data_type,
            editable=editable,
            mandatory=mandatory,
            unique=unique,
            visible=visible,
            ui_value_displayable=ui_value_displayable,
            properties=properties,
        )

        schema_field_record.additional_properties = d
        return schema_field_record

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
