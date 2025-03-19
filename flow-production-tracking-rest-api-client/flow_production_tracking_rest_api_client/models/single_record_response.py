from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record import Record
    from ..models.self_link import SelfLink


T = TypeVar("T", bound="SingleRecordResponse")


@_attrs_define
class SingleRecordResponse:
    """
    Example:
        {'data': {'type': 'Project', 'attributes': {'tank_name': None, 'end_date': None, 'duration': None,
            'tracking_settings': {'navchains': {'Asset': 'Asset.sg_asset_type', 'Shot': 'Shot.sg_sequence', 'Cut':
            'Cut.entity', 'CutItem': 'CutItem.cut.entity'}}, 'color': '129,183,255', 'client_site_settings_saved': False,
            'last_accessed_by_current_user': None, 'code': None, 'start_date': None, 'sg_status': None,
            'cached_display_name': 'Film Template', 'billboard': None, 'sg_description': None, 'filmstrip_image': None,
            'is_template': True, 'created_at': '2016-03-11T01:54:00Z', 'updated_at': '2018-02-28T22:46:35Z', 'sg_type':
            'Feature', 'image': None, 'landing_page_url': '/page/project_overview?project_id=82', 'archived': False,
            'is_demo': False, 'current_user_favorite': False, 'name': 'Film Template'}, 'relationships': {'users': {'data':
            [{'id': 19, 'name': 'Artist 1', 'type': 'HumanUser'}, {'id': 18, 'name': 'Artist 2', 'type': 'HumanUser'},
            {'id': 66, 'name': 'Manager 1', 'type': 'HumanUser'}], 'links': {'self':
            '/api/v1.1/entity/projects/82/relationships/users'}}, 'layout_project': {'data': {'id': 70, 'name': 'Demo:
            Animation', 'type': 'Project'}, 'links': {'self': '/api/v1.1/entity/projects/82/relationships/layout_project',
            'related': '/api/v1.1/entity/projects/70'}}, 'phases': {'data': [], 'links': {'self':
            '/api/v1.1/entity/projects/82/relationships/phases'}}, 'created_by': {'data': {'id': 24, 'name': 'Flow
            Production Tracking Support', 'type': 'HumanUser'}, 'links': {'self':
            '/api/v1.1/entity/projects/82/relationships/created_by', 'related': '/api/v1.1/entity/human_users/24'}},
            'updated_by': {'data': {'id': 24, 'name': 'Flow Production Tracking Support', 'type': 'HumanUser'}, 'links':
            {'self': '/api/v1.1/entity/projects/82/relationships/updated_by', 'related':
            '/api/v1.1/entity/human_users/24'}}, 'tags': {'data': [], 'links': {'self':
            '/api/v1.1/entity/projects/82/relationships/tags'}}, 'task_templates': {'data': [], 'links': {'self':
            '/api/v1.1/entity/projects/82/relationships/task_templates'}}}, 'id': 82, 'links': {'self':
            '/api/v1.1/entity/projects/82'}}, 'links': {'self': '/api/v1.1/entity/projects/82'}}

    Attributes:
        data (Union[Unset, Record]):
        links (Union[Unset, SelfLink]):
    """

    data: Union[Unset, "Record"] = UNSET
    links: Union[Unset, "SelfLink"] = UNSET
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
        from ..models.record import Record
        from ..models.self_link import SelfLink

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, Record]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = Record.from_dict(_data)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfLink]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfLink.from_dict(_links)

        single_record_response = cls(
            data=data,
            links=links,
        )

        single_record_response.additional_properties = d
        return single_record_response

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
