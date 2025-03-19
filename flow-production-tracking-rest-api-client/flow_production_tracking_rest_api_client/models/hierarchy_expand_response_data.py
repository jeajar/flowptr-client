from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hierarchy_expand_response import HierarchyExpandResponse
    from ..models.hierarchy_expand_response_data_ref import HierarchyExpandResponseDataRef
    from ..models.hierarchy_expand_response_data_target_entities import HierarchyExpandResponseDataTargetEntities


T = TypeVar("T", bound="HierarchyExpandResponseData")


@_attrs_define
class HierarchyExpandResponseData:
    """The navigation tree at a specific level.

    Attributes:
        label (Union[Unset, str]): The name of the tree node. Example: Car.
        ref (Union[Unset, HierarchyExpandResponseDataRef]): Reference to the object the tree node is representing.
        parent_path (Union[Unset, str]): Absolute path that corresponds to the parent of this tree node.
        path (Union[Unset, str]): Absolute path that corresponds to this tree node.
        target_entities (Union[Unset, HierarchyExpandResponseDataTargetEntities]): Seed for a CRUD query to get the
            target entities associated to the tree node.
        has_children (Union[Unset, bool]): Indicates if this node has children nodes.
        children (Union[Unset, list['HierarchyExpandResponse']]): When present, contains all the children of this node.
    """

    label: Union[Unset, str] = UNSET
    ref: Union[Unset, "HierarchyExpandResponseDataRef"] = UNSET
    parent_path: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    target_entities: Union[Unset, "HierarchyExpandResponseDataTargetEntities"] = UNSET
    has_children: Union[Unset, bool] = UNSET
    children: Union[Unset, list["HierarchyExpandResponse"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ref, Unset):
            ref = self.ref.to_dict()

        parent_path = self.parent_path

        path = self.path

        target_entities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target_entities, Unset):
            target_entities = self.target_entities.to_dict()

        has_children = self.has_children

        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if ref is not UNSET:
            field_dict["ref"] = ref
        if parent_path is not UNSET:
            field_dict["parent_path"] = parent_path
        if path is not UNSET:
            field_dict["path"] = path
        if target_entities is not UNSET:
            field_dict["target_entities"] = target_entities
        if has_children is not UNSET:
            field_dict["has_children"] = has_children
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hierarchy_expand_response import HierarchyExpandResponse
        from ..models.hierarchy_expand_response_data_ref import HierarchyExpandResponseDataRef
        from ..models.hierarchy_expand_response_data_target_entities import HierarchyExpandResponseDataTargetEntities

        d = dict(src_dict)
        label = d.pop("label", UNSET)

        _ref = d.pop("ref", UNSET)
        ref: Union[Unset, HierarchyExpandResponseDataRef]
        if isinstance(_ref, Unset):
            ref = UNSET
        else:
            ref = HierarchyExpandResponseDataRef.from_dict(_ref)

        parent_path = d.pop("parent_path", UNSET)

        path = d.pop("path", UNSET)

        _target_entities = d.pop("target_entities", UNSET)
        target_entities: Union[Unset, HierarchyExpandResponseDataTargetEntities]
        if isinstance(_target_entities, Unset):
            target_entities = UNSET
        else:
            target_entities = HierarchyExpandResponseDataTargetEntities.from_dict(_target_entities)

        has_children = d.pop("has_children", UNSET)

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = HierarchyExpandResponse.from_dict(children_item_data)

            children.append(children_item)

        hierarchy_expand_response_data = cls(
            label=label,
            ref=ref,
            parent_path=parent_path,
            path=path,
            target_entities=target_entities,
            has_children=has_children,
            children=children,
        )

        hierarchy_expand_response_data.additional_properties = d
        return hierarchy_expand_response_data

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
