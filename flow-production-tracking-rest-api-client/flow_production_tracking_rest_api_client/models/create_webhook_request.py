from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_webhook_request_entity_types import CreateWebhookRequestEntityTypes


T = TypeVar("T", bound="CreateWebhookRequest")


@_attrs_define
class CreateWebhookRequest:
    """
    Example:
        {'url': 'http://sometargeturl.com', 'entity_types': {'Asset': {'create': [], 'update': ['code',
            'description']}}, 'token': 'some_token_to_sign_payload', 'projects': [1, 2], 'name': 'Asset Webhook',
            'description': "Webhook for Asset creation and updates of 'code' and 'description'", 'validate_ssl_cert': True}

    Attributes:
        url (str): Webhook target url. This endpoint will be called when a delivery is available.
        entity_types (CreateWebhookRequestEntityTypes): The filters for the webhook base on entity types and action.
            **Note that even though 'entity_types' is plural, only a single entity type is currently supported.**
        token (Union[Unset, str]): Security token to use to sign the payload sent to the webhook.
        projects (Union[Unset, list[int]]): The ids of the project you want the webhook to apply to.
        name (Union[Unset, str]): The name of the webhook.
        description (Union[Unset, str]): Description of the webhook.
        validate_ssl_cert (Union[Unset, bool]): If the request to the webhook endpoint should validate the SSL
            certificate.
        batch_deliveries (Union[Unset, bool]): Indicates if the webhook should deliver batches or single deliveries
    """

    url: str
    entity_types: "CreateWebhookRequestEntityTypes"
    token: Union[Unset, str] = UNSET
    projects: Union[Unset, list[int]] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    validate_ssl_cert: Union[Unset, bool] = UNSET
    batch_deliveries: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        entity_types = self.entity_types.to_dict()

        token = self.token

        projects: Union[Unset, list[int]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects

        name = self.name

        description = self.description

        validate_ssl_cert = self.validate_ssl_cert

        batch_deliveries = self.batch_deliveries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "entity_types": entity_types,
            }
        )
        if token is not UNSET:
            field_dict["token"] = token
        if projects is not UNSET:
            field_dict["projects"] = projects
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if validate_ssl_cert is not UNSET:
            field_dict["validate_ssl_cert"] = validate_ssl_cert
        if batch_deliveries is not UNSET:
            field_dict["batch_deliveries"] = batch_deliveries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_webhook_request_entity_types import CreateWebhookRequestEntityTypes

        d = dict(src_dict)
        url = d.pop("url")

        entity_types = CreateWebhookRequestEntityTypes.from_dict(d.pop("entity_types"))

        token = d.pop("token", UNSET)

        projects = cast(list[int], d.pop("projects", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        validate_ssl_cert = d.pop("validate_ssl_cert", UNSET)

        batch_deliveries = d.pop("batch_deliveries", UNSET)

        create_webhook_request = cls(
            url=url,
            entity_types=entity_types,
            token=token,
            projects=projects,
            name=name,
            description=description,
            validate_ssl_cert=validate_ssl_cert,
            batch_deliveries=batch_deliveries,
        )

        create_webhook_request.additional_properties = d
        return create_webhook_request

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
