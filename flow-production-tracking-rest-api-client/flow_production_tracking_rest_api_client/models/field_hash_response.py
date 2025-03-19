from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_hash_response_data_type_1 import FieldHashResponseDataType1
    from ..models.self_link import SelfLink


T = TypeVar("T", bound="FieldHashResponse")


@_attrs_define
class FieldHashResponse:
    """
    Example:
        {'data': {'url': 'https://sg-media-staging-
            usor-01.s3.amazonaws.com/1fe6dc157568e9ae589d66c109ace519dfee3699/f401cb001bdab191fdb6bbaa3d1a98f442a0fad6/08_a-
            team_001_ANIM_001.mov?AWSAccessKeyId=AKIAIZVDUP76QG4A6G3A&Expires=1524506637&Signature=Ylx%2BP3V7wYqNC6HtNv3crAU
            5HIM%3D&response-content-disposition=filename%3D%2208_a-team_001_ANIM_001.mov%22&x-amz-meta-user-id=85&x-amz-
            meta-user-type=HumanUser', 'name': '08_a-team_001_ANIM_001.mov', 'content_type': 'video/quicktime', 'link_type':
            'upload', 'type': 'Attachment', 'id': 111}, 'links': {'self':
            '/api/v1.1/entity/versions/6003/sg_uploaded_movie'}}

    Attributes:
        data (Union['FieldHashResponseDataType1', Unset, str]): URL to download an image or an attachment hash. Empty if
            the field is empty.
        links (Union[Unset, SelfLink]):
    """

    data: Union["FieldHashResponseDataType1", Unset, str] = UNSET
    links: Union[Unset, "SelfLink"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.field_hash_response_data_type_1 import FieldHashResponseDataType1

        data: Union[Unset, dict[str, Any], str]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, FieldHashResponseDataType1):
            data = self.data.to_dict()
        else:
            data = self.data

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
        from ..models.field_hash_response_data_type_1 import FieldHashResponseDataType1
        from ..models.self_link import SelfLink

        d = dict(src_dict)

        def _parse_data(data: object) -> Union["FieldHashResponseDataType1", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = FieldHashResponseDataType1.from_dict(data)

                return data_type_1
            except:  # noqa: E722
                pass
            return cast(Union["FieldHashResponseDataType1", Unset, str], data)

        data = _parse_data(d.pop("data", UNSET))

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfLink]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfLink.from_dict(_links)

        field_hash_response = cls(
            data=data,
            links=links,
        )

        field_hash_response.additional_properties = d
        return field_hash_response

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
