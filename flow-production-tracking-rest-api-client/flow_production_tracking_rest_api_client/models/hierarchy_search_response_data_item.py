from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hierarchy_search_response_data_item_ref import HierarchySearchResponseDataItemRef


T = TypeVar("T", bound="HierarchySearchResponseDataItem")


@_attrs_define
class HierarchySearchResponseDataItem:
    """
    Attributes:
        label (Union[Unset, str]): Name of the corresponding entity.
        incremental_path (Union[Unset, list[str]]): Each string of the array corresponds to a path to use with the
            nav_expand function to dig through the tree.
        path_label (Union[Unset, str]): Path label to be used in the client UI.
        ref (Union[Unset, HierarchySearchResponseDataItemRef]): Reference to the corresponding entity.
        project_id (Union[Unset, int]): Project of the entity.
    """

    label: Union[Unset, str] = UNSET
    incremental_path: Union[Unset, list[str]] = UNSET
    path_label: Union[Unset, str] = UNSET
    ref: Union[Unset, "HierarchySearchResponseDataItemRef"] = UNSET
    project_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        incremental_path: Union[Unset, list[str]] = UNSET
        if not isinstance(self.incremental_path, Unset):
            incremental_path = self.incremental_path

        path_label = self.path_label

        ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ref, Unset):
            ref = self.ref.to_dict()

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if incremental_path is not UNSET:
            field_dict["incremental_path"] = incremental_path
        if path_label is not UNSET:
            field_dict["path_label"] = path_label
        if ref is not UNSET:
            field_dict["ref"] = ref
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hierarchy_search_response_data_item_ref import HierarchySearchResponseDataItemRef

        d = dict(src_dict)
        label = d.pop("label", UNSET)

        incremental_path = cast(list[str], d.pop("incremental_path", UNSET))

        path_label = d.pop("path_label", UNSET)

        _ref = d.pop("ref", UNSET)
        ref: Union[Unset, HierarchySearchResponseDataItemRef]
        if isinstance(_ref, Unset):
            ref = UNSET
        else:
            ref = HierarchySearchResponseDataItemRef.from_dict(_ref)

        project_id = d.pop("project_id", UNSET)

        hierarchy_search_response_data_item = cls(
            label=label,
            incremental_path=incremental_path,
            path_label=path_label,
            ref=ref,
            project_id=project_id,
        )

        hierarchy_search_response_data_item.additional_properties = d
        return hierarchy_search_response_data_item

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
