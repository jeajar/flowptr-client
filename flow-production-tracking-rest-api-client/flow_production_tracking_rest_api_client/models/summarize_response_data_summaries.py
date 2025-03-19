from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.summarize_response_data_summaries_additional_property_type_3 import (
        SummarizeResponseDataSummariesAdditionalPropertyType3,
    )


T = TypeVar("T", bound="SummarizeResponseDataSummaries")


@_attrs_define
class SummarizeResponseDataSummaries:
    """The total summary for the query."""

    additional_properties: dict[str, Union["SummarizeResponseDataSummariesAdditionalPropertyType3", bool, int, str]] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.summarize_response_data_summaries_additional_property_type_3 import (
            SummarizeResponseDataSummariesAdditionalPropertyType3,
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, SummarizeResponseDataSummariesAdditionalPropertyType3):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.summarize_response_data_summaries_additional_property_type_3 import (
            SummarizeResponseDataSummariesAdditionalPropertyType3,
        )

        d = dict(src_dict)
        summarize_response_data_summaries = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union["SummarizeResponseDataSummariesAdditionalPropertyType3", bool, int, str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_3 = SummarizeResponseDataSummariesAdditionalPropertyType3.from_dict(data)

                    return additional_property_type_3
                except:  # noqa: E722
                    pass
                return cast(Union["SummarizeResponseDataSummariesAdditionalPropertyType3", bool, int, str], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        summarize_response_data_summaries.additional_properties = additional_properties
        return summarize_response_data_summaries

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union["SummarizeResponseDataSummariesAdditionalPropertyType3", bool, int, str]:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: Union["SummarizeResponseDataSummariesAdditionalPropertyType3", bool, int, str]
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
