from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hierarchy_search_request_search_criteria import HierarchySearchRequestSearchCriteria


T = TypeVar("T", bound="HierarchySearchRequest")


@_attrs_define
class HierarchySearchRequest:
    """
    Attributes:
        search_criteria (HierarchySearchRequestSearchCriteria): This object must contain only one of the properties
            below.
        root_path (Union[Unset, str]): Path from which the search should start. If not specified, all projects are
            searched.
        seed_entity_field (Union[Unset, str]): Indicates the schema to use for the provided path. This seed is expected
            to be an 'entity' field.
    """

    search_criteria: "HierarchySearchRequestSearchCriteria"
    root_path: Union[Unset, str] = UNSET
    seed_entity_field: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_criteria = self.search_criteria.to_dict()

        root_path = self.root_path

        seed_entity_field = self.seed_entity_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "search_criteria": search_criteria,
            }
        )
        if root_path is not UNSET:
            field_dict["root_path"] = root_path
        if seed_entity_field is not UNSET:
            field_dict["seed_entity_field"] = seed_entity_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hierarchy_search_request_search_criteria import HierarchySearchRequestSearchCriteria

        d = dict(src_dict)
        search_criteria = HierarchySearchRequestSearchCriteria.from_dict(d.pop("search_criteria"))

        root_path = d.pop("root_path", UNSET)

        seed_entity_field = d.pop("seed_entity_field", UNSET)

        hierarchy_search_request = cls(
            search_criteria=search_criteria,
            root_path=root_path,
            seed_entity_field=seed_entity_field,
        )

        hierarchy_search_request.additional_properties = d
        return hierarchy_search_request

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
