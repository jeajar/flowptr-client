from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.next_upload_part_response_links import NextUploadPartResponseLinks


T = TypeVar("T", bound="NextUploadPartResponse")


@_attrs_define
class NextUploadPartResponse:
    """
    Example:
        {'links': {'upload': 'https://yoursite.shotgunstudio.com/api/v1.1/entity/versions/1/sg_uploaded_movie/_upload?fi
            lename=logo.png&signature=OaHsK%2BrkZk5w1GxgxI3aNmJ0H3Y%3D&user_id=1&user_type=HumanUser&expiration=1532618412',
            'get_next_part': '/api/v1.1/entity/versions/1/sg_uploaded_movie/_upload/multipart?filename=logo.png&part_number=
            2&timestamp=2019-04-16T21%3A23%3A36Z&upload_id=S.04OooF4_fxTPecfUd9XcifdgsduUH2.JEdk7vus4kswJj6l&upload_type=Att
            achment'}}

    Attributes:
        links (Union[Unset, NextUploadPartResponseLinks]):
    """

    links: Union[Unset, "NextUploadPartResponseLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.next_upload_part_response_links import NextUploadPartResponseLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: Union[Unset, NextUploadPartResponseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = NextUploadPartResponseLinks.from_dict(_links)

        next_upload_part_response = cls(
            links=links,
        )

        next_upload_part_response.additional_properties = d
        return next_upload_part_response

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
