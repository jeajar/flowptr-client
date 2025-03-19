from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upload_info_response_data import UploadInfoResponseData
    from ..models.upload_info_response_links import UploadInfoResponseLinks


T = TypeVar("T", bound="UploadInfoResponse")


@_attrs_define
class UploadInfoResponse:
    """
    Example:
        {'data': {'timestamp': '2018-04-16T21:42:13Z', 'upload_type': 'Thumbnail', 'upload_id': None, 'storage_service':
            'sg', 'original_filename': 'logo.png', 'multipart_upload': False}, 'links': {'upload': 'https://yoursite.shotgun
            studio.com/api/v1.1/entity/projects/86/image/_upload?filename=logo.png&signature=OaHsK%2BrkZk5w1GxgxI3aNmJ0H3Y%3
            D&user_id=1&user_type=HumanUser&expiration=1532618412', 'complete_upload':
            '/api/v1.1/entity/projects/86/image/_upload'}}

    Attributes:
        data (Union[Unset, UploadInfoResponseData]):
        links (Union[Unset, UploadInfoResponseLinks]):
    """

    data: Union[Unset, "UploadInfoResponseData"] = UNSET
    links: Union[Unset, "UploadInfoResponseLinks"] = UNSET
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
        from ..models.upload_info_response_data import UploadInfoResponseData
        from ..models.upload_info_response_links import UploadInfoResponseLinks

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, UploadInfoResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = UploadInfoResponseData.from_dict(_data)

        _links = d.pop("links", UNSET)
        links: Union[Unset, UploadInfoResponseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = UploadInfoResponseLinks.from_dict(_links)

        upload_info_response = cls(
            data=data,
            links=links,
        )

        upload_info_response.additional_properties = d
        return upload_info_response

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
