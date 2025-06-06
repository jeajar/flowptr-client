from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Union


@dataclass
class FilterCondition:
    """Basic filter condition following Flow PTR specs."""

    field: str
    relation: str
    value: Any


@dataclass
class ComplexFilter:
    """Complex filter following Flow PTR specs."""

    logical_operator: str  # "and" or "or"
    conditions: Sequence[Union["ComplexFilter", FilterCondition]]
