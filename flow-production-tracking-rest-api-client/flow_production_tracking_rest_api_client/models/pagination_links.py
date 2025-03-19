from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationLinks")


@_attrs_define
class PaginationLinks:
    """
    Attributes:
        self_ (Union[Unset, str]): Link to current page of results Example:
            /api/v1.1/projects?page%5Bnumber%5D=2&page%5Bsize%5D=500.
        next_ (Union[Unset, str]): Link to next page of results Example:
            /api/v1.1/projects?page%5Bnumber%5D=3&page%5Bsize%5D=500.
        prev (Union[Unset, str]): Link to previous page of results. Only present if the current page number is greater
            than 1. Example: /api/v1.1/projects?page%5Bnumber%5D=1&page%5Bsize%5D=500.
    """

    self_: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    prev: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_

        next_ = self.next_

        prev = self.prev

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if next_ is not UNSET:
            field_dict["next"] = next_
        if prev is not UNSET:
            field_dict["prev"] = prev

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        self_ = d.pop("self", UNSET)

        next_ = d.pop("next", UNSET)

        prev = d.pop("prev", UNSET)

        pagination_links = cls(
            self_=self_,
            next_=next_,
            prev=prev,
        )

        pagination_links.additional_properties = d
        return pagination_links

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
