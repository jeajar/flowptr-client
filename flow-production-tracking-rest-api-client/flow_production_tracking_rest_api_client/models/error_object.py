from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_object_source import ErrorObjectSource


T = TypeVar("T", bound="ErrorObject")


@_attrs_define
class ErrorObject:
    """
    Attributes:
        id (Union[Unset, str]): A unique identifier for this particular occurrence of the problem. Example:
            a4c9279479129dcd4413145f1fcdbd78.
        status (Union[Unset, int]): HTTP status code. Example: 400.
        code (Union[Unset, int]): Flow Production Tracking defined error codes. Example: 103.
        title (Union[Unset, str]): A short, human-readable summary of the problem. Example: Request Parameters invalid..
        detail (Union[Unset, str]): A human-readable explanation specific to this occurrence of the problem.
        source (Union[Unset, ErrorObjectSource]): An object containing references to the source of the error. Example:
            {'entity': ['entity is not valid']}.
        meta (Union[Unset, str]): Non-standard meta-information about the error. Example: {'crud_error_uuid':
            '91602614-1dae-11e8-8f3d-0242ac190005'}.
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    code: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    source: Union[Unset, "ErrorObjectSource"] = UNSET
    meta: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        code = self.code

        title = self.title

        detail = self.detail

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if title is not UNSET:
            field_dict["title"] = title
        if detail is not UNSET:
            field_dict["detail"] = detail
        if source is not UNSET:
            field_dict["source"] = source
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_object_source import ErrorObjectSource

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        code = d.pop("code", UNSET)

        title = d.pop("title", UNSET)

        detail = d.pop("detail", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ErrorObjectSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ErrorObjectSource.from_dict(_source)

        meta = d.pop("meta", UNSET)

        error_object = cls(
            id=id,
            status=status,
            code=code,
            title=title,
            detail=detail,
            source=source,
            meta=meta,
        )

        error_object.additional_properties = d
        return error_object

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
