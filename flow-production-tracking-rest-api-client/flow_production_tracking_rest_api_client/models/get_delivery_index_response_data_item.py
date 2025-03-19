from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_delivery_index_response_data_item_status import GetDeliveryIndexResponseDataItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_delivery_index_response_data_item_request_body import GetDeliveryIndexResponseDataItemRequestBody
    from ..models.get_delivery_index_response_data_item_request_headers import (
        GetDeliveryIndexResponseDataItemRequestHeaders,
    )
    from ..models.get_delivery_index_response_data_item_response_headers import (
        GetDeliveryIndexResponseDataItemResponseHeaders,
    )


T = TypeVar("T", bound="GetDeliveryIndexResponseDataItem")


@_attrs_define
class GetDeliveryIndexResponseDataItem:
    """
    Attributes:
        id (Union[Unset, str]): GUID based id of the delivery.
        request_body (Union[Unset, GetDeliveryIndexResponseDataItemRequestBody]): The full request body that was sent to
            the hook.
        event_time (Union[Unset, int]): The time when delivery was sent.
        status (Union[Unset, GetDeliveryIndexResponseDataItemStatus]): Status of the delivery. `delivered` or `failed`
        process_time (Union[Unset, int]): The time it took for the hook to respond.
        body (Union[Unset, str]): Response body from the hook.
        response_code (Union[Unset, int]): HTTP response code.
        acknowledgement (Union[Unset, str]): An updatable value for services to indicate if they have processed the
            delivery.
        request_headers (Union[Unset, GetDeliveryIndexResponseDataItemRequestHeaders]): Headers sent to the webhook
            endpoint.
        response_headers (Union[Unset, GetDeliveryIndexResponseDataItemResponseHeaders]): Headers returned by the
            webhook endpoint.
    """

    id: Union[Unset, str] = UNSET
    request_body: Union[Unset, "GetDeliveryIndexResponseDataItemRequestBody"] = UNSET
    event_time: Union[Unset, int] = UNSET
    status: Union[Unset, GetDeliveryIndexResponseDataItemStatus] = UNSET
    process_time: Union[Unset, int] = UNSET
    body: Union[Unset, str] = UNSET
    response_code: Union[Unset, int] = UNSET
    acknowledgement: Union[Unset, str] = UNSET
    request_headers: Union[Unset, "GetDeliveryIndexResponseDataItemRequestHeaders"] = UNSET
    response_headers: Union[Unset, "GetDeliveryIndexResponseDataItemResponseHeaders"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        request_body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.request_body, Unset):
            request_body = self.request_body.to_dict()

        event_time = self.event_time

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        process_time = self.process_time

        body = self.body

        response_code = self.response_code

        acknowledgement = self.acknowledgement

        request_headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.request_headers, Unset):
            request_headers = self.request_headers.to_dict()

        response_headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.response_headers, Unset):
            response_headers = self.response_headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if request_body is not UNSET:
            field_dict["request_body"] = request_body
        if event_time is not UNSET:
            field_dict["event_time"] = event_time
        if status is not UNSET:
            field_dict["status"] = status
        if process_time is not UNSET:
            field_dict["process_time"] = process_time
        if body is not UNSET:
            field_dict["body"] = body
        if response_code is not UNSET:
            field_dict["response_code"] = response_code
        if acknowledgement is not UNSET:
            field_dict["acknowledgement"] = acknowledgement
        if request_headers is not UNSET:
            field_dict["request_headers"] = request_headers
        if response_headers is not UNSET:
            field_dict["response_headers"] = response_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_delivery_index_response_data_item_request_body import (
            GetDeliveryIndexResponseDataItemRequestBody,
        )
        from ..models.get_delivery_index_response_data_item_request_headers import (
            GetDeliveryIndexResponseDataItemRequestHeaders,
        )
        from ..models.get_delivery_index_response_data_item_response_headers import (
            GetDeliveryIndexResponseDataItemResponseHeaders,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _request_body = d.pop("request_body", UNSET)
        request_body: Union[Unset, GetDeliveryIndexResponseDataItemRequestBody]
        if isinstance(_request_body, Unset):
            request_body = UNSET
        else:
            request_body = GetDeliveryIndexResponseDataItemRequestBody.from_dict(_request_body)

        event_time = d.pop("event_time", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, GetDeliveryIndexResponseDataItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetDeliveryIndexResponseDataItemStatus(_status)

        process_time = d.pop("process_time", UNSET)

        body = d.pop("body", UNSET)

        response_code = d.pop("response_code", UNSET)

        acknowledgement = d.pop("acknowledgement", UNSET)

        _request_headers = d.pop("request_headers", UNSET)
        request_headers: Union[Unset, GetDeliveryIndexResponseDataItemRequestHeaders]
        if isinstance(_request_headers, Unset):
            request_headers = UNSET
        else:
            request_headers = GetDeliveryIndexResponseDataItemRequestHeaders.from_dict(_request_headers)

        _response_headers = d.pop("response_headers", UNSET)
        response_headers: Union[Unset, GetDeliveryIndexResponseDataItemResponseHeaders]
        if isinstance(_response_headers, Unset):
            response_headers = UNSET
        else:
            response_headers = GetDeliveryIndexResponseDataItemResponseHeaders.from_dict(_response_headers)

        get_delivery_index_response_data_item = cls(
            id=id,
            request_body=request_body,
            event_time=event_time,
            status=status,
            process_time=process_time,
            body=body,
            response_code=response_code,
            acknowledgement=acknowledgement,
            request_headers=request_headers,
            response_headers=response_headers,
        )

        get_delivery_index_response_data_item.additional_properties = d
        return get_delivery_index_response_data_item

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
