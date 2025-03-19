from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upload_response_data import UploadResponseData
    from ..models.upload_response_links import UploadResponseLinks


T = TypeVar("T", bound="UploadResponse")


@_attrs_define
class UploadResponse:
    """
    Example:
        {'data': {'upload_id': '2a36e9b8-419f-11e8-ac9f-0242ac190005', 'original_filename': 'logo.png'}, 'links':
            {'complete_upload': '/api/v1.1/entity/projects/86/image/_upload'}}

    Attributes:
        data (Union[Unset, UploadResponseData]):
        links (Union[Unset, UploadResponseLinks]):
    """

    data: Union[Unset, "UploadResponseData"] = UNSET
    links: Union[Unset, "UploadResponseLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
        from ..models.upload_response_data import UploadResponseData
        from ..models.upload_response_links import UploadResponseLinks

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, UploadResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = UploadResponseData.from_dict(_data)

        _links = d.pop("links", UNSET)
        links: Union[Unset, UploadResponseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = UploadResponseLinks.from_dict(_links)

        upload_response = cls(
            data=data,
            links=links,
        )

        upload_response.additional_properties = d
        return upload_response

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
