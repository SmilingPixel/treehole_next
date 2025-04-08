from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DivisionModifyDivisionModel")


@_attrs_define
class DivisionModifyDivisionModel:
    """
    Attributes:
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        pinned (Union[Unset, list[int]]):
    """

    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    pinned: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        pinned: Union[Unset, list[int]] = UNSET
        if not isinstance(self.pinned, Unset):
            pinned = self.pinned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if pinned is not UNSET:
            field_dict["pinned"] = pinned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        pinned = cast(list[int], d.pop("pinned", UNSET))

        division_modify_division_model = cls(
            description=description,
            name=name,
            pinned=pinned,
        )

        division_modify_division_model.additional_properties = d
        return division_modify_division_model

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
