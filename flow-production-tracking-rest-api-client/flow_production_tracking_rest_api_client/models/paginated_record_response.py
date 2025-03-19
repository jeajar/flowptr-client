from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_links import PaginationLinks
    from ..models.record import Record


T = TypeVar("T", bound="PaginatedRecordResponse")


@_attrs_define
class PaginatedRecordResponse:
    """
    Attributes:
        data (Union[Unset, list['Record']]):
        links (Union[Unset, PaginationLinks]):
    """

    data: Union[Unset, list["Record"]] = UNSET
    links: Union[Unset, "PaginationLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

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
        from ..models.pagination_links import PaginationLinks
        from ..models.record import Record

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = Record.from_dict(data_item_data)

            data.append(data_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, PaginationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PaginationLinks.from_dict(_links)

        paginated_record_response = cls(
            data=data,
            links=links,
        )

        paginated_record_response.additional_properties = d
        return paginated_record_response

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
