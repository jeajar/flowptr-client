from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentMetadata")


@_attrs_define
class AttachmentMetadata:
    """
    Example:
        {'width': 1920, 'height': 1080, 'display_aspect_ratio': 1.7778, 'frame_rate': 24.0, 'nb_frames': 1440,
            'start_frame': 0}

    Attributes:
        width (Union[Unset, int]): Width of the transcoded video in pixels.
        height (Union[Unset, int]): Height of the transcoded video in pixels.
        display_aspect_ratio (Union[Unset, float]): Display aspect ratio of the transcoded video.
        frame_rate (Union[Unset, float]): Frame rate of the transcoded video in frames per second.
        nb_frames (Union[Unset, int]): Duration of the transcoded video in number of video frames
        start_frame (Union[Unset, int]): Start of the transcoded video in of video frames
    """

    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    display_aspect_ratio: Union[Unset, float] = UNSET
    frame_rate: Union[Unset, float] = UNSET
    nb_frames: Union[Unset, int] = UNSET
    start_frame: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        display_aspect_ratio = self.display_aspect_ratio

        frame_rate = self.frame_rate

        nb_frames = self.nb_frames

        start_frame = self.start_frame

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if display_aspect_ratio is not UNSET:
            field_dict["display_aspect_ratio"] = display_aspect_ratio
        if frame_rate is not UNSET:
            field_dict["frame_rate"] = frame_rate
        if nb_frames is not UNSET:
            field_dict["nb_frames"] = nb_frames
        if start_frame is not UNSET:
            field_dict["start_frame"] = start_frame

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        display_aspect_ratio = d.pop("display_aspect_ratio", UNSET)

        frame_rate = d.pop("frame_rate", UNSET)

        nb_frames = d.pop("nb_frames", UNSET)

        start_frame = d.pop("start_frame", UNSET)

        attachment_metadata = cls(
            width=width,
            height=height,
            display_aspect_ratio=display_aspect_ratio,
            frame_rate=frame_rate,
            nb_frames=nb_frames,
            start_frame=start_frame,
        )

        attachment_metadata.additional_properties = d
        return attachment_metadata

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
