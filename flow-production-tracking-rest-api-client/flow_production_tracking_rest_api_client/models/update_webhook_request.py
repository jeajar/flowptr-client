from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_webhook_request_entity_types import UpdateWebhookRequestEntityTypes


T = TypeVar("T", bound="UpdateWebhookRequest")


@_attrs_define
class UpdateWebhookRequest:
    """
    Example:
        {'url': 'http://sometargeturl.com', 'entity_types': {'Asset': {'create': [], 'update': ['code',
            'description']}}, 'projects': [1, 2], 'status': 'disabled', 'name': 'Asset Webhook', 'token': 'my_secret_token',
            'description': "Webhook for Asset creation and updates of 'code' and 'description'", 'validate_ssl_cert': True}

    Attributes:
        url (Union[Unset, str]): Webhook target url. This endpoint will be called when a delivery is available.
        entity_types (Union[Unset, UpdateWebhookRequestEntityTypes]): The filters for the webhook base on entity types
            and action. **Note that even though 'entity_types' is plural, only a single entity type is currently
            supported.**
        projects (Union[Unset, list[int]]): The ids of the project you want the webhook to apply to.
        token (Union[Unset, str]): Security token to use to sign the payload sent to the webhook.
        name (Union[Unset, str]): The name of the webhook.
        description (Union[Unset, str]): Description of the webhook.
        validate_ssl_cert (Union[Unset, bool]): If the request to the webhook endpoint should validate the SSL
            certificate.
        batch_deliveries (Union[Unset, bool]): Indicates if the webhook should deliver batches or single deliveries
        status (Union[Unset, str]): The status of the webhook, either 'active' or 'disabled'.
    """

    url: Union[Unset, str] = UNSET
    entity_types: Union[Unset, "UpdateWebhookRequestEntityTypes"] = UNSET
    projects: Union[Unset, list[int]] = UNSET
    token: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    validate_ssl_cert: Union[Unset, bool] = UNSET
    batch_deliveries: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        entity_types: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity_types, Unset):
            entity_types = self.entity_types.to_dict()

        projects: Union[Unset, list[int]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects

        token = self.token

        name = self.name

        description = self.description

        validate_ssl_cert = self.validate_ssl_cert

        batch_deliveries = self.batch_deliveries

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if entity_types is not UNSET:
            field_dict["entity_types"] = entity_types
        if projects is not UNSET:
            field_dict["projects"] = projects
        if token is not UNSET:
            field_dict["token"] = token
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if validate_ssl_cert is not UNSET:
            field_dict["validate_ssl_cert"] = validate_ssl_cert
        if batch_deliveries is not UNSET:
            field_dict["batch_deliveries"] = batch_deliveries
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_webhook_request_entity_types import UpdateWebhookRequestEntityTypes

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _entity_types = d.pop("entity_types", UNSET)
        entity_types: Union[Unset, UpdateWebhookRequestEntityTypes]
        if isinstance(_entity_types, Unset):
            entity_types = UNSET
        else:
            entity_types = UpdateWebhookRequestEntityTypes.from_dict(_entity_types)

        projects = cast(list[int], d.pop("projects", UNSET))

        token = d.pop("token", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        validate_ssl_cert = d.pop("validate_ssl_cert", UNSET)

        batch_deliveries = d.pop("batch_deliveries", UNSET)

        status = d.pop("status", UNSET)

        update_webhook_request = cls(
            url=url,
            entity_types=entity_types,
            projects=projects,
            token=token,
            name=name,
            description=description,
            validate_ssl_cert=validate_ssl_cert,
            batch_deliveries=batch_deliveries,
            status=status,
        )

        update_webhook_request.additional_properties = d
        return update_webhook_request

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
