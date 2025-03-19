from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.options_parameter_return_only import OptionsParameterReturnOnly
from ..types import UNSET, Unset

T = TypeVar("T", bound="OptionsParameter")


@_attrs_define
class OptionsParameter:
    """
    Example:
        {'include_archived_projects': False, 'return_only': 'active'}

    Attributes:
        return_only (Union[Unset, OptionsParameterReturnOnly]): If `active`, only active records will be returned. If
            `retired`, only retired records will be returned. Defaults to `active`. Default:
            OptionsParameterReturnOnly.ACTIVE.
        include_archived_projects (Union[Unset, bool]): If enabled, the response will include records that are connected
            to archived projects. Defaults to `false`. Default: False.
    """

    return_only: Union[Unset, OptionsParameterReturnOnly] = OptionsParameterReturnOnly.ACTIVE
    include_archived_projects: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return_only: Union[Unset, str] = UNSET
        if not isinstance(self.return_only, Unset):
            return_only = self.return_only.value

        include_archived_projects = self.include_archived_projects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if return_only is not UNSET:
            field_dict["return_only"] = return_only
        if include_archived_projects is not UNSET:
            field_dict["include_archived_projects"] = include_archived_projects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _return_only = d.pop("return_only", UNSET)
        return_only: Union[Unset, OptionsParameterReturnOnly]
        if isinstance(_return_only, Unset):
            return_only = UNSET
        else:
            return_only = OptionsParameterReturnOnly(_return_only)

        include_archived_projects = d.pop("include_archived_projects", UNSET)

        options_parameter = cls(
            return_only=return_only,
            include_archived_projects=include_archived_projects,
        )

        options_parameter.additional_properties = d
        return options_parameter

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
