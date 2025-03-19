from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record import Record
    from ..models.self_link import SelfLink


T = TypeVar("T", bound="RelationshipsResponse")


@_attrs_define
class RelationshipsResponse:
    """
    Example:
        {'data': {'id': 24, 'name': 'Flow Production Tracking Support', 'type': 'HumanUser'}, 'links': {'self':
            '/api/v1.1/entity/projects/82/relationships/created_by'}}

    Attributes:
        data (Union['Record', Unset, list['Record']]):
        links (Union[Unset, SelfLink]):
    """

    data: Union["Record", Unset, list["Record"]] = UNSET
    links: Union[Unset, "SelfLink"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.record import Record

        data: Union[Unset, dict[str, Any], list[dict[str, Any]]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, Record):
            data = self.data.to_dict()
        else:
            data = []
            for data_type_1_item_data in self.data:
                data_type_1_item = data_type_1_item_data.to_dict()
                data.append(data_type_1_item)

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
        from ..models.record import Record
        from ..models.self_link import SelfLink

        d = dict(src_dict)

        def _parse_data(data: object) -> Union["Record", Unset, list["Record"]]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = Record.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            data_type_1 = []
            _data_type_1 = data
            for data_type_1_item_data in _data_type_1:
                data_type_1_item = Record.from_dict(data_type_1_item_data)

                data_type_1.append(data_type_1_item)

            return data_type_1

        data = _parse_data(d.pop("data", UNSET))

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfLink]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfLink.from_dict(_links)

        relationships_response = cls(
            data=data,
            links=links,
        )

        relationships_response.additional_properties = d
        return relationships_response

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
